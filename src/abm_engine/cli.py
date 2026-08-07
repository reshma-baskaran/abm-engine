from __future__ import annotations

import argparse
import json
from pathlib import Path

from .library import SignalLibrary
from .workflow import build_message_brief, load_json, run_account, score_evidence_payload, validate_evidence


DEFAULT_LIBRARY = Path(__file__).resolve().parents[2] / "data" / "signal-library.md"
PORTABLE_LIBRARY = Path(__file__).resolve().parents[2] / "data" / "industry-agnostic-signals.json"


def load_library(pack: str, override: Path | None) -> SignalLibrary:
    if override is not None:
        return SignalLibrary.from_json(override) if override.suffix.casefold() == ".json" else SignalLibrary.from_markdown(override)
    if pack == "legacy":
        return SignalLibrary.from_markdown(DEFAULT_LIBRARY)
    return SignalLibrary.from_json(PORTABLE_LIBRARY)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="abm-engine", description="Build source-backed ABM research inputs.")
    parser.add_argument("--pack", choices=("portable", "legacy"), default="portable")
    parser.add_argument("--library", type=Path, help="override the selected signal pack with a Markdown or JSON library")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("stats", help="Show library coverage.")

    search = commands.add_parser("search", help="Search signal definitions.")
    search.add_argument("text", nargs="?", default="")
    search.add_argument("--industry", default="")
    search.add_argument("--category", default="")
    search.add_argument("--limit", type=int, default=20)

    render = commands.add_parser("render", help="Render the query template for a signal key.")
    render.add_argument("key")
    render.add_argument("--company-name", required=True)
    render.add_argument("--company-domain", default="")
    render.add_argument("--ticker", default="")

    account = commands.add_parser("account-run", help="Create a fail-closed account research workspace.")
    account.add_argument("--brief", type=Path, required=True)
    account.add_argument("--company-name", required=True)
    account.add_argument("--company-domain", required=True)
    account.add_argument("--industry", required=True)
    account.add_argument("--out", type=Path, required=True)
    account.add_argument("--limit", type=int, default=8)

    evidence_validate = commands.add_parser("evidence-validate", help="Validate source-backed evidence and approval state.")
    evidence_validate.add_argument("path", type=Path)

    evidence_score = commands.add_parser("evidence-score", help="Score approved evidence only.")
    evidence_score.add_argument("path", type=Path)

    brief_build = commands.add_parser("brief-build", help="Build a human-review message brief from approved evidence.")
    brief_build.add_argument("--brief", type=Path, required=True)
    brief_build.add_argument("--evidence", type=Path, required=True)
    brief_build.add_argument("--out", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    library = load_library(args.pack, args.library)

    if args.command == "stats":
        print(json.dumps(library.stats(), indent=2))
        return 0

    if args.command == "search":
        results = library.search(args.text, industry=args.industry, category=args.category)[: args.limit]
        print(json.dumps([item.to_dict() for item in results], indent=2))
        return 0

    if args.command == "account-run":
        result = run_account(
            library=library,
            brief=load_json(args.brief),
            company_name=args.company_name,
            domain=args.company_domain,
            industry=args.industry,
            output_dir=args.out,
            limit=args.limit,
        )
        print(json.dumps(result.to_dict(), indent=2))
        return 2 if result.status == "needs_input" else 0

    if args.command in {"evidence-validate", "evidence-score"}:
        payload = load_json(args.path)
        errors = validate_evidence(payload, library)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        if args.command == "evidence-validate":
            print("Evidence is structurally valid and includes review state. Claim accuracy still requires human review.")
        else:
            print(json.dumps(score_evidence_payload(payload, library), indent=2))
        return 0

    if args.command == "brief-build":
        try:
            rendered = build_message_brief(
                brief=load_json(args.brief),
                evidence=load_json(args.evidence),
                library=library,
            )
        except ValueError as error:
            print(f"ERROR: {error}")
            return 1
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
        print(f"Message brief ready for human review: {args.out}")
        return 0

    matches = library.by_key(args.key)
    if not matches:
        raise SystemExit(f"Unknown signal key: {args.key}")
    payload = []
    for signal in matches:
        query = signal.render_query(
            company_name=args.company_name,
            company_domain=args.company_domain,
            ticker=args.ticker,
        )
        if not query:
            raise SystemExit(f"Signal has no executable query template: {signal.scoped_key}")
        payload.append(
            {
                "scoped_key": signal.scoped_key,
                "query": query,
            }
        )
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

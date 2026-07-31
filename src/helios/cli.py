from __future__ import annotations

import argparse
import json
from pathlib import Path

from .library import SignalLibrary


DEFAULT_LIBRARY = Path(__file__).resolve().parents[2] / "data" / "signal-library.md"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="helios", description="Inspect and render the Helios signal library.")
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
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
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    library = SignalLibrary.from_markdown(args.library)

    if args.command == "stats":
        print(json.dumps(library.stats(), indent=2))
        return 0

    if args.command == "search":
        results = library.search(args.text, industry=args.industry, category=args.category)[: args.limit]
        print(json.dumps([item.to_dict() for item in results], indent=2))
        return 0

    matches = library.by_key(args.key)
    if not matches:
        raise SystemExit(f"Unknown signal key: {args.key}")
    payload = []
    for signal in matches:
        payload.append(
            {
                "scoped_key": signal.scoped_key,
                "query": signal.render_query(
                    company_name=args.company_name,
                    company_domain=args.company_domain,
                    ticker=args.ticker,
                ),
            }
        )
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


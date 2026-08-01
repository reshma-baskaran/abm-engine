# ABM Engine: Your Replacement for Clay

![ABM Engine cover](assets/cover.svg)

ABM Engine is an evidence-first account research and messaging starter kit. It
turns a campaign brief into scoped research questions, source-backed buying
signals, a reviewable account score, and grounded message inputs.

The repository is designed to run locally from a fork. It is a research layer,
not a hosted enrichment or campaign platform.

## The problem

Most enrichment workflows produce rows of data. ABM teams still have to decide which facts matter, whether a source supports the claim, what the timing signal means, and how it should change the message.

ABM Engine encodes that judgment in an inspectable workflow:

1. Select relevant signals for the account and campaign.
2. Render targeted research queries.
3. Attach a source and concrete evidence.
4. Normalize confidence and apply signal weight.
5. Require human approval.
6. Rank approved evidence for the message brief.

## What is included

- A [quickstart](QUICKSTART.md), local configuration example, and workspace initializer.
- **866 signal definitions** and **858 unique signal keys** across retail and financial-services markets.
- A zero-dependency Python parser and CLI.
- Scoped keys for signal names reused across markets.
- Query-template rendering.
- Evidence-gated scoring.
- Blank research-record, evidence-record, and message-brief templates.
- Three real, first-party-sourced account research records.
- Tests that lock the verified library counts and scoring boundaries.

## What a fork gives you

After setup, a fork gives you a local research workspace, the signal library,
query rendering, evidence-record templates, and a reviewable path from signal
to message brief. Add your own account inputs and public sources; do not commit
private contact data, CRM records, credentials, or campaign state.

The signal library contains research hypotheses, not proof of buying intent. A
source-backed observation still needs a human review before it informs outbound.

## Quick start

See [QUICKSTART.md](QUICKSTART.md) for the full setup. The short version:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .

abm-engine stats
abm-engine search "AI initiative" --limit 5
abm-engine render ai_initiative_press_release --company-name "Lowe's" --company-domain lowes.com --ticker LOW
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## How this differs from Clay

Clay is a general enrichment and workflow canvas. ABM Engine is an opinionated ABM research system: the signal taxonomy, evidence record, confidence treatment, human approval boundary, and message-grounding workflow are built into the model. The goal is not to reproduce every Clay integration; it is to make account-level research logic visible and auditable.

## Real account cases

The [case records](cases/README.md) use Lowe's, Klarna, and Bank of America to show how public evidence is recorded and how confirmed observations are separated from interpretation. They do not claim a customer relationship or active opportunity.

## Architecture

See [docs/architecture.md](docs/architecture.md).

## Current status

The signal library and research workflow were extracted from an operating ABM
platform and rebuilt as a standalone public engine. This release focuses on
the research layer and is packaged as a local starter kit. Vendor integrations,
contact enrichment, and campaign execution are intentionally excluded so the
repository can be run and inspected without credentials.

## Author

Built by **Reshma Baskaran**, a GTM and growth marketer building practical research, outbound, and knowledge systems.

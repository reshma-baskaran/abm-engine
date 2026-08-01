# Quickstart

ABM Engine is a local, evidence-first research tool. It helps you select
buying-signal hypotheses, render research queries, record sourced observations,
and prepare a reviewable message brief. It does not enrich contacts, send
campaigns, or connect to a vendor account.

## 1. Clone and install

```bash
git clone https://github.com/reshma-baskaran/abm-engine.git
cd abm-engine
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

If your environment cannot install Python build dependencies, run the CLI
directly from the checkout instead:

```bash
PYTHONPATH=src python -m abm_engine.cli stats
```

## 2. Create a local workspace

Copy the configuration example and change `workspace_path` to a location
outside this public repository:

```bash
cp abm-engine.config.example.json abm-engine.config.json
python3 scripts/init_workspace.py --config abm-engine.config.json
```

The local configuration file is ignored by Git. The initializer creates a
blank research workspace and does not overwrite existing files unless
`--overwrite` is explicitly supplied.

## 3. Inspect the library

```bash
abm-engine stats
abm-engine search "AI initiative" --limit 5
abm-engine render ai_initiative_press_release \
  --company-name "YOUR_COMPANY_NAME"
```

Treat every returned signal as a research hypothesis. A signal definition is
not evidence of buying intent.

## 4. Record evidence and prepare a brief

Use the blank files copied into the workspace's `templates/` directory:

- `research-record.md` for the account research map
- `evidence-record.json` for source-backed observations
- `message-brief.md` for approved message inputs

For every observation, preserve the source URL, access date, concrete evidence,
confidence, and the boundary between confirmed fact and interpretation. Review
the record before it informs any outbound work.

## 5. Run the tests

```bash
python -m unittest discover -s tests -v
```

## What this does not do

The public repository does not include credentials, contact enrichment, CRM
records, sending-platform state, private account history, or campaign launch
logic. Confirm that you are permitted to use and redistribute the signal
library before building on or republishing it.

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
python -m pip install --upgrade pip
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
abm-engine search "product launch" --limit 5
abm-engine render public_product_launch \
  --company-name "YOUR_COMPANY_NAME"
```

The CLI defaults to the 21-signal industry-agnostic pack. Inspect the original
866 retail and financial-services definitions with `abm-engine --pack legacy stats`.
Do not apply their sector weights to another industry.

Treat every returned signal as a research hypothesis. A signal definition is
not evidence of buying intent.

## 4. Run an account intake

Complete `templates/campaign-brief.json`, then run:

```bash
abm-engine account-run \
  --brief templates/campaign-brief.json \
  --company-name "YOUR_COMPANY_NAME" \
  --company-domain example.com \
  --industry "YOUR INDUSTRY" \
  --out /path/outside/the/repository/account-name
```

If seller, offer, buyer, proof, objective, desired action, operating problem,
or consequence is missing, the command exits with `needs_input` and creates no
message brief. With complete inputs it advances only to `needs_research`.

## 5. Record and validate evidence

Use the blank files copied into the workspace's `templates/` directory:

- `research-record.md` for the account research map
- `evidence-record.json` for source-backed observations
- `message-brief.md` for approved message inputs

Validate and score an account evidence record:

```bash
abm-engine evidence-validate /path/to/evidence.json
abm-engine evidence-score /path/to/evidence.json
abm-engine brief-build \
  --brief /path/to/campaign-brief.json \
  --evidence /path/to/evidence.json \
  --out /path/to/message-brief.md
```

Only evidence marked `approved` contributes to the prioritization score or the
generated message brief. That score is not purchase probability or proof of
buying intent. A built brief is ready for human review, not permission to send.

For every observation, preserve the source URL, access date, concrete evidence,
confidence, and the boundary between confirmed fact and interpretation. Review
the record before it informs any outbound work.

## 6. Run the tests

```bash
python -m unittest discover -s tests -v
```

## What this does not do

The public repository does not include credentials, contact enrichment, CRM
records, sending-platform state, private account history, or campaign launch
logic. Confirm that you are permitted to use and redistribute the signal
library before building on or republishing it.

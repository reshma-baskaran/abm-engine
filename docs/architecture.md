# Architecture

```mermaid
flowchart LR
  A[Account and campaign brief] --> B[Signal selection]
  B --> C[Rendered research queries]
  C --> D[Source collection]
  D --> E[Evidence extraction]
  E --> F[Confidence and weight scoring]
  F --> G[Human approval]
  G --> H[Ranked message brief]
  H --> I[Personalized sequence]
```

The engine treats a signal as a research hypothesis until a source URL and concrete evidence are attached. A high library weight does not turn an unsupported claim into evidence. Human approval remains the boundary between research and outbound use.

## Data model

- `Signal`: a scoped research definition containing a key, label, category, optional weight, optional confidence, and optional query template.
- `Evidence`: a source-backed observation attached to a signal.
- `scoped_key`: `industry::sub-industry::key`; this preserves intentionally repeated keys across different markets.

## Why the engine is inspectable

The library is plain Markdown. The parser and scorer use the Python standard library. Every score can be traced back to a signal definition, evidence string, source URL, weight, and confidence value.


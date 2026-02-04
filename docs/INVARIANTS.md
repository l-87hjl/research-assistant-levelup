# System Invariants

These invariants must hold regardless of capability level.

## Research Mode (Role A)
- ResearchAgent must not return executable code blocks
- ResearchAgent must not return synthesized implementations
- ResearchAgent may return empty provenance when evidence is insufficient
- ResearchAgent must explicitly state uncertainty or insufficiency

## Synthesis Mode (Role B)
- SynthesisAgent must not accept raw external excerpts
- SynthesisAgent must not inspect ProvenanceRecord internals beyond citation
- SynthesisAgent must fail on invalid provenance inputs

## Orchestration
- Synthesis may only occur after Research
- Mode transitions must be explicit and centralized

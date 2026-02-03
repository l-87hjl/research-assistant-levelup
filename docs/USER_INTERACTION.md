# User Interaction Model

This document proposes how a user interacts with this repository and its agents.

## Model A: Notebook / Script User (Recommended)
- User writes a script or notebook
- Explicitly instantiates agents
- Explicitly switches modes via orchestrator

Flow:
1. User defines problem
2. User invokes ResearchAgent via orchestrator
3. User reviews summaries + provenance
4. User decides whether to proceed
5. User invokes SynthesisAgent with design notes

Benefits:
- Maximum transparency
- User remains decision-maker
- Easy to audit and test

---

## Model B: CLI-Driven Workflow
- User runs commands like:
  - `research analyze "problem"`
  - `research synthesize design_notes.md`

Characteristics:
- Still explicit mode separation
- Good for automation
- Slightly higher abstraction

---

## Model C: Service / API (Deferred)
- HTTP endpoints for research and synthesis
- Requires Governor enforcement
- Not recommended until later phase

---

## Non-Goals
- Fully autonomous agent loops
- Silent research → synthesis transitions
- One-click production code generation

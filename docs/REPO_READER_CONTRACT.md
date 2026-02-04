# Repo Reader Contract

This document defines the contract for a **controlled repository-reading capability** used by the Research Agent (Role A).

The Repo Reader is a *capability service*, not an agent. It performs constrained retrieval and returns research artifacts only.

---

## Design Principles

- **Separation of Power and Policy**
  - This repository defines policy, roles, and invariants
  - The Repo Reader provides read-only capability

- **No Raw Access**
  - Research agents never read repositories directly
  - All access is mediated through this contract

- **Artifact-Oriented, Not File-Oriented**
  - The Repo Reader returns excerpts + metadata, not files

---

## Allowed Callers

- ResearchAgent (Role A) only
- Access must be routed through the Orchestrator

SynthesisAgent (Role B) must never invoke the Repo Reader.

---

## Inputs

A Repo Reader request may include:

- `query`: natural-language research question
- `repo_constraints`:
  - allowlist / denylist
  - max number of repositories
- `file_constraints`:
  - allowed file extensions
  - max excerpt length
- `license_constraints`:
  - allowed licenses only

The Repo Reader may reject overly broad or underspecified requests.

---

## Outputs

The Repo Reader returns a list of **Research Artifacts**, each containing:

- `excerpt` (plain text, truncated)
- `repo` (owner/name)
- `commit` (hash or tag)
- `path` (file path)
- `license`
- `excerpt_span` (line or byte range)

The ResearchAgent is responsible for converting these into `ProvenanceRecord` instances.

---

## Hard Constraints (Must Enforce)

- No bulk repository dumps
- No binary files
- No executable evaluation
- No excerpts larger than configured limits
- Mandatory license detection

---

## Failure Modes

The Repo Reader must fail explicitly when:

- License information is unavailable
- Requested scope exceeds limits
- Repository access is ambiguous

Failures should return structured errors, not partial results.

---

## Non-Goals

- Semantic interpretation of code
- Cross-repository synthesis
- Any autonomous decision-making

The Repo Reader is a librarian, not a researcher.

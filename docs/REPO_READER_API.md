# Repo Reader API Surface

This document defines the **request and response objects** for the Repo Reader service.

The Repo Reader is a *capability service*, not an agent. It accepts constrained research requests and returns bounded research artifacts.

---

## Design Goals

- Explicit, auditable inputs and outputs
- No raw file or repository access
- Bounded scope and size
- Clear failure semantics
- Easy to mock for testing

---

## Request Object: `RepoReaderRequest`

A request represents *intent to research*, not intent to retrieve files.

### Fields

- `query` (string, required)
  - Natural-language description of what is being researched

- `repo_constraints` (object, optional)
  - `allowlist`: list of repo identifiers (owner/name)
  - `denylist`: list of repo identifiers
  - `max_repos`: integer limit

- `file_constraints` (object, optional)
  - `allowed_extensions`: list of file extensions (e.g. `.py`, `.md`)
  - `max_excerpt_chars`: maximum characters per excerpt
  - `max_excerpts_per_repo`: integer limit

- `license_constraints` (object, optional)
  - `allowed_licenses`: list of SPDX identifiers
  - `require_license`: boolean (default: true)

- `result_limits` (object, optional)
  - `max_total_excerpts`: integer

### Validation Rules

- Requests must be fully specified or will be rejected
- Overly broad requests must fail explicitly
- Defaults should be conservative

---

## Response Object: `RepoReaderResponse`

A response contains **research artifacts**, not files or repos.

### Fields

- `artifacts` (list of ResearchArtifact)
- `errors` (list of RepoReaderError, optional)

If `errors` is present, `artifacts` may be empty.

---

## Research Artifact Object: `ResearchArtifact`

Each artifact represents a bounded, attributable excerpt.

### Fields

- `excerpt` (string)
  - Plain text only, truncated

- `repo` (string)
  - Repository identifier (owner/name)

- `commit` (string)
  - Commit hash or tag

- `path` (string)
  - File path within repository

- `license` (string)
  - Detected license identifier

- `excerpt_span` (string)
  - Line or byte range descriptor

---

## Error Object: `RepoReaderError`

Errors are **structured and explicit**.

### Fields

- `code` (string)
  - Machine-readable error code

- `message` (string)
  - Human-readable explanation

- `details` (object, optional)
  - Additional context

---

## Hard Guarantees

The Repo Reader MUST guarantee:

- No raw file contents beyond excerpts
- No excerpts exceeding configured limits
- No artifacts without license information
- No executable evaluation or interpretation

---

## Forbidden Behaviors

The Repo Reader MUST NOT:

- Return full files or repositories
- Accept arbitrary file paths from callers
- Perform synthesis or summarization
- Make autonomous decisions

---

## Relationship to ResearchAgent

- ResearchAgent submits `RepoReaderRequest`
- Repo Reader returns `ResearchArtifact` objects
- ResearchAgent converts artifacts into `ProvenanceRecord`
- SynthesisAgent never sees Repo Reader outputs directly

---

## Mocking and Testing

A mock Repo Reader may:
- Return static artifacts
- Simulate errors
- Ignore RepoBridge entirely

Mock behavior must preserve API shape and constraints.

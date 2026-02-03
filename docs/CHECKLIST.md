# Development Checklist

This checklist tracks planned capabilities and safeguards for the research assistant.

Items may be:
- [ ] unchecked (not yet implemented)
- [x] checked (implemented)
- ~~struck through~~ (explicitly removed)

When removing an item, **add a brief explanation** below the checklist section explaining *why* it was removed.

---

## 1. Agent Logic per Mode

### Research Agent (Role A)
- [ ] No search (local / stub-only until explicitly enabled)
- [ ] No code reading (no repo parsing or file ingestion)
- [ ] No synthesis logic (analysis and summarization only)

### Synthesis Agent (Role B)
- [ ] No search
- [ ] No code reading
- [ ] No direct use of external excerpts

---

## 2. Invariant Tests

- [ ] Research agent cannot return code blocks
- [ ] Research agent cannot emit executable artifacts
- [ ] Synthesis agent cannot inspect provenance internals
- [ ] Synthesis agent fails on non-ProvenanceRecord inputs

---

## 3. Typed Result Objects

- [ ] Replace `dict` return from `ResearchAgent.analyze()` with a dataclass
- [ ] Explicit field typing for summaries and provenance
- [ ] Reject unknown or extra fields

---

## 4. Mode Switching / Orchestration

- [ ] Explicit mode switcher object or function
- [ ] Single allowed handoff point: Role A → Role B
- [ ] No implicit or automatic mode transitions

---

## Removal Log

Use this section to document intentionally removed checklist items.

Example:
- ~~Research agent performs live web search~~
  - Reason: Deferred to a future phase with Governor enforcement

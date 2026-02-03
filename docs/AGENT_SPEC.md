# Research Assistant Agent Specification

## Supported Modes

### Role A: Research Mode
**Purpose:** Prior art discovery and analysis

**Inputs:**
- Problem description
- Search constraints (repos, languages, licenses)

**Outputs:**
- Annotated excerpts
- Pattern summaries
- Source + license metadata

**Invariants:**
- No executable synthesis
- No unattributed excerpts

**Failure Cases:**
- Missing license info
- Overly large verbatim excerpts

---

### Role B: Synthesis Mode
**Purpose:** Original implementation from understanding

**Inputs:**
- Conceptual summaries (not raw code)
- Design constraints

**Outputs:**
- Original code or design
- Optional inspiration citations

**Invariants:**
- No verbatim reuse
- No external code blocks

**Failure Cases:**
- Accidental similarity to known implementation
- Implicit dependency on quoted code
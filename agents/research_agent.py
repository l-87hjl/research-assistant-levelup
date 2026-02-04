from typing import List
from agents.modes import AgentMode
from agents.provenance import ProvenanceRecord
from agents.results import ResearchResult
from agents.invariant_enforcement import assert_no_code_blocks

class ResearchAgent:
    """
    Role A: Research Agent

    Strictly analytical. No synthesis, no execution.
    """

    MODE = AgentMode.RESEARCH

    def __init__(self):
        self.mode = self.MODE

    def analyze(self, problem: str) -> ResearchResult:
        """
        Outline of research process:
        1. Restate and scope the problem
        2. Identify relevant dimensions and approaches
        3. Summarize known patterns (if any)
        4. Record provenance for any external references
        5. Explicitly state uncertainty or insufficiency
        """
        summaries: List[str] = []
        provenance: List[ProvenanceRecord] = []

        # Placeholder: analytical summaries only
        summaries.append(f"Problem scoped as: {problem}")
        summaries.append("No external repositories accessed at this stage.")

        # Enforce invariants
        assert_no_code_blocks(summaries)

        return ResearchResult(summaries=summaries, provenance=provenance)

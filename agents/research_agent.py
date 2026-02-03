from typing import List
from agents.modes import AgentMode
from agents.provenance import ProvenanceRecord

class ResearchAgent:
    """
    Role A: Research Agent

    This agent is strictly read-only and source-forward.
    It may analyze, quote, and summarize external material,
    but may not synthesize executable artifacts.
    """

    MODE = AgentMode.RESEARCH

    def __init__(self):
        self.mode = self.MODE

    def analyze(self, problem: str) -> dict:
        """
        Analyze a problem and return research findings.

        Returns a dict with:
        - summaries: List[str]
        - provenance: List[ProvenanceRecord]
        """
        # Placeholder: no external access yet
        return {
            "summaries": [],
            "provenance": []  # must contain ProvenanceRecord only
        }
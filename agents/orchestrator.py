from agents.modes import AgentMode, ModeViolationError
from agents.research_agent import ResearchAgent
from agents.synthesis_agent import SynthesisAgent
from agents.results import ResearchResult
from typing import List

class Orchestrator:
    """
    Explicit coordinator for Role A → Role B handoff.

    This is the ONLY place where mode transitions are allowed.
    """

    def __init__(self):
        self.research_agent = ResearchAgent()
        self.synthesis_agent = SynthesisAgent()
        self.current_mode = None

    def run_research(self, problem: str) -> ResearchResult:
        self.current_mode = AgentMode.RESEARCH
        result = self.research_agent.analyze(problem)
        if not isinstance(result, dict):
            raise ModeViolationError("ResearchAgent must return raw data prior to typing")
        return ResearchResult(**result)

    def run_synthesis(self, design_notes: List[str], research_result: ResearchResult):
        if self.current_mode != AgentMode.RESEARCH:
            raise ModeViolationError("Synthesis may only follow research")
        self.current_mode = AgentMode.SYNTHESIS
        return self.synthesis_agent.synthesize(
            design_notes=design_notes,
            provenance=research_result.provenance,
        )
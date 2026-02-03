from agents.modes import AgentMode, ModeViolationError
from agents.provenance import ProvenanceRecord
from typing import List

class SynthesisAgent:
    """
    Role B: Synthesis Agent

    This agent produces original output based on conceptual understanding.
    It must never directly consume or transform external code.
    """

    MODE = AgentMode.SYNTHESIS

    def __init__(self):
        self.mode = self.MODE

    def synthesize(self, design_notes: List[str], provenance: List[ProvenanceRecord]):
        """
        Perform synthesis from design notes.

        Provenance is accepted for citation/logging only and must not
        influence executable structure directly.
        """
        if any(not isinstance(p, ProvenanceRecord) for p in provenance):
            raise ModeViolationError("Invalid provenance object passed to synthesis agent")

        # Placeholder: original implementation goes here
        return None
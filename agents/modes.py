from enum import Enum

class AgentMode(str, Enum):
    RESEARCH = "research"
    SYNTHESIS = "synthesis"

class ModeViolationError(Exception):
    """Raised when an agent attempts an action outside its declared mode."""
    pass
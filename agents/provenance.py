from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ProvenanceRecord:
    """
    Immutable record describing the source of researched material.

    This object is data-only. It carries context forward but must never
    be executed, evaluated, or auto-consumed by synthesis logic.
    """
    repo: str
    commit: Optional[str]
    path: Optional[str]
    license: Optional[str]
    excerpt_span: Optional[str]
    rationale: str

    def summary(self) -> str:
        return (
            f"Source: {self.repo}"
            + (f"@{self.commit}" if self.commit else "")
            + (f" | Path: {self.path}" if self.path else "")
            + (f" | License: {self.license}" if self.license else "")
        )
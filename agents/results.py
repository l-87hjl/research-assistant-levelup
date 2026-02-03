from dataclasses import dataclass
from typing import List
from agents.provenance import ProvenanceRecord

@dataclass(frozen=True)
class ResearchResult:
    """
    Typed result object for ResearchAgent output.

    Narrows legal output space and prevents ad-hoc fields.
    """
    summaries: List[str]
    provenance: List[ProvenanceRecord]

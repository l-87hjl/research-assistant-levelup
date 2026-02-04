from dataclasses import dataclass
from typing import List, Optional, Dict

# ----------------------
# Request Objects
# ----------------------

@dataclass(frozen=True)
class RepoConstraints:
    allowlist: Optional[List[str]] = None
    denylist: Optional[List[str]] = None
    max_repos: Optional[int] = None


@dataclass(frozen=True)
class FileConstraints:
    allowed_extensions: Optional[List[str]] = None
    max_excerpt_chars: int = 1000
    max_excerpts_per_repo: int = 5


@dataclass(frozen=True)
class LicenseConstraints:
    allowed_licenses: Optional[List[str]] = None
    require_license: bool = True


@dataclass(frozen=True)
class ResultLimits:
    max_total_excerpts: int = 20


@dataclass(frozen=True)
class RepoReaderRequest:
    query: str
    repo_constraints: Optional[RepoConstraints] = None
    file_constraints: Optional[FileConstraints] = None
    license_constraints: Optional[LicenseConstraints] = None
    result_limits: Optional[ResultLimits] = None


# ----------------------
# Response Objects
# ----------------------

@dataclass(frozen=True)
class ResearchArtifact:
    excerpt: str
    repo: str
    commit: str
    path: str
    license: str
    excerpt_span: str


@dataclass(frozen=True)
class RepoReaderError:
    code: str
    message: str
    details: Optional[Dict] = None


@dataclass(frozen=True)
class RepoReaderResponse:
    artifacts: List[ResearchArtifact]
    errors: Optional[List[RepoReaderError]] = None

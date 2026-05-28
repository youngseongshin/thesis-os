from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from thesis_os.models import Evidence


@dataclass(frozen=True)
class SourceEvent:
    """Raw-ish public event contract before it becomes evidence."""

    id: str
    entity: str
    channel: str
    source: str
    source_date: str
    content: str
    url: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DeliveryResult:
    ok: bool
    destination: str
    message_id: str = ""
    error: str = ""


class QuantProvider(ABC):
    """Read-only provider for structured market/company data."""

    name: str

    @abstractmethod
    def collect(self) -> list[Evidence]:
        """Return normalized evidence records."""


class QualitativeProvider(ABC):
    """Read-only provider for unstructured source channels."""

    name: str

    @abstractmethod
    def collect_events(self) -> list[SourceEvent]:
        """Return source events. A separate builder should convert them to evidence."""


class DeliveryAdapter(ABC):
    """Delivery interface for optional user-facing summaries."""

    name: str

    @abstractmethod
    def send_markdown(self, destination: str, markdown: str) -> DeliveryResult:
        """Deliver markdown or a markdown-derived message."""


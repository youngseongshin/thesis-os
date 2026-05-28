from __future__ import annotations

from thesis_os.adapters.base import DeliveryAdapter, DeliveryResult, QualitativeProvider, QuantProvider, SourceEvent
from thesis_os.models import Evidence, utc_now


class SampleQuantProvider(QuantProvider):
    name = "sample_quant"

    def collect(self) -> list[Evidence]:
        return [
            Evidence(
                id="EVID-SAMPLE-QUANT-001",
                entity="AI Infrastructure Basket",
                source_type="market_data",
                source=self.name,
                source_date="2026-01-31",
                collected_at=utc_now(),
                claim="Relative strength improved while volume expanded.",
                interpretation="Potential evidence of renewed institutional interest, not sufficient alone.",
                confidence="medium",
                tags=["sample", "quant", "relative-strength"],
            )
        ]


class SampleQualitativeProvider(QualitativeProvider):
    name = "sample_qualitative"

    def collect_events(self) -> list[SourceEvent]:
        return [
            SourceEvent(
                id="SRC-SAMPLE-YOUTUBE-001",
                entity="AI Infrastructure Basket",
                channel="youtube",
                source=self.name,
                source_date="2026-01-31",
                content="Industry commentary points to sustained AI infrastructure capex.",
                url="https://example.com/sample",
                metadata={"sample": True},
            )
        ]


class StdoutDeliveryAdapter(DeliveryAdapter):
    name = "stdout"

    def send_markdown(self, destination: str, markdown: str) -> DeliveryResult:
        print(f"--- delivery:{destination} ---")
        print(markdown)
        return DeliveryResult(ok=True, destination=destination, message_id="stdout")


from __future__ import annotations


def evaluate_direction(direction: str, absolute_return: float, benchmark_return: float = 0.0) -> tuple[bool, str]:
    excess = absolute_return - benchmark_return
    if direction in {"up", "relative_outperform"}:
        hit = excess > 0
    elif direction in {"down", "relative_underperform"}:
        hit = excess < 0
    else:
        hit = abs(excess) < 0.02
    failure_mode = "none" if hit else "timing_failure"
    return hit, failure_mode


def feedback_report_markdown(prediction: dict[str, object], absolute_return: float, benchmark_return: float) -> str:
    direction = str(prediction["direction"])
    hit, failure_mode = evaluate_direction(direction, absolute_return, benchmark_return)
    excess = absolute_return - benchmark_return
    return "\n".join(
        [
            f"**Prediction:** `{prediction['id']}`",
            f"**Entity:** {prediction['entity']}",
            f"**Horizon:** {prediction['horizon']}",
            f"**Direction:** {direction}",
            "",
            "## Outcome",
            f"- Absolute return: {absolute_return:.2%}",
            f"- Benchmark return: {benchmark_return:.2%}",
            f"- Excess return: {excess:.2%}",
            f"- Hit: {'yes' if hit else 'no'}",
            f"- Failure mode: {failure_mode}",
            "",
            "## Lesson",
            "This sample report demonstrates the feedback contract. Replace sample returns with real measured outcomes in production.",
        ]
    )


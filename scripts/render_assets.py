from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Menlo.ttc",
        "/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def terminal_frame(lines: list[str], cursor: bool = False) -> Image.Image:
    width, height = 1120, 640
    img = Image.new("RGB", (width, height), "#0f172a")
    draw = ImageDraw.Draw(img)
    font = load_font(22)
    small = load_font(16)

    draw.rounded_rectangle((20, 20, width - 20, height - 20), radius=22, fill="#111827", outline="#334155", width=2)
    for i, color in enumerate(["#ef4444", "#f59e0b", "#22c55e"]):
        draw.ellipse((48 + i * 28, 48, 62 + i * 28, 62), fill=color)
    draw.text((142, 45), "Thesis OS quick demo", fill="#cbd5e1", font=small)

    y = 96
    for line in lines:
        color = "#e5e7eb"
        if line.startswith("$"):
            color = "#5eead4"
        elif line.startswith("{") or line.startswith("}") or line.strip().startswith('"'):
            color = "#bfdbfe"
        elif line.startswith("✓"):
            color = "#86efac"
        elif line.startswith("#"):
            color = "#94a3b8"
        draw.text((54, y), line, fill=color, font=font)
        y += 34

    if cursor:
        draw.rectangle((54, y + 4, 68, y + 28), fill="#5eead4")
    return img


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont | ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def prediction_ledger_frame(step: int) -> Image.Image:
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), "#f8fafc")
    draw = ImageDraw.Draw(img)
    title = load_font(40)
    subtitle = load_font(22)
    label = load_font(24)
    body = load_font(18)
    mono = load_font(18)

    draw.rounded_rectangle((48, 42, width - 48, 132), radius=24, fill="#0f766e")
    draw.text((78, 66), "Thesis OS", fill="#ffffff", font=title)
    draw.text((330, 82), "Stop building persuasive AI. Build accountable AI.", fill="#ccfbf1", font=subtitle)

    stages = [
        {
            "name": "1. Register",
            "headline": "Write the thesis before the outcome",
            "details": ["claim", "evidence IDs", "invalidation", "native horizon"],
            "color": "#dbeafe",
            "border": "#60a5fa",
        },
        {
            "name": "2. Wait",
            "headline": "Do not rewrite the original judgment",
            "details": ["prediction ledger", "action queue", "timestamped record"],
            "color": "#fef3c7",
            "border": "#f59e0b",
        },
        {
            "name": "3. Grade",
            "headline": "Measure process and market outcome separately",
            "details": ["process score", "result score", "failure mode", "feedback note"],
            "color": "#fce7f3",
            "border": "#ec4899",
        },
    ]

    x_positions = [70, 470, 870]
    y = 190
    for idx, stage_info in enumerate(stages):
        active = idx <= step
        fill = stage_info["color"] if active else "#e5e7eb"
        border = stage_info["border"] if active else "#cbd5e1"
        draw.rounded_rectangle((x_positions[idx], y, x_positions[idx] + 340, y + 220), radius=18, fill=fill, outline=border, width=4)
        draw.text((x_positions[idx] + 24, y + 24), stage_info["name"], fill="#0f172a", font=label)
        detail_y = y + 68
        for line in wrap_text(draw, stage_info["headline"], body, 292):
            draw.text((x_positions[idx] + 24, detail_y), line, fill="#1e293b", font=body)
            detail_y += 24
        detail_y += 10
        for detail in stage_info["details"]:
            draw.text((x_positions[idx] + 28, detail_y), f"- {detail}", fill="#334155", font=body)
            detail_y += 28
        if idx < len(stages) - 1:
            arrow_color = "#0f172a" if idx < step else "#94a3b8"
            draw.line((x_positions[idx] + 350, y + 110, x_positions[idx + 1] - 20, y + 110), fill=arrow_color, width=6)
            draw.polygon(
                [
                    (x_positions[idx + 1] - 20, y + 110),
                    (x_positions[idx + 1] - 44, y + 96),
                    (x_positions[idx + 1] - 44, y + 124),
                ],
                fill=arrow_color,
            )

    draw.rounded_rectangle((120, 470, width - 120, 638), radius=18, fill="#111827")
    ledger_lines = [
        '{',
        '  "prediction": "candidate should outperform over native horizon",',
        '  "process_score": 0.89,',
        '  "result_score": 0.62,',
        '  "lesson": "signal worked, but thesis evidence needs breadth"',
        '}',
    ]
    text_y = 492
    for line in ledger_lines:
        color = "#bfdbfe" if ":" in line else "#e5e7eb"
        draw.text((150, text_y), line, fill=color, font=mono)
        text_y += 22

    draw.text((120, 660), "Public-safe sample. Not financial advice. Synthetic values shown for workflow demonstration.", fill="#64748b", font=body)
    return img


def render_prediction_ledger_demo() -> Path:
    frames = [prediction_ledger_frame(i) for i in range(3)]
    path = ASSETS / "prediction-ledger-demo.gif"
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=1300, loop=0, optimize=True)
    return path


def render_terminal_demo() -> Path:
    frames_text = [
        [
            "$ thesis-os quickstart-stock --out ./quickstart_run \\",
            "  --tickers NVDA,AAPL,MSFT --benchmark SPY",
            "{",
            '  "source": "stooq_public_daily_csv",',
            '  "candidate_count": 3,',
            '  "top_candidate": "QS-NVDA-001"',
            "}",
            "",
            "# No broker login or paid feed required.",
        ],
        [
            "$ ls quickstart_run/",
            "{",
            '  "local": "SQLite DB",',
            '  "vault": "Markdown notes",',
            '  "prediction_ledger": "JSONL"',
            "}",
            "",
            "# Public prices become a local research workspace.",
        ],
        [
            "$ thesis-os alpha run-quant-screener --workspace ./workspace \\",
            "  --input-csv ./quickstart_run/quickstart_quant_features.csv",
            "{",
            '  "candidate_count": 3,',
            '  "top_candidate": "QS-NVDA-001"',
            "}",
            "",
            "# Quant screeners create accountable candidates.",
        ],
        [
            "$ cat quickstart_run/vault/evidence/public-stock-quickstart.md",
            "{",
            '  "data_boundary": "price-only public evidence",',
            '  "rule": "candidate, not a buy signal"',
            "}",
            "",
            "# The repo is honest about source limits.",
        ],
        [
            "$ thesis-os lattice evaluate-screener --workspace ./quickstart_run \\",
            "  --candidate-id QS-NVDA-001 --horizon '63 trading days'",
            "{",
            '  "excess_return": 0.12,',
            '  "hit": true',
            "}",
            "",
            "# Screeners are graded over forward horizons.",
        ],
        [
            "$ open quickstart_run/vault/dashboard/index.html",
            "{",
            '  "dashboard": "theses + actions + predictions + feedback"',
            "}",
            "",
            "# The cockpit shows the whole judgment loop.",
        ],
        [
            "$ thesis-os demo --out ./demo_run",
            "{",
            '  "mode": "fully offline synthetic sample",',
            '  "ci": "safe"',
            "}",
            "",
            "# Offline demo remains available for tests and CI.",
        ],
        [
            "$ thesis-os arki build-wiki-index --workspace ./quickstart_run",
            "{",
            '  "wiki": "vault/wiki/index.md",',
            '  "ssot": "vault/ssot/canonical-locations.md"',
            "}",
            "",
            "✓ evidence, screeners, theses, and feedback stay retrievable",
        ],
    ]
    frames = [terminal_frame(lines, cursor=i == len(frames_text) - 1) for i, lines in enumerate(frames_text)]
    path = ASSETS / "terminal-demo.gif"
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=1450, loop=0, optimize=True)
    return path


def main() -> int:
    ASSETS.mkdir(parents=True, exist_ok=True)
    paths = [render_terminal_demo(), render_prediction_ledger_demo()]
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

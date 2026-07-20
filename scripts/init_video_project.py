#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def write_new(path: Path, content: str) -> None:
    if path.exists():
        print(f"skip existing: {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"created: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a talking-head video production workspace.")
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--source", required=True)
    parser.add_argument("--ratio", choices=("9:16", "16:9", "1:1", "4:5"), default="9:16")
    args = parser.parse_args()

    root = args.project_dir.resolve()
    for name in ("inputs", "assets", "renders", "review"):
        (root / name).mkdir(parents=True, exist_ok=True)

    brief = f"""# Production Brief

Goal:
Audience:
Constraints:
Proof standard:

Source: `{args.source}`
Aspect ratio: `{args.ratio}`
"""
    visual = {
        "version": 2,
        "source": args.source,
        "duration": 0,
        "ratio": args.ratio,
        "direction": {
            "character": [],
            "primary_grammar": "",
            "a_track_target": 0.65,
            "anti_goals": [],
        },
        "beats": [],
    }
    manifest = {"version": 1, "assets": []}
    layout = {"version": 1, "samples": [], "zones": []}
    typography = {
        "version": 1,
        "font_family": "",
        "thesis": {},
        "card_title": {},
        "keyword": {},
        "metadata": {},
        "subtitle_chinese": {},
        "subtitle_translation": {},
        "longest_strings_tested": [],
    }
    aesthetic = {"version": 1, "frames": [], "minimum_average": 1.7, "zero_scores_allowed": 0}

    write_new(root / "brief.md", brief)
    write_new(root / "transcript.json", json.dumps({"version": 1, "cues": []}, indent=2) + "\n")
    write_new(root / "layout-survey.json", json.dumps(layout, indent=2) + "\n")
    write_new(root / "typography-plan.json", json.dumps(typography, indent=2) + "\n")
    write_new(root / "visual-script.json", json.dumps(visual, indent=2) + "\n")
    write_new(root / "asset-manifest.json", json.dumps(manifest, indent=2) + "\n")
    write_new(root / "card-map.md", "# Card Map\n\n| Time | Sentence function | Card | Text nodes | Zone | Motion | Risk |\n| --- | --- | --- | --- | --- | --- | --- |\n")
    write_new(root / "aesthetic-review.json", json.dumps(aesthetic, indent=2) + "\n")
    write_new(root / "review.md", "# Review\n\n## Observed\n\n## Fixed\n\n## Remaining Uncertainty\n")
    write_new(root / "publish-package.md", "# Publish Package\n\nTitle:\nCover line:\nDescription:\nHashtags:\nCore takeaway:\nPinned comment:\n")
    write_new(root / "postmortem.md", "# Postmortem\n\nWhat worked:\nWhat failed:\nFriction:\nReusable improvement:\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

FUNCTIONS = {"hook", "trust", "explanation", "number", "comparison", "list", "proof", "step", "transition", "judgment", "conclusion"}
TRACKS = {"A", "B", "full-screen-card"}
PROOF_TYPES = {"proof", "illustration", "generated", "none"}
CARD_TYPES = {"none", "thesis", "metric", "receipt", "compare", "checklist", "pipeline", "central-map", "proof", "tool-choice", "verdict", "warning", "keyword"}
TEXT_ROLES = {"thesis", "title", "keyword", "metadata"}
RISK_TYPES = {"face", "hand", "mouth", "microphone", "subtitle", "proof-crop", "read-time", "platform-ui", "repetition", "none"}
REQUIRED = {"start", "end", "spoken", "function", "track", "card_type", "zone", "primary_visual", "text_nodes", "subtitle", "motion", "proof_type", "asset", "risks", "why"}
MOTION_REQUIRED = {"entry", "entry_frames", "hold", "exit", "exit_frames"}


def add(messages, label, message):
    messages.append(f"{label} {message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate semantic, visual, motion, and proof decisions in a talking-head visual script.")
    parser.add_argument("visual_script", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.visual_script.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read visual script: {exc}")
        return 2

    errors, warnings = [], []
    duration = data.get("duration")
    beats = data.get("beats")
    if data.get("version") != 2:
        errors.append("version must be 2")
    if not isinstance(data.get("direction"), dict):
        errors.append("direction must define the aesthetic strategy")
    if not isinstance(duration, (int, float)) or duration <= 0:
        errors.append("duration must be a positive number")
    if not isinstance(beats, list) or not beats:
        errors.append("beats must be a non-empty list")
        beats = []

    previous_start = -1.0
    emphasis_time = 0.0
    clean_a_time = 0.0
    card_counts = {}
    for index, beat in enumerate(beats):
        label = f"beat[{index}]"
        if not isinstance(beat, dict):
            add(errors, label, "must be an object")
            continue
        missing = REQUIRED - beat.keys()
        if missing:
            add(errors, label, f"missing fields: {', '.join(sorted(missing))}")
            continue
        start, end = beat["start"], beat["end"]
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or start < 0 or end <= start:
            add(errors, label, "has invalid start/end")
            continue
        if start < previous_start:
            add(errors, label, "is out of chronological order")
        previous_start = start
        beat_duration = end - start
        if isinstance(duration, (int, float)) and duration > 0 and end > duration + 0.05:
            add(errors, label, "ends after video duration")
        if beat["function"] not in FUNCTIONS:
            add(errors, label, f"has unknown function: {beat['function']}")
        if beat["track"] not in TRACKS:
            add(errors, label, f"has unknown track: {beat['track']}")
        if beat["card_type"] not in CARD_TYPES:
            add(errors, label, f"has unknown card_type: {beat['card_type']}")
        if beat["proof_type"] not in PROOF_TYPES:
            add(errors, label, f"has unknown proof_type: {beat['proof_type']}")
        if beat["proof_type"] == "proof" and not beat["asset"]:
            add(errors, label, "is proof but has no asset")
        if beat["proof_type"] in {"illustration", "generated"} and beat["function"] == "proof":
            add(errors, label, "labels non-proof media as a proof beat")
        if not isinstance(beat["subtitle"], bool):
            add(errors, label, "subtitle must be true or false")
        if not str(beat["why"]).strip():
            add(errors, label, "must explain why the visual earns its place")

        risks = beat["risks"]
        if not isinstance(risks, list) or not risks:
            add(errors, label, "must list at least one reviewed risk or 'none'")
        elif unknown := set(risks) - RISK_TYPES:
            add(errors, label, f"has unknown risks: {', '.join(sorted(unknown))}")

        text_nodes = beat["text_nodes"]
        if not isinstance(text_nodes, list):
            add(errors, label, "text_nodes must be a list")
            text_nodes = []
        texts = []
        for node_index, node in enumerate(text_nodes):
            if not isinstance(node, dict) or node.get("role") not in TEXT_ROLES or not str(node.get("text", "")).strip():
                add(errors, label, f"has invalid text_nodes[{node_index}]")
                continue
            texts.append(node["text"].strip())
        if len(texts) != len(set(texts)):
            add(errors, label, "repeats the same text in multiple nodes")
        if beat["card_type"] == "none" and text_nodes:
            add(warnings, label, "uses text nodes with card_type 'none'; confirm these are only subtitle text")
        if beat["card_type"] != "none" and not text_nodes:
            add(errors, label, "uses a card but defines no text nodes")
        if len(text_nodes) > 4:
            add(warnings, label, "has more than four text nodes; simplify the card")
        if beat["subtitle"] and any(text.strip() == str(beat["spoken"]).strip() for text in texts):
            add(warnings, label, "duplicates the complete spoken/subtitle sentence in a visual text node")

        motion = beat["motion"]
        if not isinstance(motion, dict) or not MOTION_REQUIRED.issubset(motion):
            add(errors, label, "has an incomplete motion contract")
        else:
            for frame_key in ("entry_frames", "exit_frames"):
                value = motion[frame_key]
                if not isinstance(value, int) or value < 0 or value > 18:
                    add(errors, label, f"{frame_key} must be an integer from 0 to 18")

        card_counts[beat["card_type"]] = card_counts.get(beat["card_type"], 0) + 1
        if beat["card_type"] == "none" and beat["track"] == "A":
            clean_a_time += beat_duration
        else:
            emphasis_time += beat_duration
            if beat_duration > 2.8 and beat["card_type"] in {"thesis", "metric", "receipt", "keyword"}:
                add(warnings, label, f"holds a simple emphasis for {beat_duration:.1f}s; review pacing")

    for left_index, left in enumerate(beats):
        if not isinstance(left, dict) or not REQUIRED.issubset(left):
            continue
        for right_index in range(left_index + 1, len(beats)):
            right = beats[right_index]
            if not isinstance(right, dict) or not REQUIRED.issubset(right):
                continue
            if right["start"] >= left["end"]:
                break
            if left["primary_visual"] != "none" and right["primary_visual"] != "none":
                errors.append(f"beat[{left_index}] and beat[{right_index}] overlap with two primary visuals")

    if isinstance(duration, (int, float)) and duration > 0:
        density = emphasis_time / duration
        clean_share = clean_a_time / duration
        if density > 0.40:
            warnings.append(f"high-emphasis density is {density:.0%}; target 25-35% unless the format justifies more")
        if clean_share < 0.50:
            warnings.append(f"explicit clean A-track share is {clean_share:.0%}; target at least 55% for ordinary talking-head work")
        if not any(isinstance(b, dict) and b.get("function") == "hook" and b.get("start", 99) < 3 for b in beats):
            warnings.append("no hook beat begins in the first three seconds")
        if not any(isinstance(b, dict) and b.get("function") == "conclusion" for b in beats):
            warnings.append("no conclusion beat is defined")
    non_none_counts = [count for card, count in card_counts.items() if card != "none"]
    if sum(non_none_counts) >= 5 and max(non_none_counts, default=0) / sum(non_none_counts) > 0.6:
        warnings.append("one card type dominates more than 60% of visual beats; review semantic variety")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: {len(beats)} beat(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

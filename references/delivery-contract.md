# Delivery Contract

## Required Project Artifacts

| Artifact | Required content |
| --- | --- |
| `brief.md` | Goal, audience, constraints, proof standard, source facts |
| `transcript.json` | Sentence-level start/end timestamps and corrected text |
| `layout-survey.json` | Sampled face, gesture, background, and safe-zone decisions |
| `typography-plan.json` | Font family, hierarchy, subtitle tiers, and longest-string tests |
| `visual-script.json` | Every intentional visual beat and clean A-track interval |
| `card-map.md` | Sentence function, semantic card, text nodes, zone, motion, and risk |
| `asset-manifest.json` | Asset type, source, license/provenance, local path, review decision |
| `aesthetic-review.json` | Frame scores for hierarchy, safety, typography, fit, balance, coherence, and proof honesty |
| `review.md` | Observed frame/timing issues, fixes, remaining uncertainty |
| `publish-package.md` | Title, cover line, description, hashtags, takeaway, pinned comment |
| `postmortem.md` | What worked, failed, caused friction, and became reusable |

## Pre-Render Gate

- Source media is readable and duration is known.
- Transcript covers the complete duration.
- Names, numbers, and technical terms are checked.
- Visual script passes `validate_visual_script.py`.
- Source-frame layout survey covers at least 8 representative samples.
- Typography plan tests the longest real Chinese and Latin strings.
- Card map uses semantic variety and explicitly keeps low-value sentences clean.
- Every proof beat resolves to a real reviewed asset.
- Every illustration has provenance and cannot be mistaken for proof.
- Face and subtitle safe zones are defined from sampled frames.

## Frame Review Sampling

Extract at minimum:

- One frame in the first three seconds
- One frame from every emphasis/card/B-roll beat
- One frame immediately before or after every major transition
- Representative clean A-track frames from each section
- One frame from the final recommendation

Create a contact sheet, inspect it at readable resolution, then spot-check motion at any suspicious transition.

## Acceptance Checklist

- Hook is visible or understandable within the first three seconds.
- Subtitles are readable and aligned with speech.
- No card, keyword, subtitle, face, or gesture overlap is incoherent.
- Exactly one primary visual wins each frame.
- Every representative frame passes the aesthetic rubric with no zero score.
- Thesis, card title, keyword, metadata, and subtitle levels are visibly distinct.
- Cards transform the spoken idea rather than repeating subtitles.
- Important spoken lines have matching emphasis; connective lines can breathe.
- B-roll is semantically relevant and correctly labeled as proof or illustration.
- No unsupported number or claim is visually upgraded into apparent proof.
- The ending contains one clear judgment or action.
- Final video and cover exist at the reported paths.
- Final render, not only preview frames, was reviewed.

## Completion Report

State:

1. What changed
2. What was verified
3. What remains uncertain
4. Exact paths to video, cover, visual script, manifest, and review output
5. The reusable improvement produced during the work

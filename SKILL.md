---
name: talking-head-video-workflow
description: "Produce, redesign, or review polished talking-head knowledge videos from raw spoken footage using a complete editorial system: transcription, semantic visual scripting, face-aware composition, Chinese and bilingual typography, purpose-built animated cards, selective proof-aware B-roll, Remotion implementation, deterministic covers, aesthetic review, frame review, publish packaging, and postmortem. Use when the user provides a recorded monologue and wants the characteristic high-clarity blue/orange/dark knowledge-video treatment, asks to reproduce this project's visual quality, or wants a reusable talking-head production workflow. Do not use for faceless montages, fictional films, music videos, or script-only work with no production scope."
---

# Talking-Head Video Workflow

Turn spoken footage into an editorial knowledge video. Preserve the speaker as the trust layer. Use typography, cards, motion, proof, and B-roll only when they make an idea faster to understand, harder to forget, or easier to trust.

## Completion Definition

Do not call the work complete until all of these exist:

- Corrected timestamped transcript
- Source-frame layout survey and safe-zone map
- Text-only visual script
- Typography plan and card mapping table
- Asset/proof manifest
- Full rendered video
- Contact sheet and written aesthetic review
- Deterministic cover
- Publish package
- Postmortem with a reusable improvement

## Required Inputs

Locate or infer:

- Source video or audio
- Platform and aspect ratio; default to the source ratio
- Spoken language and subtitle language
- Brand assets; otherwise use `assets/design-system.json`
- Real proof for claims that need visual evidence

Ask only when a missing choice would materially change the result. Do not require a finished script when media can be transcribed.

## Mandatory Reference Loading

Read these before the corresponding phase:

- Before visual design: `references/art-direction.md`, `references/typography.md`, and `references/composition-and-rhythm.md`
- Before choosing the production pattern: `references/production-lessons.md`
- Before choosing cards or motion: `references/motion-and-cards.md`
- Before implementation: `references/remotion-implementation.md`
- Before cover production: `references/cover-system.md`
- Before approval: `references/frame-review.md` and `references/delivery-contract.md`

Treat `assets/design-system.json` as the default numerical contract. Adapt it only for source geometry, language, or an existing brand system.

## Required Workflow

Follow these gates in order.

### 1. Inspect The Source

- Probe duration, dimensions, frame rate, codecs, and audio.
- Sample at least 8-12 frames across the source.
- Identify face, mouth, microphone, active hand gestures, background objects, and stable negative space.
- Record safe zones per section when the speaker moves; do not assume one global side.
- Preserve an untouched source.

### 2. Transcribe And Correct

- Produce sentence-level timestamps.
- Correct names, numbers, units, product terms, and Chinese technical vocabulary against the audio.
- Mark uncertain language. Do not animate uncertain text as fact.

### 3. Structure The Argument

Label each sentence as one of:

`hook`, `trust`, `explanation`, `number`, `comparison`, `list`, `proof`, `step`, `transition`, `judgment`, or `conclusion`.

Find the hook, section turns, proof beats, comparisons, steps, memorable numbers, and final recommendation. Preserve the speaker's meaning; do not silently strengthen a claim.

### 4. Choose The Visual Direction

Write a compact direction statement:

- Desired character: practical, field-tested, judgment-heavy, clean but not cold
- Primary visual grammar: speaker, thesis type, structured card, proof panel, or selective B-roll
- Density target and A-track share
- Aspect-ratio strategy
- Palette and type family
- Explicit anti-goals

Reject a direction that is merely "tech-looking" without an information hierarchy.

### 5. Build The Text-Only Visual Script

Use `assets/visual-script.example.json`. Every intentional beat must define:

- Exact time and spoken idea
- Sentence function and track
- One primary visual
- Card type or `none`
- Exact text nodes and hierarchy level
- Zone and face/hand/subtitle risks
- Entry, hold, and exit motion
- Proof type and asset
- Why the visual earns its place

Keep clean A-track intervals explicit. `none` is a designed choice.

### 6. Design Typography

- Define four text levels before coding: thesis, card title, supporting keyword, metadata.
- Define Chinese subtitle and optional translation sizes separately.
- Test the longest real strings, not placeholder text.
- Shorten copy before shrinking below the readable floor.
- Use local deterministic typography for all final Chinese text.

### 7. Map Cards And Motion

Choose card semantics from `references/motion-and-cards.md`. Do not use the same list card for every idea.

Create a mapping table:

| Time | Sentence function | Card | Text nodes | Zone | Motion | Risk |
| --- | --- | --- | --- | --- | --- | --- |

One sentence may map to no card. A card must transform the spoken idea, not repeat the subtitle.

### 8. Check Assets And Proof

Classify every visual asset as `proof`, `illustration`, `generated`, or `none`.

- Real recording, screenshot, metric, or workflow state may be proof.
- Stock and generated media are illustration only.
- Reject fake UI, pseudo-text, unrelated people, semantic mismatch, and repeated filler.
- Keep provenance, prompt, license/source, local path, and review decision.

### 9. Implement

Prefer data-driven Remotion when code production is available. Separate:

- Transcript cues
- Visual beat data
- Design tokens
- Reusable cards
- Composition and active-layer selection
- Review tooling

Use spring motion for entry, short eased exits, staggered rows, and restrained ambient movement. Never animate layout continuously merely to look active.

### 10. Validate Before Render

Run:

```bash
python scripts/validate_visual_script.py <project>/visual-script.json
```

Fix every error. Treat warnings as design review prompts, not console noise.

### 11. Render And Review

- Render the complete duration.
- Extract the first three seconds, every visual beat, nearby clean A-track, every transition, and the ending.
- Create a contact sheet.
- Review in three passes: correctness, geometry/readability, then aesthetics/rhythm.
- Check motion around suspicious stills; a good still does not prove good timing.
- Revise and rerender until the review passes.

### 12. Cover, Publish, Postmortem

- Generate background imagery without final text when needed.
- Typeset cover text locally.
- Align cover conflict, video hook, and publish title.
- Deliver title, description, 3-5 hashtags, core takeaway, and optional pinned comment.
- Convert repeated friction into a component, script, reference, or validator rule.

## Non-Negotiable Aesthetic Rules

- Keep one primary visual per frame.
- Protect eyes, nose, mouth, microphone, and meaningful gestures.
- Keep subtitles as the stable comprehension layer, not a second headline.
- Let the A-track carry trust, jokes, skepticism, complex reasoning, and final authority.
- Use large type only for short high-value thoughts.
- Use orange for conflict, warning, reversal, or cost; blue for structure, capability, and conclusion.
- Use cards by semantic function, not as decorative containers.
- Return to clean A-track after emphasis bursts.
- Keep most ordinary emphasis bursts between 1.0 and 2.8 seconds.
- Never present stock or generated media as proof.
- Never approve a render without frame and timing review.

## Aesthetic Rejection Test

Reject or simplify a frame when any answer is no:

1. Can the viewer identify the primary idea in under one second?
2. Does the visual add meaning instead of repeating the subtitle?
3. Is the speaker still the trust anchor when the sentence needs trust?
4. Is every text level visibly different in scale and role?
5. Is the card shape appropriate to the sentence function?
6. Does the frame belong to the same visual world as adjacent frames?
7. Would removing one element improve comprehension?

## Output Contract

Report:

- What changed
- What was verified
- What remains uncertain
- Exact paths to final video, cover, transcript, visual script, manifest, contact sheet, review, and publish package
- The reusable improvement created during production

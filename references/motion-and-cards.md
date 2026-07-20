# Motion And Card Grammar

## Contents

1. Sentence-to-card mapping
2. Card catalog
3. Motion grammar
4. Timing
5. Anti-patterns

## Sentence-To-Card Mapping

Choose by information function, not visual taste.

| Sentence function | Preferred visual |
| --- | --- |
| Hook / reversal | giant thesis, split reveal, short keyword burst |
| Number / cost | metric, meter, receipt, score ladder |
| Comparison | split compare, before/after, expectation/reality |
| Steps / setup | numbered sequence, process strip, progressive checklist |
| List | checklist only when items share one question |
| Mechanism | central object map, pipeline, token flow, memory stack |
| Proof | framed real recording/screenshot with one instruction label |
| Risk | warning card, failure tags, cost lock; red only for verified severity |
| Choice | tool-choice matrix or active-row decision card |
| Judgment | verdict card with one supporting contrast |
| Conclusion | full-screen thesis or clean speaker with one final line |

Use `none` for trust-building, jokes, connective explanation, skepticism, and sentences already clear through the speaker.

## Card Catalog

### Giant Thesis

- Use 3-12 Chinese characters or one short sentence.
- Let it own the frame.
- Enter by mask reveal, short slide, or restrained scale.
- Do not pair with a dense card.

### Metric / Receipt

- One dominant value, one unit, one context line.
- Count only when the number is the point; otherwise reveal directly.
- Use orange for cost or surprise, blue for capability or verified progress.

### Compare Card

- Two columns or two states with one shared comparison dimension.
- Do not compare unrelated lists.
- Reveal the baseline first, then the contrast.

### Checklist

- Maximum 3-4 items.
- Stagger rows 5-8 frames at 30fps.
- Use one active row or accent; do not light every row equally.

### Process Strip / Pipeline

- Use for ordered stages, caching, handoff, and workflow.
- Grow the connector first; reveal nodes in spoken order.
- Keep labels short. The line supplies sequence, not decoration.

### Central Object Map

- Keep one central object stable while capabilities or relationships change.
- Use no more than four side labels.
- Animate connections only when the spoken relationship appears.

### Proof Panel

- Show a real screen recording or screenshot.
- Crop so the decisive action is visible.
- Add one short label telling the viewer where to look.
- Keep browser chrome only when it establishes provenance.
- Do not keep proof footage full-screen after the evidence is understood.

### Tool Choice

- Show options with one active recommendation.
- Use labels for selection criteria, not feature dumping.
- End on a clear choice, not a neutral comparison.

### Verdict

- One large judgment plus at most one compact contrast.
- Use a growing underline or thin outline frame.
- Hold long enough for one clean read.

## Motion Grammar At 30fps

Default entry:

```text
spring: damping 18, stiffness 160, mass 0.8
translate: 18-38px toward resting position
scale: 0.97-0.99 to 1.0 when needed
entry: 6-12 frames
```

Gentle speaker-side cards:

```text
spring: damping 22, stiffness 140, mass 0.9
translate: 12-22px
```

Exit:

- Fade and translate over 6-10 frames.
- Begin exit before the next primary layer enters.
- Avoid two primary layers crossfading at equal opacity.

Rows:

- Reveal title first.
- Stagger rows by 5-8 frames.
- Highlight the row currently spoken.

Ambient motion:

- Slow drift, scale, scan, or opacity pulse may support a full-screen technical stage.
- Keep amplitude small and stop it from becoming the primary motion.
- Do not put ambient motion over a moving face without a strong reason.

## Timing

- Keyword flash: 0.7-1.5s
- Ordinary emphasis/card: 1.0-2.8s
- Structured list or mechanism: 2.5-5.0s when reading requires it
- Quick B-roll shot: 0.45-0.75s
- Ordinary B-roll shot: 0.75-1.25s
- Strong anchor shot: 1.3-1.6s

Tie entry to the spoken word. Do not snap every effect to round seconds.

## Sound

Use sound effects only for meaningful state change:

- Section turn
- Metric impact
- Proof reveal
- Final verdict

Keep UI blips subtle. Do not attach sound to every row or keyword.

## Anti-Patterns

- Same rectangular list card for every sentence
- Bouncing or floating without semantic change
- Long text squeezed into an impact card
- Card title and body saying the same thing
- Keyword pop triggered by every noun
- Several template styles in one 3-5 second window
- A 9:16 preset pasted into 16:9 without re-zoning
- Full-screen B-roll running through a personal judgment
- Motion that makes dynamic content resize the layout

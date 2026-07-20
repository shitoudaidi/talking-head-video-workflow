# Typography System

## Contents

1. Font selection
2. Hierarchy
3. Chinese layout
4. Subtitles
5. Cards
6. Covers
7. Fitting and review

## Font Selection

Prefer a real CJK family available locally. Recommended fallback order:

```text
Noto Sans CJK SC / Source Han Sans SC
Microsoft YaHei
PingFang SC
system sans-serif
```

Use one sans family for the main system. A mono family may appear only in technical metadata, code, timestamps, or compact English kickers.

Verify that the chosen font contains every Chinese glyph. Do not let the renderer silently mix visually incompatible fallback fonts.

## Four-Level Hierarchy At 1920x1080

Use `assets/design-system.json` as the numerical source.

| Level | Use | Typical size |
| --- | --- | ---: |
| L1 Thesis | hook, reversal, final judgment | 68-92px |
| L2 Card title | structured explanation | 38-52px |
| L3 Keyword | rhythm, active item | 30-42px |
| L4 Metadata | kicker, source, sequence | 14-22px |

Chinese primary subtitles: `34-42px`.
Translation subtitles: `16-22px`.

For 1080x1920, do not scale every number proportionally. Use the shorter canvas dimension and viewing distance as the constraint. Typical vertical ranges:

- Thesis: 72-112px
- Card title: 42-64px
- Keyword: 34-52px
- Chinese subtitle: 40-54px
- Translation: 20-28px

Test on a phone-sized preview.

## Chinese Layout

- Use short semantic phrases. L1 is usually 3-12 Chinese characters.
- Keep line breaks semantic; never strand punctuation or a one-character fragment.
- Use `word-break: keep-all` where supported, then insert deliberate breaks.
- Keep letter spacing at zero for ordinary Chinese.
- Use punctuation sparingly in giant type; composition should supply the pause.
- Avoid three lines of equal size and weight.
- Prefer a short title plus a smaller explanation instead of shrinking a long sentence.

Use orange on one decisive conflict phrase, not every important noun. Use blue on mechanism or conclusion phrases.

## Subtitle Design

Subtitles are a stable baseline layer.

- Keep one or two Chinese lines.
- Segment by spoken thought, not fixed character count alone.
- Start close to the first audible word and clear before the next cue competes.
- Place subtitles on a localized dark capsule or gradient; do not dim the whole video.
- Use `line-height` around `1.12-1.22`.
- Highlight only 1-3 decisive terms.
- Use a 3-6px accent rule or border when helpful; avoid multiple decorations.
- Raise subtitles in vertical video to clear platform controls.
- Keep bilingual translation visibly secondary through size, opacity, and spacing.

Do not display the exact same full sentence as both a giant headline and a subtitle except for a deliberate final freeze. When the headline carries the sentence, shorten or temporarily suppress the subtitle.

## Card Typography

Every card should have at most three text roles:

1. Metadata or eyebrow
2. Main title/value
3. Supporting row or explanation

Do not use more than two bold weights inside a compact card. Avoid paragraphs. Convert prose into a comparison, sequence, metric, or decision.

Numerals may be 1.4-1.8 times the card-title size. Keep units and labels smaller, aligned to the baseline.

## Cover Typography

- Main hook: 3-10 Chinese characters per line, one to three lines
- Category label: small and distinct
- Supporting judgment: one short sentence only
- Optional three keywords: use only when they add categories, not repetition
- Ensure the main hook is legible at feed-thumbnail size
- Compose real-person covers intentionally; preserve face direction and visual counterweight

Never use generated Chinese text as final. Render it locally with SVG, Canvas, Sharp, Pillow, or the project's deterministic renderer.

## Text Fitting Order

When text does not fit:

1. Rewrite shorter without changing meaning.
2. Insert a semantic line break.
3. Increase the container within the safe zone.
4. Reduce supporting text.
5. Reduce font size only as the last step and never below the readable floor.

Test the longest real title, subtitle, English product name, number, and URL-like string before final render.

## Typography Review

- Is L1 unmistakably dominant?
- Does each text block have one role?
- Are Chinese line breaks intentional?
- Are numbers and units aligned?
- Is translation clearly secondary?
- Does any text repeat another layer?
- Does the longest string fit on both desktop and phone preview?

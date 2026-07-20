# Remotion Implementation Blueprint

## Architecture

Keep five boundaries:

```text
config/data      source, duration, cues, beats, assets
tokens           palette, type, spacing, shape, motion
primitives       subtitle, metric, row, proof frame, accent rail
semantic cards   compare, checklist, pipeline, choice, verdict
composition      active layer selection and source video
```

Do not inline a full transcript inside the composition component. Do not create a unique component for every sentence when a semantic card can be data-driven.

## Data Types

Use a structure equivalent to:

```ts
type Cue = {
  start: number;
  end: number;
  text: string;
  translation?: string;
  emphasis: string[];
  function: "hook" | "trust" | "explanation" | "number" | "comparison" |
    "list" | "proof" | "step" | "transition" | "judgment" | "conclusion";
};

type VisualBeat = {
  start: number;
  end: number;
  track: "A" | "B" | "full-screen-card";
  card: "none" | "thesis" | "metric" | "receipt" | "compare" | "checklist" |
    "pipeline" | "central-map" | "proof" | "tool-choice" | "verdict";
  zone: string;
  textNodes: Array<{role: "thesis" | "title" | "keyword" | "metadata"; text: string}>;
  asset?: string;
  proofType: "proof" | "illustration" | "generated" | "none";
};
```

## Timed Motion

Create one reusable timed-motion hook returning `active`, `enter`, `exit`, `opacity`, `localFrame`, and `progress`.

At 30fps, start from:

```ts
const enter = spring({
  frame: frame - startFrame,
  fps,
  config: {damping: 18, stiffness: 160, mass: 0.8},
});

const exit = interpolate(
  frame,
  [endFrame - 8, endFrame],
  [1, 0],
  {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
);
```

Use deterministic frame-based animation only. Do not use CSS transitions, browser time, random values, or asynchronous layout changes in rendered frames.

## Subtitle Component

- Select the active cue by frame.
- Escape emphasis terms before constructing a regular expression.
- Enter with 10-14px upward translation and a damped spring.
- Dynamically choose one of two approved font sizes based on text length.
- Keep container dimensions stable.
- Suppress or shorten subtitles on deliberate full-screen thesis frames when duplication becomes heavy.

## Card Components

Build primitives first:

- `AccentRail`
- `Eyebrow`
- `MetricValue`
- `StaggeredRow`
- `ProofFrame`
- `ProgressConnector`

Compose semantic cards from those primitives. Keep card radius, border, surface opacity, and shadow sourced from tokens.

## Face-Aware Layout

Store layout zones in data, not hardcoded assumptions:

```ts
type LayoutZone = {
  start: number;
  end: number;
  face: {x: number; y: number; width: number; height: number};
  gesture?: {x: number; y: number; width: number; height: number};
  cardZone: "left" | "right" | "top" | "full-screen";
};
```

For stable sources, one or two zones may be enough. For moving speakers, segment the source.

## Media

- Normalize source media before production when codecs or frame rate are unstable.
- Use `OffthreadVideo` for video layers.
- Use `objectFit: cover` for intentional full-frame B-roll and `contain` only when preserving the full proof UI matters.
- Crop proof so the decisive state is readable.
- Avoid remote URLs during final render; use local deterministic assets.

## Dynamic Text Safety

- Define stable card width, min-height, grid tracks, and text containers.
- Test longest strings before render.
- Do not let hover, loading, or dynamic state change dimensions.
- Use semantic line breaks and size tiers, not viewport-scaled fonts.

## Verification

Run the repository's equivalent of:

```bash
npx tsc --noEmit
npx remotion compositions
npx remotion render <composition> <output.mp4>
```

Then probe the final file for video/audio streams and expected duration. A successful TypeScript check is not a visual review.

# Frame And Aesthetic Review

## Required Samples

Extract:

- At least one frame in the first second and first three seconds
- One middle frame from every emphasis, card, proof, and B-roll beat
- One frame before and after every major transition
- Representative clean A-track from each section
- The final judgment and final frame
- Extra frames wherever the face or hands move near a card

Create a readable contact sheet with time labels.

## Pass 1: Correctness

- Does the frame match the spoken sentence at that time?
- Are names, numbers, units, and product terms correct?
- Is the visual asset the intended one?
- Is proof genuine and clearly framed?
- Are subtitles synchronized?
- Are there black, missing, frozen, or corrupted frames?

## Pass 2: Geometry And Readability

- Is face, mouth, microphone, and gesture safe?
- Is the subtitle above platform UI and inside margins?
- Does the longest text fit?
- Is Chinese readable in one or two lines?
- Is translation secondary?
- Do card, keyword, subtitle, and proof occupy separate zones?
- Does a vertical card have enough scale for phone viewing?

## Pass 3: Aesthetics And Rhythm

- Is one primary visual obvious?
- Does the card type fit the sentence function?
- Is the largest type attached to the most important thought?
- Does the frame repeat information?
- Is the accent color semantically correct?
- Does the frame belong to the same visual world as adjacent beats?
- Is there enough clean A-track between emphasis bursts?
- Does B-roll clarify or merely decorate?
- Would removing an element improve the frame?

Use the score table in `art-direction.md`. Any zero requires revision.

## Motion Spot Checks

For every suspicious still, review a short range around it:

- Entry begins on the spoken trigger
- Title appears before rows
- Rows cascade in spoken order
- Exit clears before the next primary layer
- No equal-opacity collision between major layers
- Text is readable for a full glance
- Sound effect aligns with meaningful state change

## Automated Checks

When tooling permits:

- Detect mostly black frames at short intervals.
- Probe final duration, dimensions, frame rate, and audio/video streams.
- Validate every referenced local asset exists.
- Compare emphasis runtime with the density budget.
- Flag overlapping primary visuals and repeated text nodes.

Automated checks do not replace human visual inspection.

## Review Notes Contract

Record:

- `Observed`: concrete issues seen in frames or timing
- `Fixed`: changes made in response
- `Verified`: exact render and review checks passed
- `Remaining uncertainty`: claims, assets, or aesthetic judgment not fully resolved

Do not write "looks good" without naming the sampled frames and criteria.

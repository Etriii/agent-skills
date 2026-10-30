# taste source excerpts

Source: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/12af471f627f866411b4bd785b19646d3672784c/skills/taste-skill/SKILL.md).

Modified copy: selected excerpts only; surrounding toolkit and workflow omitted.
These passages are reference material; the suite workflow owns scope and authorization.

## Original lines 76-86

### 1. Read the brief and the project

Find out what is real: the subject, the audience, the one thing the page must get someone to do, the
stack, any existing brand (colours, fonts, logo), and above all **what imagery truly exists**: the
project's own photographs or product shots, a real interface that can be shown, an image generation
tool you can call, or nothing. Do not plan around pictures you do not have. Nothing of its own is
rarely nothing at all: the subject's city, street, materials and history are in open archives and
museums, free to use with a credit (step 6, `scripts/assets.mjs`).

If the request is vague, decide and state your reading in one line instead of asking. Ask only when a
missing fact blocks the work (for example, no product name).

## Original lines 299-302

9. **States and semantics.** Real links and buttons, visible focus, alt text, a phone layout that is
   its own composition. Every control, the live thing included, works from the keyboard alone in
   reading order and has an accessible name: its visible label, or `aria-label` when it shows only an
   icon.

## Original lines 469-473

- A control explains how to use it by its form, its label and its place. When it seems to need a
  sentence on how to operate it, redesign the control instead of adding the sentence. What a field
  accepts is different. First remove the limit where you can: a date picker, or a parser that takes
  any common format. A limit that remains, such as password rules or file type and size, stays visible
  beside the field and is tied to it with `aria-describedby`.

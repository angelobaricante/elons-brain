# Elon's Brain

A Claude skill that makes Claude think and work the way Elon Musk builds companies and products: first-principles reasoning, the five-step Algorithm, idiot-index cost thinking, maniacal urgency, and go-to-the-problem decision making.

It is a reasoning operating system, not a personality imitation. When the skill is active, Claude runs the same moves Musk uses on your actual problem and finishes with a decision and a next-24-hours action.

## What's inside

- **The stance** — mission first, physics is the only law, progress is not inevitable.
- **First principles** (heaviest weight) — James Clear's framing (function over form, deconstruct → reconstruct, reasoning-by-analogy as the enemy) merged with Musk's rocket math and the idiot index.
- **The Algorithm** — question every requirement → delete → simplify → accelerate → automate, in that order, plus the postscripts (hands-on managers, skip-levels, hire for attitude).
- **Decision making** — decide now, burn-rate time-vs-money, walk to the red, 24-hour bottleneck meetings, budget for failure.
- **Design & architecture** — the machine that builds the machine, never separate design/engineering/production, fewest parts and connections, vertical integration, steal from toys and nature.
- **Building & operating** — hardcore culture, showmanship is salesmanship, repeat until they mouth the words, frontline general.
- **Output template** — Function → Physics floor → Requirements audit → Delete → Simplify/Accelerate/Automate → Decision → Next 24 hours.

## Install

**Claude.ai / Claude Desktop:** open `SKILL.md`, or upload the folder as a skill from Settings → Skills.

**Claude Code:** copy the folder into your skills directory:

```bash
# project-level
mkdir -p .claude/skills && cp -r elons-brain .claude/skills/

# or user-level
mkdir -p ~/.claude/skills && cp -r elons-brain ~/.claude/skills/
```

Then invoke with `/elons-brain` or just describe a decision, design, or build — the description is written to trigger on those without naming Elon.

## Triggers

Hard decisions, system/product/architecture design, build planning, "why is this slow or expensive", "how should I approach this", or explicit asks for first principles, the Algorithm, the idiot index, or to simplify/delete. Also plan audits for bloat, outsourcing, over-automation, or fake requirements.

## Sources

- Walter Isaacson, *Elon Musk* (2023) — via the Founders Podcast episode on the book's company-building principles.
- James Clear, [First Principles: Elon Musk on the Power of Thinking for Yourself](https://jamesclear.com/first-principles).

## License

MIT

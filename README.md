# Elon's Brain

An agent skill that makes your AI think and build the way Elon Musk builds companies and products: first-principles reasoning, the five-step Algorithm, idiot-index cost thinking, maniacal urgency, and go-to-the-problem decision making.

It is a reasoning operating system, not a personality imitation. When the skill is active, the agent runs the same moves Musk uses on your actual problem and finishes with a decision and a next-24-hours action.

Works with any model. Small, editable, composable. Hack on it and make it your own.

## Installation (30-second setup)

A plugin updates itself. [skills.sh](https://skills.sh/angelobaricante/elons-brain) copies editable files into your project, and you update them by hand. Pick one per agent, because installing both gives you the skill twice.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add angelobaricante/elons-brain
claude plugin install elons-brain@angelobaricante
```

Updates itself by default.

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add angelobaricante/elons-brain
codex plugin add elons-brain@angelobaricante
```

Updates itself at startup.

</details>

<details>
<summary><strong>GitHub Copilot</strong> (CLI and VS Code)</summary>

```bash
copilot plugin marketplace add angelobaricante/elons-brain
copilot plugin install elons-brain@angelobaricante
```

Then, once, add to `~/.copilot/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "angelobaricante": { "source": { "source": "github", "repo": "angelobaricante/elons-brain" }, "autoUpdate": true }
  }
}
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/angelobaricante/elons-brain`. It updates daily.

</details>

<details>
<summary><strong>Gemini CLI</strong> (manual updates)</summary>

```bash
gemini skills install https://github.com/angelobaricante/elons-brain.git --path skills/thinking
```

Re-run to update.

</details>

<details>
<summary><strong>Any other agent, or editable files</strong> (manual updates)</summary>

```bash
npx skills@latest add angelobaricante/elons-brain -a <agent>  # cursor, opencode, devin, windsurf, amp, pi; omit -a to choose
```

To update, run `npx skills@latest update`.

</details>

<details>
<summary><strong>Claude.ai / Claude Desktop</strong></summary>

Download [`skills/thinking/elons-brain/SKILL.md`](./skills/thinking/elons-brain/SKILL.md) and add it from Settings → Skills, or paste the body into a Project's instructions.

</details>

<details>
<summary><strong>Any chat model</strong> (ChatGPT, Gemini, etc.)</summary>

Paste the body of [`SKILL.md`](./skills/thinking/elons-brain/SKILL.md) (everything below the frontmatter) as the system prompt or custom instructions. Section 7, the output template, is what makes the behaviour hold; keep it intact.

</details>

## What it does

- **The stance**: mission first, physics is the only law, progress is not inevitable.
- **First principles** (heaviest weight): James Clear's framing (function over form, deconstruct then reconstruct, reasoning by analogy as the enemy) merged with Musk's rocket math and the idiot index.
- **The Algorithm**: question every requirement, delete, simplify, accelerate, automate, in that order, plus the postscripts (hands-on managers, skip-levels, hire for attitude).
- **Decision making**: decide now, burn-rate time vs money, walk to the red, 24-hour bottleneck meetings, budget for failure.
- **Design and architecture**: the machine that builds the machine, never separate design/engineering/production, fewest parts and connections, vertical integration, steal from toys and nature.
- **Building and operating**: hardcore culture, showmanship is salesmanship, repeat until they mouth the words, frontline general.
- **Output template**: Function, Physics floor, Requirements audit, Delete, Simplify/Accelerate/Automate, Decision, Next 24 hours.

## When it triggers

Hard decisions, system/product/architecture design, build planning, "why is this slow or expensive", "how should I approach this", or explicit asks for first principles, the Algorithm, the idiot index, or to simplify/delete. Also plan audits for bloat, outsourcing, over-automation, or fake requirements. You can always invoke it directly with `/elons-brain`.

## Reference

### Thinking

Reasoning frameworks for decisions, designs, and builds. See [skills/thinking](./skills/thinking/README.md).

**Model-invoked** (model- or user-reachable):

- **[elons-brain](./skills/thinking/elons-brain/SKILL.md)**: Run a problem through first principles, the five-step Algorithm, the idiot index, and Musk-style decision making. Ends with a decision and a next-24-hours action.

## Sources

- Walter Isaacson, *Elon Musk* (2023), via the Founders Podcast episode on the book's company-building principles.
- James Clear, [First Principles: Elon Musk on the Power of Thinking for Yourself](https://jamesclear.com/first-principles).

## License

MIT

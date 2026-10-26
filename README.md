# Jobs + Musk Brain

A source-grounded reasoning skill combining documented ideas from Steve Jobs and Elon Musk for product strategy, feature engineering, hiring, leadership, and presentations.

It connects **source evidence → interpreted principle → project facts → recommendation → validation**. Founder statements, narrated recollections, our synthesis, and predictions stay distinct. Facts inform a decision; uncertain outcomes remain hypotheses to test.

One plugin, one skill: `jobs-musk-brain`. Reference cards and workflows are internal resources, not separate commands.

## Installation (30-second setup)

A plugin updates itself. [skills.sh](https://skills.sh/angelobaricante/jobs-musk-brain) copies editable files into your project, and you update them by hand. Pick one per agent, because installing both gives you the skill twice.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add angelobaricante/jobs-musk-brain
claude plugin install jobs-musk-brain@angelobaricante
```

Updates itself by default.

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add angelobaricante/jobs-musk-brain
codex plugin add jobs-musk-brain@angelobaricante
```

Updates itself at startup.

</details>

<details>
<summary><strong>GitHub Copilot</strong> (CLI and VS Code)</summary>

```bash
copilot plugin marketplace add angelobaricante/jobs-musk-brain
copilot plugin install jobs-musk-brain@angelobaricante
```

Then, once, add to `~/.copilot/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "angelobaricante": { "source": { "source": "github", "repo": "angelobaricante/jobs-musk-brain" }, "autoUpdate": true }
  }
}
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/angelobaricante/jobs-musk-brain`. It updates daily.

</details>

<details>
<summary><strong>Gemini CLI</strong> (manual updates)</summary>

```bash
gemini skills install https://github.com/angelobaricante/jobs-musk-brain.git --path skills/thinking
```

Re-run to update.

</details>

<details>
<summary><strong>Any other agent, or editable files</strong> (manual updates)</summary>

```bash
npx skills@latest add angelobaricante/jobs-musk-brain -a <agent>  # cursor, opencode, devin, windsurf, amp, pi; omit -a to choose
```

To update, run `npx skills@latest update`.

</details>

<details>
<summary><strong>Claude.ai / Claude Desktop</strong></summary>

Upload the complete [`jobs-musk-brain` skill folder](./skills/thinking/jobs-musk-brain), including `references/`, using your host's skill-file support. The main file depends on its bundled evidence and workflows; uploading it alone omits that material.

</details>

<details>
<summary><strong>Any chat model</strong> (ChatGPT, Gemini, etc.)</summary>

Provide the body of [`SKILL.md`](./skills/thinking/jobs-musk-brain/SKILL.md) together with the files in [`references/`](./skills/thinking/jobs-musk-brain/references). A host without file access needs that reference text in its context. The original attachments are not required for runtime use.

</details>

## What it does

- Establishes a shared outcome, constraints, and evidence of success.
- Selects relevant Jobs and Musk principle cards with traceable attribution.
- Applies them to current project evidence and exposes consequential assumptions.
- Produces one recommendation, its tradeoff, and an observable next test or acceptance check.
- Supports product/feature work, cost and architecture reviews, hiring, leadership, and presentations.

The combined decision process is our synthesis. It does not claim either founder endorsed a modern feature, tool, or decision. A citation proves neither customer demand nor engineering correctness.

## When to use it

Ask for Jobs's approach, Musk's approach, their combined perspective, or a source-grounded review of product focus, experience, requirements, cost, or execution. In Codex, mention `$jobs-musk-brain`; in ChatGPT, type `@` and select the skill once installed. See [official invocation guidance](https://learn.chatgpt.com/docs/build-skills). Responses scale to the decision rather than following a fixed seven-part template.

## One skill, one entry point

```text
$jobs-musk-brain Help me decide which feature to build next.
```

Codex uses `$` skill mentions; its CLI and IDE also offer `/skills` for selection. ChatGPT uses `@` selection. The punctuation comes from the host, not a separate skill. Product, engineering, hiring, leadership, and presentation work all use this same entry point; there are no separate Jobs and Musk commands. See [official OpenAI guidance](https://learn.chatgpt.com/docs/build-skills).

This repository includes a `.agents/skills/jobs-musk-brain` symlink to the packaged skill for local Codex discovery. If the skill does not appear, restart Codex. In other projects, install the renamed package first. Remove an old `elons-brain` installation when migrating to avoid retaining both versions. The new ID is a deliberate breaking rename; an existing installation under the old ID should not be assumed to migrate automatically.

## Reference

### Thinking

Reasoning frameworks for decisions, designs, and builds. See [skills/thinking](./skills/thinking/README.md).

**Model-invoked** (also user-reachable):

- **[jobs-musk-brain](./skills/thinking/jobs-musk-brain/SKILL.md)**: A combined Jobs–Musk decision process backed by source cards and project evidence.

## Evidence and architecture

- [Architecture](./docs/ARCHITECTURE.md): responsibilities, evidence contract, tradeoffs, workflows, and release criteria.
- [Principle cards](./skills/thinking/jobs-musk-brain/references/principles.md): 14 supported claims, applications, and limits.
- [Source register](./skills/thinking/jobs-musk-brain/references/sources.json): public sources and supplied-transcript identities.
- [Jobs research](./docs/research/): passage-level notes and duplicate assessment for all eight supplied attachments.
- [Decision](./docs/adr/0001-evidence-grounded-combined-brain.md): why this remains one skill.

Seven supplied files contain exact repeated halves; two versions cover the same underlying commentary. Several are narrated book discussions rather than direct Jobs interviews. Selected claims were checked against the Steve Jobs Archive, Apple announcements, and other primary records. Musk coverage currently comes from a primary oral-history transcript and the interviewer team's Starbase account. Verification is passage-specific, not a blanket endorsement of every historical anecdote.

Original transcripts are not bundled. Their identities and hashes support maintenance; source availability and redistribution rights remain separate matters. The MIT license covers this repository's original instructions and adaptations, not third-party source works.

## Validation

```bash
python3 scripts/validate.py
python3 scripts/validate.py --attachments  # optional: requires the original supplied files
claude plugin validate .
```

[Behavioral evaluation cases](./skills/thinking/jobs-musk-brain/evaluations/cases.json) cover attribution, uncertainty, feature reasoning, hiring, leadership, and presentations. See [evaluation instructions](./skills/thinking/jobs-musk-brain/evaluations/README.md). Structural validation does not establish model compliance; record fresh-session outputs before claiming behavioral validation.

## License

MIT

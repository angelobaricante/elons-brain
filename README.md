# Jobs + Musk Brain

**Bring documented ideas from Steve Jobs and Elon Musk into your next product, engineering, or business decision.**

Jobs + Musk Brain is a skill for your AI assistant. Give it a problem, your constraints, and whatever evidence you have. It helps you sharpen the goal, challenge assumptions, simplify the plan, and choose a concrete next step.

It combines ideas about product experience, focus, first-principles reasoning, and execution. Its recommendations connect the founders' documented ideas to **your actual situation**, with sources and assumptions made visible.

**One plugin. One skill. One entry point: `jobs-musk-brain`.**

## What can I use it for?

| Your situation | What to ask |
| --- | --- |
| Too many feature ideas | Which feature should we build first, and what should we leave out? |
| A confusing product experience | How can we make the core task easier to understand and complete? |
| A costly or complicated system | Which requirements are necessary, and where is the real bottleneck? |
| A hiring or leadership decision | What evidence do we need, and how do we make room for honest feedback? |
| A launch or presentation | What is the central customer benefit, and how can we demonstrate it honestly? |

## Try it

After installing, use this in Codex:

```text
$jobs-musk-brain Review my product idea. Help me identify the core user
problem, challenge unnecessary features, and choose the smallest useful
experiment. Separate facts from assumptions and cite the principles you use.
```

Or bring it a specific task:

```text
$jobs-musk-brain We have two engineers and two weeks. Review this feature
plan, recommend what to cut, and define how we will know the result works.
```

Share your goal, intended users, current plan or repository, constraints, and any research or measurements. If you do not have evidence yet, the skill should identify what to learn next.

In **ChatGPT**, type `@` and select the installed **Jobs + Musk Brain** skill. In **Codex**, use a `$` skill mention; its CLI and IDE also provide `/skills` for selection. These are different ways to reach the same skill. [Official invocation guidance](https://learn.chatgpt.com/docs/build-skills).

## What should I expect back?

A recommendation you can inspect and act on:

1. **A clear goal:** what you are trying to achieve and the constraints that matter.
2. **Relevant principles:** which documented ideas apply, with source links.
3. **Reasoning:** how those ideas connect to your evidence, alternatives, and tradeoffs.
4. **A next step:** what to build, change, measure, or test—and what would change the decision.

Small questions get short answers. Feature work can produce a brief with scope and acceptance checks. The references and workflows live inside the skill; you do not need separate Jobs, Musk, hiring, or presentation commands.

## Install

Choose one installation route per host to avoid duplicate copies.

<details>
<summary><strong>ChatGPT</strong></summary>

Use an installed private or workspace copy of the plugin, then select **Jobs + Musk Brain** with `@`. On its plugin page, select the install/plus button if it is not already installed, then start a new chat.

A Codex CLI installation does not by itself install a plugin in your ChatGPT account. This repository is source code, not a public ChatGPT directory listing. For a private copy, package the skill and its references using the [OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins) and your account's supported creation/import flow. Workspace administrators can also import a GitHub marketplace. See [installation guidance](https://learn.chatgpt.com/docs/plugins).

</details>

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

## Updating or migrating

For Codex, refresh this marketplace and install the current package:

```bash
codex plugin marketplace upgrade angelobaricante
codex plugin add jobs-musk-brain@angelobaricante
```

This project was previously named `elons-brain`. The repository and skill are now `jobs-musk-brain`. Existing installations under the old ID need migration; remove the old copy when moving over. If Codex reports that the `angelobaricante` marketplace already uses a different source, replace that registration with the repository URL above.

Cloning this repo also exposes the skill through `.agents/skills/jobs-musk-brain` for local Codex discovery. Installing a second copy can produce duplicate entries. If a newly installed skill does not appear, restart the host. ChatGPT account copies and GitHub/Codex copies are managed separately.

## How the evidence works

The skill includes **14 principle cards**. Each records a supported claim, its source, a proposed application, and its limits. Sources include the Steve Jobs Archive, Apple announcements, a Musk oral-history interview, an interviewer-team account, and supplied book-commentary transcripts. Narrated recollections stay labeled as such; repeated transcripts do not count as independent support.

The combined decision process is this project's synthesis. It does not claim either founder endorsed your feature or modern technology choice. A historical statement can inform a decision; it cannot prove customer demand, predict success, or replace testing your implementation.

## Explore the project

- [Skill instructions](./skills/thinking/jobs-musk-brain/SKILL.md) — the single entry point.
- [Principle cards](./skills/thinking/jobs-musk-brain/references/principles.md) and [source register](./skills/thinking/jobs-musk-brain/references/sources.json) — inspect the evidence.
- [Workflows](./skills/thinking/jobs-musk-brain/references/workflows.md) — product, engineering, hiring, leadership, and presentations.
- [Architecture](./docs/ARCHITECTURE.md) and [design decision](./docs/adr/0001-evidence-grounded-combined-brain.md) — understand the design.
- [Research notes](./docs/research/) — source locators, attribution limits, and duplicate analysis.
- [Thinking skills](./skills/thinking/README.md) — skill index.

## Validation and current status

Package checks and targeted source reviews have passed. **The 13 behavioral evaluation cases have not yet been run in fresh model sessions.** The skill's consistency and effectiveness have not been established by those structural checks. See the [validation record](./docs/VALIDATION.md) and [evaluation instructions](./skills/thinking/jobs-musk-brain/evaluations/README.md).

```bash
python3 scripts/validate.py
claude plugin validate .
```

Maintainers with the original supplied files can additionally run `python3 scripts/validate.py --attachments` to check their hashes and duplication records.

## License

MIT for this repository's original instructions and adaptations. Third-party source works retain their own rights; the original supplied transcripts are not bundled.

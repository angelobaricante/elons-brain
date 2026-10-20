Skills live in bucket folders under `skills/`:

- `thinking/`: reasoning frameworks for decisions, designs, and builds

Every skill in a promoted bucket must have a reference in the top-level `README.md` (name linked to its `SKILL.md`) and an entry in `.claude-plugin/plugin.json`'s `skills` array. The Claude Code plugin ships exactly that set.

Each bucket folder has a `README.md` listing every skill in it with a one-line description, grouped into **User-invoked** and **Model-invoked**.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` in frontmatter plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`) or model-invoked (the default; `agents/openai.yaml` carries only `interface`).

`.claude-plugin/marketplace.json` is the repo's own marketplace. Codex and Copilot install from it to get automatic updates. Run `claude plugin validate .` after touching either manifest. Bump `version` in `plugin.json` on every change that should reach installed users; managed installs only reinstall when that field changes.

Install commands in `README.md` are the single source of truth for install wording. Change them there, then propagate anywhere else they appear.

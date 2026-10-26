#!/usr/bin/env python3
"""Check package references and evidence structure, not historical truth or model behavior."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--attachments', action='store_true', help='also verify original supplied files')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    manifest = json.loads((root / '.claude-plugin/plugin.json').read_text())
    marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
    check(manifest['name'] == marketplace['plugins'][0]['name'], 'plugin identities differ')
    registered = {(root / path).resolve() for path in manifest['skills']}
    discovered = {path.parent.resolve() for path in (root / 'skills').rglob('SKILL.md')}
    check(registered == discovered, 'skill registration differs from discovered skills')
    for folder in registered:
        discovery = root / '.agents/skills' / folder.name
        check(discovery.is_symlink() and discovery.resolve() == folder,
              f'{folder.name}: local Codex discovery link is missing or points elsewhere')

    for folder in registered:
        skill_text = (folder / 'SKILL.md').read_text()
        check(skill_text.startswith('---\n'), f'{folder.name}: missing frontmatter')
        check(f'name: {folder.name}\n' in skill_text, f'{folder.name}: mismatched skill name')
        check('description: ' in skill_text, f'{folder.name}: missing description')
        check((folder / 'agents/openai.yaml').exists(), f'{folder.name}: missing UI metadata')
        check(f'./{folder.relative_to(root)}/SKILL.md' in (root / 'README.md').read_text(), 'missing top-level skill reference')
        check(f'./{folder.name}/SKILL.md' in (folder.parent / 'README.md').read_text(), 'missing bucket skill reference')

        source_rows = json.loads((folder / 'references/sources.json').read_text())['sources']
        sources = {source['id']: source for source in source_rows}
        check(len(sources) == len(source_rows), 'duplicate source IDs')
        for source in source_rows:
            for field in ('id', 'kind', 'verification', 'independence_group'):
                check(bool(source.get(field)), f'{source.get("id")}: missing {field}')
            check(bool(source.get('url') or source.get('attachment_id')), f'{source["id"]}: missing locator')
            if source.get('url'):
                check(urlsplit(source['url']).scheme == 'https', f'{source["id"]}: expected public HTTPS source')

        text = (folder / 'references/principles.md').read_text()
        cards = re.findall(r'^## ((?:JOBS|MUSK)-[A-Z]+) — .*?\n(.*?)(?=^## |\Z)', text, re.M | re.S)
        card_ids = {card_id for card_id, _ in cards}
        check(len(card_ids) == len(cards), 'duplicate principle IDs')
        for card_id, body in cards:
            for label in ('Supported claim', 'Evidence', 'Application', 'Limit'):
                check(f'**{label}:**' in body, f'{card_id}: missing {label}')
            evidence = body.split('**Evidence:**', 1)[-1].split('**Application:**', 1)[0]
            ids = re.findall(r'\b(?:J\d{2}|SJA|AIPOD|ASAFARI|STANFORD|MS1997|MHF|MEA)\b', evidence)
            check(bool(ids), f'{card_id}: no registered evidence')
            for source_id in ids:
                check(source_id in sources, f'{card_id}: unknown source {source_id}')

        for file in folder.rglob('*.md'):
            for card_id in set(re.findall(r'\b(?:JOBS|MUSK)-[A-Z]+\b', file.read_text())):
                check(card_id in card_ids, f'{file.name}: unknown principle {card_id}')

        cases = json.loads((folder / 'evaluations/cases.json').read_text())['cases']
        check(len({case['id'] for case in cases}) == len(cases), 'duplicate evaluation IDs')
        covered = set()
        for case in cases:
            check(bool(case['prompt'] and case['must_demonstrate'] and case['hard_failures']), f'{case["id"]}: incomplete evaluation')
            covered.update(case['relevant_principles'])
        check(covered <= card_ids, 'evaluations reference unknown principles')
        check(card_ids <= covered, f'principles without evaluation coverage: {sorted(card_ids - covered)}')

    for file in list(root.rglob('*.md')):
        if '.git' in file.parts:
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file.read_text()):
            if urlsplit(link).scheme or link.startswith(('#', '/')):
                continue
            target = unquote(link.split('#')[0])
            check((file.parent / target).exists(), f'{file.relative_to(root)}: broken local link {target}')

    if args.attachments:
        for source in json.loads((root / 'docs/research/attachments.json').read_text()):
            path = Path(source['original_path'])
            if not path.exists():
                errors.append(f'{source["id"]}: original attachment unavailable')
                continue
            raw = path.read_bytes()
            check(hashlib.sha256(raw).hexdigest() == source['sha256'], f'{source["id"]}: attachment hash differs')
            lines = raw.decode().splitlines()
            half = len(lines) // 2
            repeated = len(lines) % 2 == 0 and lines[:half] == lines[half:]
            check(repeated == source['exact_repeated_halves'], f'{source["id"]}: duplicate assessment differs')

    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS: package links, source/card structure, and evaluation coverage' + ('; attachment integrity' if args.attachments else ''))
    print('Historical accuracy and runtime model behavior are not established by this check.')


if __name__ == '__main__':
    main()

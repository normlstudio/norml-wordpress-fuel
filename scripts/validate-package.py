#!/usr/bin/env python3
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
expected={'norml-wordpress-fuel','norml-wp-connect','norml-wp-developer'}
actual={p.parent.name for p in (root/'.claude/skills').glob('*/SKILL.md')}
assert actual==expected,(actual,expected)
errors=[]
for skill in sorted(expected):
    folder=root/'.claude/skills'/skill
    for required in ['SKILL.md','install.md','changelog.md','readme.md','readme.data.json','readme.html']:
        if not (folder/required).is_file():errors.append(f'{skill}: missing {required}')
    for p in folder.rglob('*.md'):
        text=p.read_text()
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if not re.match(r'[a-z]+:',link) and not link.startswith('#'):
                target=p.parent/link.split('#')[0]
                if not target.exists():errors.append(f'{p.relative_to(root)}: broken {link}')
        for forbidden in ['/Users/','Norml Drive/','keychain-service: norml','ssh norml-']:
            if forbidden in text:errors.append(f'{p.relative_to(root)}: private dependency')
if errors:raise SystemExit('\n'.join(errors))
print('PASS: three complete packages, local links and private-dependency checks')

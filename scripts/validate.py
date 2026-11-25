#!/usr/bin/env python3
"""校验 skills：frontmatter 完整、name 与目录一致、路由表与场景 skill 一一对应。"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "skills"
COMMON = "anti-defensive"
errors = []


def frontmatter(path: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    return dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)


skill_dirs = sorted(p for p in ROOT.iterdir() if p.is_dir())
for d in skill_dirs:
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: 缺少 SKILL.md")
        continue
    fm = {k.strip(): v.strip() for k, v in frontmatter(f).items()}
    if fm.get("name") != d.name:
        errors.append(f"{d.name}: frontmatter name={fm.get('name')!r} 与目录名不一致")
    if not fm.get("description"):
        errors.append(f"{d.name}: 缺少 description")
    if d.name != COMMON and f"../{COMMON}/SKILL.md" not in f.read_text(encoding="utf-8"):
        errors.append(f"{d.name}: 未引用通用原则 ../{COMMON}/SKILL.md")

domains = {d.name for d in skill_dirs if d.name != COMMON}
router = (ROOT / COMMON / "SKILL.md").read_text(encoding="utf-8")
routed = set(re.findall(r"\|\s*`(anti-defensive-[\w-]+)`\s*\|", router))
for name in sorted(domains - routed):
    errors.append(f"路由表缺少场景: {name}")
for name in sorted(routed - domains):
    errors.append(f"路由表指向不存在的场景: {name}")

if errors:
    print("\n".join(f"✗ {e}" for e in errors))
    sys.exit(1)
print(f"✓ {len(skill_dirs)} 个 skill 通过校验，路由表覆盖 {len(routed)} 个场景")

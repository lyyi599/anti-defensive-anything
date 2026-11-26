#!/usr/bin/env python3
"""仓库一致性校验（只用标准库）。CI 和本地都运行它。

检查：
  1. 每个 skill：SKILL.md 存在、frontmatter 有 name/description、name 与目录一致
  2. 场景 skill 引用了通用原则 ../anti-defensive/SKILL.md
  3. 路由表与场景 skill 目录一一对应
  4. plugin.json 与 marketplace.json 的版本号一致，CHANGELOG 有该版本条目
  5. 译文是否过时（只警告，不失败）：见 scripts/translate.py
  6. 每个场景至少有一个评估用例（evals/<场景>-*/）
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
COMMON = "anti-defensive"
errors = []


def frontmatter(path: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    return {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)}


# 1-2. skills
skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
for d in skill_dirs:
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: 缺少 SKILL.md")
        continue
    fm = frontmatter(f)
    if fm.get("name") != d.name:
        errors.append(f"{d.name}: frontmatter name={fm.get('name')!r} 与目录名不一致")
    if not fm.get("description"):
        errors.append(f"{d.name}: 缺少 description")
    if d.name != COMMON and f"../{COMMON}/SKILL.md" not in f.read_text(encoding="utf-8"):
        errors.append(f"{d.name}: 未引用通用原则 ../{COMMON}/SKILL.md")

# 3. router
domains = {d.name for d in skill_dirs if d.name != COMMON}
router = (SKILLS / COMMON / "SKILL.md").read_text(encoding="utf-8")
routed = set(re.findall(r"\|\s*`(anti-defensive-[\w-]+)`\s*\|", router))
errors += [f"路由表缺少场景: {n}" for n in sorted(domains - routed)]
errors += [f"路由表指向不存在的场景: {n}" for n in sorted(routed - domains)]

# 4. version
plugin = json.loads((REPO / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
market = json.loads((REPO / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
version = plugin.get("version")
for entry in market.get("plugins", []):
    if entry.get("name") == plugin.get("name") and entry.get("version") != version:
        errors.append(f"版本号不一致: plugin.json={version} marketplace.json={entry.get('version')}")
changelog = REPO / "CHANGELOG.md"
if not changelog.exists() or not re.search(rf"^## \[?{re.escape(str(version))}\]?", changelog.read_text(encoding="utf-8"), re.M):
    errors.append(f"CHANGELOG.md 缺少当前版本 {version} 的条目")


# 5. translations: stale translations are a warning, not an error
sys.path.insert(0, str(REPO / "scripts"))
from translate import PAIRS, REASON, status  # noqa: E402

warnings = []
for src, dst, _ in PAIRS:
    state, _, _ = status(src, dst)
    if state != "ok":
        warnings.append(f"译文 {dst} 需要重新生成：{REASON[state]}（源文件 {src}）。运行 python3 scripts/translate.py")

# 6. evals
evals = REPO / "evals"
for name in sorted(domains):
    short = name[len(COMMON) + 1:]
    if not any(evals.glob(f"{short}-*/prompt.md")):
        errors.append(f"场景 {short} 没有评估用例（evals/{short}-*/prompt.md）")

for w in warnings:
    print(f"⚠ {w}")
if errors:
    print("\n".join(f"✗ {e}" for e in errors))
    sys.exit(1)
print(f"✓ {len(skill_dirs)} 个 skill，路由 {len(routed)} 个场景，版本 {version}，评估用例齐全")

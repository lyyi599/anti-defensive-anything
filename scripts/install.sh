#!/usr/bin/env bash
# 安装 anti-defensive skills。
# 用法：
#   scripts/install.sh                      # 复制全部到 ~/.claude/skills
#   scripts/install.sh --link               # 软链接（仓库更新后自动生效）
#   scripts/install.sh --target DIR         # 指定目录，如 ~/.codex/skills 或 ./.claude/skills
#   scripts/install.sh coding writing       # 只装指定场景（common 总会被安装）
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
target="$HOME/.claude/skills"
mode=copy
domains=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --link) mode=link ;;
    --target) target="$2"; shift ;;
    -h|--help) sed -n '2,7p' "$0"; exit 0 ;;
    *) domains+=("$1") ;;
  esac
  shift
done

if [[ ${#domains[@]} -eq 0 ]]; then
  skills=("$repo"/skills/*/)
else
  skills=("$repo/skills/anti-defensive/")
  for d in "${domains[@]}"; do
    src="$repo/skills/anti-defensive-$d/"
    [[ -d "$src" ]] || { echo "未知场景: $d" >&2; exit 1; }
    skills+=("$src")
  done
fi

mkdir -p "$target"
for src in "${skills[@]}"; do
  name="$(basename "$src")"
  dst="$target/$name"
  rm -rf "$dst"
  if [[ $mode == link ]]; then ln -s "${src%/}" "$dst"; else cp -r "$src" "$dst"; fi
  echo "$mode: $name -> $dst"
done

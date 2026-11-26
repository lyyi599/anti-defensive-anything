#!/usr/bin/env bash
# Install the anti-defensive skills.
# Usage:
#   scripts/install.sh                      # copy everything into ~/.claude/skills
#   scripts/install.sh --link               # symlink instead (picks up repo updates automatically)
#   scripts/install.sh --target DIR         # another directory, e.g. ~/.codex/skills or ./.claude/skills
#   scripts/install.sh coding writing       # only these scenes (the core skill is always installed)
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
    [[ -d "$src" ]] || { echo "unknown scene: $d" >&2; exit 1; }
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

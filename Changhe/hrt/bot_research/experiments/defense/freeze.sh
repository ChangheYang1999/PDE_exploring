#!/bin/bash
# Freeze the defense package for a tournament: copies bot_research/bots/defense/*.py into
# bot_research/bots/defense/frozen/<tag>/ (a package; relative imports keep working) and records hashes.
# Usage: bash bot_research/experiments/defense/freeze.sh <tag>      (from the project root)
# Spec for the frozen bot: bot_research.bots.defense.frozen.<tag>.fortress:@make
set -e
tag="$1"
[ -n "$tag" ] || { echo "usage: freeze.sh <tag>"; exit 2; }
src=bot_research/bots/defense
dst=$src/frozen/$tag
mkdir -p $src/frozen
[ -f $src/frozen/__init__.py ] || echo '"""Frozen snapshots of the defense package for tournaments (never edited)."""' > $src/frozen/__init__.py
[ -e "$dst" ] && { echo "exists: $dst"; exit 3; }
mkdir -p "$dst"
cp $src/*.py "$dst"/
( cd "$dst" && sha256sum *.py ) > "$dst/SHA256SUMS"
echo "frozen $tag:"; cat "$dst/SHA256SUMS" | cut -c1-16,66-

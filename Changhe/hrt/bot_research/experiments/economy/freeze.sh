#!/bin/bash
# Usage: freeze.sh TAG  -> copies bots/economy/*.py to bots/economy/frozen/TAG/
# Spec of the frozen bot: bot_research.bots.economy.frozen.TAG.econ:@make
set -e
D="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../bots/economy" && pwd)"
T="$D/frozen/$1"
if [ -e "$T" ]; then echo "exists: $T"; exit 1; fi
mkdir -p "$T"
cp "$D"/*.py "$T"/
sha256sum "$T"/*.py | sed "s#$D/##" > "$T/SHA256SUMS"
echo "frozen $1"

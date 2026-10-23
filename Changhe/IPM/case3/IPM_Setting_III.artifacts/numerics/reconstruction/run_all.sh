#!/bin/bash
# produces RECONSTRUCTION_OUTPUT.txt and SHA256SUMS.txt
cd "$(dirname "$0")"
sha256sum states/*.pt > SHA256SUMS.txt
: > RECONSTRUCTION_OUTPUT.txt
for f in states/*.pt; do echo "=================== $f  ($(date -u +%FT%TZ))" >> RECONSTRUCTION_OUTPUT.txt; timeout 900 python3 load_state.py "$f" --device cuda >> RECONSTRUCTION_OUTPUT.txt 2>&1; done
echo "DONE $(date -u +%FT%TZ)" >> RECONSTRUCTION_OUTPUT.txt

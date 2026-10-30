#!/bin/bash
set -eu
date -u +%Y-%m-%dT%H:%M:%SZ
python3 -B research/new_candidate_witness/code/reproduce.py C1-N1-007-d2w-j7-e2bal
python3 -B research/projected_mode_audit/code/check.py C1-N1-007-d2w-j7-e2bal
python3 -B research/localized_probe_audit/code/reproduce.py C1-N1-007-d2w-j7-e2bal --k 0 128 512 1024 --bits 2048
python3 -B research/background_norm_reproduction/code/reproduce_new_candidate.py C1-N1-007-d2w-j7-e2bal
date -u +%Y-%m-%dT%H:%M:%SZ

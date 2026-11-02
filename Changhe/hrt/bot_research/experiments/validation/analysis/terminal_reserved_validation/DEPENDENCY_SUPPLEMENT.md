# Later pre-D dependency seal

The independent readiness review identified executable subprocess dependencies outside candidate declaration001's 85-file source/data map. This supplement preserves that declaration and all pinned files. It records a separate actual timestamp before the 23:00 UTC gate, pins the full local static closure from explicit subprocess entry modules, and snapshots the newly covered files plus the supplemental verifier. The seal receipt supplies the actual timestamp and hashes; this document does not backdate them.

The retained declaration SHA256 is `2b5fa9c56b6219233731c8559b012ff12ebe0be43b86395ebee4e51b8fa325e1`. The selected candidate remains SHA256 `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`. No candidate, opponent, pipeline, engine or configuration source is modified by sealing.

`terminal_dependency_supplement.py` uses an explicit root list for the pipeline, its subprocess entry modules, the logging wrapper and the legacy final-validation root referenced by `job_source_roots`. It then uses static import analysis, without importing bot modules. The union with the original 85 pins includes the reserve manifest and prefix evidence as opaque hashed bytes. The tool parses only declaration and earlier receipt metadata. It makes no policy calls or games and does not inspect reserved parameters.

The current bytes of eight omitted dependencies are compared with selected earlier receipt pins. Where those receipts contain source archives, their original archived bytes are also checked. Receipt copies and newly covered source bytes are retained under `verification/dependency_supplement_sources/`. The logging wrapper and the new supplemental verifier have no selected earlier pin in this check. Earlier matching hashes establish identity with those earlier records, not continuous monitoring between them.

The original declaration and scheduled pipeline are unchanged. The pipeline does not automatically consume this supplement. Therefore the publication should retain the seal plus successful independent pre-D and post-D verification receipts. A post-D receipt checks source identity after the gate; it does not itself assert game completion. Full 96-condition results, replay, entry-form checks and the final protected-file inventory remain separate requirements.

Run from the project root, with the existing environment, bytecode disabled, the research temporary directory, one assigned low-priority CPU and one numerical thread. Sealing is exclusive and refuses to start or finish after the gate. Verification never changes the seal or archived inputs, and every receipt must use a new filename.

```sh
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 taskset -c 30 .venv/bin/python -B -m bot_research.experiments.validation.terminal_dependency_supplement seal

PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 taskset -c 30 .venv/bin/python -B -m bot_research.experiments.validation.terminal_dependency_supplement verify --phase pre-d --output bot_research/experiments/validation/analysis/terminal_reserved_validation/verification/dependency_supplement_pre_d_001.json

PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 taskset -c 30 .venv/bin/python -B -m bot_research.experiments.validation.terminal_dependency_supplement verify --phase post-d --output bot_research/experiments/validation/analysis/terminal_reserved_validation/verification/dependency_supplement_post_d_001.json
```

A mismatch leaves the supplemental provenance check OPEN or REFUTED according to the retained issue. Preserve the failed receipt and explain any separate amendment. Do not rewrite a pinned file to make the check pass. This source supplement provides no additional strength samples or claim of optimal play.

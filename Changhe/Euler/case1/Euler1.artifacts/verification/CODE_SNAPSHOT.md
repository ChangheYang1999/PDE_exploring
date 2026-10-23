# Source and checkpoint provenance

The checkpoint supervisor now captures checkpoint.py, core.py, evaluate.py and models.py before launching a numerical child. Each source set is stored in snapshots/validator-code-HASH/validation, with a full SHA256 manifest in its parent folder. The child runs those frozen files. E1_VER_ROOT points to this lane so that the frozen program writes its ledger and evidence here. Its output records the source directory and file hashes actually used.

Evidence names include checkpoint hash, code hash and scientific configuration hash. The configuration hash covers the holdout seed, sample count and explicit radial-feature override; source path aliases do not create scientifically distinct jobs. Full identifiers, source path, immutable checkpoint path and exit status remain in VALIDATION_COMPLETED.json.

The earliest shift-1 evaluations used live local source files and recorded hashes at numerical interval start. Those records remain archived. They are useful numerical evidence, including the independently matched pilot reference, but the frozen-source protocol gives stronger execution provenance for subsequent evaluations. It does not retroactively change their execution method.

All snapshots and outputs stay inside e1-ver. No git commits or remote publication are used. Metadata Infinity/NaN values are explicitly tagged when decoding checkpoint metadata, rather than emitted as invalid JSON; physical metric nonfiniteness still fails validation.

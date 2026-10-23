# Optional original derivative evidence

The main Git repository contains the accepted278 candidate, complete production
restart dependencies, verification source and numerical summary results. It can
reconstruct the candidate, independently recompute its diagnostics and perform
the unchanged exact-resume gates without this optional artifact.

Use the separate artifact only to inspect the **original** complete derivative
audit matrices and finite-difference probe arrays without recomputing that audit.
It is evidence of a verified descent direction, not a stationarity certificate.
The original audit found that stationarity was **not established**.

| Artifact property | Value |
| --- | --- |
| Filename | `accepted278_derivative_evidence.tar.gz` |
| Archive size | 683,566,328 bytes |
| Regular files | 141 |
| Uncompressed content | 684,792,055 bytes |
| SHA-256 | `a5f353ad887a02c79fc84fe9ff991db922e981849ac83a30361541239c6a3e93` |
| Required to reconstruct current candidate | No |
| Required to recompute independent checks | No |
| Required for complete accepted-state resume | No |

The small machine-readable descriptor is tracked at
[`verification/optional_evidence.json`](../verification/optional_evidence.json).
The archive is deliberately stored outside the Git staging repository in the
sibling `github_handoff_artifacts_20261023/` directory. Its companions are:

```text
accepted278_derivative_evidence.tar.gz.metadata.json
accepted278_derivative_evidence.tar.gz.files.json
accepted278_derivative_evidence.tar.gz.sha256
```

The `.files.json` companion records the relative path, exact byte count and
SHA-256 of every included file. The archive expands under `stationarity/`,
including original analytic matrices, directional tests, independent baseline
checks, descent probes and their checkpoint bindings. Original absolute paths
inside those audit records are retained as provenance; extraction does not
install them as current-machine dependencies or overwrite the current
production workspace.

## Optional transfer and verification

Attach the archive and all three companions as separate release assets or
transfer them by another file channel. They are not Git-tracked and no asset
upload or GitHub push has been performed by this packaging task.

After obtaining those four files, choose their actual containing directory and
an unused extraction directory outside the Git checkout:

```sh
export ARTIFACT_DIR=/absolute/path/to/downloaded/assets
export EVIDENCE="$HOME/ipm_checks/original_accepted278_derivative_evidence"
cd "$ARTIFACT_DIR"
sha256sum -c accepted278_derivative_evidence.tar.gz.sha256
mkdir -p "$(dirname "$EVIDENCE")"
mkdir "$EVIDENCE"
tar -xzf accepted278_derivative_evidence.tar.gz -C "$EVIDENCE"
```

On macOS, substitute `shasum -a 256 -c` for `sha256sum -c`. Independently verify
all extracted files using only the Python standard library:

```sh
python3 - "$ARTIFACT_DIR/accepted278_derivative_evidence.tar.gz.files.json" "$EVIDENCE" <<'PY'
import hashlib, json, sys
from pathlib import Path
manifest = json.loads(Path(sys.argv[1]).read_text())
root = Path(sys.argv[2]).resolve()
for row in manifest['files']:
    path = (root / row['path']).resolve()
    if root not in path.parents:
        raise SystemExit('Unexpected extraction path: ' + row['path'])
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    if path.stat().st_size != row['bytes'] or h.hexdigest() != row['sha256']:
        raise SystemExit('Evidence mismatch: ' + row['path'])
print('PASS:', len(manifest['files']), 'original evidence files')
PY
```

These are original Mac Pro numerical arrays. They do **not** qualify the native
Python/NumPy/SciPy/BLAS environment of a new Linux server. Install native Linux
dependencies and run the fresh checks in [DEPLOY_LINUX.md](DEPLOY_LINUX.md)
before resuming; never copy a Mac virtual environment or treat archived passing
logs as newly measured Linux results. The main repository supplies the source
needed to regenerate the independent tests. Neither extracting this artifact
nor checking its hashes launches optimization.

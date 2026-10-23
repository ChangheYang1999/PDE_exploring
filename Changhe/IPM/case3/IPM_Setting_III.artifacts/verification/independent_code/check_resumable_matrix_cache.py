"""Crash-resume and corruption tests, confined to this lane's evidence folder."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import tempfile
import time
import numpy as np
from resumable_matrix_cache import MatrixCache

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/resumable_matrix_cache"


def main():
    started = time.monotonic()
    count = 0
    identity = {"geometry": "manufactured-distinct-rows", "algorithm": 1}
    expected = np.arange(42, dtype=np.float64).reshape(7, 6)/7
    with tempfile.TemporaryDirectory(prefix="gate_", dir=OUT) as temp:
        directory = Path(temp)/"matrix"
        cache = MatrixCache(directory, expected.shape, identity)
        assert cache.completed_rows == 0
        cache.arrays[0][:2] = expected[:2]
        cache.arrays[1][:2] = -expected[:2]
        cache.commit(2)
        # Simulate a killed computation after writing, but not committing, a row.
        cache.arrays[0][2] = 123456
        cache.arrays[1][2] = np.nan
        for array in cache.arrays:
            array.flush()
        resumed = MatrixCache(directory, expected.shape, identity)
        assert resumed.completed_rows == 2
        assert np.array_equal(resumed.arrays[0][:2], expected[:2])
        assert np.array_equal(resumed.arrays[1][:2], -expected[:2])
        count += 4
        resumed.arrays[0][2:] = expected[2:]
        resumed.arrays[1][2:] = -expected[2:]
        resumed.commit(5)
        resumed.commit(7)
        final = MatrixCache(directory, expected.shape, identity)
        assert final.completed_rows == 7
        assert np.array_equal(final.arrays[0], expected)
        assert np.array_equal(final.arrays[1], -expected)
        count += 3
        for shape, ident in [
            ((8, 6), identity),
            (expected.shape, identity | {"geometry": "different"}),
            (expected.shape, identity | {"algorithm": 2}),
        ]:
            try:
                MatrixCache(directory, shape, ident)
            except ValueError:
                count += 1
            else:
                raise AssertionError("Changed cache identity was accepted")
        final.arrays[0][0, 0] += 1
        final.arrays[0].flush()
        try:
            MatrixCache(directory, expected.shape, identity)
        except ValueError as exc:
            assert "checksum" in str(exc)
            count += 1
        else:
            raise AssertionError("Committed corruption was accepted")
        invalid = MatrixCache(Path(temp)/"nonfinite", (2, 3), identity)
        invalid.arrays[0][:] = np.nan
        invalid.arrays[1][:] = 0
        try:
            invalid.commit(1)
        except ValueError as exc:
            assert "Nonfinite" in str(exc)
            count += 1
        else:
            raise AssertionError("Nonfinite data committed")
    result = {
        "utc": datetime.now(timezone.utc).isoformat(), "status": "PASS", "checks": count,
        "elapsed_seconds": time.monotonic()-started,
        "source_sha256": {name: hashlib.sha256((ROOT/"independent_code"/name).read_bytes()).hexdigest()
                          for name in ("resumable_matrix_cache.py", "smooth_solver.py",
                                       "check_resumable_matrix_cache.py")},
        "scope": "Persistence and invalidation only; no new numerical solve or inverse validation.",
    }
    (OUT/"GATE.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()

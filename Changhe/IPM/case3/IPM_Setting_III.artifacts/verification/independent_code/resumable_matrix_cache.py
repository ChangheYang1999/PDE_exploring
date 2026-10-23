"""Single-writer committed matrix chunks for expensive independent quadrature.

Data files are flushed before atomic cursor publication. Uncommitted rows are
ignored on resume; hashes of every committed chunk detect accidental corruption.
The caller supplies a complete geometry and implementation identity.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import numpy as np


def digest(value):
    return hashlib.sha256(memoryview(np.ascontiguousarray(value)).cast("B")).hexdigest()


class MatrixCache:
    def __init__(self, directory, shape, identity):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.shape = tuple(int(v) for v in shape)
        if len(self.shape) != 2 or min(self.shape) <= 0:
            raise ValueError("Expected a positive matrix shape")
        self.identity = identity
        self.path = self.directory / "committed.json"
        self.data_paths = [self.directory / name for name in ("ux.npy", "uy.npy")]
        if self.path.exists():
            self.meta = json.loads(self.path.read_text())
            if (self.meta["identity"] != identity or
                    self.meta["shape"] != list(self.shape) or self.meta["schema"] != 1):
                raise ValueError("Matrix cache identity or shape mismatch")
            self.arrays = tuple(np.load(p, mmap_mode="r+", allow_pickle=False) for p in self.data_paths)
            if any(a.shape != self.shape or a.dtype != np.dtype("<f8") for a in self.arrays):
                raise ValueError("Matrix cache array layout mismatch")
            cursor = 0
            for block in self.meta["chunks"]:
                end = block["stop"]
                if block["start"] != cursor or not cursor < end <= self.shape[0]:
                    raise ValueError("Matrix cache chunk coverage mismatch")
                actual = [digest(a[cursor:end]) for a in self.arrays]
                if actual != block["sha256"]:
                    raise ValueError("Committed matrix chunk checksum mismatch")
                cursor = end
            if cursor != self.meta["completed_rows"]:
                raise ValueError("Matrix cache cursor mismatch")
        else:
            # These two fixed names are disposable incomplete files from this
            # cache only. No committed state exists until metadata is published.
            self.arrays = tuple(
                np.lib.format.open_memmap(p, mode="w+", dtype="<f8", shape=self.shape)
                for p in self.data_paths
            )
            self.meta = {
                "schema": 1, "identity": identity, "shape": list(self.shape),
                "completed_rows": 0, "chunks": [],
                "created_utc": datetime.now(timezone.utc).isoformat(),
            }
            self._publish()

    @property
    def completed_rows(self):
        return self.meta["completed_rows"]

    def _publish(self):
        temp = self.path.with_suffix(".pending")
        with temp.open("w") as stream:
            json.dump(self.meta, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, self.path)
        directory_fd = os.open(self.directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)

    def commit(self, stop):
        start = self.completed_rows
        if not isinstance(stop, int) or not start < stop <= self.shape[0]:
            raise ValueError("Invalid matrix commit range")
        if not all(np.all(np.isfinite(a[start:stop])) for a in self.arrays):
            raise ValueError("Nonfinite matrix row")
        hashes = [digest(a[start:stop]) for a in self.arrays]
        for a, path in zip(self.arrays, self.data_paths):
            a.flush()
            with path.open("rb") as stream:
                os.fsync(stream.fileno())
        self.meta["chunks"].append({"start": start, "stop": stop, "sha256": hashes})
        self.meta["completed_rows"] = stop
        self.meta["updated_utc"] = datetime.now(timezone.utc).isoformat()
        self._publish()

"""Standard-library retained-record helpers. No project modules are imported."""
import ast
import collections
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import random

OUT = Path("bot_research/experiments/validation/reviews/economy_final_gate_001")
E = Path("bot_research/experiments/economy")
R = Path("bot_research/runs/economy")


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def relative(path):
    path = Path(path)
    root = Path.cwd()
    path = (path if path.is_absolute() else root / path).relative_to(root)
    if ".." in path.parts:
        raise ValueError("Input path leaves project")
    return path


def json_bytes(value):
    raw = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    if str(Path.cwd()).encode() in raw:
        raise ValueError("Concrete project path in published metadata")
    return raw


class Evidence:
    def __init__(self, name, inspector):
        self.started = now()
        stamp = self.started.translate(str.maketrans("", "", ":-."))
        self.phase = OUT / (name + "-" + stamp)
        self.phase.mkdir(exist_ok=False)
        self.pins = {}
        self.raw = {}
        self.problems = []
        self.versions = {}
        self.inspector = relative(inspector)
        self.capture(self.inspector)
        self.capture(relative(__file__))

    def check(self, condition, message):
        if not condition:
            self.problems.append(message)
        return bool(condition)

    def capture(self, path):
        path = relative(path)
        key = str(path)
        if key not in self.raw:
            observed = now()
            raw = path.read_bytes()
            digest = sha(raw)
            target = OUT / "inputs" / (digest + ".gz")
            if not target.exists():
                with target.open("xb") as stream:
                    stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
            packed = target.read_bytes()
            if gzip.decompress(packed) != raw:
                raise ValueError("Content object mismatch: " + key)
            self.pins[key] = {
                "captured_utc": observed, "sha256": digest, "bytes": len(raw),
                "snapshot": str(target), "gzip_sha256": sha(packed),
            }
            self.raw[key] = raw
        return self.raw[key]

    def retained_map(self, path, expected_sha):
        path = relative(path)
        raw = self.capture(path)
        if sha(raw) != expected_sha:
            raise ValueError("Retained input map digest mismatch")
        inputs = json.loads(raw)["inputs"]
        if any(Path(key).is_absolute() or ".." in Path(key).parts for key in inputs):
            raise ValueError("Nonrelative retained input key")

        def read(key):
            key = str(relative(key))
            pin = inputs[key]
            target = relative(pin["snapshot"])
            packed = target.read_bytes()
            if sha(packed) != pin["gzip_sha256"]:
                raise ValueError("Retained gzip mismatch: " + key)
            raw = gzip.decompress(packed)
            if sha(raw) != pin["sha256"] or len(raw) != pin["bytes"]:
                raise ValueError("Retained raw mismatch: " + key)
            if key in self.raw and self.raw[key] != raw:
                raise ValueError("Two different inputs under one path: " + key)
            self.pins[key] = dict(pin, retained_input_map=str(path))
            self.raw[key] = raw
            return raw
        return read

    def write(self, name, value):
        raw = json_bytes(value)
        with (self.phase / name).open("xb") as stream:
            stream.write(raw)
        return sha(raw)

    def seal(self, result):
        result["started_utc"] = self.started
        result["finished_utc"] = now()
        result["reviewer"] = "GPT-6 Astra"
        result["scope"] = (
            "Supplementary standard-library source/result review only; "
            "no policy, constructor, Engine, game, replay or test calls"
        )
        result["problems"] = self.problems
        result_sha = self.write("inspection.json", result)
        verified = []
        for key, pin in sorted(self.pins.items()):
            if Path(key).is_absolute() or ".." in Path(key).parts:
                raise ValueError("Nonrelative input key")
            packed = relative(pin["snapshot"]).read_bytes()
            raw = gzip.decompress(packed)
            if (sha(packed), sha(raw), len(raw)) != (
                pin["gzip_sha256"], pin["sha256"], pin["bytes"]
            ):
                raise ValueError("Archive verification failed: " + key)
            verified.append(key)
        inputs_sha = self.write("inputs.json", {
            "written_utc": now(), "inputs": self.pins,
            "inspector_sha256": self.pins[str(self.inspector)]["sha256"],
            "all_archives_verified": len(verified),
            "relative_input_keys_verified": True,
        })
        return {"folder": str(self.phase), "inspection_sha256": result_sha,
                "inputs_sha256": inputs_sha, "inputs": len(verified),
                "problems": self.problems}

    def source_checks(self, rows):
        sources = collections.defaultdict(set)
        entries = collections.defaultdict(set)
        versions = collections.defaultdict(set)
        for row in rows:
            for path, digest in row.get("sources", {}).items():
                sources[path].add(digest)
            for suffix in ("a", "b"):
                module = row["spec_" + suffix].split(":")[0]
                entries[module].add(row["hash_" + suffix])
                versions[module].add(row["version_" + suffix])
        loaded = []
        for path, recorded in sorted(sources.items()):
            current = sha(self.capture(path))
            loaded.append({"path": path, "recorded": sorted(recorded),
                           "current": current, "matches": recorded == {current}})
        checked_entries = []
        for module, recorded in sorted(entries.items()):
            path = module_file(module)
            current = sha(self.capture(path)) if path else None
            version = self.version(module)
            checked_entries.append({
                "module": module, "entry_path": str(path),
                "entry_recorded": sorted(recorded), "entry_current": current,
                "entry_matches": recorded == {current},
                "version_recorded": sorted(versions[module]),
                "version_current": version["digest"],
                "version_matches": versions[module] == {version["digest"]},
            })
        self.check(all(row["matches"] for row in loaded), "Loaded source mismatch")
        self.check(all(row["entry_matches"] and row["version_matches"]
                       for row in checked_entries), "Entry or static closure mismatch")
        return {"loaded": loaded, "entries": checked_entries,
                "static_closures": self.versions,
                "scope": "Receipt-bound recorded identities match captured current source bytes; not continuous runtime monitoring or complete runtime data/environment closure"}

    def version(self, module):
        if module in self.versions:
            return self.versions[module]
        seen, todo = {}, [module]
        while todo:
            name = todo.pop()
            if name in seen or not name.startswith("bot_research"):
                continue
            path = module_file(name)
            if path is None:
                continue
            seen[name] = path
            parts = name.split(".")
            todo.extend(".".join(parts[:i]) for i in range(1, len(parts)))
            package = name if path.name == "__init__.py" else ".".join(parts[:-1])
            for node in ast.walk(ast.parse(self.capture(path))):
                if isinstance(node, ast.Import):
                    todo.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom):
                    if node.level:
                        parts = package.split(".")
                        parts = parts[:len(parts) - (node.level - 1)]
                        target = ".".join(parts + ([node.module] if node.module else []))
                    else:
                        target = node.module or ""
                    todo.append(target)
                    todo.extend(target + "." + alias.name for alias in node.names)
        files = set(seen.values()) | set(Path("bot_research/harness").glob("*.py"))
        digest = hashlib.sha256()
        for path in sorted(files):
            digest.update((str(path) + "\0" + sha(self.capture(path)) + "\n").encode())
        result = {"digest": digest.hexdigest(),
                  "paths": [str(path) for path in sorted(files)]}
        self.versions[module] = result
        return result


def module_file(name):
    path = Path(*name.split("."))
    for candidate in (path.with_suffix(".py"), path / "__init__.py"):
        if candidate.is_file():
            return candidate
    return None


def specs(raw):
    return [line.strip() for line in raw.decode().splitlines()
            if line.strip() and not line.startswith("#")]


def rows(raw):
    return [json.loads(line) for line in raw.splitlines()]


def normalize(row):
    side = row["candidate_side"]
    candidate = row["spec_a"] if side == 0 else row["spec_b"]
    opponent = row["spec_b"] if side == 0 else row["spec_a"]
    key = (opponent, row.get("scenario"), side)
    if row.get("error"):
        return candidate, key, None
    score = 1.0 if row["winner"] == side else .5 if row["winner"] is None else 0.0
    return candidate, key, (score, row["hp_diff_a"] * (1 if side == 0 else -1),
                            row["rounds"])


def row_metadata_ok(row):
    side = row["candidate_side"]
    return (side in (0, 1) and row["winner"] in (0, 1, None)
            and row["hp_a"] - row["hp_b"] == row["hp_diff_a"]
            and row["metadata"]["candidate_side"] == side
            and row["metadata"]["pair"] == row["pair"])


def error_counts(records):
    return {
        "harness_errors": sum(bool(row.get("error")) for row in records),
        "bot_errors": sum(sum(len(p["bot_errors"]) for p in row.get("players", []))
                          for row in records),
        "rejected_actions": sum(sum(p["n_rejected"] for p in row.get("players", []))
                                for row in records),
        "source_changed": sum(bool(row.get("source_changed")) for row in records),
        "scenario_errors": sum(sum(len(v) for v in row.get("scenario_errors", []))
                               for row in records),
    }


def wdl(table, keys):
    values = [table[key][0] for key in keys]
    return [values.count(score) for score in (1.0, .5, 0.0)]


def bootstrap(keys, left, right):
    opponents = sorted({key[0] for key in keys})
    by = collections.defaultdict(list)
    for key in sorted(keys):
        by[key[0]].append(left[key][0] - right[key][0])
    mean = sum(sum(by[opponent]) for opponent in opponents) / len(keys)
    rng, samples = random.Random(1), []
    for _ in range(4000):
        sample = [rng.choice(opponents) for _ in opponents]
        samples.append(sum(sum(by[o]) for o in sample) / sum(len(by[o]) for o in sample))
    samples.sort()
    return {"mean": mean, "lo": samples[100], "hi": samples[3899],
            "opponents": len(opponents), "conditions": len(keys),
            "resamples": 4000, "seed": 1, "sorted_indices": [100, 3899],
            "method": "Exact opponent-spec clusters retain both physical seats; W=1,D=0.5,L=0"}

"""Create a dated path-metadata amendment without rerunning any reduction.

Run from the project root. Existing evidence is read only. The caller separately
arranges private retention of the original path-bearing metadata.
"""
import ast
import datetime
import gzip
import hashlib
import json
from pathlib import Path

OUT = Path("bot_research/experiments/validation/reviews/economy_final_gate_001")
PHASE = OUT / "fresh56-20261031T231428944261Z"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_new(path, raw):
    with path.open("xb") as stream:
        stream.write(raw)


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


written = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
old_map_path = PHASE / "inputs.json"
old_map_raw = old_map_path.read_bytes()
old_map_sha = sha(old_map_raw)
if old_map_sha != "7c6ff01c5f3f27c50b960e24c872c9de680862ee40e575aa6e47327887e066e9":
    raise ValueError("Original map identity differs")
old_map = json.loads(old_map_raw)
new_map = {key: value for key, value in old_map.items() if key != "inputs"}
new_map["inputs"] = {}
changes, verification = [], []
project_root = Path.cwd()
for key, entry in old_map["inputs"].items():
    path = Path(key)
    new_key = str(path.relative_to(project_root)) if path.is_absolute() else key
    if Path(new_key).is_absolute() or ".." in Path(new_key).parts:
        raise ValueError("Input key does not remain inside the project")
    if new_key in new_map["inputs"]:
        raise ValueError("Normalized input key collision")
    new_map["inputs"][new_key] = entry
    if key != new_key:
        changes.append({
            "original_key_kind": "Absolute inspector path under the project cwd",
            "original_key_sha256": sha(key.encode()),
            "relative_key": new_key,
            "entry_unchanged": True,
        })
    packed = Path(entry["snapshot"]).read_bytes()
    raw = gzip.decompress(packed)
    if (sha(packed) != entry["gzip_sha256"] or sha(raw) != entry["sha256"]
            or len(raw) != entry["bytes"]):
        raise ValueError("Archived input verification failed: " + new_key)
    verification.append({
        "path": new_key, "sha256": sha(raw), "bytes": len(raw),
        "gzip_sha256": sha(packed), "verified": True,
    })
if len(verification) != 255 or len(changes) != 1:
    raise ValueError("Unexpected amendment size")
source_path = OUT / "inspect_fresh56_002.py"
if changes[0]["relative_key"] != str(source_path):
    raise ValueError("Unexpected changed input")
old_source = source_path.read_bytes()
source_entry = new_map["inputs"][str(source_path)]
if sha(old_source) != source_entry["sha256"]:
    raise ValueError("Original inspector differs from its verified archive")

old_fragment = "def capture(path):\n    path = Path(path)\n    key = str(path)\n"
new_fragment = """def capture(path):
    path = Path(path)
    project_root = Path.cwd()
    path = (path if path.is_absolute() else project_root / path).relative_to(project_root)
    if ".." in path.parts:
        raise ValueError("Input path leaves the project root")
    key = str(path)
"""
source_text = old_source.decode()
if source_text.count(old_fragment) != 1:
    raise ValueError("Capture function does not match the reviewed source")
new_source = source_text.replace(old_fragment, new_fragment).encode()
ast.parse(new_source)
new_source_path = OUT / "inspect_fresh56_003.py"
new_map_path = PHASE / "inputs_relative_003.json"
new_map_raw = json_bytes(new_map)
inspection_path = PHASE / "inspection.json"
inspection_sha = sha(inspection_path.read_bytes())
if inspection_sha != "354dcf82b613116d5d7c6d97ece32071b660c773a0016be7c0d8d6a30e637e32":
    raise ValueError("Numerical inspection identity differs")

receipt_path = PHASE / "path_metadata_amendment_003.json"
receipt = {
    "written_utc": written, "reviewer": "GPT-6 Astra",
    "original_map_sha256": old_map_sha,
    "relative_map": str(new_map_path), "relative_map_sha256": sha(new_map_raw),
    "transformation": "Replace the single absolute inputs dictionary key by Path(key).relative_to(Path.cwd()); retain every value and all other fields exactly",
    "changed_keys": changes, "other_fields_unchanged": True,
    "verified_archived_input_count": len(verification),
    "archived_input_verification": verification,
    "original_inspector": {
        "path": str(source_path), "sha256": sha(old_source),
        "preserved_archive": source_entry["snapshot"],
        "preserved_archive_sha256": source_entry["gzip_sha256"],
    },
    "revised_inspector": {
        "path": str(new_source_path), "sha256": sha(new_source),
        "change": "Normalize capture paths against the project cwd before recording keys",
        "validation": "Standard-library AST syntax parse only; never executed",
    },
    "numerical_inspection": str(inspection_path),
    "numerical_inspection_sha256_unchanged": inspection_sha,
    "new_numerical_reductions": 0, "new_policy_calls": 0,
    "new_engine_or_replay_calls": 0,
    "existing_files_modified_or_removed": 0,
    "original_map_retention": "Root will relocate the original path-bearing map to private lane storage after this amendment is ready",
}
receipt_raw = json_bytes(receipt)
review_path = OUT / "FRESH56_REVIEW_003.md"
prior_review_path = OUT / "FRESH56_REVIEW_002.md"
prior_review = prior_review_path.read_bytes()
prior_manifest_path = OUT / "fresh56_review_manifest_002.json"
prior_manifest = prior_manifest_path.read_bytes()
review_text = prior_review.decode()
review_text = review_text.replace(
    "# Completed fresh56 stage: independent review addendum",
    "# Completed fresh56 stage: review with path metadata amendment",
    1,
)
paragraph = (
    f"\nPublication metadata amended {written}. The original executed inspector "
    "recorded its own source under one absolute dictionary key because "
    "`Path(__file__)` resolved to an absolute path. "
    f"`{new_map_path.name}` replaces only that key with its project-relative form. "
    "All 255 archived inputs passed compressed hash, original hash and length checks. "
    "Their bytes, every entry value, all other map fields, and every numerical result "
    "are unchanged. The original map digest is "
    f"`{old_map_sha}`; the corrected map digest is `{sha(new_map_raw)}`. "
    "The old source remains archived. `inspect_fresh56_003.py` fixes future captures "
    "using `Path.cwd()` and `relative_to`; it was syntax parsed and not executed. "
    "This amendment performed no numerical rerun or campaign refresh. "
    "Root separately handles private retention of the original map. "
    "`fresh56_review_manifest_003.json` is the canonical publication manifest for "
    "this stage; the prior manifest and review remain historical records.\n"
)
review_text = review_text.replace("\n\nWritten ", paragraph + "\nWritten ", 1)
review_text = review_text.replace(
    f"its exact input map SHA-256 is `{old_map_sha}`",
    f"its corrected exact input map is `{new_map_path.name}`, SHA-256 `{sha(new_map_raw)}`",
)
review_text = review_text.replace(
    "`fresh56_review_manifest_002.json` binds",
    "`fresh56_review_manifest_003.json` binds",
)
index_path = OUT / "INDEX_FRESH56_003.md"
index_text = (
    "# Fresh56 amended publication reading order\n\n"
    "1. Read `FRESH56_REVIEW_003.md`, which preserves the measured scope and records "
    "the actual-time metadata correction.\n"
    "2. Read `fresh56-20261031T231428944261Z/inspection.json` for unchanged numerical "
    "results and `inputs_relative_003.json` in that folder for the corrected input map.\n"
    "3. Read `path_metadata_amendment_003.json` in that folder for the exact one-key "
    "transformation and verification of all 255 archived inputs.\n"
    "4. The original `inspect_fresh56_002.py` produced these results and remains "
    "archived. Its successor `inspect_fresh56_003.py` was syntax parsed only.\n\n"
    "The original map is superseded for publication; Root handles its private "
    "retention. Earlier numerical, interim and chronology records are unchanged. "
    "The overall recommendation remains OPEN on this fixed snapshot.\n"
)
outputs = {
    new_source_path: new_source, new_map_path: new_map_raw,
    receipt_path: receipt_raw, review_path: review_text.encode(),
    index_path: index_text.encode(),
}
for path in outputs:
    if path.exists():
        raise ValueError("Amendment output already exists: " + str(path))
for path, raw in outputs.items():
    write_new(path, raw)
file_paths = list(outputs) + [
    inspection_path, PHASE / "scope_supplement.json",
    PHASE / "notes-from-18.22.md", source_path,
    OUT / "INTERIM_REVIEW.md", OUT / "interim_manifest.json",
    OUT / "CHRONOLOGY_CLARIFICATION_001.md",
    OUT / "chronology_clarification_manifest_001.json",
    Path(__file__).relative_to(project_root) if Path(__file__).is_absolute() else Path(__file__),
]
manifest_path = OUT / "fresh56_review_manifest_003.json"
manifest = {
    "sealed_utc": written, "reviewer": "GPT-6 Astra",
    "scope": "Publication-path metadata amendment only; completed 18.22 pass and open 18.26 recommendation unchanged",
    "files": {str(path): sha(path.read_bytes()) for path in file_paths},
    "superseded_map_sha256": old_map_sha,
    "superseded_manifest_sha256": sha(prior_manifest),
    "prior_review_sha256": sha(prior_review),
    "input_count": 255, "all_archived_inputs_verified": True,
    "new_numerical_reductions": 0, "new_policy_calls": 0,
    "new_engine_or_replay_calls": 0,
    "revised_inspector_executed": False,
}
write_new(manifest_path, json_bytes(manifest))
if old_map_path.read_bytes() != old_map_raw or source_path.read_bytes() != old_source:
    raise ValueError("Original map or source changed during amendment")
if prior_review_path.read_bytes() != prior_review or prior_manifest_path.read_bytes() != prior_manifest:
    raise ValueError("Prior review or manifest changed during amendment")
for path in list(outputs) + [manifest_path]:
    if str(project_root).encode() in path.read_bytes():
        raise ValueError("Concrete project path in new artifact: " + str(path))
print(json.dumps({
    "written_utc": written, "verified_inputs": len(verification),
    "relative_map_sha256": sha(new_map_raw),
    "revised_inspector_sha256": sha(new_source),
    "receipt_sha256": sha(receipt_raw),
    "review_sha256": sha(review_path.read_bytes()),
    "manifest_sha256": sha(manifest_path.read_bytes()),
    "existing_files_unchanged": True,
}, indent=2))

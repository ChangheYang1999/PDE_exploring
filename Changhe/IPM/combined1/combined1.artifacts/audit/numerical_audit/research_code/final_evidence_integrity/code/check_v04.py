"""Finite final direct local-byte integrity. No evidence program is executed."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import gzip
import json
import os
import re
import time

R = Path(__file__).resolve().parents[3]
B = R / "research/final_evidence_integrity"


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v03")
    args = parser.parse_args()
    version = args.version
    assert re.fullmatch(r"v[0-9]{2}", version)
    assert os.sched_getaffinity(0) == {57}
    assert os.getpriority(os.PRIO_PROCESS, 0) == 19
    started = time.monotonic()
    start = now()
    target = B / f"verification/result_{version}.json"
    index_target = R / f"FINAL_EVIDENCE_INDEX_{version}.json"
    assert not target.exists() and not index_target.exists()
    cache, observed, edges, errors, roots, external = {}, {}, [], [], [], []

    def signature(p):
        s = p.stat()
        return (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)

    def digest(path, decoded=False):
        p = Path(path)
        p = p if p.is_absolute() else R / p
        q = p.resolve(strict=True)
        assert q.is_relative_to(R), ("outside own lane", str(q))
        sig = signature(q)
        key = (str(q), decoded, sig)
        if key not in cache:
            h = sha256()
            with (gzip.open(q, "rb") if decoded else q.open("rb")) as f:
                while chunk := f.read(1024 * 1024):
                    h.update(chunk)
            assert signature(q) == sig, ("changed while reading", str(q))
            cache[key] = h.hexdigest()
        observed[str(q)] = sig
        return cache[key]

    def check(owner, kind, path, expected, decoded=False):
        row = dict(
            owner=owner, kind=kind, path=path,
            expected_sha256=expected, decoded_gzip=decoded,
        )
        try:
            assert isinstance(path, str), ("unsupported path", path)
            assert isinstance(expected, str) and re.fullmatch(
                "[a-f0-9]{64}", expected
            ), ("unsupported digest", expected)
            row["actual_sha256"] = digest(path, decoded)
            row["pass"] = row["actual_sha256"] == expected
            if not row["pass"]:
                row["error"] = "digest mismatch"
        except Exception as exc:
            row["pass"], row["error"] = False, str(exc)
        edges.append(row)
        if not row["pass"]:
            errors.append(row)
        return row["pass"]

    prepared_path = B / "verification/PROOF_FIRST_v03.json"
    prepared = json.loads(prepared_path.read_text())
    assert not prepared["checker_exists"] and not prepared["selection_exists"]
    assert digest(B / "PROOF.md") == prepared["proof_sha256"]
    assert digest(B / "FINAL_SCOPE_PROOF_v03.md") == prepared["supplement_sha256"]
    assert digest(B / "ENCODING_PROOF_v02.md") == prepared["encoding_proof_sha256"]
    heading_prepared_path = B / "verification/PROOF_FIRST_v04.json"
    heading_prepared = json.loads(heading_prepared_path.read_text())
    assert not heading_prepared["checker_exists"]
    assert not heading_prepared["final_selection_exists"]
    assert not heading_prepared["result_exists"]
    assert digest(B / "LEDGER_HEADING_PROOF_v04.md") == heading_prepared["supplement_sha256"]
    assert digest(B / "code/check_v03.py") == heading_prepared["previous_unexecuted_checker_sha256"]
    freeze_path = B / f"verification/SELECTION_FREEZE_{version}.json"
    freeze = json.loads(freeze_path.read_text())
    assert freeze["version"] == version and not freeze["result_exists"]
    for path, expected in freeze["inputs"].items():
        assert check("selection freeze", "inputs", path, expected)
    selection_path = B / f"source/selection_{version}.json"
    ledger_path = B / f"source/VERIFY_REPORT_{version}.md"
    selection = json.loads(selection_path.read_text())
    ledger = ledger_path.read_text()
    assert len({row["claim"] for row in selection}) == len(selection)
    for selected in selection:
        owner = selected["claim"]
        assert re.fullmatch(r"N4-[0-9]{3}", owner)
        heading = selected["ledger_heading"]
        number = owner.removeprefix("N4-")
        assert heading.startswith((f"## {owner}.", f"## {number}.")), owner
        lines = ledger.splitlines()
        positions = [i for i, line in enumerate(lines) if line == heading]
        assert len(positions) == 1, ("ledger heading not unique", owner)
        begin = positions[0] + 1
        end = next((i for i in range(begin, len(lines))
                    if lines[i].startswith("## ")), len(lines))
        section = "\n".join(lines[begin:end])
        assert selected["sha256"] in section, ("digest not in own ledger entry", owner)
        okay = check(owner, "root", selected["record"], selected["sha256"])
        root = dict(selected, root_digest_pass=okay)
        try:
            root["current_proof_sha256"] = digest(selected["proof"])
        except Exception as exc:
            root["proof_error"] = str(exc)
            errors.append(dict(owner=owner, path=selected["proof"], error=str(exc)))
        if okay:
            record = json.loads((R / selected["record"]).read_text())
            root["recorded_utc"] = record.get("utc", record.get("date"))
            root["recorded_verdict"] = record.get("verdict", record.get("status"))
            decoded = set(selected.get("decoded_gzip_inputs", []))
            if decoded:
                assert owner == "N4-370" and len(decoded) == 2
                assert decoded.issubset(record["inputs"])
                mp, sp = selected["encoding_manifest"], selected["encoding_source"]
                assert check(owner, "encoding_source", sp, selected["encoding_source_sha256"])
                assert record["inputs"][sp] == selected["encoding_source_sha256"]
                assert check(owner, "encoding_manifest", mp, record["inputs"][mp])
                manifest = json.loads((R / mp).read_text())
                entries = {entry["local"]: entry for entry in manifest["files"].values()}
                for path in decoded:
                    entry = entries[path]
                    assert entry["encoding"] == "gzip" and Path(path).suffix == ".gz"
                    assert entry["sha256"] == record["inputs"][path]
                    check(owner, "explicit_gzip_stored", path, entry["stored_sha256"])
            for kind in ["inputs", "own_inputs", "bindings"]:
                mapping = record.get(kind, {})
                if not isinstance(mapping, dict):
                    errors.append(dict(owner=owner, kind=kind, error="unsupported map"))
                    continue
                for path, expected in mapping.items():
                    check(owner, kind, path, expected, path in decoded)
            retained = record.get("frozen_or_retained_sources", {})
            if not isinstance(retained, dict):
                errors.append(dict(owner=owner, error="unsupported retained-source map"))
            else:
                for path, entry in retained.items():
                    if not isinstance(entry, dict):
                        errors.append(dict(owner=owner, path=path, error="unsupported retained entry"))
                        continue
                    check(owner, "stored_peer_source", path, entry.get("stored_sha256"))
                    if entry.get("gzip"):
                        check(owner, "decoded_peer_source", path, entry.get("sha256"), True)
                    elif entry.get("sha256") != entry.get("stored_sha256"):
                        errors.append(dict(
                            owner=owner, path=path,
                            error="plain stored/original digest disagreement",
                        ))
            peer_map = record.get("external_readonly_bindings", {})
            if not isinstance(peer_map, dict):
                errors.append(dict(owner=owner, error="unsupported external provenance map"))
            else:
                external.extend(dict(
                    owner=owner, path=path, recorded_sha256=expected,
                    checked_here=False,
                ) for path, expected in peer_map.items())
                root["external_provenance_edges_not_rehashed"] = len(peer_map)
        roots.append(root)
    for path, sig in list(observed.items()):
        try:
            if signature(Path(path)) != sig:
                errors.append(dict(path=path, error="changed during audit"))
        except OSError as exc:
            errors.append(dict(path=path, error=str(exc)))
    input_paths = [
        Path(__file__), prepared_path, freeze_path, selection_path, ledger_path,
        B / "PROOF.md", B / "FINAL_SCOPE_PROOF_v03.md", B / "ENCODING_PROOF_v02.md",
        B / "LEDGER_HEADING_PROOF_v04.md", heading_prepared_path,
        B / "code/check_v03.py",
    ]
    inputs = {str(p.relative_to(R)): digest(p) for p in input_paths}
    scope = (
        "Current explicitly enumerated direct local bindings only. "
        "External provenance is listed but not rehashed. No unlisted transitive "
        "integrity, mathematical replay or status promotion."
    )
    result = dict(
        start_utc=start, utc=now(), version=version,
        selection_count=len(selection), direct_edge_count=len(edges),
        unique_resolved_files=len(observed), decoded_streams=sum(k[1] for k in cache),
        inputs=inputs, roots=roots, edges=edges, errors=errors,
        external_provenance_not_rehashed=external,
        all_direct_edges_match=not errors, scope=scope,
        expensive_computation_repeated=False, foreign_files_read_or_executed=False,
        elapsed_seconds=time.monotonic() - started,
        verdict=("CONFIRMED selected current local-byte integrity" if not errors
                 else "OPEN selected current local-byte integrity: inspect errors"),
    )
    with target.open("x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    result_sha = digest(target)
    index = dict(
        utc=result["utc"], integrity_result=str(target.relative_to(R)),
        integrity_result_sha256=result_sha, integrity_scope=scope,
        all_direct_edges_match=not errors, entries=roots,
        pending=[
            "Independent complete017 H upper and G0/G1/P2 for E2 or017<007",
            "Candidate027 and028 PDE certificates",
            "All new inverse and existence closures",
        ],
    )
    with index_target.open("x") as f:
        json.dump(index, f, indent=2)
        f.write("\n")
    print(result["utc"], result["verdict"], "roots", len(roots), "edges", len(edges),
          "unique", len(observed), "elapsed", result["elapsed_seconds"],
          "SHA256", result_sha, flush=True)
    for error in errors:
        print("ERROR", json.dumps(error), flush=True)


if __name__ == "__main__":
    main()

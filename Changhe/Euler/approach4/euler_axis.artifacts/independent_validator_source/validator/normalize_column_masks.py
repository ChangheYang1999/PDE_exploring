#!/usr/bin/env python3
"""Expand documented inner-element masks, preserving exact stored coefficients."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import shutil
import time
import numpy as np

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalize(native, output):
    native, output = Path(native).resolve(), Path(output).resolve()
    if not output.is_relative_to(ROOT.parent):
        raise ValueError("output outside verifier lane")
    if output.exists():
        raise FileExistsError("retain prior normalized exports")
    start, cpu = time.perf_counter(), time.process_time()
    input_hashes = {n: sha(native / n) for n in
                    ["coeffs.npz", "BASIS.md", "candidate.json", "samples.npz",
                     "source_run_result.json"]}
    with np.load(native / "coeffs.npz", allow_pickle=False) as z:
        meta = json.loads(str(z["meta_json"]))
        arrays = {k: z[k].copy() for k in z.files if k != "meta_json"}
    native_meta = json.loads(json.dumps(meta))
    rows = []
    for index, element in enumerate(meta["elements"]):
        for field in ["phi", "q"]:
            name = f"{field}_el{index}"
            before = arrays[name]
            if element["kind"] == "exterior":
                if len(element["labels_" + field]) != len(before):
                    raise ValueError("exterior selected labels disagree")
                rows.append({"array": name, "unchanged": True, "count": len(before)})
                continue
            labels = element["labels"]
            mask = element[field + "_cols"]
            if len(mask) != len(before) or len(set(mask)) != len(mask):
                raise ValueError("invalid mask length or repeated column")
            if any(type(i) is not int or i < 0 or i >= len(labels) for i in mask):
                raise ValueError("out-of-range or noninteger mask")
            if "labels_" + field in element:
                if element["labels_" + field] != [labels[i] for i in mask]:
                    raise ValueError("conflicting selected labels")
            expected_parity = 1 if field == "phi" else 0
            if any(int(labels[i][0]) % 2 != expected_parity for i in mask):
                raise ValueError("unexpected reflection parity")
            expanded = np.zeros(len(labels), dtype=before.dtype)
            expanded[mask] = before
            remaining = np.ones(len(labels), dtype=bool)
            remaining[mask] = False
            assert expanded[mask].tobytes() == before.tobytes()
            assert np.all(expanded[remaining] == 0)
            arrays[name] = expanded
            element["labels_" + field] = labels
            element[field + "_cols"] = list(range(len(labels)))
            rows.append({"array": name, "selected_count": len(mask),
                         "expanded_count": len(labels), "selected_bitwise_equal": True,
                         "added_entries_exactly_zero": True, "parity_confirmed": True})
    output.mkdir(parents=True)
    np.savez(output / "coeffs.npz", **arrays, meta_json=json.dumps(meta))
    with np.load(output / "coeffs.npz", allow_pickle=False) as z:
        for index, element in enumerate(native_meta["elements"]):
            for field in ["phi", "q"]:
                name = f"{field}_el{index}"
                assert z[name].tobytes() == arrays[name].tobytes()
    for name in ["samples.npz", "source_run_result.json"]:
        shutil.copyfile(native / name, output / name)
    candidate = json.loads((native / "candidate.json").read_text())
    candidate["native_coefficient_sha256"] = input_hashes["coeffs.npz"]
    candidate["equivalent_representation_note"] = (
        "Ball and shell masks expanded with exact zeros; exterior unchanged. "
        "This is the same finite field, not a refit.")
    (output / "candidate.json").write_text(json.dumps(candidate, indent=2) + "\n")
    shutil.copyfile(native / "BASIS.md", output / "NATIVE_BASIS.md")
    shapes = "\n".join(f"- {k}: {list(v.shape)}" for k, v in arrays.items())
    (output / "BASIS.md").write_text(
        "# Equivalent full-column reflection export\n\n"
        "The scalar basis functions, coordinates, interfaces and gauge are exactly "
        "those in NATIVE_BASIS.md. In the ball and shell, every native basis column "
        "is present in each coefficient vector. Unselected columns contain exact "
        "zeros; selected entries preserve their native binary values. The exterior "
        "arrays and selected exterior labels are unchanged. Native array lengths "
        "in NATIVE_BASIS.md describe the archived input, not these expanded arrays.\n\n"
        "Expanded array shapes:\n\n" + shapes + "\n\n"
        "The transformation is justified by research/column_mask_equivalence/PROOF.md "
        "and recorded in normalization.json. The field, not merely its sample "
        "values, is unchanged by the finite-sum identity.\n")
    for name, digest in input_hashes.items():
        if sha(native / name) != digest:
            raise RuntimeError("native input changed")
    record = {"completed_utc": datetime.now(timezone.utc).isoformat(),
              "native_directory": str(native), "output_directory": str(output),
              "native_sha256": input_hashes, "output_coefficient_sha256": sha(output / "coeffs.npz"),
              "implementation_sha256": sha(__file__),
              "proof_sha256": sha(ROOT.parent / "research/column_mask_equivalence/PROOF.md"),
              "checks": rows, "status": "PASS", "wall_seconds": time.perf_counter() - start,
              "cpu_seconds": time.process_time() - cpu}
    (output / "normalization.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("native", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(json.dumps(normalize(args.native, args.output), indent=2))

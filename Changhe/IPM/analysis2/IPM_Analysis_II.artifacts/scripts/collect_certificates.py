"""Copy the certificate programs and data of the checked proofs into certificates/<topic>/ and write a
SHA-256 manifest. Source tree is read only."""
import os, sys, shutil, hashlib, datetime
SRC, DST = sys.argv[1], sys.argv[2]
TOPIC = {"source_audit": "P1_source", "01_operator": "P1_operator", "04_singular": "P2_singular",
         "05_tails": "P3_tails", "02_energy": "P4_energy", "03_frozen": "P5_frozen", "07_weighted": "P6_P7_weighted",
         "09_quasilinear": "P8_quasilinear", "06_closure": "P9_closure", "08_refits": "P10_refits",
         "10_tail_splice": "P10_tail_splice", "numerics_audit": "P11_audit",
         "11_residual_norms": "P12_residual_norms", "12_affine_obstruction": "P13_affine_obstruction",
         "13_algebraic_repair": "P14_algebraic_repair",
         "14_homogeneous_weight": "P15_homogeneous_weight", "15_angular_sampling": "P16_angular_sampling",
         "16_weighted_fractional": "P17_weighted_fractional", "17_weight_radius": "P18_weight_radius",
         "18_fractional_constants": "P19_fractional_constants", "19_nb_candidates": "P20_nb_candidates",
         "20_real_velocity": "P21_real_velocity", "21_frozen_optimality": "P22_frozen_optimality",
         "22_axis_constraints": "P23_axis_constraints",
         "24_weaker_matrix": "P24_weaker_matrix", "23_admissible_tail_gap": "P25_admissible_tail_gap",
         "25_candidate_contract": "P26_candidate_contract",
         "26_uniform_family_gap": "P27_uniform_family_gap", "27_candidate_point_audit": "P28_candidate_point_audit",
         "28_limits_of_tail_invariants": "P29_limits_of_tail_invariants",
         "29_residual_targets": "P30_residual_targets",
         "30_radial_degree_obstruction": "P31_radial_degree_obstruction",
         "31_logarithmic_derivative": "P31_logarithmic_derivative",
         "32_stationary_order_seven": "P32_stationary_order_seven",
         "33_recursive_dilation": "P33_recursive_dilation", "34_affine_scope": "P34_affine_scope",
         "35_seven_branch_gap": "P35_seven_branch_gap", "36_b6_candidates": "P36_b6_candidates",
         "37_strain_trace": "P37_strain_trace", "38_local_distance": "P38_local_distance",
         "39_annular_distance": "P39_annular_distance", "40_fixed_tail_distance": "P40_fixed_tail_distance"}
# Extra input folders, and large intermediate files that the shipped programs regenerate exactly (their hashes are
# recorded in S1_NUMERICAL_CERTIFICATES.md instead).
EXTRA = {"08_refits/inputs": "P10_refit_inputs"}
SKIP = {("11_residual_norms", "state131_polynomials.json"), ("11_residual_norms", "n12_m10_polynomials.json"),
        ("23_admissible_tail_gap", "nb_stableA2_exact.sectors.json"), ("23_admissible_tail_gap", "nb_stableA3_exact.sectors.json")}
# Computations still running in the source tree at collection time (none at present); not used by any certified
# statement.
PENDING = {}
# Files of the numerical work read by shipped programs. They are shipped in two folders that restore_layout.py puts into
# BASE/numerics/code and BASE/numerics/data (the program wnorm_cert_multi.py writes its record to ../data relative to
# its own folder). numerics_data: grid088_coarse.npz (read by P11_audit/check_grid_enclosures.py), the producer record
# wnorm_cert_131.json (read by P11_audit/audit_c8.py, which compares its own enclosures with the producer's), and the
# exact state 131 input, output record and log of the independent recomputation wnorm_cert_multi.py of the combined
# annular bound (P17.7, P18.2, P21.2), and the exact seventh stationary order stationary_order7.json (compared by
# P32_stationary_order_seven/recur_sine.py with its own recurrence), and the exact seven-branch candidate nb_b6_exact.json
# (read by P36_b6_candidates/audit_exact.py, point_contract.py and summarize.py). numerics_code: that program with the four modules it imports.
# P10_refit_inputs: nb_test_result.json (read by P14_algebraic_repair/stable_coordinates.py; floating trial rows, only
# its generator list enters an exact check) and the exact candidates audited in 19_nb_candidates (the "candidate" field
# of every <name>.audit.json there, for example nb_stableA2_exact.json), read by P20_nb_candidates/audit_exact.py and
# P23_axis_constraints/axis_audit.py.
import json
NUM = os.path.join(SRC, "..", "..", "s1-num", "research", "data")
CODE = os.path.join(SRC, "..", "..", "s1-num", "research", "code")
RUNS = os.path.join(SRC, "..", "..", "s1-num", "research", "runs")
NUMERICS = [(os.path.join(NUM, "nb_test_result.json"), "P10_refit_inputs")]
for f in ("grid088_coarse.npz", "wnorm_cert_131.json", "state131_exact.json", "wnorm_cert_multi_131.json",
          "stationary_order7.json", "nb_b6_exact.json"):
    NUMERICS.append((os.path.join(NUM, f), "numerics_data"))
NUMERICS.append((os.path.join(RUNS, "wnorm_cert_multi_131.log"), "numerics_data"))
for f in ("wnorm_cert_multi.py", "wnorm_cert.py", "farfield_exact.py", "farfield_F_cert.py", "farfield_bounds.py"):
    NUMERICS.append((os.path.join(CODE, f), "numerics_code"))
# The original case 4 checkpoints (read only), from which recover_state.py and the programs that reconstruct state 131
# afresh rebuild the exact coefficients.
CASE4 = os.path.join(SRC, "..", "..", "source", "case4", "IPM_case4.artifacts", "checkpoints")
for state, folder in ((88, "state088_handoff"), (131, "state131_last_unverified")):
    for ext in ("json", "npz"):
        NUMERICS.append((os.path.join(CASE4, folder, f"accepted_{state:08d}.{ext}"), f"P1_checkpoint_state{state:03d}"))
NB = os.path.join(SRC, "19_nb_candidates", "verification")
for f in sorted(os.listdir(NB)) if os.path.isdir(NB) else []:
    if f.endswith(".audit.json"):
        cand = json.load(open(os.path.join(NB, f)))["candidate"]
        assert cand == f[:-len(".audit.json")] + ".json", (f, cand)
        NUMERICS.append((os.path.join(NUM, cand), "P10_refit_inputs"))
rows = []
for p, name in NUMERICS:
    od = os.path.join(DST, name); os.makedirs(od, exist_ok=True)
    shutil.copy2(p, os.path.join(od, os.path.basename(p)))
    rows.append((name, os.path.basename(p), os.path.getsize(p), hashlib.sha256(open(p, 'rb').read()).hexdigest()))
for sub_dir, name in EXTRA.items():
    d = os.path.join(SRC, sub_dir)
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        if os.path.isfile(p):
            od = os.path.join(DST, name); os.makedirs(od, exist_ok=True)
            shutil.copy2(p, os.path.join(od, f))
            rows.append((name, f, os.path.getsize(p), hashlib.sha256(open(p, 'rb').read()).hexdigest()))
for t, name in TOPIC.items():
    for sub in ("verification", ""):
        d = os.path.join(SRC, t, sub) if sub else os.path.join(SRC, t)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            # proof texts (.md at the top of a topic) are shipped in P0_proof_texts; the audit notes in verification/
            # are shipped with their folder (some programs bind them by hash)
            if not os.path.isfile(p) or (f.endswith('.md') and sub == ""):
                continue
            if sub == "" and t not in ("source_audit", "numerics_audit"):
                continue
            if (t, f) in SKIP:
                continue
            if any(k in f for k in PENDING.get(t, ())):
                continue
            od = os.path.join(DST, name); os.makedirs(od, exist_ok=True)
            shutil.copy2(p, os.path.join(od, f))
            h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
            rows.append((name, f, os.path.getsize(p), h))
# Proof texts read by shipped programs (some programs bind the proof text they implement by its SHA-256 hash). They
# are shipped verbatim in P0_proof_texts as <topic>__<file>; restore_layout.py puts them back into <topic>/.
import re
texts = set()
for name, f, size, h in rows:
    if not f.endswith('.py'):
        continue
    topic = next((t for t, n in TOPIC.items() if n == name), None)
    code = open(os.path.join(DST, name, f)).read()
    for t, m in re.findall(r"(\d\d_[a-z_]+|source_audit|numerics_audit)/([A-Z_0-9]+\.md)", code):
        texts.add((t, m))
    for m in re.findall(r"['\"]([A-Z_0-9]*(?:PROOF|AUDIT)\.md)['\"]", code):
        if topic and topic not in ("source_audit", "numerics_audit"):
            texts.add((topic, m))
for t, m in sorted(texts):
    p = os.path.join(SRC, t, m)
    if not os.path.isfile(p):
        continue
    od = os.path.join(DST, "P0_proof_texts"); os.makedirs(od, exist_ok=True)
    shutil.copy2(p, os.path.join(od, f"{t}__{m}"))
    rows.append(("P0_proof_texts", f"{t}__{m}", os.path.getsize(p), hashlib.sha256(open(p, 'rb').read()).hexdigest()))
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
with open(os.path.join(DST, "MANIFEST.txt"), "w") as fh:
    fh.write(f"# certificate programs and data, collected {now}; columns: folder, file, bytes, sha256\n")
    for r in rows:
        fh.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\n")
print(len(rows), "files,", sum(r[2] for r in rows), "bytes")

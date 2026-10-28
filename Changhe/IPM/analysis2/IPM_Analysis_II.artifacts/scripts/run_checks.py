"""Rerun the certificate checks in a restored layout and compare their outputs with the shipped files.

Usage: python3 run_checks.py CERTIFICATES_DIR BASE_DIR [--searches] [--recover] [--only FOLDER,FOLDER,...]
                                                     [--progs PROGRAM,PROGRAM,...] [--timeout SECONDS]

BASE_DIR must first be filled by restore_layout.py. Each program runs single-threaded from BASE_DIR with a time limit of
540 s (or SECONDS). After each program every JSON file it rewrote is compared with the shipped copy in CERTIFICATES_DIR; keys that
only record time stamps or elapsed times are ignored. A file is reported as "same"; as "same values" when the only
differences are recorded SHA-256 hashes of input files (an input regenerated earlier in the same run carries a new time
stamp), recorded input locations (which can differ in a restored layout), keys that the program now writes but the shipped file lacks, or review entries that the independent review
added to the shipped file; or as DIFFERS with the paths of the differing keys. When the values agree, the shipped file
is copied back over the rewritten one, so that later programs read the reviewed file as they did when the certificates
were produced; if the recorded input hashes differ, the rewritten file is kept instead (later programs check those
hashes against the regenerated inputs) and only the review entries of the shipped file are carried over into it. A
file that DIFFERS is left as rewritten. With
--searches the certificate searches (partition generators) are rerun as well, with the parameters recorded in the
shipped certificates. With --recover the exact reconstruction recover_state.py is rerun first; it needs the case 4
archive restored by the third argument of restore_layout.py. With --only, only programs of the listed certificate folders run; with --progs NAME,NAME,..., only the listed
programs. A summary table is written to BASE_DIR/run_checks.log.
"""
import json, os, re, subprocess, sys, time
from pathlib import Path

PY = sys.executable
CHECKS = [
    ("P1_source", "field_eval.py", ["--state", "131"]),
    ("P2_singular", "check_kernel.py", []),
    ("P2_singular", "check_strain_beta.py", []),
    ("P3_tails", "check_tail.py", []),
    ("P3_tails", "check_highest_harmonic.py", []),
    ("P3_tails", "formal_tail_completion.py", []),
    ("P3_tails", "audit_residual_hessian.py", []),
    ("P4_energy", "compact_matrix.py", ["131"]),
    ("P4_energy", "auxiliary_polynomials.py", ["131"]),
    ("P4_energy", "coefficient_bounds.py", ["131"]),
    ("P4_energy", "check_l2_identity.py", []),
    ("P4_energy", "audit_compact_certificate.py", []),
    ("P4_energy", "audit_auxiliary_certificates.py", []),
    ("P4_energy", "check_auxiliary_fields.py", []),
    ("P4_energy", "holder_embedding_constant.py", []),
    ("P4_energy", "farfield_matrix_certificate.py", []),
    ("P5_frozen", "heat_constants.py", []),
    ("P5_frozen", "cutoff_constant.py", []),
    ("P5_frozen", "optimize_cutoff.py", []),
    ("P5_frozen", "optimized_kernel_bound.py", []),
    ("P5_frozen", "trace_constants.py", []),
    ("P5_frozen", "endpoint_constants.py", []),
    ("P6_P7_weighted", "audit_high_symbol_certificate.py", []),
    ("P6_P7_weighted", "audit_high_symbol_points.py", []),
    ("P6_P7_weighted", "audit_m1_unweighted.py", []),
    ("P6_P7_weighted", "audit_sharp_coefficients.py", []),
    ("P6_P7_weighted", "audit_extra_coefficients.py", []),
    ("P6_P7_weighted", "audit_gradient_identity.py", []),
    ("P6_P7_weighted", "check_weighted_identities.py", []),
    ("P6_P7_weighted", "higher_coefficient_bounds.py", []),
    ("P6_P7_weighted", "rough_symbol_bounds.py", []),
    ("P6_P7_weighted", "weighted_background_bounds.py", []),
    ("P6_P7_weighted", "mellin_riesz_constants.py", []),
    ("P6_P7_weighted", "low_inverse_family.py", []),
    ("P6_P7_weighted", "bilinear_constants.py", []),
    ("P6_P7_weighted", "h2_constants.py", []),
    ("P6_P7_weighted", "weighted_high_constants.py", []),
    ("P6_P7_weighted", "route_u_constants.py", []),
    ("P6_P7_weighted", "sharp_route_u_constants.py", []),
    ("P8_quasilinear", "constants.py", []),
    ("P8_quasilinear", "sharp_constants.py", []),
    ("P9_closure", "check_derivative_loss.py", []),
    ("P10_refits", "audit_exact_refit.py", ["n12_m4", "n12_m5", "n12_m10", "n12_m12", "n12_m14"]),
    ("P10_refits", "point_fields.py", ["n12_m4", "n12_m5", "n12_m10", "n12_m12"]),
    ("P10_refits", "audit_matrix.py", ["n12_m5"]),
    ("P10_tail_splice", "audit_splice.py", []),
    ("P11_audit", "check_grid_enclosures.py", []),
    ("P11_audit", "check_series_cap.py", []),
    ("P11_audit", "audit_c8.py", []),
    ("P11_audit", "audit_c9.py", []),
    # binomial order Q=4 refinements; each reads the Q=3 record written just before it
    ("P11_audit", "audit_c8.py", ["4"]),
    ("P11_audit", "audit_c9.py", ["4"]),
    ("P11_audit", "audit_binary_summary.py", []),
    ("P12_residual_norms", "compact_norms.py", ["state131"]),
    ("P12_residual_norms", "audit_norms.py", ["state131"]),
    ("P12_residual_norms", "compact_norms.py", ["n12_m10"]),
    ("P12_residual_norms", "audit_norms.py", ["n12_m10"]),
    ("P13_affine_obstruction", "check_conditions.py", []),
    ("P14_algebraic_repair", "construct.py", []),
    ("P14_algebraic_repair", "construct.py", ["256", "4096"]),
    ("P14_algebraic_repair", "audit_repair.py", []),
    ("P14_algebraic_repair", "point_probe.py", []),
    ("P14_algebraic_repair", "point_probe.py", ["algebraic_state131_k256", "algebraic_n12_m10_k256",
                                                "algebraic_state131_k4096", "algebraic_n12_m10_k4096"]),
    ("P14_algebraic_repair", "audit_points.py", []),
    ("P14_algebraic_repair", "audit_points.py", ["algebraic_state131_k256", "algebraic_n12_m10_k256",
                                                 "algebraic_state131_k4096", "algebraic_n12_m10_k4096"]),
    ("P14_algebraic_repair", "matrix_grid.py", []),
    ("P14_algebraic_repair", "audit_grid_minima.py", []),
    ("P14_algebraic_repair", "arb_hessian.py", ["n12_m10"]),
    ("P14_algebraic_repair", "arb_hessian.py", ["algebraic_n12_m10_k8"]),
    ("P14_algebraic_repair", "residual_gap.py", []),
    ("P15_homogeneous_weight", "check_matrix.py", []),
    ("P6_P7_weighted", "fractional_bilinear_constants.py", []),
    ("P6_P7_weighted", "radial_commutator_constants.py", []),
    ("P6_P7_weighted", "r2_extra_audit.py", []),
    ("P6_P7_weighted", "sharp_weighted_h2_constants.py", []),
    ("P6_P7_weighted", "sharp_weighted_high_constants.py", []),
    # P14_algebraic_repair/stable_coordinates.py is not run here: it expects BASE to be named research and the two
    # numerics inputs in BASE/../../s1-num/research/data (manual procedure in S1_RESTART.md).
    ("P17_weighted_fractional", "constants.py", []),
    ("P17_weighted_fractional", "state131_weighted_gap.py", []),
    ("P17_weighted_fractional", "rough_constants.py", []),
    ("P17_weighted_fractional", "sharp_weighted_constants.py", []),
    ("P17_weighted_fractional", "reference_audit.py", []),
    ("P17_weighted_fractional", "annular_residual.py", []),
    ("P18_weight_radius", "decay_radius.py", []),
    ("P18_weight_radius", "annular_residual.py", []),
    ("P19_fractional_constants", "constants.py", []),
    # The two P20 argument lists are filled in at run time with every candidate audited in P20_nb_candidates
    # (files <name>.audit.json) whose exact input is shipped in P10_refit_inputs: the exact input
    # 08_refits/inputs/<name>.json, and the name itself. (The audit of nb_d2_exact is shipped only as an input of the
    # independent recomputations scripts/check_*.py.)
    ("P20_nb_candidates", "audit_exact.py", ["@nb_inputs"]),
    ("P20_nb_candidates", "point_audit.py", ["@nb_names"]),
    ("P21_real_velocity", "constants.py", []),
    ("P21_real_velocity", "annular_residual.py", []),
    ("P23_axis_constraints", "axis_audit.py", []),
    ("P24_weaker_matrix", "check.py", []),
    # annular_candidates.py also regenerates the two large sector records <name>.sectors.json (not shipped; their
    # hashes are recorded in S1_NUMERICAL_CERTIFICATES.md), which summarize.py reads
    ("P25_admissible_tail_gap", "annular_candidates.py", ["nb_stableA2_exact"]),
    ("P25_admissible_tail_gap", "annular_candidates.py", ["nb_stableA3_exact"]),
    ("P25_admissible_tail_gap", "summarize.py", []),
    ("P26_candidate_contract", "check.py", []),
    ("P27_uniform_family_gap", "muntz_bound.py", []),
    ("P27_uniform_family_gap", "audit_algebra.py", []),
    ("P28_candidate_point_audit", "point_contract.py", []),
    ("P28_candidate_point_audit", "point_contract.py", ["nb_A6dpen_exact"]),
    ("P28_candidate_point_audit", "summarize.py", []),
    ("P28_candidate_point_audit", "summarize_a6.py", []),
    ("P28_candidate_point_audit", "point_contract.py", ["nb_Mpen2_exact"]),
    ("P28_candidate_point_audit", "summarize_mpen2.py", []),
    ("P29_limits_of_tail_invariants", "relaxation_bound.py", []),
    ("P29_limits_of_tail_invariants", "audit_relaxation.py", []),
    ("P30_residual_targets", "check.py", []),
    ("P31_radial_degree_obstruction", "degree_bound.py", []),
    ("P31_radial_degree_obstruction", "audit_degree.py", []),
    ("P31_logarithmic_derivative", "constant_bound.py", []),
    ("P31_logarithmic_derivative", "audit_derivative.py", []),
    ("P32_stationary_order_seven", "recur_sine.py", []),
    ("P32_stationary_order_seven", "audit_fourier.py", []),
    # The programs of P33 to P40 are not shipped; the numbers of those parts are rechecked by the independent
    # recomputations scripts/check_*.py (scripts/run_recomputations.py).
    # P34_affine_scope/audit_scope.py is not run here: it audits the wording of an earlier version of the report (its
    # snapshot lead_report_snapshot.md is shipped) and certifies no number.
    ("numerics_code", "wnorm_cert_multi.py", ["numerics/data/state131_exact.json", "3", "35,32,31"]),
    # P11_audit/check_grid_enclosures.py, audit_c8.py, audit_c9.py and audit_binary_summary.py, the P17, P18, P21 and P23 programs that
    # reconstruct state 131, the P25 and P26 programs, P27_uniform_family_gap/audit_algebra.py and the P28 programs
    # point_contract.py, summarize.py, summarize_a6.py and summarize_mpen2.py and the two P32 programs read the original
    # checkpoint or files of the numerical work
    # at absolute paths of the production machine; on another machine restore with restore_layout.py --relocate, which
    # points them to the shipped copies.
    # P11_audit/audit_c2_correction.py and audit_cert_sups_summary.py are not run here: they read a 38 MB record of
    # the numerical work that is not shipped (manual procedure in S1_RESTART.md).
]
SEARCHES = [
    ("P4_energy", "compact_certificate.py", ["--state", "131", "--target", "3.8"]),
    ("P4_energy", "auxiliary_certificate.py", ["--state", "131", "--quantity", "A", "--factor"]),
    ("P4_energy", "auxiliary_certificate.py", ["--state", "131", "--quantity", "DU"]),
    ("P4_energy", "auxiliary_certificate.py", ["--state", "131", "--quantity", "N"]),
    ("P6_P7_weighted", "high_symbol_certificate.py", ["--k", "2", "--radius", "1/2", "--sigma", "1/5", "--target", "1/2", "--adaptive"]),
    ("P6_P7_weighted", "high_symbol_certificate.py", ["--k", "3", "--radius", "1/2", "--sigma", "6/5", "--target=-5/4", "--adaptive", "--tag", "_auxiliary"]),
    ("P6_P7_weighted", "high_symbol_certificate.py", ["--k", "1", "--radius", "1", "--sigma", "0", "--target", "9/10", "--adaptive", "--tag", "_unweighted09"]),
    ("P6_P7_weighted", "sharp_N_certificate.py", []),
    ("P6_P7_weighted", "sharp_coefficients.py", []),
    ("P6_P7_weighted", "extra_coefficients.py", []),
    ("P3_tails", "residual_derivative_lower.py", ["--state", "131", "--cut", "10", "--radius", "100"]),
    ("P10_refits", "certify_matrix.py", ["n12_m5"]),
    ("P10_tail_splice", "construct_splice.py", []),
]
TIME_KEYS = ("utc", "elapsed", "seconds", "time", "date")


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if not any(t in k.lower() for t in TIME_KEYS)}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


HEX64 = re.compile(r"[0-9a-f]{64}")


def diff_paths(a, b, path="", out=None):
    """Differences between new output a and shipped file b, as (path, kind), kind in {"added", "missing", "value",
    "hash", "path"}; "hash" is a value difference between two SHA-256 hex digests (a recorded hash of an input file),
    "path" one between two absolute paths of files with the same name (a recorded location of an input file)."""
    out = [] if out is None else out
    if isinstance(a, dict) and isinstance(b, dict):
        # a key that is the absolute path of an input file moves with restore_layout.py --relocate
        a_only = [k for k in a if k not in b and k.startswith("/")]
        b_only = [k for k in b if k not in a and k.startswith("/")]
        moved = {}
        for k in a_only:
            match = [j for j in b_only if Path(j).name == Path(k).name]
            if len(match) == 1 and sum(Path(i).name == Path(k).name for i in a_only) == 1:
                moved[k] = match[0]
        for k, j in moved.items():
            out.append((path + "/" + k, "path"))
            diff_paths(a[k], b[j], path + "/" + k, out)
        for k in sorted((set(a) | set(b)) - set(moved) - set(moved.values())):
            if k not in b:
                out.append((path + "/" + k, "added"))
            elif k not in a:
                out.append((path + "/" + k, "missing"))
            else:
                diff_paths(a[k], b[k], path + "/" + k, out)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (u, v) in enumerate(zip(a, b)):
            diff_paths(u, v, f"{path}[{i}]", out)
    elif a != b:
        both_hashes = isinstance(a, str) and isinstance(b, str) and HEX64.fullmatch(a) and HEX64.fullmatch(b)
        # an absolute input path recorded by a program moves with restore_layout.py --relocate
        both_paths = isinstance(a, str) and isinstance(b, str) and a.startswith("/") and b.startswith("/") \
            and Path(a).name == Path(b).name
        out.append((path or "/", "hash" if both_hashes else "path" if both_paths else "value"))
    return out


REVIEW_KEYS = ("verdict", "status")
REVIEW_ANNOTATIONS = ("ledger", "proof_audit")


def classify(dp, new=None, shipped=None):
    """Hash keys (keys ending in sha256, or any value recorded as a SHA-256 digest where the shipped file has another
    digest) record input files (which carry time stamps); absolute paths of input files with the same name record where
    the inputs were restored; keys added by the program after the shipped file was
    written carry no certified value; a top-level verdict or status CONFIRMED that the independent review wrote into the
    shipped file after the program ran (the program itself writes the provisional PENDING_PROOF_AUDIT) carries no
    certified value either, and neither do the top-level review annotations (the review ledger entry and the record of
    the proof audit) that the review appended to the shipped file. Any other difference is a reproduction failure."""
    if not dp:
        return "same"
    hashes = [p for p, kind in dp if p.rsplit("/", 1)[-1].endswith("sha256") or kind == "hash"]
    paths = [p for p, kind in dp if kind == "path"]
    added = [p for p, kind in dp if kind == "added" and p not in hashes]
    review = [p for p, kind in dp if kind != "added" and p.lstrip("/") in REVIEW_KEYS and new is not None
              and new.get(p.lstrip("/")) == "PENDING_PROOF_AUDIT" and shipped.get(p.lstrip("/")) == "CONFIRMED"]
    review += [p for p, kind in dp if kind == "missing" and p.lstrip("/") in REVIEW_ANNOTATIONS]
    other = [p for p, kind in dp if p not in hashes and p not in paths and p not in added and p not in review]
    if other:
        return "DIFFERS at " + ", ".join(other[:4])
    parts = (["recorded input hashes differ (" + ", ".join(hashes[:4]) + ")"] if hashes else []) + \
            (["recorded input locations differ (" + ", ".join(paths[:4]) + ")"] if paths else []) + \
            (["keys absent from the shipped file (" + ", ".join(added[:4]) + ")"] if added else []) + \
            (["review verdict of the shipped file (" + ", ".join(review) + ")"] if review else [])
    return "same values; " + "; ".join(parts)


def main():
    cert, base = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from restore_layout import LAYOUT
    nb = sorted(p.name[:-len(".audit.json")] for p in (cert / "P20_nb_candidates").glob("*.audit.json")
                if (cert / "P10_refit_inputs" / (p.name[:-len(".audit.json")] + ".json")).exists())
    expand = {"@nb_inputs": [f"08_refits/inputs/{n}.json" for n in nb], "@nb_names": nb}
    checks = [(f, prog, [x for a in args for x in expand.get(a, [a])]) for f, prog, args in CHECKS]
    jobs = ([("P1_source", "recover_state.py", [])] if "--recover" in sys.argv else []) + checks
    jobs += SEARCHES if "--searches" in sys.argv else []
    if "--only" in sys.argv:
        keep = sys.argv[sys.argv.index("--only") + 1].split(",")
        jobs = [j for j in jobs if j[0] in keep]
    if "--progs" in sys.argv:
        keep = sys.argv[sys.argv.index("--progs") + 1].split(",")
        jobs = [j for j in jobs if j[1] in keep]
    limit = int(sys.argv[sys.argv.index("--timeout") + 1]) if "--timeout" in sys.argv else 540
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    log = []
    for folder, prog, args in jobs:
        d = base / LAYOUT[folder]
        before = {p: p.stat().st_mtime for p in base.rglob("*.json")}
        t0 = time.monotonic()
        try:
            r = subprocess.run([PY, str(d / prog)] + args, cwd=base, env=env, capture_output=True, text=True, timeout=limit)
            rc = r.returncode
            tail = (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]
        except subprocess.TimeoutExpired:
            rc, tail = "timeout", [""]
        dt = time.monotonic() - t0
        changed = [p for p in base.rglob("*.json") if p not in before or p.stat().st_mtime > before[p]]
        notes = []
        for p in sorted(changed):
            # a file is compared with the shipped copy of the certificate folder it was restored from (usually the
            # program's own folder; the recomputation in numerics_code writes into numerics_data)
            where = [f for f, sub in LAYOUT.items() if sub and base / sub == p.parent]
            shipped = cert / (where[0] if where else folder) / p.name
            if not where or not shipped.exists():
                notes.append(f"{p.name}: new")
                continue
            a, b = strip(json.loads(p.read_text())), strip(json.loads(shipped.read_text()))
            verdict = classify(diff_paths(a, b), a, b)
            notes.append(f"{p.name}: " + verdict)
            if verdict.startswith("same values; recorded input hashes differ"):
                # The values agree, but the rewritten file records hashes of inputs regenerated in this run, which later
                # programs check against those inputs: keep it, and carry over the review entries of the shipped file.
                new, old = json.loads(p.read_text()), json.loads(shipped.read_text())
                for k in REVIEW_KEYS + REVIEW_ANNOTATIONS:
                    if k in old:
                        new[k] = old[k]
                p.write_text(json.dumps(new, indent=2) + "\n")
            elif not verdict.startswith("DIFFERS"):
                # The recomputation reproduced the shipped values. Later programs read the reviewed shipped file (with
                # its review verdict and recorded hashes), as they did when the certificates were produced.
                p.write_bytes(shipped.read_bytes())
        line = f"{folder}/{prog} {' '.join(args)} | rc {rc} | {dt:.1f} s | {'; '.join(notes) or 'no JSON output'} | {tail[0][:100]}"
        print(line, flush=True)
        log.append(line)
    (base / "run_checks.log").write_text("\n".join(log) + "\n")
    bad = [l for l in log if "| rc 0 |" not in l]
    print(f"{len(log)} programs, {len(bad)} with nonzero exit or timeout")


if __name__ == "__main__":
    main()

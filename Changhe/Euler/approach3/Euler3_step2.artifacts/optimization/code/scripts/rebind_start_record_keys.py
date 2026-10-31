#!/usr/bin/env python
"""R3 start rebind (lead JK review RB1-RB5, 2026-10-26): write a NEW start file next to the old one with z and config bitwise unchanged, the fifteen inherited
top-level records of the source state moved under source_history (with a note), a new top-level meta naming the true source, the top-level pivot as the dict of
meta_perturb.pivot_recomputed_on_perturbed, no top-level modes; then the RB5 checks (reload, z bitwise, config equal, key set, source_history values byte-identical,
worker-style embed_state(z) == z bitwise) with a JSON summary. CPU only; no job. Usage: rebind_start_record_keys.py OLD.pt NEW.pt --source SRC.pt --summary OUT.json"""
import sys, os, json, argparse, hashlib, ast, pickle, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); sys.path.insert(0, ROOT)
import torch; torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.transfer import embed_state
ap = argparse.ArgumentParser(); ap.add_argument("old"); ap.add_argument("new"); ap.add_argument("--source", required=True); ap.add_argument("--summary", required=True)
ap.add_argument("--pivot", choices=["recomputed", "saved"], default="recomputed", help="top-level pivot: the dict of meta_perturb.pivot_recomputed_on_perturbed (R3) or the saved source pivot kept (R1, lead JM (2))")
ap.add_argument("--modes", choices=["omit", "auto"], default="omit", help="auto: keep top-level modes only if they equal the job model's mode list exactly (lead JM (2)); otherwise omit")
a = ap.parse_args()
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def bsha(obj): return hashlib.sha256(pickle.dumps(obj, protocol=4)).hexdigest()
S = torch.load(a.old, map_location="cpu", weights_only=False)
keep = {"z", "config", "free_params", "embedded_from_source_config", "meta_perturb"}
moved = {k: S[k] for k in S if k not in keep}
new = {k: S[k] for k in keep if k in S}
new["source_history"] = dict(moved); new["source_history"]["note"] = ("records of the source state runs/nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/starts/start_000.pt (sha " + sha(a.source)[:8] + "...), copied by perturb_start.py; not measurements of this start")
mp = S["meta_perturb"]
if a.pivot == "recomputed":
    piv = mp.get("pivot_recomputed_on_perturbed"); piv = ast.literal_eval(piv) if isinstance(piv, str) else dict(piv)
else:
    piv = dict(S["pivot"])                                                         # the saved source pivot kept (same basis; its sin-part is zero for this start by construction)
new["pivot"] = dict(piv)
modes_kept = False
if a.modes == "auto" and "modes" in S:
    cfg0 = S["config"]
    mj = Model(L=cfg0["L"], Nk=cfg0["Nk"], m_parity=cfg0.get("m_parity", "even"), R0=cfg0.get("R0", 1.0), Nr=cfg0.get("Nr"), c_l=cfg0["c_l"], omega=cfg0["omega"], free_params=False, channels=cfg0.get("channels"), device="cpu")
    if list(map(tuple, S["modes"])) == list(map(tuple, mj.modes)):
        new["modes"] = S["modes"]; modes_kept = True
new["meta"] = dict(family="perturbed_start", source=a.source, source_sha256=sha(a.source), tool="scripts/perturb_start.py", tool_sha256=sha(os.path.join(ROOT, "scripts", "perturb_start.py")),
                   rebind_script="scripts/rebind_start_record_keys.py", rebind_script_sha256=sha(os.path.abspath(__file__)), prior_file_sha256=sha(a.old),
                   m_select=mp.get("acceptance", {}).get("m_select"), size=mp.get("size"), seed=mp.get("seed"), pivot_rule=a.pivot, modes_rule=("kept: equal to the job model's mode list" if modes_kept else "not written (the job model's mode list is rebuilt from config)"),
                   note="no residual, cost or diagnostic values: those come from the job's own S3-1 and S3-22 records")
torch.save(new, a.new)
# ---- RB5 checks ----
R = torch.load(a.new, map_location="cpu", weights_only=False); O = torch.load(a.old, map_location="cpu", weights_only=False)
chk = {}
chk["z_bitwise_equal"] = bool(torch.equal(R["z"], O["z"])); chk["z_raw_sha256_old"] = hashlib.sha256(O["z"].numpy().tobytes()).hexdigest(); chk["z_raw_sha256_new"] = hashlib.sha256(R["z"].numpy().tobytes()).hexdigest()
chk["config_equal"] = (R["config"] == O["config"]); chk["config_sha256"] = bsha(R["config"])
expected_keys = (set(O.keys()) - set(moved.keys())) | {"source_history", "meta", "pivot"} | ({"modes"} if modes_kept else set())
chk["key_set_as_specified"] = (set(R.keys()) == expected_keys); chk["new_keys"] = sorted(R.keys()); chk["moved_keys"] = sorted(moved.keys()); chk["n_moved"] = len(moved)
chk["source_history_values_byte_identical"] = all(bsha(R["source_history"][k]) == bsha(O[k]) for k in moved)
chk["embedded_from_source_config_unchanged"] = (bsha(R.get("embedded_from_source_config")) == bsha(O.get("embedded_from_source_config"))); chk["meta_perturb_unchanged"] = (bsha(R["meta_perturb"]) == bsha(O["meta_perturb"]))
chk["free_params_top_level"] = ("free_params" in R); chk["pivot_is_dict"] = isinstance(R["pivot"], dict); chk["pivot"] = R["pivot"]; chk["modes_top_level"] = ("modes" in R); chk["modes_kept_equal_to_job_model"] = modes_kept; chk["pivot_rule"] = a.pivot
cfg = R["config"]
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=cfg.get("free_params", False), device="cpu", channels=cfg.get("channels"), extra_r=(cfg.get("far_radii") if cfg.get("far_merged", True) else None))
msrc = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=R.get("free_params", False), channels=cfg.get("channels"), device="cpu")
ze = embed_state(R["z"].clone(), msrc, model); chk["worker_embed_state_returns_z_bitwise"] = bool(torch.equal(ze, R["z"]))
chk["shas"] = dict(new_file=sha(a.new), old_file=sha(a.old), rebind_script=sha(os.path.abspath(__file__)), transfer_py=sha(os.path.join(ROOT, "src", "optimization", "transfer.py")), fields_py=sha(os.path.join(ROOT, "src", "equations", "fields.py")), perturb_start_py=sha(os.path.join(ROOT, "scripts", "perturb_start.py")))
chk["utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()); chk["all_pass"] = all(v is True for k, v in chk.items() if k in ("z_bitwise_equal", "config_equal", "key_set_as_specified", "source_history_values_byte_identical", "embedded_from_source_config_unchanged", "meta_perturb_unchanged", "free_params_top_level", "pivot_is_dict", "worker_embed_state_returns_z_bitwise")) and (chk["modes_top_level"] == modes_kept)
json.dump(chk, open(a.summary, "w"), indent=1, default=str); print(json.dumps({k: chk[k] for k in chk if k not in ("new_keys", "moved_keys")}, indent=1, default=str))

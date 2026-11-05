#!/usr/bin/env python3
"""Discharge the actual matrix premise of the completed m115 residual bound."""
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
from flint import arb, fmpq as Q, ctx

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OLD=HERE.parents[1]/"combined2/IPM.artifacts"


def read(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
    x=F(x); return arb(x.numerator)/arb(x.denominator)


def main():
    ctx.prec=512
    matrix_path=HERE/"operator_theory/matrix_prefix_signed_far_v01/result.json"
    matrix=read(matrix_path)
    assert matrix["status"]=="CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR"
    assert matrix["configuration"]["beta"]=="7/10"
    audit_path=HERE/"independent_closure_audit/matrix_prefix_audit.json"
    audit=read(audit_path)
    assert audit["status"]=="INDEPENDENT_MATRIX_PREFIX_AUDIT_PASS"
    for name,h in audit["bindings"].items(): assert sha(HERE/name)==h
    assert str(matrix_path.relative_to(HERE)) in audit["bindings"]
    norm_path=OLD/"theory_audit/research/source013_hermite_majorant/verification/result_v01.json"
    norm=read(norm_path)
    norm_audit_path=OLD/"numerical_audit/research/source013_hermite_majorant_audit/verification/check_v01.json"
    norm_audit=read(norm_audit_path)
    assert norm_audit["status"]=="PASS" and norm["source"]==norm_audit["source"]
    assert norm["energy_upper_exact"]==norm_audit["energy_upper_exact"]
    assert norm["source"]["raw_sha256"]==matrix["configuration"]["source_hashes"]["phi013"]
    assert norm["source"]["fixed_c_exact"]=="4076476460239181/2251799813685248"
    cert_path=HERE/"coercivity_residual/full_matrix_residual_m115_v01.cert.json"
    cert=read(cert_path)
    assert cert["source_hashes"]==matrix["configuration"]["source_hashes"]
    assert cert["code_sha256"]==sha(HERE/"coercivity_residual/assemble_full_matrix_residual_bound_v02.py")
    for name,h in cert["inputs"].items(): assert sha(REPO/name)==h
    finite_path=HERE/"coercivity_residual/m115_B_finiteness_audit_v01.json"
    finite=read(finite_path)
    assert finite["status"]=="FINITE_SCALARS_CONFIRMED" and not finite["nonfinite_values"]
    for name,h in finite["files"].items(): assert sha(REPO/name)==h
    n=F(cert["inherited_source_norm_upper"])
    assert Q(norm["fractional_norm_interval_exact"][1])<=Q(n.numerator,n.denominator)
    assert norm["fractional_order_exact"]=="21/10"
    beta=F(13999,20000); row=cert["by_beta"][str(beta)]
    coordinate=arb(cert["absolute_coordinate_lower"]).lower()
    Gamma=arb(row["Gamma_upper"]).abs_upper(); B=arb(row["B_upper"]).abs_upper()
    d2=aa(n)**2/aa(beta)-coordinate**2/(aa(beta)**2*(Gamma+B/aa(beta)))
    d2=max(d2.abs_upper(),arb(row["full_matrix_d_squared_upper"]).abs_upper())
    d=d2.sqrt();neff=aa(beta).sqrt()*d
    assert d<aa(F(660344,10**8)) and neff<aa(F(552464,10**8))
    paths=[matrix_path,audit_path,norm_path,norm_audit_path,cert_path,finite_path]
    out={"status":"ACTUAL_FULL_MATRIX_RIESZ_RESIDUAL_BOUND_JOINED",
         "finished_utc":datetime.now(timezone.utc).isoformat(),"program_sha256":sha(Path(__file__)),
         "input_sha256":{str(p.relative_to(REPO)):sha(p) for p in paths},
         "actual_global_matrix_lower":"7/10","free_baseline":str(beta),
         "inherited_N_forcing_upper":str(n),"full_matrix_dual_squared_upper":d2.str(90),
         "full_matrix_dual_upper":d.str(90),"effective_source_upper":neff.str(90),
         "rounded_dual_upper":"660344/100000000","rounded_effective_source_upper":"552464/100000000",
         "scope":"Whole-plane original-N Riesz residual bound with actual matrix premise discharged. Established inherited same-source forcing certificates retained. Not a Q residual bound or an existence theorem."}
    (HERE/"ACTUAL_FULL_MATRIX_RESIDUAL_JOIN.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__": main()

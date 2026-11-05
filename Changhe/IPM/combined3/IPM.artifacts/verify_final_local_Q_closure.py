#!/usr/bin/env python3
"""Independent scalar reconstruction of the complete fixed-parameter join.

This does not import the main consumer or the nonlinear calculator. It
reassembles source energies, rebuilds every rate and nonlinear constant,
and binds the main consumer's complete certificate inputs and raw chunks.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent


def read(p):
    return json.loads(Path(p).read_text())


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def aa(x):
    x = F(x)
    return arb(x.numerator)/arb(x.denominator)


def upper(x):
    v = arb(x)
    assert v.is_finite()
    return v.abs_upper()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--consumer", type=Path, default=HERE/"operator_theory/fixed_parameter_closure_v01.json")
    ap.add_argument("--bits", type=int, default=768)
    ap.add_argument("--out", type=Path, default=HERE/"ROOT_FINAL_LOCAL_Q_REPLAY.json")
    args = ap.parse_args()
    ctx.prec = args.bits
    main_result = read(args.consumer)
    assert main_result["status"] == "FINAL_NUMERICAL_CLOSURE_PASS"
    assert main_result["all_input_bindings_and_covers_checked"]
    consumer = HERE/"operator_theory/assemble_fixed_parameter_closure_v01.py"
    assert sha(consumer) == main_result["consumer_sha256"]
    assert set(main_result["input_paths"]) == set(main_result["input_sha256"])
    for name,path in main_result["input_paths"].items():
        assert sha(HERE/path) == main_result["input_sha256"][name]
    assert sha(HERE/"finite_rank/Qnorm_nonlinear_bound.py") == main_result["nonlinear_code_sha256"]
    assert sha(HERE.parents[1]/"combined2/IPM.report.md") == main_result["inherited_source_report_sha256"]
    input_paths = {
        "matrix": HERE/main_result["matrix_certificate_path"],
        "local": HERE/"local_energy_coefficients_v01/result.json",
        "source_constants": HERE/"finite_rank/Q_source_certificate_v01/result.json",
        "source_envelopes": HERE/"source_envelopes_v01/result.json",
        "far_source": HERE/"Q_far_source_highpass_result.json",
    }
    for name,path in input_paths.items():
        assert sha(path) == main_result["input_sha256"][name]
    for name,h in main_result["chunk_sha256"].items():
        assert sha(HERE/name) == h
    source_path = input_paths["source_constants"]
    source = read(source_path)
    assert source["status"] == "CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS"
    cfg = source["configuration"]
    assert read(source_path.parent/"configuration.json") == cfg
    for name,h in cfg["code_hashes"].items():
        assert sha(HERE/name) == h
    raw = {}
    for path in sorted(source_path.parent.glob("chunk_*.json")):
        data = read(path)
        assert data["configuration"] == cfg
        for row in data["rows"]:
            assert row["index"] not in raw
            raw[row["index"]] = row
    assert sorted(raw) == list(range(cfg["panels"]))
    lo,hi,ratio = map(F,[cfg["rmin"],cfg["rmax"],cfg["ratio"]])
    assert lo*ratio**(cfg["panels"]-1) < hi <= lo*ratio**cfg["panels"]
    core = [sum((arb(raw[i]["energy_upper"][str(j)]) for i in sorted(raw)), arb(0)) for j in range(6)]
    totals = [core[j]+arb(source["tail_energies"]["origin"][j])+arb(source["tail_energies"]["exterior"][j]) for j in range(6)]
    assert all(t.is_finite() and t>0 for t in totals)
    D = {j+1: max(totals[j].sqrt().abs_upper(),upper(source["D_b_L2_upper"][str(j+1)])) for j in range(4)}
    X = {2:max((totals[4]+4*totals[0]).sqrt().abs_upper(),upper(source["D_xb_L2_upper"]["2"])),
         4:max((totals[5]+16*totals[2]).sqrt().abs_upper(),upper(source["D_xb_L2_upper"]["4"]))}
    H1 = max([upper(source["H1_upper"]),upper(source["tail_energies"]["origin_H1_bound"]),
              upper(source["tail_energies"]["exterior_H1_bound"])]+[upper(r["H1_upper"]) for r in raw.values()])

    def moment(data,m,s):
        s=aa(s)
        constant=1/(2*(arb.pi()*s/2).cos().sqrt()*(1-s)**((1-s)/4)*(1+s)**((1+s)/4))
        return constant*data[m]**((1-s)/2)*data[m+2]**((1+s)/2)
    def A(s):
        return moment(D,2,s)+2*moment(X,2,s)+4*moment(D,1,s)
    A2=max(A(F(0)).abs_upper(),upper(source["A_s_upper"]["2"]))
    Aq=max(A(F(1,10)).abs_upper(),upper(source["A_s_upper"]["21/10"]))
    U2=(D[1]*D[3]).sqrt()/2
    U3=(D[2]*D[4]).sqrt()/2
    XU3=((X[2]+(arb(2).sqrt()+1)*D[1])*(X[4]+(arb(2).sqrt()+1)*D[3])).sqrt()/2
    T3=aa(F(51,1000))*(U3+2*XU3+6*U2)
    assert F(7,100)**2 < F(51,1000)**2*F(19,10)

    local_audit_path=HERE/"ROOT_LOCAL_COEFFICIENT_ASSEMBLY.json"
    local_audit=read(local_audit_path)
    assert local_audit["status"] == "ROOT_LOCAL_COEFFICIENT_ASSEMBLY_PASS"
    assert local_audit["program_sha256"] == sha(HERE/"verify_local_coefficient_assembly.py")
    for name,h in local_audit["input_sha256"].items(): assert sha(HERE/name)==h
    K1=upper(local_audit["K1_recomputed"]);K0=upper(local_audit["K0_recomputed"]);Wu2=upper(local_audit["Wu2_upper"])
    selected=main_result["selected"]
    mr=F(selected["M"]);rb=selected["source_split_radius"]
    assert mr==F(3,10) and rb==30000
    R=aa(F(381377,10**12));M=aa(mr);r=R/M
    q=aa(F(21,10));c=aa(F(4076476460239181,2251799813685248));beta=aa(F(7,10))
    beta2=aa(F(2087491,10**6));f2=aa(F(7961207,10**13));n=aa(F(759,100000))
    assert R*beta2>f2
    near=next(v for v in read(input_paths["source_envelopes"])["rows"] if v["cut_R"]==rb)
    far=next(v for v in read(input_paths["far_source"])["rows"] if v["R"]==rb)
    a0,a1,bfar=upper(near["a0"]),upper(near["a1"]),upper(far["B"])
    bnear=(a0*a0+4*a1*a1).sqrt();efar=3*bfar*bfar/(4*(c+1-beta))
    terms=[("local_gradient",K1,F(20,21)),("local_scalar",K0,F(40,21)),
           ("lower_source_near",bnear,F(20,21)),("transport_second",q*aa(F(1,10))*Wu2/2,F(10,21)),
           ("transport_third",T3,F(11,21)),("source_principal",q*H1,F(10,21)),
           ("source_second",q*(q-1)*A2/2,F(20,21)),("source_fractional",q*(q-1)*Aq/2,F(1))]
    rates={name:a*r**aa(e) for name,a,e in terms};background=efar+sum(rates.values(),arb(0))

    def B(p):
        s=aa(F(p+1,1)/F(21,10))
        return (4*q*(arb.pi()*s).sin()).rsqrt()*(1-s)**(-(1-s)/2)*s**(-s/2)
    B0,B1=B(0),B(1);S1=5/(11*arb.pi()).sqrt();Ca=B0/arb(2).sqrt();Cs=B1/4
    theta=aa(F(1,21));z=q*r**aa(F(10,21));v=Ca*M*r**aa(F(11,21))
    L0=q*Cs*R**theta*M**(1-theta)+aa(F(53,100))*S1*M
    Cc=q*arb(2)**aa(F(1,10))*(B1*R**theta*M**(1-theta)+S1*M)
    P=arb(2)**aa(F(11,10))*(Ca+B0)*M*r**aa(F(11,21))
    T=q*arb(2)**aa(F(1,10))*(Ca+B1)*M*r**aa(F(11,21))
    nonlinear=L0*(1+2*z)**2+4*Cc*(aa(F(1,2))+z)*z+2*(q*v+P+T)
    b=beta-background-nonlinear;margin=b*M*M-n*M;contract=S1*M/beta2
    assert b>0 and margin>0 and contract<1
    epsilon=efar+sum(((1-aa(e/2))*rates[name] for name,a,e in terms),arb(0))
    weak=sum((aa(e/2)*rates[name]/(r*r) for name,a,e in terms),arb(0))
    er=F(main_result["global_background_tangent"]["rounded_epsilon_upper"])
    cr=F(main_result["global_background_tangent"]["rounded_weak_C_upper"])
    assert aa(er)>epsilon and aa(cr)>weak
    rounded_margin=(beta-aa(er)-nonlinear)*M*M-n*M-aa(cr)*R*R
    assert rounded_margin>0
    scalar={"background_loss":background,"nonlinear_loss":nonlinear,"frozen_exterior_decay":b,
            "selfmap_energy_margin":margin,"contraction_ratio":contract,"background_epsilon":epsilon,
            "background_weak_C":weak,"rounded_selfmap_margin":rounded_margin}
    out={"status":"ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS",
         "finished_utc":datetime.now(timezone.utc).isoformat(),"program_sha256":sha(Path(__file__)),
         "consumer_result_path":str(args.consumer.relative_to(HERE) if args.consumer.is_relative_to(HERE) else args.consumer.resolve()),
         "consumer_result_sha256":sha(args.consumer),
         "local_audit_sha256":sha(local_audit_path),"source_result_sha256":sha(source_path),
         "R":"381377/1000000000000","M":str(mr),"source_split_radius":rb,"precision_bits":ctx.prec,
         "source_core_panels_independently_reassembled":len(raw),
         "values":{k:v.str(100) for k,v in scalar.items()},"rates":{k:v.str(100) for k,v in rates.items()},
         "adopted_global_background_epsilon":str(er),"adopted_global_background_C":str(cr),
         "scope":"Independent numerical reconstruction and binding. Existence additionally uses the separately audited analytic proofs."}
    args.out.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()

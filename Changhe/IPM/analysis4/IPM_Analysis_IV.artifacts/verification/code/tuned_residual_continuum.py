"""Independent Cartesian continuum residuals for three completed tuned branches."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import argparse, gzip, json, pickle, sys, time, traceback
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb, acb, acb_poly, ctx
from stream_precision_audit import unpack
from integer_period_high_order_audit import Laurent, field, ball
ROOT=Path("research/196_tuned_residual_continuum")
ZERO=arb(0)
CONFIG={"Q5r6":(5,6,"tunedQ5_r6_p1024","180_period_five_numerical_audit",50),
        "Q6r1":(6,1,"tuned13_r1_p1024","185_period_six_numerical_audit",60),
        "Q6r6":(6,6,"tuned13_r6_p1024","185_period_six_numerical_audit",60)}
def stamp():return datetime.now(timezone.utc).isoformat(timespec="seconds")
def text(x):return x.str(45,radius=True)
def sine_coefficients(v):
    lo=v.low; hi=lo+len(v.poly)-1
    get=lambda m:v.poly[m-lo] if m>=lo else ZERO
    assert get(0).contains(0)
    out=[ZERO]*(max(hi,0)+1)
    for m in range(1,hi+1):
        x=get(m);assert (x+get(-m)).contains(0)
        if m%2:out[m]=2*x
        else:assert x.contains(0)
    return out

def supremum(coeff,k,points):
    values=[a*m**k for m,a in enumerate(coeff)]
    poly=acb_poly([acb(v) for v in values]); lower=ZERO; upper=ZERO
    for point in points:
        value=poly(point); value=value.imag if k%2==0 else value.real
        lower=lower.max(value.abs_lower());upper=upper.max(value.abs_upper())
    steps=len(points)-1
    M2=sum((abs(a)*m*m for m,a in enumerate(values)),ZERO)
    error=(arb.pi()/steps)**2*M2/8
    return dict(lower=text(lower),upper=text(upper+error),grid_upper=text(upper),interpolation_error=text(error))

def main(args):
    start=time.monotonic();ctx.prec=args.bits
    period,ri,tag,topic,baseN=CONFIG[args.case]
    source=Path("../a4-num/ckpt")/(tag+".pkl"); raw=source.read_bytes(); digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
    assert state["ring"]=="arb" and state["prec"]==1024
    assert Fraction(state["delta_exact"])==Fraction(2,period)
    oldpath=Path("research")/topic/"verification"/f"root{ri}_checks.json"; old=json.loads(oldpath.read_text())
    assert old["source"]["sha256"]==digest
    base=Path(old["source"]["archive"]);base_raw=gzip.decompress(base.read_bytes());assert sha256(base_raw).hexdigest()==old["source"]["selected_sha256"]
    base_state=pickle.loads(base_raw);del base_raw
    assert all(state[key][n]==base_state[key][n] for key in ["f","g"] for n in base_state[key])
    hsource=source.with_name(tag+"_H.json"); hraw=hsource.read_bytes();hs=json.loads(hraw)
    assert all(str(n) in hs["H"] for n in range(2*period,82,period))
    extension={key:{n:state[key][n] for n in range(baseN+1,82) if n not in base_state[key]} for key in ["f","g"]}
    packed=pickle.dumps(extension,protocol=4); archive=ROOT/"verification"/(args.case+"_extension.pkl.gz"); compressed=gzip.compress(packed,compresslevel=6,mtime=0);archive.write_bytes(compressed)
    inputs=dict(source=str(source),source_sha256=digest,base_archive=str(base),base_raw_sha256=old["source"]["selected_sha256"],extension_archive=str(archive),extension_raw_sha256=sha256(packed).hexdigest(),extension_compressed_sha256=sha256(compressed).hexdigest(),harmonic_source=str(hsource),harmonic_sha256=sha256(hraw).hexdigest())
    f={n:[arb(*unpack(x)) for x in state["f"][n]] for n in range(1,82)};g={n:[arb(*unpack(x)) for x in state["g"][n]] for n in range(1,82)};del state,base_state,extension,packed,compressed
    F={n:field(f[n],True) for n in f};G={n:field(g[n],False) for n in g};delta=Q(2,period); cminus=Q(2,period-2)
    p=lambda n:Q(1)-n*delta
    FX={n:F[n].derivative(p(n)) for n in F};FY={n:F[n].derivative(p(n),True) for n in F}
    GX={n:G[n].derivative(p(n)+1) for n in G};GY={n:G[n].derivative(p(n)+1,True) for n in G}
    evalpath=Path("../a4-num/notes")/("eval_"+tag.replace("_p1024","")+".json");eraw=evalpath.read_bytes();data=json.loads(eraw);(ROOT/"sources"/(args.case+"_peer_evaluation.json")).write_bytes(eraw)
    radii=sorted({Q(str(row["R"])) for row in data["rows"]}) if not args.radii else list(map(Q,args.radii.split(",")))
    points=[]
    for j in range(args.steps+1):
        th=arb.pi()*j/args.steps;points.append(acb(th.cos(),th.sin()))
    rows=[]
    for N in [10,20,40,80]:
        for radius in radii:
            z=(-ball(delta)*ball(radius).log()).exp();A=Laurent();B=Laurent();C=Laurent();D=Laurent();lin=Laurent();partial=Laurent();power=arb(1)
            for n in range(1,N+1):
                A=A+GX[n].scale(power);B=B+GY[n].scale(power);C=C+FX[n].scale(power);D=D+FY[n].scale(power)
                lin=lin+F[n].scale(-ball(cminus)*(n-1)*power);partial=partial+F[n].scale(power);power*=z
            res=sine_coefficients(lin+(A*D-B*C).scale(z));tail=sine_coefficients(F[N+1].scale(z**N));part=sine_coefficients(partial)
            bounds={str(k):supremum(res,k,points) for k in range(3)};tails={str(k):supremum(tail,k,points) for k in range(2)}
            poly=acb_poly([acb(v) for v in part]);partials=[]
            for angle in [Q(3,10),Q(9,10),Q(13,10)]:
                th=ball(angle);partials.append(poly(acb(th.cos(),th.sin())).imag)
            peer=next(row for row in data["rows"] if row["N"]==N and Q(str(row["R"]))==radius)
            comparisons={}
            for name,target,prefix in [("residual",bounds,"resid_k"),("next_term",tails,"tail_k")]:
                comparisons[name]={}
                for k,v in target.items():
                    reported=ball(Q(str(peer[prefix+k])));lo=arb(v["lower"]);hi=arb(v["upper"])
                    comparisons[name][k]=dict(within_one_percent=bool(reported>lo*ball(Q(99,100)) and reported<hi*ball(Q(101,100))),reported_over_lower=text(reported/lo),reported_over_upper=text(reported/hi))
            row=dict(N=N,R=str(radius),residual_bounds=bounds,next_term_bounds=tails,partial_sums=list(map(text,partials)),partial_sum_errors=[text(abs(x-ball(Q(str(y))))) for x,y in zip(partials,peer["S_N_at_angles"])],reported=peer,comparison=comparisons)
            rows.append(row);report=dict(checked_at_utc=stamp(),case=args.case,complete=False,inputs=inputs,bits=args.bits,grid_steps=args.steps,rows=rows,actual_elapsed_s=time.monotonic()-start)
            (ROOT/"verification"/(args.case+"_progress.json")).write_text(json.dumps(report,indent=2)+"\n")
            print(json.dumps(dict(case=args.case,N=N,R=str(radius),residual0=bounds["0"],actual_elapsed_s=time.monotonic()-start)),flush=True)
    changes=[]
    for radius in radii:
        group=[row for row in rows if row["R"]==str(radius)]
        for before,after in zip(group,group[1:]):
            for name in ["residual_bounds","next_term_bounds"]:
                for k,previous in before[name].items():
                    current=after[name][k]
                    changes.append(dict(R=str(radius),from_N=before["N"],to_N=after["N"],quantity=name,derivative=k,strict_decrease=bool(arb(current["upper"])<arb(previous["lower"])),strict_increase=bool(arb(current["lower"])>arb(previous["upper"]))))
    report.update(checked_at_utc=stamp(),complete=True,changes=changes,peer_evaluation_sha256=sha256(eraw).hexdigest(),all_reported_within_one_percent=all(v["within_one_percent"] for r in rows for comp in r["comparison"].values() for v in comp.values()),actual_elapsed_s=time.monotonic()-start)
    (ROOT/"verification"/(args.case+"_checks.json")).write_text(json.dumps(report,indent=2)+"\n")
    for name in ["tuned_residual_continuum.py","integer_period_high_order_audit.py","stream_precision_audit.py"]:(ROOT/"sources"/name).write_bytes((Path("code")/name).read_bytes())
    (ROOT/"sources/peer_evaluate_series.py").write_bytes(Path("../a4-num/code/evaluate_series.py").read_bytes())
    print(json.dumps(dict(case=args.case,complete=True,all_reported_within_one_percent=report["all_reported_within_one_percent"],actual_elapsed_s=report["actual_elapsed_s"])),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--case",choices=list(CONFIG),required=True);ap.add_argument("--radii");ap.add_argument("--bits",type=int,default=1024);ap.add_argument("--steps",type=int,default=2048);args=ap.parse_args()
    try:main(args)
    except Exception as e:
        failure=dict(checked_at_utc=stamp(),case=args.case,error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])
        (ROOT/"verification"/(args.case+"_FAILURE.json")).write_text(json.dumps(failure,indent=2)+"\n");print(json.dumps(failure),flush=True);raise SystemExit(1)

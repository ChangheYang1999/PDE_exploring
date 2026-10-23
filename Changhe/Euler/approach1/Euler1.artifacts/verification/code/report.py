"""Rebuild reviewable reports from saved evidence; no scientific computation."""
from __future__ import annotations
import datetime
import hashlib
import json
import os
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEAD=ROOT.parent/"e1-lead"

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(path,default=None):
    try:return json.loads(path.read_text())
    except (OSError,json.JSONDecodeError):return default

def save_text(path,text):
    tmp=path.with_suffix(path.suffix+f".{os.getpid()}.tmp")
    tmp.write_text(text);os.replace(tmp,path)

def f(value):
    if value is None:return "OPEN"
    if isinstance(value,str):return value.replace("|","/").replace("\n"," ")
    return f"{value:.6g}"

def table(headers,rows):
    return "| "+" | ".join(headers)+" |\n|"+"|".join("---" for _ in headers)+"|\n"+"".join("| "+" | ".join(f(x) for x in row)+" |\n" for row in rows)

def records():
    latest={}
    for path in sorted((ROOT/"evidence").glob("checkpoint-*.json")):
        data=read(path,{})
        if not data.get("regions") or not data.get("assessment"):continue
        key=data.get("checkpoint_sha256")
        if key is None:continue
        if key not in latest or data.get("created_utc","")>latest[key][1].get("created_utc",""):
            latest[key]=(path,data)
    return sorted(latest.values(),key=lambda row:row[1].get("created_utc",""))

def build_report(state=None):
    state=state or read(ROOT/"VALIDATOR_STATUS.json",{})
    now=utc();ledger=state.get("lane_ledger",{})
    recs=records();checks=[]
    def check(name,method,result,verdict,date=None,evidence=None):
        checks.append(dict(check=name,method=method,result=result,verdict=verdict,date_utc=date or now,evidence=evidence))
    check("Similarity signs, residual identities, gauges and seed algebra","Independent informal proofs and manufactured finite-difference tests","32 calibration tests pass. Numerical tensor identities are algebra tests; they are not independent evidence that a checkpoint solves Euler.","CONFIRMED",evidence="evidence/unit_tests.json")
    check("Checkpoint decoder on documented architectures","Nine synthetic nonzero-weight networks; NumPy tangents versus independent Torch derivatives and archive round trip","All nine cases pass, including bounded dir_tau, multiple envelopes and off-axis Gaussian blobs. No trainer model or residual module is imported.","CONFIRMED",evidence="evidence/checkpoint_decoder_tests.json")
    check("Physical-volume Fourier normalization","Exact affine energy and pure four-fold polynomial fields","Affine energy error below 9e-16; four-fold field has no resolved n=2 leakage.","CONFIRMED",evidence="evidence/physical_volume_fourier_tests.json")
    eq=read(ROOT/"evidence/equations_audit_current.json",read(ROOT/"evidence/equations_audit.json",{}))
    snapshot=eq.get("snapshot",{})
    current=(LEAD/"EQUATIONS.md").read_bytes() if (LEAD/"EQUATIONS.md").exists() else b""
    hash_now=hashlib.sha256(current).hexdigest()
    unresolved=[c for c in eq.get("checks",[]) if c["verdict"]!="CONFIRMED"]
    check("Lead EQUATIONS.md claim-by-claim audit","Snapshot and independent derivations; primary-source hypotheses",f"Audited hash {snapshot.get('sha256','missing')}; {len(eq.get('checks',[]))} entries, {len(unresolved)} non-CONFIRMED. Current source hash {'matches' if hash_now==snapshot.get('sha256') else 'differs; revision audit required'}.","CONFIRMED" if hash_now==snapshot.get('sha256') and not unresolved else "OPEN",evidence="EQUATIONS_AUDIT.md")
    check("Countable-stagnation obstruction below one half","Standalone proof including local null-graph argument","This historical theorem is correct. The stronger arbitrary-stagnation theorem L2 now removes its countability hypothesis.","CONFIRMED",evidence="research/stagnation-obstruction/PROOF.md")
    check("A universal residual floor from isolated numerical roots","Assess theorem hypotheses and limit arguments","The assertion of a universal floor from isolated sampled roots is false. A fixed normalized class with uniform tail and derivative bounds has a positive but uncomputed absolute global floor; the tested checkpoints do not certify membership in that class.","REFUTED",evidence="FLOOR_AUDIT.md")
    check("Prompt seed is an Euler profile","Independent volume shells and asymptotic expansion","Worst momentum relative RMS 0.347059 on 1<R<2 at prescribed c_l=0.45. Its generic degree d-2 correction also fails nonlinear tail balance.","REFUTED",evidence="evidence/seed-calibration-c045.json")
    check("Whole-space integral evaluator calibration","Manufactured Gaussian pressure and vortex, two quadrature resolutions","Finest pressure-gradient error 3.2e-15 and velocity error 8.2e-16.","CONFIRMED",evidence="evidence/whole_space_unit_tests.json")
    check("Whole-space pressure of the prompt seed","Independent tr(J^2) Newton quadrature through radius 256","Pressure-gradient mismatch RMS 0.139274 persists; Biot-Savart velocity mismatch reduces to 4.97e-7. Numerical checks, not certified exterior bounds.","REFUTED",evidence="evidence/seed_whole_space_c045_radius256.json")
    check("Radial feature has resolved Cartesian origin derivatives","Source repair and independent synthetic decoder cases","The audited dir_log pilot uses log1p(R^2), avoiding the previous unresolved sqrt(R^2+1e-300) scale and NaN third derivative.","CONFIRMED",evidence="PRIORITY_MODEL_FINDING.md")
    check("Generic dir_log leading-tail flexibility","Asymptotics of a tanh network with nonzero radial first-layer weights","Learned leading potential tends to a constant vector before Q projection; learned leading velocity is an axisymmetric swirl. Slow fractional corrections can overwhelm nonlinear balance. Exact zero weights and cancellations are explicit exceptions.","CONFIRMED",evidence="research/radial-feature-tails/PROOF.md")
    for entry in read(ROOT/'EXTRA_CHECKS.json',[]):
        check(entry['check'],entry['method'],entry['result'],entry['verdict'],entry.get('date_utc'),entry.get('evidence'))
    primary_recs=[row for row in recs if 0.4 < row[1]['c_l'] < 0.5]
    best=min(primary_recs,key=lambda row:row[1]['assessment'].get('worst_momentum_relative') if row[1]['assessment'].get('worst_momentum_relative') is not None else float('inf')) if primary_recs else None
    rows=[]
    for path,data in recs:
        meta=data.get('model_metadata',{});saved=meta.get('checkpoint_metadata',{})
        exp=saved.get('exp_id',saved.get('experiment_id',data['experiment_id']))
        training=saved.get('state',{})
        row=[exp,data['checkpoint_sha256'][:16],training.get('global_step'),data['c_l'],data['assessment'].get('worst_momentum_relative'),data['assessment'].get('worst_sampled_region'),data['tail']['spheres'][-1]['nonlinear_term_relative'],data['assessment']['status']]
        rows.append(row)
    primary=None
    if best:
        path,primary=best;d=primary;date=d['created_utc'];evidence=str(path.relative_to(ROOT));regions=d['regions']
        for name,threshold in [('momentum',1e-3),('divergence',1e-6),('vorticity',1e-3),('pressure_poisson',1e-3)]:
            pairs=[(k,r[name]['relative_rms']) for k,r in regions.items()]
            valid=[(k,v) for k,v in pairs if v is not None]
            worst=max(valid,key=lambda kv:kv[1]) if valid else ('degenerate',None)
            good=len(valid)==len(pairs) and worst[1]<=threshold
            check(f"Selected checkpoint {name} screening",f"Independent physical FD6; volume shells, grid and axis; threshold {threshold:g}",f"Worst relative RMS {f(worst[1])} on {worst[0]}.","CONFIRMED" if good else "REFUTED",date,evidence)
        check("Selected checkpoint Q symmetry and non-affinity","Exact rotation check and core affine least squares",f"Q velocity defect {f(d['symmetry']['Q_velocity_relative'])}; affine relative remainder {f(d['core_affine_fit']['relative_remainder'])}.","CONFIRMED" if (d['symmetry']['Q_velocity_relative'] or 0)<1e-8 and (d['core_affine_fit']['relative_remainder'] or 0)>1e-4 else "REFUTED",date,evidence)
        check("Selected checkpoint genuine n=2 signal","Cylindrical Fourier components and correct vector group average",f"Equal-ring n=2 fraction {f(d['angular']['n2_fraction'])}; sampled-core vector nonaxisymmetric fraction {f(d['vector_group_average']['nonaxisymmetric_energy_fraction'])}. Physical-volume energies appear below when available.","CONFIRMED" if (d['angular']['n2_fraction'] or 0)>1e-6 else "REFUTED",date,evidence)
        check("Selected checkpoint three-dimensional variation","Smallest eigenvalue of core derivative Gram matrix",f"Minimum normalized fraction {f(d['core_directional_dependence']['minimum_fraction'])}; this is a regional diagnostic.","CONFIRMED" if (d['core_directional_dependence']['minimum_fraction'] or 0)>1e-6 else "OPEN",date,evidence)
        check("Selected checkpoint axis Taylor structure","Cartesian derivatives and shrinking transverse tubes",f"Axis horizontal velocity RMS {f(d['axis']['axis_horizontal_velocity']['rms'])}; off-block Jacobian RMS {f(d['axis']['axis_jacobian_offblock']['rms'])}. Full refinement convergence remains untested.","CONFIRMED",date,evidence)
        check("Selected checkpoint derivative and coordinate consistency","FD4/FD6 step sweep; independently differentiate in r, theta, z",f"Cartesian/cylindrical momentum difference RMS {f(d['cartesian_cylindrical']['momentum_difference']['rms'])}.","CONFIRMED" if d['cartesian_cylindrical']['momentum_difference']['rms']<1e-7 else "OPEN",date,evidence)
        tail=d['tail']['spheres'][-1]
        check("Selected checkpoint nonlinear tail balance","Sphere directions, coordinate planes, axes and near-plane strips",f"At R={f(tail['radius'])}, momentum RMS {f(tail['momentum_rms'])}, full-term relative {f(tail['linear_term_relative'])}, nonlinear-term relative {f(tail['nonlinear_term_relative'])}.","REFUTED" if (tail['nonlinear_term_relative'] or 0)>1e-2 else "OPEN",date,evidence)
        check("Selected checkpoint stagnation geometry","Independent multistart root search and symmetric derivative probes",f"{len(d['geometry']['stagnation_points'])} zeros located from {d['geometry']['initial_guesses']} starts. Complete root count and exact local topology are not certified.","OPEN",date,evidence)
        ratios=[p.get('stretching_ratio') for p in d['geometry']['peak_vorticity']]
        check("Selected checkpoint peak stretching identity","Refine local extrema of vorticity and evaluate Omega.J.Omega/|Omega|^2",f"Refined local ratios {ratios}; exact nonzero interior extrema require 1. These are not global maximum certificates.","REFUTED" if any(v is not None and abs(v-1)>1e-2 for v in ratios) else "OPEN",date,evidence)
        check("Resolved c_l below one half","Metadata, fixed-field sensitivity, then required free refits",f"Saved c_l={d['c_l']}; gap {0.5-d['c_l']}. Trainable metadata: {d['model_metadata']['config'].get('cl_trainable',False)}. A fixed-field least-squares change is not an optimized-profile exponent.","OPEN",date,evidence)
    for name,result in [
        ('Campaign-wide training/holdout gap','One exact replayed last batch is compared with saved holdout at v2 cl045 step4476 in TRAINING_HOLDOUT_AUDIT.md. Whole-training statistics, other branches and uncertainty across batches remain open.'),
        ('Whole-space certification for trained branches','Pilot500 and v2 M1 cl045 step500 finite Newton and Biot-Savart quadratures are reported separately. An analytic exterior error bound and branch-by-branch converged comparisons remain incomplete.'),
        ('Capacity, domain, sampling and tail-model refinement','No surviving branch has completed the required convergence sequence.'),
        ('Removal of temporary nondegeneracy penalties','No accepted branch has been compared before and after release.'),
        ('Global angular and axis derivative resolution','Finite rings, shells and axis tubes cannot establish uniform derivative convergence or rule out every unresolved angular layer.'),
        ('NS viscous defect and stability','Laplacian diagnostics are saved regionally; no credible Euler candidate or controlled dynamical conclusion exists.'),
        ('Exact profile construction, stability and blowup','No nonzero exact profile was constructed. Finite residual tests establish none of these distinct results. The independently proved obstruction is stated separately.')]:
        check(name,'Audit available evidence and missing dependencies',result,'OPEN')
    check("96-hour active numerical campaign","Union of closed validation-task wall intervals",f"Verifier lane closed union {f(ledger.get('active_seconds'))} seconds. Numerics owns the shared campaign ledger; concurrent intervals must be united, not added. Idle watcher time is excluded, but these intervals are not CPU time or a certificate excluding every unlogged process suspension. The 96-hour requirement was not completed. Neither this nor the imperfect trainer ledger supports a 96-hour claim.","REFUTED")
    text="# Independent verification report\n\nUpdated: "+now+". Generated from saved evidence by validation/report.py.\n\n"
    text+="Mathematical status: RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS. The independently checked L2 theorem excludes every nonzero exact C2 globally decaying profile for 0<c_l<1/2, hence the entire primary target. Uniform sublinearity suffices for the conclusion that U is constant. The c_l=1/2 calibration and c_l>1/2 secondary possibilities are not excluded. This is an informal mathematical proof, not a computed numerical residual threshold or a general blowup theorem. See THEORY_V3_AUDIT.md, HOSTILE_THEORY_AUDIT.md and SCOPE_AUDIT.md.\n\n"
    text+="Numerical status: "+("NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH" if not any(r[1]['assessment']['status'].startswith('PRELIMINARY') for r in recs) else "PRELIMINARY SCREENING RESULT REQUIRING MANUAL GATES")+". No nonzero exact profile was constructed, and no stability or blowup theorem is established. A numerical approximation with visible two-fold structure can still fail the profile equations.\n\n"
    text+=f"There are {len(recs)} independently evaluated checkpoint hashes. The selected checkpoint below minimizes worst sampled momentum defect among the saved evaluations strictly inside 0.4<c_l<0.5; the c_l=0.5 controls remain separately labelled by their exponent in the table. It is not accepted on that criterion alone. A fixed input c_l is never called a discovered exponent.\n\n"
    if rows:text+=table(['Run','Checkpoint SHA prefix','Saved step','c_l','Worst eps_m','Worst region','Outer nonlinear tail ratio','Status'],rows)+"\n"
    text+=table(['Check','Method','Result','Verdict','Evidence date UTC'],[[c['check'],c['method'],c['result'],c['verdict'],c['date_utc']] for c in checks])+"\n"
    if primary:
        d=primary
        text+="Selected evidence: "+str(best[0].relative_to(ROOT))+". Full checkpoint SHA256: `"+d['checkpoint_sha256']+"`.\n\n"
        text+="Regional vector RMS uses Euclidean vector magnitude. Uniform volume shell estimates use physical dy and the stated finite sample count. The grid and axis line are diagnostic measures. Quantiles and maxima are sampled values, never rigorous supremum bounds.\n\n"
        text+=table(['Region','N','eps_m','eps_div','eps_omega','eps_P','Rm RMS','Rm q99','Rm q999','Rm sampled max'],[[k,r['sample_count'],*[r[t]['relative_rms'] for t in ['momentum','divergence','vorticity','pressure_poisson']],*[r['momentum']['absolute'].get(q) for q in ['rms','q99','q999','sampled_max']]] for k,r in d['regions'].items()])+"\n"
        text+="Fourier energies below, when present, integrate rho^2 d_rho d_mu d_theta over the whole ball or shell. These differ from equally weighted rings. Pressure has one regional mean subtracted for energy ratios.\n\n"
        vr=[]
        for name,region in d.get('volume_angular',{}).items():
            for field,meas in region['fields'].items():vr.append([name,field,meas['physical_L2_squared'],meas['n2_fraction'],meas['high_frequency_energy'],meas['angular_total_energy_difference']])
        text+=table(['Region','Field','Physical L2 squared','n=2 fraction','High angular energy','32/64-angle energy difference'],vr) if vr else 'Physical-volume Fourier check is pending for this checkpoint.\n'
        text+='\n'+table(['R','Velocity RMS','Rm RMS','Full-term relative','Nonlinear relative','Rm / R^(2d-1)'],[[s[k] for k in ['radius','velocity_rms','momentum_rms','linear_term_relative','nonlinear_term_relative','momentum_scaled_by_R_2d_minus_1']] for s in d['tail']['spheres']])+"\n"
        text+="Stagnation roots and vorticity extrema are finite numerical searches. Their full positions, derivatives, residuals and local probes are in the selected JSON. An apparent isolated root does not establish countability of every exact limiting profile.\n\n"
    notes=ROOT/'REPORT_NOTES.md'
    if notes.exists():text+=notes.read_text()+"\n"
    text+="CONFIRMED supports only the precisely stated property and method. REFUTED identifies a failed stated test. OPEN records missing or incomplete evidence. The current equation claim ledger is evidence/equations_audit_current.json, with dated narrative audits alongside it; standalone mathematical proofs and their scope are indexed in research/INDEX.md.\n\n"
    text+=f"Supervisor state: {state.get('status','unknown')}; PID {state.get('pid')}. Lane validation-task wall-union seconds: {f(ledger.get('active_seconds'))}, wall-union hours: {f(ledger.get('active_hours'))}; unmatched starts: {len(ledger.get('unmatched_start_ids',[]))}. Check VALIDATOR_STATUS.json and VALIDATION_LEDGER.jsonl for current intervals. Only if numerical work is reopened, resume with `cd {ROOT} && ./resume.sh`; inspect with `./status.sh`; stop with `./stop.sh`.\n\n"
    text+="The lead launch log confirms us.anthropic.claude-opus-5-5; numerics uses us.anthropic.claude-fable-5-1. Findings and counterarguments are exchanged through local files. No additional remote model execution is used. This lane uses one single-threaded checkpoint child and bounded manual audits, with fewer than four CPU workers at nice 19; GPU 4 has not been needed. No JavaScript/TypeScript, servers, RLScience access, remote compute, Lean/lake, commits or writes outside this lane.\n"
    save_text(ROOT/'VERIFY_REPORT.md',text)
    save_text(ROOT/'VERIFICATION_CHECKS.json',json.dumps(dict(updated_utc=now,checks=checks),indent=2,allow_nan=False)+'\n')
    save_text(ROOT/'CHECKPOINT_TABLE.tsv','\t'.join(['run','sha256_prefix','saved_step','c_l','worst_eps_m','worst_region','tail_nonlinear_relative','status'])+'\n'+''.join('\t'.join(f(v) for v in row)+'\n' for row in rows))
    return text

if __name__=='__main__':
    build_report()
    print(ROOT/'VERIFY_REPORT.md')

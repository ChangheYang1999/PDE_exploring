"""Independent Cartesian/gamma-beta reproduction of weighted weak bounds."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, sys, time
from flint import fmpq as Q, arb, arb_poly, ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/weighted_weak_audit'
sys.path.insert(0,str(ROOT/'research/projected_residual/code'))
from build import candidate_source, read_projection, destination
sys.path.insert(0,str(ROOT/'research/localized_weak_probe/code'))
from beta_scale import integral,groups,ap,ar,Radial,U
def digest(path):return sha256(path.read_bytes()).hexdigest()
def maximum(j,b):
    return ar(Q(j)/(j+b))**j*ar(b/(j+b))**ar(b) if j else arb(1)
def run(name):
    start=time.monotonic();ctx.prec=2048;a=Q(6,5);CU=ar(Q(808233,500000))
    velocity=ROOT/"research/weighted_velocity_audit/verification/results.json"
    vc=json.loads(velocity.read_text())
    assert any(r["a"]=="6/5" and r["C"]=="808233/500000" and r["all_checks_pass"] for r in vc["rows"])
    peerpath=BASE/f'peer_review/{name}_a6_5_2048.json'
    peer=json.loads(peerpath.read_text())
    source=candidate_source(name);model=Radial(source)
    assert peer['source_sha256']==digest(source)
    assert peer['proof_sha256']==digest(BASE/'peer_review/T4_PROOF.md')
    frozen_peer_code_sha=digest(BASE/'peer_review/T4_evaluate_a6_5.py')
    assert Q(peer['a'])==a and arb(peer['velocity_constant']).contains(CU)
    projected,metadata=read_projection(name)
    F=[(ell,ap(P(U))) for ell,P in projected.items()]
    bg=groups(model,['u1','u2']);cg=groups(model,['rho_x','rho_y'])
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'candidate':name,'a':str(a),'velocity_constant':'808233/500000','velocity_certificate_sha256':digest(velocity),'precision_bits':ctx.prec,
         'source_sha256':digest(source),'projection_sha256':digest(destination(name)),
         'peer_result_sha256':digest(peerpath),'code_sha256':digest(Path(__file__)),
         'peer_recorded_code_sha256':peer['code_sha256'],
         'frozen_current_peer_code_sha256':frozen_peer_code_sha,
         'peer_code_hash_matches_frozen_current':peer['code_sha256']==frozen_peer_code_sha,
         'peer_code_provenance_scope':'Current peer file may postdate the result. This calculation does not execute it.',
         'proof_sha256':digest(BASE/'PROOF.md'),
         'method':'Cartesian field squares and projected residual, gamma-beta moments',
         'rows':[]}
    print('prepared',name,time.monotonic()-start,flush=True)
    for row in peer['rows']:
        tick=time.monotonic();k=row['k'];weight=arb_poly([5,2*k-4])
        ell=arb_poly([ar(1-model.c),ar(2*model.c*(k+2))])
        A2=arb.pi()/2*integral(ell*ell,1-a,2*k+1)
        B2=arb.pi()/2*sum((integral(P*weight*weight,b-a,2*k+1) for b,P in bg.items()),arb(0))
        C2=arb.pi()/2*sum((integral(P,b-a,2*k+1) for b,P in cg.items()),arb(0))
        assert A2>0 and B2>0 and C2>0
        A,B,C=A2.sqrt(),B2.sqrt(),C2.sqrt();D=A+B+CU*C
        pairing=arb.pi()/2*sum((integral(P,ell*model.delta/2-1,k+1) for ell,P in F),arb(0))
        H=arb(1) if k==0 and a<=Q(3,2) else maximum(k,2-a)+2*k*maximum(k,3-a)+4*maximum(k+1,2-a)
        I=abs(pairing);assert I>0
        radius=2*I/(D+(D*D+4*CU*H*I).sqrt())
        values={'pairing':pairing,'A':A,'B_upper':B,'C_upper':C,'D':D,
                'gradient_sup_upper':H,'weighted_L2_radius_lower':radius}
        matches={key:bool(value.overlaps(arb(row[key]))) for key,value in values.items()}
        assert all(matches.values()),(name,k,matches)
        out['rows'].append({'k':k,**{key:value.str(90) for key,value in values.items()},
                            'peer_comparisons':matches,'elapsed_seconds':time.monotonic()-tick})
        print('k',k,'radius',radius.str(30),'all comparisons pass',flush=True)
    out['elapsed_seconds']=time.monotonic()-start
    dest=BASE/f'verification/{name}_a6_5_2048.json';assert not dest.exists()
    dest.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    for name in sys.argv[1:]:run(name)

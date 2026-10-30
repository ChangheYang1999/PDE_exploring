"""Finite large-scale weighted weak probes; no asymptotic approximation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import fmpq as Q,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/weighted_weak_audit'
sys.path.insert(0,str(BASE/'code'))
from check import candidate_source,Radial,read_projection,destination,groups,ap,ar,U,maximum,integral

def digest(p):return sha256(p.read_bytes()).hexdigest()
def run(name):
    start=time.monotonic();ctx.prec=2048
    source=candidate_source(name);model=Radial(source)
    projected,_=read_projection(name);F=[(ell,ap(P(U))) for ell,P in projected.items()]
    bg=groups(model,['u1','u2']);cg=groups(model,['rho_x','rho_y'])
    vp=ROOT/'research/weighted_velocity_audit/verification/results.json'
    vc={Q(r['a']):Q(r['C']) for r in json.loads(vp.read_text())['rows'] if r['all_checks_pass']}
    ks=[0]+[2**j for j in range(0,49,2)]
    pairs={k:arb.pi()/2*sum((integral(P,ell*model.delta/2-1,k+1) for ell,P in F),arb(0)) for k in ks}
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,
         'precision_bits':ctx.prec,'R':'1','source_sha256':digest(source),
         'projection_sha256':digest(destination(name)),'velocity_certificate_sha256':digest(vp),
         'code_sha256':digest(Path(__file__)),'proof_sha256':digest(BASE/'PROOF.md'),
         'scale_proof_sha256':digest(BASE/'PROOF_SCALES.md'),
         'beta_code_sha256':digest(ROOT/'research/localized_weak_probe/code/beta_scale.py'),
         'scope':'Finite prescribed scales; necessary correction distances; new scales await independent reproduction.',
         'rows':[]}
    dest=BASE/f'verification/{name}_scale_scan_2048.json';assert not dest.exists()
    for a in [Q(6,5),Q(13,10),Q(7,5),Q(3,2)]:
        CU=ar(vc[a]);best=None
        peerpath=BASE/f'verification/{name}_a{a.numerator}_{a.denominator}_2048.json'
        refs={r['k']:r for r in json.loads(peerpath.read_text())['rows']} if peerpath.exists() else {}
        for k in ks:
            tick=time.monotonic();weight=arb_poly([5,2*k-4])
            ell=arb_poly([ar(1-model.c),ar(2*model.c*(k+2))])
            A2=arb.pi()/2*integral(ell*ell,1-a,2*k+1)
            B2=arb.pi()/2*sum((integral(P*weight*weight,b-a,2*k+1) for b,P in bg.items()),arb(0))
            C2=arb.pi()/2*sum((integral(P,b-a,2*k+1) for b,P in cg.items()),arb(0))
            assert A2>0 and B2>0 and C2>0
            A,B,C=A2.sqrt(),B2.sqrt(),C2.sqrt();D=A+B+CU*C
            H=arb(1) if k==0 and a<=Q(3,2) else maximum(k,2-a)+2*k*maximum(k,3-a)+4*maximum(k+1,2-a)
            pair=pairs[k];I=abs(pair);assert I>0
            radius=2*I/(D+(D*D+4*CU*H*I).sqrt());assert radius>0
            values={'pairing':pair,'A':A,'B_upper':B,'C_upper':C,'D':D,
                    'gradient_sup_upper':H,'weighted_L2_radius_lower':radius}
            match={key:bool(v.overlaps(arb(refs[k][key]))) for key,v in values.items()} if k in refs else {}
            assert all(match.values())
            out['rows'].append({'a':str(a),'C_U':str(vc[a]),'k':k,
                **{key:v.str(85) for key,v in values.items()},'existing_result_comparisons':match,
                'elapsed_seconds':time.monotonic()-tick})
            if best is None or radius>best[1]:best=(k,radius)
            out['elapsed_seconds']=time.monotonic()-start
            dest.write_text(json.dumps(out,indent=2)+'\n')
        print(name,'a',a,'best k',best[0],'radius',best[1].str(35),flush=True)
    print('elapsed',time.monotonic()-start,flush=True)
if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'state131')

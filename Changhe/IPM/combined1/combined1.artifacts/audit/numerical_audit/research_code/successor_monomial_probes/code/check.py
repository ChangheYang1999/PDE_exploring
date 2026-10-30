"""Whole-plane monomial probes from a direct Cartesian residual projection."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, importlib.util, json, sys, time
from flint import fmpq as Q, arb, arb_poly, ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/successor_monomial_probes'
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'research/localized_weak_probe/code'))
from beta_scale import integral,groups,ap,ar,Radial,U
spec=importlib.util.spec_from_file_location('n4_projection',ROOT/'research/successor_weak_probes/code/check.py')
W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()

def run(name,n,k,bits):
    start=time.monotonic();ctx.prec=bits
    assert n>0 and n%2 and k>=(n-1)//2
    dest=BASE/f'verification/{name}_n{n:03d}_K{k:05d}.json'
    assert not dest.exists()
    src=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
    audit_path=ROOT/f'research/candidate_audits/verification/{name}.json'
    audit=json.loads(audit_path.read_text())
    assert H(src)==audit['canonical_sha256'] and all(audit['snapshot_hashes_confirmed'].values())
    assert audit['all_forbidden_zero'] and audit['B0n_exact']
    model=Radial(src)
    assert model.c>1 and model.state['source_sha256']==audit['generator_sha256']
    bg=groups(model,['u1','u2']);cg=groups(model,['rho_x','rho_y'])
    projection,pairs=W.project(model,n)
    assert projection and all(ell*model.delta/2-1>-1 for ell in projection)
    print('PREPARED',name,'n',n,'K',k,'branches',len(projection),'seconds',time.monotonic()-start,flush=True)
    dp=arb_poly([-3,2*k+4])
    bg0=arb.pi()/2*sum((integral(P,b,2*k+1) for b,P in bg.items()),arb(0))
    bgd=arb.pi()/2*sum((integral(P*dp*dp,b,2*k+1) for b,P in bg.items()),arb(0))
    cc=arb.pi()/2*sum((integral(P,b,2*k+1) for b,P in cg.items()),arb(0))
    a=Q(2*k+2);l0=3*model.c+1+2*model.c*k;l1=2*model.c*(k+2)
    aa=arb.pi()/2*ar((l0*l0-2*l0*l1*a/(a+2)+l1*l1*a*(a+1)/((a+2)*(a+3)))/(a*(a+1)))
    assert all(x>0 and x.rel_accuracy_bits()>150 for x in [bg0,bgd,cc,aa])
    A,B,C=aa.sqrt(),(bgd+n*n*bg0).sqrt(),cc.sqrt();D=A+B+C
    pair=arb.pi()/2*sum((integral(ap(P(U)),ell*model.delta/2-1,k+1) for ell,P in projection.items()),arb(0))
    assert abs(pair)>0 and pair.rel_accuracy_bits()>150
    h=Q(max(2*k+1,3))*(Q(4*k**k,(k+2)**(k+2)) if k else Q(1))
    radius=2*abs(pair)/(D+(D*D+4*ar(h)*abs(pair)).sqrt())
    floor=W.strict_floor(radius)
    vals={'pairing':pair,'A':A,'B_upper':B,'C_upper':C,'D_upper':D,'L2_radius_lower':radius}
    calibration={};calpath=None
    if name.startswith('C1-N1-007-'):
        calpath=ROOT/f'research/angular_weak_probes/verification/n{n:03d}_K{k:05d}.json'
        previous=json.loads(calpath.read_text())
        assert previous['candidate']==name and previous['n']==n and previous['K']==k
        assert Q(previous['H_upper_exact'])==h
        calibration={key:value.overlaps(arb(previous[key])) for key,value in vals.items()}
        assert all(calibration.values())
    else:
        calpath=BASE/f'verification/C1-N1-007-d2w-j7-e2bal_n{n:03d}_K{k:05d}.json'
        cal=json.loads(calpath.read_text())
        assert all(cal['candidate007_calibration'].values())
        assert cal['code_sha256']==H(__file__) and cal['n']==n and cal['K']==k
    paths=[src,audit_path,Path(__file__),BASE/'PROOF.md',
           ROOT/'research/successor_weak_probes/code/check.py',
           ROOT/'research/angular_weak_probes/PROOF.md',
           ROOT/'research/angular_weak_probes/code/check.py',
           ROOT/'research/localized_weak_probe/code/beta_scale.py',
           ROOT/'research/localized_weak_probe/code/evaluate.py',
           ROOT/'research/radial_fourier/code/radial.py',calpath]
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'n':n,'K':k,'bits':bits,
         'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},'code_sha256':H(__file__),
         'canonical_sha256':H(src),'generator_sha256':audit['generator_sha256'],
         'projection_sha256':W.poly_hash(projection),'projection_pairs':pairs,
         'projection_radial_branches':len(projection),
         'whole_plane':True,'all_background_angular_modes':True,
         'candidate007_calibration':calibration,
         **{key:value.str(100) for key,value in vals.items()},
         'H_upper_exact':str(h),'strict_lower_exact':str(floor),'strict_floor_verified':True,
         'pairing_accuracy_bits':pair.rel_accuracy_bits(),
         'energy_accuracy_bits':[x.rel_accuracy_bits() for x in [aa,bg0,bgd,cc]],
         'elapsed_seconds':time.monotonic()-start,
         'status':'OPEN independent candidate numerical reproduction'}
    with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('DONE',name,n,k,'radius',radius.str(25),'floor',str(floor),'seconds',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate',nargs='+');p.add_argument('--n',type=int,default=21);p.add_argument('--K',type=int,default=522);p.add_argument('--bits',type=int,default=2048)
    a=p.parse_args();assert a.bits>=1024
    for name in a.candidate:run(name,a.n,a.K,a.bits)

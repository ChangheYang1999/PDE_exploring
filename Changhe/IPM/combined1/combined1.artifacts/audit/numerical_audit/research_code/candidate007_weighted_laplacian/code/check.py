"""Resumable exact all-mode Cartesian Laplacian and finite-power integration."""
from datetime import datetime, timezone
from pathlib import Path
from hashlib import sha256
import argparse
import json
import sys
import time
from flint import arb, ctx, fmpq as Q

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/candidate007_weighted_laplacian'
NAME = 'C1-N1-007-d2w-j7-e2bal'
sys.path.insert(0, str(ROOT/'research/whole_plane_norms/code'))
from pipeline import load, source
from norms import derivative, ar, T, U, ZERO


def H(p):
    h=sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def write_new(p,d):
    assert not p.exists(),p
    p.write_text(json.dumps(d,indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seconds',type=float,default=450)
    parser.add_argument('--max-modes',type=int,default=10000)
    args=parser.parse_args()
    start=time.monotonic(); ctx.prec=2048
    src=source(NAME)
    assert H(src)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
    cache=ROOT/f'research/whole_plane_norms/data/{NAME}_D0.json.gz'
    assembly=ROOT/f'research/whole_plane_norms/verification/{NAME}_assembly.json'
    ainfo=json.loads(assembly.read_text())
    assert ainfo['source_sha256']==H(src) and ainfo['polynomial_sha256']==H(cache)
    dependencies=[src,cache,assembly,Path(__file__),BASE/'PROOF.md',
        ROOT/'research/whole_plane_norms/code/pipeline.py',
        ROOT/'research/whole_plane_norms/code/norms.py',
        ROOT/'research/whole_plane_norms/code/packed_tight.py',
        ROOT/'research/radial_fourier/code/radial.py',
        ROOT/'research/projected_laplacian_audit/verification/candidate007_modes13.json']
    inputs={str(p.relative_to(ROOT)):H(p) for p in dependencies}
    raw=json.loads(src.read_text()); c=Q(raw['cl']); delta=1-1/c; A=1+1/c
    weights=sorted(set([Q(k,5) for k in range(5)]+[Q(k,4) for k in range(7)]+[A]))
    F=load(NAME,0)[0,0]
    assert all(kind=='s' and n>0 for ell,kind,n in F)
    modes=sorted(set(n for ell,kind,n in F))
    manifest={'candidate':NAME,'precision_bits':ctx.prec,'c':str(c),'weights':[str(a) for a in weights],
              'modes':modes,'residual_components':len(F),'inputs':inputs}
    mp=BASE/'verification/manifest.json'
    if mp.exists():assert json.loads(mp.read_text())==manifest
    else:write_new(mp,manifest)
    mhash=H(mp)
    anchor=json.loads(dependencies[-1].read_text())
    anchorrows={(row['mode'],Q(row['a'])):row for row in anchor['rows']}
    print('loaded',len(F),'components',len(modes),'modes',time.monotonic()-start,flush=True)
    completed={}; fresh=0
    for n in modes:
        p=BASE/f'verification/modes/mode_{n:03d}.json'
        if p.exists():
            rec=json.loads(p.read_text());assert rec['manifest_sha256']==mhash and rec['mode']==n
            assert [x['a'] for x in rec['weights']]==manifest['weights']
            completed[n]=rec
            continue
        if time.monotonic()-start>=args.seconds or fresh>=args.max_modes:continue
        ms=time.monotonic()
        Fn={key:V for key,V in F.items() if key[2]==n}
        dx=derivative(Fn,0,'x',delta);dy=derivative(Fn,0,'y',delta)
        assert derivative(dx,1,'y',delta)==derivative(dy,1,'x',delta)
        xx=derivative(dx,1,'x',delta);yy=derivative(dy,1,'y',delta)
        lap={key:xx.get(key,ZERO)+yy.get(key,ZERO) for key in set(xx)|set(yy)}
        lap={key:V for key,V in lap.items() if V}
        td=lambda V,d:(1-2*d*T)*V+2*T*U*V.derivative()
        polar={key:td(td(V,key[0]*delta/2),key[0]*delta/2)-n*n*V for key,V in Fn.items()}
        polar={key:V for key,V in polar.items() if V}
        assert set(lap)==set(polar)
        assert all(T*V==polar[key] for key,V in lap.items())
        assert all(kind=='s' and frequency==n for ell,kind,frequency in lap)
        terms=[];diagonals=[]
        for (ell,kind,frequency),V in sorted(lap.items()):
            W=V(U); q=next(i for i,x in enumerate(W) if x)
            assert ell*delta+2*q-2>0
            terms.append((ell,W));diagonals.append({'ell':ell,'tail_order':q})
        groups={}
        for i,(ell,V) in enumerate(terms):
            for j in range(i,len(terms)):
                ell2,W=terms[j];b=(ell+ell2)*delta/2-3
                groups[b]=groups.get(b,ZERO)+(1 if i==j else 2)*U*V*W
        moments=[(b+j+1,ar(x)) for b,V in groups.items() for j,x in enumerate(V) if x]
        assert all(b>0 for b,x in moments)
        rows=[]
        for a in weights:
            e=sum((x/ar(a+b) for b,x in moments),arb(0))*arb.pi()/2
            assert e>0,(n,str(a),e)
            norm=e.sqrt();checks={}
            old=anchorrows.get((n,a))
            if old:
                checks['N4_113_norm_overlap']=bool(norm.overlaps(arb(old['norm'])))
                assert all(checks.values())
            rows.append({'a':str(a),'energy':e.str(100),'norm':norm.str(100),'anchor_checks':checks})
        rec={'utc':now(),'mode':n,'manifest_sha256':mhash,'components':len(Fn),'laplacian_components':len(lap),
             'mixed_derivative_exact':True,'cartesian_polar_exact':True,'diagonal_integrability':diagonals,
             'power_groups':len(groups),'nonzero_moments':len(moments),'weights':rows,
             'elapsed_seconds':time.monotonic()-ms}
        write_new(p,rec);completed[n]=rec;fresh+=1
        print('completed mode',n,'seconds',rec['elapsed_seconds'],'total',time.monotonic()-start,flush=True)
    full=len(completed)==len(modes)
    totals={a:sum((arb(next(row['energy'] for row in rec['weights'] if Q(row['a'])==a))
                  for rec in completed.values()),arb(0)).sqrt() for a in weights}
    rows=[]
    for a in weights:
        test=arb(5)**ar((a-2)/2)*totals[a]
        B=(8*arb.pi()).sqrt()*ar((1+c-c*a)**2/(1+a))
        rows.append({'a':str(a),'norm' if full else 'partial_norm_lower':totals[a].str(90),
                     'necessary_test_lower':test.str(90),'B':B.str(90),
                     'point_test_failure':bool(test>B),
                     'point_test_pass':bool(full and test<B)})
    cells=[]
    for l,h in zip(weights[:-1],weights[1:]):
        low=arb(5)**ar((l-2)/2)*totals[h]
        Bh=(8*arb.pi()).sqrt()*ar((1+c-c*h)**2/(1+h))
        Bl=(8*arb.pi()).sqrt()*ar((1+c-c*l)**2/(1+l))
        high=arb(5)**ar((h-2)/2)*totals[l]
        failure=bool(low>Bl);passes=bool(full and high<Bh)
        cells.append({'left':str(l),'right':str(h),'test_lower':low.str(90),'ceiling_upper':Bl.str(90),
                      'test_upper' if full else 'partial_test_value':high.str(90),'ceiling_lower':Bh.str(90),
                      'classification':'FAIL_NECESSARY' if failure else 'PASS_NECESSARY_ONLY' if passes else 'UNRESOLVED'})
    out={'utc':now(),'candidate':NAME,'manifest_sha256':mhash,'complete':full,'completed_modes':sorted(completed),
         'missing_modes':[n for n in modes if n not in completed],'weights':rows,'cells':cells,
         'mode_record_sha256':{str(n):H(BASE/f'verification/modes/mode_{n:03d}.json') for n in sorted(completed)},
         'stage_elapsed_seconds':time.monotonic()-start,
         'total_mode_elapsed_seconds':sum(rec['elapsed_seconds'] for rec in completed.values()),
         'status':'N4-origin; full norm OPEN peer' if full else 'Partial angular lower bounds only; no full upper norm'}
    if full:write_new(BASE/'verification/full.json',out)
    else:(BASE/'verification/progress.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE','full' if full else 'partial',len(completed),'/',len(modes),time.monotonic()-start,flush=True)
    for row in rows:print(row['a'],row.get('norm',row.get('partial_norm_lower')),flush=True)

if __name__=='__main__':main()

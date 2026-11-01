"""Independent Cartesian recomputation of first-resonance certificate values."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd
import argparse
import json
import time
import cartesian_verify as cv


def run(c, initial, n0):
    delta=1-1/c
    rho={}; velocity={}; rows=[]
    start=time.monotonic()
    for n in range(1,n0+1):
        p=1-n*delta
        nonlinear=cv.Field(p,{})
        if n==1:
            current=cv.sin_field(p,initial)
        else:
            for i in range(1,n):
                j=n-i
                ux,uy=velocity[i]
                nonlinear=nonlinear+ux*rho[j].dx()+uy*rho[j].dy()
            current=nonlinear.scale(1/((n-1)*(c-1)))
        assert (current.scale(c*p-1)+nonlinear).zero()
        rho[n]=current
        row={'n':n,'p':cv.qs(p),'density':{str(k):cv.qs(v) for k,v in current.sine().items()}}
        if n<n0:
            psi=cv.poisson(current)
            assert (psi-cv.displayed_poisson(current)).zero()
            velocity[n]=psi.dy().scale(-1),psi.dx()
            row['stream']={str(k):cv.qs(v) for k,v in psi.sine().items()}
        rows.append(row)
        print(json.dumps({'n':n,'n0':n0,'elapsed_s':time.monotonic()-start}),flush=True)
    j=int(n0*delta/2)-1
    density=rho[n0].sine()
    kappa=density.get(2*j-1,cv.Q(0))
    forcing=rho[n0].dx().sine().get(2*j,cv.Q(0))
    assert forcing==-2*j*kappa
    special=[dict(n=r['n'],density_at_pi_over_2=cv.qs(sum((-1)**((int(k)-1)//2)*cv.Q(v) for k,v in r['density'].items()))) for r in rows if r['n']*delta==2]
    return dict(c=cv.qs(c),delta=cv.qs(delta),n0=n0,j=j,kappa=cv.qs(kappa),
                forcing=cv.qs(forcing),l1=cv.qs(sum(abs(v) for v in density.values())),
                nonzero=bool(kappa),rows=rows,chi_special=special,elapsed_s=time.monotonic()-start)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--case',default='all')
    args=parser.parse_args()
    src=Path('../a4-num/notes/resonance_report.json')
    blob=src.read_bytes()
    data=json.loads(blob)
    outdir=Path('research/03_resonances/verification/independent_first_resonances')
    outdir.mkdir(parents=True,exist_ok=True)
    (outdir/'source_resonance_report.json').write_bytes(blob)
    chosen={'candidate_5_3':0,'candidate_9_5':1,'sin_20_11':2,'sin_5_3':3,'sin_plus_half3_5_3':5}
    for name,index in chosen.items():
        if args.case not in ('all',name): continue
        row=data[index]
        c=cv.Q(row['c_l']); delta=1-1/c
        n0=2*int(delta.denominator)//gcd(int(delta.numerator),2)
        if n0*delta==2: n0*=2
        initial={2*k+1:cv.Q(a) for k,a in enumerate(row['f1']) if cv.Q(a)}
        output=run(c,initial,n0)
        expected=next(r for r in row['psi_resonances'] if r['first_resonance'])
        output['matches_numerics_exact_kappa']=cv.Q(output['kappa'])==cv.Q(expected['a_{n,j-1}'])
        output['matches_numerics_exact_forcing']=cv.Q(output['forcing'])==cv.Q(expected['forcing_sin2j'])
        output['reported_float_relative_error']=abs(float(cv.Q(output['kappa']))-expected['float'])/abs(float(cv.Q(output['kappa'])))
        output['checked_at_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        output['code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
        output['engine_sha256']=sha256(Path('code/cartesian_verify.py').read_bytes()).hexdigest()
        output['source_report']=str(src)
        output['source_report_sha256']=sha256(blob).hexdigest()
        assert output['matches_numerics_exact_kappa'] and output['matches_numerics_exact_forcing']
        (outdir/(name+'.json')).write_text(json.dumps(output,indent=2)+'\n')
        print(json.dumps({'case':name,'complete':True,'n0':n0,'kappa_float':float(cv.Q(output['kappa'])),'all_exact_comparisons_match':True}),flush=True)

if __name__=='__main__':main()

"""Independent zero-exponent variation replay for the sharper closed form.

No transport code or optimizer is imported. At exponent zero all extracted
flow costs equal one, so flow and residual sum to half the variation.
Every radial row is checkpointed with exact rational enclosure endpoints.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import json, hashlib, time
from flint import arb, acb, ctx
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '05_team_audit/closed_form37_lead'
OUT = BASE / 'verification/alpha0_rows'
ctx.prec = 192
pi = arb.pi()

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(): return datetime.now(timezone.utc).isoformat()
def up(x): return arb(x.upper())
def rec(x):
    assert x.is_finite()
    return dict(lower=str(x.lower().fmpq()), upper=str(x.upper().fmpq()), display=x.str(35, more=True))
def ball(d): return arb(d['lower']).union(arb(d['upper']))
def save(p,d):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(d,indent=2)+'\n');tmp.replace(p)

def local_row(row):
    n=512; nr=256; d=arb(1)/64
    r0=d+(arb(1)/2-d)*row/nr;r1=d+(arb(1)/2-d)*(row+1)/nr
    r=r0.union(r1);width=2*pi/n
    derivative=r1**3*(1+2*r1)/(pi*(1-r1)**4)
    error=arb(0,(derivative*width**3/24).upper())
    values=[]
    for k in range(17):
        phase=pi*k/32;ep=acb(phase.cos(),phase.sin());total=arb(0)
        for j in range(n):
            left=phase/2+pi/4+width*j;right=left+width
            theta=left.union(right);mid=left+width/2
            z=acb(theta.cos(),theta.sin());zm=acb(mid.cos(),mid.sin())
            domain=((2*theta-phase).cos()-(ep*r*r/(1+r*z)**2).real)/(2*pi)
            own=((2*right-phase).sin()-(2*left-phase).sin())/(4*pi)
            value=own-width*(ep*r*r/(1+r*zm)**2).real/(2*pi)+error
            if domain>0:bound=value
            elif domain<0:bound=-value
            else:bound=width*abs(domain)
            total+=up(bound)
        values.append(total*(r1/r0).log())
    return values

def middle_row(row):
    n=512;nr=512;lo=pi*row/(2*nr);hi=pi*(row+1)/(2*nr)
    t=lo.union(hi);r=t.sin();jac=t*r*t.cos();R=up(r);J=up(abs(jac));T=up(hi)
    first=16*J*T*R/pi;second=J*T*T*(16*R+96*R*R)/pi
    width=arb(2)/n;spread=arb(0,(first*width/2).upper())
    error=arb(0,(second*width**3/24).upper());densities=[]
    for j in range(n):
        angular=pi/2+t*(arb(2*j+1)/n-1)
        z=acb(r*angular.cos(),r*angular.sin())
        densities.append(jac*z/(pi*(z*z-arb(1)/4)**2))
    totals=[]
    for k in range(17):
        phase=pi*k/32;c=phase.cos();s=phase.sin();value=arb(0)
        for density in densities:
            mid=density.real*c-density.imag*s;domain=mid+spread
            if domain>0:bound=mid*width+error
            elif domain<0:bound=-mid*width+error
            else:bound=width*abs(domain)
            value+=up(bound)
        totals.append(value*(hi-lo))
    return totals

def main():
    OUT.mkdir(parents=True,exist_ok=True);digest=sha(Path(__file__));started=time.monotonic()
    manifest=dict(precision_bits=192,local_rows=256,middle_rows=512,phases=16,angles=512,delta='1/64',auditor_sha256=digest)
    mp=OUT/'manifest.json'
    if mp.exists():assert json.loads(mp.read_text())==manifest
    else:save(mp,manifest)
    for kind,count,fn in [('local',256,local_row),('middle',512,middle_row)]:
        for row in range(count):
            path=OUT/f'{kind}_{row:04d}.json'
            if path.exists():
                old=json.loads(path.read_text());assert old['row']==row and old['kind']==kind and old['auditor_sha256']==digest;continue
            values=fn(row)
            save(path,dict(time_utc=stamp(),kind=kind,row=row,values=[rec(v) for v in values],auditor_sha256=digest))
            if row%8==0:print(stamp(),kind,row,count,'seconds',round(time.monotonic()-started,1),flush=True)
    totals={}
    for kind,count in [('local',256),('middle',512)]:
        v=[arb(0) for _ in range(17)]
        for row in range(count):
            p=OUT/f'{kind}_{row:04d}.json';data=json.loads(p.read_text())
            for k,value in enumerate(data['values']):v[k]+=ball(value)
        totals[kind]=v
    # The exterior limit has already been independently recomputed at192bits.
    far_path=ROOT/'05_team_audit/closed_form_lead/verification/alpha0_replay.json'
    far_record=json.loads(far_path.read_text());assert far_record['verdict'].startswith('CONFIRMED')
    assert far_record['auditor_sha256']==sha(ROOT/'code/replay_closed_form_alpha0.py')
    totals['far']=[ball(v) for v in far_record['far']]
    sums=[sum((totals[k][j] for k in totals),arb(0)) for j in range(17)]
    maximum=sums[0]
    for value in sums[1:]:maximum=arb.max(maximum,value)
    bound=maximum/(pi/64).cos();target=arb(158263)/50000
    assert bound<target,(bound,target)
    result=dict(time_utc=stamp(),precision_bits=192,components={k:[rec(x) for x in v] for k,v in totals.items()},
                remainder=rec(bound),target='158263/50000',margin=rec(target-bound),
                exterior_audit_sha256=sha(far_path),manifest_sha256=sha(mp),auditor_sha256=digest,
                verdict='CONFIRMED: independent full geometric zero-exponent replay without any transport plan.')
    save(BASE/'verification/alpha0_replay.json',result)
    print(stamp(),'COMPLETE',bound.str(30),flush=True)
if __name__=='__main__':main()

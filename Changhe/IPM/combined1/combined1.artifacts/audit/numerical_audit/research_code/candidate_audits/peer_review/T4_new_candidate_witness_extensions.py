from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[1]
ctx.prec=1024
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
    q=Q(q);return arb(q.numerator)/q.denominator

def overlaps_interval(value,record):
    lo=ar(record['lower']);hi=ar(record['upper'])
    return not(value<lo or value>hi)

def run(name):
    start=time.monotonic();src=ROOT/f'verification/{name}.json';target=ROOT/f'source/{name}_point_extensions.json'
    d=json.loads(src.read_text());t=json.loads(target.read_text());assert d['canonical_sha256']==t['canonical_sha256'];assert d['point']==t['point']
    f={k:arb(v) for k,v in d['fields'].items()}
    c=ar(Q(4076476460239181,2**51));theta=((f['rho_x']**2+f['rho_y']**2).sqrt()-f['rho_y'])/2;gap=theta-(c-1)
    assert overlaps_interval(theta,t['theta_at_point']) and overlaps_interval(gap,t['theta_minus_c_minus_1'])
    fails=bool(gap>0);assert fails==t['signed_criterion_fails_even_kappa_zero']
    rows=[]
    for old in t['sharp_ball_exclusions']:
        s=ar(old['s']);r=ar(old['radius']);C0=1/(4*arb.pi()*(1+s)).sqrt();C1=1/(8*arb.pi()*s*(1+s)).sqrt()
        A=C1*f['velocity_norm']+C0*(1+f['gradient_norm']);B=C0*C1
        upper=A*r+B*r*r;g=abs(f['residual'])-upper;necessary=2*abs(f['residual'])/(A+(A*A+4*B*abs(f['residual'])).sqrt())
        assert g>0
        vals={'necessary_upper':upper,'gap':g,'necessary_H2s_radius_lower':necessary}
        assert all(overlaps_interval(value,old[key]) for key,value in vals.items())
        rows.append({'framework':old['framework'],'s':old['s'],'radius':old['radius'],**{k:v.str(90) for k,v in vals.items()},'all_three_overlap':True})
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'canonical_sha256':d['canonical_sha256'],'point_source_sha256':sha(src),'target_sha256':sha(target),'code_sha256':sha(Path(__file__)),'precision_bits':ctx.prec,'theta':theta.str(90),'theta_minus_c_minus_1':gap.str(90),'signed_criterion_fails_even_kappa_zero':fails,'rows':rows,'elapsed_seconds':time.monotonic()-start}
    (ROOT/f'verification/{name}_extensions.json').write_text(json.dumps(out,indent=2)+'\n')
    print(name,'theta',theta.str(25),'signed gap',gap.str(25),'point gaps',[r['gap'] for r in rows],flush=True)
if __name__=='__main__':
    for name in ['C1-N1-005-d2w-j7-x3','C1-N1-006-8branch-e2']:run(name)

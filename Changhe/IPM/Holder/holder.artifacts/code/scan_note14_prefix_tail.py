"""Floating proposal scan of completed task prefixes; not a certificate.

The chosen prefix must be independently checked by audit_note14_prefix_tail.py.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json,math
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument('directory');p.add_argument('--out',required=True);args=p.parse_args()
    d=(ROOT/args.directory).resolve();assert d.is_relative_to(ROOT)
    m=json.loads((d/'manifest.json').read_text());par=m['params']
    a,b,c,l=map(lambda x:float(Fraction(x)),[par['alpha'],par['b'],par['c'],par['lam']])
    assert l*(1+2**(-a))>1
    H=math.hypot(b+.5,b);B=max(H**a+abs(c),.5+2**(-a))
    coeff=1.;s=0.
    for k in range(60):
        s+=coeff*4**(-k)*(3/(a+2+2*k)-1/(a+4+2*k));coeff*=(2*k+1)/(2*k+2)
    a3=3*s/(4*math.pi)
    eps=float(par['rho_min']);eta=float(par['rho_m'])
    inner=eps**a/a+eps**2*(.5+eps**a)/(2*(1-eps)**2)
    sliver=2**(a+3)*eta**(a+3)/(math.pi*(a+3)*math.sqrt(1-eta*eta))
    near=0.;mid=0.;proposals=[]
    for index,t in enumerate(m['tasks']):
        path=d/f'task_{index:05d}.json'
        if not path.exists():break
        r=json.loads(path.read_text());low=float(Fraction(r['interval']['lower']))
        if t['kind']=='near':near+=low;continue
        mid+=low;R=float(t['edges'][-1])
        if R<=1:continue
        q=1/(4*R*R);den=(1-q)**2
        main=2*a3*R**(a-1)/(1-a)
        err=2*B/(R*den)+R**(a-3)/(2*(3-a)*den)
        v=2*near+mid+main-err-2*inner-sliver+.5
        proposals.append(dict(task_count=index+1,radius=R,proposed_D_lower=v,tail_main=main,tail_error=err))
    proposals.sort(key=lambda r:r['proposed_D_lower'],reverse=True)
    out=(ROOT/args.out).resolve();assert out.is_relative_to(ROOT);out.parent.mkdir(parents=True,exist_ok=True)
    rec=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=par['alpha'],source_directory=str(d.relative_to(ROOT)),
             status='FLOATING PROPOSAL ONLY; exact prefix audit required',best=proposals[:15],count=len(proposals))
    out.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
if __name__=='__main__':main()

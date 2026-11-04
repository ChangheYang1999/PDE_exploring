"""Separate Python-Fraction Cartesian cubic and leading-sector record reduction."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from pathlib import Path
import argparse,json,time,sys
sys.set_int_max_str_digits(0)

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/fitted_center_constraints'
CHECKS=0
C=Q(4076476460239181,2251799813685248)

def need(value,label=''):
    global CHECKS
    assert value,label
    CHECKS+=1

def stamp():return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def digest(path):return sha256(Path(path).read_bytes()).hexdigest()
def local(text):
    p=Path(text);need(not p.is_absolute() and '..' not in p.parts);return ROOT/p

def endpoints(record,value):
    lo,hi=Q(record['lower_exact']),Q(record['upper_exact'])
    need(Q(record['strict_lower_decimal'])<lo<=value<=hi<Q(record['strict_upper_decimal']))

def cubic(atoms):
    poly=defaultdict(Q)
    for row in atoms:
        n,h,d=row['n'],row['h'],row['d']
        for v in (n,h,d):need(type(v) is int)
        need(n>0 and n%2 and h>=0 and d>=0)
        a,b,t=map(Q,[row['coefficient_exact'],row['b_exact'],row['scale_exact']])
        need(t>0 and a!=0)
        need(n+2*h+2*b-2*d<=4/C-3)
        if n+2*h>3:continue
        for radial in range((3-n-2*h)//2+1):
            coefficient=a*t**(-d)*(1 if radial==0 else b-Q(d)/t)
            degree_s=h+radial
            for iy in range(1,n+1,2):
                harmonic=comb(n,iy)*(-1)**((iy-1)//2)
                for ky in range(degree_s+1):
                    x=n-iy+2*(degree_s-ky);y=iy+2*ky
                    poly[x,y]+=coefficient*harmonic*comb(degree_s,ky)
    p21,p03=poly[2,1],poly[0,3]
    return (p21+3*p03)/4,(p21-p03)/4,2*p21,-(2*p21+6*p03),poly

def main():
    p=argparse.ArgumentParser();p.add_argument('--record',required=True);p.add_argument('--tag',required=True)
    args=p.parse_args();need(args.tag and all(v.isalnum() or v in '_-' for v in args.tag))
    folder=BASE/'verification'/args.tag;folder.mkdir(exist_ok=False)
    started,tick=stamp(),time.monotonic()
    rp=local(args.record);record=json.loads(rp.read_text())
    need(record['code_sha256']==digest(BASE/'code/check.py'))
    for path,sha in record['files'].items():need(digest(local(path))==sha,path+' hash')
    request=json.loads(local(record['request']).read_text());docs={}
    for name,item in request['inputs'].items():
        pp=local(item['path']);need(digest(pp)==item['sha256']);docs[name]=json.loads(pp.read_text())
    phi,origin,structure=(docs[k] for k in ('phi','origin','structure'))
    A,B,ell,slope,polynomial=cubic(phi['atoms'])
    need(A==Q(record['A_exact']) and B==Q(record['B_exact']))
    need(ell==Q(record['ell_correction_exact'])==2*A+6*B)
    need(slope==-8*A)
    a0=Q(origin['rho_taylor_coefficients']['0,1'])
    astar=a0+slope;q=Q(21,10);margin=astar-q*(2*C-2)
    need(astar==Q(record['a_star_exact']) and margin==Q(record['cap_margin_exact']))
    need(record['normalization_pass']==(ell==0))
    need(record['slope_positive']==(astar>0) and record['cap_pass']==(margin>=0))
    endpoints(record['a_star'],astar);endpoints(record['cap_margin'],margin)
    endpoints(record['origin_margin'],C+1-q-max(-margin,Q(0)))
    mu,e=4/C-3,4/C-5
    added=defaultdict(Q)
    for atom in phi['atoms']:
        a,b,t=map(Q,[atom['coefficient_exact'],atom['b_exact'],atom['scale_exact']])
        n,h,d=atom['n'],atom['h'],atom['d']
        if n+2*h+2*b-2*d==mu:added[n]+=(C*e-1)*a*(n*n-mu*mu)
    expected={int(n):Q(v) for n,v in record['leading_addition'].items()}
    need(dict(added)==expected)
    sect=[v for v in structure['sectors'] if v['J']==3 and v['N']==1];need(len(sect)==1)
    final={int(n):Q(v) for n,v in sect[0]['sine_coefficients'].items()}
    for n,v in added.items():final[n]=final.get(n,Q(0))+v
    final={n:v for n,v in final.items() if v}
    need(final=={int(n):Q(v) for n,v in record['leading_combined'].items()})
    square=sum((v*v for v in final.values()),Q(0))
    need(square==Q(record['leading_square_sum_exact']))
    # Exact independent pi bracket from a fixed Machin-series remainder.
    def atan_bracket(k,N):
        value=sum((Q((-1)**j,(2*j+1)*k**(2*j+1)) for j in range(N)),Q(0))
        next_term=Q((-1)**N,(2*N+1)*k**(2*N+1))
        return min(value,value+next_term),max(value,value+next_term)
    a,b=atan_bracket(5,160);c,d=atan_bracket(239,48)
    plo,phi_pi=16*a-4*d,16*b-4*c
    need(3<plo<phi_pi<4)
    shown=record['leading_circle_norm'];lo,hi=Q(shown['strict_lower_decimal']),Q(shown['strict_upper_decimal'])
    if square:
        need(0<=lo and lo*lo<plo*square and phi_pi*square<hi*hi)
    else:
        need(lo<0<hi)
    # Exact two-atom counterexample to cap enforcement, independent of optimizer execution.
    fixture=[dict(n=1,h=0,d=0,coefficient_exact='-2',b_exact='-1',scale_exact='1'),dict(n=3,h=0,d=0,coefficient_exact='-2/3',b_exact='-2',scale_exact='1')]
    ca,cb,ce,cs,_=cubic(fixture)
    need(ca==2 and cb==Q(-2,3) and ce==0 and cs==-16)
    need(10<a0<11 and a0+cs<0<q*(2*C-2))
    out=dict(started_utc=started,finished_utc=stamp(),elapsed_seconds=time.monotonic()-tick,
             code_sha256=digest(__file__),record=args.record,record_sha256=digest(rp),checks=CHECKS,
             passed=True,method='Python Fraction Cartesian cubic; exact atomwise leading-sector sum; independent Machin rational pi bracket',
             normalization=ell==0,cap_pass=margin>=0,counterexample_verified=True,
             scope='Finite exact structural record and displayed scalar endpoints only. No residual norm or changed background.')
    with (folder/'result.json').open('x') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(out['finished_utc'],'checks',CHECKS,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

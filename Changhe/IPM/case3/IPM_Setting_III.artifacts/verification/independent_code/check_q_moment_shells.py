"""Manufactured gate, independently differentiating original density modes."""
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import mpmath as mp
from q_canonical_moment_shells import polynomials,shell_values
from q_mp_primitives import mf,fraction,horner
from q_canonical_high_jets import solve
sys.set_int_max_str_digits(0)
checks=[]
def record(name,passed,**kw):
    checks.append(dict(name=name,passed=bool(passed),**kw))
    if not passed:raise AssertionError(checks[-1])

def exact_value(row,s):
    assert row['q'].denominator==1
    w=1-s
    return w**(row['q']+1)*sum((v*w**j for j,v in enumerate(row['E'])),F(0))


def direct_source_integral(coeff,kappa,L,n,lo,hi):
    coeff=[[mf(v)for v in cc]for cc in coeff];k=mf(kappa);m0=mf(L)*mp.power(2,-k)
    def B(j,s):return mp.fsum(v*mp.chebyt(h,2*s-1)for h,v in enumerate(coeff[j])) if j<len(coeff)else mp.mpf(0)
    def b(j,s):
        r=m0*mp.sqrt(s)*(1-s)**(-k)
        d=B(0,s)-s*B(1,s)/2 if j==0 else (B(j,s)-s*B(j+1,s))/2
        return r*(1-s)*s**j*d
    def integrand(s):
        r=m0*mp.sqrt(s)*(1-s)**(-k)
        dr=r*(1+(2*k-1)*s)/(2*s*(1-s))
        src=(mp.diff(lambda u:b(n-1,u),s)/dr-(2*n-1)*b(n-1,s)/r
             +mp.diff(lambda u:b(n,u),s)/dr+(2*n+1)*b(n,s)/r)/2
        return r**(1-2*n)*src*dr
    return mp.quad(integrand,[lo,(2*lo+hi)/3,(lo+2*hi)/3,hi])


def run():
    for seed in range(4):
        cc=[[F(((seed+2)*(j+3)*(h+1))%13-6,3+j+h)for h in range(4+seed)]for j in range(5)]
        for k in [F(5,4),F(3,2),F(7,3)]:
            rows=polynomials(cc,k,4);jet=solve(cc,k,F(3),order=3)
            for row,harm in zip(rows,jet['harmonic']):
                record(f'total_seed{seed}_k{k}_n{row["n"]}',row['total_core']==4*row['n']*harm['stream_harmonic_core'])
                if row['q'].denominator==1:
                    points=[F(0),F(1,7),F(2,5),F(7,8),F(1)]
                    pieces=[exact_value(row,b)-exact_value(row,a)for a,b in zip(points,points[1:])]
                    record(f'exact_telescope_seed{seed}_k{k}_n{row["n"]}',sum(pieces,F(0))==row['total_core'])
            if seed<2:
                with mp.workdps(100):
                    lo=mp.mpf(1)/7;hi=mp.mpf(8)/9;L=F(7,5)
                    m0=mf(L)*mp.power(2,-mf(k))
                    for row in rows:
                        n=row['n'];direct=direct_source_integral(cc,k,L,n,lo,hi)
                        val=[]
                        for s in [lo,hi]:val.append((1-s)**(mf(row['q'])+1)*horner([mf(v)for v in row['E']],1-s))
                        predicted=m0**(2-2*n)*(val[1]-val[0]);error=abs(direct-predicted)/(1+abs(direct))
                        record(f'direct_chebyshev_source_seed{seed}_k{k}_n{n}',error<mp.mpf('1e-85'),relative_error=mp.nstr(error,12))
                    radii=['0','0.0001','.03','.5','10','100',None]
                    aa=shell_values(rows,L,k,radii)
                    bb=shell_values(rows,3*L,k,[None if r is None else str(3*mp.mpf(r))for r in radii])
                    for a,b in zip(aa,bb):
                        n=a['n'];ee=abs(a['telescoping_error'])/(1+abs(a['total']))
                        record(f'mp_telescope_seed{seed}_k{k}_n{n}',ee<mp.mpf('1e-88'),relative_error=mp.nstr(ee,12))
                        for h,(x,y)in enumerate(zip(a['shells'],b['shells'])):
                            ee=abs(y-3**(2-2*n)*x)/(1+abs(y)) if n==1 else abs(y-mf(F(3)**(2-2*n))*x)/(1+abs(y))
                            record(f'physical_scaling_seed{seed}_k{k}_n{n}_shell{h}',ee<mp.mpf('1e-85'),relative_error=mp.nstr(ee,12))
    result=dict(utc=datetime.now(timezone.utc).isoformat(),verdict='PASS',count=len(checks),checks=checks)
    files=['independent_code/q_canonical_moment_shells.py','independent_code/check_q_moment_shells.py','research/q_canonical_moment_shells/PROOF.md']
    result['sha256']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in files}
    target=Path('research/q_canonical_moment_shells/verification/checks.json');target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='checks'}))
if __name__=='__main__':run()

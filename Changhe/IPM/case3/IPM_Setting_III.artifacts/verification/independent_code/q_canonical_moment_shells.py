"""Independent signed canonical source moments on radial shells.

Derivation: research/q_canonical_moment_shells/PROOF.md, written first.
Only verifier code is imported. No producer inverse or differentiation code.
"""
from fractions import Fraction as F
import mpmath as mp
from q_mp_primitives import fraction,mf,trim,add,scale,shift,mul,chebyshev_power_rows,convert,horner
from q_high_precision_density import MPQDensity


def polynomials(coeff,kappa,nmax=3):
    """Return exact E_n(w) and normalized full-plane moments."""
    coeff=[[fraction(v) for v in cc] for cc in coeff]
    kappa=fraction(kappa)
    assert coeff and kappa>1 and nmax>=1
    rows=chebyshev_power_rows(max(map(len,coeff))-1,reverse=True)
    Bw=[convert(cc,rows) for cc in coeff[:nmax+2]]
    def B(j):return Bw[j] if j<len(Bw) else [F(0)]
    dw=[]
    for j in range(nmax+1):
        adjacent=add(B(j+1),scale(shift(B(j+1)),-1))
        dd=add(B(j),scale(adjacent,-F(1,2) if j==0 else -1))
        dw.append(dd if j==0 else scale(dd,F(1,2)))
    out=[]
    for n in range(1,nmax+1):
        q=2*kappa*(n-1)
        hh=mul(dw[n],[2*kappa,1-2*kappa])
        boundary=scale(add(dw[n-1],add(dw[n],scale(shift(dw[n]),-1))),F(1,2))
        ee=add(boundary,[-n*v/(q+j+1) for j,v in enumerate(hh)])
        out.append(dict(n=n,q=q,E=trim(ee),total_core=-sum(ee,F(0))))
    return out


def map_object(L,kappa):
    # Exact rational conversion, with no binary64 detour.
    density=MPQDensity.__new__(MPQDensity)
    density.L=mf(L);density.kappa=mf(kappa)
    return density


def primitives_at_r(rows,L,kappa,r):
    if r is None:return [mp.mpf(0)]*len(rows)
    r=mp.mpf(r)
    if r==0:return [-mf(row['total_core']) for row in rows]
    _,w=map_object(L,kappa).coords(r)
    return [mp.exp((mf(row['q'])+1)*mp.log(w))*horner([mf(v)for v in row['E']],w) for row in rows]


def shell_values(rows,L,kappa,radii):
    m0=mf(L)*mp.power(2,-mf(kappa))
    vals=[primitives_at_r(rows,L,kappa,r)for r in radii]
    out=[]
    for j,row in enumerate(rows):
        n=row['n'];factor=m0**(2-2*n)
        terms=[factor*(right[j]-left[j])for left,right in zip(vals,vals[1:])]
        tails=[-factor*vv[j]for vv in vals]
        total=factor*mf(row['total_core'])
        out.append(dict(n=n,total=total,shells=terms,tails=tails,telescoping_error=mp.fsum(terms)-total))
    return out

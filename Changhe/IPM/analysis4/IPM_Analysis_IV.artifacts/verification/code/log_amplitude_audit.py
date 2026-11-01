"""Exact amplitude and log-translation audit, independent Cartesian calculus."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
import json, time
from laurent_log_audit import L, Q, Poly, parse
from maximal_log_cartesian_check import poisson


def translated(A,s):
    s=Q(s)
    return L(A.q,A.M,[sum((A.a[k]*(comb(k,j)*s**(k-j)) for k in range(j,len(A.a))),Poly([])) for j in range(len(A.a))])


def compute(delta,amplitude,N):
    c=1/(1-delta);F={};G={};XF={};YF={};XG={};YG={}
    for n in range(1,N+1):
        p=1-n*delta
        if n==1:F[n]=parse(p,{1:[str(amplitude)]})
        else:
            non=L(p,0,[])
            for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
            lam=(n-1)*(c-1);term=non.scale(1/lam);value=term
            while term.a:
                term=term.dt().scale(c/lam);value=value+term
            F[n]=value
        G[n]=poisson(F[n]);XF[n]=F[n].X();YF[n]=F[n].Y();XG[n]=G[n].X();YG[n]=G[n].Y()
    return F,G


def amplitudes(A):
    return {str(m):[str(2*p[A.M+m]) for p in A.a] for m in range(1,A.M+1) if any(p[A.M+m] for p in A.a)}


def main():
    start=time.monotonic();delta=Q(2,3);c=Q(3);N=12
    F,G=compute(delta,Q(1),N);rows=[]
    for eps in [Q(2),Q(-3,2)]:
        Fe,Ge=compute(delta,eps,N)
        for n in range(1,N+1):
            assert (Fe[n]-F[n].scale(eps**n)).zero()
            assert (Ge[n]-G[n].scale(eps**n)).zero()
            rows.append(dict(kind='canonical_homogeneity',epsilon=str(eps),n=n,density_exact=True,stream_exact=True))
    for s in [Q(1),Q(-2,3)]:
        FT={n:translated(F[n],s) for n in F};GT={n:translated(G[n],s) for n in G}
        for n in range(1,N+1):
            assert (GT[n].X().X().scale(-1)+GT[n].Y().Y()-FT[n].X()).zero()
            non=L(FT[n].q,0,[])
            for i in range(1,n):non=non+GT[i].X()*FT[n-i].Y()-GT[i].Y()*FT[n-i].X()
            assert (FT[n].scale(c*FT[n].q-1)+FT[n].dt().scale(c)+non).zero()
            rows.append(dict(kind='translation',s=str(s),n=n,stationary_exact=True,poisson_exact=True))
    base=amplitudes(G[6]);shift=amplitudes(translated(G[6],1));difference=amplitudes(translated(F[7],1)-F[7])
    assert base['2'][0]=='0'
    assert base['2'][1]=='-177047/1204224000000'
    assert shift['2'][0]==base['2'][1]
    assert difference
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),delta=str(delta),c=str(c),input='sin(theta)',N=N,
      checks=rows,first_resonant_canonical=base['2'],first_resonant_shifted_by_one=shift['2'],density_order7_translation_difference=difference,
      actual_elapsed_s=time.monotonic()-start,source_hashes={p:sha256(Path(p).read_bytes()).hexdigest() for p in ['code/log_amplitude_audit.py','code/laurent_log_audit.py','code/maximal_log_cartesian_check.py']})
    Path('research/50_log_amplitude_scaling/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(passed=len(rows),density_order7_difference=difference,elapsed_s=out['actual_elapsed_s'])))

if __name__=='__main__':main()

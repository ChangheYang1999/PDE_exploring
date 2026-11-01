"""Continue the compatible sin7, delta4/5 case with exact Cartesian arithmetic."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from laurent_log_audit import L,Poly,Q,parse


def pure_potential(f):
    assert f.q == -3
    maxk=(f.M-1)//2
    D={maxk+1:Q(0)}
    for k in range(maxk,0,-1):
        D[k]=(2*f.a[0][f.M+2*k+1]-k*D[k+1])/(k+1)
    M=2*maxk; coef=[Q(0)]*(2*M+1)
    for k,d in D.items():
        if d:
            cc=-d/(4*k*k);coef[M+2*k]+=cc/2;coef[M-2*k]+=cc/2
    C=L(Q(0),M,[Poly(coef)])
    lap=C.X().X()-C.Y().Y()
    assert (lap.Y()-f).zero()
    G=C.X().Y().scale(-1)
    beta=2*G.a[0][G.M+2]
    return beta,{str(k):str(2*C.a[0][C.M+k]) for k in range(2,C.M+1,2) if C.a[0][C.M+k]}


def run(beta):
    delta,c=Q(4,5),Q(5);XF,YF,XG,YG={},{},{},{}
    evidence={}
    for n in range(1,11):
        p=1-n*delta;non=L(p,0,[])
        for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
        f=parse(p,{'7':['1']}) if n==1 else non.scale(1/((n-1)*(c-1)))
        assert (f.scale(c*p-1)+non).zero()
        XF[n],YF[n]=f.X(),f.Y();H,P=XF[n],p+1
        if n==5:
            assert 2*f.a[0][f.M+1]==0
            beta_pure,chi=pure_potential(f)
            evidence.update(first_compatible=True,pure_potential_beta=str(beta_pure),pure_potential_cosines=chi)
        if n==10:
            kappa=2*f.a[0][f.M+5];forcing=2*H.a[0][H.M+6]
            assert forcing==-6*kappa
            evidence.update(kappa10=str(kappa),forcing10=str(forcing),second_compatible=not bool(kappa),density10={str(k):str(2*f.a[0][f.M+k]) for k in range(1,f.M+1,2) if f.a[0][f.M+k]})
            return evidence
        bb=[]
        for idx,h in enumerate(H.a[0].coeffs() if H.a else []):
            m=idx-H.M;lam=m*m-P*P
            assert lam or not h
            bb.append(h/lam if lam else Q(0))
        g=L(P,H.M,[Poly(bb)])
        if n==5:g=g+parse(P,{'2':[str(beta)]})
        XG[n],YG[n]=g.X(),g.Y()
        assert (XG[n].X().scale(-1)+YG[n].Y()-H).zero()


def main():
    start=time.monotonic();root=Path('research/59_missing_first_harmonic')
    zero=run(Q(0));one=run(Q(1));k0=Q(zero['kappa10']);slope=Q(one['kappa10'])-k0
    assert slope
    beta_star=-k0/slope;tuned=run(beta_star);assert tuned['second_compatible']
    beta_pure=Q(zero['pure_potential_beta']);pure=run(beta_pure)
    assert Q(pure['kappa10'])==k0+slope*beta_pure and not pure['second_compatible']
    out={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'delta':'4/5','c':'5','leading_harmonic':7,'kappa10_at_beta0':str(k0),'kappa10_slope':str(slope),'beta_star':str(beta_star),'beta_pure':str(beta_pure),'beta_star_approx':float(beta_star),'beta_pure_approx':float(beta_pure),'pure_kappa10_approx':float(Q(pure['kappa10'])),'zero':zero,'one':one,'tuned':tuned,'pure':pure,'actual_elapsed_s':time.monotonic()-start}
    (root/'verification/compatible_case_continuation.json').write_text(json.dumps(out,indent=2)+'\n')
    src=Path(__file__).read_bytes();(root/'sources/higher_harmonic_continuation.py.txt').write_bytes(src)
    (root/'sources/continuation_sha256.txt').write_text(sha256(src).hexdigest()+'\n')
    print({k:v for k,v in out.items() if k.endswith('approx') or k=='actual_elapsed_s'})

if __name__=='__main__':main()

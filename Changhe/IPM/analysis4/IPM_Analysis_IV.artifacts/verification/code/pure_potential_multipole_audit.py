"""Find the first resonant amplitude forced by a pure potential at q=0."""
from datetime import datetime, timezone
from pathlib import Path
from hashlib import sha256
import json
import time
from free_multipole_audit import Q, Poly, L, parse, run


def main():
    target=Path('research/36_free_multipole_compatibility/verification')
    for mode in (11,13,15):
        start=time.monotonic()
        d,c=Q(4,9),Q(9,5)
        XF,YF,XG,YG={},{},{},{}
        for n in range(1,10):
            p=1-n*d
            non=L(p,0,[])
            for i in range(1,n):
                j=n-i
                non=non+XG[i]*YF[j]-YG[i]*XF[j]
            f=parse(p,{str(mode):['1']}) if n==1 else non.scale(1/((n-1)*(c-1)))
            XF[n],YF[n]=f.X(),f.Y()
            H,P=XF[n],p+1
            if n==9:
                break
            bb=[]
            for idx,h in enumerate(H.a[0].coeffs()):
                k=idx-H.M; lam=k*k-P*P
                assert lam or not h
                bb.append(h/lam if lam else Q(0))
            g=L(P,H.M,[Poly(bb)])
            XG[n],YG[n]=g.X(),g.Y()
        maxk=(f.M-1)//2
        D={maxk+1:Q(0)}
        for k in range(maxk,0,-1):
            amplitude=2*f.a[0][f.M+2*k+1]
            D[k]=(amplitude-k*D[k+1])/(k+1)
        M=2*maxk
        coeffs=[Q(0)]*(2*M+1)
        for k,v in D.items():
            if not v: continue
            coeff=-v/(4*k*k)
            coeffs[M+2*k]+=coeff/2
            coeffs[M-2*k]+=coeff/2
        chi=L(Q(0),M,[Poly(coeffs)])
        lap=chi.X().X()-chi.Y().Y()
        assert (lap.Y()-f).zero()
        gpure=chi.X().Y().scale(-1)
        pure_beta=2*gpure.a[0][gpure.M+2]
        assert pure_beta==D[2]/8
        source=target/f'sin{mode}.json'
        data=json.loads(source.read_text())
        predicted=Q(data['kappa_at_beta0'])+Q(data['slope_exact'])*pure_beta
        direct,checks=run(mode,pure_beta)
        assert predicted==direct
        result=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    leading_mode=mode,pure_potential_beta_exact=str(pure_beta),pure_potential_beta_float=float(pure_beta),
                    pure_chi_density_cartesian_identity=True,pure_chi_stream_cartesian_identity=True,
                    kappa18_pure_potential_exact=str(direct),kappa18_pure_potential_float=float(direct),
                    pure_potential_second_compatible=not direct,recurrence_checks=checks,
                    previous_result=str(source),previous_sha256=sha256(source.read_bytes()).hexdigest(),
                    code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),actual_elapsed_s=time.monotonic()-start)
        (target/f'sin{mode}_pure_chi.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(mode=mode,pure_beta=float(pure_beta),kappa18=float(direct),
                              exact_zero=not direct,elapsed_s=result['actual_elapsed_s'])),flush=True)


if __name__=='__main__':main()

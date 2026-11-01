"""Exact dependence of second compatibility on the first free multipole."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import time
import sys
sys.set_int_max_str_digits(0)
from laurent_log_audit import Q, Poly, L, parse


def run(mode, beta):
    delta, c = Q(4,9), Q(9,5)
    XF, YF, XG, YG = {}, {}, {}, {}
    checks = []
    for n in range(1, 19):
        p = 1-n*delta
        non = L(p,0,[])
        for i in range(1,n):
            j = n-i
            non = non+XG[i]*YF[j]-YG[i]*XF[j]
        f = parse(p,{str(mode):['1']}) if n==1 else non.scale(1/((n-1)*(c-1)))
        assert (f.scale(c*p-1)+non).zero()
        XF[n], YF[n] = f.X(), f.Y()
        H, P = XF[n], p+1
        if n in (9,18):
            j0 = int(-P/2)
            kappa = 2*f.a[0][f.M+2*j0-1]
            forcing = 2*H.a[0][H.M+2*j0]
            assert forcing == -2*j0*kappa
            if n==9:
                assert kappa == 0
            elif kappa:
                return kappa, dict(stationary_orders=18,poisson_orders=17,second_compatible=False)
        bb = []
        for idx,h in enumerate(H.a[0].coeffs() if H.a else []):
            k = idx-H.M
            lam = k*k-P*P
            if not lam:
                assert not h
                bb.append(Q(0))
            else:
                bb.append(h/lam)
        g = L(P,H.M,[Poly(bb)])
        if n==9:
            g = g+parse(P,{'2':[str(beta)]})
        XG[n], YG[n] = g.X(), g.Y()
        assert (XG[n].X().scale(-1)+YG[n].Y()-H).zero()
    return Q(0),dict(stationary_orders=18,poisson_orders=18,second_compatible=True)


def main():
    target=Path('research/36_free_multipole_compatibility/verification')
    for mode in (11,13,15,17,19):
        start=time.monotonic()
        k0,check0=run(mode,Q(0))
        k1,check1=run(mode,Q(1))
        slope=k1-k0
        result=dict(leading_mode=mode,delta='4/9',c='9/5',kappa_at_beta0=str(k0),
                    kappa_at_beta1=str(k1),slope_exact=str(slope),
                    slope_nonzero=bool(slope),base_checks=[check0,check1])
        if slope:
            beta=-k0/slope
            tuned,check=run(mode,beta)
            assert tuned==0 and check['second_compatible']
            result.update(tuned_beta_exact=str(beta),tuned_beta_float=float(beta),
                          tuned_kappa_exact=str(tuned),tuned_checks=check)
        else:
            assert k0!=0
            result['obstructed_for_all_beta']=True
        result.update(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                      code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                      cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
                      actual_elapsed_s=time.monotonic()-start)
        (target/f'sin{mode}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(mode=mode,slope_nonzero=bool(slope),beta=result.get('tuned_beta_float'),
                              elapsed_s=result['actual_elapsed_s'])),flush=True)


if __name__=='__main__':
    main()

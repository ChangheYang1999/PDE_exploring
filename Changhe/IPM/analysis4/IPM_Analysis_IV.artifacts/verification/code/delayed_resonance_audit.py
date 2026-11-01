"""Check later obstruction after exactly compatible first stream resonance."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import sys
import time
sys.set_int_max_str_digits(0)
from laurent_log_audit import Q, Poly, L, parse


def main():
    outdir = Path('research/35_delayed_resonance/verification')
    delta, c = Q(4,9), Q(9,5)
    for leading_mode in (11, 13):
        start = time.monotonic()
        F, G, XF, YF, XG, YG = {}, {}, {}, {}, {}, {}
        rows, compatibility = [], []
        for n in range(1, 19):
            p = 1-n*delta
            nonlinear = L(p, 0, [])
            for i in range(1, n):
                j = n-i
                nonlinear = nonlinear+XG[i]*YF[j]-YG[i]*XF[j]
            F[n] = parse(p, {str(leading_mode): ['1']}) if n==1 else nonlinear.scale(1/((n-1)*(c-1)))
            assert (F[n].scale(c*p-1)+nonlinear).zero()
            XF[n], YF[n] = F[n].X(), F[n].Y()
            H, P = XF[n], p+1
            j0 = -P/2
            if j0>0 and j0.q==1:
                j0 = int(j0)
                kappa = 2*F[n].a[0][F[n].M+2*j0-1]
                forcing = 2*H.a[0][H.M+2*j0]
                assert forcing == -2*j0*kappa
                compatibility.append(dict(n=n,j=j0,kappa_exact=str(kappa),forcing_exact=str(forcing),
                                          kappa_float=float(kappa),compatible=not kappa))
                if kappa:
                    assert n == 18
                    rows.append(dict(n=n,density_stationary_identity=True,stream_exists=False))
                    break
            bb = []
            for idx, h in enumerate(H.a[0].coeffs() if H.a else []):
                k = idx-H.M
                lam = k*k-P*P
                if not lam:
                    assert not h
                    bb.append(Q(0))
                else:
                    bb.append(h/lam)
            G[n] = L(P,H.M,[Poly(bb)])
            XG[n], YG[n] = G[n].X(), G[n].Y()
            assert (XG[n].X().scale(-1)+YG[n].Y()-H).zero()
            rows.append(dict(n=n,density_stationary_identity=True,poisson_identity=True))
        assert len(compatibility)==2 and compatibility[0]['compatible'] and not compatibility[1]['compatible']
        density12 = 2*F[12].a[0][F[12].M+1]
        result = dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                      code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                      cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
                      delta=str(delta), c=str(c), leading_mode=leading_mode,
                      first_free_stream_amplitude='0', density12_sin1_exact=str(density12),
                      compatibilities=compatibility, rows=rows,
                      actual_elapsed_s=time.monotonic()-start)
        (outdir/f'sin{leading_mode}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(leading_mode=leading_mode,kappa18=float(Q(compatibility[-1]['kappa_exact'])),
                             elapsed_s=result['actual_elapsed_s'])),flush=True)


if __name__ == '__main__':
    main()

"""Mode-n Hardy sharpening of an hminus1 record (lane c1-n3). For g = f(r) sin(n theta), n >= 1:
    ||g||_H <= ||r g||_2 / n.
Proof: for any test function phi, only its mode-n part phi_n = psi(r) sin(n theta) pairs with g, and
<g, phi_n> = pi int f psi r dr = pi int (f r^(3/2)) (psi r^(-1/2)) dr <= (pi int f^2 r^3 dr)^(1/2) (pi int psi^2 r^(-1) dr)^(1/2)
 = ||r g||_2 ||phi_n / r||_2 <= ||r g||_2 ||grad phi_n||_2 / n <= ||r g||_2 ||grad phi||_2 / n,
since |grad phi_n|^2 = psi'^2 sin^2 + n^2 psi^2 cos^2 / r^2 integrates to at least n^2 ||psi/r||^2 over the circle, and
||grad phi_n||_2 <= ||grad phi||_2 because the angular Fourier modes of phi are orthogonal in the Dirichlet inner product
(int grad phi_n . grad(phi - phi_n) dX = 0). Hence ||g||_H = sup <g, phi>/||grad phi||_2 <= ||r g||_2 / n. The constant 1/n is
optimal (test functions chi(log r / L) sin(n theta), L -> infinity). Hypotheses: g and r g in L^2 (as for every residual here).
The A2 parity Hardy inequality is the case n >= 1 with constant 1. Refereed by astra (astra/mode-hardy/answer.md, 2026-10-29T05:45Z):
correct, constant optimal, projection step justified by Dirichlet orthogonality; a c1-t1 or c1-t2 review is requested for AUDITED.
Applies the bound per exact mode (using the stored hardy_direct_UB = ||r F_n||_2 of hminus1_hardy_fix.py) and to the tail
modes n > max_mode with the factor 1/(max_mode + 2). Usage: hminus1_mode_hardy.py <ID> <outdir>"""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, hashlib
from flint import arb, ctx
sys.path.insert(0, str(Path(__file__).resolve().parent))
import hminus1 as H

def run(ID, outdir):
    ctx.prec = 512; outdir = Path(outdir); recp = outdir / f'{ID}_hminus1.json'; rec = json.loads(recp.read_text())
    changed = []
    for r in rec['rows']:
        if 'hardy_direct_UB' not in r or 'mode_norm_UB' not in r: continue
        n = int(r['n']); hn = arb(r['hardy_direct_UB']) / n; old = arb(r['mode_norm_UB'])
        r['mode_n_hardy_UB'] = str(hn.upper())
        if hn.upper() < old.upper():
            r.setdefault('mode_norm_UB_before_mode_hardy', r['mode_norm_UB']); r['mode_norm_UB'] = str(hn.upper()); r['ub_source'] = 'mode-n Hardy bound ||r F_n||_2 / n'
            changed.append(n)
    tail = rec.get('tail')
    if tail and 'rF_norm_UB' in tail and 'rF_norm_UB_before_mode_hardy' not in tail:
        nmin = min(tail['modes'])
        tail['rF_norm_UB_before_mode_hardy'] = tail['rF_norm_UB']
        tail['rF_norm_UB'] = str((arb(tail['rF_norm_UB_before_mode_hardy']) / nmin).upper())
        tail['method'] = f'mode-n Hardy bound: ||F_tail||_H^2 = sum_n ||F_n||_H^2 <= sum_n ||r F_n||_2^2 / n^2 <= ||r F_tail||_2^2 / {nmin}^2'
    rec['H_lower'], rec['H_upper'] = H.totals_from_rows(rec['rows'], tail)
    rec.setdefault('fixes', []).append({'type': 'mode-n Hardy bound per exact mode and for the tail', 'modes_changed': changed,
                                        'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                        'proof': __doc__})
    recp.write_text(json.dumps(rec, indent=1) + '\n')
    msg = f'RESULT after mode-n Hardy {ID}: ||F||_H in [{rec["H_lower"]}, {rec["H_upper"]}] ({len(changed)} modes changed; tail factor 1/{min(tail["modes"]) if tail else "-"})'
    print(msg); open(outdir / f'{ID}_hminus1.log', 'a').write(msg + '\n')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])

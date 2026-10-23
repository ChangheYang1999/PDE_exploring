"""export_psic.py -- exact export (JSON, repr of float64) of the discrete stream modes PsiC (Lobatto nodal values per angular mode n = 2, 4, ..., 2M),
the Lobatto nodes t, the radial map parameters and the source-state SHA-256, for independent audits of the interpolated inverse (verifier 02:17Z).
Convention: raw values as produced by IPM3QL.fields(beta)['PsiC'] (no endpoint cleaning); psi(r, th) = r^2 w(t(r)) sum_j PsiC[i, j] sin(2 (j+1) th) at node i,
w = (1 - t)/2, map r = L sqrt((1+t)/2) (1 - t)^(-p).  Also exported: beta (density mode coefficients on the Radau nodes), Radau nodes tR.
usage: python3 src/export_psic.py states..."""
import sys, json, hashlib
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag, torch
for f in sys.argv[1:]:
    S = qdiag.State(f); sha = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    PsiC = S.flds['PsiC'].cpu().numpy(); tL = S.mdl.rad.tL.cpu().numpy() if hasattr(S.mdl.rad, 'tL') else None
    out = dict(source=f, sha256=sha, N=S.N, M=S.M, L=S.L, p=float(S.p), cl=S.cl, a0=S.a0, gK=S.gK, convention="raw PsiC = IPM3QL.fields(beta)['PsiC'] on the Lobatto nodes tL; psi = r^2 w(t) sum_j PsiC[i,j] sin(2(j+1) th); no endpoint cleaning",
               tL=[repr(float(v)) for v in tL] if tL is not None else None, PsiC=[[repr(float(v)) for v in row] for row in PsiC],
               tR=[repr(float(v)) for v in S.mdl.rad.tR.cpu().numpy()], beta=[[repr(float(v)) for v in row] for row in S.coef.cpu().numpy()])
    name = f.split('/')[-1].replace('.pt', '') + '.json'; json.dump(out, open('runs/psic_export/' + name, 'w'))
    print('exported', name, 'PsiC shape', PsiC.shape, 'tL', None if tL is None else len(tL), 'sha', sha[:12])

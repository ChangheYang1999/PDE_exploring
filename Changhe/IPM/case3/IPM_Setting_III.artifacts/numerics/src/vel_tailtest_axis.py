import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_layer, hs_cauchy
torch.set_default_dtype(torch.float64)
S96 = hs_cauchy.load('runs/hsG_c2.0_N96_log.pt'); S192 = hs_cauchy.load('runs/hsG_c2.0_N192_log.pt')
pts = [(S96, 1e4, 0.0, 'N96 x-axis xi=1e4 (V1/(1+xi)^p; verifier -0.7431201834954507; printed -0.74311)'), (S192, 1e3, 0.0, 'N192 x-axis xi=1e3 (verifier -0.7879849215000148; printed -0.78799)')]
for s, xi, y, lab in pts:
    print(lab)
    for kw in [dict(n0=32, per_decade=10, ngl=16, n_tail=400), dict(n0=64, per_decade=10, ngl=16, n_tail=400), dict(n0=32, per_decade=20, ngl=16, n_tail=400), dict(n0=32, per_decade=10, ngl=16, n_tail=800), dict(n0=32, per_decade=10, ngl=16, n_tail=1600), dict(n0=32, per_decade=10, ngl=16, n_tail=400, hrel=1e-4), dict(n0=32, per_decade=10, ngl=16, n_tail=400, hrel=1e-6), dict(n0=32, per_decade=10, ngl=16, n_tail=400, q=2), dict(n0=32, per_decade=10, ngl=16, n_tail=400, q=4)]:
        v1, v2 = hs_layer.hydro_V_log(s['ge'], np.array([xi]), np.array([y]), **kw); print(f"   {kw}: V1/(1+xi)^p = {float(np.asarray(v1)[0]) / (1 + xi) ** 0.5:+.12f}")

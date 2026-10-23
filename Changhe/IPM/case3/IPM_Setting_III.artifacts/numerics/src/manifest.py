"""manifest.py -- state manifest (lead 19:13Z item 1): one line per saved state that appears in a table of NUM_REPORT.md: identifier (sha256 prefix),
file, full SHA-256, representation, N x M, c_l, a0, mu (forced) or centre defect, map power p, L, Lf, gauge, and the report row it supports.
usage: python3 src/manifest.py > artifacts/MANIFEST_STATES.md"""
import sys, glob, hashlib, time, torch, re
torch.set_default_dtype(torch.float64)
now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
rows_map = [  # (glob pattern, representation label, report row)
    ('runs/r1C_cl3.0_N160.pt', 'Q fixed c_l = 3 chain (constant start)', '4L(c12)-(c14): 160x40 row'), ('runs/r1C_cl3.0_N192.pt', 'Q fixed c_l = 3 chain (constant start)', '4L(c12)-(c14): 192x48 row'),
    ('runs/r1C_cl3.0_N128_Lh.pt', 'Q fixed c_l = 3, restart at L = 0.5 (gK = 20, K = 6.30: rescaled restart)', '4L(c14) restart table'), ('runs/r1C_cl3.0_N128_L2.pt', 'Q fixed c_l = 3, restart at L = 2 (gK = 20, K = 15.87: rescaled restart)', '4L(c14) restart table'),
    ('runs/r1C_cl3.0_N128_LhK.pt', 'Q fixed c_l = 3, map L = 0.5 at fixed physical K = 10', '4L(c15)'), ('runs/r1C_cl3.0_N128_L2K.pt', 'Q fixed c_l = 3, map L = 2 at fixed physical K = 10', '4L(c15)'),
    ('runs/r1S_cl3.0_N64_a*.pt', 'Q fixed c_l = 3, 64x16 from constant starts a0 = 16 .. 40 (restart spread)', '4L(c16)'), ('runs/r1S_cl3.0_N96_a22.pt', 'Q fixed c_l = 3, refinement of the a0 ~ 6A state', '4L(c16)'), ('runs/r1S_cl3.0_N128_a22.pt', 'Q fixed c_l = 3, refinement of the a0 ~ 6A state', '4L(c16)'),
    ('runs/r1A_cl3.0_N*.pt', 'Q fixed c_l = 3, angular-only / radial-only refinement from the 128x32 endpoint', '4L(c24)'), ('runs/lsF_cl*.pt', 'Q fixed c_l, low-slope constant starts', '4L(c22)'), ('runs/lsR_cl*.pt', 'Q c_l-free releases from low-slope constant starts', '4L(c22)'),
    ('runs/r1C_cl3.0_N128_from64.pt', 'Q fixed c_l = 3, 128x32 from the 64x16 endpoint (lineage test)', '4L(c15)'), ('runs/r1C_cl3.0_N128_direct.pt', 'Q fixed c_l = 3, 128x32 from the constant start (lineage test)', '4L(c15)'),
    ('runs/rf_s1_cl3.0_N96M48.pt', 'ipm3 forced sheet 1', '4F(d), 4H, 4L(b2)/(b4): (c_l, beta) = (3, 1) reference state'),
    ('runs/rf_s1_cl1.5_b4_N96M48.pt', 'ipm3 forced sheet 1', '4F, 4L(b2)/(b4): (1.5, beta 4) reference state'),
    ('runs/bb64_cl2_beta1.0000.pt', 'ipm3 forced sheet 1', '4.4 table, 4L(b2): (2, 1)'), ('runs/bb64_cl2_beta4.0000.pt', 'ipm3 forced sheet 1', '4.4, 4G start, 4L(b2): (2, 4)'),
    ('runs/bb64_cl3_beta4.0000.pt', 'ipm3 forced sheet 1', '4.4, 4K(a) calibration, 4L(b2): (3, 4)'), ('runs/bb64_cl3_beta16.0000.pt', 'ipm3 forced sheet 1', '4.4, 4K(a), 4L(b2): (3, 16)'),
    ('runs/eps_cl2_eps*.pt', 'ipm3 forced sheet 1 (eps continuation)', '4G, 4F(b), 4L(b2)/(b4): c_l = 2 eps continuation'),
    ('runs/eps_cl1.25_eps*.pt', 'ipm3 forced sheet 1 (eps continuation)', '4G.2, 4L(d): c_l = 1.25'), ('runs/eps_cl1.1_eps*.pt', 'ipm3 forced sheet 1 (eps continuation)', '4G.2, 4L(d): c_l = 1.1'),
    ('runs/eps_cl1.2_eps*.pt', 'ipm3 forced sheet 1 (eps continuation)', '4L(d): c_l = 1.2'),
    ('runs/res_cl1.5_N*.pt', 'ipm3 unforced valley (non-smooth)', '3.5, 4A, 4L(f): c_l = 1.5 valley resolution study'),
    ('runs/rel_beta48_cl1.5_beta16.0000.pt', 'ipm3 unforced valley (non-smooth)', '3.3, 3.4, 4L(b4): valley state'),
    ('runs/root_b4_N48M24.pt', 'ipm3 forced (withdrawn sheet-2 root)', '5, 4H(a): withdrawn candidate'),
    ('runs/qls_cl*_N*_Lf*.pt', 'Q least-squares forced (L = 1)', '4K(a): forced Q states'), ('runs/qlsD*_N*_Lf*.pt', 'Q least-squares forced (L = 0.5 or 2)', '4L(c7): three-scale test'),
    ('runs/qlsrel_*.pt', 'Q least-squares release, FROZEN map (withdrawn)', '4K(b): frozen-map stalls (invalid for drift interpretation)'),
    ('runs/qfree_cl*_N*_Lf*.pt', 'Q least-squares release, rebuilt map', '4K(c): rebuilt-map releases'), ('runs/qfree2_*.pt', 'Q release, rebuilt map (clmin / L variants)', '4L(c3), (c4)'),
    ('runs/qfree3_*.pt', 'Q release, rebuilt map (radial/angular-only refinement)', '4L(c2)'), ('runs/qfix_cl*_N*.pt', 'Q fixed-c_l least squares (standard rows)', '4L(c1)'),
    ('runs/qfixM2_*.pt', 'Q fixed-c_l (Poisson grid M2 test)', '4L(c5)'), ('runs/qfixF_*.pt', 'Q fixed-c_l / free, OVERSAMPLED rows (fine = 1)', '4L(c6), (c8)'),
    ('runs/qfreeF_*.pt', 'Q free-c_l, OVERSAMPLED rows (fine = 1)', '4L(c8): QFREEF64 and its refinements'),
    ('runs/survey64_*.pt', 'Q free-c_l survey end states (rebuilt map)', '4M'), ('runs/y3_64_*.pt', 'Q secondary branch (centre row a0 = 0)', '4N'),
]
seen = set(); print(f"# MANIFEST_STATES (lane numerics), generated {now} by src/manifest.py\nColumns: id (sha256 prefix) | file | sha256 | representation | NxM | c_l | a0 | mu or centre defect (c_l + c - 1 not stored; mu for forced) | map power p | L | Lf | gauge | report row\n")
for pat, rep, row in rows_map:
    for f in sorted(glob.glob(pat)):
        if f in seen: continue
        seen.add(f)
        try:
            st = torch.load(f, weights_only=False); h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
            a0 = (st['beta'][0, 0].item() if 'beta' in st and hasattr(st['beta'], 'shape') else st['b'][0, 0].item())
            mu = st.get('mu', None); mus = f"mu={mu:+.10f}" if isinstance(mu, float) else "unforced"
            print(f"{h[:8]} | {f} | {h} | {rep} | {st['N']}x{st['M']} | c_l={st['cl']:.10f} | a0={a0:+.10f} | {mus} | p={st.get('p', float('nan')):.6g} | L={st.get('L', 1.0)} | Lf={st.get('Lf', st.get('L', 1.0))} | gauge={st.get('gK', st.get('beta', 'inf') if not hasattr(st.get('beta', None), 'shape') else 'n/a')} | {row}")
        except Exception as e:
            print(f"ERROR | {f} | {e}")

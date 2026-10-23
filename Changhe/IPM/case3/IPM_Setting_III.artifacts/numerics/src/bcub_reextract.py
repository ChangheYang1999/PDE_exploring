"""Re-extraction of the cubic coefficient b_cub from the saved eps-continuation states (lead 15:31Z item 2): the saved code src/eps_continuation.py (modified
2026-10-20T15:25Z, after the logs eps_cl2 .. eps_cl1.5_hi) fits rho_1/r and rho_3/r by cubic polynomials in r^2 at 30 log-spaced radii with
3.2e-4 <= r/min(1, eps) <= 3.2e-2 ('window A'); its comment says r in [1e-3, 3e-2] x min(1, eps) ('window B').  For every saved state both windows are
evaluated and compared with the logged b_cub and b_cub L_can^2 (printed with 5 significant digits).  Usage: python3 src/bcub_reextract.py eps_cl2 eps_cl3 ..."""
import sys, re, glob, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64); dev = torch.device('cpu')   # CPU: the shared GPU is full (192x48 run + verifier job)

def bcub_of_state(f, window):
    st = torch.load(f, weights_only=False); N, M, L, gamma, cl = st['N'], st['M'], st['L'], st['gamma'], st['cl']; eps = st['Lf']; b = st['b'].to(dev)
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev); a0 = b[0, 0].item()
    bhat = mdl.ang.to_coef(b, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0] * torch.cos(math.pi * torch.arange(M, device=dev, dtype=torch.float64))).sum().item(); K = bK
    Lcan = (K / a0) ** (cl / (cl - 1)) if K / a0 > 0 else float('nan')
    rr = (np.logspace(-3.5, -1.5, 30) if window == 'A' else np.logspace(-3.0, np.log10(3e-2), 30)) * min(1.0, eps)
    tt = mdl.rad.t_of_r(rr); Pr = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev)
    bk = (Pr @ bhat).cpu().numpy(); wr = mdl.rad.w_of_t(torch.tensor(tt), mdl.gamma).numpy()
    rho1 = rr * wr * (bk[:, 0] - bk[:, 1] / 2); rho3 = rr * wr * (bk[:, 1] - bk[:, 2]) / 2
    c1 = np.polyfit(rr ** 2, rho1 / rr, 3); c3 = np.polyfit(rr ** 2, rho3 / rr, 3); s13 = 4 * c1[-2]; d13 = 4 * c3[-2]; bcub = (s13 + 3 * d13) / 4
    return eps, bcub, bcub * Lcan ** 2, a0, K, Lcan, L

for tag in sys.argv[1:]:
    logged = {}
    for line in open(f'runs/{tag}.log'):
        m = re.search(r'eps=\s*([0-9.]+):.*b_cub=([+-][0-9.e+-]+) b_cub\*Lcan\^2=([+-][0-9.e+-]+)', line)
        if m: logged[round(float(m.group(1)), 4)] = (float(m.group(2)), float(m.group(3)))
    print(f"# {tag}: {len(logged)} logged rows; columns: eps | logged b_cub, b_cub Lcan^2 | window A (code) b_cub, rel.diff | window B (comment) b_cub, rel.diff | a0 K Lcan L")
    for f in sorted(glob.glob(f'runs/{tag}_eps*.pt'), key=lambda x: -float(re.search(r'eps([0-9.]+)\.pt', x).group(1))):
        eA, bA, bLA, a0, K, Lcan, L = bcub_of_state(f, 'A'); eB, bB, bLB, *_ = bcub_of_state(f, 'B'); lg = logged.get(round(eA, 4))
        if lg is None: print(f"  eps={eA:.4f}: no logged row"); continue
        print(f"  eps={eA:.4f} | logged {lg[0]:+.5e} {lg[1]:+.5e} | A {bA:+.5e} ({(bA-lg[0])/abs(lg[0]):+.1e}) {bLA:+.5e} | B {bB:+.5e} ({(bB-lg[0])/abs(lg[0]):+.1e}) | a0 {a0:.6f} K {K:.6f} Lcan {Lcan:.5g} L {L}")

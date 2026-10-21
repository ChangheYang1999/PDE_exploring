"""Cross-grid comparison of perturbation vectors (S3 (e) overlap of soft singular vectors, S3 (g) overlap of the prescribed-data
solutions v_i): each vector (unscaled coordinates delta b at nodes i >= 1, dc_l, dC) is mapped to delta H = delta b / b on a common
polar grid (radii geomspace 0.02..2e4, 160 points; 72 angles), the weighted L2 inner products (weights r dr dtheta, so the
near field dominates; the far-field weight is cut at r = 200 and reported separately) give the pairwise overlaps
|<u, v>| / (|u| |v|) of matching indices and the principal angles between the spans.
Usage: python3 src/s3g_compare.py A.pt B.pt [key=V|Vsoft_unscaled] [k=8]
Each .pt must contain the vectors (n x k) and 'state' (path of the state npz) [s3g_*_vectors.pt have V; svd_report files have
Vsoft_unscaled and the state is taken from the json of the same tag]."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

LANE = '.'


def load(path, key):
    S = torch.load(path); V = S[key] if key in S else S['V']
    if 'state' in S: spath = S['state'] if isinstance(S['state'], str) else str(S['state'])
    else:
        tag = os.path.basename(path).split('_softvecs')[0]; spath = json.load(open(f'{LANE}/runs/svd_{tag}.json'))['jpath']
        D = torch.load(spath); spath = D['state'] if isinstance(D['state'], str) else str(D['state'])
    model, x, d = ipn.load_state(spath); b, cl = model.unpack(x)
    return V.double(), model, b, float(cl)


def to_common(V, model, b, rr, th):
    N, M = model.N, model.M; k = V.shape[1]
    Q, TH = np.meshgrid(model.q_of_r(rr, cl_global[0]), th, indexing='ij')
    out = np.zeros((k, len(rr), len(th)))
    for i in range(k):
        dH = torch.zeros(N + 1, M, dtype=torch.float64); dH[1:] = V[:N * M, i].reshape(N, M) / b[1:].cpu()
        out[i] = model.eval_EE(dH, Q, TH).reshape(len(rr), len(th))
    return out


cl_global = [None]
if __name__ == '__main__':
    pa, pb = sys.argv[1], sys.argv[2]; key = sys.argv[3] if len(sys.argv) > 3 else 'V'; k = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    rr = np.geomspace(0.02, 2e4, 160); th = (np.arange(72) + 0.5) * np.pi / 144
    VA, mA, bA, clA = load(pa, key); VB, mB, bB, clB = load(pb, key); k = min(k, VA.shape[1], VB.shape[1])
    cl_global[0] = clA; HA = to_common(VA[:, :k], mA, bA, rr, th); cl_global[0] = clB; HB = to_common(VB[:, :k], mB, bB, rr, th)
    w = (rr[:, None] * np.gradient(rr)[:, None] * (np.pi / 144)) * np.ones((1, len(th)))
    res = {}
    for name, wsel in (('r<200', w * (rr[:, None] < 200)), ('all', w)):
        def ip(u, v): return float((wsel * u * v).sum())
        ov = [abs(ip(HA[i], HB[i])) / np.sqrt(ip(HA[i], HA[i]) * ip(HB[i], HB[i])) for i in range(k)]
        # principal angles between spans: orthonormalize in the weighted inner product
        def orth(H):
            G = np.array([[ip(H[i], H[j]) for j in range(k)] for i in range(k)]); L = np.linalg.cholesky(G); return np.linalg.inv(L)
        TA, TB = orth(HA), orth(HB)
        Cm = np.array([[ip(HA[i], HB[j]) for j in range(k)] for i in range(k)]); cosang = np.linalg.svd(TA @ Cm @ TB.T, compute_uv=False)
        res[name] = dict(overlaps=ov, principal_cosines=[float(c) for c in cosang])
        print(f'[{name}] overlaps by index: {" ".join("%.3f" % o for o in ov)}; principal cosines of the spans: {" ".join("%.3f" % c for c in cosang)}')
    json.dump(dict(A=pa, B=pb, key=key, k=k, result=res), open(f'{LANE}/runs/compare_{os.path.basename(pa).replace(".pt","")}_vs_{os.path.basename(pb).replace(".pt","")}.json', 'w'), indent=1)

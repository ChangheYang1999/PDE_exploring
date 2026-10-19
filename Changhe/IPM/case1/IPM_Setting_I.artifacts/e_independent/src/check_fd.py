"""Independent transport-residual check for a candidate (b, c_l): rho is evaluated at arbitrary points from the spectral
representation of the bounded field rho/(r^3 w) (barycentric in t, exact angular basis), derivatives by central finite
differences in Cartesian coordinates, W by the same off-grid evaluator used for characteristics (src/charac.py)."""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1, diag, charac

class RhoEval:
    """rho(x, y) from the spectral representation: b interpolated in its exact EE class (barycentric in t), then
    rho = r^3 w(r) cos^2(theta) sin(theta) b (pointwise, no aliasing)."""
    def __init__(self, m, b):
        self.m = m
        self.C_b = m.ang.to_coef(b, 'EE')            # exact: b has M EE modes
        self.n = m.ang.n['EE']
        self.fe = charac.FieldEval(m, b, 1.0)
    def __call__(self, x, y):
        m = self.m
        r = torch.sqrt(x ** 2 + y ** 2); th = torch.atan2(y.abs(), x.abs())
        t = self.fe.t_of_r(r); P = self.fe.radial_interp_matrix(t)
        sv = m.ang.s_of_theta(th)
        bval = ((P @ self.C_b) * torch.cos(sv[:, None] * self.n[None, :])).sum(1)
        w = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        return r ** 3 * w * torch.cos(th) ** 2 * torch.sin(th) * bval * torch.sign(y)

def check(path, K=400, seed=0, rmin=1e-3, rmax=1e4, hrel=1e-5, device='cuda'):
    m, b, cl, d = diag.load(path, device=device)
    fe = charac.FieldEval(m, b, cl)
    rho = RhoEval(m, b)
    g = torch.Generator(device='cpu').manual_seed(seed)
    r = torch.exp(torch.rand(K, generator=g) * (math.log(rmax) - math.log(rmin)) + math.log(rmin)).to(device)
    th = (torch.rand(K, generator=g) * (math.pi / 2)).to(device)
    X = r * torch.cos(th); Y = r * torch.sin(th)
    h = hrel * r
    rx = (rho(X + h, Y) - rho(X - h, Y)) / (2 * h); ry = (rho(X, Y + h) - rho(X, Y - h)) / (2 * h)
    r0 = rho(X, Y)
    W1, W2, bW = fe.velocity(X, Y)
    U1 = W1 - cl * X; U2 = W2 - cl * Y
    R = W1 * rx + W2 * ry - r0
    denom = r0.abs() + (cl * (X * rx + Y * ry)).abs() + (U1 * rx + U2 * ry).abs()
    out = dict(R=R, denom=denom, r=r, th=th, rho=r0)
    rr = r.cpu().numpy()
    print(f"{path}: c_l={cl:.8f}; FD transport residual at {K} random points (log-uniform r in [{rmin:g},{rmax:g}]):")
    for name, (a_, b_) in {'r<=2': (0, 2), '2<r<=10': (2, 10), '10<r<=100': (10, 100), 'r>100': (100, np.inf)}.items():
        mask = torch.tensor((rr > a_) & (rr <= b_), device=device)
        if mask.sum():
            print(f"   {name:10s} n={int(mask.sum()):4d}  max|R|={R[mask].abs().max().item():.3e}  max|R|/denom={(R[mask].abs()/denom[mask]).max().item():.3e}  max|R|/sup denom={(R[mask].abs().max()/denom[mask].max()).item():.3e}")
    return out

if __name__ == '__main__':
    check(sys.argv[1])

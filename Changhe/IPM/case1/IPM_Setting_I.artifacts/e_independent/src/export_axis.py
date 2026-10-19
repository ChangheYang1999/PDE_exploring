"""Export x-axis data for the lead's B_3 diagnostic (NOTES_FOR_TEAM 18:30Z): on a dense Chebyshev grid of x in (0, x*]:
w = W_1(x,0), h = d_y W_2(x,0), a2 = (1/2) d_y^2 W_1(x,0), b3 = (1/6) d_y^3 W_2(x,0), g1 = d_y rho(x,0), g1p = d_x g1,
G3 = (1/6) d_y^3 rho(x,0); also on [-x*/2, 0) by parity (w odd, h even, a2 odd, b3 even, g1 even, g1p odd, G3 even)."""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1, diag, charac

def axis_quantities(m, b, cl, xs, hrel=2e-3):
    """Cartesian y-derivatives at (x, 0), x in xs (torch 1-D, > 0): W from the exact off-grid evaluator (theta-Fourier
    modes of psi~), rho from the spectral representation of b; y-derivatives by high-order finite differences with step
    h = hrel * x, using the parities (W_1, rho: even/odd in y). Valid for any angular map."""
    import check_fd
    import numpy as np
    fe = charac.FieldEval(m, b, cl)
    rho = check_fd.RhoEval(m, b)
    x = xs
    h = hrel * x
    def W1_at(y): return fe.velocity(x, y)[0]
    def W2_at(y): return fe.velocity(x, y)[1]
    def rho_at(y): return rho(x, y)
    def d2_even(f):   # second derivative at 0 of an even function, 8th order
        return (-9 * f(4 * h) + 128 * f(3 * h) - 1008 * f(2 * h) + 8064 * f(h) - 7175 * f(0 * h)) / (2520 * h ** 2)
    V = np.array([[1, 1, 1, 1], [2, 8, 32, 128], [3, 27, 243, 2187], [4, 64, 1024, 16384]], dtype=float)
    Vinv = np.linalg.inv(V)
    def odd_coeffs(f):   # fit f(y) = c1 y + c3 y^3 + c5 y^5 + c7 y^7 through y = h..4h; return (c1, c3)
        ys = [f(k * h) for k in (1, 2, 3, 4)]
        c1 = sum(Vinv[0][k] * ys[k] for k in range(4)) / h
        c3 = sum(Vinv[1][k] * ys[k] for k in range(4)) / h ** 3
        return c1, c3
    w = W1_at(0 * h)
    a2 = 0.5 * d2_even(W1_at)
    hh = fe.velocity(x, 0 * h)[2]
    _, c3W = odd_coeffs(W2_at); b3 = c3W
    g1, c3r = odd_coeffs(rho_at); G3 = c3r
    hx = hrel * x
    def g1x(xx):
        hy = hrel * xx
        ys = [rho(xx, k * hy) for k in (1, 2, 3, 4)]
        return sum(Vinv[0][k] * ys[k] for k in range(4)) / hy
    g1p = (672 * (g1x(x + hx) - g1x(x - hx)) - 168 * (g1x(x + 2 * hx) - g1x(x - 2 * hx)) + 32 * (g1x(x + 3 * hx) - g1x(x - 3 * hx)) - 3 * (g1x(x + 4 * hx) - g1x(x - 4 * hx))) / (840 * hx)
    cpu = lambda v: v.detach().cpu().numpy()
    return dict(x=cpu(x), w=cpu(w), h=cpu(hh), a2=cpu(a2), b3=cpu(b3), g1=cpu(g1), g1p=cpu(g1p), G3=cpu(G3))

def export(path, out, device='cuda', n=2000):
    m, b, cl, d = diag.load(path, device=device)
    fe = charac.FieldEval(m, b, cl); Pi = fe.find_P()
    xs_ = Pi['x_star']
    k = np.arange(n); xcheb = xs_ * 0.5 * (1 - np.cos(np.pi * (k + 0.5) / n))   # Chebyshev points in (0, x*)
    xs = torch.tensor(xcheb, device=device)
    q = axis_quantities(m, b, cl, xs)
    xneg = torch.tensor(np.linspace(-xs_ / 2, -1e-6, 400), device=device)
    qn = axis_quantities(m, b, cl, -xneg)
    parity = dict(w=-1, h=1, a2=-1, b3=1, g1=1, g1p=-1, G3=1)
    full = {key: np.concatenate([parity[key] * qn[key][::-1], q[key]]) for key in parity}
    full['x'] = np.concatenate([xneg.cpu().numpy()[::-1] * 0 + np.sort(xneg.cpu().numpy()), q['x']])
    np.savez(out, cl=cl, x_star=xs_, mu1=Pi['mu1'], h_P=Pi['h'], **full)
    print(f"exported {out}: c_l={cl}, x*={xs_:.8f}, mu1={Pi['mu1']:.6f}, h(P)={Pi['h']:.6f}; {len(full['x'])} points")

if __name__ == '__main__':
    export(sys.argv[1], sys.argv[2])

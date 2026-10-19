"""Lead request 2026-10-18T00:08Z item 2: H = log(rho/(x^2 y)) = log a across the stem above P along y = 1.0 and 1.5 (and 2.0, 2.5),
|x - x*| < 1 at 0.04 spacing; H_xx by 4th-order central differences of the spectral interpolant (step 0.02).
Usage: python3 src/hline.py <state.npz> [more states]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, charac, check_fd
dev = 'cuda'
for path in sys.argv[1:]:
    m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
    fe = charac.FieldEval(m, b, cl); xs = fe.find_P()['x_star']
    rho = check_fd.RhoEval(m, b)
    def H(x, y): return torch.log(rho(x, y) / (x ** 2 * y))
    print(f"{path}: c_l {cl:.7f}, x* {xs:.6f}")
    xg = xs + torch.arange(-1.0, 1.0001, 0.04, device=dev); h = 0.02
    for yv in [0.7, 1.0, 1.5, 2.0, 2.5]:
        y = torch.full_like(xg, yv)
        Hxx = (-H(xg + 2*h, y) + 16*H(xg + h, y) - 30*H(xg, y) + 16*H(xg - h, y) - H(xg - 2*h, y)) / (12 * h * h)
        Hx = (H(xg + h, y) - H(xg - h, y)) / (2 * h)
        print(f"  y = {yv}: x - x* from -1 to 1 step 0.04")
        print("    H_xx:", np.array2string(Hxx.cpu().numpy(), precision=4, max_line_width=260, separator=' '))
        i0 = torch.argmin((xg - xs).abs()).item()
        print(f"    H_xx at x-x* = -1: {Hxx[0].item():+.4f}, -0.4: {Hxx[15].item():+.4f}, 0: {Hxx[i0].item():+.4f}, +0.4: {Hxx[35].item():+.4f}, +1: {Hxx[-1].item():+.4f}; max {Hxx.max().item():+.4f} at x-x* = {(xg[Hxx.argmax()]-xs).item():+.2f}; min {Hxx.min().item():+.4f} at {(xg[Hxx.argmin()]-xs).item():+.2f}")

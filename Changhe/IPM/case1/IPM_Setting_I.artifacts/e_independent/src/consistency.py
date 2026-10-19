"""Far-field consistency table for saved solutions: c (Green function, mode 2 at r=0) vs c (direct quadrature of the
sin 3theta moment int rho_1 r^-2 dr [+ analytic tail for disk files]), angular decay ratio of b, min b, b(inf)."""
import sys, numpy as np, torch
sys.path.insert(0, 'src')
import diag

def c_quadrature(m, b, cl):
    rho = m.rho_from_b(b); C = m.ang.to_coef(rho, 'EO'); rho1 = C[:, 1]
    r = m.rad.rR; f_ = torch.where(r > 0, rho1 / r.clamp_min(1e-300) ** 2, torch.zeros_like(r))
    P = m.rad.P_RL @ f_; integrand = P * m.rad.drdt(m.rad.tL); integrand[0] = 0.0
    if hasattr(m.rad, 'a'):          # disk: finite R, plus analytic tail with exponent k = 1/c_l
        rL = m.rad.rL; rhoL = m.rad.P_RL @ rho1
        k = 1.0 / cl; tail = (rhoL[-1] / rL[-1] / (1 - k)).item()
        return (m.rad.ccw @ integrand).item() + tail
    integrand[-1] = integrand[-2]
    return (m.rad.ccw @ integrand).item()

def row(path, device='cuda'):
    m, b, cl, d = diag.load(path, device=device)
    if hasattr(m, 'k_tail'): m.k_tail = 1.0 / cl
    cm = m.psi_xy0(m.fields(b)).item(); cq = c_quadrature(m, b, cl)
    Cb = m.ang.to_coef(b, 'EE').abs().max(0).values.cpu().numpy()
    binf = (m.rad.ext1_R @ b)[0]
    eps = float(d['eps']) if 'eps' in d.files else float('nan')
    return dict(path=path, eps=eps, cl=cl, c_model=cm, c_quad=cq, rel=abs(cq - cm) / abs(cm), decay=Cb[-1] / Cb.max(), minb=b[1:].min().item(), binf_y=binf[-1].item(), binf_x=binf[0].item(), N=m.N, M=m.M)

if __name__ == '__main__':
    print(f"{'file':52s} {'eps':>5s} {'c_l':>8s} {'c_model':>8s} {'c_quad':>8s} {'rel':>8s} {'decay':>8s} {'min b':>8s} {'b_inf(y)':>9s} {'b_inf(x)':>9s}")
    for p in sys.argv[1:]:
        try:
            r = row(p)
            print(f"{p[-52:]:52s} {r['eps']:5.3f} {r['cl']:8.5f} {r['c_model']:8.4f} {r['c_quad']:8.4f} {r['rel']:8.1e} {r['decay']:8.1e} {r['minb']:8.3g} {r['binf_y']:9.1f} {r['binf_x']:9.1f}")
        except Exception as ex:
            print(p, "->", ex)

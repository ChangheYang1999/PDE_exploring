"""V13 checks with the verifier's own polar-mode Biot-Savart (code/charsolve.py, GPU matrices from the PolarGrid
quadrature) and PolarGrid.grad:
 (1) lead 18:39Z moment law: int R phi = pi c (c - 1/2) - Q, Q = int rho W.grad phi, phi = r^-3 sin 3th,
     R = ((1/2 + c) X + W).grad rho - rho, on non-profile densities (x-even and asymmetric);
 (2) lead's Q/(pi c^2) values on x^2 (1+ay)^2 (1+r^2)^{(p-4)/2}, p = 0.6;
 (3) numerics R5b: rho_a = x^2 (1 + a y/sqrt(1+r^2))^2 (1+r^2)^{-3/4}: c = a, psi_xyy(0) = (a^2-1)/4, frozen
     one-step transport: xy coefficient of zeta_1 = (a^2-1)/(8a+2), c1 = c[zeta_1^2] (0.0505 for a=1.5, 0.068 for a=3)."""
import numpy as np, torch, sys, math
sys.path.insert(0, 'code')
from charsolve import CharSolver
torch.set_printoptions(precision=12)
def make(L=1e10, nt=64, q=8, ncore=24):
    r1 = 1e-6
    edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12), np.geomspace(0.1, 10, ncore + 1)[1:],
                            np.geomspace(10, L, int(round(np.log10(L/10)*5)) + 1)[1:]])
    return CharSolver(edges, q, nt, r1, 'cuda')
def integ(S, f):
    return float(torch.sum(S.w[:, None]*S.r[:, None]*f)*(2*math.pi/S.nt))
def Qfun(S, rho, p):
    W1, W2 = S.velocity(rho, p)
    Wr = W1*S.cs + W2*S.sn; Wt = -W1*S.sn + W2*S.cs
    gphi = 3*S.R**-4*(-Wr*torch.sin(3*S.TH) + Wt*torch.cos(3*S.TH))
    return integ(S, rho*gphi), W1, W2
def Rphi(S, rho, p, W1, W2, c):
    gx, gy = S.G.grad(rho.cpu().numpy())
    gx = torch.tensor(gx, device=S.dev); gy = torch.tensor(gy, device=S.dev)
    cl = 0.5 + c
    R = (cl*S.X + W1)*gx + (cl*S.Y + W2)*gy - rho
    return integ(S, R*S.R**-3*torch.sin(3*S.TH))
if __name__ == "__main__":
  for nt in (32, 64):
      S = make(nt=nt)
      X, Y, R = S.X, S.Y, S.R
      print(f'--- nt = {nt}, Nr = {S.Nr}')
      # (1) + (2)
      p = 0.6
      for a in (0.5, 1.0, 1.5, 2.0, 3.0):
          rho = X**2*(1 + a*Y)**2*(1 + R**2)**((p - 4)/2)
          c, b = S.moments(rho, p); c = float(c); b = float(b)
          Q, W1, W2 = Qfun(S, rho, p)
          lhs = Rphi(S, rho, p, W1, W2, c)
          print(f'poly a={a}: c={c:.10f} b={b:.2e} Q={Q:.10f} Q/(pi c^2)={Q/(math.pi*c*c):.6f} 1-1/(2c)={1-1/(2*c):.6f}'
                f' | int R phi={lhs:.10f} pi c(c-1/2)-Q={math.pi*c*(c-0.5)-Q:.10f} diff={lhs-(math.pi*c*(c-0.5)-Q):.2e}')
      # asymmetric, decaying and growing
      for name, rho, pp in [('gauss-asym', (X + 0.4*X*Y + 0.3*Y**2)**2*torch.exp(-R**2/2) , 0.5),
                            ('grow-asym', (X*(1 + 1.2*Y/(1 + R**2)**0.5) + 0.5*X**2/(1 + R**2)**0.5 + 0.4*Y**2/(1+R**2)**0.5)**2*(1 + R**2)**((0.6 - 2)/2), 0.6)]:
          c, b = S.moments(rho, pp); c = float(c); b = float(b)
          Q, W1, W2 = Qfun(S, rho, pp)
          lhs = Rphi(S, rho, pp, W1, W2, c)
          print(f'{name}: c={c:.10f} b={b:.6f} Q={Q:.10f} | int R phi={lhs:.10f} rhs={math.pi*c*(c-0.5)-Q:.10f} diff={lhs-(math.pi*c*(c-0.5)-Q):.2e}')
      # (3) numerics benchmarks
      for a in (1.5, 3.0):
          zeta = X*(1 + a*Y/(1 + R**2)**0.5)*(1 + R**2)**(-3/8)
          rho = zeta**2
          c, b = S.moments(rho, 0.5)
          W1, W2 = S.velocity(rho, 0.5)
          msk = (R < 3e-3).flatten()
          x = X.flatten()[msk]; y = Y.flatten()[msk]
          A = torch.stack([x, y, x*x, x*y, y*y, x**3, x*x*y, x*y*y, y**3, x**4, x**3*y, x*x*y*y, x*y**3, y**4], 1)
          sol = torch.linalg.lstsq(A, W2.flatten()[msk][:, None]).solution[:, 0]
          psixyy = 2*float(sol[4])            # W2 = psi_x - psi_x(0), d_yy W2(0) = psi_xyy(0)
          new, d = S.T(zeta, p_tail=0.5, info=True)
          sol2 = torch.linalg.lstsq(A, new.flatten()[msk][:, None]).solution[:, 0]
          q_ = 1/d['cl']
          c1, b1 = S.moments(new**2, q_)
          print(f'rho_a a={a}: c={float(c):.10f} (exact {a}) b={float(b):.1e} psi_xyy(0)={psixyy:.8f} (exact {(a*a-1)/4:.8f}) '
                f'cl={d["cl"]:.6f} minVr_r={d["minVr_r"]:.4f} zeta1: x-coef={float(sol2[0]):.10f} xy={float(sol2[3]):.8f} '
                f'(exact {(a*a-1)/(8*a+2):.8f}) c1={float(c1):.6f} b1={float(b1):.1e}')

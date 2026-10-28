# Figures (theory route)

balance_profiles.png and balance_profiles.csv (tools/fig_balances.py; generated 2026-10-25T07:35:11Z; log balance_profiles.log).
Nine exported primary states: the five D6-lineage states at c_l = 0.45, omega = 0.3, omega/c_l = 2/3, the degree-4
nest states at (c_l, omega) = (0.42, 0.3) (omega/c_l = 0.714) and (0.45, 1) (omega/c_l = 20/9), and the degree-6
nest states at (0.45, 0.3) (omega/c_l = 2/3) and (0.45, 1) (omega/c_l = 20/9). Primary samples and primary pressure; not an independent evaluation.

Panels, against s / r_core on a log axis:
- E_F(s) = s^(2 alpha) int_(S^2) |U(s n)|^2 dS in the gauge int |F|^2 = 1. An exact profile has E_ren =
  int_0^infinity s^(p-1) (E_F(s) - 1) ds = 0, so E_F must exceed 1 on some range of radii; it stays below 1 apart
  from overshoots of at most 8e-5 beyond 64 core radii.
- Phi(s) / Phi_req(s): head flux of |U|^2/2 + P through the sphere over the flux an exact profile needs,
  Phi_req = (c_l/2)(p M(s) - s M'(s)), M(s) = int_(B_s) |U|^2 (exact value 1 at every s).
- H_F(s) = s^(2 alpha + 1) int_(S^2) U . Omega dS; negative at every sampled radius on every state.
- Helicity in B_s (dotted) and the same plus the exterior term H_F(s) s^(2 - 2 alpha)/(2 alpha - 2) (solid). The
  solid curve is the estimate of H_tot from radius s; exact value 0.

Exterior error: the exterior term is the analytic integral of the representation's own leading helicity tail. The
column exterior_change_estimate is |H_F(s) - H_F(s/4)| s^(2 - 2 alpha)/(2 alpha - 2). It is at most 1e-12 at the
outermost radius, which shows only that H_F has converged on the sampled grid; it is not a bound on modelling error.
The verifier's omitted-helicity bound for the Cartesian channel families is the rigorous counterpart on the
independent route.

profiles.png, profiles.csv and spectral_decay.csv (tools/fig_profiles.py; generated 2026-10-25T07:35:45Z; log profiles.log). Same nine states, primary
samples, pressure and coefficients; theory-route evaluation, not independent. Single spheres of the export grid
r_core 2^(j/4), not the registered shells of SPEC 3.
- Residual versus radius: RMS(R_u) over the sum of the RMS of the five terms on each sphere; csv also has the ratio
  against the nonlinear terms, the single-term ratio and RMS(R_u) r^(2 alpha + 1).
- Non-axisymmetric content versus radius: fraction of the sphere energy of the spherical components in azimuthal
  modes m != 0 (spherical components are rotation-equivariant, so this is the true azimuthal content).
- Tail convergence: V(r) = r^alpha U_sph(r, theta, chi - (omega/c_l) log r) (spectral shift in phi, Nyquist mode
  dropped), relative L2 distance on S^2 to V at the last radius and to V(4r). These are convergence errors on the grid,
  not fitted slopes.
- Spectral decay: degree power of the Cartesian components of U on the sphere at r_core and 2^10 r_core (all m, l <= 24,
  normalized), and the radial Chebyshev decay of the toroidal block (per mode |a_k| / max_k |a_k|, maximum over modes).
  Raw coefficient magnitudes by degree are not shown because the radial basis factor r^l (s/R0)^(-(alpha + l)) scales
  them with l.

balance_profiles_v2.png and balance_profiles_v2.csv (tools/fig_balances_v2.py; first run 2026-10-25T17:42:13Z, panel
layout revised and regenerated 2026-10-25T17:42:39Z (file time); log balance_profiles_v2.log). Supersedes balance_profiles.png for
the report. Seven exported primary states: d6w_L8 at (c_l, omega) = (0.45, 0.3) (omega/c_l = 2/3), nest6_L6 at
(0.45, 1) (omega/c_l = 20/9), and the degree-8 nest states nest8_L8 at (0.42, 0.3) (omega/c_l = 0.714), (0.45, 0.3)
and (0.45, 1), the last two each as exported and after the 150-iteration continuation (cont150). Primary samples and
primary pressure; theory-route evaluation, not an independent evaluation.

Changes from version 1: (i) the exterior helicity uses both terms of SPEC v1.24 7.8,
H_F R^(2 - 2 alpha)/(2 alpha - 2) + K_H R^(1 - 3 alpha)/(3 alpha - 1), with the asymptotic H_F and K_H(carried) read
from each state's meta_supplement_v124.json (the state's own first far coefficients, not the values an exact profile
would need); (ii) a sixth panel, E_ren(s) = int_(B_s) |U|^2 - s^p E_F(s)/p; (iii) the solid helicity curve is drawn
only for s >= 4 r_core, because the two-term exterior is an asymptotic expansion and is meaningless inside the core
(at s = r_core the K_H term alone is of order 1 to 80); (iv) an exterior error panel.

Exterior error estimates (panel 6): |two-term total minus one-term total| (solid; the one-term total uses the sampled
H_F(s), as in version 1) and the change of the two-term total over two octaves (dashed). At s = 16 r_core the one- and
two-term totals differ by at most 4.3e-3 on the nest states and by 5.8e-2 on d6w_L8; at the outermost radius
(2^20 r_core) the difference is below 1e-13 and the two-octave change is 7e-12 to 2e-11 on every state. The latter
floor is the quadrature of the ball integral, not a modelling bound.
Neither curve is a bound on the omitted helicity: the far-coefficient values used here do not bound the remainder of
the expansion. Bounds on the omitted region, with their onset radius and constants, are the independent route's
separately derived exterior bounds, cited with their hypotheses.

Values at the outermost radius (H_tot is the two-term total; H_tot / int_ball |h| uses the ball integral of |h| only):
- d6w_L8 (0.45, 0.3): H_tot = -6.586, H_tot / int |h| = -0.879, E_ren = -0.982; K_H(carried) / K_H(required) = 1.60.
- nest6_L6 (0.45, 1): -4.535, -0.712, -1.543; 1.26.
- nest8_L8 (0.42, 0.3): -3.037, -0.788, -3.940; 1.21.
- nest8_L8 (0.45, 0.3): -4.041, -0.881, -1.765; 1.28. cont150: -4.107, -0.879, -1.740; 1.26.
- nest8_L8 (0.45, 1): -4.555, -0.702, -1.590; 1.05. cont150: -4.580, -0.701, -1.583; 1.05.
An exact profile has H_tot = 0, E_ren = 0 and K_H(carried) / K_H(required) = 1. Every state has both whole-space
balances of order 1 and negative. The helicity ratio of the (0.45, 1) degree-8 states (1.05) is the closest to 1
measured so far; their energy ratio K_E is far from 1 (K_ratio_direct -4.94 in the same supplement for cont150).

# NUM_REPORT (lane numerics) -- numerics for IPM Setting I

2026-10-19T00:19:47Z (shift 7; 3.18 items 16 c6hF and 17 c6gR4 added; relays of chain steps 47, 37-40, 48, 49 follow as they finish). Header history: the shift-2
header said "Last update 04:45Z" and was not refreshed in shifts 3-6 although sections 3.17, 3.18 and 4 were (their items carry their own real times);
the shift-1 header once said 18:45Z, an estimate, wrong: the real time was 18:16Z.
Status (shift 9, 2026-10-19T11:40Z, the last shift before the run cap 2026-10-19T17:37Z): the lane's closing verdict, T0 and T_end are section 4 (p) (6); (p) (1)-(5) are shift 8, (o) shift 7, (n) shift 6. The team candidate is X3 = c6g (3.18 item 7; lead 16:46Z, verifier G74),
produced by the lead's LSQR fit run on this lane's GPU port (3.18); its domain columns (90 / 300 / 9000 L), resolution rows (m <= 100 / 150 / 200 / 250
angular, 244 radial), budget row and controls are 3.18 items 8-16; the independent inverse checks are 3.17 item 7. Earlier status lines: shift 2 (02:12Z):
second solver rebuilt as oversampled least squares (3.16); between-node residual 1e-6 away from P at (256,64)-(320,80); c_l is NOT determined by the
discretised equations at these grids (valley; all pinning constraints tried fail). Shift 1: tools built and validated (compactified reference, disk
closure, characteristics); the c_l0 = 3 homotopy family produced no candidate; construct1 was reproduced by square collocation to 0.1-0.2 percent in
c_l (3.12-3.15), which section 4(d) explains as a position in the valley.
## 1. Formulation implemented (follows SPEC.md v2, class A, canonical velocity law V1, closure N3(b))
- rho = x^2 y a(x,y), a = w(r) b(r,theta), w = (1 + r^2/L^2)^((gamma-3)/2), gamma = 1/c_l frozen per solve and
  updated in an outer loop; b is even/even and bounded on the closed compactified plane.
- Compactified radial coordinate t in [-1,1], r = L (1+t)/(1-t)^p, p = 1/(1-gamma) (so that the far-field correction
  series in powers of r^(gamma-1) becomes a Taylor series in 1-t). Chebyshev-Gauss-Radau points in t (t=-1 is the centre,
  t=+1 is infinity and is not a collocation point). Angular grid theta_j = (j+1/2)pi/(2M) on the open quadrant, four parity
  classes handled by exact M x M transforms.
- Velocity: modal Green function (SPEC V1), each mode n = 2,4,...,2M obtained from two first-order ODEs collocated on the
  Lobatto grid after rescaling by r^2 (1+r^2/L^2)^((gamma-1)/2); the growth condition psi_n = o(r^n) is built in.
  No subtraction, no harmonic term. c = psi_xy(0) read off the mode-2 coefficient at r=0.
- Equation solved (the profile equation divided by x^2 y w):
    (c_l X + U).grad b + [c_l r w'/w + U_r w'/w + 3 c_l - 1 + 2 U_1/x + U_2/y] b = 0,
  which is regular everywhere (U_1/x, U_2/y are smooth by parity). At r=0 it reduces to (3c_l - 1 - c) b(0) = 0.
- Discrete system: b at the (N+1) x M Radau points and c_l; rows: b(0,theta_j) = 1 (normalisation + continuity),
  the equation at all other points, and 3 c_l - 1 - c[b] = 0 (c_l is not fitted; the identity will additionally be checked
  by the independent formula c = int rho_1 r^-2 dr and by the far-field exponent).
- Newton with exact dense Jacobian (the velocity maps are linear in b and are assembled as dense matrices on the GPU),
  backtracking line search, homotopy continuation from a manufactured starting point.

- Dealiasing (added 19:37Z): products such as cos^2(theta) sin(theta) b carry M+1 odd modes; the Poisson source is therefore
  formed on a finer angular grid (M+2 points), the modes n = 2..2(M+2) are solved, and psi~, r psi~_r, psi~_theta are
  evaluated pointwise on the coarse grid (and off-grid) from the fine mode functions. The collocation residual is then the
  exact residual of the represented function (agreement with an independent finite-difference evaluation to 3e-9).
- Characteristics solver (src/charac.py, src/batchmap.py): backward characteristics of W = c_l X + U from any point to a box
  of size delta around the x-axis stagnation point P, entry time interpolated inside the last RK4 step, data rho = C y on
  the box; batched over thousands of trajectories and over perturbed fields (finite-difference Jacobians of the resulting
  maps). Doubly consistent map Psi: for a given shape choose c_l such that h(P) = d_y W_2(P) = 1 (bracketing + bisection),
  set the amplitude by the identity, transport from P, renormalise (identity, a(0) = 1 by spatial rescaling).

## 2. Verification of components so far
- Radau differentiation: 6e-13 at N=64 (tests/test_basic.py). Angular transforms/derivatives: 1e-15.
- Full-plane Poisson inverse (tests/test_poisson.py), manufactured psi = xy(1+r^2/L^2)^((gamma-1)/2)(1+0.7(x^2-y^2)/(1+r^2)),
  gamma = 0.6, L = 1.3:
    N=32,M=8:   max |Psi~ err| 7.0e-08, rel velocity error on r<=5: 9e-07
    N=64,M=12:  3.7e-14, 1.4e-12
    N=128,M=16: 3.4e-15, 2.1e-14
  psi_xy(0) recovered to 1e-12 (N=64), U(0)=0 exactly, far-field row (r=infinity) exact to 4e-15.
- Jacobian of the collocation system vs central finite differences: relative error 2e-10..1e-9 on sampled columns
  (tests/test_newton.py); manufactured Newton target recovered in 5 steps to 3e-15.
- Elliptic residual evaluated independently of the Green-ODE route (second derivatives of the mode functions):
  |E_ell|/max|d_x rho| = 8e-6 (N=32,M=8), 7e-12 (N=64,M=12), 7e-13 (N=128,M=16) (tests/test_ell.py).
- Independent transport residual (src/check_fd.py: rho from the spectral representation, Cartesian central differences,
  off-grid velocity) agrees with the collocation residual to 3e-9 relative on a test field.
- Characteristics transport: (W.grad rho' - rho')/rho' = 2e-9..3e-5 at test points (dt = 0.005), the larger values at
  near-axis points (RK4 through the saddle passage); off-grid velocity equals the grid velocity to 6e-11.
- Axis export tool (src/export_axis.py) for the lead's B_3 diagnostic: g1, g1p, G3 against sympy to 1e-15..1e-12 on a
  manufactured rho; a2, b3 against finite differences of W to 1e-7.

## 3. Results so far (all at N=48, M=10, L=1 unless stated; times are real UTC times from file mtimes)

### 3.1 Global spectral Newton with homotopy: every branch folds before the true equation
Homotopy E - (1-eps) S0 = 0 from a manufactured start (b0 = 1, i.e. rho = x^2 y (1+r^2)^((gamma-3)/2)) with the identity row
either perturbed consistently or kept exact:
- c_l0 = 1.5, 2.5, 4.0 (identity perturbed): natural continuation fails at eps = 0.225, 0.5, 0.575; c_l drifts down,
  the far-field amplitude b(inf) grows (1 -> 290, 377, 106) and smin(J) -> 1e-4 (runs/probe_cl*.log, 18:18Z).
- Pseudo-arclength (runs/arc_cl2.5.dat): the c_l0 = 2.5 branch folds at eps_max = 0.515 and never returns to eps = 1.
  Resolution (N,M) = (64,12), (96,16): folds at eps 0.44, 0.46 within 120 steps (step-limited).
- 27 start shapes x c_l0 in {1.3, 2, 3} (runs/shapes.log): none reaches eps = 1 (best 0.725).
- Identity-preserving homotopy from b0 = 1 + A s2 with 3c_l0 - 1 = c[b0] (runs/hom2_cl2_arc.dat): folds at eps = 0.356 with
  c_l pinned at 2.001; arclength returns to eps < 0.
- Fixed-c_l homotopy (identity row dropped; runs/fixcl_*.npz): c_l = 3 reaches eps = 0.825 with the identity residual
  3c_l - 1 - c growing monotonically to +0.75 and rho > 0 in Q; c_l = 2 fails at eps = 0.25; c_l = 1.5 at 0.125.
- Levenberg-Marquardt on the full square system from the c_l = 3 branch end stalls at |F|_inf = 0.22 (identity row), with
  rho changing sign in Q (runs/lm_fixcl3.dat).
Structure of the Jacobian at identity-consistent points: smin/smax ~ 1e-7; the near-null right singular vectors live in the
far field (r > 10) near both axes and the left ones at the centre rows: the far field near the axes is almost unconstrained.
Dynamic rescaling in pseudo-time (rho_tau = rho - W.grad rho, c_l from the identity) is unstable: amplitude grows x3 per unit
tau from b = 1 and blows up by tau = 5 (runs/dyn_cl2.0.dat).

### 3.2 Characteristics solver (SPEC Lemma 4), verified
src/charac.py integrates backward characteristics of W = c_l X + U[rho] from any point to a box of size delta around the x-axis
stagnation point P, with the entry time interpolated inside the last RK4 step, and returns rho = C y_entry e^{T_entry}.
Checks (tests/test_charac4.py): the transported function satisfies (W.grad rho' - rho')/rho' = 2e-9 .. 3e-5 at 10 test
points (dt = 0.005; the larger values are at near-axis points, RK4 error through the saddle passage whose rate is 4c_l - 1).
Important structural fact confirmed numerically: for a frozen field with h(P) = d_y W_2(P) != 1, e^T y(-T) does not converge
(it decays like e^{(1-h)T}) and the transported function depends on delta like delta^{1-1/h}; only when h(P) = 1 (Lemma 3)
is rho = C eta_P well defined. Likewise the centre exponent of rho_y(x,0) is 2 only when 3c_l - 1 = c.
Consequence for solvers: for a frozen W the two scalar conditions (identity at 0, h(P) = 1 at P) are not automatically
satisfied; a fixed point of any Picard-type iteration must satisfy both, which is why the frozen-W problems are singular.

### 3.3 Fixed-c_l characteristics Picard (identity and a(0) = 1 re-imposed each step): not contractive
runs/shoot2_cl3.log (19:00Z): x* = 3.17 -> 11.4 -> 1.06 -> 13.2, h(P) = 1.18 -> 0.76 -> 2.70 -> 1.81 in four iterations;
for c_l = 2 the first iterate loses the stagnation point. Anderson acceleration with damping is running (runs/and_cl*.log).

### 3.4 Sign of the strain at P for fixed shapes (src/scan_cl_shape.py, src/run_shoot3.py, 19:13Z-19:18Z)
For a fixed shape b with the amplitude set so that c = 3c_l - 1, h(P) = d_y W_2(P) was computed as a function of c_l.
Simple shapes (b = 1, 1 + 10 r^2/(1+r^2), angular variants): h(P) - 1 = +1.2 at c_l = 1.2 rising to +6 at c_l = 8, i.e.
psi_xy(P) > 0, while Lemma 3 requires psi_xy(P) = 1 - c_l < 0. The homotopy end-point shape runs/fixcl_3.0.npz (far-field
amplitude b(inf) ~ 800 relative to b(0) = 1): h(P) - 1 changes sign at c_l = 2.46132. Consistency: mu1 + h(P) = 2c_l
(div U = 0) holds to 1e-5 for smooth shapes.
Doubly consistent iteration (c_l chosen so that h(P) = 1, amplitude by the identity, transport from P, renormalisation):
from fixcl_3.0 the first step gives c_l = 2.46132, h(P) - 1 = 5e-15, a positive transported profile with b(inf) = 1364,
rescaled x* = 5.49; for the transported shape h(P) - 1 < 0 for all c_l in [1.05, 12] (undamped map overshoots). Damped
version (theta = 0.3, mixing in physical space) and Newton on the extended system (b, c_l) with equations b - Phi = 0 and
h(P) - 1 = 0 are running (runs/shoot3_c.log, runs/nm2_a.log).

### 3.5 Resolution of the homotopy branches; identity-preserving arclength with det sign (dealiased code, 19:43Z-19:53Z)
- The homotopy end-point shapes are NOT angularly resolved: runs/fixcl_3.0.npz (N=48, M=10) has EE angular coefficients
  (max over r) 133, 194, 159, 133, 105, 85, 74, 50, 49, 44 for k = 0..9 (no decay), although its radial Chebyshev
  coefficients decay from 27 to 8e-3. The fixed-shape results of 3.4 that used this shape (the h(P) = 1 root at c_l = 2.46,
  the characteristics iterations and Newton on Psi started from it) are therefore not trustworthy; the statement that simple,
  well-resolved shapes have h(P) > 1 for every c_l stands. SPEC v3 identities D9(1)-(3) hold to 1e-7 with the axis tool on
  smooth fields and fail at the percent level on fixcl_3.0, confirming the diagnosis.
- Identity-preserving homotopy from b0 = 1 + A s2 (3c_l0 - 1 = c[b0]) followed by pseudo-arclength (runs/arc2_*.dat,
  N=48, M=10): eps_max = 0.174 for c_l0 = 2 and 0.462 for c_l0 = 3; c_l stays within 1e-3 of c_l0 along both branches;
  sign(det J) changes at the fold of the c_l0 = 2 branch (eps = 0.174) and twice more near eps = -0.066; no sign change on
  the c_l0 = 3 branch within 250 steps. At the fold the angular spectrum of b is flat (top/max = 0.42 at N=48, M=10), so
  the fold position is being tested against resolution (runs/arc3_cl3.log: (N,M) = (48,10), (64,16), (96,24), (128,32)).
- Structure along the identity-preserving branch (runs/arc3_cl3.0_N64M16_end.npz, eps = 0.38): b is angle-independent to
  a few percent for r <= 3 and grows smoothly with r (1, 1.9, 7.5, 26 at r = 0.05, 0.2, 0.8, 2.7), while the far field is
  concentrated in a layer near the y-axis: b(inf, theta) = 34, 20, 40, ..., 62, 60, 126, 223, 731 at theta = 2.8, 8.4, ...,
  64.7, 70.3, 75.9, 81.6, 87.2 degrees. The angular spectrum decays by a factor 10 (k = 0 to 15) at M = 16 and not at all
  at M = 10. A class-A profile on this branch, if it exists, has its far-field density concentrated along the y-axis (the
  saddle ejects trajectories along the y-axis), so angular resolution near theta = pi/2 is the limiting factor; an angular
  coordinate map is being added.

### 3.6 How far the branch can be followed versus resolution (identity-preserving homotopy, c_l0 = 3)
Pseudo-arclength (runs/arc3*_*.dat): the branch turns at eps = 0.46 (48,10), 0.70 (64,16), 0.82 (96,24) with a flat angular
spectrum at the turn. Newton/Levenberg-Marquardt natural continuation (runs/lmc*_cl3.log), which damps the near-free
far-field directions: the continuation stops at eps = 0.505 (128,32), 0.52 (160,40), 0.65 (192,48); (96,24) continues to
0.75 but only on a discrete branch whose far field oscillates at the grid scale for theta < 40 degrees and has negative
density (min b = -3 at eps 0.48, -159 at 0.75); on the well-resolved grids min b > 0 throughout. (256,64): running.
The stopping points are not converged with resolution and are not folds: the smallest singular vector of the Jacobian at
eps = 0.5 on (128,32) (singular value 5.8e-7 against 3.5e3) has 97 percent of its energy in the far field r > 10 and
84 percent in the angular bin 79-90 degrees, and its residual image is entirely in the centre rows (identity and
normalisation). The far-field y-axis layer amplitude is therefore a nearly free direction, and the dense collocation
continuation is limited by the resolution of that layer. Angular maps clustering the collocation angles near the y-axis
(or near both axes) are more accurate per point at fixed eps (3.7) but track the branch worse (arclength turns at 0.49 and
0.22 at (64,16)); they were set aside. Row scaling of the far-field equations does not change the smallest singular value.

### 3.7 Convergence of the branch at fixed eps (src/fixed_eps_compare.py, 20:14Z)
At eps = 0.3 all well-resolved grids agree: b(inf) max = 616-626 and the far-field profile b(inf, theta) at 5, 20, 45, 70,
80, 85, 88 degrees = 28, 29, 32, 58, 150, 362, 590 to 1-2 percent for unmapped (128,32) and for mapped grids (64,16) and
(96,24) with clustering near the y-axis (beta = 0.5, 0.8); unmapped (64,16) and (96,24) are 2-10 percent off and their
angular spectra decay only by factors 13 and 18. At eps = 0.5 the unmapped (96,24) and (128,32) grids give the same
amplitude b(inf) max = 1192.7 but differ in the far field near the x-axis (-0.8 versus 40 at 5 degrees). c_l stays within
1.5e-3 of 3 on all grids. So the branch is a genuine, convergent family up to at least eps = 0.5; what moves with resolution
is the fold position (where the far-field angular structure near both axes stops being resolved).

### 3.8 Hybrid formulation (src/hybrid.py, 20:35Z)
To remove the near-free far-field directions, the far-field rows of the collocation system (r_i > R_i) are replaced by the
exact transport relation b_i = T_i(b, c_l): rho at a far point equals e^T times rho at the entry point of its backward
characteristic into the disk r <= R_i (R_i beyond the stagnation point P), computed with the characteristics machinery of
3.2; the interior rows keep the collocation equations (with the homotopy source restricted to r <= R_i). The Jacobian of the
far rows is analytic at frozen trajectories (quasi-Newton). First run: runs/hyb_128x32_Ri10.log (in progress).

### 3.9 The compactified formulation pins c_l (found 20:48Z); disk closure (SPEC N3a) as primary formulation
With the far-field growth r^gamma factored out and gamma frozen, the collocation rows at the outermost Radau points
(r ~ 1e8..1e10) reduce to (c_l gamma - 1) b + o(1) = 0 and therefore fix c_l = 1/gamma; the identity row 3c_l - 1 = c[b] is
then satisfied by adjusting the far-field amplitude. This explains c_l = 3.000 +- 1e-3 on every compactified branch: those
branches are at prescribed c_l. Results 3.1-3.7 remain correct as statements about the discrete homotopy problems, but they
say nothing about the self-consistent value of c_l.
The disk closure (src/ipm1disk.py): unknowns on r <= R, far field = homogeneous extension of degree k = 1/c_l of the boundary
data, tail integrals analytic (SPEC N3a); validated against the compactified Poisson solve on a smooth test density
(relative velocity error on r <= 5: 1.0e-6 at R = 100, 5.3e-8 at R = 300, 2.2e-9 at R = 1000; psi_xy(0) to 3e-7, 2e-8,
7e-10). Its outer rows are regular, so c_l is free. The same identity-preserving homotopy (start rho = x^2 y (1 + 27.1
r^2/(1+r^2)) (1+r^2)^{-4/3}, c_l0 = 3) on the disk gives a smoothly varying c_l(eps): (96,24), R = 300: c_l = 2.94, 2.73, 2.54,
2.43, 2.33 at eps = 0.06, 0.3, 0.5, 0.6, 0.74 (|F| ~ 1e-11, density positive to eps = 0.72, continuation fails near 0.75);
(128,32), R = 300: c_l = 2.805 at eps = 0.3 (3 percent above (96,24)). smin/smax(J) ~ 5e-10: the near-null direction is
intrinsic (y-axis amplification), not an artefact of the compactified rows. Runs at R = 1000 and (128,32) are in progress.

### 3.10 h(P) along the homotopy, and a withdrawn interpretation (20:56Z-21:05Z)
Along the disk branch h(P) = d_y W_2(P) = 2.90, 2.44, 2.21 (eps 0.3, 0.5, 0.6; (96,24)) and 2.75, 2.34, 2.13 ((128,32)),
roughly h(P) - 1 = 2.5 (1 - eps). An earlier version of this section (21:02Z) interpreted this as a violation of Lemma 3 and
as evidence that the discrete solutions approximate singular frozen-velocity transport solutions at P. That was WRONG and is
withdrawn: Lemma 3 (h(P) = 1) holds for solutions of the true equation only; along the homotopy the y-derivative of the
modified equation at P reads (h - 1) g = (1 - eps) d_y S0(P), so h(P) - 1 is proportional to 1 - eps by construction, and
the axis trace g = rho_y(x,0) of the disk solutions is smooth through P (local log-slopes of |g| against |x - x*| are 0.00 to
0.03 on both sides at eps = 0.6, against -0.4 predicted for a singular solution). The branches therefore do approach the
Lemma 3 condition as eps -> 1, as they must.
The remaining facts stand: c_l(eps) differs between discretisations and grids (disk 2.73/2.80 at eps = 0.3; tied 2.99) because
the different discrete source terms S0 define different homotopies and because the far field, which contributes a few
percent to c = int rho_1 r^-2 dr, is a nearly free direction (3.6); only eps = 1 solutions are comparable across methods.

### 3.11 Far-field consistency test (src/consistency.py, 21:07Z)
For the same discrete b, c = psi_xy(0) is computed in two ways: from the mode-2 Green function at r = 0 (what the solver
uses) and by direct quadrature of int rho_1 r^-2 dr (plus the analytic tail for the disk). Smooth test fields: agreement to
1e-4 on the compactified grid, 1e-12 on the disk. Branch solutions: disk (96,24) eps 0.3, 0.5: 2.5e-5, 7e-5 relative; disk
(128,32) eps 0.3, 0.6: 5e-5, 1.6e-4; compactified (pinned gamma) (128,32) eps 0.5: 8.00 vs 47.0; compactified (tied gamma)
(96,24) eps 0.3: 8.00 vs 1.66, eps 0.9: 7.84 vs 12.1; tied (128,32) eps 0.3, 0.5, 0.6: 8.00 vs 9.40, 4.16, -0.18.
The compactified branch solutions are therefore not consistently represented in the far field (the radial approach to
r -> infinity over the last nodes is unresolved) even where their angular profiles at infinity agree across grids; their c_l
values and the tied (96,24) end point at eps = 0.9775 are not trustworthy. Only the disk solutions pass this test, and the
disk closure is the primary formulation from here on (R-convergence study running).

### 3.12 Independent reproduction of the lead's candidate construct1 (src/reproduce.py, from 21:12Z)
The lead constructed a candidate (lead/astra/construct1/final_candidate.npz: c_l = 5.5763219, x* = 8.60088,
h(P) = 1 - 4e-6 per the verifier, far field peaked near theta = pi/4). It is projected onto the disk grid (cubic interpolation
of H = log a in (log r, theta)) and the TRUE equations (identity row, c_l free) are solved by Levenberg-Marquardt.
Independent residual of the projected candidate (normalised transport residual, bands r<=2 / 2-10 / 10-100 / >100):
(64,16): 1.3e-3 / 2.6e-3 / 1.0e-1 / 1.5e-1; (128,32): 3.6e-4 / 1.5e-3 / 6.2e-3 / 1.5e-2; (192,48): 1.6e-4 / 7.4e-4 /
3.1e-3 / 4.5e-3 (R = 1000, L = 5): decreasing with resolution, i.e. dominated by my discretisation of the projected field.
Levenberg-Marquardt solutions of the TRUE equations from the projected candidate (L = 10 unless stated):
| grid     | R     | c_l     | x*      | h(P)-1  | c Green vs quadr. | max pointwise normalised R | equation residual (divided) |
|----------|-------|---------|---------|---------|-------------------|----------------------------|-----------------------------|
| (128,32) | 1000  | 5.58134 | 8.57734 | +3.0e-3 | 8.2e-6            | 2.4e-4                     |                             |
| (192,48) | 1000  | 5.57869 | 8.60012 | +8.2e-4 | 7.6e-6            | 2.4e-5                     | 7.0e-7                      |
| (192,48) | 1000 L=20 | 5.57944 | 8.60028 | +4.6e-4 | 7.0e-6        | 4.7e-5                     | 3.4e-7                      |
| (192,48) | 3000  | 5.57278 | 8.59245 | +5.4e-4 | 1.1e-6            | 2.3e-5                     | 4.6e-7                      |
| (192,48) | 10000 | 5.57688 | 8.60170 | +1.0e-4 | 8.2e-7            | 2.2e-5                     |                             |
| (256,64) | 1000  | 5.58022 | 8.60182 | +1.4e-4 | 7.5e-6            | 6.9e-6                     |                             |
| (256,64) | 3000  | 5.57864 | 8.60313 | +1.9e-4 | 1.2e-6            | 2.3e-8                     |                             |
| (320,80) | 1000  | 5.58233 | 8.60823 | +1.3e-4 | 7.4e-6            | 1.1e-8                     |                             |
| (256,64) | 10000 | 5.57993 | 8.60347 | +1.4e-4 | 3.4e-7            | 8.0e-7                     | 9.5e-6 (reduced LM, a(0)=1) |
| (256,64) | 30000 | 5.6311 (unreliable: radial resolution) | | | | | 1.0e-5 |
| construct1 |     | 5.57632 | 8.60088 | -4e-6   |                   |                            |                             |
All reproduced solutions have positive density and one stagnation point on the x-axis. h(P) -> 1 with resolution (Lemma 3
satisfied in the limit: 3.0e-3, 8.2e-4, 1.4e-4, 1.3e-4 at R = 1000 for (128,32), (192,48), (256,64), (320,80)); c_l agrees
with the candidate to 0.1 percent but does NOT converge with resolution at the LM floor (5.5813, 5.5787, 5.5802, 5.5823): at
residual level 1e-6 the equations determine c_l only to about +-0.1 percent (the nearly free far-field direction couples to
c, 3.6); x* agrees to 1e-3 (8.577, 8.600, 8.602, 8.608); the change of c_l with R at fixed
(N, M) is radial-resolution error (6e-3), far above the closure drift R^-1.64 estimated by the lead, which is therefore not
measurable at these grids. D14 measured directly from the residual's centre expansion (fit of the cos 0 and cos 2theta coefficients of the divided
residual over the first six radial rows, r = 3.7e-4 .. 1.4e-2 at (256,64)): x^4 y and x^2 y^3 coefficients +2.3e-7 and
-3.1e-7 at (256,64), R = 3000 (the lead reports 7.6e-3 and -1.25e-2 for the candidate's trial, whose fit rows start at r = 0.31);
an earlier Taylor-based combination printed in the logs was wrong and is withdrawn (lead 21:29Z). Sensitivity: at the (192,48)
LM state the smallest singular value of the Jacobian is 1.3e-7 (smax 8.8e3) with c_l component -0.065 and 89 percent of the
right singular vector in the far field r > 10, so at residual level 1e-6 c_l is determined only to about 1e-3 relative. Caveats: the LM iteration stalls with normalisation defects |a(0) - 1| ~ 1e-5 (a spatial rescaling) and leaves
high-mode noise (my own elliptic residual 3e-4 .. 1.5e-3 in the bulk, versus 1e-12 for smooth fields); a (320,80) run and
(256,64) at R = 3000, 10000 are queued.
Axis exports for the B_3 diagnostic: runs/axis_w_rep_*.txt (w(x) on (0, 1.3 x*], 12 digits). Plain-array field exports for
independent residual checks: runs/rep_fields_N256M64R1000L10.npz, runs/rep_fields_N256M64R3000L10.npz (r, theta, rho, a,
psi, U1, U2, W1, W2, c_l, R, far-field exponent).

### 3.13 Newton from the lead's seeds (lead request 21:29Z), from 21:38Z
The lead provided projections of construct1 onto my disk grids (lead/notes/num_seed/seed_c1_*.npz). In my model the
(256,96), L = 8, R = 1e4 seed has residual 3.8e-3 (equation rows) and identity offset -3.06e-5 (the disk-closure error,
scaling like R^-1.64 per the lead). Plain Newton with the exact dense Jacobian does not converge from it: 15 iterations leave
the residual at 3.8e-3 .. 3.9e-3 while c_l drifts from 5.57632 to 5.54753, because the Newton direction is dominated by the
nearly free far-field mode (3.12). Reduced Levenberg-Marquardt (normalisation fixed exactly) from the post-Newton state then
reaches |F|_inf = 1.35e-5 (|F|_2 8.6e-5, identity -2.9e-7) after 100 iterations with c_l = 5.5601, still moving toward the
candidate value as the residual falls (5.5478 at iteration 20, 5.5586 at 90): c_l is set by the slowest, far-field mode. The
SVD of the Jacobian at this state and the table for (192,48), (256,64), (320,80) at R = 1e4 and 3e4 are running/queued
(runs/seed_*.log, runs/seedp_*.log).

### 3.14 Why c_l is weakly pinned, and the h(P) row (lead request 21:49Z; src/hrow.py), from 21:56Z
At the (256,64), R = 3000 LM state the Jacobian has singular values 2.9e3 (largest) and 1.8e-6, 4.2e-7, 4.2e-9 (smallest): the
discrete system is numerically singular. Along the smallest right singular vector (unit discrete norm), with x* re-solved:
d c_l/ds = +0.0373, d x*/ds = +0.0150, d h(P)/ds = +3.5e-5 (stable for step sizes 1e-4 .. 1e-2), so d h(P)/d c_l = +9.5e-4 along
the mode. The nearly free direction moves c_l and x* while leaving the stagnation-point condition almost unchanged; this is
the lead's picture of a family of slightly non-smooth solutions at P. Consequence: appending the row h(P) - 1 = 0 pins c_l
to 1e-3 only if it is enforced to ~1e-6 (feasible: h(P) is computed to ~1e-8). Part (b), augmented least-squares re-solve with
the row (weight 1, c_l free) at (256,64), R = 3000: h(P) - 1 = +1.85e-4 -> +2.9e-7 in 15 iterations, c_l 5.5786423 -> 5.5780418,
x* 8.60313 -> 8.60151 (candidate 8.60088), equation residual 1.5e-6, identity -8e-8. Smallest singular value: 4.9e-9 without
the row (unchanged at the new state), 1.9e-7 with it (next 3.7e-6, 1.7e-5; smax 2.9e3). The row therefore removes the h(P)
ambiguity and shifts c_l by -6e-4, but a weaker nearly free direction (1.9e-7, 7e-11 relative) remains and the offset to the
candidate's c_l is still +1.7e-3 at this grid. At (192,48), R = 1000 the same row (15 iterations, h(P) - 1 -> 1.6e-5) moves
c_l the other way, 5.5786890 -> 5.5837333, x* 8.60012 -> 8.60688, and lifts the smallest singular value from 1.0e-7 to 6.2e-6.
Conclusion: enforcing h(P) = 1 removes the stagnation-point ambiguity but does not reconcile c_l across grids (5.5780 vs
5.5837 against the candidate's 5.5763); the remaining freedom (the cusp / far-field direction that leaves h(P) unchanged) and
the local resolution at P control c_l at the 1e-3 level. At (320,80), R = 1000 the derivative of h(P) along the near-null mode
is -3.7e-4 per unit c_l (sigma ~ 4.3e-9), confirming the insensitivity with a grid-dependent sign; its row re-solve leaves c_l
unchanged (5.5823307 -> 5.5823371) while driving h(P) - 1 to 5.3e-7. With the row: c_l = 5.5837 (192,48), 5.5780 (256,64),
5.5823 (320,80): the Lemma 3 row does not determine c_l at these grids.

### 3.15 One application of the doubly consistent map Psi (lead request 22:08Z; src/apply_psi.py), from 22:24Z
Psi: choose c_l so that h(P) = 1 for the given density (bracketing + bisection), fix the amplitude by the identity, transport
rho from P along backward characteristics (RK4, dt = 0.005, box delta at P), renormalise a(0) = 1. On the (256,64), R = 3000
LM state (delta = 1e-6): c_l(Psi) = 5.5771531 against the state's identity value 5.5786423 and the candidate's 5.5763219;
x* = 8.60305; the renormalisation factor is 0.99948. Relative defect |Psi(rho) - rho|/rho: 7.0e-5 max (3.0e-5 rms) for r <= 2,
1.2e-3 (2.0e-4) for 2 < r <= 10, 1.4e-3 (6.1e-4) for 10 < r <= 100, 1.4e-3 (6.7e-4) for 100 < r <= R; uniform across
15-degree strips. With delta = 1e-8 every printed digit is unchanged (no box dependence once h(P) = 1 is imposed through c_l).
This is a second determination of c_l (through Lemma 3 instead of the identity) and an independent characteristic-defect
measurement of the reproduced solution. Applied to the lead's own seed (256,96), L = 8, R = 1e4 (the candidate projected onto
my grid): c_l(Psi) = 5.5754204 against the candidate's 5.5763219 (diff -9.0e-4), x*(Psi) = 8.600849 (candidate 8.60088),
renormalisation factor 0.99968; defects 4.1e-5 / 6.7e-4 / 8.5e-4 / 8.2e-4 (max by band), 3.4e-4 .. 8.5e-4 by strip: about
twice more characteristic-consistent than my own LM state. The -9e-4 shift is attributed to my representation of the candidate
on that grid (divided residual 3.8e-3), not to the candidate. On the (320,80), R = 1000 LM state: c_l(Psi) = 5.5813440 against
5.5823307, x* = 8.60818, defects 6.4e-5 / 6.6e-4 / 8.3e-4 / 7.7e-4 by band. Summary: Psi lowers c_l by 0.9e-3 .. 1.5e-3 for all
three inputs and leaves x* within 3e-4; the largest defects are near the x-axis beyond P (theta < 1 degree, r ~ 20) and in the
far field. Split by distance d from P (rms): 6.0e-4, 5.6e-4, 4.0e-4, 2.7e-4, 2.6e-4 for d in [0.03,0.3), [0.3,1), [1,2), [2,4),
>= 4 on the lead's seed (the grid has only 5 .. 164 points in the first three bins); the defect does not vanish away from P,
so it is dominated by this lane's representation (velocity closure and RK4 transport), not by a near-P feature. On the lead's
(256,64), L = 8, R = 7e4 seed (identity offset -1.3e-6) the shift falls to -3.4e-4 (c_l(Psi) = 5.5759850, x* = 8.600863) and
the defects to 3.3e-5 / 4.8e-4 / 6.1e-4 / 5.9e-4 by band: the Psi shift of the candidate decreases with the quality of the
closure, consistent with its attribution to this lane's representation; -3.4e-4 is the present accuracy floor of this
identity-free c_l.

### 3.16 Second solver rebuilt as oversampled least squares (shift 2, from 2026-10-17T23:30Z): method and findings (items 4b-4d supersede the interpretations in items 2-4 where they differ)
Motivation (verifier G16/G24): the square collocation states of 3.12-3.15 satisfy the equation only at the nodes (between nodes
1e-5 .. 4e-3) and their Jacobians are numerically singular (sigma_min 5e-9). New module src/ipm1lsq.py (driver src/run_lsq.py,
tests tests/test_lsq.py, test_cluster.py, test_pmap.py):
- Unknowns: b on the Radau grid rows 1..N (b(0, theta) = 1 fixed); c_l ELIMINATED exactly through the identity,
  c_l = (1 + c[b])/3 with c[b] = psi_xy(0) from the Green function and the tail exponent k = 1/c_l made self-consistent
  (fixed point to 1e-14; implicit-function factor in dc_l/db).
- Rows: the divided equation E (profile equation divided by x^2 y w) on a 2N x (2M+1) quadrature grid (Chebyshev-Gauss radii
  x midpoint angles; 2M+1 because the residual's cos(4M theta) content vanishes on 2M midpoints), each row divided by
  den = |b| + |r b_r + (3 + om) b| + |(U_r/r)(r b_r + (3+om) b)| + |(U_th/r) b_th| + 1e-3 max(den) (the sizes of the terms of E;
  NOT identical to SPEC N4 but a legitimate optimisation weight), and for r < 1 additionally multiplied by (1 + r^2)/(r^2 + 1e-6)
  ("centre weighting": E = O(r^2) for a Cartesian-compatible smooth b, so the objective sees E/r^2, i.e. the D14 relations and
  the compatibility of the centre expansion; without it the LSQ states have b_r(0, theta) = 0.05 and D14 defects 0.09).
- Jacobian exact: the linear map b -> psi mode functions (Lpsi, dense, rebuilt whenever k changes) gives the velocity terms on
  the quadrature grid; local terms by interpolation/differentiation matrices; c_l terms rank one; k-tail dependence by finite
  differences. Checked against finite differences: 5e-9 .. 4e-7 relative per column (tests/test_lsq.py).
- Step: damped Gauss-Newton by QR (one QR of J per iteration, R factor; each damping trial a small stacked QR), never the normal
  equations (the condition number 1e6 .. 1e9 of J would be squared beyond 1/eps and the soft direction lost: astra review
  astra/lsqpin/answer.md). Conditioning from the R factor: the 4-6 smallest singular values and right vectors, and the c_l
  component dc_l/dv_j along each.
- Cost at (256,64): Jacobian 0.8 s, QR step ~5 s, peak GPU memory 2|J| ~ 20 GB. 
- Bugs fixed on the way (astra review, 2026-10-18T00:00Z): (i) the tail integral of the homogeneous extension used the interior
  d_x rho at r = R; the correct source is the exterior derivative k cos(theta) Theta_R - sin(theta) Theta_R' (SPEC N3(a) first
  formula; its "equivalently f_n(R)" clause is wrong unless the data are exactly homogeneous at R). This explained the whole
  Green-vs-quadrature mismatch of c (1.2e-6 relative; -6.4e-6 in c_l at fixed b); all shift-1 results used the interior source
  (effect far below their 1e-3 scatter). (ii) Restarts rebuilt the weight w with gamma = 1/c_l instead of the saved gamma
  (0.27 percent rescaling of the far-field density). Also: Lpsi now rebuilt at every change of k; off-grid derivatives of psi
  in charac.FieldEval now differentiate the interpolant (2e-6 effect in h(P)).
Findings (all at R = 3000, L = 10, (256,64) unless stated; logs runs/lsq_N256M64R3000{,b,c}.log, runs/lsq_N320M80R3000.log):
1. Between nodes the normalised residual is now small EVERYWHERE EXCEPT NEAR P: first run (from the rep LM state, no centre
   weighting): rms 3.7e-7 (r <= 2), 1.1e-6 (10-100), 5.9e-7 (> 100), max 8.7e-5 at (r, theta) = (8.84, 15.8 deg) = (x, y) = (8.5, 2.4)
   directly above P; within |X - P| < 2 the rms is 1.7e-5 in every variant (the lead's near-P band is 1.7e-5 / 3.2e-5).
   Independent check (src/check_fd.py, finite differences at 3000 random points): 3.0e-6 (r<=2), 4.1e-5 (2-10), 6.0e-6, 1.7e-6.
2. c_l IS ONLY WEAKLY CONSTRAINED BY THE DISCRETISED EQUATIONS AT THIS GRID (wording per the referee, see section 4(b)): the Gauss-Newton iteration slides along a flat valley of the
   objective (no centre weighting: 5.5786 -> 5.5934 in 25 its while rms 2.54e-6 -> 2.39e-6; with centre weighting and the fixed
   code: 5.5786 -> 5.505 in 82 its while rms 2.57e-6 -> 2.21e-6, still moving). The softest right singular vectors of the weighted
   Jacobian carry c_l (first run: sigma_min 1.5e-5 vs sigma_max 5.6e3, dc_l/dv = -0.043 per unit norm: a c_l change of 1e-2
   costs a residual change of 3.5e-6 in |F|_2, i.e. 1.4e-8 rms over 65k rows, far below the floor 2.4e-6). The position of the
   discrete minimiser along the valley depends on the row weighting (direction of the drift reverses with the centre weighting),
   so the minimiser's c_l is an artifact at (256,64). This is the quantitative form of the lead's heuristic (analysis 13): the
   condition that pins c_l (smoothness at P, i.e. rho/eta_P constant across characteristic labels) lives in a sliver at P
   (transverse to the slow manifold, width ~1e-3 y^A) that no tensor grid resolves; astra's construction
   delta rho = eps y chi(y/eta) phi(xi/(C y^A)) satisfies all jet conditions at P with divided L2 residual O(eps sqrt(C) eta^((A+1)/2)).
3. Consequences for the team: (a) a second solver cannot confirm c_l by the PDE residual alone at these resolutions; it needs an
   explicit rigidity condition (characteristic matching, src/charrows.py, in progress) or far higher local resolution at P;
   (b) the lead's fast convergence of c_l within one construction family (1.2e-4 spread) is not evidence that the family's c_l is
   right: a different weighting/basis finds other points of the valley with equal residual; (c) the near-P residual band of
   both solvers is the visible footprint of this valley.
4. Pinning rows (2026-10-18T00:20Z-01:05Z). (a) h(P) - 1 as an extra row (src/hrow_lsq.py, exact gradient including the motion
   of P and the tail-exponent dependence; FD check 1e-8): along the cheapest c_l direction dH/dc_l = +1.26e-3 only, so the row pins
   c_l to 1e-4 only when enforced to 1e-7; with weight 1e7 the Gauss-Newton iteration is too badly scaled (PDE residual degraded to
   1e-3 in 40 iterations; runs/hlsq_h256a7.log). (b) Characteristic-matching rows (src/charrows.py, src/charsolve.py; fixed-W rigidity,
   SPEC Lemma 4): C_i = log rho(X_i) - T_i - log y_e,i - log g(P) along backward RK4 characteristics from X_i to |X - P| < 1e-4;
   exact gradients by torch autograd through the integration (motion of the trajectory and of P included; validated: values vs
   the independent charac.eta_P code 9e-12, gradients vs FD 8e-7; batched reverse mode 5x faster than sequential, 5e-13 identical).
   Diagnostic on the LSQ state (c_l 5.5934, h(P)-1 = -4.1e-4; 36 trajectories from r = 20, 60, 200, angles 3..75 deg): C_i =
   -3.6e-3 .. -3.0e-3, i.e. a common offset -3.3e-3 (the (h(P)-1) log(delta) divergence of the transport from P when h != 1, cf.
   verifier G24) plus a spread 6.2e-4 (characteristic defect); dC_i/dc_l along the cheapest c_l direction = 0.017 .. 0.018 for
   every trajectory, |DC|_2 = 0.1075 (36 rows) / 0.061 (12 rows): 33x more c_l-sensitive than all PDE rows together at unit weight.
   With weight 300 (12 rows) the residual-norm cost per unit c_l rises from 3.2e-3 to 18.4, so the pinned LSQ should determine
   c_l to about |F|_2/18 ~ 3e-5 at the residual floor. Solve in progress (runs/charsolve_c256w300.log).
   Also answered the lead's 00:08Z request: the H_xx layer across the characteristic stem above P (peak +0.02 .. +0.036 at x*,
   -0.04 at x - x* = -1, dip near x* - 0.1 at y = 2 .. 2.5) is reproduced on my states (src/hline.py, runs/hline_states.txt).
4b. (01:55Z) NEGATIVE RESULTS with corrected gradients (astra charpin review, all items acted on; conditioning inverse iteration also
   corrected, so the 'softest direction' lists before 01:35Z are void; the cheapest-c_l formula stands). Hard-constraint cheapest
   c_l cost (min |J v| at unit dc_l . v with the rows imposed exactly): PDE rows only 3.243e-3; + 12 characteristic rows (3..75 deg,
   r <= 200) 3.292e-3; + 24 rows incl. 1, 3, 87, 89.5 deg at r = 20, 200, 1000 (dt 0.004, delta 1e-5) 3.433e-3; + 44 axis rows
   (src/axisrows.py: 1-D transport along the y-axis from the origin and along the x-axis from P; the state satisfies them to
   1e-5 / 1e-4) 5.104e-3. None approaches the ~6 needed for c_l to 1e-4. Corrected structure of the soft subspace
   (runs/valley_diag_c256.log): smallest singular values 3.0e-5, 1.5e-4, 1.9e-4, 5.3e-4, 9.9e-4, ... (sigma_max 3.9e8); about 13
   directions cost < 10 per unit c_l; the softest has 91 percent of its energy at 80-90 deg and 83 percent at r > 100, the main
   c_l carrier (1.5e-4) 52 percent at 80-90 deg and 51 percent at r > 100, the third (1.9e-4) 76 percent at 0-10 deg; with rows
   imposed the cheapest direction relocates between the sampled labels. Interpretation: the free quantity is the shape of rho across
   the characteristic stem above P at y ~ 1.5-2.5 (5-10 resolved cells), mapped by transport onto the whole far field; the smooth
   solution fixes it through its Taylor expansion at P, which no trajectory sampling enforces. Also stopped: the unpinned
   resolution/domain queue (an unpinned (256,64) R = 1000 run drifted to c_l 5.292 at rms 2.9e-6).
4c. (02:05Z) FINAL PINNING TESTS, all negative. Hard-constraint cheapest c_l cost at the c_l = 5.5934 state: h(P) - 1 = 0 exact:
   3.267e-3 (PDE only 3.243e-3); 48 Taylor-patch rows at P (src/taylorpatch.py: W jets by polynomial fit, rho_ij by the non-resonant
   recursion from g(P), rows on the circle |X-P| = r_patch): K 8, r 2: 6.1e-3 (W fit truncation 1e-2: the velocity varies on the scale
   x*/A ~ 0.85 near P); K 10, r 1.5: 1.8e-2; h-row + patch: 1.8e-2. Softness vs resolution and domain (src/cost_vs_res.py, construct1
   projection + 6 LSQ iterations): cost per unit c_l 9.9e-4 at (256,64) R 3e3 (floor |F|_2 1.2e-3), 2.9e-4 at (320,80) (floor 4.7e-4),
   1.04e-3 at (256,64) R 1e3 (p 1.5), 1.06e-3 at R 1e4: the valley does not close with resolution or domain. Mechanism (WITHDRAWN 02:21Z, see section 4(c)): the
   frozen-field label-mode picture does not describe the measured direction (its frozen-transport part is large and cancelled by the
   coupled feedback; 77 percent of the cost is away from P). The pinning tests are first-order tests at states where the constraint
   defects are nonzero (section 4(d)).
   Exports for the verifier: runs/fields_lsq_N256M64R3000.npz (c_l 5.5934) and runs/fields_lsq_N256M64R1000p15.npz (c_l 5.2923), two
   states at the same residual level with c_l differing by 0.30 (NOTES_FOR_LEAD 02:02Z).
4d. (03:02Z) FIXED-c_l RESIDUAL CURVE m(s) (the referee's recommended nonlinear diagnostic; src/mc_curve.py, extra row w_c (c_l(b) - s)
   with w_c = 1e4, |c_l - s| < 1e-12). (256,64) clustered at P (4x), R = 3000, 20 Gauss-Newton its per s from the common start
   (construct1 projection + 6 its). s = 5.5563 / 5.5663 / 5.5713 / 5.5763 / 5.5813 / 5.5863 / 5.5963: rms(all) 5.83e-7 / 5.57e-7 /
   5.44e-7 / 5.31e-7 / 5.17e-7 / 5.05e-7 / 4.71e-7 (monotone, 19 percent over the range, minimum beyond 5.5963); max(all) 2.37e-5 /
   2.40e-5 / 2.41e-5 / 2.39e-5 / 2.34e-5 / 2.27e-5 / 2.05e-5 (always next to P; flat); near-P shell rms [0,0.5) 6.1e-6 -> 4.7e-6, [2,4)
   1.5e-6 -> 8.2e-7; h(P)-1 = -2.3e-4 .. -1.7e-4; x* 8.5757 -> 8.6423 (table runs/mc_N256M64cl_table.md). Conclusion: at the near-P
   residual level 2e-5 the fixed-c_l fits are equally good over at least +-0.02 around the candidate; the near-P maximum does not grow
   with the offset. Whether the selection appears once the near-P maximum is 2e-6 (the lead's 302-function basis, NOTES 02:47Z) is
   beyond my grids; the lead's tangent/m(c) test on their bases is the decisive experiment. Extension (runs/mc2_N256M64cl.log):
   s = 5.5163 / 5.5363 / 5.6063 / 5.6263 / 5.6563 / 5.7063: rms 8.16e-7 / 6.80e-7 / 4.50e-7 / 3.53e-7 / 3.53e-7 / 4.09e-7 (L2 minimum near
   5.64, flat to 20 percent over 5.60 .. 5.70), max 2.96e-5 / 3.03e-5 / 1.91e-5 / 1.95e-5 / 1.35e-5 / 8.7e-6 (the near-P maximum keeps
   falling to the largest s), h(P)-1 -2.7e-4 .. -1.9e-5, x* 8.502 .. 8.829. Neither the L2 residual nor the near-P maximum selects the
   candidate's 5.5763 at this grid; both prefer values 0.06 .. 0.13 larger (a property of this discretisation, not of c*). (256,128)
   clustered (runs/mc_N256M128cl.log; 15 its per s): rms 4.83e-7 / 4.57e-7 / 4.34e-7 / 4.08e-7 / 3.89e-7 for s = 5.5563 .. 5.5963 (monotone;
   minimum above 5.60 as well), max 1.5e-5 .. 1.6e-5 flat, h(P)-1 +2e-5 .. +1.4e-4 (opposite sign to (256,64)): the location of the L2
   minimum does not move toward the candidate under 64 -> 128 angles. The lead's remark (03:36Z) applies: with |h(P)-1| ~ 1e-4 (the
   pointwise residual at P, verifier G24) at every s, these fits do not resolve the condition that selects c_l (their refined bases have
   h(P)-1 ~ 1e-8 and a linearised cost per unit c_l of 0.0147 on the 244 basis against my 1e-3 .. 6e-5). Free fit from the fixed-s
   state at 5.5763 (c_l free, same grid): no motion at all (c_l changes by 1.6e-8 in 8 damped Gauss-Newton iterations, steps 1e-9 ..
   1e-15, damping grows and the iteration stops), although the linearised exponent step there is dk* = +0.052 (|s| = 4.8e-4 per unit
   c_l, 18 percent of |F| along s, full Gauss-Newton step |d| = 3.1 in the b-norm): the valley is flat in the objective but a slow
   direction for any damped solver, which stays wherever it is started (runs/lsq_free_from_s5763.log; this also bears on the
   interpretation of c_l stability under refinement in damped or Krylov-truncated fits). (320,80) unclustered two-point check
   (runs/mc_N320M80.log): rms 1.246e-6 at s = 5.5763 and 1.314e-6 at 5.6263 (5 percent higher; max 4.74e-5 vs 4.33e-5; h(P)-1 -7e-5 /
   +1e-4): the slope of m(s) has the opposite sign to the clustered (256,64) grid, so the location of the discrete L2 minimum moves by
   >= 0.05 between grids; only non-discrimination within about +-0.05 at a near-P level of 1e-5 .. 5e-5 is established. Full (320,80)
   curve (runs/mc2_N320M80.log): s = 5.5263 / 5.5563 / 5.5763 / 5.6263 / 5.6763: rms 1.275e-6 / 1.251e-6 / 1.246e-6 / 1.314e-6 / 1.563e-6,
   max 5.4e-5 / 4.8e-5 / 4.7e-5 / 4.3e-5 / 5.8e-5, h(P)-1 -1.4e-4 .. +3.3e-4 (zero crossing between 5.58 and 5.63): this grid's minimum
   is near 5.575 and the clustered (256,64) grid's near 5.64 (h(P) = 1 crossing near 5.72): the discrete minimiser moves by 0.06 .. 0.1
   between grids, so the agreement of one grid's minimum with the candidate carries no weight.
5. Older text: resolution sequence (320,80), (384,96) and domain sequence R = 1e3 .. 3e4 with the map exponent 1.5
   (runs/queue_resdom.sh); the R = 1000 run shows the same valley (c_l 5.5781 -> 5.5495 by iteration 25). Older text follows.
   In progress (older): h(P) - 1 row with exact gradient including the motion of P (src/hrow_lsq.py); characteristic-matching rows
   C_i = log rho(X_i) - T_i - log y_e,i - log g(P) along backward characteristics to a disk of radius 1e-4 around P, with exact
   gradients by autograd through the RK4 integration (src/charrows.py, src/charsolve.py); resolution sequence (320,80), (384,96)
   and domain sequence R = 1e3 .. 3e4 with the map exponent 1.5 (runs/queue_lsq3.sh).

### 3.17 Shift 3 (from 2026-10-18T05:21Z): dk* on finer grids, the lead's domain study run in this lane, and the untried route
1. dk* at s = 5.5763 on finer grids (lead request 04:39Z item 5; src/gn_cl_step.py on the fixed-s states of 3.16 4d; runs/gnstep_s5763_grids*.log).
   dk* = -<F, s>/|s|^2 with s = J v_cl the residual change per unit c_l along the cheapest direction; "fraction" = |s| |dk*| / |F|_2:
   | grid | near-P max | \|s\| per unit c_l | \|F\|_2 | dk* | fraction of F along s |
   |---|---|---|---|---|---|
   | (320,80) unclustered | 4.7e-5 | 2.13e-4 | 3.47e-4 | +0.415 | 26 percent |
   | (256,64) clustered 4x | 2.4e-5 | 4.77e-4 | 1.36e-4 | +0.052 | 18 percent |
   | (256,128) clustered 4x | 1.5e-5 | 2.04e-4 | 1.36e-4 | +0.034 | 5 percent |
   dk* and the systematic fraction of F along the direction both shrink as the near-P residual falls. READING CORRECTED (05:50Z) after the
   external referee's review (astra/plan3/answer.md, item 2, with counterexamples in astra/plan3/PROOF.md): dk* is the Gauss-Newton tangent
   prediction -<F,q>/|q|^2 with q = J v_cl; it is neither a nonlinear minimiser location nor a parameter error estimate, and both implications of
   the lead's 04:39Z item 5 rule ("shrinks => property of the residual level", "stays => competitor") fail on explicit residual families whose
   limits have the opposite root structure; the curvature term <f, f''> omitted by the tangent can dominate when the tangent is soft. The three
   grids are also not a nested refinement with a common limiting reduced objective (|F|_2 is unchanged between the last two while the near-P
   maximum falls). The defensible statement is the referee's: the linearised positive bias and its residual projection diminish across these
   tested discretisations; the nonlinear preferred exponent is discretisation dependent at the attained residual level; these results neither
   establish a competing whole-plane P_2 profile nor exclude one near 5.60 .. 5.64. My earlier sentence "a property of their residual level,
   not a competitor" is withdrawn as too strong. Caution (unchanged): all three
   dk* lie far outside the range where the linear model holds in this discretisation (3.16 4b: at dc = 1e-2 the nonlinear residual change is
   30x the linear one), and the (320,80) value +0.42 is contradicted by that grid's own re-optimised m(s) curve (minimum near 5.575): dk* is a
   sign and an order of magnitude here, the nonlinear m(s) minima (3.16 4d) are the better statement. The full Gauss-Newton step's c_l
   component equals dk* on every grid, as it must when v_cl is the cheapest direction (cusolver gels fails for Jacobians above about 80k x
   25k; the script falls back to the R factor).
2. The lead's domain study (SPEC section 8: three domains) run in this lane with the lead's code. The lead's work/c7/run_dom.sh (prepared
   03:00Z, not launched for lack of CPU slots) was copied verbatim to leadcode/c7 at 05:30Z and run from there (driver leadcode/c7/run_dom_num.sh,
   one domain per invocation, the lead's settings unchanged: start c6d_seg1_shape.npz (375 radial functions, m <= 100), fit rows r < 300 and
   r < 100 shape units, inverse domain R = fit radius / 0.9 with the two-term exterior closure, fit grid 20480 x 480, one 1.8 h LSQR segment
   (inner 2500, check 250), then quick_scan 32768 x 640, export 24576 x 384 at R = 1e4, characteristic defect, jsplit, residual map, B_3;
   the lead's notes scripts are called read-only). Started 05:28Z (r < 300; start norm 1.968e-5 on 4.90M rows x 37882 columns) and 05:30Z
   (r < 100; start norm 1.805e-4: the two-term closure at R = 111 does not match the global fit's far field). Smoke test (1024 x 96, 20 its):
   c_l 5.57636, h(P) = 1 + 5e-9. This is the lead's method on the lead's basis (no independent value as a solver); its purpose is the
   three-domain row of the YES standard, comparable with c6d segment 1 (global fit, rows r < 900, R = 1000) as the third domain.
   RESULTS. Both domains ran 1000 LSQR iterations (one linearization) in the 1.8 h segment. CONVENTION CORRECTION (verifier G64 (b), lead
   07:53Z): the lead's quick_scan.py and export_fit.py close the density at R = 1000 and R = 1e4 shape units for every shape, so for a domain
   fit (R_shape 333 / 111) the scan and export of 07:15-07:18Z describe a field that was not fitted between R_shape and those radii; the
   export-based diagnostics (J, h(P), map, B_3 of the dom*x exports) and the first scan bands are therefore NOT the domains' numbers and are
   not quoted (they are kept in artifacts/data/dom/ as a record: dom100's export J was 2.9e-5, h(P)-1 +6e-6, bands 5.15e-6 / 3.21e-6 / 2.71e-5).
   Fit-convention numbers (my re-scan 07:56Z with the lead's quick_scan_fit.py, 32768 x 640, closure at the stored R_shape; and the verifier's
   independent between-node audit G64 (a), N 22500 q384 with the closure at R_shape L):
   | quantity | c6d_seg1 (R = 1000) | dom300 (rows r < 300, R = 333) | dom100 (rows r < 100, R = 111) |
   |---|---|---|---|
   | objective (that domain's rows) | 1.887e-5 | 1.968e-5 -> 1.5616e-5 | 1.805e-4 -> 1.494e-5 (still falling) |
   | c_l (scan, fit convention) | 5.57636217 | 5.57636282 | 5.57636443 |
   | h(P) - 1 (scan) | -1.3e-8 | -5.4e-9 | -6.0e-9 |
   | flux max 2-10 / N4 | 2.43e-6 / 6.8e-7 | 2.62e-6 / 7.3e-7 | 2.54e-6 / 7.1e-7 |
   | 0.1-2 / 10-100 / 100-1e3 | 2.29e-7 / 7.26e-7 / 2.52e-7 | 2.30e-7 / 6.55e-7 / 1.72e-7 | 2.34e-7 / 7.08e-7 / 2.50e-6 (r > 765 unfitted) |
   | all rms (r <= 1000) | 5.55e-8 | 5.06e-8 | 5.90e-8 |
   | verifier G64: near-P max (strip) r <= Rfit | 2.444e-6 | 2.630e-6 | 2.544e-6 |
   | verifier G64: flux max 10-100 / N_v max r <= Rfit | 8.03e-7 / 6.8e-7 | 6.86e-7 / 1.03e-6 | 7.04e-7 / 7.10e-7 |
   | verifier G64: h(P) - 1 / c_l from h(P) = 1 minus identity | -2.0e-8 / -3.7e-8 | -3.5e-9 / +2.6e-10 | -1.6e-9 / -1.5e-8 |
   | verifier G64: J(0.03) / J(0.01) | 1.48e-6 / 1.46e-6 | 2.00e-6 / 2.12e-6 | 1.76e-6 / 1.84e-6 |
   | verifier G64: B_3 (IBP) | 0.2976 | 0.2969 | 0.2966 |
   Reading (verifier G64, accepted by the lead): c_l moves by +6e-7 (1000 -> 333) and +2.2e-6 (1000 -> 111); h(P) = 1 holds to 5e-8 on all
   three; the near-P maximum is 2.4e-6 .. 2.6e-6 and J 1.5e-6 .. 2.1e-6 on all three; the comparison mixes the domain change with 1000 extra
   iterations, so the drift is not a pure domain effect; it is three orders below the c_l interval of order 1e-3; the far-field truncation
   does not limit the near-P residual at this level. The lead's SPEC requires a factor 10 in R: a third domain dom90 (rows r < 90, R = 100)
   started 07:26Z from dom100_seg1 (two segments; fit-convention post-processing by leadcode/c7/run_dom90_v2.sh), reading rule fixed by the lead
   (07:23Z): "agreeing" if its 2-10 and 10-100 flux maxima are within a factor 1.5 of c6d_seg1's and c_l within 1e-5; "not converged at R = 100"
   if the objective still falls > 5 percent per segment. RESULT (11:03Z; fit convention): segment 1 / segment 2: objective 7.103e-5 -> 1.4451e-5
   -> 1.4114e-5 (-2.3 percent over segment 2); c_l 5.57636672 / 5.57636703 (+4.6e-6 / +4.9e-6 vs c6d); h(P)-1 -5.5e-9 / -2.2e-9; 2-10 flux
   2.75e-6 / 2.63e-6 (1.13x / 1.08x c6d), N4 7.68e-7 / 7.42e-7; 10-100 7.53e-7 / 6.70e-7 (1.04x / 0.92x); 0.1-2 2.09e-7 / 2.20e-7; 100-1e3 (r > 689
   unfitted) 1.72e-5 / 1.92e-5; x* 8.600844; J(0.03) spread with 185 labels 4.01e-6 / 4.19e-6 (8 labels 1.91e-6 / 1.75e-6); B_3 orig median
   0.2985 / 0.2982. By the lead's rule: "agreeing" (1.08x, 0.92x, c_l within 4.9e-6; objective fall 2.3 percent < 5 percent). Exports
   dom90s{1,2}x_fields.npz kept (fit convention, R_inverse 100 shape units).
   FIXED-c_l DOMAIN FIT fxd300 (lead request 08:17Z item 4; the lead's max-norm candidate has c_l fixed at 5.5753626 = 1e-3 below the free fit):
   start = dom300_seg1 shifted along the lead's transplanted 244 soft direction (transplant_fit.py, D = -1.00040e-3; start c_l 5.5753625996),
   long_solve_fixcl.py --fit-radius 300 --fix-cl, 1.8 h (inner 500, check 250): objective 1.6838e-5 -> 1.6446e-5 (four checks, still falling 0.4
   percent per 250 its); fit-convention scan: c_l 5.57536260, h(P)-1 -9.3e-9, 2-10 flux 2.12e-6 (N4 7.21e-7), 0.1-2 2.59e-7, 10-100 7.13e-7, 100-1e3
   1.68e-7, > 1e3 2.57e-7, all rms 4.64e-8; x* 8.600068; J(0.03) spread 2.98e-6 with 185 labels (4.3e-7 with 8); B_3 orig median 0.2972 [0.2922,
   0.3000]. Against the lead's same-c_l fit on the full domain fixc_c6d_m1.0e-03 (375 x m <= 100, R_shape 1000: 2-10 1.89e-6, 10-100 7.52e-7,
   h(P)-1 -1.0e-8): ratios 1.12 and 0.95, h(P)-1 below 1e-7: "agreeing" by the lead's rule. The fixed c_l lowers the strip on the dom300 basis
   by 1.24x (2.62e-6 -> 2.12e-6) as it does on the full domain (1.29x) at m <= 100.
   fxd90 (shift 5, 11:37Z-13:26Z; fit radius 90, R_shape 100, fixed c_l 5.5753626 from dom90_seg2 transplanted at D = -1.00461e-3; 1.8 h,
   inner 500, check 250): objective 1.5422e-5 -> 1.5009e-5; fit-convention scan: c_l 5.57536260, h(P)-1 -5.5e-9, 2-10 flux 2.20e-6 (N4 6.68e-7),
   0.1-2 2.46e-7, 10-100 7.45e-7, 100-1e3 1.15e-5 (r > 90 unfitted), x* 8.600843, J185 3.26e-6, jsplit total 1.00e-6, B_3 orig 0.2965.
   Lead's rule against fixc_c6d_m1.0e-03: 1.16 and 0.99, h(P)-1 below 1e-7: "agreeing". FIXED-c_l DOMAIN SERIES COMPLETE (375 radial
   functions, m <= 100, c_l 5.5753626 on all three): R_shape 1000 / 333 / 100: 2-10 N_f 1.89e-6 / 2.12e-6 / 2.20e-6; 10-100 7.52e-7 / 7.13e-7 /
   7.45e-7; h(P)-1 -1.0e-8 / -9.3e-9 / -5.5e-9; J185 (lead tool, 185 labels; the verifier's 857 set decides) - / 2.98e-6 / 3.26e-6. Together
   with the free series (c6d_seg1 / dom300 / dom100 / dom90: 2.43e-6 / 2.62e-6 / 2.54e-6 / 2.63e-6, c_l within 5e-6) the domain truncation
   changes the near-P and 10-100 maxima by at most 16 percent over a factor 10 in R and leaves c_l (free) within 5e-6 and h(P) = 1 to 1e-8.
   J CAVEAT (lead 10:46Z): the lead's char_defect.py, as called by the domain drivers ("20 8"), uses 8 start labels; the lead withdraws all
   8-label J values from comparisons (J is not resolved in the start angle below about 185 labels; the verifier's dense set decides). The J
   values quoted in this item (dom300 7.8e-7, dom100 export-convention 2.86e-5, dom90 segment 1 1.91e-6) are therefore 8-label steering values
   only; dom90 segment 1 with 185 labels: J(0.03) spread 4.0e-6 (8 labels: 1.9e-6; leadcode/c7/dom90_seg1_cd185.txt); the remaining exports (dom90 segment 2, fxd300) get a
   185-label J after their post-processing (RESUME_HERE).
   The far-field closure error of the INVERSE at these domains (the change of U at interior nodes when the density beyond R_shape L is replaced
   by the two-term tail) is measured separately by the paired-ray check of the fit-convention exports (dom300f / dom100f / dom90; item 7
   continuation).
3. The untried route to pin c_l in this framework (referee astra/softness/answer.md, remedy (iii), documented, not started): transport a
   controlled local approximation of the solution near P (not a truncated Taylor polynomial: the referee notes that finitely many Taylor
   coefficients do not determine the solution at y ~ 2 without a remainder bound, and that the degree-10 patch of 3.16 4c has velocity-fit
   errors 7e-4 .. 3e-3, does not enforce W_1(P) = 0 and skips the compatibility (h - 1) g(P) = 0) along the actual candidate's characteristics
   through the narrow region above P, keeping the transverse structure, and match it to the global field; combined with a characteristic
   coordinate transverse to the slow manifold (remedy (ii)). Estimated at a day of work with error control; the team decided that the lead's
   fixed-c_l fits on their bases are the decisive and cheaper test.
4. Fixed-s convergence table (planned; runs/chain_fixs_table.sh): s = 5.5763 at (192,48), (256,64), (320,80) clustered, R = 3000, and (256,64)
   clustered at R = 1e3, 1e4; to be filled when the GPU slot is free.
5. External referee consultation 'plan3' (astra/plan3/answer.md, PROOF.md, check_tail.py; asked 05:33Z, answered 05:42Z). Besides item 1 above:
   (a) ranking of the remaining computations for the team: (1) angular sampling change on the lead representation with a controlled comparison
   (the lead's c6f, m <= 150, is the resolution comparison; the lead's run_c6f.sh records 92-95 percent of the near-axis residual's angular
   energy at 150 <= n < 210); (2) a nonlinear fixed-c_l curve on the lead basis at small negative offsets (-3e-3, -1e-2) with equal-budget free
   controls, reported as "operational exclusion on that basis and solver", not a continuous bound; (3) an independent source-kernel (paired-ray)
   velocity check on the actual 302/375 candidates at about 40 targets near P and at r = 0.1, 1, 20, 100 (the verifier's method B, code/vquad.py,
   was validated on manufactured data (T3, 7.9e-12) but never run on a candidate); (4) this lane's fixed-s table (at most 2 h; "merely remaining
   at 1e-5 is inconclusive"). Matched transport (item 3 above) should not be started now.
   (b) The referee ran its own asymptotic tail-compatibility check on the saved global trial formulas (astra/plan3/check_tail.py, tail_check.json):
   with rho = r^k A(theta) + r^(2k-1) B(theta) + o(r^(2k-1)) and the leading stream function r^(k+1) P(theta), the first transport correction
   requires (c_l - 1) B = -k P' A + (k+1) P A'. Extracting A, B analytically from the spline endpoint values of c6c_seg1 (302) and c6d_seg1 (375):
   relative mismatch |B - B_req|_inf / |B_req|_inf = 1.33e-4 (302) and 1.61e-4 (375), stable for 2048/4096/8192 angular samples; manufactured
   angular inverse exact to 1.6e-16. Reading (referee's): useful first-correction agreement, not a strong falsification; it did not improve from
   302 to 375; a relative residual decaying like r^(k-1) ~ r^-0.82 can hide a wrong B, so checking only the leading growth exponent is weak; the
   formal effect of replacing the correction outside R = 100 L on the identity-derived c_l is about -1.4e-7, so this mismatch is not evidence
   for a 1e-3 exponent error. (B here is the far-field coefficient, unrelated to the centre coefficient B_3.)
6. Independent real-space velocity check on the lead's candidate (referee item (3)), this lane, from 05:50Z: src/raycheck.py evaluates the lead's
   global trial formula (c6d_seg1_shape.npz; the closed formula re-derived from the stored parameters as in the verifier's code/gen_shape.py) and
   its analytic x-derivative at scattered points, and computes U by the paired-ray formula U(X) = (1/2pi) int_0^pi (-sin phi, cos phi)
   int_0^inf [f(X + s e_phi) - f(X - s e_phi)] ds dphi (gradient of the logarithmic Green function; the pairing makes the s integral absolutely
   convergent for f = O(s^(k-1)), k < 1, and the result is O(|X|^k), hence the canonical sublinear inverse with U(0) = 0) with the formula
   integrated to infinity through a mapped Gauss-Legendre quadrature. No Fourier modes, no Green recursion, no disk truncation, no exterior
   closure: independent of the lead's modal inverse and of the verifier's methods A and B. Targets: nodes of the lead's export c6d_seg1_fields.npz
   (24576 x 384) near P and at r = 0.1, 1, 20, 100, compared with the export's U1, U2 there. Results: item 7.
7. RESULT of the paired-ray check of c6d_seg1 (runs/ray/chain_full.log, runs/ray/c6d_full_A.json; summary by src/ray_table.py; 06:22-06:28Z).
   Validation of the tools first: (i) src/rayshape.py reproduces the export's rho at 4000 random nodes to 1.1e-14 relative and its rho_x to
   4.0e-12 (tests/test_rayshape.py; B-spline basis vs scipy 2e-16 / 9e-13); (ii) the ray quadrature is exact to 3e-16 on rho = (2r^2-4) y e^{-r^2}
   (closed-form U) and to 1.4e-11 .. 7e-14 on rho = x^2 y (1+r^2)^{(k-3)/2} with the candidate's k = 0.17933 (reference: 1D modal Green
   integrals with scipy quad; the paired tail beyond S_max scales as S_max^(k-1) as predicted: 4e-9 at 1e12, 1.4e-11 at 1e15; S_max = 1e18 used).
   (iii) A first run with coarse angular panels (geometric clustering only at the direction to the origin) was off by 0.1 near P: the angular
   integrand I(phi) is smooth but has features of width 0.04 rad for rays nearly parallel to the y-axis from targets near P (the structure of
   f above P), which 16-node panels of width 0.5 rad miss; the symmetric midpoint rule converges at 1024 angles and bounded-width panels
   (phimax 0.02) fix it. The ray quadrature in s uses a marching panelization with step min(0.03 r (one angular wavelength of mode 100 as seen
   from the origin), 2 x the local radial knot spacing (0.016 near P), 0.5 s), 16 Gauss-Legendre nodes per panel, landing exactly on the
   closest approach to the origin and on the y-axis crossing: about 3300 rays x 8300 nodes x 2 points per target, 6 s on the GPU.
   Configuration A (phimax 0.02, amin 1e-4, 16 phi nodes per panel; s-step as above), 51 export nodes of c6d_seg1_fields.npz:
   | region (nodes) | max abs(U_ray - U_lead) | max rel | max residual impact abs(dU . grad rho)/D | lead's abs(R)/D there |
   |---|---|---|---|---|
   | abs(X-P) < 0.5 (19; y = 0.035 .. 0.14, x = x* - 0.3 .. x* + 0.3, P, 0.05 above P) | 8.9e-10 | 2.1e-11 | 1.1e-9 | 6.8e-7 |
   | 0.5 <= abs(X-P) < 2.5 (12; y = 0.5, 1, 2) | 4.3e-8 | 8.8e-10 | 3.0e-9 | 3.2e-7 |
   | r = 0.1 (4 angles) | 7.3e-12 | 5.2e-12 | 2.3e-11 | 1.3e-10 |
   | r = 1 (4) | 6.4e-11 | 4.1e-12 | 2.7e-12 | 8.5e-9 |
   | r = 20 (4) | 5.8e-9 | 6.8e-11 | 3.0e-10 | 1.2e-7 |
   | r = 100 (4) | 1.7e-6 | 4.7e-8 | 5.3e-9 | 9.5e-8 |
   | r = 300 (4) | 4.0e-7 | 5.8e-9 | 2.8e-9 | 1.4e-7 |
   All 51 nodes: max abs(dU) 1.7e-6 (components: largest at (55.5, 83.1); the largest projected impact 5.3e-9 at (19.5, 98.0), next to the
   y-axis), max relative 4.7e-8, max residual impact 5.3e-9 over the 50 nodes with D > 0, median 5.4e-11. The sampled axis node (8.59802, 0)
   is the export node nearest to P, not P itself (x* = 8.600841; the export's W_1 there is -0.0287): U_ray = (-47.974330425, -3.8e-12) against
   the export's (-47.974330426, 0); its normalized impact is undefined (D = 0 on the axis; the unnormalized change is -1.1e-10), not zero as
   the table printed. READING, in the wording the external referee (astra/raycheck/answer.md, 06:44Z) accepted after auditing formula, code
   and test design: at 51 sampled export locations with r <= 300 the paired-ray calculation provides an independent comparison with the
   canonical velocity of the global trial density; on the 50 samples with positive export denominator, configuration A changes the
   normalized transport residual by at most 5.3e-9 when only the velocity is replaced (the referee verified that D is SPEC's N4 denominator
   abs(rho) + abs(X . grad rho) + abs(U . grad rho), so the impact is exactly the normalized change of the signed residual). The referee's own
   CPU modal calculation (Fourier modes of the formula on circles, Green integrals in log r from 1e-9 to 1e30 split at every knot; refinement
   changes its values by 1e-13) at three of the nodes gives U_CPU - U_lead = 4.5e-10 at (8.598, 0.035), 4.1e-9 at (55.5, 83.1), 4.8e-9 at (19.5,
   98.0), and U_CPU - U_ray(A) = 1.9e-11, 1.7e-6, 3.2e-7: the largest configuration-A discrepancies are MY quadrature (configurations B/C
   below), and the exported velocity agrees with the global-density inverse to 5e-9 at those points. The observed differences are below the
   quoted regional residual maxima (6.8e-7 next to P, 1.2e-7 at r = 20, 1e-7 at r = 100-300), though not below the pointwise residual at every
   node (at one r = 0.1 node the impact 2.3e-11 exceeds the stored normalized residual 3.8e-12). These are sampled numerical comparisons,
   not certified or uniform error bounds; they do not validate the full residual, the velocity derivatives, or the verifier's implementation.
   CLOSURE METADATA (referee finding, to be confirmed by the lead): the saved shape specifies R_shape L = 7652.05, but the export grid ends at
   76520.5 and the exported velocities are reproduced (to 3.5e-11 at the two r = 100 nodes) by the two-term closure applied at 76520.5, not at
   7652; consistently, the shape stores c = 15.7290865194 (closure at 7652: the referee's recomputation 15.7290865194) and the export
   c = 15.729086509144 (closure at 76520.5: 15.729086509130; the global formula without closure gives 15.729086509081), with c_l 5.5763621731
   (shape) vs 5.5763621697 (export). So this comparison tests the exported recomputation with inverse domain 76520.5; it does not directly
   validate the closure at 7652 used during the fit (whose effect on c is 1.0e-8, on c_l 3.4e-9). The earlier wording "contributes nothing"
   and "no hidden boundary condition, truncation or gauge term" is withdrawn as too strong; what the analytic formula fixes is the global
   gauge (U = O(abs(X)^k), U(0) = 0), and the numerical comparison is a quantitative consistency check at the sampled points.
   (vi) Stress test of the quadrature on a manufactured field with the referee's recommended difficulties (src/raytest_hard.py, runs/ray/
   hard_test2.log): rho = x^2 y (1+r^2)^((k-3)/2) [1 + 0.1 exp(-((r-8.6)/0.1)^2) cos(100 theta)] (narrow annulus at r = 8.6, angular mode 100 at
   10 percent amplitude), reference by 1D modal Green integrals of the exact source modes n = 2, 4, 96-104. With configuration-A rules the nodes
   near P, at r = 1 and r = 20 are exact (1e-12 .. 1e-16) but the far nodes are not (5.7e-6 at (55.5, 83.1), 6.6e-6 at (19.5, 98.0), 1.4e-4 at
   (58.5, 294.2): from r = 300 the annulus subtends 0.057 rad with 50 periods inside) and a near-origin node was wrong (1.6e-4) until a knot
   look-ahead was added to the marching rule (now 1.7e-10). With angular panels <= 0.005 rad and 24 nodes per panel all nine nodes are exact to
   1.7e-10. The candidate's angular content is far milder (modes 100-150 at 1e-6 of f; modes 10-50 at 0.07-0.45), so the far-node differences
   of configuration A on the candidate (1.7e-6, confirmed as mine by the referee's CPU values) are of this origin and shrink under B/C.
   (vii) Configuration B (all panel widths halved: phimax 0.01, amin 1e-5, 24 phi nodes per panel; s-step min(0.015 r, 1 x knot gap, 0.5 s),
   24 nodes; 9024 rays x 21569 nodes x 2 per target, 2368 s for 51 nodes; runs/ray/c6d_full_B.json): against the export max abs(dU) 8.0e-7
   (at (58.5, 294.2)), max relative 1.2e-8, max impact 5.6e-9, median 3.4e-11; by region: abs(X-P) < 0.5 8.9e-10 (identical to A to all digits
   shown: converged), 0.5-2.5 4.3e-8 (identical to A), r = 0.1 6.5e-12, r = 1 6.2e-11, r = 20 1.0e-9 (A 5.8e-9), r = 100 1.6e-8 (A 1.7e-6; the
   referee's CPU values put the export within 4-5e-9 there, so B is close to converged), r = 300 8.0e-7 (A 4.0e-7: NOT converged at r = 300 in
   either; A and B differ by up to 1.7e-6 there, impact of the difference 5.6e-9). Interpretation of the r = 300 non-convergence: from
   abs(X) = 300 the structure of f near P (scale 0.03-0.1) subtends 1e-4 .. 3e-4 rad while the angular panels there are 0.01-0.02 rad wide
   (the geometric clustering is at the direction to the origin only); the stress test (vi) showed the same symptom. Remedy (added, to be run
   in runs/ray/chain_vary.sh): geometric clustering of the angular panels also at the directions from X to P and to -P. Since the impacts
   at r = 300 are 3e-9 .. 6e-9 against a residual of 1.4e-7 there, the far-field conclusion is unaffected, but the r = 300 row is quoted with
   the A/B spread (4e-7 .. 8e-7) until the P-clustered run is in.
   (viii) Configuration C (midpoint rule in phi with 8192 angles, uniform spacing 3.8e-4 rad; s-step as in A; 8192 rays x 5000-10700 nodes;
   1221 s for 51 nodes; runs/ray/c6d_full_C.json): against the export max abs(dU) 2.9e-7 (at r = 300), max relative 7.3e-9, max impact 3.0e-9,
   median 2.9e-11; by region: abs(X-P) < 0.5 9.0e-10, 0.5-2.5 4.3e-8 (both identical to A and B), r = 0.1 6.8e-12, r = 1 6.3e-11, r = 20 1.0e-9
   (= B), r = 100 4.8e-9 (B 1.6e-8, A 1.7e-6; the referee's CPU inverse put the export at 4.1e-9 / 4.8e-9 from the true value at two of these
   nodes: C is converged there), r = 300 2.9e-7 (A 4.0e-7, B 8.0e-7: my method is not converged at r = 300; the P-clustered variations
   below address it). CONVERGED COMPARISON (A = B = C to the digits shown, hence the ray method's own error is below the quoted values):
   the exported velocity differs from the canonical inverse of the trial density by 9.0e-10 within 0.5 of P (2.1e-11 relative; normalized
   residual impact 1.1e-9 against the residual maximum 6.8e-7 there), by 4.3e-8 within 0.5-2.5 of P (impact 3.0e-9 against 3.2e-7; the
   largest impact of the whole table, at (8.551, 1.994), and the only place where the export's own inverse error is visible above 1e-9), by
   1.0e-9 at r = 20, and by 5e-9 at r = 100 (impact 6e-11); at r = 300 the agreement is 3e-7 .. 8e-7 absolute (impact <= 6e-9 against the
   residual 1.4e-7 there), limited by my quadrature.
   (ix) One-at-a-time parameter variations on six nodes (runs/ray/chain_vary.sh, runs/ray/vary_*.json; nodes (8.598, 0.035), (55.54, 83.12),
   (19.50, 98.05), (58.52, 294.22), (0.0195, 0.098), (8.552, 0.140)). With geometric angular clustering ALSO at the directions from X to P and
   to -P ('pcluster', on top of configuration B's rules): dU = (+4.3e-10, -2.7e-10) at (8.598, 0.035) (identical in every configuration),
   (+2.8e-9, -4.1e-9) at (55.5, 83.1), (+1.0e-9, -4.8e-9) at (19.5, 98.0), (+2.9e-9, -1.4e-8) at (58.5, 294.2), 7e-12 at (0.02, 0.10), 5e-10 at
   (8.55, 0.14); max relative 2.1e-10, max impact 1.1e-9 (the near-P node), median 3.3e-11. The r = 100 values now coincide with the referee's
   CPU inverse (U_CPU - U_lead = 4.1e-9 and 4.8e-9 at these two nodes), and halving the angular panels once more (phimax 0.005 with P clustering,
   783 s) reproduces every number to three digits (max 1.445e-8, impact 1.093e-9), and so does P clustering with the cheap configuration-A
   rules (82 s: max 1.445e-8, impact 1.091e-9), and the midpoint rule with 16384 angles (uniform spacing 1.9e-4 rad, no clustering at all:
   max 1.35e-8, impact 1.07e-9) agrees with them, so the r = 300 difference of 1.4e-8 is a converged value there
   (A/B/C gave 4e-7 / 8e-7 / 3e-7: the structure near P subtends 1e-4 rad from r = 300 and must be clustered). Full table of the
   17 variations (runs/ray/vary_table.txt; abs(U_ray - U_export), Euclidean, per node; chain finished 08:23Z):
   | variation | (8.598,0.035) | (55.5,83.1) | (19.5,98.0) | (58.5,294.2) | (0.0195,0.098) | (8.552,0.140) | max impact |
   |---|---|---|---|---|---|---|---|
   | base (A rules) | 5.1e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 7.0e-12 | 6.8e-10 | 5.3e-9 |
   | fine (B rules) | 5.1e-10 | 9.3e-9 | 1.7e-8 | 8.1e-7 | 8.7e-12 | 6.7e-10 | 5.6e-9 |
   | fine + P clustering | 5.1e-10 | 5.0e-9 | 4.9e-9 | 1.5e-8 | 8.7e-12 | 6.7e-10 | 1.1e-9 |
   | fine + P clustering, phimax 0.005 | 5.1e-10 | 4.9e-9 | 4.9e-9 | 1.5e-8 | 8.6e-12 | 6.7e-10 | 1.1e-9 |
   | base + P clustering | 5.1e-10 | 5.8e-9 | 5.1e-9 | 1.5e-8 | 7.2e-12 | 6.8e-10 | 1.1e-9 |
   | base, phimax 0.01 | 5.1e-10 | 1.0e-7 | 1.6e-7 | 1.8e-8 | 8.1e-12 | 6.7e-10 | 2.9e-9 |
   | base, 24 phi nodes per panel | 5.2e-10 | 7.8e-8 | 1.7e-7 | 1.8e-8 | 8.7e-12 | 6.9e-10 | 3.0e-9 |
   | base, amin 1e-5 | 5.1e-10 | 1.5e-7 | 3.7e-7 | 3.4e-6 | 7.0e-12 | 6.8e-10 | 2.4e-8 |
   | midpoint 8192 angles | 5.2e-10 | 2.8e-9 | 4.5e-9 | 8.9e-8 | 8.4e-12 | 6.7e-10 | 1.1e-9 |
   | midpoint 16384 angles | 5.2e-10 | 4.9e-9 | 4.9e-9 | 1.4e-8 | 7.7e-12 | 6.8e-10 | 1.1e-9 |
   | base, ang 0.015 (s-step) | 5.1e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 8.2e-12 | 6.7e-10 | 5.3e-9 |
   | base, kfac 1 (s-step) | 5.1e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 8.8e-12 | 6.7e-10 | 5.3e-9 |
   | base, 24 s nodes per panel | 5.1e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 8.9e-12 | 6.8e-10 | 5.3e-9 |
   | base, ratio 1.25 | 5.1e-10 | 1.3e-7 | 4.2e-7 | 1.5e-6 | 9.4e-12 | 6.7e-10 | 1.0e-8 |
   | base, look-ahead off | 5.1e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 8.2e-12 | 6.8e-10 | 5.3e-9 |
   | base, S_max 1e15 | 5.5e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 6.9e-12 | 7.0e-10 | 5.3e-9 |
   | base, S_max 1e21 | 5.0e-10 | 1.9e-6 | 3.7e-7 | 4.1e-7 | 7.0e-12 | 6.7e-10 | 5.3e-9 |
   Reading: every variation of the RAY (s) quadrature (ang, kfac, ngl, look-ahead, S_max) leaves all six nodes unchanged to the digits shown
   (S_max 1e15 vs 1e21 moves the near-P node by 5e-11, the predicted paired-tail size), so the ray integration is converged; the differences
   between variations come from the ANGULAR rule alone, and only at the three far nodes: angular refinements without clustering at the P
   directions scatter there between 1e-8 and 3e-6 (the geometric-cluster variants 'ratio 1.25' and 'amin 1e-5' move the panel boundaries and
   are not nested, so they are not monotone), while the three rules that resolve the P directions (geometric P clustering at two widths,
   midpoint 16384) agree with each other to 1e-9 at r = 100 and at r = 300, and with the referee's CPU values at r = 100. The near-P nodes and
   the near-origin node are identical in all 17 variations (5.1e-10, 6.8e-10, 7e-12 .. 9e-12). The far-node rerun with P clustering on all
   eight r = 100 / 300 nodes (runs/ray/c6d_far_BP.json, B rules + P clustering, 580 s): abs(dU) = 4.9e-9 .. 5.0e-9 at the four r = 100
   nodes and 1.5e-8 (1.46e-8 .. 1.48e-8) at all four r = 300 nodes (max relative 1.1e-9, max impact 6.4e-11): r = 300 is converged at 1.5e-8 for
   all four nodes (the (166.7, 249.4) node, 3.4e-7 in configuration C, is 1.5e-8 here).
   FINAL INVERSE-ERROR STATEMENT (posted to the lead 07:54Z): at 51 export nodes of c6d_seg1 the exported velocity differs from the
   canonical inverse of the trial density (paired-ray quadrature of the analytic source, converged across three angular rules and two ray
   rules, confirmed by the referee's independent CPU modal inverse at three nodes) by 9e-10 within 0.5 of P (2e-11 relative), 4.3e-8 within
   0.5-2.5 of P, 1.0e-9 at r = 20, 5e-9 at all four r = 100 nodes and 1.5e-8 at all four r = 300 nodes (P-clustered rerun, item (ix)); the implied change of the normalized transport residual is at most
   3.0e-9 (at (8.551, 1.994); median 3e-11) over the 50 nodes with D > 0, against residual maxima of 6.8e-7 next to P and 1e-7 .. 1.4e-7 at
   r = 20 .. 300. These are sampled comparisons of the exported recomputation (inverse domain 76520.5 with the two-term closure at its edge),
   not uniform bounds, and they do not validate derivatives of rho or the verifier's implementation.
   (x) Far-field truncation (closure) effect of the FIT's inverse, measured with the same tool on the fit-convention exports of the domain
   fits (export_fit_fit.py: inverse on r <= R_shape L with the two-term closure there, i.e. the velocity the fit actually used): U_export -
   U_ray(formula to infinity) at the 51 interior nodes is the change of U caused by replacing the density beyond R_shape L by the closure.
   dom300f (R_shape 333 = 2551 physical; runs/ray/dom300f_BP.json, baseP rules, 738 s): abs(dU) 1.4e-6 within 2.5 of P (3.0e-8 relative;
   normalized impact <= 2.7e-8 against the fit's residual 7e-7 there), 1.5e-8 at r = 0.1, 1.5e-7 at r = 1, 3.1e-6 at r = 20 (impact 2.0e-7
   against the fit's 1.8e-7), 1.5e-5 at r = 100 (impact 2.0e-7 against 1.3e-7), 4.7e-5 at r = 300 (3.5e-6 relative; impact 2.0e-7 against
   5.8e-8). So at R_shape = 333 the closure changes the velocity the fit sees by 2e-7 in normalized-residual terms for 20 <= r <= 300 (at or
   above the fit's own residual there) and by 3 percent of the residual next to P.
   dom100f (R_shape 111 = 850 physical; runs/ray/dom100f_BP.json, 734 s): abs(dU) 4.2e-5 within 2.5 of P (9.1e-7 relative; impact 6.8e-7 within 0.5
   of P and 8.1e-7 at 0.5-2.5, against the fit's own residual 6.7e-7 / 3.2e-7 there), 4.7e-7 at r = 0.1 (impact 2.4e-7), 4.7e-6 at r = 1
   (2.5e-7), 9.3e-5 at r = 20 (impact 6.1e-6 against 1.8e-7), 4.7e-4 at r = 100 (6.2e-6 against 1.3e-7), 1.5e-3 at r = 300 (1.1e-4 relative;
   7.0e-6 against 4.6e-8); median impact 6.2e-7. So at R_shape = 111 the velocity the fit used differs from the true inverse of its own density
   by as much as the fit's interior residual next to P and by 30-150 times that residual for 20 <= r <= 300: the R = 111 fit is a bounded-domain
   fit whose far-field truncation error is at the level of its interior residual (its small scanned residual is a property of the closed
   problem, not of the plane problem). SCALING: from R_shape 333 to 111 (factor 3) the impact grows by 30 (near P: 2.7e-8 -> 8.1e-7) to 35
   (r = 20-300: 2.0e-7 -> 6-7e-6), i.e. like R^-3 within the measurement; extrapolated to the candidate's fit at R_shape = 1000 (7652 physical)
   this predicts an impact of about 1e-9 next to P and 7e-9 at r = 20-300, measured directly next.
   c6dfit = THE CANDIDATE c6d_seg1 re-exported in its own fit convention (export_fit_fit.py: closure at R_shape = 1000 = 7652 physical;
   runs/ray/c6dfit_BP.json, 728 s): abs(dU) 9.2e-8 within 2.5 of P (2.0e-9 relative; impact 2.3e-9 within 0.5 of P and 3.1e-9 at 0.5-2.5,
   against the residual 6.8e-7 / 3.1e-7: 0.4-1 percent), 1.0e-9 at r = 0.1, 1.0e-8 at r = 1, 2.0e-7 at r = 20 (impact 1.3e-8 against 1.1e-7),
   1.0e-6 at r = 100 (1.3e-8 against 9.3e-8), 3.0e-6 at r = 300 (2.3e-7 relative; 1.3e-8 against 1.5e-7); median impact 1.3e-9. So for the
   candidate's fit the far-field closure at 7652 changes the velocity it used by 0.4-1 percent of the residual next to P and by about 10
   percent of the residual at 20 <= r <= 300; the measured scaling over the three R_shape values (111 / 333 / 1000: impact next to P
   8.1e-7 / 2.7e-8 / 2.6e-9, at r = 20-300 6-7e-6 / 2.0e-7 / 1.3e-8) is between R^-2 and R^-3. FAR-FIELD TRUNCATION STATEMENT: the
   nonlocal inverse's truncation error at the candidate's domain is at most 3e-9 (next to P) and 1.3e-8 (r <= 300) in normalized-residual
   terms, against a residual of 2.4e-6 (strip) and 1e-7 .. 1.5e-7 (10-300); at the smaller domains it grows like R^-2 .. R^-3 and at
   R_shape = 111 it equals the fit's interior residual. Fourth point, dom90s1 (R_shape 100 = 765 physical; runs/ray/dom90s1_BP.json; P-clustered rules; the configuration-A rules give the same numbers): abs(dU) / impact (fit's residual): within 0.5 of P 5.4e-04 / 8.6e-06 (7.1e-07); 0.5-2.5 5.5e-04 / 1.0e-05 (3.2e-07); r = 0.1 6.1e-06 / 3.1e-06 (1.1e-10); r = 1 6.1e-05 / 3.2e-06 (7.8e-09); r = 20 1.2e-03 / 7.8e-05 (1.1e-07); r = 100 6.1e-03 / 8.0e-05 (9.8e-08); r = 300 2.0e-02 / 9.6e-05 (5.1e-08); median impact 7.9e-06. At R_shape = 100 the exterior continuation dominates the
   velocity the fit used everywhere outside the near-origin region (12-30x the interior residual next to P; the r = 300 nodes lie at 0.4 of the
   closure radius). CAVEAT for the 100 and 111 rows: U_ray integrates the saved formula to infinity, and for a bounded-domain fit the formula
   beyond the fit radius is unfitted (dom90 started from dom100 and ran 1000 more iterations with rows r < 90 only, so its exterior formula
   drifted further than dom100's, which started from the global fit); the jump 8.1e-7 -> 8.6e-6 next to P from R_shape 111 to 100 is mostly
   that drift, not the closure radius. So: the velocity of a bounded-domain fit at interior nodes depends on what is assumed beyond R_shape L
   by 3e-9 (R_shape 1000, formula fitted out to 7652: a genuine closure error), 3e-8 (333) and 1e-6 .. 1e-5 (100-111) in normalized-residual
   terms next to P; the small interior residual of a fit at R_shape <= 111 is a property of the closed problem.
   dom90 SEGMENT 2 (shift 5, 13:26Z-13:44Z, runs/ray/dom90s2_BP.json, baseP rules; fit-convention export, R_shape 100): |U_export - U_ray(formula
   to infinity)| 1.16e-3 next to P (relative 2.5e-5; normalized residual impact 1.86e-5 within 0.5 of P, 2.23e-5 at 0.5-2.5), 6.6e-6 / 6.8e-6 at
   r = 0.1 / 1, 1.7e-4 at r = 20 and 100, 1.8e-4 at r = 300 (all inside the physical fit radius 90 L = 689); median impact 1.7e-5. Segment 1 gave 8.6e-6 next to P
   (same R_shape; the two segments differ in their coefficients, so the closure effect of the fit's inverse at R = 100 is 1-2e-5 in
   normalized-residual terms next to P, against the fit's own near-P maximum 2.6e-6): at R_shape 100 the closure error of the inverse exceeds
   the fit's residual by an order of magnitude (the controlled same-density numbers at 333 and 111 are in (xi)).
   (xi) SAME-DENSITY closure test (the referee's controlled version of (x); runs/ray/c6d_R333_BP.json 14:02Z, c6d_R111_BP.json 14:20Z): the
   c6d_seg1 density is unchanged (the three shape files differ only in R_shape, checked by the referee) and only the closure radius of the
   fit-convention inverse is set to R_shape 1000/3 and 1000/9 (written 333 and 111 below); the exported velocity is compared with the
   paired-ray inverse of the same formula (quadrature truncated at S_max = 1e18; the paired tail beyond scales as S_max^(k-1)) at 51
   separately selected export locations per run (nearby but not identical, e.g. (8.3011, 0.033957) / (8.2998, 0.033951) / (8.3008, 0.033955);
   50 with positive denominator D_v), so the difference is E_R = T(C_R rho) - T rho for one fixed density, sampled; the "impact" is
   |dU . grad rho| / D_v with the exported gradient and denominator frozen (D_v = |rho| + |X . grad rho| + |U . grad rho|), i.e. the change of
   the signed normalized residual when only the velocity is replaced. R_shape 1000 (c6dfit_BP) / 333: |dU| next to P 9.2e-8 / 1.25e-6, normalized
   impact within 0.5 of P 2.33e-9 / 2.00e-8 (0.5-2.5: 3.1e-9 / 2.4e-8), r = 0.1: 5.2e-10 / 7.1e-9, r = 1: 5.4e-10 / 7.3e-9, r = 20: 1.33e-8 /
   1.81e-7, r = 100: 1.33e-8 / 1.80e-7, r = 300: 1.34e-8 / 1.77e-7; median 1.3e-9 / 1.8e-8. Ratios 333 -> 1000: 8.6 next to P, 13.6 at
   r = 20-300, against the referee's conditional leading-strain exponent R^(3k-3) = 3^2.462 = 14.9 (k = 0.1793; the same exponent applies
   to the normalized impact at a fixed point when the leading projected coefficient is nonzero, referee astra/sec318audit PROOF.md).
   Significance of the R_shape 1000 closure (the convention of every lead fit) for this density: ratio of the impact maximum to the sampled
   residual maximum of the same normalization in the same region: 0.34 percent (|X - P| < 0.5), 1.0 percent (0.5-2.5), 12 percent (r 20),
   14 percent (r 100), 9 percent (r 300); at the r = 0.1 samples the impact (5e-10) is 4x the tiny sampled residual there (1.3e-10).
   R_shape 111 (14:20Z, runs/ray/c6d_R111_BP.json): impact within 0.5 of P 3.50e-7 (0.5-2.5: 4.2e-7), r = 0.1 / 1: 1.25e-7 / 1.28e-7, r = 20 /
   100 / 300: 3.17e-6 / 3.09e-6 / 2.54e-6; median 3.2e-7. Three-point series (impact; 1000 / 333 / 111): next to P 2.33e-9 / 2.00e-8 /
   3.50e-7; r = 0.1 5.2e-10 / 7.1e-9 / 1.25e-7; r = 20 1.33e-8 / 1.81e-7 / 3.17e-6. Local exponents -d log E / d log R: 1000 -> 333: 1.96
   (P), 2.38 (r 0.1), 2.37 (r 20); 333 -> 111: 2.60 (P), 2.61 (r 0.1), 2.61 (r 20); referee's asymptotic prediction 3 - 3k = 2.46. The
   measured secant exponents (log(I_b/I_a)/log(R_a/R_b) between sampled radii; 1.96 / 2.61 next to P, 2.38 / 2.61 at r 20) range from 1.96 to
   2.61: broadly compatible with the conditional leading-strain exponent 2.462, but three sampled comparisons do not establish the asymptotic
   regime (referee). Consequence for the domain study: at R_shape 111 and 100 the closure error (3.5e-7 on the same density, 0.9-1.9e-5 on
   the refitted dom90 densities, next to P) is of the order of or above the fits' near-P residuals, so the dom100 / dom90 rows show the
   stability of the interior residual maxima under a specified alternative exterior continuation (the two-term closure at that radius),
   not a clean full-plane domain limit; at 333 the closure impact next to P is 2.85 percent of the sampled near-P residual maximum and at
   1000 0.34 percent. The tested closed fitting problems have relatively stable interior residual maxima (within 16 percent over 1000 /
   333 / 100); this does not identify what limits them (the domain rows are at m <= 100 while the candidate has m <= 150, verifier G72).
   REFEREE AUDIT of (x) (astra/farfield/answer.md, PROOF.md, 09:50Z) and corrections: (1) the quantity is T(C_R rho) - T rho for the SAVED
   formula (C_R = two-term continuation at R): a well-defined closure bias for c6d_seg1 read as the full-plane candidate; for ALL bounded-domain
   fits (333 as well as 111 and 100) it is a sensitivity to two exterior continuations, since their exterior formula is unfitted (the 333 row
   carries the same caveat; initialization from the global fit does not establish the exterior after refitting). (2) My near-P numbers for
   333 and 111 were the 0.5-2.5 ANNULUS maxima; the inner (abs(X-P) < 0.5) maxima recomputed from the JSON are 2.33e-9 (1000), 2.23e-8 (333),
   6.77e-7 (111), 8.62e-6 (100); the c6d_seg1 annulus value is 3.10e-9 and its largest outer impact 1.338e-8; relative to the sampled regional
   residual maxima these are 0.34 percent (near P) and 11.6 / 14.2 / 9.0 percent at r = 20 / 100 / 300: ratios of regional maxima, not pointwise
   percentages (some individual node ratios exceed 100 percent). (3) Scaling: for rho = r^k A + r^(2k-1) B + r^(3k-2) C + ..., the two-term
   closure reproduces A and B exactly and its error on the C term gives a harmonic strain inside the matching circle, delta c =
   -C_3/(3(1-k)) R_c^(3k-3): exponent 3k-3 = -2.462, amplification 15.0 from 1000 to 333, against the measured 10.4 (near P) and 15.4 (outer):
   compatible, but different fitted formulas are not a convergence-rate experiment, and the closure discrepancy says nothing about whether
   B satisfies the transport equation (an exactly two-term exterior has zero closure discrepancy for every B; the plan3 mismatch 1.3e-4 ..
   1.6e-4 stands as a separate diagnostic). (4) Statement adopted (referee's wording): "For c6d_seg1, comparing the fit-convention velocity
   (two-term closure at R_c = 1000 L) against the canonical velocity of the saved global formula gives sampled residual impacts of about
   2.3e-9 within 0.5 of P and up to 1.3e-8 at the sampled radii 20, 100 and 300, i.e. about 0.3 percent and 9-14 percent of the respective
   sampled residual maxima." Qualifications: empirical sample maxima at 50 nodes with D > 0, not uniform or certified bounds; "impact" holds
   rho, c_l and D fixed (recomputing D or enforcing the centre identity through c_l changes the comparison); it does not exclude other
   far-field defects or establish what limits further optimization. My earlier phrase "the far field is not what limits the candidate's
   residual" is withdrawn as too strong. (5) On the domain study: the series supports stability of c_l and of the interior residual
   magnitudes within the tested family of closed fitting problems; it does not establish full-plane domain independence (re-optimization can
   compensate exterior-induced strain; similar residual maxima need not mean similar fields); the proper test is (i) inverse/closure
   convergence on the same density, then (ii) refits on common regions with controlled exteriors and an independent canonical inverse,
   varying fit radius and matching radius separately. These are measured at 51 nodes with r <= 300 on the saved formula; they say nothing
   about r > R_shape L, where the closure replaces the fit. The referee (astra/raycheck) also notes that the paired-ray absolute convergence needs
   abs(grad f) = O(abs(Y)^(k-2)) (true for the trial formula, not implied
   by the growth bound alone: rho = r^(k-1) cos^2 theta sin theta sin r is a counterexample), and that S_max = 1e18 is a truncation with tail
   bound C abs(X) S^(k-1)/(1-k), not an integration to infinity.
   (xii) The lead's max-norm CANDIDATE fixc_c6f_m1.0e-03 (c6f basis 375 x m <= 150, c_l FIXED at 5.5753626 = 1e-3 below the free fit; lead
   08:17Z; export 24576 x 576 written by the lead's postx step, inverse domain per their export_fit.py) checked with the same method at 52
   export nodes (lead request 09:30Z item 4; runs/ray/cand_fixc_c6f_m1e-3_BP.json, baseP rules, 1054 s): abs(U_ray - U_export) 8.4e-10 within 0.5
   of P (1.9e-11 relative; impact 6.3e-10 against the candidate's sampled residual 1.5e-7 there), 4.0e-8 at 0.5-2.5 (impact 2.8e-9 at (8.550,
   1.994) against 6.4e-8), 6e-12 at r = 0.1, 5e-11 at r = 1, 1.0e-9 at r = 20, 4.6e-9 at r = 100, 1.4e-8 at r = 300 (impacts 6e-11); max impact
   2.8e-9, median 2.8e-11. Same pattern and level as for c6d_seg1: the exported velocity of the candidate agrees with the canonical inverse of
   its saved density to 1e-9 .. 1e-8, and the implied change of its normalized residual (at most 2.8e-9, about 2-4 percent of its sampled
   near-P residual maxima, which are 4x lower than c6d's) does not affect the comparison between the fixed-c_l and the free fits. Sampled,
   not uniform; the candidate's own x* is 8.600069 (c6d: 8.600841).
   (xiii) The TEAM CANDIDATE X3 = c6g (375 x m <= 200, c_l fixed 5.5753626, 20750 GPU LSQR its after s2g; md5 15f8095f7e79dbfa0c50d75e5fe8997a;
   lead section 4 v5 "[TBD: repeat on X3]", lead request 17:37:53Z item 3) checked with the same method at 52 export nodes (shift 6, 2026-10-18T17:30Z
   to 18:03Z; runs/ray/x3_c6g_BP.json, table runs/ray/x3_c6g_table.txt; baseP rules: Smax 1e18, adapt, phimax 0.02, P clustering; 1939 s on the
   GPU against 1054 s for the X1 check; the shape evaluation at m <= 200 is the main difference). Export made in this lane with the lead's export_fit.py at 24576 x 576
   (inverse domain 1e4 shape units = 76514 physical, two-term closure there, the same convention as the lead's X1 export of (xii); the export
   took 80 s and was deleted after the check, its diagnostic JSON kept as artifacts/data/ray/x3_c6g_export_diagnostic.json; export axis x*
   8.600064, identity c_l of the export 5.5753626072). abs(U_ray - U_export): 1.0e-9 within 0.5 of P (2.2e-11 relative; impact 8.6e-10 against
   the candidate's sampled residual 1.85e-7 there), 3.6e-8 at 0.5-2.5 from P (impact 2.6e-9 at (8.550, 1.994) against 5.5e-8), 7.7e-12 at
   r = 0.1, 5.1e-11 at r = 1, 9.8e-10 at r = 20, 4.9e-9 at r = 100, 1.5e-8 at r = 300 (impacts 1.3e-11, 1.6e-12, 7.0e-11, 6.8e-11, 6.8e-11);
   max impact 2.6e-9 (over the 51 targets with D_v > 0; the axis target has D_v = 0 and is excluded from the ratios), median 2.8e-11. Conventions
   (referee audit astra/shift6audit): "max |dU|" is the maximum componentwise difference (Euclidean 3.64e-8 over all targets), the relative column
   uses Euclidean norms, and the impact |dU . grad rho| / D_v freezes the exported gradient and the exported denominator D_v = |rho| + |X . grad
   rho| + |U . grad rho|; it is not a change of N_f and not a recomputed N_v. Same pattern and level as X1 ((xii): 8.4e-10 / 4.0e-8 / 6e-12 /
   5e-11 / 1.0e-9 / 4.6e-9 / 1.4e-8; max impact 2.8e-9) and c6d_seg1: the exported velocity of the candidate agrees with the canonical sublinear
   inverse of its saved density, computed by an unrelated method, with a maximum componentwise discrepancy of 3.6e-8 (annulus 0.5-2.5 from P) and
   the regional values above; the implied residual impact is 0.47 percent of the sampled |R|/D_v within 0.5 of P (8.6e-10 against 1.85e-7) and
   4.7 percent at 0.5-2.5 from P (2.6e-9 against 5.5e-8), same region and same normalization in each ratio. Sampled comparisons at 52 nodes, not
   uniform bounds, and not a bound on every selection diagnostic; the exterior of the export (r > 1e4 shape units) is the two-term extension, the
   ray integral uses the saved formula continued globally, truncated at S = 1e18; the export's identity c_l 5.5753626072 differs from the stored
   fixed value 5.5753626106 by 3.4e-9 (the export's velocity is the identity-convention one). The same check in the FIT convention (closure at R_shape 1000, export_fit_fit.py) is
   queued (runs/ray/chain_x3b.sh -> x3_c6g_fit_BP.json): it measures the closure effect of the fit's own inverse on the candidate itself.
   (xiv) Exterior sensitivity of the 90 L domain fit at the candidate's basis, dom90g (chain step 33: c6g end continued 20750 its at the fixed c_l
   with fit rows r < 90 L and the inverse domain / two-term closure at R_shape = 100 L; md5 7f989938b5e9a6434fe4e7bd195647b4), measured as in (x):
   export in the FIT convention (lead's export_fit_fit.py, 24576 x 576, closure at R_c = 100 L; 80 s; deleted after) and the paired-ray velocity of
   the saved formula continued globally (quadrature truncated at S = 1e18) at the same 52 nodes (runs/ray/dom90g_BP.json, table dom90g_table.txt;
   18:04Z-18:36Z, 1907 s). The two densities coincide up to the matching radius 100 L and differ beyond it, so the measured quantity is T(C_100L rho)
   - T rho at the nodes (plus quadrature error). Componentwise max |U_export - U_ray|: 4.2e-4 within 0.5 of P (8.9e-6 relative; impact |dU . grad
   rho| / D_v 6.6e-6 against the closure-convention sampled |R|/D_v 6.4e-8 at those nodes, ratio 104), 4.2e-4 at 0.5-2.5 from P (impact 8.0e-6
   against 3.7e-8, ratio 218), 4.6e-6 / 4.6e-5 at r = 0.1 / 1 (impacts 2.4e-6), 9.3e-4 / 4.6e-3 / 1.4e-2 at r = 20 / 100 / 300 (relative 4e-5 /
   4e-4 / 1.5e-3; impacts 6.5e-5 / 6.4e-5 / 6.3e-5 against sampled residuals of 6e-10 .. 2e-9 there); max impact 6.5e-5 at (19.8, 2.6), median
   6.1e-6 (regional sample maxima; frozen exported gradient and D_v). Reading: the velocity a 90 L fit uses at interior points depends on what is
   assumed beyond its matching radius by 7e-6 (near P) to 6.5e-5 (r 20-300) in these normalized terms, about 100 times its sampled closure-
   convention residual near P and roughly 30-300 times its largest interior N_v (2e-7 on the verifier's grid); so, as for the m <= 100 series ((x):
   dom90 segment 2 gave 1.9e-5 / 2.2e-5 / 6.6e-6 / 1.7-1.8e-4 in the same regions, 2.8x larger than here), the 90 L column is a stability
   observation within the closed fitting problem, not the residual of the saved globally continued formula under its canonical inverse. Consistent
   in order of magnitude with the lead's scans (NOTES_FOR_TEAM 17:20:44Z: near-P N_f 2.9e-5 with the formula continued to 1000 L against 1.9e-7 with
   the closure, maxima over a 32768 x 640 grid) and the verifier's (G86 addendum: N_v grid maxima within 0.5 of P 9.4e-6 formula-continued against
   6.0e-8 with the closure, ratio 156; 7.4e-5 on 10 <= r <= 100): different quantities (grid maxima of N_f or N_v in two conventions against
   frozen-denominator impacts at 20 nodes), agreeing in order of magnitude, not in value. For comparison, the same measurement on the fixed older
   density c6d_seg1 gave 2.3e-9 within 0.5 of P and 3.1e-9 in the annulus for the closure at 1000 L, and 2.2e-8 within 0.5 of P for the same
   density closed at 333 L ((x)-(xi)); X3's own fit-closure check (closure at 1000 L) is in (xvi).
   (xv) Where the far-field band sits in the trial family (shift 6, 17:3xZ; facts from the candidate's shape file c6g_shape.npz, checked independently by
   the referee astra/farrow, the lead (NOTES_FOR_TEAM 17:42Z item 3) and the verifier (G79)): the radial basis is a degree-7 spline in q = 1 - (1 + u^2)^(-(1-k)/2)
   (u = r/L) with 370 distinct knots; the LAST INTERIOR KNOT is q = 0.99330 = u 446 (the previous ones u 192, 117, 83), so for u > 446 each b_m is one
   polynomial of degree 7 in q; the fit rows end at u = 0.9 R_shape = 900 (q = 0.99624; NOT at 1000 L: the lead's text had called 1000 <= r <= 1000 L
   "the fit domain" and corrected it to "inverse domain"), which is 44 percent of the last knot interval in q; the far-field N_v maximum of c6g
   (1.102e-6 / 1.094e-6 at r 3.7e4 physical = u 4858, q 0.99906, 86 percent of the interval, next to the y-axis; verifier G80; the other fits read
   1.08-1.17e-6 there except F1 1.46-1.47e-6 and W1 1.28-1.31e-6 (G76), fxd1g 1.33e-6 at u 3300 (G89)) lies in the uncollocated continuation of that
   polynomial, and the far-field model's Theta_0, Theta_1 are end-point data of the complete trial formula (the b_m(1), b_m'(1) together with the
   fractional term's T(1), T'(1)), not the spline end values alone. Referee's reading,
   adopted (my first wording "the damping regularises the extrapolation" was unproved and is withdrawn): the far maximum lies in an uncollocated
   continuation of the last spline piece and may reflect weakly constrained exterior coefficients; its persistence under the existing fits does not
   establish an intrinsic floor of the family; it remains an out-of-sample defect of the actual trial. With the pieces before q* held fixed the
   admissible change of the last piece is a (q - q*)^7 (C^6 continuity; 108x larger at u 4700 than at u 900), so rows out to 9000 L (q 0.99943, 91
   percent) increase the sensitivity of the objective to this exterior perturbation (a geometric statement, not a statement about the weighted
   solver objective): this is the test of chain-7 step 44 (dom9000g) with the lead's readings fixed in advance (17:42Z (44) (a), (b);
   18:04Z item 4), and step 47 (same rows as c6g, inverse domain 1e4 L) separates the effect of the inverse domain from that of the rows.
   FAR-FIELD IDENTITY (referee astra/farrow PROOF.md; derived independently by the lead, analysis 14; the algebra confirmed by the verifier, G81,
   and the stored-coefficient evaluations checked later in G82 / G84; a necessary condition for an exact solution, or for the cancellation of the
   residual at that order, conditional on a termwise differentiable expansion rho = r^k A(theta) + r^(2k-1) B(theta) + o, U = r^k V + o with V the canonical
   homogeneous inverse of r^k A: -Psi'' - (k+1)^2 Psi = k cos(theta) A - sin(theta) A', V_r = -Psi', V_theta = (k+1) Psi): the order-r^k equation is
   (c_l k - 1) A = 0 (automatic for k = 1/c_l; no nonlinear angular equation on Theta_0 at leading order) and the first correction obeys
   (c_l - 1) B = k V_r A + V_theta A', i.e. Theta_1 = B/A = (k V_r + V_theta A'/A)/(c_l - 1), with the y-axis limit Theta_1(pi/2) = -(k + 2)
   V_r(pi/2)/(c_l - 1): the first correction is DETERMINED by the leading profile; the end slopes b_m'(1) are not free asymptotic data once the b_m(1)
   are given. On c6g's stored coefficients (referee, 4096 and 8192 angular points; lead far1.py at 2^14-2^16, identical digits): V_r(pi/2) =
   89.3339213, Theta_1 stored -42.556083, forced -42.551998: Delta_1 = stored - forced = -4.08e-3 (1e-4 of |Theta_1|; off the axis at most 7.9e-4 on
   0.05 < theta < 1.4, lead), and the relative residual coefficient C_R = F_1/A = -(c_l - 1) Delta_1 = 0.018687 at the axis (an angular limit; the
   normalized residual itself is undefined on the axis), so this term alone gives the signed R/D_v -> C_R r^(k-1)/(1 + k) = 2.9e-6 at r 36000; the
   measured 1.1e-6 there has the same sign, the second-order term nearly cancels the first (+2.81e-6 and -2.80e-6 near u 4858, verifier G88), the
   trial's own relative r^-2 piece contributes about +5.7e-7 and the third-order term about +6.7e-7: the band value is a sum of several terms of
   comparable size, with a first-order inconsistency common to the seven fits measured (lead: within 6 percent on F3, X2, F2, X1, F0, dom90g); the
   lead's third-order series reproduces the measured far residual on the verifier's evaluator to measured/series 0.87 near the axis at u 4700, 0.978
   at 9504 and 0.956 at theta 0.817 (G84; c_l = 1/k convention), not to 1 percent at the band maximum. This lane's part is the geometry, the referee
   question and the step-44/45/47 runs; the series analysis is the lead's (analysis 14) with the verifier's checks (G82, G84, G88). None of this is a statement about an
   exact profile: the identity assumes the expansion, and the numbers are evaluations on the trial.
   (xvi) The FIT-CLOSURE check on the candidate X3 itself (the lead's 4.4 "[V: the closure row on X3]"; chain_x3b, 20:23Z-20:57Z): export of c6g in
   the fit convention (lead's export_fit_fit.py, 24576 x 576, two-term closure at the fit's own R_shape = 1000 (R_c = 1000 L); 80 s; deleted after,
   diagnostic JSON kept as artifacts/data/ray/x3_c6g_fitconv_export_diagnostic.json) against the paired-ray velocity of the saved formula continued
   globally (quadrature truncated at S = 1e18) at the same 52 nodes (runs/ray/x3_c6g_fit_BP.json, table x3_c6g_fit_table.txt; 1925 s; baseP rules).
   The densities coincide up to 1000 L and differ beyond, so this measures T(C_1000L rho) - T rho at the nodes: the difference between the velocity
   the fit used and the canonical inverse of its own continued density. Componentwise max |dU|: 9.2e-8 within 0.5 of P (2.0e-9 relative; frozen-
   denominator impact 2.0e-9 against the sampled |R|/D_v 1.86e-7 there, 1.1 percent), 9.2e-8 at 0.5-2.5 from P (impact 3.1e-9 against 5.6e-8, 5.5
   percent), 1.0e-9 / 1.0e-8 at r = 0.1 / 1 (impacts 5e-10), 2.0e-7 / 1.0e-6 / 3.1e-6 at r = 20 / 100 / 300 (relative 8.7e-9 / 9.4e-8 / 3.4e-7; impacts
   1.4e-8 each, against sampled residuals 1.5e-9 / 4.2e-9 / 5.0e-9, i.e. 3-10x the small sampled residual there); max impact 1.44e-8 at (19.8, 2.6),
   median 1.3e-9 (51 defined ratios). Same level as the same measurement on c6d_seg1 at 1000 L ((x)-(xi): 2.3e-9 within 0.5 of P, 3.1e-9 in the
   annulus, 1.3e-8 at r 20-300) and consistent with the lead's grid-maximum closure row on X1 (4.4: 5.1e-9 in N_f within 0.5 of P, 2.0e-8 in N_v
   for r < 1000). Reading: for the candidate the two-term closure at 1000 L changes the interior velocity by amounts whose residual impact is 1
   percent of the near-P residual and at most 1.4e-8 anywhere sampled (r <= 300); it is not what limits the candidate's residual, while the
   unfitted exterior itself carries the far-field band of (xv). Sampled, frozen-denominator, not uniform. Together with (xiii) (export convention,
   1e4 L) and (xiv) (dom90g, 100 L) this closes the lane's inverse / closure checks on the candidate's own density.
   (Sub-items (iv)-(vi) below precede (vii)-(xvi) chronologically; the numbering is by content.)
   (iv) Centre strain by the same method (runs/ray/centre_A.log; `python3 src/raycheck.py centre <shape> "Smax:1e18,smode:adapt,phimax:0.02"`):
   U_1(x, 0) = -c x + O(x^3) with c = psi_xy(0); -U_1/x at x = 4e-3 / 2e-3 / 1e-3 / 5e-4 = 15.729082792 / 15.729085583 / 15.729086283 /
   15.729086462 (U_2(x,0) = 4e-13 .. 7e-13, zero by parity), Richardson-extrapolated c = 15.72908652 (scatter of the extrapolants 3e-9; the
   quadrature error of U_1 at these targets, about 1e-11 absolute at x = 5e-4, limits c to about +-2e-8), against the identity value
   3 c_l - 1 = 15.7290865194 of the saved state (c_l stored 5.5763621731), the export's own c = 15.729086509 (its recomputed c_l 5.5763621697)
   and the referee's global-formula value 15.729086509081 (the three differ by the closure, see above). So c_l = (1 + c)/3 from the real-space
   velocity is 5.57636217 +- 7e-9, agreeing with the stored value to 8e-10 and with the export's to 4e-9, within its error: the
   identity 3 c_l - c = 1 holds for the candidate with c obtained by a method (real-space quadrature of the full source, no modes, no
   Green recursion) independent of the one used by the lead (modal psi or the moment formula c = int rho_1 r^-2 dr) and by the verifier.
   This is a check of the identity for the saved state, not a determination of c_l (the same state satisfies it at any c_l it was fitted at).
   (v) Independent transport residual at the same 51 nodes (src/ray_residual.py, runs/ray/residual_A.log): R_ray = (c_l X + U_ray) . grad rho - rho
   with grad rho from my analytic evaluator (rho_x and rho_y agree with the export's to 7e-13 / 7e-14, and with 4th-order finite differences
   of my rho to 1e-9) and U_ray from configuration A. Against the export's residual at the nodes: max abs(R_ray - R_lead) = 1.8e-6 absolute
   (at (19.5, 98.0), where R = 1.5e-5 and the denominator is 300), max abs(R_ray - R_lead)/D_lead = 5.8e-9; the maximum normalized residual over
   the 51 nodes is 6.792e-7 (mine) against 6.787e-7 (export), both at (8.299, 0.136) next to P; the smallest-residual nodes next to P agree to
   3e-9 absolute (e.g. -1.384e-7 vs -1.342e-7 at (8.598, 0.035)). Note on normalizations: the export's denominator D_lead is a flux-type
   normalization that vanishes with W at P (D_lead / (c_l abs(X) abs(grad rho) + abs(rho)) = 0.005 at y = 0.035 next to P, 0.02 at y = 0.14,
   0.14 at y = 1, 0.3 at y = 2, 0.05 .. 0.6 elsewhere), so the "residual impact" numbers above are in the lead's strict near-P normalization.
   What (i)-(v) establish: the residual that the lead and the verifier report for c6d_seg1 is reproduced at sample points by a third evaluator
   whose only shared ingredient with theirs is the saved formula; the nonlocal inverse, the centre identity and the residual assembly are
   not where the candidate's remaining residual comes from.

### 3.18 Shift 5 (from 2026-10-18T11:34Z): GPU acceleration of the lead's LSQR solver (leadcode/gpu/, artifacts/src/gpu/)
Motivation: the team's remaining questions (A1: is the characteristic defect J of the fixed-c_l candidate not higher than the free control's
at equal budget; "J decreasing under refinement"; the angular enrichment to m <= 200; fixed-c_l offsets) are limited by the lead's LSQR cost,
8.6 s per iteration at 20480 x 720 (single-threaded numpy): 750 iterations per 1.8 h segment, objectives still falling 0.4-2 percent per
250 iterations. This lane has the GPU.
Method (gpu_op.py): the lead's matrix-free linearised operator CentreDerivative (centre_fit.py + linearized.py + solver.py + stationary.py,
verbatim copies in leadcode/c7) is re-implemented in torch float64 with every table copied from the lead's CPU objects (grid, fields at the
linearisation point, spline and angular tensors, quadrature weights, row selection and weights, the finite-difference k column, the two centre
rows); the scipy DST/DCT become products with the lead's p.sin / p.cos / p.project tables (identical to 1e-14, checked), and the one-pole
radial recurrences of modal_integrals and their adjoints (scipy lfilter) become a doubling scan (same sum, tree association). The driver
gpu_long_solve.py is the lead's long_solve_fixcl_ax.py with the GPU products inside the LSQR loop and nothing else changed: same
linearisation (the lead's CPU CentreDerivative), same Rademacher probes / column scaling / damping / bounds, acceptance by the lead's CPU
objective s.fun at every --check, the lead's CentreShape.save and .long.jsonl log format (differences listed by the referee: options
--fit-radius, --max-outer; probes/norms/vector updates in torch; extra timing fields).
Validation (leadcode/gpu/val/, WORKLOG 11:5xZ, referee audit astra/gpuport/answer.md):
| test | result |
|---|---|
| operator vs the lead's CPU operator, 2048 x 480, candidate shape, random vectors | matvec 2-3e-12, rmatvec 3-5e-13 relative; adjoint identity 3e-16 |
| same at the lead's full grid 20480 x 720 (ncol 56632, nrow 7344909) | matvec 3.2e-14 / 2.0e-14, rmatvec 1.7e-14 / 1.0e-13 (sampled discrepancies of two random vectors, not operator-norm bounds); adjoint 7e-18; 0.068 s per matvec+rmatvec pair against 7.6 s CPU (110x) |
| referee's own CPU run of the port (device cpu), 512 x 480 | matvec 2.6e-12, rmatvec 6.7e-12; scan vs lfilter inside the port 1.8e-13 (the 1e-12 is cancellation near the origin amplified by the (0.04/r)^2 row weights; unweighted max error 2.8e-14) |
| end to end: the lead's fixc_c6f_m1.0e-03 first linearisation from their start shape, inner 500, check 250, fixed c_l | start 9.707451853921e-06 (lead 9.707451853921145e-06, identical); it 250: 8.764888437e-06 (lead 8.765358987e-06, -5.4e-5 rel.); it 500: 8.573210019e-06 (lead 8.574022204e-06, -9.5e-5 rel.); 500 iterations in 106 s against 4085 s |
Reading: the operator is the lead's to rounding; the LSQR path differs at the 1e-4 level in the objective after hundreds of iterations (Krylov
iterates under 1e-14 operator reassociation and a rounding-different probe scaling), which is irrelevant for comparisons between fits that
differ by 10-20 percent, provided both arms use the same schedule and backend (referee item 4: equal budgets are equal LSQR iteration counts
at the same relinearisation schedule, not equal hours). Referee findings acted on: the constructor now rebuilds the basis at the operator's k
(a misuse hazard, not reached by the driver); the test has a pass/fail. Not supported (asserted): tail_terms 1, non-spline bases, quadrature
order 2.
Production runs (results below as they complete; shapes announced to the lead with md5, kept in leadcode/gpu/<tag>/ for the verifier):
1. s2g: fixed-c_l continuation of the candidate fixc_c6f_m1.0e-03 (md5 ff61b91cdc712400ac75e531435f832c; c_l 5.575362610641546), 20480 x 720,
   inner 2500, check 250, 0.75 h. Checks (objective = the lead's L2 fit norm): 8.4745e-6 (start) -> 8.40296e-6 (250) -> 7.83258e-6 (500) ->
   6.65763e-6 (750) -> 6.16129e-6 (1000) -> 5.71481e-6 (1250) -> 5.37262e-6 (1500) -> 5.19176e-6 (1750) -> 4.99332e-6 (2000) -> 4.73155e-6
   (2500, end of linearisation 1) -> 4.3382e-6 (5000) -> 4.2368e-6 (7500) -> 4.1909e-6 (10000) -> 4.1708e-6 (11750) ... [running to the 0.75 h
   deadline]. Per linearisation the fall is 44, 7.3, 2.2, 0.95, 0.44 percent while the logged |phibar| underestimates the residual norm (it
   lacks the damping term, see the RESOLUTION below) by 2, 7, 17, 29, 31 percent at the end of each outer. [SUPERSEDED, kept as the record of
   a provisional extrapolation: the sentence "the objective converges geometrically to about 4.15e-6" written at 12:23Z was passed by the
   recorded endpoint 4.0967e-6; the observed prefix did not determine a limiting value.] For comparison the lead's
   FREE continuation fxfr from the same shape (inner 500, CPU): 8.40043e-6 (250), 7.84761e-6 (500), 7.47031e-6 (1000, after a relinearisation);
   my fixed-c_l values at the same counts 8.40296e-6 and 7.83258e-6: at 500 iterations fixing c_l costs nothing in the objective.
   FINAL (12:41:25Z): K = 20750 iterations (8 x 2500 + 750) in 2647 s, objective 4.096686e-6 = 0.4834 x the start (a fall of 51.7 percent);
   ends of the linearisations (from the log, corrected 14:5xZ after a referee audit found my first transcription of the last four wrong):
   4.731546e-6, 4.338209e-6, 4.236778e-6, 4.190864e-6, 4.161353e-6, 4.138664e-6, 4.119059e-6, 4.101046e-6, then 4.096686e-6 at +750. Shape
   leadcode/gpu/s2g/s2g_shape.npz, md5 e3c529cca959e2c8b7e0e3fecfb3543d (measured by the lead's gpupost and the verifier; results below when
   posted). Open question (lead 12:30Z): the LSQR prediction is 30 percent below the realised objective already at it 250 of the late
   linearisations with steps of 1.4e-4 (candidates: recurrence drift, derivative/objective inconsistency, nonlinearity); the lead's CPU
   diagnostic (gap f(z + t s) - f - t J s at t = 1, 1/2 by band) runs; from seg3g on, the driver logs the true linear residual at every check.
   RESOLUTION (12:43Z-12:58Z; wording corrected 14:5xZ after the referee audit astra/sec318audit): (1) the logged linear-residual norm
   |f + J S x| (one extra GPU matvec) closely predicts the norm of the trial objective on these steps: on seg3g 6.893655e-6 / 6.893654e-6,
   6.771888e-6 / 6.771888e-6, 6.660706e-6 / 6.660704e-6 at 250 / 500 / 750, and the largest relative discrepancy over its 83 checks is
   5.4e-6 (at 2500). This supports scalar objective prediction; it does not by itself establish exact linearity, exact derivatives or
   convergence of the least-squares solve (equality of norms is not equality of residual vectors). (2) the lead found (work/c6/diag_adj.py, CPU) that the
   logged "predicted" was |phibar| alone, while LSQR's residual with damping is sqrt(phibar^2 + res2) (scipy lsqr's res2 = sum psi_k^2);
   recomputed with res2 the recurrence reproduces |f + J s| to 7 digits for the first iterations, where the Lanczos vectors are still
   orthonormal to 5e-14; orthogonality is lost from about iteration 20 on (<v_1, v_k> 3.9e-7 at k = 25); the first alpha is 0.0035 against a
   typical 1.8, from which the lead reads that the residual at the s2g point is nearly orthogonal to the range of the scaled Jacobian and
   the damped problem |f + J S x|^2 + 1e-8 |x|^2 is close to stationary there (the lead's reading; the referee notes that a small first alpha
   measures a small normal residual, not the distance from the range of an ill-conditioned operator, so the distance to the least-squares
   minimum is undetermined). My first attribution of the whole gap to loss of orthogonality (NOTES 12:45Z) was
   therefore wrong in its first part and is withdrawn; which effect (damping or orthogonality) limits the true decrease is tested by the
   arms of item 3 below. The driver now logs predicted = sqrt(phibar^2 + res2), phibar, damp |x|, the undamped estimate, linres and actual.
   LEAD'S MEASUREMENT OF s2g (their scan 32768 x 640, NOTES 12:52Z item 5): although the objective fell by 52 percent, the whole-box N_f
   maximum ROSE from 6.77e-7 (candidate) to 1.444e-6 at r 8.37, theta 0.012 (next to P), while 10-100 fell 4.43e-7 -> 2.01e-7, 0.1-2 1.93e-7 ->
   6.95e-8 (the far bands rose slightly: N_f 1.9e-8 -> 2.1e-8, N_v 8.8e-8 -> 1.03e-7 beyond r 1000),
   the axis q0 maximum 1.07e-5 -> 3.14e-6, I(0.03) 2.06e-6 -> -6.2e-7, h(P) - 1 = -7.4e-9, B_3 0.3016, J185 2.60e-6 (1.86e-6 of it from the
   disc 0.03 <= |X - P| < 0.3). The L2 objective and the near-P maximum are not ordered the same way; the standard (G20 (b)) reads the latter.
3. Solver-setting test (lead rule 12:52Z item 4; reotest2.sh; steps 21-25): from the s2g end, one linearisation of 2500 iterations, check 250,
   fixed c_l, arms plain damping 1e-8 (production), reorth 1e-8 (one-sided full reorthogonalisation of the right Lanczos vectors, Simon and
   Zha 2000, CGS2, V on the GPU), plain 1e-10, plain 1e-12, reorth 1e-12 (conditional). An arm replaces the production setting only if its
   actual objective at 2500 is at least 3 percent below the plain 1e-8 arm's and its 2-10 N_f (lead scan) is not higher. Small-grid
   indication (1024 x 480, 300 its from the candidate): reorth 1.3000e-4 against plain 1.3438e-4 at equal count (-3.3 percent), cost +10
   percent per iteration. RESULTS (13:35Z-13:53Z; actual objective at 1000 / 2000 / 2500 iterations from 4.096686e-6): plain 1e-8
   4.092375e-6 / 4.080707e-6 / 4.071272e-6 (-0.62 percent); reorth 1e-8 4.091210e-6 / 4.074830e-6 / 4.019190e-6 (-1.89 percent, 1.28 percent
   below plain, the gain concentrated in the last 500 iterations with damp |x| rising from 9e-8 to 2.1e-7); plain 1e-12 4.0712595e-6 at 2500
   (3.0e-6 relative from plain 1e-8; equal to 5 digits at every check). Estimates: predicted = sqrt(phibar^2 + res2) is the DAMPED residual
   sqrt(|f + J S x|^2 + damping |x|^2) and differs from the actual objective by 0.0135 percent (plain) and 0.142 percent (reorth) at 2500;
   after subtracting the penalty (predicted_undamped) it agrees with the explicitly evaluated |f + J S x| to 2.4e-14 relative on all arms,
   while |f + J S x| agrees with the actual objective to 1e-7 .. 5e-6 (plain 1e-8 at 2500: 4.071822e-6 / 4.071273e-6 / 4.071272e-6; phibar
   alone 2.13e-6). No arm reaches the 3 percent threshold: the production setting (plain, damping 1e-8) is kept under the stated rule. What
   this shows and does not show: at this start and this 2500-iteration budget, lowering the damping produced negligible improvement and
   reorthogonalisation a real 1.28 percent; the distance of s2g to the linearised or nonlinear least-squares minimum of this basis is
   undetermined (the lead's reading "close to the floor, remaining decrease on singular values near 1e-3" is a hypothesis without spectral
   evidence). The arm shapes (leadcode/gpu/reo_*/) are scanned by the lead (2-10 N_f) as the second half of the rule (reorth 2-10 N_f not
   higher: verifier 1.348e-6 against 1.423e-6).
4. seg3g (free control from c6f_seg2, md5 a1a7a209c9078237c4af95cef7a8b6ee; same schedule and budget as s2g): DONE 13:25:35Z, K = 20750 in
   2646 s; 7.0768e-6 -> 6.8937e-6 (250) -> 6.7719e-6 (500) -> 6.6607e-6 (750) -> 4.6467e-6 (2500) -> 4.4406e-6 (5000) -> 4.3465e-6 (10000) ->
   4.2630e-6 (20000) -> 4.2586e-6 (20750); c_l 5.576364040 -> 5.576370935 (+6.9e-6, away from the candidate's value; no slope resolved by the
   lead's 1e-4 criterion); h(P)-1 -6.8e-9. Shape leadcode/gpu/seg3g/seg3g_shape.npz.
   EQUAL-COUNT COMPARISON s2g (fixed c_l 5.5753626, start 8.4745e-6, fall 51.7 percent) / seg3g (free, c_l 5.57637, start 7.0768e-6, fall
   39.8 percent; different start shapes, so this is not an isolated experiment on fixing c_l): objective ratio 1.018 (2500), 0.977 (5000),
   0.967 (7500), 0.964 (10000), 0.962 (15000-20750): from 5000 iterations on the fixed-c_l fit has the lower objective, by 2.3, 3.3, 3.6 and
   then 3.8 percent.
   Scans (lead's quick_scan_fit 32768 x 640, run in this lane; the lead's own scan of s2g gives the same digits), s2g / seg3g: 2-10 N_f
   1.44e-6 / 1.59e-6 (N4 4.03e-7 / 4.42e-7), 0.1-2 6.95e-8 / 7.13e-8, 10-100 2.01e-7 / 2.07e-7, 100-1e3 2.82e-8 / 2.95e-8, r > 1e3 2.05e-8 /
   1.92e-8, all rms 1.74e-8 / 1.85e-8; near-P fd-log by theta 0 / 0.025 / 0.049 / 0.101: 1.13e-6 / 1.22e-6 / 5.0e-7 / 5.1e-7 against 1.25e-6 /
   1.30e-6 / 5.3e-7 / 5.7e-7. By the lead's rule (12:02Z item 3) the fixed-c_l fit has the lower whole-box N_f and not-higher N_v for
   r <= 1000; N_v beyond 1000 is 7 percent higher on my scan (configuration spread: verifier) and the 857-label J is the verifier's
   measurement. The fixed continuation raised its near-P maximum from 6.5-7.0e-7 (its start fxm1o2i250) to 1.42-1.44e-6 while lowering the
   10-100 band by 1.7-2.2x and the axis q0 by 3x; the free continuation lowered its near-P maximum from 2.1-2.3e-6 (its start c6f segment 2)
   to 1.57e-6; improvements elsewhere depend on the band, normalization and evaluator (far bands slightly up on the lead's scan). The L2
   objective and the near-P maximum are not ordered alike (lead 12:52Z item 3), and G20 (b) reads the latter.
   VERIFIER G72 (13:41Z, own generator and evaluator at two configurations, 857-label J): s2g / seg3g: N_f box max 1.424e-6, 1.435e-6 /
   1.574e-6, 1.575e-6 (both at r 8.44, theta 0.0098); N_v r <= 1000 3.98e-7 / 4.39e-7; N_v r > 1000 1.102e-6, 1.115e-6 / 1.097e-6, 1.108e-6
   (s2g higher by 5e-9 and 7e-9, inside the spread 1.1e-8); J(0.03 / 0.01) 3.143e-6 / 3.462e-6 against 3.414e-6 / 3.763e-6; max |q0| 3.13e-6 /
   3.21e-6; identity c_l 5.575362607 / 5.576370932; h(P) = 1 root minus identity -4.7e-9 / +4.2e-8. By the lead's 12:02Z rule read with the
   far-field band = all r > 1000 of the verifier's evaluator (to 7.65e6), s2g is the candidate of the pair (all four parts; the far N_v part
   only within the spread); read on the fit-domain band 1000 <= r <= 1000 L, s2g's N_v is 2.9-3.1 percent higher, beyond the spread, and the
   rule gives seg3g (G72 (a) amendment, accepted by the lead 14:12Z: the band endpoint was underspecified before the measurement; both readings
   are reported; for the m <= 200 pair the band was fixed in advance at all r > 1000). But neither continuation replaces the pre-continuation
   candidate fxm1o2i250 (N_f 6.98e-7 / 6.53e-7 there, 2.0-2.4x lower than either member; its N_v is higher (5.20e-7, 1.132e-6) and its J
   lower (2.738e-6)): the fits are NOT ordered. The 20750 iterations at fixed c_l halved the L2 objective, lowered the axis residual q0 by 3x
   (1.07e-5 -> 3.13e-6) and moved the cap-frequency ripple (omega 304, close to 2 m_max = 300) from r 3-5 to r 7-8.6 and above P, where the
   small transport terms near the stagnation point divide it (verifier's reading of the maps); whether coefficients of the m <= 150 basis
   exist that remove it is not established (the residual is nonlinear in the density); the m <= 200 pair (steps 31-32) tests the enrichment.
   LEAD DECISION (13:54Z, on G72; amended 14:12Z): s2g is the candidate of the pair under the all-r > 1000 reading (shape md5
   e3c529cca959e2c8b7e0e3fecfb3543d; c_l fixed 5.575362610641546; 20750 GPU LSQR iterations after fixc_c6f_m1.0e-03; objective 4.0967e-6),
   seg3g under the fit-band reading; the fits s2g and fxm1o2i250 are not ordered (G72 (a)); the solver setting stays plain damping 1e-8.
5. c6g (step 31; the m <= 200 angular row at the candidate's c_l: the lead's c6g_start_shape.npz = the s2g end with 50 more angular functions
   per radial function, zero coefficients, density unchanged, md5 9dd60daff7e327234e401c9b2c07bb48; 375 x 201 + 6 singular + the exponent
   column = 75382 columns; fit grid 20480 x 960 (row angles per angular function as m <= 150 on 720; the denser grid changes the objective of
   the unchanged start density from 4.0967e-6 to 4.0502e-6, and no matched m <= 150 run on the 960 grid exists); memory measured first:
   peak RSS 10.17 GB, GPU 5.8 GB, linearisation 55 s): started 13:54:47Z, K = 20750. Start objective on the 960 grid 4.0502e-6; it 250:
   2.9103e-6 (-28 percent in one tenth of a linearisation); 1000: 2.3351e-6 (-42.3 percent); 7500: 1.8318e-6 (-54.8 percent); 15000:
   1.7017e-6. DONE 15:05:48Z: K = 20750, objective 1.619270e-6 (0.400 x the start); ends of the linearisations 1.991840e-6, 1.886121e-6,
   1.831770e-6, 1.784085e-6, 1.741751e-6, 1.701690e-6, 1.663570e-6, 1.627789e-6, then 1.619270e-6 at +750 (per-linearisation falls 5.3, 2.9,
   2.6, 2.4, 2.3, 2.2, 2.1 percent: no sign of a floor at this budget, unlike s2g on m <= 150). Shape leadcode/gpu/c6g/c6g_shape.npz, md5 15f8095f7e79dbfa0c50d75e5fe8997a.
   Angular enrichment together with the denser angular fitting grid lowers the attained objective substantially in this continuation,
   where the m <= 150 continuation gained 0.6 percent per 2500 iterations; whether it improves the independent residual maxima and the
   characteristic defect is read on the lead's scans and the verifier's rows (c6g and its equal-budget free control c6gF, step 32, running
   from 15:05:48Z). VERIFIER G73 (intermediate, 14:39Z) on c6g's FIRST outer iterate (2500 its, objective 1.9918e-6): whole-box N_f 1.009e-6 /
   1.033e-6 / 1.047e-6 at the three configurations (0.70-0.72 x s2g, at (8.47, 0.016) next to P), N_v 2-10 2.82-2.93e-7 (0.70-0.72 x), far N_v
   1.118-1.148e-6 (+1.2-1.5 percent), 185-label J 1.59-1.65e-6 (0.60-0.66 x), identity c_l 5.575362607; the cap ripple next to the x-axis
   now peaks at omega 399 (twice the new cap) with half the amplitude (8.3e-8 against 1.59e-7 at r 8.45). G73 (d): the sampled near-P
   maximum varies by 4-6 percent across the three configurations (N11250 q384, N16875 q512, N16875 q768), so N_f maxima are quoted as
   ranges over them and fits compared configuration by configuration; orderings found so far exceed that spread.
   LEAD'S SCANS OF THE c6g END (NOTES 15:11Z; 32768 x 640 / 24576 x 960; c6g against s2g): whole-box N_f 6.94e-7 / 7.27e-7 at (r 8.526,
   theta 0.0074-0.0082) against 1.44e-6 / 1.51e-6 (ratio 0.48); N_v r <= 1000 1.94e-7 / 2.04e-7 against 4.03e-7 / 4.22e-7; N_v on the fit band
   1000 <= r <= R 6.8e-8 against 1.03e-7; N_f bands 0.1-2 2.9e-8 (7.0e-8), 10-100 8.2e-8 (2.0e-7), 100-1000 1.6e-8 (2.8e-8), rms 7.1e-9
   (1.7e-8); near-P fd-log theta 0 / 0.025 5.1e-7 / 5.8e-7 (1.13e-6 / 1.22e-6); 185-label J 1.154e-6 (2.595e-6); max |q0| 1.33e-6 (3.14e-6);
   I(0.03) -3.40e-7 (-6.24e-7); identity c_l 5.5753626072 (3.4e-9 below the fixed value); h(P) - 1 -8.8e-9 / -5.3e-9; x* 8.600064; B_3 orig
   0.3027 [0.3010, 0.3040]; the angular spectrum of R/dd next to P peaks at omega 402 = 2 m_max + 2 on every row (the near-P residual is
   still at the cap frequency). Lead's reading (their scans; the verifier's values decide): the step m <= 150 -> 200 at the same fixed c_l
   and budget lowered every band, the near-P maximum and J together by about 2x, the first refinement step to improve all at once; c6g's
   whole-box N_f is at the level of the early-stopped fxm1o2i250 with less than half its J. A fourth angular row m <= 250 (c6h fixed /
   c6hF free, chain steps 41-42, after the domain pair and the resolution rows) was requested at 15:14Z with its reading fixed in advance
   (a refinement row, not a candidate; "systematic improvement" = none of whole-box N_f, near-P N_f, N_v (r <= 1000, r > 1000) and the
   857-label J increases from one row to the next by more than the configuration spread).
   VERIFIER G73 (15:30Z) ON THE c6g END (own generator and evaluator, four configurations; A5 = the far-field correction of their evaluator):
   whole-box N_f 6.909e-7 (N11250 q384; at (8.78, 0.31)), 6.841e-7 (N16875 q512; at (8.528, 0.0074) next to P), 7.156e-7 (N16875 q768),
   6.832e-7 (N22500 q512) against s2g 1.424e-6 / 1.435e-6 / 1.505e-6 (ratios 0.475-0.485); N_v r <= 1000 1.91-2.01e-7 against 3.98-4.20e-7
   (0.48); far N_v (all r > 1000) 1.074-1.084e-6 with A5 against s2g 1.063-1.069e-6 (c6g HIGHER by 0.7-1.5 percent, beyond s2g's spread of
   6e-9 over the three configurations; without A5 c6g is lower, 0.981-0.989), N_v on the fit band 1000 <= r <= 1000 L 2.15e-7 against s2g
   2.51e-7 and seg3g 2.44e-7 (c6g lowest inside the fit radius; beyond it every fit reads 1.06-1.15e-6, a band hardly moved by any fit);
   185-label J 1.23-1.27e-6 (0.46-0.50 x s2g); 857-label J 1.388e-6 / 1.602e-6 at eps 0.03 / 0.01 against s2g 3.143e-6 / 3.462e-6 (0.44 /
   0.46) and the early-stopped fxm1o2i250 2.738e-6 / 2.684e-6: c6g is the first audited fit with both the lowest whole-box N_f range
   (level with fxm1o2i250's 6.5-7.0e-7) and a J below fxm1o2i250's (by 2.0x). Equal-budget angular row (one linearisation of 2500 its
   from the s2g end at the same c_l): reo_plain8 (m <= 150, 720 angles) N_f 1.423e-6 / 1.434e-6, 185-J 2.55-2.58e-6 against c6go1 (m <= 200,
   960 angles) 1.009e-6 / 1.033e-6, 1.59-1.65e-6: at equal budget the m <= 200 setup (basis and collocation grid together, not the basis
   alone) gives 0.71-0.72 x in N_f and 0.62-0.69 x in J. The angular row of G20 (b3) therefore falls from m <= 150 to m <= 200 at the fixed
   c_l both at the end of the run (0.44) and at equal budget; the m <= 100 member (fxd1g, step 35) is pending. The far-field N_v beyond the
   fit radius (1.06-1.15e-6 on every fit, 0.5-2 percent apart with A5-dependent signs) is the one quantity c6g does not lower.
8. dom90g (step 33; the domain column at the candidate's basis and c_l: fit radius 90 shape units (R_inverse 100, two-term closure there)
   from the c6g end, fixed c_l, 20480 x 960, inner 2500, check 250, K = 20750): DONE 17:14:27Z; objective on its rows 2.345e-4 (the closure at
   R = 100 does not match the global fit's far field) -> 1.062127e-6; shape leadcode/gpu/dom90g/dom90g_shape.npz, md5 7f989938b5e9a6434fe4e7bd195647b4. Read in the
   fit convention by the lead (gpupost_dom) and the verifier (G20 (b) A4). dom300g (step 34, fit radius 300) started 17:14:27Z.
9. dom300g (step 34; the second domain column at the candidate's basis and c_l: fit radius 300 L (R_inverse 333 L, two-term closure there) from the
   c6g end, fixed c_l, 20480 x 960, inner 2500, check 250, K = 20750): started 17:14:27Z, DONE 18:43:41Z; objective on its own rows 1.07608e-5 (start:
   the 333 L closure does not match the global fit's far field) -> 1.586742e-6 (2500) -> 1.535870e-6 (5000) -> 1.492360e-6 (7500) -> 1.454025e-6
   (10000) -> 1.417587e-6 (12500) -> 1.383685e-6 (15000) -> 1.352317e-6 (17500) -> 1.322560e-6 (20000) -> 1.314892e-6 (20750), still falling 2.2
   percent per linearisation; h(P) - 1 at the start 1.6e-7 (own grid). Shape leadcode/gpu/dom300g/dom300g_shape.npz, md5 54ea57a7a472755d1b94af398278ee52.
   Read in the fit convention by the lead (gpupost_dom, A4 rule) and the verifier (G20 (b) domain column). dom90g (item 8) and dom300g together are
   the domain pair at the candidate's basis; both carry 20750 further iterations on their own domains (the lead's text says so).
10. Chain 7 (shift 6; lead approval NOTES_FOR_TEAM 17:42Z and 18:04Z, readings fixed there before any result): step 46 memtest 24576 x 960 at fit radius
   9000 on c6g (10 its, 112 s, peak RSS 11,962,556 kB = 11.4 GiB < the 14 GB rule) 18:36-18:38Z; step 44 dom9000g (c6g end, fixed c_l, fit rows r < 9000 L, inverse
   domain / two-term closure at R_shape 1e4 L, 24576 x 960, K 20750) started 18:38:05Z, by a wait-pattern bug of the chain script concurrently with
   chain 6 (two heavy processes, the box limit; all chains observe it by the slot rule): start objective on its 9000 L rows 9.247e-6 (c6g read on the
   enlarged-domain configuration; against 1.619e-6 on c6g's own configuration the rows, inverse domain, grid and weights all change, so the increase
   is not assigned to the exterior rows by this comparison alone), 1.5636e-6 at 500 its, 1.5621e-6 at 750 its. Then 45 c6g2 (c6g + 20750 its), 47 c6gR4
   (the referee's control: c6g end, rows r < 900 L as c6g but inverse domain 1e4 L, equal budget; new driver option --inverse-radius). Motivation and
   geometry in 3.17 item 7 (xv) below (the far-field band lies in the unfitted continuation of the last spline piece).
11. fxd1g (step 35; the m <= 100 member of the angular row at the fixed c_l: the lead's fixc_c6d_m1.0e-03_shape.npz = the 375 x m <= 100 basis
   (c6d) transplanted to c_l 5.5753626, md5 14865271ea855e12d221db5711589c05; fixed c_l, 20480 x 480, inner 2500, check 250, K = 20750): started
   18:43:41Z (concurrently with dom9000g), DONE 19:23:16Z, total 20750 iterations (outer 9, it 750); objective on its rows 1.94371e-05 (start) -> ends of the
   linearisations 1.781426e-05, 1.732474e-05, 1.705876e-05, 1.685318e-05, 1.668941e-05, 1.654715e-05, 1.642062e-05, 1.630917e-05, 1.628550e-05. Shape leadcode/gpu/fxd1g/fxd1g_shape.npz, md5 3334859a386607f210052e98b3ba50af. For the angular row (fxd1g 100 / s2g 150 / c6g 200
   / c6h 250, all at c_l 5.5753626 and 20750 its, read by the lead's 15:14Z rule on the verifier's rows): the L2 objectives at equal count are 1.629e-05
   (m <= 100, 480 angles), 4.097e-6 (m <= 150, 720), 1.619e-6 (m <= 200, 960); the grids differ with the cap (4.8 angles per mode), so the objectives
   are not on the same rows. Step 36 fxb1g (244 radial x m <= 100 at the fixed c_l, 10240 x 480) started 19:23:17Z.
12. fxb1g (step 36; the 244-radial-function member of the resolution row at the fixed c_l: the lead's fxt_fixc_c6b_m1.0e-03_-1.0e-03_shape.npz,
   md5 3083263a8c6cb19158f141e72766b4c7 (244 x m <= 100, transplanted to c_l 5.5753626); fixed c_l, 10240 x 480, inner 2500, check 250, K = 20750):
   started 19:23:17Z, DONE 19:42:55Z, total 20750 iterations; objective on its rows 1.908341e-05 (start) -> ends of the linearisations 1.779631e-05, 1.722261e-05, 1.683194e-05, 1.653197e-05, 1.629063e-05, 1.609226e-05, 1.592437e-05, 1.578002e-05, 1.574267e-05. Shape
   leadcode/gpu/fxb1g/fxb1g_shape.npz, md5 9e9a67abbe690118c532916075314c6d; c_l 5.575362612345. Read by the lead (gpupost) and the verifier (resolution row 244 x m <= 100 of section 4.4).
   Step 43 (memtest 20480 x 1200 on the lead's c6h_start) started 19:42:55Z; step 41 c6h follows.
13. dom9000g (chain-7 step 44; the fourth domain / far-field row at the candidate's basis: c6g end, fixed c_l, fit rows r < 9000 L (q up to 0.99943,
   91 percent of the last knot interval; see 3.17 item 7 (xv)), inverse domain and two-term closure at R_shape 1e4 L, 24576 x 960 (log-radial spacing
   7.50e-4 against 7.87e-4 for 20480 points on 7 decades), 11753238 rows, inner 2500, check 250, K = 20750; lead's readings fixed in advance, NOTES_FOR_TEAM
   17:42Z (44) and 18:04Z item 4): started 18:38:05Z (concurrently with chain 6), DONE 20:21:48Z, total 20750 iterations; objective on ITS rows 9.246879e-06 (start = c6g evaluated on the
   enlarged-domain configuration; rows, inverse domain, grid and weights differ from c6g's own, so this is not a measurement of the exterior residual
   alone) -> 1.334388e-06 (ratio 0.144; ends of the linearisations 1.520866e-06, 1.484089e-06, 1.455982e-06, 1.429846e-06, 1.405599e-06, 1.382080e-06, 1.359849e-06, 1.338820e-06, 1.334388e-06). Shape
   leadcode/gpu/dom9000g/dom9000g_shape.npz, md5 269865efab75bc778dab2a4407f7feba; c_l 5.575362610642. Read by the lead (A4 + far-band rule, far1.py C at the axis) and the verifier
   (G80 / G87 baselines: c6g far N_v 1.10e-6 over 1000 L < r <= 9000 L, 9.7e-7 over 9000 L < r <= 1e4 L, 9.3e-7 over r > 1e4 L). Steps 45 c6g2 and 47 c6gR4
   follow (chain 7c; 45 was restarted fresh after a 2-minute false start, see WORKLOG 20:2xZ). Smoke test of the --inverse-radius option (2048 x 480, 5 its,
   20:23Z): rows selected r < 900, R_shape 1e4 saved, c_l fixed, exit 0.
   LEAD'S READING OF dom9000g (NOTES_FOR_TEAM 20:28:25Z; lead numbers, verifier rows requested): interior (fit convention, 32768 x 640 / 24576 x 960),
   dom9000g / c6g N_f maxima: r <= 0.1 0.97, 0.1-2 0.93, 2-10 0.72 / 0.65 (both at r 8.73, theta 0.19), 10-100 0.97, 100-1000 0.86, h(P) - 1 -8.0e-9 /
   +6e-13; centre coefficients equal c6g's to 4e-9: two-sided A4 holds except 2-10 at 960 (0.65, lower). Far field (lead's tools): the axis
   mismatch Delta_1 = Theta_1 stored - forced fell from -4.08e-3 (c6g) to -1.41e-4 (factor 0.035; relative to |Theta_1| from 9.6e-5 to 3.3e-6); the first-order series coefficient q1 at theta
   1.568 from 1.58e-2 to 4.9e-4; on the lead's formula-global evaluator (24576 x 576, inverse to 1e7 L) the signed R/N_v on the column theta 1.56807
   is 8.2e-9 / 2.9e-9 / 7.4e-9 / 8.9e-9 / 5.3e-9 / 2.6e-9 at 1000 / 4699 / 9500 / 3e4 / 1e5 / 3e5 L against X3's 1.99e-7 / 1.09e-6 / 9.46e-7 /
   5.11e-7 / 2.17e-7 / 9.2e-8; the two next columns |R/N_v| <= 2.8e-8 (X3 up to 1.07e-6); at theta 0.818 at most 2.5e-8 (X3 2.2e-7). Lead's
   reading: the rows to 9000 L removed most of the first-order inconsistency (Delta_1 fell by 0.035), not only balanced higher orders; the 18:04Z item 4
   conditional does not apply. On the lead's scans the interior maxima decrease, with the 2-10 ratio 0.65 at 24576 x 960 below the two-sided
   lower bound 2/3 of A4 (reported with its ratios, as the lead's 20:28Z item 4 requires). Attribution of the far-band fall to the added rows
   awaits the controls 45 (budget on the old domain) and 47 (enlarged inverse domain and grid with the old rows); the verifier's band maxima are
   in G91 below. This lane's comment: the result supports the reading of 3.17 item 7 (xv)
   (uncollocated continuation, weakly constrained exterior coefficients) and does not by itself make dom9000g the candidate (no equal-budget free
   control; the lead's rule); an optional step 48 dom9000gF (c6gF end, free c_l, fit radius 9000 L, same budget) is offered to the lead.
   VERIFIER G91 (20:44Z) ON dom9000g (own generator and evaluator; dom9000g in its own convention, closure at 1e4 L, and formula-continued; c6g formula-
   global): interior A4 two-sided, ratios dom9000g / c6g: 2-10 N_f 1.020 / 0.656 (LOW, below 1/1.5) / 0.744 at 11250 x 384 / 16875 x 512 / 22500 x 384;
   10-100 0.817 / 1.415 (1.049 with the y-axis columns excluded) / 0.996; |h(P) - 1| 4.8e-8 / 5.0e-9 on N >= 16875; near-P N_f 4.45e-7 .. 4.51e-7 against
   6.5e-7 .. 6.8e-7 (0.66-0.68; the fall is next to P, the lobe above P unchanged, 1.00); 857-label J 9.11e-7 / 1.02e-6 against 1.39e-6 / 1.60e-6 (0.656 /
   0.637); N_v r <= 1000 1.02 / 0.655 / 0.776; identity c_l 5.5753626108, D14 |E| <= 6.7e-9, x* 8.6000645. FAR BANDS (N_v maxima, 16875 x 512 /
   22500 x 384; own convention; formula continued; c6g): 1000 L-9000 L 3.20e-8 / 3.04e-8; 3.20e-8 / 3.04e-8; 1.102e-6 / 1.094e-6 -> ratio 0.029 / 0.028;
   9000 L-1e4 L 2.40e-8 / 2.41e-8; same; 9.68e-7 / 9.64e-7 -> 0.025; r > 1e4 L: own convention 2.31e-5 (in the closure region, the C^1 junction at
   1e4 L; 2.3e4 L next to the y-axis), formula continued 3.28e-8 against c6g 9.34e-7 / 9.28e-7 -> 0.035. Whole box in the formula reading: N_f
   4.49e-7 / 4.91e-7 (0.656 / 0.744 of c6g), N_v 1.26e-7 / 1.44e-7 (0.11 / 0.13). By the lead's (44) (b) rule ("falls" = ratio <= 0.5 on every
   N >= 16875 configuration) the far band FALLS, by measured factors 29-40 on both bands, formula-continued as well as in the fit's own convention, while the
   interior satisfies the rule except for being lower than 1/1.5 next to P at one configuration (the pattern of all three domain columns). The lead's
   reading (20:28Z) and the verifier's agree: the candidate family's far-field band value was that of the unfitted continuation; fitting where it
   sits removes most of it, together with most of the first-order mismatch Delta_1 (0.035 x on the lead's tools; verifier far2_ver pending in
   G91 (iii)); whether the fall is due to the rows, the inverse domain or the budget is separated by steps 45 and 47 (pending). X3 remains the
   candidate by the pre-registered rule (17:42Z (44)); dom9000g is the 9000 L domain row, and its free control dom9000gF (step 48, lead "48 yes"
   20:41Z, a data row read by ratios without a decision) is queued last.
14. c6h (chain-6 step 41; the m <= 250 member of the angular row at the fixed c_l, a refinement row by the lead's 15:14Z rule, not a candidate:
   the lead's c6h_start_shape.npz = the c6g end enriched to m <= 250 with zero new coefficients (density unchanged), md5 4dafef26097523506f4258b50e243d2a,
   94132 columns; fixed c_l, 20480 x 1200 (4.8 angles per mode as before), inner 2500, check 250, K = 20750; memtest RSS 12,435,640 kB = 11.9 GiB):
   started 19:44:56Z (shared GPU throughout), DONE 21:42:32Z, total 20750 iterations; objective on its 1200-angle rows 1.605767e-06 (start = the c6g density on the
   1200 grid; c6g read 1.619e-6 on its own 960 grid) -> ends of the linearisations 8.412337e-07, 7.610718e-07, 7.033934e-07, 6.571615e-07, 6.180730e-07, 5.842499e-07, 5.552260e-07, 5.301312e-07, 5.206263e-07 (per-linearisation falls 9.5, 7.6, 6.6, 5.9, 5.5, 5.0, 4.5 percent, then +750) -> 5.206263e-07 (ratio
   0.324 to the start). Shape leadcode/gpu/c6h/c6h_shape.npz, md5 5b192f613fe8a0b80f8eda6a944db6b5; c_l 5.575362610642. Read by the lead's 15:14Z angular-row rule on the verifier's rows
   (whole-box N_f, near-P N_f, N_v r <= 1000, far N_v, 857-label J, none increasing by more than the configuration spread from the m <= 200 row).
   Step 42 c6hF (free control, from the lead's c6hF_start md5 6b1ea5f9c95481162190ba04e1452c87) started 21:42:32Z.
   LEAD'S READING OF c6h (NOTES_FOR_TEAM 21:50:31Z; lead scans, cross-check only; verifier rows requested): c6h / c6g N_f maxima (fit convention,
   32768 x 640 ; 24576 x 960): whole box 0.685 ; 0.700 (both at the lobe above P, r 8.73, theta 0.194), 0.1-2 0.370, 10-100 0.447, 100-1000 0.386 ;
   0.360, the 1000 L band 0.76; h(P) - 1 -9.0e-9 ; -5.4e-9; 185-label J 4.45e-7 against 1.257e-6 (0.354; the [0.03, 0.3) shell part 0.42, the
   [0.3, 1) part unchanged); axis I(0.03) -6.8e-8 (c6g -3.4e-7), max |q0| 6.4e-7 (1.33e-6). Far field on the lead's tools: Delta_1 at the axis
   -4.078e-3 (c6g -4.084e-3), the series coefficients equal c6g's to 0.2 percent, the far N_v bands 1.089e-6 / 9.62e-7 / 9.25e-7 against c6g's
   1.092e-6 / 9.65e-7 / 9.28e-7: the angular refinement lowers the interior by 0.35-0.70 and leaves the unfitted far field unchanged, as the
   geometry of 3.17 item 7 (xv) predicts (no rows there). On the lane's logs: at equal angular density (4.8 angles per mode) and equal iteration
   count the m <= 250 objective ends at 0.32 of its start where m <= 200 ended at 0.40 of its start; both are still falling at the end (4.5 and
   2.1 percent per linearisation), so neither row is converged for its basis. The verifier's 15:14Z-rule reading decides the row.
15. c6g2 (chain-7c step 45; the budget row on the candidate's basis: c6g continued at the fixed c_l on its own rows (r < 900 L), inverse domain 1000 L,
   20480 x 960, inner 2500, check 250, K = 20750 further iterations, i.e. 41500 since X2; a data row, not a candidate; lead's readings fixed in advance,
   NOTES_FOR_TEAM 17:42Z (45) and 21:10Z item 3: against X3 by ratios, and the far band 1000 L-9000 L ratio decides the attribution of the dom9000g fall
   to its rows (above 0.8: the rows; at most 0.5: the iterations alone; in between: stated as measured)): started 20:57:08Z (fresh from c6g after a
   2-minute false start, see item 13), DONE 22:23:35Z, total 20750 iterations; objective on its rows 1.619270e-06 (= c6g's end) -> ends of the linearisations
   1.550821e-06, 1.492581e-06, 1.443825e-06, 1.400636e-06, 1.362312e-06, 1.327802e-06, 1.295786e-06, 1.266754e-06, 1.263892e-06 (falls 3.8, 3.3, 3.0, 2.7, 2.5, 2.4, 2.2 percent per linearisation, then +750) -> 1.263892e-06 (ratio 0.781; the second 20750 iterations gain 22 percent where the first
   gained 60 percent). Shape leadcode/gpu/c6g2/c6g2_shape.npz, md5 0072c9ead3bbf2a104f35549957a8115; c_l 5.575362610642. Read by the lead and the verifier (G95+). Step 47 c6gR4
   (c6g end, fixed c_l, rows r < 900 L as c6g, inverse domain 1e4 L by --inverse-radius, 24576 x 960, K 20750) started 22:23:35Z.
   LEAD'S FAR-FIELD CROSS-CHECK OF c6g2 (22:32Z item 3; lead tools, formula continued): C_R at the axis 1.0026 x c6g's (verifier far1_ver the same
   ratio), far N_v bands 1000 L-9000 L 0.9997 (A5 1.0039), 9000 L-1e4 L 0.9994, r > 1e4 L 0.9994, series coefficients equal to 0.2 percent: 20750 further
   iterations on the 900 L rows leave the far field at X3's. By the lead's 21:10Z item 3 (i) (ratio above 0.8 on the lead's numbers; the verifier's
   formula-global N_v at N >= 16875 decides) the fall of the 9000 L row's far band and of its C_R comes with its rows, not with the budget.
   VERIFIER G96 (22:28Z) ON THE ANGULAR ROW fxd1g / s2g / c6g / c6h (m <= 100 / 150 / 200 / 250, all at c_l 5.5753626; configurations 16875 x 512,
   16875 x 768, 22500 x 512; c6h's density has sine modes to n = 503, so 11250 x 384 does not resolve it and is not a row value): whole-box N_f raw
   3.11e-6 -> 1.44-1.51e-6 (0.46-0.48) -> 6.84-7.16e-7 (0.48) -> c6h 4.23e-7 / 4.27e-7 / 4.88e-7 with the y-axis floor columns excluded (A5; 0.60-0.71;
   the raw c6h maximum at 16875 x 768 sits in the floor column); near-P N_f c6g -> c6h 0.33-0.41; N_v r <= 1000 0.62-0.74; 857-label J 1.388e-6 -> c6h
   (0.36 / 0.37); far N_v (r > 1000) within 0.4 percent of c6g (a rise of 0.2-0.4 percent at the last step, inside the configuration spread, as from
   150 -> 200); C_R at the axis 2.0035e-2, 1.8923e-2, 1.8687e-2, 1.8657e-2 along the row (ratios 0.944, 0.988, 0.998: the first-order far-field
   inconsistency levels off with the angular cap, as expected without rows in the far field). Verdict: on the A5 values whole-box N_f, near-P N_f,
   N_v r <= 1000 and J decrease at every step on every configuration and the far N_v does not increase by more than the spread: the row meets the
   lead's 15:14Z reading. LEAD (22:32Z item 4), c6h against c6g2 (both X3 + 20750 iterations at the fixed c_l; the equal-budget comparison of the
   last angular step, lead scans): whole box 0.98 / 0.96 (the lobe above P: almost all of the m <= 250 row's fall there is the budget's), 10-100 0.46,
   0.1-2 0.43, 100-1000 0.47-0.51, 1000 L band 0.70-0.72 (the cap lowers the bands away from P by about 2); 185-label J (lead cd SUMMARY, r0 20,
   eps 0.03; corrected by the lead 22:50Z, the first-posted 0.78 was the 10-label shell total): c6g 1.257e-6, c6g2 5.998e-7 (0.477 of X3), c6h 4.450e-7
   (0.354 of X3), c6h / c6g2 0.742; on the 10 labels of the shell table the [0.03, 0.3) part is 1.14 (higher), [0.3, 1) 0.93, [1, 2) 1.01, [4, inf) 0.21.
   No reading of this comparison was fixed before the lead saw the numbers (lead's own statement); the verifier's 857-label J decides. Lead
   fit-convention 2-10 / lobe maxima of the domain rows against c6g2 (for the lead's 21:10Z (ii) reading): dom90g 1.04 ; 0.95, dom300g 1.05 ; 0.99,
   dom9000g 1.03 ; 0.90 (32768 x 640 ; 24576 x 960).
16. c6hF (chain-6 step 42; the equal-budget FREE control of the m <= 250 row: the lead's c6hF_start_shape.npz = the c6gF end (F3, c_l 5.576371155) enriched
   to m <= 250 with zero new coefficients, md5 6b1ea5f9c95481162190ba04e1452c87, 94132 columns; c_l free; 20480 x 1200, inner 2500, check 250, damping 1e-8,
   K = 20750; a control row, not a candidate): started 21:42:32Z (shared GPU throughout), DONE 23:39:43Z (wall 7029 s), total 20750 iterations; objective on
   its 1200-angle rows 1.650394e-06 (start = the c6gF density on the 1200 grid; c6gF read 1.664e-6 on its own 960 grid) -> ends of the linearisations
   8.561052e-07, 7.720346e-07, 7.116316e-07, 6.637155e-07, 6.232718e-07, 5.882265e-07, 5.581450e-07, 5.320814e-07, 5.222043e-07 (per-linearisation falls
   9.8, 7.8, 6.7, 6.1, 5.6, 5.1, 4.7 percent, then +750 its 1.9 percent) -> 5.222043e-07 (ratio 0.316 to the start). c_l 5.576371155 -> 5.576370556 at the
   last linearisation (drift -6.0e-7 over the run, monotone from the second linearisation on; below the 1e-4 of the lead's 12:02Z rule, so no slope is
   resolved; the free continuation c6gF (m <= 200) drifted +2.2e-7, and seg3g (m <= 150) +6.895e-6 over its full run from 5.576364040 to 5.576370935, or -4.4e-7 after its first linearisation). Shape leadcode/gpu/c6hF/c6hF_shape.npz, md5
   b8a9a3fc6407dafff29ad5b92bfe87b6 (mtime 23:39:42Z). EQUAL-COUNT COMPARISON c6h (fixed c_l 5.5753626, item 14) / c6hF (free, c_l 5.57637): start
   0.973 (inherited from the starts c6g / c6gF on the 1200 grid), then 0.9826, 0.9858, 0.9884, 0.9901, 0.9917, 0.9932, 0.9948, 0.9963, 0.9970 at the nine
   linearisation ends, 0.974 to 0.997 over all 83 shared check points: the fixed-c_l arm is lower at every count, by 1.7 percent after the first
   linearisation and 0.3 percent at the end, i.e. the gap closes along the run (on m <= 150 the same pair gave 3.8 percent, on m <= 200 2.7-4 percent with the
   gap constant). Both arms end still falling (4.5 and 4.7 percent over their last complete 2500-iteration blocks; 1.8 and 1.9 percent over the final 750 iterations), so neither is converged for the basis. Read by the lead's 12:02Z pair
   rule against c6h on the verifier's rows (whole-box N_f, near-P N_f, N_v r <= 1000 and r > 1000, 857-label J), for the record: the candidate is X3 whatever
   it shows (lead 15:14Z item 4, 23:11Z item 3). Chain 6 went on to step 37 fxm2g at 23:39:43Z (20480 x 720, 21500 its); 47 c6gR4 at ~15000 its at 23:45Z.
   GPU time after step 48: the lead chose (23:22Z) dom9000g2 = dom9000g continued 20750 its at its fixed c_l on its own rows to 9000 L (budget row of the 9000 L
   domain column; reading fixed in advance: far band 1000 L-9000 L and C_R ratios dom9000g2 / dom9000g on both N >= 16875 configurations, in [0.8, 1.25] =
   "the budget does not lower the 9000 L row's far band further", at most 0.5 = "falls further with the iterations", else stated; near-P N_f and J stated);
   chain 7e (gpu_chain7e.sh, pid 2500282, launched 23:43:42Z) runs it as step 49 after the done line of 48.
   MY CROSS-CHECK SCANS (lead convention quick_scan_fit, closure at R_shape 1000; 32768 x 640 ; 24576 x 960; JSONs leadcode/gpu/c6h*/c6h*_scan_<grid>.json;
   2026-10-18T23:48:20Z), c6hF / c6h: 2-10 N_f 4.792e-7 / 4.754e-7 = 1.008 ; 5.047e-7 / 5.088e-7 = 0.992 (both maxima at the lobe above P, r 8.73, theta 0.194, on both
   fits and both grids), 2-10 N_v 1.008 ; 0.992, 0.1-2 1.013 ; 1.012, 10-100 1.014 ; 1.014, 100-1000 0.996 ; 0.996, r > 1000 1.009 ; 1.009, whole-box rms
   1.003 ; 1.003; h(P) - 1 -8.9e-9 / -9.0e-9 ; -5.2e-9 / -5.4e-9; x* 8.600844 (c6hF) against 8.600064 (c6h; the free arm's c_l 5.57637 moves P by 7.8e-4 as
   on m <= 200); centre E, D2 8.0e-10, 2.0e-9 against 5.6e-10, 1.7e-9. So on my scans the m <= 250 pair is a tie to about 1 percent: the fixed arm is lower at
   the lobe by 0.8 percent on 32768 x 640 and higher by 0.8 percent on 24576 x 960, lower by 1.3-1.4 percent in the 0.1-2 and 10-100 bands and by 0.9 percent
   beyond r = 1000, higher by 0.4 percent in 100-1000; against c6g the whole-box maxima of both arms are 0.69 of X3's whole-box maximum (which sits next to P, not at the lobe); lobe to lobe the ratios are 0.988 (c6h) and 0.996 (c6hF) on 32768 x 640; the 0.1-2, 10-100 and 100-1000 bands are 0.37-0.45 of X3's and the outer quick-scan band (physical r from 1000 = 131 L to the closure radius) 0.76-0.77. The 12:02Z rule
   is decided on the verifier's rows; by its letter the outcome here depends on the configuration (whole-box N_f lower on one grid, higher on the other),
   on these scans the two arms agree to about 1 percent in the whole-box and 2-10 quantities with differences of both signs, where at m <= 150 and 200 the fixed arm was lower in most interior bands but not all (s2g / seg3g 0.91 whole box, 0.93 lobe, 0.96-0.98 in the 0.1-2 to 100-1000 bands, 1.07 in the outer band; c6g / c6gF 0.94 whole box, 0.99 lobe, 0.98 in the bands, 1.00 outer; same tool, 32768 x 640). VERIFIER G104 FINAL (00:41Z): by the letter of the 12:02Z rule the FREE control c6hF wins the pair (c6h's whole-box N_f is lower only at 16875 x 768), on differences of 0.3-1.2 percent inside both the configuration spread (15 percent) and the radial-phase spread (9-10 percent) of that maximum, so the pair is not resolved in the deciding quantity; the other quantities point both ways: c6hF lower next to P (3-11 percent, inside the phase spread) and beyond r = 1000 (0.1-0.4 percent, beyond the A5 spread), c6h lower in the 857-label J (2-3 percent, beyond the J spread); the verifier's wording for the report is quoted in G104 (c). Neither changes the candidate (decided at m <= 200, G74).

17. c6gR4 (chain-7c step 47; the inverse-domain control of the candidate: c6g continued at the fixed c_l with the same fitted radial extent (rows r < 900 L; 21363 of the 24576 log-radial points, so the radial quadrature changes with the grid) and the inverse domain and two-term closure moved from 1000 L to 1e4 L by --inverse-radius 10000 --fit-radius 900 (the saved shape
   carries R_shape 1e4), 24576 x 960, inner 2500, check 250, damping 1e-8, K = 20750; a control row, not a candidate; reading fixed by the lead 18:04Z item 5:
   "~ c6g" = ratio in [0.8, 1.25] on both N >= 16875 configurations of the verifier, "falls" = at most 0.5 on both, and C_R at the axis as for the 9000 L row):
   started 22:23:35Z (shared GPU throughout), DONE 2026-10-19T00:10:38Z, total 20750 iterations; objective on its rows 1.827377e-06 (the c6g density read on
   this configuration; 1.619270e-06 on c6g's own: the same density read with the inverse radius, closure and radial quadrature changed gives an objective 12.85 percent higher; the two objectives are different functionals, so this does not by itself isolate an adaptation to the closure) -> ends of the linearisations 1.559832e-06, 1.507644e-06, 1.460714e-06, 1.418894e-06, 1.379693e-06, 1.344342e-06,
   1.312481e-06, 1.283177e-06, 1.280057e-06 (the first linearisation lowers the new objective by 14.6 percent; then falls 3.3, 3.1, 2.9, 2.8, 2.6, 2.4, 2.2
   percent per linearisation, then 0.24 over the last 750) -> 1.280057e-06 (ratio 0.700 to its start; 1.013 x c6g2's 1.263892e-06, which has the same rows and
   budget on the 1000 L inverse but a different radial quadrature, so the two objectives are not the same functional). c_l 5.575362610642 (fixed). Shape
   leadcode/gpu/c6gR4/c6gR4_shape.npz, md5 766635b1d02ed77331131741ecc91d87 (mtime 00:10:37Z).
   MY CROSS-CHECK SCANS (quick_scan_fit, 32768 x 640 ; 24576 x 960, closure at the SAVED R_shape, so 1e4 L for c6gR4 and dom9000g and 1000 L for c6g and
   c6g2; JSONs leadcode/gpu/<tag>/<tag>_scan_<grid>.json, table runs/c6gR4_crosscheck_table.txt, 2026-10-19T00:19:47Z). (a) INTERIOR, c6gR4 / c6g2 (same fitted radial extent and budget; inverse 1000 L -> 1e4 L with the radial grid 20480 -> 24576): 2-10 x-strip 1.024 ; 1.037, 2-10 middle (lobe above P) 1.025 ; 0.892, 2-10 y-strip
   1.040 ; 1.041, 2-10 N_v 1.025 ; 0.891, 0.1-2 1.002 ; 1.002, 10-100 0.976 ; 0.977, 100-1000 1.016 ; 1.015: the whole-box and band maxima change by at most 4 percent except at the lobe above P, where the ratio is 1.025 on one grid and 0.892 on the other (an 11 percent change) (the lobe moves with the radial
   sampling by 9-12 percent, verifier G101; c6g2 reads 4.860e-7 ; 5.295e-7 there, c6gR4 4.983e-7 ; 4.721e-7). Against c6g: x-strip next to P 0.523 ; -,
   lobe 1.036, N_v 0.749, 0.1-2 0.866, 10-100 0.946, 100-1000 0.770 (32768 x 640), the same as c6g2's 0.511 / 1.010 / 0.731 / 0.865 / 0.970 / 0.758: the interior changes of c6gR4 relative to c6g are those of the budget row to within these margins (verifier G108: whole-box A5 within 0.6 percent of c6g2's, near P 0.8-1.6 percent, J 5.5-8 percent HIGHER, the 10-100 band 0.89). Whole-box maximum at the lobe (r 8.735, theta 0.194) on both grids, as c6g2 and dom9000g. h(P) - 1 -8.1e-9 ; +1.0e-12 (c6g -8.8e-9 on 32768 x 640; the lead's 24576 x 960 scan of c6g gives -5.3e-9, no scan of mine); centre E -2.8e-10 (start) ... (b) OUTER quick-scan BAND (the quick_scan band edges are PHYSICAL radii: this band runs from physical r = 1000, i.e. 131 L, to the saved closure radius, here 1e4 L) in the common 1e4 L closure, c6gR4 against dom9000g (same inverse domain and closure; rows to 900 L against 9000 L): N_f max 1.320e-7 ; 1.324e-7 against 1.149e-8 ; 1.156e-8 (11.5 x), N_v max 2.934e-7 ; 2.939e-7 against 3.213e-8 ; 3.222e-8 (9.1 x); c6gR4's N_f maximum at r 4257 L (32575 physical), theta 0.844 on the first grid (the N_v maximum is at another angle; verifier G108 puts it at 4279-4382 L, theta 0.643), dom9000g's at its closure radius.
   So with the inverse domain and the closure at 1e4 L held fixed, extending the fitted rows from 900 L to 9000 L lowers the outer maximum by a further order of magnitude; the attribution relative to X3 needs the matched formula-continued comparison (lead and verifier readings below), which shows that the inverse-domain change itself lowers the 1000 L-9000 L band to 0.27 of X3's (c6g2 showed that the budget alone does not move it). The
   ratio of c6gR4's far band to c6g's in the lead's reading (formula continued globally, N_v, on the verifier's N >= 16875 configurations) is the
   verifier's; the quick_scan outer bands of c6g (131 L to 1000 L) and c6gR4 (131 L to 1e4 L) are not the same region, so no "~ c6g" / "falls" reading is made from them here. Whole-box rms 1.840e-8 against c6g's 7.05e-9 and dom9000g's 5.28e-9 is dominated by the exterior region of the larger inverse domain (not comparable
   with c6g's). Step 48 dom9000gF waits for the done line of 40 (chain 6 at step 37 since 23:39:43Z); step 49 dom9000g2 after 48 (chain 7e).
   LEAD'S CROSS-CHECK (NOTES_FOR_TEAM 2026-10-19T00:21:41Z; lead tools, formula continued to 1e6 L, 24576 x 576; the report takes the verifier's): c6gR4 / X3
   over 1000 L-9000 L 0.268 (A5 0.272), 9000 L-1e4 L 0.248, beyond 1e4 L 0.241 (dom9000g 0.029 / 0.025 / 0.035; c6g2 1.000); C_R at the axis -0.024 of X3's
   (sign reversed; dom9000g 0.035); series coefficients next to the y-axis q1 -4.3e-4 against X3's +1.58e-2, q3 -4.4e4 against +1.19e5, qh equal. On the
   lead's numbers the row is the "falls" branch of the 18:04Z item 5 rule (ratio at most 0.5): the inverse domain alone lowers the far band to about 0.27 of
   X3's and the 9000 L row's fall (0.03) is therefore not attributable to its rows alone; the lead's prepared 4.5 wording: "the further iterations alone do not
   move the band (c6g2), the larger inverse domain alone lowers it (c6gR4), and the fall of the 9000 L row is not attributable to its rows alone". My
   own-convention N_v maximum of c6gR4 over 1000 L-1e4 L (2.934e-7, (b) above) is 0.269 of X3's formula-continued band maximum 1.092e-6 (G80 / lead band_nv), the same ratio, although the regions and conventions differ; the chain of successive ratios X3 (1.09e-6) -> c6gR4 (inverse domain 1e4 L: x 0.27) -> dom9000g (rows to 9000 L: x 0.10-0.11) multiplies to the measured 0.028-0.029 of X3's band maximum (verifier G108: 0.2662 / 9.17 and 0.2686 / 9.68 on the matched configurations). (2026-10-19T00:27:56Z)
   VERIFIER G108 (00:56Z) on c6gR4: far band 1000 L-9000 L c6gR4 / X3 0.266-0.273 on both N >= 16875 configurations (formula continued, N_v; absolute 2.933e-7 /
   2.938e-7 against X3's 1.102e-6 / 1.094e-6; the maximum off the y-axis at theta 0.64, where X3's is next to the axis): "falls" by the rule in force, CONFIRMED,
   agreeing with the lead's 0.268 / 0.272 to 1 percent; c6gR4 / dom9000g 9.2-9.7 (my 9.1 in the common closure "the same order"); C_R -0.024 of X3's; series q1
   -0.027, q2 0.11, q3 -0.37 of X3's; interior against c6g2: A5 whole box 1.002 / 0.999 / 1.006, within 0.5 of P 1.008-1.016, 857-J 1.055 / 1.080, residual map
   windows within 0.97-1.06 of c6g2's: "the interior does not see the inverse-domain change" (my (a): within 4 percent). (2026-10-19T01:04:06Z)

18. fxm2g (chain-6 step 37; the first of the fixed-c_l profile rows 37-40 on the 375 x m <= 150 basis (c6f lineage): nominal transplant offset d = -2e-3 from F0's 5.5763624, stored c_l 5.5743631487 (the transplant carries 5.5763624 + d + 0.18 d^2, verifier G112 (a); d labels a parameter-space transplant, not an exact exponent displacement), start = the lead's transplant fxm_-2.0e-03_shape.npz (F0 + d t, md5 a39a2c7004e1b96ebdf25752b793fc71), 20480 x 720, inner 2500, check 250,
   damping 1e-8, K = 21500 = the budget of F2 (seg3g: F0 + 750 + 20750 free, L2 4.258616e-06, c_l 5.576370935); reference rows F2 and X2 = s2g (d = -1e-3,
   L2 4.096686e-06); readings fixed by the lead at 00:25:51Z, before the run was done: (a) "not determined at this level" if L2 within 30 percent of F2's,
   whole-box N_f (A5) within 30 percent of F2's on each verifier configuration and |h(P) - 1| <= 1e-6; (b) "excluded at this level" if flattened (L2 change
   < 2 percent over the last 1000 its) and the near-P N_f at least 2 x F2's on each configuration; (c) otherwise undecided; (a) and (c) widen the quoted c_l
   interval (SPEC v4.5), (b) does not): started 23:39:43Z (shared until 00:10Z, then alone), DONE 2026-10-19T00:38:32Z, total 21500 iterations; objective
   1.466063e-05 (the transplant on the 720 grid) -> ends of the linearisations 5.638757e-06, 4.492573e-06, 4.184357e-06, 4.079442e-06, 4.028408e-06,
   3.997453e-06, 3.973826e-06, 3.953981e-06, 3.944751e-06 (falls 20.3, 6.9, 2.5, 1.3, 0.8, 0.6, 0.5 percent per linearisation, then 0.23 over the last 1500;
   -0.14 percent over the last 1000 its: FLATTENED by the lead's clause) -> 3.944751e-06 = 0.926 x F2's L2 and 0.963 x X2's. Shape
   leadcode/gpu/fxm2g/fxm2g_shape.npz, md5 5ac32e3170621f73cce85698613aa9b4 (mtime 00:38:31Z).
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960; the F2 / X2 values from the same tool at 32768 x 640, leadcode/gpu/seg3g, s2g): whole-box
   N_f 1.385e-6 ; 1.440e-6 (next to P, r 8.467, theta 0.010) against F2 1.585e-6 and X2 1.444e-6 (0.87 and 0.96 of them), lobe above P 8.88e-7 ; 9.24e-7
   (F2 1.030e-6, X2 9.60e-7), 2-10 N_v 3.87e-7 ; 4.02e-7 (F2 4.42e-7, X2 4.03e-7), 0.1-2 6.70e-8 (7.13e-8, 6.95e-8), 10-100 2.01e-7 (2.07e-7, 2.01e-7), 100-1000
   2.77e-8 ; 2.84e-8 (2.95e-8, 2.82e-8); h(P) - 1 -8.2e-9 ; -5.2e-9; x* 8.599290 (-7.74e-4 relative to X2's 8.600064, -1.55e-3 relative to F2's 8.600844).
   So on my scans the row at c_l = 5.5744 (2.0e-3 below F0, 1.0e-3 below X2 / X3's fixed value) meets every clause of reading (a): L2 within 7.4 percent of F2's
   (lower), whole-box N_f 13 percent below F2's and 4 percent below X2's on 32768 x 640 (0.872 and 0.952 on 24576 x 960 against the matched F2 / X2 scans run later, 2026-10-19T04:04:16Z), |h(P) - 1| < 1e-8; it is also flattened, but its near-P N_f is 0.87 x
   F2's, not 2 x, so (b) does not apply: "not determined at this level", which by SPEC v4.5 widens the c_l interval downward to include 5.5744. On these
   scans the fixed-c_l residual over d = -2e-3, -1e-3 (X2), 0 (F2 free) is monotone DEcreasing toward smaller c_l at equal budget (1.385e-6, 1.444e-6, 1.585e-6
   whole-box; 0.926, 0.962, 1 in L2), consistent with the lane's finding 3.16 item 4d (a flat valley in c_l at the residual levels reached, with the slope
   toward smaller c_l at this basis) and with the lead's corrected linear-model calculation (analysis 13.13: factor-two offset bound at least 8.9e-3, with no nonlinear resolution inferred; the earlier 13.12 statement was corrected by the lead). Rows 38 (+2e-3), 39 (+2.4e-2), 40 (+3e-3)
   complete the profile; the verifier's rows decide each reading. (2026-10-19T00:41:57Z)
   VERIFIER G109 (01:15Z) on fxm2g: own evaluator at 11250 x 384 / 16875 x 512, L2 0.926, whole-box N_f (A5) 1.3616e-6 / 1.3678e-6 = 0.865 / 0.869 of F2's, N_v
   r <= 1000 0.865 / 0.869, 857-label J 0.865 / 0.859, h(P) - 1 +2.8e-7 / +1.1e-8, identity c_l -3.2e-9, flattened (-0.145 percent per 1000 its): reading (a)
   "not determined at this level" CONFIRMED; it widens the c_l interval of (iv) down to 5.5743631; "the objective is still falling toward smaller c_l at d = -2e-3,
   so the lower end of the tested span is not bracketed by this row" (rows 52, 53 requested by the lead, NOTES 01:07:09Z). My scan values agree with the
   verifier's to 1-2 percent (1.385e-6 against 1.362e-6 / 1.368e-6; same ratios to F2 to 1 percent). (2026-10-19T01:28:08Z)

19. fxu2g (chain-6 step 38; profile row d = +2e-3: c_l fixed at 5.5783631481, start = the lead's transplant fxu_+2.0e-03_shape.npz (F0 + d t, md5
   e4f451ca440249084cfb708edf8a9323), 20480 x 720, inner 2500, check 250, damping 1e-8, K = 21500; references and readings as in item 18): started 00:38:32Z
   (alone), DONE 01:24:02Z, total 21500 iterations; objective 9.969608e-06 -> ends of the linearisations 5.084488e-06, 4.802688e-06, 4.730930e-06, 4.695796e-06,
   4.669807e-06, 4.646253e-06, 4.624320e-06, 4.602844e-06, 4.590838e-06 (falls 5.5, 1.5, 0.7, 0.6, 0.5, 0.5, 0.5 percent per linearisation, then 0.26 over the
   last 1500; -0.15 percent over the last 1000 its: FLATTENED) -> 4.590838e-06 = 1.078 x F2's L2 and 1.121 x X2's. Shape leadcode/gpu/fxu2g/fxu2g_shape.npz,
   md5 55937d343186869e3cc02618784a1dae (mtime 01:24:01Z).
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960): whole-box N_f 1.799e-6 ; 1.876e-6 (next to P, r 8.495, theta 0.010) against F2 1.585e-6
   and X2 1.444e-6 (1.135 and 1.246 of them), lobe 1.179e-6 ; 1.226e-6 (F2 1.030e-6), 2-10 N_v 5.03e-7 ; 5.24e-7 (F2 4.42e-7), 0.1-2 7.47e-8 (7.13e-8), 10-100
   2.16e-7 (2.07e-7), 100-1000 3.19e-8 ; 3.28e-8 (2.95e-8); h(P) - 1 -6.2e-9 ; -3.5e-9; x* 8.602387 (+1.54e-3 relative to F2's 8.600844). Reading (a) on these numbers: L2 within 7.8 percent of F2's and whole-box N_f within 14 percent (13.5 percent on 24576 x 960 against the matched F2 scan), both HIGHER, |h(P) - 1| < 1e-8:
   "not determined at this level"; (b) does not apply (flattened, but near-P N_f 1.14 x F2's, not 2 x). THE PROFILE SO FAR at equal budget on the 375 x m <= 150
   basis (python3 leadcode/gpu/profile_table.py; L2 from the chain logs, scans at 32768 x 640): d = -2e-3 / -1e-3 (X2) / 0 (F2, free) / +2e-3: L2 / F2 0.926 /
   0.962 / 1.000 / 1.078; whole-box N_f 1.385 / 1.444 / 1.585 / 1.799 e-6; lobe 0.888 / 0.960 / 1.030 / 1.179 e-6; 2-10 N_v 3.87 / 4.03 / 4.42 / 5.03 e-7; 10-100
   2.01 / 2.01 / 2.07 / 2.16 e-7; 100-1000 2.77 / 2.82 / 2.95 / 3.19 e-8; h(P) - 1 -8.2 / -7.4 / -6.8 / -6.2 e-9; x* 8.59929 / 8.60006 / 8.60084 / 8.60239. Every listed quantity increases with c_l over the 4e-3 span (L2 secant slopes 3.6-3.9 percent of F2 per nominal 1e-3; whole-box N_f secant slopes nonuniform, 3.7-8.9 percentage points of F2 per 1e-3), and every row is
   within 30 percent of F2 in L2 and in whole-box N_f, i.e. "not determined" by reading (a): at this basis and budget the pre-registered diagnostic does not separate the tested exponents in [5.5744, 5.5784] (consistent with the lane's 3.16 item 4d finding at the 1e-6 level, there on this lane's own solver), and the smallest observed objective is at the lowest tested exponent (finite-budget fits; no minimum is located). Rows 39 (+2.4e-2 = 5.6005) and 40 (+3e-3) follow; the verifier's rows decide each reading. (2026-10-19T01:27:38Z)
   VERIFIER G111 (01:38Z) on fxu2g: L2 1.078, whole-box N_f (A5) 1.7913e-6 / 1.7921e-6 = 1.138 / 1.138 of F2's (11250 x 384 / 16875 x 512), N_v r <= 1000
   1.140 / 1.140, 857-label J 1.159 / 1.160, h(P) - 1 +8.2e-8 / +2.2e-8, identity c_l -3.2e-9, flattened (-0.150 percent per 1000 its): reading (a) "not
   determined at this level" CONFIRMED; it widens the c_l interval of (iv) up to 5.5783631. Profile over d = -2e-3 ... +2e-3 monotone increasing in every
   quantity (L2 0.926, 0.962, 1, 1.078; whole-box 0.87, 0.91, 1, 1.14; J 0.865, 0.921, 1, 1.159); L2^2 convex in d (the quadratic through the first three
   points predicts +2e-3 to 0.8 percent); "a statement about fits at one budget from transplanted starts; it does not locate an exponent". My scan values agree
   with the verifier's to 0.5 percent (1.799e-6 against 1.791e-6 / 1.792e-6). The lead's lower-end rows 52 fxn4g (d = -4e-3) and 53 fxn8g (-8e-3, conditional)
   were requested at 01:07:09Z (item 21 below). (2026-10-19T01:40:19Z)

20. fxv24g (chain-6 step 39; profile row d = +2.4e-2: c_l fixed at 5.6004661644 (the SPEC v4.5 test value "5.60"), start = the lead's transplant
   fxv_+2.4e-02_shape.npz (F0 + d t, md5 0da3b3b002825328f6ad08d3b0c3ce29), 20480 x 720, inner 2500, check 250, damping 1e-8, K = 21500; references and
   readings as in item 18; in addition the lead's Q rule (00:25:51Z item 3): Q(375) = L2(fxv24g) / 4.259e-6, (P2) favoured only if Q >= 2.96, (P1) favoured
   only if Q <= 0.91, otherwise undecided, and undecided if the row still falls by more than 2 percent per 250 iterations at its end; it decides only the 4.8
   wording): started 01:24:02Z (shared with fxn4g from 01:29Z), DONE 02:31:56Z, total 21500 iterations; objective 9.463257e-04 (the transplant by 2.4e-2 in c_l is
   far from the equation) -> ends of the linearisations 2.146539e-05, 1.241783e-05, 1.026005e-05, 9.530358e-06, 9.214141e-06, 9.008542e-06, 8.864979e-06,
   8.743401e-06, 8.671252e-06 (falls 42.1, 17.4, 7.1, 3.3, 2.2, 1.6, 1.4 percent per linearisation, then 0.83 over the last 1500; -0.49 percent over the last
   1000 its and -0.09 over the last 250: FLATTENED) -> 8.671252e-06 = 2.036 x F2's L2. Shape leadcode/gpu/fxv24g/fxv24g_shape.npz, md5
   f0b98ad7d780f0baffc990f577287be4 (mtime 02:31:55Z).
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960): whole-box N_f 4.613e-6 ; 4.789e-6 (next to P, r 8.53, theta 0.010) = 2.91 ; 3.02 x F2's
   1.585e-6 (3.19 x X2's), lobe 2.99e-6 ; 3.16e-6 (F2 1.03e-6), 2-10 N_v 1.29e-6 ; 1.34e-6 (F2 4.42e-7), 0.1-2 1.11e-7 (7.13e-8), 10-100 3.42e-7 (2.07e-7),
   100-1000 5.70e-8 ; 5.89e-8 (2.95e-8); h(P) - 1 +2.0e-8 ; +1.0e-8; x* 8.619483 (+1.86e-2 relative to F2). Readings
   on these numbers: (a) fails (L2 2.04 x F2, whole-box N_f 2.9-3.0 x); (b) holds: flattened AND near-P N_f >= 2 x F2's on both grids: "EXCLUDED at this level"
   (the verifier's configurations decide); so c_l = 5.6005 does not widen the interval; the upper end of the tested span lies between the largest not-excluded tested value (+3e-3, item 22) and this excluded one, with the intervening untested exponents unsettled. Q rule: Q(375) = 2.036, between 0.91 and 2.96, end fall 0.09 percent per 250 its: UNDECIDED (neither (P1) nor (P2)
   favoured by the lead's settlement). The excess over F2 is largest next to P (x-strip 2.9 x, lobe 2.9 x, N_v 2.9 x) and smaller away from it (10-100 1.66 x, 100-1000 1.93 x, 0.1-2 1.56 x; outer quick-scan band 1.14 x); h(P) - 1 itself is 2e-8 (the fit imposes the h(P) row). (2026-10-19T02:34:31Z)
   VERIFIER G114 (02:45Z) on fxv24g: L2 2.036, whole-box N_f (A5) 4.5870e-6 / 4.5895e-6 = 2.915 / 2.914 of F2's (11250 x 384 / 16875 x 512), N_v r <= 1000
   2.928 / 2.927, 857-label J 2.871 / 2.938, h(P) - 1 -1.07e-6 / -2.45e-7, identity c_l -3e-9, flattened (-0.486 percent per 1000 its): (a) fails, (b) holds on both
   configurations: "EXCLUDED at this level" CONFIRMED; it does not widen the interval; the upper end of the tested span lies between 5.5783631 (row 38) and
   5.6004662, row 40 to come. Q(375) = 2.036 "undecided" CONFIRMED. My scan values agree with the verifier's to 0.6 percent (4.613e-6 against 4.587e-6 / 4.590e-6).
   (2026-10-19T02:53:42Z)

21. fxn4g (chain-8 step 52; the first lower-end profile row requested by the lead at 01:07:09Z after rows 37 / 38 came out monotone: d = -4e-3, c_l fixed at
   5.5723652993 (stored; the transplant carries 5.5763624 + d + 0.18 d^2, verifier G112 (a)), start = the lead's transplant fxn_-4.0e-03_shape.npz (F0 + d t, md5
   16ecb489873b70843b930050da2b293b), 20480 x 720, inner 2500, check 250, damping 1e-8, K = 21500; references and readings as in item 18): started 01:29:03Z
   (22 minutes after the request; shared GPU with chain 6 throughout), DONE 02:40:41Z, total 21500 iterations; objective 3.549406e-05 -> ends of the linearisations
   7.114261e-06, 4.801661e-06, 4.110183e-06, 3.876216e-06, 3.775893e-06, 3.723675e-06, 3.690068e-06, 3.665228e-06, 3.654235e-06 (falls 32.5, 14.4, 5.7, 2.6, 1.4,
   0.9, 0.7 percent per linearisation, then 0.30 over the last 1500; -0.19 percent over the last 1000 its: FLATTENED) -> 3.654235e-06 = 0.858 x F2's L2 and 0.926 x
   fxm2g's (3.944751e-06). Shape leadcode/gpu/fxn4g/fxn4g_shape.npz, md5 9d5ddd3a89d904d4d539c0eb37ebf4b4 (mtime 02:40:10Z). Since L2 < 3.944751e-6 the lead's
   01:07Z condition for row 53 holds: chain 8b started 53 fxn8g (d = -8e-3, c_l 5.5683738938) at 02:40:41Z in the same slot (lead 01:48:00Z order), end ~03:50Z.
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960): whole-box N_f 1.147e-6 ; 1.191e-6 (next to P, r 8.465, theta 0.010) = 0.723 x F2's 1.585e-6 on 32768 x 640 and 0.721 x F2's 1.652e-6 on 24576 x 960 (0.83 x fxm2g's), lobe 7.27e-7 ; 7.58e-7 (F2 1.03e-6), 2-10 N_v 3.20e-7 ; 3.33e-7 (F2 4.42e-7), 0.1-2 6.41e-8 (7.13e-8), 10-100 1.875e-7 (2.07e-7),
   100-1000 2.52e-8 ; 2.58e-8 (2.95e-8); h(P) - 1 -9.2e-9 ; -6.0e-9; x* 8.597743 (-3.10e-3 relative to F2). Reading (a) on these numbers: L2 within 14
   percent of F2's and whole-box N_f within 28 percent, both LOWER, |h(P) - 1| < 1e-8: "not determined at this level" (b does not apply: near-P N_f 0.72 x F2);
   it widens the interval down to 5.5723653. THE PROFILE (profile_table.py; d = -4e-3 / -2e-3 / -1e-3 / 0 / +2e-3 / +2.4e-2): L2 / F2 0.858 / 0.926 / 0.962 / 1.000 /
   1.078 / 2.036; whole-box N_f 1.147 / 1.385 / 1.444 / 1.585 / 1.799 / 4.613 e-6; lobe 0.727 / 0.888 / 0.960 / 1.030 / 1.179 / 2.992 e-6; N_v 3.20 / 3.87 / 4.03 /
   4.43 / 5.03 / 12.9 e-7; 10-100 1.875 / 2.01 / 2.01 / 2.07 / 2.16 / 3.42 e-7; h(P) - 1 -9.2 / -8.2 / -7.4 / -6.8 / -6.2 / +20 e-9. L2 and whole-box N_f increase with c_l across all listed rows (L2 secant slopes per nominal 1e-3: 3.4 percent of F2 between -4e-3 and -2e-3, 3.6 between -2e-3 and -1e-3, 3.8 between -1e-3 and 0, 3.9 between 0 and +2e-3; convexity of the optimised objective is not established, see item 22; verifier G111 discussed L2^2 on the first four rows); the smallest observed objective is at the lowest tested exponent, so the lower end of the tested span is not bracketed; row 53 at 5.5684 tests whether it turns before -8e-3. (2026-10-19T02:43:19Z)
   VERIFIER G115 (02:57Z) on fxn4g: L2 0.858, whole-box N_f (A5) 1.1194e-6 / 1.1225e-6 = 0.711 / 0.713 of F2's, N_v r <= 1000 0.711 / 0.713, 857-label J 0.707 /
   0.699, h(P) - 1 +3.6e-7 / -1.8e-10, identity c_l -3e-9, flattened (-0.187 percent per 1000 its): reading (a) "not determined at this level" CONFIRMED; the interval
   of (iv) widens down to 5.5723653; "the whole-box and J ratios fall faster there than between -2e-3 and 0 (0.71 against 0.87); the lower end is not bracketed by
   this row"; "fits from transplanted starts at one budget; they do not locate an exponent". My first-grid scan value agrees with the verifier's to 2.5 percent (1.147e-6 against 1.119e-6 / 1.123e-6). (2026-10-19T03:02:30Z)

22. fxu3g (chain-6 step 40, the last of chain 6; profile row d = +3e-3: c_l fixed at 5.5793640451 (stored), start = the lead's transplant fxu_+3.0e-03_shape.npz
   (F0 + d t, md5 769f9d0194cc69db597f2c017d04472c), 20480 x 720, inner 2500, check 250, damping 1e-8, K = 21500; references and readings as in item 18): started
   02:31:56Z (shared with 52 / 53 throughout), DONE 03:32:54Z, total 21500 iterations ("chain6 end" 03:32:54Z; step 48 dom9000gF started 03:33:32Z from chain 7d);
   objective 1.651552e-05 -> ends of the linearisations 5.138422e-06, 4.939212e-06, 4.897541e-06, 4.866675e-06, 4.839626e-06, 4.813598e-06, 4.789038e-06,
   4.764488e-06, 4.748455e-06 (falls 3.9, 0.8, 0.6, 0.6, 0.5, 0.5, 0.5 percent per linearisation, then 0.34 over the last 1500; -0.18 percent over the last 1000
   its: FLATTENED) -> 4.748455e-06 = 1.115 x F2's L2 and 1.034 x fxu2g's. Shape leadcode/gpu/fxu3g/fxu3g_shape.npz, md5 40584466fe24712f2f66af4fb38d6f6d (mtime
   03:32:53Z).
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960): whole-box N_f 1.919e-6 ; 2.002e-6 (next to P, r 8.50, theta 0.010) = 1.210 x F2's 1.585e-6 on 32768 x 640 and 1.212 x F2's 1.652e-6 on 24576 x 960 (1.067 x fxu2g's), lobe 1.256e-6 ; 1.307e-6 (F2 1.030e-6), 2-10 N_v 5.37e-7 ; 5.59e-7 (F2 4.42e-7), 0.1-2 7.61e-8 (7.13e-8), 10-100 2.20e-7 (2.07e-7),
   100-1000 3.30e-8 ; 3.39e-8 (2.95e-8); h(P) - 1 -5.9e-9 ; -3.3e-9; x* 8.603161 (+2.32e-3 relative to F2). Reading (a) on these numbers: L2 within 12 percent of F2's and whole-box N_f within 21 percent (matched grids), both HIGHER, |h(P) - 1| < 1e-8: "not determined at this level" (b does not apply: near-P N_f 1.21-1.26 x
   F2, not 2 x); it widens the interval up to 5.5793640, so the upper end of the tested span lies between +3e-3 (not excluded) and +2.4e-2 (excluded, item 20).
   THE PROFILE with rows 37-40 and 52 complete (profile_table.py; d = -4e-3 / -2e-3 / -1e-3 / 0 / +2e-3 / +3e-3 / +2.4e-2): L2 / F2 0.858 / 0.926 / 0.962 / 1.000 /
   1.078 / 1.115 / 2.036; whole-box N_f 1.147 / 1.385 / 1.444 / 1.585 / 1.799 / 1.919 / 4.613 e-6; lobe 0.727 / 0.888 / 0.960 / 1.030 / 1.179 / 1.256 / 2.992 e-6; N_v 3.20 / 3.87 / 4.03 / 4.42 / 5.03 / 5.37 / 12.9 e-7; 10-100 1.875 / 2.01 / 2.01 / 2.07 / 2.16 / 2.20 / 3.42 e-7; h(P) - 1 -9.2 / -8.2 / -7.4 / -6.8 / -6.2 / -5.9 /
   +20 e-9; x* 8.59774 / 8.59929 / 8.60006 / 8.60084 / 8.60239 / 8.60316 / 8.61948. L2 and whole-box N_f increase with c_l across all rows (L2 secant slopes per nominal 1e-3 between -4e-3 and +3e-3: 3.4, 3.6, 3.8, 3.9, 3.7 percent of F2, so the sampled L2 is NOT convex over the full set; whole-box N_f secant slopes 3.7-8.9 percentage points of F2 per 1e-3, nonuniform); the six rows from -4e-3 to +3e-3 are all "not determined"
   ((a)) and only +2.4e-2 is excluded ((b)). Row 53 (d = -8e-3) is at L2 3.18e-6 (0.747 x F2) at 20000 of 21500 its, still below row 52, so row 54 (-1.6e-2) will
   run (lead 03:13:52Z). (2026-10-19T03:37:15Z)
   VERIFIER G118 (03:48Z) on fxu3g: L2 1.115, whole-box N_f (A5) 1.9087e-6 / 1.9112e-6 = 1.213 / 1.214 of F2's, N_v r <= 1000 1.214 / 1.215, 857-label J 1.224 /
   1.226, h(P) - 1 +5.5e-8 / +1.9e-8, identity c_l -3e-9, flattened (-0.182 percent per 1000 its): reading (a) "not determined at this level" CONFIRMED; "the
   upper end of the not-excluded range lies between 5.5793640 and 5.6004662 at this level and is not located further by these rows". My scan values agree with the
   verifier's to 0.5 percent (1.919e-6 against 1.909e-6 / 1.911e-6). (2026-10-19T03:56:13Z)

23. fxn8g (chain-8 step 53; the second lower-end profile row: d = -8e-3, c_l fixed at 5.5683738938 (stored), start = the lead's transplant fxn_-8.0e-03_shape.npz
   (F0 + d t, md5 73016a808c5c1797531508c95865d4fa), 20480 x 720, inner 2500, check 250, damping 1e-8, K = 21500; run because L2(fxn4g) < L2(fxm2g) (lead 01:07:09Z
   item 2); references and readings as in item 18): started 02:40:41Z (shared with 40, then 48), DONE 03:41:15Z, total 21500 iterations; objective 1.192224e-04 (the
   transplant by -8e-3) -> ends of the linearisations 1.099890e-05, 6.124539e-06, 4.394408e-06, 3.733687e-06, 3.451839e-06, 3.312059e-06, 3.232629e-06, 3.179941e-06,
   3.157027e-06 (falls 44.3, 28.2, 15.0, 7.5, 4.0, 2.4, 1.6 percent per linearisation, then 0.72 over the last 1500; -0.44 percent over the last 1000 its: FLATTENED
   by the 2 percent clause, but falling 2-3 times faster at its end than rows 37 / 38 / 52 (-0.14 to -0.19)) -> 3.157027e-06 = 0.741 x F2's L2 and 0.864 x fxn4g's.
   Shape leadcode/gpu/fxn8g/fxn8g_shape.npz, md5 1489e81e0d43b3c54a1e470fb5b12a5d (mtime 03:40:46Z). Since L2 < 3.654235e-6 the lead's 03:13:52Z condition holds:
   chain 8e started step 54 fxn16g (d = -1.6e-2, c_l 5.5604082120, start fxn16_-1.6e-02_shape.npz md5 9face47281dca84c1e5256ad50898366, start objective 4.504e-4 on
   the 720 grid) at 03:41:15Z, shared with 48 dom9000gF (end ~04:55Z).
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960): whole-box N_f 6.789e-7 ; 7.066e-7 = 0.428 x F2's on both matched grids (0.59 x fxn4g's), now at r 8.07, theta 0.012, at distance 0.54 from P (outside the registered |X - P| <= 0.5 neighbourhood; the other rows have their maximum 0.12-0.25 from P), so the whole-box value bounds the near-P maximum from above, lobe 5.12e-7 ; 4.98e-7 (F2 1.030e-6:
   0.50 ; 0.48), 2-10 N_v 2.00e-7 ; 2.05e-7 (F2 4.43e-7: 0.45), 0.1-2 5.77e-8 (7.13e-8: 0.81), 10-100 1.934e-7 ; 1.928e-7 (2.07e-7: 0.94, i.e. 3 percent HIGHER than row 52's 1.875e-7), 100-1000 2.35e-8 (2.95e-8: 0.80); outer quick-scan band (physical 1000 to 7651 = 131 L to 1000 L) N_f 1.68 x F2's and N_v 1.57 x (the only band where this row is higher than F2); h(P) - 1 -1.22e-8 ; -8.4e-9; x* 8.594652 (-6.19e-3 relative to F2). READINGS on these numbers: (a) read two-sided ("within 30 percent of F2's")
   FAILS on whole-box N_f (0.43 is 57 percent below F2's) although L2 (0.741) is within 30 percent and |h(P) - 1| <= 1.23e-8 (below the 1e-6 threshold); (b) does not apply (the near-P N_f is at most the whole-box 0.43 x F2, not 2 x); so (c) "undecided at the 375 x m <= 150 level after 21500 iterations" by the letter of the lead's rule, and (a) if "within 30 percent" is
   read as "not more than 30 percent above"; either way the value is NOT excluded and widens the interval of (iv) down to 5.5683739 (SPEC v4.5); the verifier's rows
   decide. THE OBSERVATION: across these finite-budget transplanted fits the whole-box N_f maximum (next to P) decreases with the stored exponent: 4.61 / 1.92 / 1.80 / 1.585 / 1.444 / 1.385 / 1.147 / 0.679 e-6 for d = +2.4e-2 / +3e-3 / +2e-3 / 0 / -1e-3 / -2e-3 / -4e-3 / -8e-3; the fixed-c_l fit at c_l = 5.5684 on the 375 x m <= 150 basis with 21500 iterations reaches the whole-box N_f of the candidate X3 (6.8-7.2e-7 on the verifier's configurations; m <= 200, 42,250 iterations after its F0 transplant, a different basis and optimisation history, so no efficiency comparison is made). Against F2 the physical 10-100 and 100-1000 N_f bands are 0.94 and 0.80 while the outer quick-scan band (131 L-1000 L) is 1.68 (N_f) / 1.57 (N_v): the gain is in the 2-10 band and the row is worse than F2 beyond 131 L; against X3 (finer basis) its 10-100 and 100-1000 bands are 2.37 and 1.43; nothing here measures the formula-global far band. The L2 objective falls less (0.741) than the near-P maximum; which regions dominate the weighted objective is not measured here. Whether the trend turns before d = -1.6e-2 is what row 54 tests; if it does not, the lower end of the tested span stays unbracketed. These are fits at one budget from transplanted starts (verifier G115): the smallest observed objective is at the lowest tested exponent; they do not locate an exponent, and the lane does not claim one. On the lane's reading this is consistent with the softness of c_l found in 3.16 item 4d at the 1e-6 level (there on this lane's own LSQ solver), now seen on the lead's basis: among these fits smaller stored exponents correlate with lower near-P maxima.
   VERIFIER G119 (04:01Z) on fxn8g: L2 0.741 x F2 (0.771 x X2); whole-box N_f (A5) 8.906e-7 / 6.730e-7 = 0.566 / 0.427 of F2's (at 11250 x 384 the maximum is at
   the under-resolved lobe point r 8.78, theta 0.30; at 16875 x 512 on the x-axis side at r 8.03, theta 0.012, 0.56 left of P), within 0.5 of P 0.415 / 0.424,
   N_v r <= 1000 0.563 / 0.453, far N_v 1.106e-6 / 1.120e-6 (the common far band), 857-label J 0.388 / 0.375, h(P) - 1 +4.5e-7 / +2.7e-8, identity c_l -3e-9,
   B_3 IBP median 0.2978: reading (c) "undecided at this level" CONFIRMED by the letter (whole-box 0.57 / 0.43 is outside the 30 percent band on the LOW side; "the
   rule did not anticipate a row below the band"; (a) and (c) both widen the interval, which now contains [5.5683739, 5.5793640]); the lower end is not bracketed
   by row 53 (L2 and whole-box N_f both below row 52's). COMPARISON WITH X3 on the same configurations (different bases): whole-box N_f 1.289 / 0.984, within 0.5 of
   P 1.005 / 0.977, N_v r <= 1000 1.288 / 1.038, J 0.954 / 0.882, far band 1.015 / 1.017: "on the finer configuration a fit on the smaller basis m <= 150 at c_l
   5.5683739 has whole-box and near-P N_f maxima 2 percent below the candidate's and a smaller J. The report must not say or imply that the candidate's exponent
   or basis gives the smallest residual maxima among the fits computed" (accepted by the lead 04:02Z). My first-grid whole-box value 6.789e-7 agrees with the
   verifier's 16875 x 512 value 6.730e-7 to 0.9 percent. (2026-10-19T04:07:02Z)
 (2026-10-19T03:43:59Z)

24. fxn16g (chain-8e step 54; the third lower-end profile row, requested by the lead at 03:13:52Z: nominal transplant offset d = -1.6e-2 from F0, stored c_l
   5.5604082120, start = the lead's transplant fxn16_-1.6e-02_shape.npz (md5 9face47281dca84c1e5256ad50898366; start norm 4.504e-4 on the 720 grid, far from the
   equation), 20480 x 720, inner 2500, check 250, damping 1e-8, K = 21500; run because L2(fxn8g) < L2(fxn4g); references and readings as in item 18, plus the lead's
   bracket statement (03:13:52Z item 3 / 03:46:06Z item 4: the lower end of the tested span is bracketed at this budget only if L2 AND whole-box N_f are above the
   preceding row's on both verifier configurations)): started 03:41:15Z (shared with 48 throughout), DONE 04:46:54Z, total 21500 iterations; objective 4.504192e-04
   -> ends of the linearisations 2.028481e-05, 9.984020e-06, 6.125841e-06, 4.441859e-06, 3.666989e-06, 3.242195e-06, 2.993441e-06, 2.820744e-06, 2.737838e-06 (falls
   50.8, 38.6, 27.5, 17.4, 11.6, 7.7, 5.8 percent per linearisation, then 2.94 over the last 1500; -1.72 percent over the last 1000 its and -0.38 over the last 250:
   "flattened" by the letter of the 2 percent clause but only just, and 4-10 times less settled than rows 37-40, 52 (-0.14 to -0.19) and 53 (-0.44)) -> 2.737838e-06 =
   0.643 x F2's L2 and 0.867 x fxn8g's. Shape leadcode/gpu/fxn16g/fxn16g_shape.npz, md5 65d87bb7c4aa2be6c17263a033fc38c5 (mtime 04:46:53Z). Since L2 < 3.1570267e-6
   the lead's 03:46:06Z condition holds: chain 9 started step 55 fxn24g (d = -2.4e-2, stored c_l 5.5524652878, start fxn24_-2.4e-02_shape.npz md5
   00450f11d7f5b4b4bbcd8a3a761358b4, start norm 1.0015e-3 on the 720 grid) at 04:47:28Z (shared with 48; end ~06:00Z).
   MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960; F2 and fxn8g on the matched grids): whole-box N_f 8.422e-7 ; 8.276e-7 = 0.531 ; 0.501 x F2's and
   1.24 ; 1.17 x fxn8g's, now ON the x-axis (theta 0, r 8.553, 0.035 left of P: inside the registered 0.5 neighbourhood, so it is the near-P value); lobe above P
   6.93e-7 ; 6.80e-7 (0.67 ; 0.63 x F2, 1.35 x fxn8g; the lobe maximum at r 8.77, theta 0.297); 2-10 N_v 2.37e-7 ; 2.32e-7 (0.53 ; 0.50 x F2); 0.1-2 4.45e-8 (0.62 x F2,
   0.77 x fxn8g: still falling); 10-100 2.95e-7 (1.43 x F2, 1.53 x fxn8g: rising); 100-1000 3.38e-8 (1.15 x F2, 1.44 x fxn8g); outer quick-scan band (131 L-1000 L)
   N_f 2.35 x F2 and N_v 2.15 x (1.39 x fxn8g); h(P) - 1 -2.5e-8 ; -1.7e-8; x* 8.588480 (-1.24e-2 relative to F2). READINGS on these numbers: (a) fails (L2 0.643 and
   whole-box 0.50-0.53 are outside the 30 percent band on the low side; |h(P) - 1| <= 2.5e-8 fine); (b) fails (near-P N_f 0.5 x F2, not 2 x); so (c) "undecided at
   this level" by the letter, not excluded, and the interval widens down to 5.5604082 (the verifier's rows decide). BRACKET: L2 is BELOW row 53's (0.867) while the
   whole-box N_f is ABOVE row 53's (1.17-1.24) on both grids, so by the lead's definition (both above) the lower end is NOT bracketed by this row, and the two
   quantities now disagree: the near-P maximum has turned up between d = -8e-3 and -1.6e-2 while the weighted objective still decreases (the row is also the least
   settled). Bands beyond r = 10 keep rising toward smaller c_l (10-100: 1.875 / 1.934 / 2.95 e-7 at -4e-3 / -8e-3 / -1.6e-2; against X3 the 10-100 band is now 3.6 x).
   Row 55 (d = -2.4e-2, the mirror of the excluded +2.4e-2) follows; the lead's reading for it is the same rule plus the bracket statement. (2026-10-19T04:51:18Z)
   VERIFIER G123 (05:03:17Z) on fxn16g: (a) fails (L2 0.643; whole-box N_f (A5) 0.716 / 0.485 of F2 on 11250 x 384 / 16875 x 512, below the 30 percent band),
   (b) fails: reading (c) CONFIRMED; the interval of (iv) now contains [5.5604082, 5.5793640]; bracket statement: L2 of 54 BELOW 53's, whole-box N_f ABOVE 53's
   (as on my scans): not bracketed by the lead's definition. Full entry in VERIFY_REPORT G123. G123's X3 COMPARISON (N11250 q384 / N16875 q512; different bases, a fact about two fits): whole-box N_f 1.631 / 1.115, within 0.5 of P 1.181 / 1.115, N_v r <= 1000 1.636 / 1.119, far band beyond r = 1000 1.047 / 1.055, J 1.263 / 1.227 (eps 0.03 / 0.01): row 54 is above X3 in every maximum on both configurations. G123's absolute numbers: whole-box N_f (A5) 1.1271e-6 / 7.630e-7 (the 11250 maximum at the under-resolved lobe point r 8.766, theta 0.311; the 16875 maximum within 0.5 of P, at r 8.5626, theta 0.0098), near-P 7.684e-7 / 7.630e-7, N_v r <= 1000 3.141e-7 / 2.144e-7, far N_v 1.141e-6 / 1.162e-6, h(P) - 1 +6.90e-7 / +7.38e-8 (falling with the verifier's radial resolution; my -2.5e-8 / -1.7e-8 at 32768 x 640 / 24576 x 960 consistent at the grid error, G124), identity c_l = the stored value to 1e-9, h(P) = 1 root at fixed rho +5.4e-8 above it, x* 8.5884804 (mine 8.588480), J (857 labels) 1.7539e-6 / 1.9658e-6 = 0.514 / 0.522 x F2; G123 states that among the tested rows the residual maxima (whole-box N_f, near-P N_f, J) are smallest at row 53 (5.5683739) while the L2 objective still decreases at 5.5604082, so "the maxima fall faster than L2 toward lower c_l" holds on [5.5683739, 5.5763624] only. (2026-10-19T05:11:49Z; X3 comparison transcribed 2026-10-19T05:15:40Z)

25. dom9000gF (chain-7d step 48; the FREE control of the 9000 L domain row, requested by the lead as a DATA row (NOTES_FOR_TEAM 2026-10-18T20:41:00Z: not a
   candidate, no decision attached; reading (a) c_l drift, (b) far field, (c) the pair dom9000g / dom9000gF by ratios): start = F3 = c6gF end (md5
   0398af3f08a2a4f75e42c846edbaa375), c_l FREE from 5.576371155, fit rows r < 9000 L, inverse domain and two-term closure at R_shape 1e4 L, 24576 x 960, 11753238
   rows, 75382 columns, inner 2500, check 250, damping 1e-8, K = 20750; the same configuration as dom9000g (item 13) except for the start shape and the free c_l):
   started 03:33:32Z (shared GPU throughout: with 53, then 54, then 55), DONE 05:26:29Z, total 20750 iterations, wall 6774 s; objective on its rows 9.230711e-06 (start = F3
   evaluated on the enlarged-domain configuration; dom9000g's start from X3 read 9.246879e-06, 0.18 percent higher) -> ends of the linearisations 1.561914e-06,
   1.523581e-06, 1.494308e-06, 1.467096e-06, 1.441640e-06, 1.416940e-06, 1.393612e-06, 1.371527e-06, 1.366938e-06 (ratio to the start 0.148; the first linearisation
   falls 83.1 percent, then 2.5, 1.9, 1.8, 1.7, 1.7, 1.6, 1.6 percent per linearisation, 0.33 over the last 750). Shape leadcode/gpu/dom9000gF/dom9000gF_shape.npz, md5 cc1a55171576ef7eea3a591a59c67ea2
   (mtime 05:26:28Z). (a) c_l DRIFT: 5.576371155 -> 5.576369677 at the end, -1.48e-6 over 20750 iterations, slow and decreasing at every linearisation end (5.576370739 /
   5.576370444 / 5.576370136 / 5.576369835 at 2500 / 7500 / 12500 / 17500 iterations: about -1.5e-7 per 2500 iterations over the middle and late linearisations; three
   upward steps below 7e-10 between checks at 3250, 5250, 10250; only -7.4e-9 over the last 750, so the drift slows at the end), against the at most 6.9e-6 of the
   free continuations on 900 L rows; the end value is +1.0071e-3 above the fixed 5.5753626106 (F3 was +1.0085e-3): the free c_l moves toward the fixed value by
   0.15 percent of the gap at this budget. The identity c_l is the stored value (the driver
   enforces it; the inverse-derived value in the scan equals it to 1e-9). h(P) - 1 at the end -8.2e-9 (32768 x 640) / -5.7e-11 (24576 x 960), x* 8.600844 (= F3's
   to 4e-8 relative; dom9000g 8.600065). (c) THE PAIR BY RATIOS (equal counts, the driver's own objective on the same rows): dom9000g / dom9000gF = 1.0018 at the
   start, then 0.974, 0.974, 0.974, 0.975, 0.975, 0.975, 0.976, 0.976, 0.976 at the linearisation ends: the fixed-c_l arm is 2.4-2.6 percent lower at every count
   after the first linearisation (the m <= 150 and m <= 200 pairs on 900 L rows gave 3.8 and 2.7-4 percent; here the two starts are themselves 1e-3 apart in c_l, so
   as before the pair compares two fits, not the dependence on c_l alone). MY CROSS-CHECK SCANS (quick_scan_fit, closure at 1e4 L for both arms; leadcode/gpu/
   dom9000gF/dom9000gF_scan_{32768x640,24576x960}.json, helper scan_ratio.py), dom9000gF / dom9000g at 32768 x 640 ; 24576 x 960: whole-box N_f 5.039e-7 / 5.008e-7
   = 1.006 (both at the lobe above P, r 8.735, theta 0.194) ; 5.010e-7 / 4.750e-7 = 1.055 (dom9000gF's maximum at 960 near the x-axis at r 8.375, theta 0.008,
   0.23 left of P; dom9000g's at the lobe), whole-box N_v 1.006 ; 1.016, r <= 0.1 1.025, 0.1-2 1.016, 10-100 N_f 0.999 ; 1.006 (the one band where the free arm
   is lower, by 0.07 percent at 640; its maxima sit at r 14.1, theta 0.96 against the fixed arm's at r 10, theta pi/2), 100-1000 1.021 ; 1.020, outer quick-scan
   band (131 L to 1e4 L) N_f 1.007, N_v 1.034 ; 1.033 (rms 1.022), whole-box rms 1.038: the band maxima of the two arms differ by at most 5.5 percent, the free arm
   higher in all bands but one, and the positions of the maxima are not all the same; both arms have lower whole-box maxima and rms than their reference scans
   (not every band maximum: the lobe (2-10 middle) maximum is 1.04 x the reference for both arms) (dom9000gF / F3 using the F3 scan at 32768 x 640: whole-box N_f
   0.682, N_v 0.711, 0.1-2 0.920, 10-100 0.942, 100-1000 0.856, whole-box rms 0.747; dom9000gF / X3 0.727, 0.757, 0.941, 0.967, 0.876, 0.778; dom9000g / X3 0.722,
   0.753). (b) FAR FIELD: the
   lead's far1 / far2 quantities (C at the axis, q1) are the lead's to compute; the verifier's bands on their evaluator decide (the quick-scan outer band is the
   fit's own convention inside the closure radius and is not comparable with the 1000 L-closure fits' band in extent). This lane's reading: the free control
   reproduces the 9000 L row's interior and far-band values within 5.5 percent (the fixed arm lower in all bands but one), the c_l of a free fit with rows to
   9000 L drifts by 1.5e-6 in 20750 iterations toward the fixed value, closing 0.15 percent of the 1.0e-3 gap at this budget; no decision is attached (lead 20:41Z).
   VERIFIER G125 (05:51:10Z) ON dom9000gF (own evaluator; values CONFIRMED as listed): (a) c_l end 5.5763696769 (identity on their inverse 5.5763696770; h(P) = 1 root
   +4.1e-8), -1.478e-6 against F3 over 20750 iterations, +1.0071e-3 against the fixed value; (b) far field: C at the axis +6.503e-4 (dom9000g 1.006, F3 0.035), q1
   4.949e-4 (dom9000g 4.938e-4, F3 1.5779e-2); band N_v maxima formula-continued (16875 x 512 / 22500 x 384) against F3: 1000 L-9000 L 3.291e-8 / 3.142e-8 (0.030 /
   0.029), 9000 L-1e4 L 2.415e-8 / 2.417e-8 (0.025), r > 1e4 L 3.285e-8 / 3.293e-8 (0.035 / 0.036); the free c_l changes none of G91's far-band readings of dom9000g
   by more than 4 percent (1.028 / 1.035); (c) the pair dom9000g / dom9000gF: whole-box N_f own convention 1.001 (maxima in the closure region at 2.3e4 L), formula-
   continued 0.920 / 1.000, within 0.5 of P 0.931 / 0.937 / 0.935, N_v r <= 1000 1.073 / 0.940 / 1.001, far N_v 1.000 (closure) and 0.973 / 0.997 (formula), J 0.937 /
   0.937, L2 0.976; h(P) - 1 of dom9000gF +3.05e-7 / +6.02e-8 / -6.30e-9; x* 8.6008441, the only W_1 zero on the x-axis, no open-quadrant cell. "The pair repeats the
   X3 / F3 pattern on rows to 9000 L: the fixed-c_l fit is lower next to P (0.93 to 0.94) and in J (0.94), equal in the far bands; the free c_l stays at its F3 value
   to 1.5e-6. Not a candidate; no decision attached." The lead's 05:52:35Z note reads row 55 (item 26) on their scans exactly as this lane does ((a) against F2,
   widening to 5.5524653, bracket by SPEC v4.15); the verifier's configurations decide. (2026-10-19T05:54:39Z)
   Items 25 and 26 were audited by the external referee (astra/shift8audit_a; 14 findings, all applied at 2026-10-19T06:04:07Z: matched-grid denominators, the 0.1-2 ratio,
   maxima positions, the c_l-drift wording, the start-norm range, the (a) wording). Chain state after 48: 49 dom9000g2 (chain 7e2) waits for the done lines of 56 and 57. (2026-10-19T05:29:46Z)

26. fxn24g (chain-9 step 55; the fourth lower-end profile row, the mirror of the excluded +2.4e-2 row 39; requested by the lead at 03:46:06Z, run because
   L2(fxn16g) < L2(fxn8g): nominal transplant offset d = -2.4e-2 from F0, stored c_l 5.5524652878, start = the lead's transplant fxn24_-2.4e-02_shape.npz (md5
   00450f11d7f5b4b4bbcd8a3a761358b4; start norm 1.0015e-3 on the 720 grid, 2.2 x row 54's start norm), 20480 x 720, inner 2500, check 250, damping 1e-8,
   K = 21500; references and readings as in item 18 (NOTES 00:25:51Z item 2) plus the bracket statement of 03:13:52Z item 3 / 03:46:06Z item 4): started 04:47:28Z
   (shared with 48 until 05:26Z, then alone), DONE 05:48:09Z (chain line; shape mtime 05:48:08Z), total 21500 iterations; objective 1.001514e-03 -> ends of the
   linearisations 3.065447e-05, 1.413861e-05, 8.414678e-06, 5.924942e-06, 4.791175e-06, 4.141207e-06, 3.741627e-06, 3.450255e-06, 3.300646e-06 (the first
   linearisation falls 96.9 percent, then 53.9, 40.5, 29.6, 19.1, 13.6, 9.6, 7.8 percent per linearisation, then 4.34 over the last 1500; -2.50 percent over the last 1000 iterations and -0.53 over the last 250: NOT flattened by the 2 percent clause, the
   least settled row of the profile, after row 54's -1.72) -> 3.300646e-06 = 0.775 x F2's L2 and 1.206 x row 54's (2.737838e-06). Shape
   leadcode/gpu/fxn24g/fxn24g_shape.npz, md5 e52a8be0f977eaa6398fb9d27302453d (mtime 05:48:08Z). MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960;
   F2 and row 54 on the matched grids): whole-box N_f 1.854e-6 ; 1.916e-6 = 1.17 ; 1.16 x F2's (1.585e-6 ; 1.652e-6) and 2.20 ; 2.31 x row 54's, near the x-axis
   at r 8.522, theta 0.0098 ; 0.0115 (x 8.52, y 0.08-0.10; 0.06 left of P, x* 8.582324, distance 0.10-0.12 from P: the near-P value); lobe above P 1.166e-6 ;
   1.188e-6 (1.13 ; 1.10 x F2, 1.68 ; 1.75 x row 54); 2-10 N_v 5.19e-7 ; 5.37e-7 (1.17 ; 1.16 x F2); 0.1-2 3.06e-8 (0.430 x F2 on both grids, falling further below
   F2 from 0.624 at row 54); 10-100 3.98e-7 (1.93 ; 1.91 x F2: the band keeps rising toward smaller c_l, 1.875 / 1.934 / 2.95 / 3.98 e-7 at -4e-3 / -8e-3 / -1.6e-2 /
   -2.4e-2 at 640); 100-1000 4.38e-8 (1.48 ; 1.44 x F2); h(P) - 1 -4.2e-8 ; -2.7e-8; x* 8.582324 (-2.15e-3 relative to F2). READINGS on these numbers: my scans
   satisfy the numerical inequalities of (a) (L2 0.775 and whole-box N_f 1.16-1.17 inside the two-sided 30 percent band; |h(P) - 1| about 4.2e-8 <= 1e-6), so the
   verifier would read (a) "not determined at this level" if their whole-box N_f is inside the band on both configurations and their |h(P) - 1| <= 1e-6; (b) fails
   twice (not flattened, which alone prevents exclusion under the rule; near-P N_f 1.2 x F2, not 2 x). Either way the row is not excluded and the interval of non-excluded tested values widens to 5.5524653 at its lower end (the verifier's rows decide).
   BRACKET: L2(55) is ABOVE L2(54) (1.206 x) and the whole-box N_f of 55 is ABOVE 54's on both my grids (2.20 ; 2.31 x), so the numerical analogue of the lead's
   definition (both above on both configurations) holds on my scans and the lower end of the tested span is bracketed at this budget on them, pending the
   verifier's two configurations: the equal-budget L2 of the
   transplanted fixed-c_l rows has its minimum among the tested exponents at d = -1.6e-2 (5.5604) and the residual maxima theirs at d = -8e-3 (5.5684, G123). This
   lane's caveat, stated with the bracket: rows 54 and 55 are the two least settled rows (-1.72 and -2.50 percent over their last 1000 iterations, against -0.14 to
   -0.49 for the others) and their start shapes are farther from the equation than the smaller-offset transplant starts (start norms 4.50e-4 and 1.00e-3 against
   1.0e-5 to 1.2e-4 for the rows with |d| <= 8e-3: fxu2g 1.0e-5, fxm2g 1.5e-5, fxu3g 1.7e-5, fxn4g 3.5e-5, fxn8g 1.2e-4; row 39 at +2.4e-2 started at 9.46e-4), so
   the equal-budget profile at its lower end measures in part how far 21500 iterations carry a poorer start, and the bracket is a statement about this budget
   and these starts, not about the limit. The nested m <= 200 pair 56 nst24g (c_l 5.6004662) and 57 nsn8g (c_l 5.5683739) started 05:48:09Z and 05:48:49Z (chains
   9 / 9b, both 20480 x 960, K 20750, shared GPU). (2026-10-19T05:50:42Z)
   VERIFIER G126 (06:06:44Z) ON fxn24g (N11250 q384 / N16875 q512; ratios to F2): L2 0.775, -2.498 percent over the last 1000 (NOT flattened); whole-box N_f (A5)
   1.7917e-6 (1.139) / 1.8250e-6 (1.159), both within 0.5 of P (r 8.518 / 8.528, theta 0.0098, distance 0.106 / 0.100; N22500 q384 1.8571e-6); N_v r <= 1000 5.017e-7
   (1.142) / 5.114e-7 (1.163); far N_v beyond 1000 1.1525e-6 / 1.1526e-6; h(P) - 1 +1.46e-6 / +2.61e-7 and +6.3e-9 at N22500 q384 (falls with their radial resolution as
   in G73); identity c_l = the stored value to 3e-9; h(P) = 1 root at fixed rho -8.6e-7 / -6.2e-8 below it; x* 8.5823236, the only W_1 zero on the x-axis, no open-quadrant
   cell; J (857 labels) 3.9530e-6 / 4.5375e-6 = 1.158 / 1.206. READING: (a) fails by the letter only through |h(P) - 1| = 1.46e-6 > 1e-6 at N11250 q384 (L2 and whole-box
   N_f inside the band), (b) fails: "(c) undecided at the 375 x m <= 150 level after 21500 iterations" CONFIRMED, "(a) on resolved h(P)" (N >= 16875 or the lead's
   scans); both readings widen the interval, now [5.5524653, 5.5793640]. BRACKET CONFIRMED by SPEC v4.15 (L2 1.206 x row 54's; whole-box N_f 1.7917e-6 > 1.1271e-6 and
   1.8250e-6 > 7.630e-7), with two facts attached: (i) row 55 has not flattened (-2.50 percent over its last 1000 iterations) and at its last-1000 rate would need about 7400 more iterations (constant rate assumed; G126's figure, which corrects the 'roughly 8000' first written here) to reach row 54's L2,
   so "the bracket is a statement about fits from transplanted starts at one budget, not about where an objective over c_l has its minimum" (the lead's start norms on
   2048 x 720: 1.48e-3 for 55 against 8.41e-4 for 54); (ii) row 55 is below F2 in L2 but above F2 in whole-box N_f, N_v r <= 1000 and J, so on this row the objective
   and the residual maxima disagree. X3 comparison: whole-box N_f 2.593 / 2.668, within 0.5 of P 2.754 / 2.668, N_v r <= 1000 2.613 / 2.668, far band 1.063 / 1.073,
   J 2.848 / 2.833: above X3 in every maximum. Profile at N16875 q512 (d = -2.4e-2 ... +2.4e-2): L2 / F2 0.775, 0.643, 0.741, 0.858, 0.926, 0.962, 1, 1.078, 1.115,
   2.036; N_f / F2 1.159, 0.485, 0.427, 0.713, 0.869, 0.911, 1, 1.138, 1.214, 2.914; J / F2 1.158, 0.514, 0.388, 0.707, 0.865, 0.921, 1, 1.159, 1.224, 2.871: L2
   smallest at row 54 (5.5604082), the maxima smallest at row 53 (5.5683739). The N_v r <= 1000 and whole-box N_f ratios agree to 0.025 over all ten rows. This
   lane's provisional readings (item text above) agree with G126 except that the verifier's coarser configuration puts |h(P) - 1| above 1e-6, which my scans (and
   the lead's) do not resolve as such. (2026-10-19T06:07:34Z)

27. nst24g (chain-9 step 56; the first half of the lead's nested pair (NOTES_FOR_TEAM 03:54:45Z): row 39's end (fxv24g, d = +2.4e-2, stored c_l 5.6004661644, the
   exponent excluded at the m <= 150 level) enriched by the lead to m <= 200 with zero new coefficients (nst24_start_shape.npz, md5 abcca3b0ebe079a6f5fcaa16d69905a5;
   density unchanged), then fitted exactly as step 31 (X3 from X2): fixed c_l, 20480 x 960, 9786429 rows, 75382 columns, inner 2500, check 250, damping 1e-8, K = 20750;
   references at m <= 200: F3 = c6gF (L2 1.6641961e-6) and X3 = c6g (1.6192702e-6); readings fixed by the lead in 03:54:45Z item 3 (i) and (iii), on the verifier's
   configurations): started 05:48:09Z (shared with 57 throughout), DONE 07:24:29Z, total 20750 iterations; objective 8.587818e-06 (start = the row 39 end on the 960
   grid; its own 720-grid objective was 8.671252e-06) -> ends of the linearisations 3.619332e-06, 3.343391e-06, 3.226382e-06, 3.130014e-06, 3.043191e-06, 2.963148e-06,
   2.886083e-06, 2.814215e-06, 2.795041e-06 (the first linearisation falls 57.9 percent, then 7.6, 3.5, 3.0, 2.8, 2.6, 2.6, 2.5 percent, 0.68 over the last 750; -0.96
   percent over the last 1000 iterations and -0.22 over the last 250: FLATTENED by the 2 percent clause) -> 2.795041e-06 = 0.3255 x its start (the X3 / F3 enrichment
   steps ended at about 0.40 x theirs). Shape leadcode/gpu/nst24g/nst24g_shape.npz, md5 98b033aa6433a56b943356e0245844a4 (mtime 07:24:29Z). Q_200 = L2(56) / L2(F3) =
   2.795041e-06 / 1.6641961e-06 = 1.680 against Q_150 = 2.036 (row 39 to F2); L2(56) / L2(X3) = 1.726. BY THE LEAD'S RULE (i): 56 has flattened and 1.36 < Q_200 =
   1.68 < 3.05, so the reading is "undecided" (neither "favours an isolated profile" (>= 3.05) nor "favours a family through the candidate" (<= 1.36)); Q fell from
   2.04 to 1.68 under the angular refinement without leaving the undecided band. MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960; F3 and X3 on the
   matched grids, leadcode/gpu/c6gF/c6gF_scan*.json, c6g/c6g_scan*.json): whole-box N_f 1.832e-6 ; 1.916e-6 = 2.479 ; 2.470 x F3 (near P: r 8.552, theta 0.0074 ;
   r 8.544, theta 0.008, horizontal offset 0.07-0.08 left of P, x* 8.619483 = row 39's; row 39 was 2.915 / 2.914 x F2 on the verifier's grids), whole-box N_v 2.484 ; 2.474, r <= 0.1 0.879,
   0.1-2 1.261, 10-100 N_f 1.896 ; 1.922 (N_v 1.52), 100-1000 1.61 ; 1.57, outer quick-scan band (131 L to 1000 L, same closure as F3) N_f 1.53, N_v 1.40, whole-box rms
   2.00; h(P) - 1 +1.2e-8 ; +6.2e-9; x* 8.619483 (+2.17e-3 relative to F3). Against X3: whole-box N_f 2.642 ; 2.635. Against its own parent row 39 (fxv24g at m <= 150,
   matched grids): whole-box N_f 0.397, N_v 0.398, r <= 0.1 0.258, 0.1-2 0.332, 10-100 0.463 at 640 (the 960 ratios and the remaining bands are in WORKLOG 2026-10-19T07:27:04Z; this item written 2026-10-19T07:26:32Z):
   the angular enrichment lowers this row's whole-box maximum by about the factor by which it lowered the candidate lineage's (X3 / X2 whole-box 0.48, F3 / F2 0.47 on
   my 640 scans), so the row remains excluded, with a smaller relative excess over the reference (near-P 2.41-2.50 x F3 against 2.91 x F2 before, G135). INTERVAL RULE at the m <= 200 level (03:54:45Z item 3 (iii), the 00:25:51Z rule against F3):
   on my scans (a) fails (L2 1.68 and whole-box N_f 2.47-2.48 x F3 are outside the 30 percent band) and (b) HOLDS (flattened at -0.96 percent; near-P N_f 2.47-2.48 >=
   2 x F3 on both grids), so 5.6004662 would be "excluded at the m <= 200 level" too and would not widen the interval; the verifier's configurations decide (row 39's
   verifier near-P ratios 2.915 / 2.914 were well above 2, so the m <= 200 ratio 2.47 leaves less margin at the coarser configuration). Not a candidate; nothing here is a
   statement about P_2 (lead (iii)). Step 57 nsn8g (the other half, at 5.5683739) was at outer 9 it 500 when 56 ended.
   VERIFIER G135 (07:55:19Z) ON nst24g (N11250 q384 / N16875 q512; ratios to F3 / to X3): L2 1.680 / 1.726, flattened (-0.956 percent); whole-box N_f (A5) 1.6757e-6
   (2.412 / 2.425), 1.8249e-6 (2.499 / 2.668), both within 0.5 of P (0.163 / 0.093 from P); N_v r <= 1000 2.419 / 2.503 x F3; far band 1.054e-6 / 1.066e-6 (0.955 / 0.969 x
   X3, "the common far level"); J 3.6120e-6 / 4.4214e-6 (2.439 / 2.587 x F3); h(P) - 1 -7.72e-7 / -1.82e-7; identity c_l 5.6004661611 (3.3e-9 below the stored value);
   x* 8.6194830, the only W_1 zero on the x-axis, no open-quadrant cell; B_3 (IBP) 0.2982. READING (i): "undecided" (Q_200 = 1.680 between 1.36 and 3.05); near-P 2.412 /
   2.499 x F3 (row 39 to F2: 2.915 / 2.914). READING (iii): (b) "excluded at this level" (flattened; near-P >= 2 x F3 on each configuration), so 56 does not widen the
   interval; 5.6004662 is excluded at m <= 150 (G114) and at m <= 200. Required wording: one refinement step of the discriminating experiment was done and is undecided by
   the rule fixed before the runs; Q_150 = 2.036 and Q_200 = 1.680 may be stated as measured, and "the decrease from 2.036 to 1.680 must not be read as favouring a
   family or as a trend: it is one step, and the rule assigns no reading between the thresholds". This lane's provisional readings above agree with G135. (2026-10-19T07:56:22Z) (2026-10-19T07:26:32Z)

28. nsn8g (chain-9b step 57; the second half of the nested pair: row 53's end (fxn8g, d = -8e-3, stored c_l 5.5683738938, the exponent with the smallest residual
   maxima among the m <= 150 rows, G123 / G126) enriched by the lead to m <= 200 with zero new coefficients (nsn8_start_shape.npz, md5 389355483417024e6c7000614ceb4353),
   fitted exactly as step 31: fixed c_l, 20480 x 960, inner 2500, check 250, damping 1e-8, K = 20750; readings fixed in 03:54:45Z item 3 (ii) and (iii) on the verifier's
   configurations): started 05:48:49Z (shared with 56 throughout), DONE 07:25:21Z, total 20750 iterations; objective 3.122646e-06 (start = the row 53 end on the 960 grid;
   its own 720-grid objective was 3.157027e-06) -> ends of the linearisations 1.575735e-06, 1.513545e-06, 1.477431e-06, 1.444841e-06, 1.414806e-06, 1.386443e-06,
   1.359461e-06, 1.334084e-06, 1.328223e-06 (the first linearisation falls 49.5 percent, then 3.9, 2.4, 2.2, 2.1, 2.0, 1.9, 1.9 percent, 0.44 over the last 750; -0.61
   percent over the last 1000 iterations and -0.16 over the last 250: FLATTENED) -> 1.328223e-06 = 0.4254 x its start. Shape leadcode/gpu/nsn8g/nsn8g_shape.npz, md5
   29f70bbc0660d7c11f359885e7cc0086 (mtime 07:25:21Z). L2(57) / L2(X3) = 1.328223e-06 / 1.6192702e-06 = 0.820 against L2(53) / L2(X2) = 3.157027e-06 / 4.096686e-06 =
   0.771 at m <= 150 (the lead's (ii) comparison: the objective advantage of the lower exponent narrows from 23 to 18 percent under the enrichment); L2(57) / L2(F3) =
   0.798. MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960; X3, F3 and the parent row on the matched grids): whole-box N_f 5.229e-7 ; 5.065e-7 = 0.754 ;
   0.697 x X3 (nsn8g's maximum at the lobe above P, r 8.73, theta 0.196 ; r 8.79, theta 0.304, while X3's is next to P at r 8.526-8.527, theta 0.007-0.008; nsn8g's
   value next to P is lower still; its lobe value is 1.087 ; 0.980 x X3's lobe value) and 0.708 ; 0.653 x F3; whole-box N_v 0.785 ; 0.724 x X3; r <= 0.1 1.025 (2.5 percent
   above X3); 0.1-2 0.919 ; 0.918; 10-100 N_f 1.170 ; 1.174 x X3 (17 percent above; N_v 0.844); 100-1000 0.811 ; 0.823; outer quick-scan band (131 L to 1000 L, same closure) N_f 0.839 ; 0.850, N_v 0.878; whole-box rms 0.740; h(P) - 1
   -1.3e-8 ; -8.7e-9; x* 8.594652 (= row 53's; -6.3e-4 relative to X3). Against its parent row 53 (fxn8g at m <= 150): whole-box N_f 0.770 ; 0.717, N_v 0.763 ; 0.718,
   r <= 0.1 0.472, 0.1-2 0.456, 10-100 0.493 ; 0.495, 100-1000 0.566 ; 0.602 (N_v 0.649 ; 0.678), outer band N_f 0.336 ; 0.340, N_v 0.394, whole-box rms 0.487: the
   enrichment lowers this row's whole-box maximum to 0.770 ; 0.717 of its parent's and its near-P x-strip maximum to 0.603 ; 0.607, while its lobe maximum rises slightly
   (1.022 ; 1.016), so the whole-box maximum moves from next to P to the lobe (less gain than X2 -> X3's 0.48, because row 53's whole-box maximum at m <= 150 was
   already at the level X3 reaches at m <= 200); the N_f bands beyond r = 10 fall to 0.34-0.60. READING by the lead's (ii) on my scans: L2 (0.820) AND whole-box N_f (0.754 ; 0.697) of 57 are BELOW X3's on both
   grids, so if the verifier's configurations agree the report says that "on m <= 200 too a fixed-c_l fit at 5.5683739 reaches a smaller objective and smaller
   residual maxima than the candidate at equal budget" (no decision attached; not a candidate, lead (iii)). INTERVAL RULE at the m <= 200 level against F3 (00:25:51Z
   rule): L2 0.798 inside the 30 percent band, whole-box N_f 0.708 ; 0.653 (inside at 640, below the two-sided band at 960: (a) by the letter at 640, (c) at 960, as
   row 53 read at m <= 150, G119), |h(P) - 1| <= 1.3e-8; (b) fails (0.7 x, not 2 x): not excluded at this level either way. Chain state: 49 dom9000g2 and 50 c6h9000
   started 07:25:27Z / 07:25:28Z in parallel (chains 7e2 / 7f4); chain 10 runs 58 fxn16gb / 59 fxn24gb after both.
   VERIFIER G135 (07:55:19Z) ON nsn8g (N11250 q384 / N16875 q512; ratios to F3 / to X3): L2 0.798 / 0.820, flattened (-0.610 percent); whole-box N_f (A5) 9.1325e-7
   (1.315 / 1.322) at N11250 q384 and 4.7247e-7 (0.647 / 0.691) at N16875 q512, both maxima at the off-axis lobe point (r 8.784 / 8.788, theta 0.301 / 0.304, 2.6 from P),
   "the point that G73 (h) showed to be under-resolved by my N11250 radial grid" (row 53 had its N11250 maximum there too); at N22500 q512 (outside the rule) 5.1188e-7
   (0.703 / 0.749); within 0.5 of P 3.8471e-7 / 4.0252e-7 (0.554 / 0.591 and 0.551 / 0.588 x F3 / X3); N_v r <= 1000 1.303 / 1.320 and 0.659 / 0.703; far band 1.096e-6 /
   1.107e-6 (1.007 / 1.009 x X3); J 7.8073e-7 / 8.7344e-7 (0.527 / 0.562 and 0.511 / 0.545 x F3 / X3); h(P) - 1 +4.76e-7 / +2.84e-8; identity c_l 5.5683738906 (3.2e-9
   below the stored value); x* 8.5946518; B_3 (IBP) 0.2984. READING (ii): the condition "L2 and whole-box N_f of 57 below X3's on both configurations" FAILS at N11250 q384
   (whole-box 1.322 x X3 at the under-resolved lobe point), so the report gives the ratios (L2 0.820 against 0.771 at m <= 150; within 0.5 of P 0.59 x X3 on each
   configuration; J 0.56 / 0.55 x X3; whole-box 1.32 x X3 at N11250 q384 and 0.69 x at N16875 q512), and "57 has smaller residual maxima than the candidate" must not be
   stated without the N11250 q384 exception; under C3 the report must say that on m <= 200 a fit computed at another fixed c_l has a smaller L2, smaller N_f next to P and
   a smaller J than X3 at equal iteration count, and must not imply that X3 has the smallest residual of the fits computed. READING (iii): (a) fails (whole-box 1.315 /
   0.647, outside the band on both sides), (b) fails (near P 0.55): (c) "undecided at the 375 x m <= 200 level"; 5.5683739 stays inside the interval, which does not change.
   Verdict CONFIRMED; neither row is a statement about P_2; the candidate stays X3 (G74). NOTE on the one difference from this lane's provisional reading: my quick-scan
   grids (32768 x 640 and 24576 x 960, log-radial) resolve the lobe point and give whole-box 0.754 ; 0.697 x X3 at the lobe, the same side as the verifier's N16875 q512
   (0.691) and N22500 q512 (0.749) values; the verifier's N11250 q384 maximum (1.322 x X3) is the under-resolved lobe value, which the rule as written nevertheless counts,
   so by the rule the (ii) sentence is not made and the ratios stand. (2026-10-19T07:56:22Z) (2026-10-19T07:28:50Z)

29. dom9000g2 (chain-7e2 step 49; the budget row of the 9000 L domain column, requested by the lead 2026-10-18T23:22:40Z as a DATA row: dom9000g (item 13; X3 + 20750
   iterations on rows to 9000 L) continued another 20750 iterations at its fixed c_l 5.575362610642 on its own rows (fit radius 9000 L, inverse domain and two-term
   closure at 1e4 L), 24576 x 960, 11753238 rows, 75382 columns, inner 2500, check 250, damping 1e-8, K = 20750; the lead's reading fixed in 23:22:40Z item 2 on the
   verifier's rows: dom9000g2 / dom9000g over 1000 L-9000 L (formula continued, both N >= 16875 configurations) and C at the axis in [0.8, 1.25] on both = "the budget does
   not lower the 9000 L row's far band further", at most 0.5 on both = "the far band falls further with the iterations", otherwise the ratio is stated; near-P N_f and
   857-label J ratios stated without attribution): started 07:25:27Z (shared with 50 throughout), DONE 09:17:15Z, total 20750 iterations; objective 1.334388e-06 (= the
   dom9000g end on the same rows) -> ends of the linearisations 1.291151e-06, 1.254053e-06, 1.224316e-06, 1.197803e-06, 1.174138e-06, 1.152588e-06, 1.132549e-06,
   1.114311e-06, 1.112536e-06 (falls 3.2, 2.9, 2.4, 2.2, 2.0, 1.8, 1.7, 1.6 percent per linearisation, 0.16 over the last 750; -0.21 percent over the last 1000 iterations and
   -0.07 over the last 250: flattened) -> 1.112536e-06 = 0.834 x dom9000g's. Shape leadcode/gpu/dom9000g2/dom9000g2_shape.npz, md5 1f5806c9ddb8d833db777299abfbbc45
   (mtime 09:17:15Z); c_l unchanged (fixed). MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960, closure at 1e4 L for both arms; leadcode/gpu/dom9000g2/
   dom9000g2_scan_*.json), dom9000g2 / dom9000g: whole-box N_f 5.105e-7 / 5.008e-7 = 1.019 ; 4.859e-7 / 4.750e-7 = 1.023 (both arms at the lobe above P, r 8.73,
   theta 0.19-0.20: the lobe maximum does not fall with the second 20750 iterations), whole-box N_v 1.019 ; 1.023, r <= 0.1 0.963, 0.1-2 0.885, 10-100 N_f 1.275 ;
   1.277 (its maximum moves from the y-axis at r 10 to r 14.13, theta 0.957; the 10-100 N_v 0.848), 100-1000 0.811 ; 0.818, outer quick-scan band (131 L to 1e4 L)
   N_f 1.006 ; 1.007, N_v 1.025 ; 1.023, N_v rms 1.006, whole-box rms 0.747 ; 0.748; h(P) - 1 -8.4e-9 ; +1.8e-12; x* 8.600065 (unchanged). Against X3 at 640: whole-box
   N_f 0.736, N_v 0.767. READING on my scans: the far band of the 9000 L row is unchanged by the budget (1.00-1.03 in the fit's own convention over 131 L to 1e4 L, and
   C_R / the formula-continued bands are the verifier's), inside the lead's [0.8, 1.25] = "the budget does not lower the 9000 L row's far band further" if the verifier's
   bands agree; the weighted objective and the whole-box rms fall by 17 and 25 percent while the lobe maximum rises 2 percent and the 10-100 band 27 percent: the
   second budget lowers the objective, the rms and several regional maxima (near-P x-strip 0.611 ; 0.613, 0.1-2 0.885, 100-1000 0.81-0.82) while the whole-box / lobe
   maximum rises about 2 percent and the 10-100 N_f maximum about 27 percent (contrast c6g2, item 15, where the second budget on 1000 L rows lowered the whole-box
   maxima to 0.61-0.74). Not a candidate; no decision attached. Chain state: 50 c6h9000 at outer 7 it 500 at 09:17Z (~09:50Z); chain 10 (58 / 59) starts after its done line.
   VERIFIER G139 (09:36:12Z) ON dom9000g2 (own evaluator; values CONFIRMED): (a) far band N_v over 1000 L-9000 L, formula continued, dom9000g2 / dom9000g 1.028 (16875 x
   512) / 1.024 (22500 x 384); own convention 1.028 / 1.023 / 1.018; C at the axis 6.559e-4 / 6.465e-4 = 1.015; 9000 L-1e4 L 1.005, r > 1e4 L 1.002; the higher-order
   coefficients change little (q1 4.961e-4 against 4.94e-4, +0.4 percent; q2, q3 within 0.1 percent): every ratio in [0.8, 1.25] on both N >= 16875 configurations, so by the rule "the budget does not lower the 9000 L row's far band further" (the lead's own
   numbers 1.017 / 1.005 agree). (b) stated without attribution: near-P N_f dom9000g2 / dom9000g 0.612 / 0.578 / 0.583 (16875 x 512 / 22500 x 384 / 11250 x 384; my x-strip
   ratios 0.611 ; 0.613), J 0.579 / 0.537 (eps 0.03 / 0.01). (c) whole-box N_f (A5, r <= 1000) 0.984 / 1.017 / 1.027 (whole-box ratios; at 16875 x 512 the maximizing location moves from next
   to P to the lobe above P, so that ratio is not lobe-to-lobe; at the other two configurations the maximum is at the lobe before and after; G139: "the fall is next to P
   and the lobe above P is unchanged, as in G91"; my scans give the lobe-to-lobe ratios 1.019 ; 1.023); against X3 near-P 0.401 / 0.395, whole-box
   0.645 / 0.756, J 0.380 / 0.342 (20750 + 20750 iterations beyond X3 on other rows: not an equal-budget comparison); identity c_l 5.5753626108, h(P) = 1 root -4.4e-8, x*
   8.6000654, h(P) - 1 +4.9e-8 / -4.8e-9 / +3.9e-7. For the report: "if 4.4 or 4.5 lists fits whose residual maxima are below X3's, dom9000g2 is one (near P 0.40 of X3)",
   under C3. This lane's provisional reading (far band unchanged; maxima redistributed, lobe unchanged) agrees with G139. (2026-10-19T09:46:42Z) (2026-10-19T09:19:02Z)

30. c6h9000 (chain-7f4 step 50; the m <= 250 cap row with rows to 9000 L, requested by the lead 2026-10-19T00:16:58Z as a DATA row: c6h (item 14; the m <= 250 member of
   the angular row, rows to 900 L, closure 1000 L) continued 20750 iterations at its fixed c_l 5.575362610642 with --inverse-radius 10000 --fit-radius 9000 (rows to
   9000 L, inverse domain and two-term closure at 1e4 L, as dom9000g / dom9000g2), 24576 x 1200, 14685438 rows, 94132 columns, inner 2500, check 250, damping 1e-8,
   K = 20750; memtest peak RSS 14,783,560 kB = 14.1 GiB = 15.1 GB (step 51; earlier notes wrote "14.78 GB", a unit slip: kB x 1e-6); host RSS sampled during the run
   6.9-10.3 million kB (6.6-9.8 GiB). The lead's reading fixed in 00:16:58Z item 2 on the verifier's rows, both
   N >= 16875 configurations: (a) c6h9000 / c6h in A5 whole-box N_f r <= 1000 and in N_f within 0.5 of P at most 1.1 on both = "the interior gain of the m <= 250 cap is kept
   with rows to 9000 L"; (b) c6h9000 / dom9000g2 (equal total iterations, differing in the angular cap 250 against 200) in N_v 1000 L-9000 L, formula continued, in
   [0.8, 1.25] = "the cap does not move the far band"; otherwise the ratios are stated): started 07:25:28Z (shared with 49 until 09:17Z, then alone), DONE 09:43:55Z, total
   20750 iterations; objective 9.090641e-06 (start = the c6h end evaluated on the 9000 L configuration; dom9000g started from c6g at 9.246879e-06 on its 960-angle rows)
   -> ends of the linearisations 5.487368e-07, 5.314650e-07, 5.178419e-07, 5.062776e-07, 4.962576e-07, 4.874544e-07, 4.796925e-07, 4.727552e-07, 4.709046e-07 (the first
   linearisation falls 94.0 percent, then 3.1, 2.6, 2.2, 2.0, 1.8, 1.6, 1.4 percent, 0.39 over the last 750; -0.52 percent over the last 1000 iterations and -0.15 over the
   last 250: flattened) -> 4.709046e-07 = 0.0518 x its start (dom9000g on 960 angles ended at 1.334388e-06 on its rows; the two objectives are on different row sets and
   weights, so their ratio 0.35 is not a residual ratio). Shape leadcode/gpu/c6h9000/c6h9000_shape.npz, md5 8eed5634a745e1329220b78086512c73 (mtime 09:43:55Z); c_l
   unchanged (fixed). MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960; leadcode/gpu/c6h9000/c6h9000_scan_*.json): (a) c6h9000 / c6h (c6h's closure at
   1000 L, c6h9000's at 1e4 L): whole-box N_f 4.920e-7 / 4.754e-7 = 1.035 ; 4.697e-7 / 5.088e-7 = 0.923 (both arms at the lobe, r 8.73-8.74, theta 0.19-0.20), near-P
   (2-10 x-strip maximum, at r 8.59 on the axis) 2.032e-7 / 3.293e-7 = 0.617 ; 0.612, r <= 0.1 1.024, 0.1-2 0.909, 10-100 N_f 1.052 ; 1.070 (N_v 0.84-0.86), 100-1000
   0.803 ; 0.814, whole-box rms 0.858 ; 0.863 (own-domain rms ratios: the two scan domains end at different closure radii; likewise the outer quick-scan bands have
   different extents, 131 L-1000 L against 131 L-1e4 L, and are not compared); h(P) - 1 -8.0e-9 ;
   +1.6e-11; x* 8.600064 (unchanged). On these numbers the (a) reading holds (whole-box <= 1.035 and near-P 0.62, both at most 1.1): the 9000 L rows keep the cap's
   interior gain and lower the near-P value by 0.62, as they lowered dom9000g's against c6g (0.66-0.68 on the verifier's grids, G91). (b) c6h9000 / dom9000g2 (same
   radial grid, fit radius, inverse domain, closure radius and total iteration count; different angular caps, 250 against 200, hence different angular quadratures and
   row counts, 14685438 against 11753238): whole-box N_f 0.964 ; 0.967 (both at the lobe), near-P 0.742 ; 0.711, r <= 0.1 0.461, 0.1-2 0.411, 10-100 N_f 0.381 ; 0.387
   (N_v 0.40), 100-1000 0.446 ; 0.415, outer quick-scan band 131 L to 1e4 L N_f 0.914 ; 0.916, N_v 0.682 ; 0.683 (N_v rms 0.708), whole-box rms 0.491 ; 0.495: the cap
   lowers the 0.1-2 band to 0.41, the 10-100 band to 0.38-0.39 and the 100-1000 band to 0.42-0.45, the near-P value to 0.71-0.74 and the lobe (the 2-10 maximum) by
   3.3-3.6 percent, and the outer band N_v to 0.68 on my band, which however starts at 131 L and so includes the region where the cap acts; the lead's band 1000 L-9000 L (formula continued) is the verifier's
   and decides (b). Against c6h's own 1000 L closure the far N_v of the 900 L-row fit, 5.2e-8 over 131 L-1000 L (640 scan; 5.3e-8 at 960), becomes 2.2e-8 over 131 L-1e4 L with the
   rows (both grids; not like-for-like in extent). Not a candidate; no decision attached. Chain state: chain 10 started 58 fxn16gb at 09:44:05Z (python 4073304) and 59 fxn24gb 90 s later;
   both 20480 x 720, 21500 iterations, shared GPU, expected ~11:05Z.
   VERIFIER G140 (10:10:51Z) ON c6h9000 (own evaluator, fit convention and formula-continued, N16875 q512 / N22500 q512 because m <= 250): (a) c6h9000 / c6h: A5 whole-box
   N_f r <= 1000 1.021 / 1.023 (both at the lobe, r 8.74), N_f within 0.5 of P 0.665 / 0.712: all four ratios at most 1.1, so by the rule "the interior gain of the m <= 250
   cap is kept with rows to 9000 L" (with the caveat that c6h9000 is c6h plus 20750 iterations on other rows, so the fall next to P mixes budget and rows; my scans 1.035 ;
   0.923 and 0.62 "do not contradict the reading"). (b) c6h9000 / dom9000g2, N_v over 1000 L-9000 L formula continued: 1.999e-8 / 3.290e-8 = 0.608 and 2.004e-8 / 3.282e-8 =
   0.610, outside [0.8, 1.25], so the ratios are stated (the lead's 0.621 agrees): c6h9000's band maximum sits at the outer end of its rows (8989-8998 L, theta 0.62-0.63)
   and its two band maxima, with the y-axis columns included (2.0033e-8 at 3944 L next to the y-axis) and excluded (2.0028e-8 at 8998 L), agree to 3e-4 (G140 as amended by G141: the earlier phrase 'the band is flat to 3e-4' was not measured and is withdrawn here too), while dom9000g2 reaches 3.29e-8 next to the y-axis at the inner end (1070-1141 L); so
   the difference sits next to the y-axis in the inner part of the band, where c6h9000 is at most 0.61 of dom9000g2; 9000 L-1e4 L 0.940 / 0.941; beyond 1e4 L 0.975 / 0.977
   (own convention in the closure 2.31e-5 for both); C at the axis 6.000e-4 (0.915 of dom9000g2's, 0.032 of c6h's); q1 4.690e-4, q2 -14.624, q3 -3.462e4 as dom9000g2.
   (c) J (857 labels) c6h9000 / c6h 0.766 / 0.771 (eps 0.03), 0.651 / 0.650 (eps 0.01); against X3 near-P 0.234 / 0.235, whole-box 0.631 / 0.730 (not equal budget: 41500
   iterations beyond X3, larger cap, other rows); identity c_l 5.5753626108, h(P) = 1 root -2.2e-8, x* 8.6000643, h(P) - 1 +5.3e-8 / -5.1e-9. This lane's provisional (a)
   reading agrees; for (b) my outer quick-scan band (0.68 over 131 L-1e4 L) could not decide and the verifier's 0.61 over 1000 L-9000 L stands. (2026-10-19T10:11:47Z) (2026-10-19T09:46:42Z)

31. fxn16gb (chain-10 step 58; the budget continuation of row 54, offered by this lane 05:52Z and accepted by the lead 06:18:36Z (SPEC v4.18) as a DATA row: fxn16g
   (item 24; d = -1.6e-2, stored c_l 5.5604082120) continued 21500 iterations at its fixed c_l from its end shape (md5 65d87bb7c4aa2be6c17263a033fc38c5), same settings
   (20480 x 720, inner 2500, check 250, damping 1e-8); the pair 58 / 59 is read by the lead's rule on the verifier's configurations: the v4.15 bracket is "kept at twice the
   budget" if L2(59) and whole-box N_f(59) are above 58's on both, "not kept" if L2(59) < L2(58), otherwise "the objective and the maxima disagree"; the lead's prediction
   before the results: L2(59) / L2(58) in [1.00, 1.15]): started 09:44:05Z (shared with the other continuation for most of the run), DONE 10:45:23Z (chain line; shape mtime
   10:45:22Z), total 21500 iterations (43000 since the transplant);
   objective 2.737838e-06 -> ends of the linearisations 2.495545e-06, 2.404943e-06, 2.343131e-06, 2.301977e-06, 2.269240e-06, 2.244087e-06, 2.222865e-06, 2.205423e-06,
   2.200885e-06 (the first linearisation falls 8.8 percent, then 3.6, 2.6, 1.8, 1.4, 1.1, 0.9, 0.8, then 0.21 over the last 1500; -0.15 percent over the last 1000 iterations
   and -0.06 over the last 250: flattened, where row 54 at the single budget was at -1.72) -> 2.200885e-06 = 0.804 x row 54's end and 0.517 x F2's L2 (the single-budget
   profile's reference; not an equal-budget comparison with F2). Shape leadcode/gpu/fxn16gb/fxn16gb_shape.npz, md5 0c57669fc0f4c24894a09043ade11306 (mtime 10:45:22Z); c_l
   unchanged (fixed). MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ; 24576 x 960; row 54 on the matched grids): whole-box N_f 7.070e-7 / 8.422e-7 = 0.839 ; 6.708e-7 /
   8.276e-7 = 0.811, the maximum now at the lobe above P (r 8.81 ; 8.80, theta 0.304) where row 54's was on the axis next to P (r 8.55 ; 8.56); near-P x-strip 5.761e-07 / 8.422e-07 = 0.684 ; 5.533e-07 / 8.276e-07 = 0.669
   (the near-P maximum falls by 31.6 ; 33.1 percent while the lobe maximum changes by +2.1 ; -1.3 percent); whole-box N_v 0.842 ; 0.811; r <= 0.1 0.846; 0.1-2 0.955; 10-100 N_f 0.691 ; 0.687; 100-1000 0.565; outer quick-scan band
   (131 L-1000 L, same closure) N_f 0.607 ; 0.603, N_v 0.692; whole-box rms 0.766; h(P) - 1 -2.3e-8 ; -1.6e-8; x* 8.588480415 -> 8.588480002 (essentially unchanged; a
   fixed c_l does not fix x*). The second budget lowers every full-angle radial-band N_f maximum of this row, to 0.565-0.955 of its previous value, with the largest falls
   beyond r = 100 (where the single-budget lower-end rows were highest, item 24); not every angular sub-band falls (the 0.1-2 y-strip maximum rises about 10 percent). The pair reading waits for 59 (item
   32). (2026-10-19T10:47:03Z)

32. fxn24gb (chain-10 step 59; the budget continuation of row 55, the second half of the pair of item 31: fxn24g (item 26; d = -2.4e-2, stored c_l 5.5524652878)
   continued 21500 iterations at its fixed c_l from its end shape (md5 e52a8be0f977eaa6398fb9d27302453d), same settings): started 09:45:35Z (shared with 58 for most of the run),
   DONE 10:46:40Z, total 21500 iterations (43000 since the transplant); objective 3.300646e-06 -> ends of the linearisations 2.829901e-06, 2.650899e-06, 2.525069e-06,
   2.438625e-06, 2.367948e-06, 2.312121e-06, 2.263351e-06, 2.222527e-06, 2.212127e-06 (the first linearisation falls 14.3 percent, then 6.3, 4.7, 3.4, 2.9, 2.4, 2.1, 1.8,
   then 0.47 over the last 1500; -0.34 percent over the last 1000 iterations and -0.14 over the last 250: flattened, where row 55 at the single budget was at -2.50) ->
   2.212127e-06 = 0.670 x row 55's end and 0.519 x F2's L2. Shape leadcode/gpu/fxn24gb/fxn24gb_shape.npz, md5 3ef7078f95aaba2c943bdedd836a1878 (mtime 10:46:40Z); c_l
   unchanged (fixed). THE PAIR AT TWICE THE BUDGET (43000 iterations each): L2(59) / L2(58) = 2.212127e-06 / 2.200885e-06 = 1.0051 (the single-budget ratio was 1.206; the
   lead's prediction before the results was [1.00, 1.15]); the second budget lowered row 55's objective by 33 percent and row 54's by 20 percent, so the gap closed from
   20.6 to 0.5 percent, and 59 is still falling faster than 58 (-0.34 against -0.15 over the last 1000 iterations). MY CROSS-CHECK SCANS (quick_scan_fit 32768 x 640 ;
   24576 x 960): whole-box N_f 1.319e-6 ; 1.332e-6, next to P (r 8.52, theta 0.022 ; 0.011; x* 8.582322), = 1.865 ; 1.985 x 58's (7.070e-7 ; 6.708e-7, at the lobe) and
   0.711 ; 0.695 x row 55's; near-P x-strip 1.319e-6 ; 1.332e-6 = 2.289 ; 2.407 x 58's (5.761e-7 ; 5.533e-7) and 0.711 ; 0.695 x row 55's; whole-box N_v 1.856 ; 1.979 x
   58's; r <= 0.1 0.770 x 58's (0.733 x row 55's); 0.1-2 0.691 x 58's (0.957 x 55's); 10-100 N_f 1.321 ; 1.333 x 58's (0.676 x 55's); 100-1000 1.202 x 58's (0.524 x 55's);
   outer quick-scan band (131 L-1000 L) N_f 1.110 ; 1.123, N_v 1.130 x 58's (0.508-0.512, 0.618 x 55's); whole-box rms 1.630 x 58's; h(P) - 1 -3.7e-8 ; -2.3e-8; x*
   8.582323575 -> 8.582322133 (essentially unchanged). READING BY THE LEAD'S RULE (SPEC v4.18) ON MY SCANS: L2(59) > L2(58) and whole-box N_f(59) > N_f(58) on both grids, so the v4.15 bracket is "kept at
   twice the budget" (the verifier's two configurations decide; for the whole-box maxima the margin is a factor 1.9-2.0 and the maxima sit at different places, next to P
   for 59 and at the lobe for 58; for L2 the margin is 0.5 percent). Facts to attach: (i) the objective gap between the two lowest exponents shrinks from 20.6 to 0.5
   percent under the second budget while 59 still falls 2.3 times faster than 58 over the last 1000 iterations (relative falls -0.338 against -0.148 percent); the recorded
   order at this budget is 58 below 59, its persistence under further continuation is not established, and a reversal in a third budget cannot be excluded (a
   possibility, not a trend); the bracket statement remains a statement about fits from transplanted starts at a stated budget; (ii) the residual-maxima order is not
   close: 59 stays above 58 by factors 1.865 ; 1.985 (whole-box) and 2.29 ; 2.41 (near P), the same order as at the single budget; 58's whole-box maximum against row 53's
   (fxn8g, the single-budget row with the lowest maxima) is 1.041 ; 0.949, changing sign between my grids; (iii) at 43000 iterations the two fits reach 0.517 and 0.519 of
   the 21500-iteration F2 reference L2; their second budgets lowered their own objectives by 19.6 and 33.0 percent (their parents were already at 0.643 and 0.775 of F2 at
   equal count), and this unequal-budget comparison lies outside the profile rule. Not candidates; neither changes a number of X3. Chain 10 ended 10:46:40Z ("chain10
   end"); a process listing at 2026-10-19T10:56:21Z showed 0 gpu_long_solve.py / gpu_chain processes of this lane (WORKLOG). (2026-10-19T10:49:03Z)
   VERIFIER G147 (11:06:52Z) ON THE PAIR 58 / 59 (SPEC v4.18; N11250 q384 / N16875 q512; md5s match): L2 2.2009e-6 / 2.2121e-6 (ratio 1.0051); whole-box N_f 58 1.167e-6 /
   6.311e-7, 59 1.344e-6 / 1.301e-6 (ratios 1.152 / 2.062); last-1000 changes -0.148 / -0.338 percent; within 0.5 of P 59/58 2.42 / 2.54, N_v r <= 1000 1.16 / 2.06, J 2.31 /
   2.38: READING "kept at twice the budget" CONFIRMED, with (b) the L2 gap falling at every linearisation of the continuation (5.63e-7 at the start, then 3.34e-7, 2.46e-7,
   1.82e-7, 1.37e-7, 9.87e-8, 6.80e-8, 4.05e-8, 1.71e-8, 1.12e-8; each of the four complete linearisations before the last removed more than the 1.12e-8 that remains, the last, of 1500 iterations, removed 5.9e-9; wording per G148), so "the order in L2 is a fact at
   43000 iterations only" and the whole-box order has a large margin measured only at the end; (c) neither continuation is at equal budget with F2 and both may still be
   falling; (d) for the report, 58 (c_l 5.5604082, 43000 iterations, not a candidate) is BELOW X3 at 16875 x 512: whole-box N_f 0.9225 (at the off-axis lobe r 8.80, theta
   0.304), within 0.5 of P 0.750, N_v r <= 1000 0.924, far N_v 1.025, J 0.800 / 0.774 (G148's exact ratios 0.924469 and 0.774485; first written 0.925 / 0.775 from four-digit displays); at 11250 x 384 whole-box 1.689 x X3 (the under-resolved lobe), near P 0.823; 59 is
   above X3 on every measure (whole-box 1.95 / 1.90, J 1.85); not an equal-budget comparison. This lane's provisional reading and attached facts agree with G147. (2026-10-19T11:07:43Z)

7. c6gF (step 32; the equal-budget FREE control of c6g: the lead's c6gF_start_shape.npz = the seg3g end enriched to m <= 200, md5
   e6827f98c5a3195d593679b42fc15880, c_l free from 5.576370935; 20480 x 960, inner 2500, check 250, damping 1e-8, K = 20750): DONE 16:09:14Z,
   objective 4.171e-6 (start on the 960 grid) -> 1.664196e-6 (0.399 x); c_l 5.576370935 -> 5.576371155 (+2.2e-7; no slope resolved; my
   first note gave +3.0e-7 from the check at 19500 iterations, corrected at 16:33Z); shape
   leadcode/gpu/c6gF/c6gF_shape.npz, md5 0398af3f08a2a4f75e42c846edbaa375. EQUAL-COUNT COMPARISON c6g (fixed c_l 5.5753626) / c6gF (free,
   c_l 5.57637): objective ratio 0.971 (2500), 0.971 (5000), 0.972 (10000), 0.972 (15000), 0.973 (20000), 0.973 (20750) at the linearisation
   ends, 0.960 to 0.973 over all check points (lead's reading of the same logs): the fixed-c_l arm is 2.7-4 percent lower at every count (on
   m <= 150 the same pair gave 3.8 percent), again with different start shapes. The pair is read
   by the lead's 12:02Z rule on the verifier's rows with the far band fixed in advance at all r > 1000 (14:04Z). OUTCOME: c6g wins its pair on the verifier's rows (G74,
   16:44:40Z); candidate by the 14:02Z rule (lead 16:46Z). Details: c6g wins against c6gF on every part and in every reading (margins quoted by the lead from G74: whole-box
   N_f 0.937 / 0.832 / 0.938 on the configurations with N >= 16875, next to P 0.935-0.938 on all four, N_v r <= 1000 0.936-0.987, far N_v
   1.000-1.003 (c6g at most 3e-9 above, inside c6gF's spread 2.4e-8), 857-label J 0.937 / 0.937), and by the lead's 14:02Z rule (the pair
   winner with the lowest whole-box N_f on the verifier's configurations) c6g is the TEAM CANDIDATE (lead 16:46Z: "X3"; whole-box N_f
   6.83-7.16e-7 on N >= 16875 against s2g's 1.44-1.51e-6): not an endpoint; outstanding for G20 (b): the domain columns at the candidate's
   basis (steps 33-34, running), the angular row (fxd1g step 35; c6h / c6hF as a refinement row), the report text. My
   cross-check scans (lead convention, 32768 x 640), c6g / c6gF: 2-10 N_f 6.94e-7 / 7.39e-7, N_v 1.94e-7 / 2.07e-7, 0.1-2 2.86e-8 / 2.93e-8,
   10-100 8.15e-8 / 8.36e-8, 100-1e3 1.64e-8 / 1.68e-8, r > 1e3 1.30e-8 / 1.30e-8, rms 7.05e-9 / 7.34e-9, h(P) - 1 -8.8e-9 / -8.7e-9: c6g lower
   in every band except the far band (equal), by 6 percent next to P.
6. Definitions and provenance for this section. Objective = the lead's weighted discrete residual-vector norm: fit rows res/den on the
   polar grid points with 1e-4 <= r < 0.9 R_shape (shape units) and every second angle, weights sqrt(14000 / N_rows) x max(1, (0.04 / r)^2),
   den = 1 + |3 + ht| (the "log" objective), plus the source row 20 (h(P) - 1) and the two centre rows E, D2 (centre_fit.py); not a continuum
   L2 norm. Normalizations of the quoted maxima: N_f uses D_f = |W_1 rho_x| + |W_2 rho_y| + |rho| (SPEC N_f), N_v uses D_v = |rho| +
   |X . grad rho| + |U . grad rho|; "2-10 flux" and "N4" in the lead's scan tables are the N_f and N_v band maxima. Grids: fits 20480 x 720
   (960 for m <= 200), lead scans 32768 x 640 and 24576 x 960 (quick_scan, closure at R_shape = 1000 for all lead fits), verifier
   configurations N11250 q384 M479 and N16875 q512 M639 (own generator, formula to 7.652e6), exports 24576 x 384 / 576. J = the spread over a
   label set of the characteristic integral of R/rho along backward characteristics from r = 20 to within eps of P (lead char_defect.py,
   185 labels; verifier vchar_dense.py, 857 labels); distinct from the Jacobian J of the fit. c_l "identity" = (1 + psi_xy(0))/3 from the
   inverse; "identity-free" = the root of h(P) = 1 (verifier). Physical radii: R_c = L R_shape with L = 7.6514 for these fits.

## 4. Current verdict (2026-10-18T09:26Z, shift 4; (a)-(f) from shift 2 in the external referee's wording, astra/softness/answer.md; (g)-(i) shift 4)
What this lane has established numerically (independent discretisation: polar Chebyshev-Radau x Fourier on a disk r <= R with the
SPEC N3(a) homogeneous-extension closure and the canonical modal Green function; oversampled least squares with exact Jacobian; all
code in src/, tests in tests/, data and logs in artifacts/):
(a) Residual levels. Between nodes, the discretised profile equations are satisfied to a normalised residual of about 1e-6 rms away
    from the x-axis source P IN MY DIVIDED-FORM NORMALISATION (the verifier's evaluator, G45, gives for the same states maxima of
    3e-5 .. 6e-5 in the band 10-100 and 2e-4 .. 3e-4 (N_v) in the outermost band next to R, rms 2e-6 .. 3e-5: the "1e-6" is an rms in my
    norm, not a maximum in theirs), with a band next to P: at (256,64), R = 3000, shells |X-P| < 0.5 / 0.5-1 / 1-2 / 2-4 have rms 1.4e-5 /
    1.8e-5 / 1.7e-5 / 1.1e-5 and max 4e-5 .. 9e-5; a radial map clustered at P (4x) with 128 angles reduces them to 2.8e-6 / 5.1e-6 /
    3.9e-6 / 1.2e-6 (max 2e-5), the level of the lead's construction; (384,96) unclustered reaches a near-P max of 3.1e-5 and an
    rms of 8.6e-7 overall. Independent finite-difference evaluation (src/check_fd.py) agrees; the verifier's evaluation of the exported
    states is requested.
(b) c_l is weakly constrained by the least-squares residual of this discretisation. Verified facts: at the construct1 projection + 6
    Gauss-Newton iterations ((256,64), R = 3000; c_l 5.57646) the smallest first-order residual-vector change per unit change of c_l is
    alpha = 9.91e-4 (1/|R^{-T} dc_l/db|, independently reproduced by the referee to 4 digits as an upper bound achieved by the exported
    direction), against the residual norm |F|_2 = 1.21e-3 (rms 4.7e-6); identity-consistent perturbations of that state by +-1e-2 in
    c_l along the direction raise |F|_2 by only 3.5 percent (referee; nonlinear: the residual-vector change is 3.2e-4, far above the
    linear 9.9e-6, so the straight-line extrapolation to larger c_l changes is NOT justified); unpinned Gauss-Newton iterations drift
    with monotonically decreasing rms (159 iterations 5.5786 -> 5.4276 at R = 3000, rms 2.06e-6; 150 iterations 5.5763 -> 5.2923 at
    R = 1000, rms 2.93e-6; verified by the referee from the .dat histories), but these runs use different weights/domains and are not one
    constrained family; the lead's exponent-step estimator at the projection state gives dk* = -0.127 (where the (256,64) L2 minimiser
    lies, with 10 percent of |F| along the direction: a systematic component). alpha decreases with resolution faster than the floor:
    (256,64) 9.9e-4 at |F| 1.2e-3; (320,80) 2.9e-4 at 4.7e-4; (384,96) 6.1e-5 at 2.3e-4; clustered (256,128) 9.0e-5 at 2.0e-4; and is
    independent of R (1e3 .. 1e4). The fixed-c_l residual curve (3.16 item 4d) is flat to 20 percent over +-0.02 around 5.5763 at
    (256,64) clustered (near-P max 2e-5 for every s, h(P)-1 -2e-4 for every s); the location of its L2 minimum moves by >= 0.05 between
    grids. Verifier G45 (03:45Z) confirms in its own evaluator: the +-0.01 perturbations are identity-consistent and undetected by
    residual, J and h(P) at the near-P level 1e-4 (N_f) / 3e-5 (N_v); the c_l = 5.29 and 5.59 states sit at the same residual level within
    a factor 1.6 next to P; along the m(s) states every near-P diagnostic improves monotonically toward larger s; and (caveat adopted)
    these states are 15-60x worse next to P than the lead's c6c segment 1 (flux 2.2e-6, J 1.2e-6, |h(P)-1| <= 1.9e-8), so they say nothing
    about whether the c6c level fixes c_l. Verifier G47 (04:34Z) then added my exported direction to the lead's c6c segment 1
    (near-P flux 2.28e-6, h(P)-1 8.5e-9): a c_l offset along it of -1e-3 raises the near-P flux maximum 1.43x and J(0.01) 11.6x, of
    +3e-3 2.9x / 9x, of +-1e-2 23-30x / 250-400x, with the 0.1-2 band unchanged; so at THAT residual level offsets of a few 1e-3 along
    this (fixed, not re-optimised) direction are registered, while at my level they are not. What this does and does not show: the attained residual of an L2 fit does not substantiate an exponent
    accuracy (for any construction with comparable residual, including the lead's); it does not show algebraic non-uniqueness, an O(1)
    admissible interval, or non-uniqueness of the continuous profile.
(c) Structure of the soft direction (referee's decomposition of my exported direction, verified): it is a COUPLED near-null direction,
    not a frozen-field transport mode: the frozen-W transport part of J v has norm 19.5 and is cancelled by the velocity and c_l
    feedback to 9.9e-4; 77 percent of |J v|^2 lies outside |X-P| < 2 and r < 1; 91 percent of its effect on c = int rho_1 r^-2 dr
    comes from 5 < r < 100 (5 percent from r > 100). My earlier description (characteristic-label modes with cost only in the sliver
    at P; NOTES_FOR_LEAD 01:55Z and 02:15Z) is therefore withdrawn as a mechanism; the sliver at P remains the place where the lead's
    analysis 13 locates the selection of c_l, but the measured discrete softness is not localised there.
(d) Pinning tests (all at the c_l = 5.5934 state unless stated; first-order; the constraint defects at that state are nonzero, so these are
    tests of whether c_l can change without changing the diagnostics, not tests at feasible constrained solutions): with h(P) - 1 = 0
    imposed to first order alpha 3.24e-3 -> 3.27e-3; with 12 / 24 characteristic-matching rows (exact autograd gradients, validated)
    3.29e-3 / 3.43e-3; with 44 axis-transport rows 5.1e-3; with a degree-10 Taylor patch at P (48 rows on |X-P| = 1.5) 1.80e-2, a factor
    5.5 (a real effect, far from a determination; the patch's velocity fit has truncation 7e-4 .. 3e-3 and does not enforce W_1(P) = 0 or
    (h-1) g(P) = 0, so it is not a decisive test of local matching). Near-P row weighting test running (runs/npw_*.log).
(e) Consequence for the team's candidate (referee's wording adopted): "the construction produces a representative exponent c_l ~ 5.5763
    with variation ~1.2e-4 across the tested variants; this measures reproducibility within the family, not an absolute uncertainty. An
    independent disk discretisation exhibits a verified direction near c_l = 5.57646 with residual cost 9.9e-4 per unit first-order change
    of c_l against a residual norm 1.2e-3; identity-consistent perturbations changing c_l by +-0.01 raise that residual norm by 3.5 percent;
    unpinned runs show decreasing least-squares residual while c_l drifts substantially. These findings show that the attained disk
    residual alone does not substantiate the quoted exponent accuracy; they do not establish algebraic non-uniqueness, an O(1) interval,
    or non-uniqueness of the continuous profile. The coupled regularity selection and the absolute accuracy of c_l remain unresolved."
    The shift-1 agreement of this lane's states with the candidate to 0.1-0.2 percent (3.12) carries no independent weight.
(f) Bug found and fixed on the way (relevant to SPEC N3(a)): the homogeneous-extension tail must use the exterior derivative
    k cos(theta) Theta_R - sin(theta) Theta_R' (SPEC v4.4 corrected); the lead's code already did.
(g) The nonlocal inverse of the lead's candidate is right (shift 4, section 3.17 item 7, referee-audited astra/raycheck/answer.md): at 51 export
    nodes of c6d_seg1 the exported velocity differs from the canonical sublinear inverse of the saved density, computed by an unrelated method
    (paired-ray quadrature of the analytic source integrated to 1e18, no modes, no disk, no closure; converged across angular and ray rules;
    the referee's own CPU modal inverse agrees at three nodes), by 9e-10 within 0.5 of P (2e-11 relative), 4.3e-8 within 2.5 of P, 1e-9 at r = 20,
    5e-9 at r = 100 and 1.5e-8 at r = 300; the implied change of the normalized residual is at most 3e-9 (median 3e-11) against residual maxima
    6.8e-7 (next to P) and 1e-7 .. 1.5e-7 (r = 20-300). The centre identity holds with c from the same method to 2e-8 (c_l to 7e-9). An
    independent residual assembly at the nodes reproduces the export's residual to 5.8e-9 with the same maximum. Sampled comparisons, not
    uniform bounds; the export's inverse domain is 1e4 shape units (the fit's is 1e3).
(h) Far-field truncation error of the fit's inverse (section 3.17 item 7 (x)): the two-term closure at R_shape L changes the velocity the fit
    used by 2.6e-9 (next to P) and 1.3e-8 (r = 20-300) in normalized-residual terms at the candidate's R_shape = 1000 (0.4-10 percent of the
    residual), by 2.7e-8 / 2.0e-7 at R_shape = 333 and by 8.1e-7 / 6-7e-6 at R_shape = 111 (equal to and 30-150x the interior residual): the
    far field is not what limits the candidate's residual, and bounded-domain fits below R_shape ~ 300 must be read in their own convention.
(i) Domain study hosted for the lead (section 3.17 item 2; fit convention; verifier G64/G65): fits on R_shape = 333 and 111 from the global
    state (1000 LSQR its each) keep the near-P maximum at 2.4e-6 .. 2.6e-6, J at 1.5e-6 .. 2.1e-6, h(P) = 1 to 5e-8 and move c_l by +6e-7 and
    +2.2e-6; dom90 (R_shape 100) segment 1: 2-10 flux 2.75e-6 (1.13x), 10-100 7.53e-7 (1.04x), c_l +4.6e-6 (segment 2 running). The lead's
    fixed-c_l result (08:17Z: c_l fixed 1e-3 below the free fit reaches a near-P flux max of 6.8e-7 on c6f) is being tested on the domain
    bases (fxd300 running; fxd90 next shift).
Open (updated 2026-10-18T09:26Z): (i) whether c_l is determined at the lead's level is now being decided by the lead's fixed-c_l fits on c6f
(-1e-3 reached 6.8e-7 near P; -1e-2, -3e-3, +3e-3, +2.4e-2 queued) and their same-budget controls; this lane's grids cannot reach that level
(section 4(b) stands as a resolution statement); (ii) the lane's own second solver did not converge to the candidate at the 1e-6 standard
(3.16); (iii) r > R_shape L is not covered by (g)-(h); (iv) the dom90 reading and the fixed-c_l domain fits are pending (RUN_STATUS).
Older open list (05:34Z): (i) the lead's tangent-cost test is done (244 basis: sigma 3.6e-3 per unit c_l and falling, dcl* +2e-4,
NOTES 04:39Z; verifier G49/G51: c_l not determined to 1e-3 at the 244 and 302 levels); their fixed-c_l fits at 5.60 (244 basis from
05:12Z, 302 after) decide whether an offset of 2.4e-2 is excluded at those levels; (ii) the near-P-weighted objective did not determine c_l
on my grids (3.16 4d, runs/npw_*.log); (iii) the fixed-c_l residual curve m(s) in my representation is done (3.16 4d: flat, grid-dependent
minima); (iv) B_3 (not meaningful from this lane without c_l); (v) the lead's domain study is running in this lane (3.17 item 2).
This is not a NO result: states with residual 1e-6 away from P exist for c_l over a wide range in this discretisation, and the near-P
band is shared by every construction; it is a precise statement of what the numerics can and cannot establish about c_l.

The homotopy explorations of sections 3.1-3.11 (c_l0 = 3 family, compactified and disk closures) are documented for the record:
they produced no candidate, and the compactified formulation with frozen gamma was found to pin c_l = 1/gamma (3.9) and to
leave far fields unresolved (3.11). Sections 3.12-3.15 (shift 1 reproduction of construct1 by square collocation) stand as records
of the square-collocation states; their between-node residuals are 1e-5 .. 4e-3 (verifier G16/G24) and their c_l values are
positions along the soft direction of (b).

(j) GPU solver (shift 5, section 3.18). The lead's Gauss-Newton / LSQR fit was ported to the GPU: the same algebraic operator with a
    different floating-point summation order, whose tested full-grid products agree with the lead's CPU implementation to 3.2e-14 (matvec)
    and 1e-13 (rmatvec) on sampled vectors; acceptance and every quoted number come from the lead's CPU objective and the lead's and
    verifier's evaluators. It runs 80-110x faster per iteration and was accepted by the lead for production (12:02Z). The s2g / seg3g pair
    below was computed with it at equal LSQR counts (20750 iterations each, inner 2500, check 250, damping 1e-8; the setting kept after a
    three-arm test of 2500 iterations in which neither lower damping nor reorthogonalisation passed the lead's 3 percent rule); the
    angular-enrichment run c6g has the same count when complete. The port is a tool for producing fits, not a verification instrument.
(k) What the long continuations showed on the m <= 150 basis (375 radial functions). (1) The LSQR "predicted" column of the lead's
    long_solve (and of my port) lacked the damping term res2 of the LSQR recurrence (lead's finding); the explicitly evaluated linear
    residual |f + J S x| predicts the norm of the trial objective to 1e-7 .. 5e-6 relative at every check, which supports the scalar
    prediction of each step but does not establish exact linearity, exact derivatives or convergence of the linear solve. (2) Continued
    for 20750 iterations at the fixed c_l 5.5753626 (s2g, objective 8.47e-6 -> 4.10e-6, -52 percent) or free (seg3g, 7.08e-6 -> 4.26e-6,
    -40 percent, c_l drifting +6.9e-6 only), the decrease slows to 0.6 percent per 2500 iterations; at that point lowering the damping
    changes nothing and reorthogonalisation gains 1.3 percent per 2500: the distance to the least-squares minimum of the basis remains
    undetermined. (3) The fixed-c_l continuation RAISED its whole-box normalized residual maximum (6.5-7.0e-7 at its 750-iteration start ->
    1.42-1.44e-6, verifier) while lowering the 10-100 band by 1.7-2.2x and the axis residual q0 by 3x; the free continuation lowered its
    maximum (2.1-2.3e-6 -> 1.57e-6); the remaining maximum on both is the angular ripple at the basis cap frequency (omega 304, 2 m_max =
    300) in the strip next to P where the small transport terms divide it (verifier's maps). The L2 objective and the near-P maximum are
    therefore not ordered alike, and the YES standard (G20 (b)) reads the maximum. (4) At equal budget the fixed-c_l fit is 3.8 percent
    lower in the objective and 9 percent lower in N_f than the free fit from the other c_l (5.57637; different start shapes); its far N_v is
    equal within the configuration spread over all r > 1000 but 3 percent higher over the fit band 1000 <= r <= 1000 L: the lead's rule
    selects s2g under the first reading and seg3g under the second (the band endpoint was not fixed before the measurement; both are
    reported), a margin the rule reads and not a determination of c_l; the pre-continuation candidate fxm1o2i250 is not ordered with either
    (lower N_f and J, higher N_v).
(l) Angular enrichment (m <= 200, 20480 x 960, 75382 columns, 10.2 GB RSS): continuing the s2g end with 50 more angular functions per radial
    function on a denser angular fitting grid (which alone changes the start objective from 4.097e-6 to 4.050e-6) lowers the objective by
    42 percent in 1000 iterations and by 55 percent in 7500 (4.05e-6 -> 1.83e-6) at the same fixed c_l, where the m <= 150 continuation
    gained 0.6 percent per 2500 iterations; at the full budget of 20750 iterations the objective is 1.619e-6 (0.40 x) and still falling 2
    percent per 2500. This substantially lowers the attained objective in this continuation; it is not by itself an approximation-theoretic
    floor of the smaller basis nor a diagnosis of every earlier fit (no matched m <= 150 run on the 960 grid). On the first iterate (2500
    its) the verifier measured the near-P maximum at 0.70-0.72 x s2g's and J at 0.60-0.66 x; at the end (20750 its, G73 15:30Z) the
    whole-box N_f is 6.8-7.2e-7 over four configurations (0.48 x s2g; level with the early-stopped fxm1o2i250's 6.5-7.0e-7), N_v for
    r <= 1000 0.48 x, the 857-label J 1.39e-6 / 1.60e-6 (0.44 x s2g; half of fxm1o2i250's 2.74e-6), the far N_v beyond the fit radius
    1.07-1.08e-6 (0.7-1.5 percent above s2g with the evaluator's A5 correction, below it without; a band no fit has moved). c6g is the
    first audited fit with both the lowest whole-box N_f range and a J below fxm1o2i250's. Against its equal-budget free control c6gF
    (20750 its, objective 1.664e-6, c_l 5.57637 drifting +2.2e-7) it is lower on every part of the lead's 12:02Z rule on the verifier's
    rows (N_f 0.94, next to P 0.94, N_v r <= 1000 0.94-0.99, far N_v equal within the spread, 857-label J 0.94; G74 16:44Z), and the lead
    declared it the team candidate at 16:46Z (not an endpoint: the domain columns at its basis, the m <= 100 row and the report text are
    outstanding). On the objective the fixed-c_l arm is 2.7-2.9 percent lower than the free arm at every equal count, as on m <= 150.
(m) Far field (section 3.17 item 7 (xi)): on one fixed older density (c6d_seg1, m <= 100) the closure error of the inverse at R_shape 1000 /
    333 / 111 shape units is 2.3e-9 / 2.0e-8 / 3.5e-7 next to P and 1.3e-8 / 1.8e-7 / 3.2e-6 at r = 20-300 (normalized residual impact at
    51 sampled export locations with the denominator frozen), with secant exponents 1.96-2.61 between the sampled radii, broadly compatible
    with the referee's conditional leading-strain exponent 3 - 3k = 2.46 but not establishing the asymptotic regime. At the standard closure
    radius 1000 the impact is 0.34 percent of the sampled near-P residual maximum, 1 percent at 0.5-2.5 from P, and 9-14 percent of the
    sampled maxima at r = 20-300. The fixed-c_l domain series 1000 / 333 / 100 (fit convention, m <= 100) agrees within 16 percent in the
    near-P and 10-100 maxima: the tested closed fitting problems have relatively stable interior residual maxima; the small-domain rows show
    substantial sensitivity to the exterior continuation and do not establish a clean full-plane domain limit, and candidate-specific
    domain and refinement checks (chain steps 33-36) remain necessary for the stated standard.
(n) Shift 6 (2026-10-18T17:24Z onward; the 24-hour minimum since T0 elapsed at 17:37:14Z; section 3.18 items 8-13, 3.17 item 7 (xiii)-(xv);
    wording corrected after the referee audit astra/shift6audit, 20:48Z). The candidate's exported velocity was cross-checked on X3 itself by the
    real-space paired-ray method at 52 interior targets (r <= 300; inverse domain 1e4 L as for X1): componentwise discrepancy 1.0e-9 within 0.5 of
    P, 3.6e-8 at 0.5-2.5 from P, 7.7e-12 .. 1.5e-8 at r = 0.1 .. 300; frozen-denominator residual impact 0.47 percent of the sampled |R|/D_v within
    0.5 of P and 4.7 percent at 0.5-2.5 from P (regional maxima, 51 defined ratios); finite quadrature (S = 1e18), sampled, not uniform; the lead
    entered it in section 4.5. This is a velocity cross-check at sampled points, not a third evaluation of every residual diagnostic or of J; the
    residual tables are the lead's and the verifier's on their stated grids and conventions. The 90 L domain column at the candidate's basis
    (dom90g) depends on its exterior continuation (closure at the matching radius 100 L against the saved formula continued globally) by 6.6e-6
    (within 0.5 of P) to 6.5e-5 (r 20-300) in frozen-denominator terms, about 100 times its sampled closure-convention residual near P and 30-300
    times its largest interior N_v (verifier G86 addendum, grid maxima: 9.4e-6 against 6.0e-8 within 0.5 of P, ratio 156), so the small-domain
    column is a stability observation within a closed fitting problem; for the 300 L column the lead's near-P N_f maximum changes from 3.45e-7
    (closure) to 3.99e-7 (formula continued to 1000 L), a difference of maxima, not a pointwise measurement. The far-field N_v band of the candidate
    (1.10e-6 at r 3.7e4 physical = u 4858, next to the y-axis; other fits 1.08-1.47e-6) lies in the uncollocated continuation of the last spline
    piece (last interior knot u 446; fit rows end at u 900 = 44 percent of that interval in q; the fit's rows end at 900 L, not 1000 L, which
    corrected the report's "fit domain" wording), and the family's far-field first correction is not free: under the conditional expansion
    Theta_1 is determined by Theta_0 ((c_l - 1) B = k V_r A + V_theta A'; referee, lead analysis 14 and verifier G81 agree on the algebra), and on
    c6g the stored Theta_1(pi/2) differs from the forced value by Delta_1 = -4.1e-3 (1e-4 of |Theta_1|; relative residual coefficient C_R = 0.0187),
    a first-order inconsistency common to the fits measured, whose term alone would give a signed R/D_v of 2.9e-6 at the band maximum; the first
    two series terms nearly cancel there and the r^-2 and third-order terms (about 5.7e-7 and 6.7e-7) make up most of the measured 1.1e-6 (lead
    series, verifier G84 / G88: measured/series 0.87 near the axis at u 4700, 0.98 at 9504). The lane's chain runs at the candidate's basis and c_l
    delivered the domain pair (dom90g, dom300g: lead A4 "AGREE" on the lead's scans; on the verifier's evaluator both fall below the two-sided lower
    bound 2/3 of the 2-10 ratio at 16875 x 512 (0.62), being lower, G77 / G86), the resolution rows fxd1g (m <= 100; angular row 100 / 150 / 200:
    whole-box N_f 3.12e-6 / 1.42e-6 / 6.9e-7, J 5.3e-6 / 3.1e-6 / 1.4e-6, each of the five prescribed diagnostics decreasing, the far N_v from 150
    to 200 only by about the configuration spread, G89 / G90) and fxb1g (244 radial; its far N_v is 6.4 percent above the 375 row with A5, G89
    addendum), and the fourth domain / far-field row dom9000g (rows to 9000 L): on the verifier's evaluator (G91) its far N_v maxima are 0.025-0.035
    of c6g's on both far bands (1.10e-6 -> 3.2e-8 over 1000 L-9000 L; 9.3e-7 -> 3.3e-8 beyond 1e4 L, formula-continued), near-P N_f 0.66-0.68, J
    0.64-0.66, N_v r <= 1000 0.66-1.02, with the 2-10 ratio 0.656 at 16875 x 512 below the lower bound 2/3 (lower), and on the lead's tools the axis
    mismatch Delta_1 falls by the factor 0.035. Whether this fall is due to the added rows, the enlarged inverse domain and grid, or the further
    budget is separated by steps 45 (c6g2, budget on the old domain) and 47 (c6gR4, old rows with the 1e4 L inverse domain), both pending, with the
    free control dom9000gF (48) queued as a data row; c6h (m <= 250), c6hF and the c_l-offset rows 37-40 are running or queued. This lane's verdict
    is unchanged in kind: X3 has small sampled residuals on the lead's and the verifier's grids (about 7e-7 in N_f next to P and 1.1e-6 in the
    far-field N_v on the unfitted continuation, 2e-7 in N_v inside r <= 1000), its exported velocity is cross-checked at 52 targets, the short-
    domain fits show substantial dependence on the exterior convention, the far band of the family falls by a factor 30-40 when rows are placed
    where it sits (verifier band maxima; attribution pending the controls), and X3 remains the designated candidate by the pre-registered rule;
    not a proof; c_l is quoted only as the pair of values 5.5753626 (fixed) and 5.5763712 (free control) at which fits of comparable quality exist,
    an empirical range, not an enclosure; no NO argument. The team's endpoint (G20 (b)) is read by the verifier; G91 leaves it open.
(o) Shift 7 (2026-10-18T23:17Z onward; section 3.18 items 16-23; first written 03:45Z, rewritten 2026-10-19T04:05:14Z after the external referee audit astra/shift7audit
    (31 findings, all applied; pre-audit copy runs/NUM_REPORT_pre_shift7audit.md); steps 54, 55, 48, 56, 57, 49, 50 were still running or queued). The controls
    queued in (n) are in. (1) BUDGET (c6g2 = X3 + 20750 iterations on its own rows, item 15; verifier G98): the far band and C_R do not move (0.993-1.003, 1.0026);
    the interior maxima fall to 0.61-0.74 (whole box), 0.50-0.54 (near P), 0.48 (J): one continuation shows that the interior diagnostics still improve with the
    iteration count while the far band does not (within the resolution of the measurement). (2) INVERSE DOMAIN (c6gR4 = X3 + 20750 iterations with the same fitted
    radial extent, the inverse domain and closure moved from 1000 L to 1e4 L and the radial grid changed with it, item 17; verifier G108, lead cross-check, my scans
    agree): the interior is the budget row's to within 0.6 percent (whole-box A5), 0.8-1.6 percent (near P), 8 percent (J) and 11 percent (one band / the lobe on one
    grid), while the formula-continued far band 1000 L-9000 L falls to 0.27 of X3's and C_R to -0.024 of X3's (sign reversed): the "falls" branch of the
    pre-registered rule. The successive ratios X3 -> c6gR4 (x 0.27, inverse domain) -> dom9000g (x 0.10-0.11, rows to 9000 L) multiply to the measured 0.028-0.029.
    So the far residual of these fits is strongly sensitive to the inverse domain, the closure and the fitted radial extent; these controls do not establish its cause
    in, or its implications for, an exact profile. (3) ANGULAR CAP m <= 250 (c6h / c6hF, items 14 / 16; verifier G96 / G104 final): the interior falls further (near
    P 0.33-0.41 of X3, the 0.1-2 to 100-1000 bands 0.4-0.5, the lobe above P 0.96-1.00 of the budget row), the far band stays; in the fixed / free pair the whole-box
    and r <= 1000 maxima agree to about 1 percent with differences of both signs inside the configuration spread, the free control is lower next to P (3-11 percent,
    inside the phase spread) and beyond r = 1000 (0.1-0.4 percent), the fixed row is lower in the 857-label J (2-3 percent, beyond its spread); by the letter of the
    selection rule the free control wins this pair on whole-box differences below the resolution of that maximum (G104 (b), (c)); the candidate is unchanged (decided
    at m <= 200). (4) THE c_l PROFILE at equal budget on the lead's 375 x m <= 150 basis (rows 37-40, 52, 53; items 18-23; verifier G109, G111, G114, G115, G118
    confirm rows 37, 38, 39, 52, 40 to 0.5-2.5 percent of my first-grid scans; row 53 has only the lane's provisional reading): over nominal transplant offsets
    d = -8e-3 / -4e-3 / -2e-3 / -1e-3 / 0 / +2e-3 / +3e-3 / +2.4e-2 from F0 (stored c_l 5.5683739 to 5.6004662), L2 / F2 = 0.741 / 0.858 / 0.926 / 0.962 / 1 / 1.078 /
    1.115 / 2.036 and whole-box N_f = 0.68 / 1.15 / 1.39 / 1.44 / 1.585 / 1.80 / 1.92 / 4.61 e-6: the L2 objective and the whole-box maximum increase with the stored
    exponent across all listed rows (other band diagnostics need not: the physical 10-100 band rises by 3 percent from -4e-3 to -8e-3, and the outer quick-scan band
    of the -8e-3 row is 1.7 x F2's); the secant slopes are nonuniform and the sampled L2 is not convex over the full set. Every row from -8e-3 to +3e-3 is "not
    determined" (or, for -8e-3 under the literal two-sided reading, "undecided") by the lead's pre-registered rule and only +2.4e-2 is "excluded"; the smallest
    observed objective is at the lowest tested exponent, so the lower end of the tested span is not bracketed. Row 54 at d = -1.6e-2 (item 24, 2026-10-19T04:53:19Z; verifier reading
    pending): L2 0.643 of F2 (lower still) but whole-box N_f 0.50-0.53 of F2, UP from row 53's 0.43, so the two bracket quantities disagree and the row is the
    least settled of the profile (-1.7 percent over its last 1000 iterations); "undecided" by the letter, not excluded. Row 55 at -2.4e-2 (item 26, DONE 05:48:09Z): L2 0.775 of F2, whole-box N_f 1.16-1.17 of F2, both ABOVE row 54's on my grids, so the lower end of the tested span is bracketed at this budget (verifier G126 06:06:44Z: CONFIRMED by SPEC v4.15; reading (c) by the letter, (a) on resolved h(P); interval of non-excluded tested values [5.5524653, 5.5793640]; L2 smallest at d = -1.6e-2, the residual maxima smallest at d = -8e-3), with the facts attached by G126 and this lane that rows 54 and 55 are the least settled rows, start farther from the equation than the small-offset rows, and that on row 55 the objective and the maxima disagree, so the bracket concerns fits from transplanted starts at one budget, not the minimum of an objective over c_l. At the stored c_l 5.5684 the fixed-c_l fit reaches the whole-box N_f of the candidate (6.8-7.1e-7) with 21,500 iterations on a
    coarser angular basis, against X3's 42,250 iterations after its F0 transplant (different bases and optimisation paths, so no efficiency conclusion), while its
    bands beyond r = 10 are higher than X3's (2.4 x at 10-100, 1.4 x at 100-1000). Among these finite-budget transplanted fits smaller stored exponents correlate
    with lower near-P maxima; these fits do not locate an exponent, and the lane does not claim one.
    THIS LANE'S VERDICT, updated: X3 remains the designated candidate by the pre-registered rule (G74); its sampled residuals are about 7e-7 (N_f next to P), 2e-7
    (N_v inside r <= 1000) and 1.1e-6 (far N_v on the unfitted continuation; the controls show that moving the inverse domain to 1e4 L lowers this band to 0.27 and
    adding rows to 9000 L to 0.03 of X3's, and that the 20750 further iterations do not move it). The tested exponents not excluded by the pre-registered diagnostic
    span at least [5.5683739, 5.5793640] (width 0.0110, 0.20 percent of c_l; verifier-confirmed through row 53) and, on this lane's provisional reading of row 54,
    down to 5.5604082 (width 0.0190, 0.34 percent), with the smallest observed objective at the lower end [HISTORICAL: this was the reading at row 54; after row 55, section (p) (2), the span is [5.5524653, 5.5793640] and the tested minimum 5.5604082 lies inside it, not at an end], so the candidate's own value
    5.5753626 is one tested point of that span and not a measured exponent. These are finite-budget fits with small sampled residuals, independently recomputed on
    X3 (verifier G20 (b) items), not an enclosure of an exact exponent and not evidence of a continuous solution family; the result of 3.16 item 4d (this lane's own
    solver did not pin c_l at the 1e-6 level) is consistent with what the lead's basis shows at the 4e-6 L2 level. The YES evidence for P_2 is therefore evidence
    of approximate profiles with small, independently recomputed residuals at every tested exponent of that span, and it does not pin the self-similar exponent
    beyond the span; it is not a proof. These computations provide no nonexistence proof; the B_3 estimator of the earlier tested fits is near 0.30 (lead / verifier
    G103: 0.2985-0.3044 along the angular row, under the budget row and with rows to 9000 L) while the trial's own y^3 |x|^p3 coefficient is +0.046 (verifier G107
    item 13), so a statement about the regularity of an exact branch would need the trial defect and the limit controlled; it is not made here. The team's endpoint
    is read by the verifier; at 2026-10-19T04:05:14Z it is open on rows 54 / 55 and T_end.
    VERIFIER G120 (04:03:44Z, endpoint statement): "In my judgement the YES endpoint for P_2, stated as numerical evidence and not as a proof, meets the standard
    as written, on the conditions C1 to C8" (residuals, three resolutions and three domains, c_l / x* / h(P), far-field and inverse errors, J decreasing, the
    independent-check paragraph: all MET as written), with the explicit statement that "the residual does not determine the exponent at this level: every tested
    value in [5.5683739, 5.5793640] is not excluded, 5.6004662 is excluded, the L2 objective and the residual maxima at equal budget decrease toward the lowest
    tested exponent, and the lower end is not bracketed"; "fits at a lower c_l on a smaller basis reach residual maxima at or below X3's on one configuration (G119),
    so X3's exponent and basis are not distinguished by the residual"; DONE is OPEN until the conditions (C1-C8: report wording, the stored exponents and readings
    of the rows, (P1) / (P2) not separated, banner and T_end, artifacts md5s, the numerics spread 5.5728-5.5823 as a variant spread, final diff audit) are verified
    in the final text. This lane's reading in (o) above is consistent with G120. (2026-10-19T04:07:02Z)

(p) Shift 8 (2026-10-19T05:12:58Z onward; section 3.18 items 25-28; first written 2026-10-19T07:57:16Z, with steps 49 dom9000g2, 50 c6h9000, 58 fxn16gb, 59 fxn24gb still running or
    queued; items 25-26 referee-audited, astra/shift8audit_a, 14 corrections applied; items 27-28 carry the verifier's G135). (1) FREE CONTROL OF THE 9000 L ROW (dom9000gF,
    item 25; verifier G125): with rows to 9000 L the free c_l moves by -1.5e-6 in 20750 iterations (0.15 percent of its 1.0e-3 gap to the fixed value), the far bands are
    0.025-0.036 of F3's (formula-continued bands; in the fits' own closure convention the N_v beyond 1e4 L is about 2.3e-5 for both) as for the fixed arm, and the fixed / free pair repeats the X3 / F3 pattern (fixed arm 0.93-0.94 next to P and in J, equal far bands, L2 0.976). The
    far-field fall of the 9000 L rows is therefore not a property of the fixed exponent, and a free fit with rows to 9000 L does not select the fixed value either. (2) THE
    LOWER END OF THE FIXED-c_l PROFILE (fxn24g, item 26; G126): at d = -2.4e-2 (5.5524653) the equal-budget L2 is 0.775 of F2 (above row 54's 0.643) and the whole-box
    maximum 1.14-1.16 of F2 (1.59 / 2.39 x row 54's on the verifier's two configurations, 2.20 / 2.31 on my quick scans), so by the lead's SPEC v4.15 definition the
    lower end of the tested span is bracketed at this budget; the row reads (c) by the letter ((a) with resolved h(P)) and is not excluded, so the interval of tested values
    not excluded is [5.5524653, 5.5793640] (width 0.0269, 0.48 percent of c_l), with the L2 minimum of the tested m <= 150, 21500-iteration fixed-exponent profile at
    5.5604082 and the minima of its residual maxima at 5.5683739. Attached facts (G126 and this lane): row 55 has not flattened (-2.50 percent over its last 1000
    iterations; about 7400 more at a constant rate to reach row 54's L2, a conditional extrapolation), rows 54 / 55 start farther from the equation than the small-offset rows (start norms 4.5e-4 / 1.0e-3
    against 1.0e-5 to 1.2e-4), and on row 55 the objective (below F2) and the maxima (above F2) disagree. So the bracket is a statement about equal-budget fits from
    transplanted starts, not about the minimum of an objective over c_l; the budget continuations 58 / 59 (lead 06:18:36Z, SPEC v4.18) test its persistence at twice the
    budget. (3) THE NESTED PAIR AT m <= 200 (items 27-28; G135): the excluded exponent 5.6004662 continued on m <= 200 at X3's budget ends at Q_200 = L2 / L2(F3) = 1.680
    (Q_150 was 2.036) with near-P maxima 2.41-2.50 x F3's: "undecided" by the pre-registered rule (between 1.36 and 3.05) and still excluded at this level; the one step
    of the discriminating experiment separates neither (P1) nor (P2), and the fall of Q is one step, not a trend. The exponent 5.5683739 continued on m <= 200 ends at L2
    0.820 x X3 (against 0.771 for its parent row 53 relative to X2 at m <= 150), near-P N_f 0.59 x X3, J 0.55-0.56 x X3 and whole-box N_f 0.69 x X3 at N16875 q512 (0.70-0.75 on this lane's two grids) but 1.32 x X3 at
    the verifier's N11250 q384, where the maximum is the under-resolved lobe point, so by the rule the ratios are stated without the sentence "smaller maxima than the
    candidate"; (c) by the interval rule. On m <= 200 too, a fit at another fixed exponent reaches a smaller objective, a smaller near-P maximum and a smaller J than X3
    at equal iteration count: X3's exponent and basis are not distinguished by the residual, as (o) said at m <= 150.
    THIS LANE'S VERDICT, updated: X3 remains the designated candidate by the pre-registered rule (G74); its sampled residuals are as in (o) (about 7e-7 next to P, 2e-7 for
    N_v inside r <= 1000, 1.1e-6 on the unfitted far continuation, which the 9000 L rows lower by a factor 30-40 in the formula-continued bands for both the fixed and
    the free exponent). The YES
    evidence for P_2 is evidence of approximate profiles with small, independently recomputed residuals at every tested exponent in [5.5524653, 5.5793640]; the equal-
    budget objective of the tested m <= 150 profile has its minimum inside that span among the tested exponents (at 5.5604082) and the residual maxima theirs at
    5.5683739, neither at the candidate's value, and
    the one refinement step of the discriminating experiment is undecided. These finite-budget computations do not pin the exponent, do not establish the proximity of
    an exact profile, and are not a proof; they provide no nonexistence argument. The team's endpoint is read by the verifier (G120 C1-C8: C2 and C7 met per G128 on
    FINAL_REPORT f62755aa, C1 and C3 met in full per G131 on 822f368d; C4 wording from G135; C5, C6, C8 with the presentation pass); DONE is open at 2026-10-19T10:56:49Z (verifier entries through G146: C6 interim check, hostile-referee pass and
    external reproduction from the artifacts tree in progress on the lead's side). Items (4) and (5) below cover steps 49 / 50 and 58 / 59; the lane's last real edit time
    of this shift is 2026-10-19T10:56:49Z (T0 = 2026-10-17T17:37:14Z; elapsed 41.3 h; the 24-hour minimum was exceeded at 2026-10-18T17:37:14Z; the run cap is 2026-10-19T17:37Z and
    the next shift records T_end).
    APPENDED 2026-10-19T09:46:42Z: (4) THE 9000 L COLUMN (items 29-30; G139 on 49): a second 20750 iterations on the 9000 L rows leave the far band unchanged (1.02-1.03 formula
    continued, C 1.015: "the budget does not lower the 9000 L row's far band further" by the rule) while the near-P maximum falls to 0.58-0.61 and J to 0.54-0.58 of
    dom9000g's and the lobe above P does not move (lobe-to-lobe 1.02 on my scans; the verifier's whole-box ratios 0.98-1.03 with the maximizing point moving to the lobe at
    one configuration); the m <= 250 cap with rows to 9000 L (c6h9000) keeps its interior gain on my scans (whole-box 0.92-1.04 and near-P 0.62 of c6h's) and sits below
    dom9000g2 by 0.71-0.74 next to P, at 0.41 in the 0.1-2 band, 0.38-0.45 in the 10-1000 bands and 3-4 percent at the lobe; the verifier (G140) confirms the interior
    reading by the rule (whole-box 1.02, near-P 0.67-0.71 of c6h's) and finds the cap lowering the 1000 L-9000 L far band to 0.61 of dom9000g2's (outside the rule's
    [0.8, 1.25] band, so stated as a ratio: the difference sits next to the y-axis at the inner end of the band; 9000 L-1e4 L 0.94, beyond 1e4 L 0.98). Both are data rows: they change no number of X3 and attach no decision, and dom9000g2 (near P 0.40 of X3 after 41500 further iterations on other rows) is
    one more fit whose residual maxima are below the candidate's, which the report's C3 must cover.
    Items 27-30 and this paragraph were audited by the external referee (astra/shift8audit_b; 20 findings: solver arithmetic, md5s and rule readings all confirmed;
    corrections of regional-maximum wording, the interval width (0.48 percent, not 0.27), the row-54 ratios, the C1 / C3 attribution and the memtest unit applied 2026-10-19T09:59:40Z).
    APPENDED 2026-10-19T10:49:03Z: (5) THE BRACKET AT TWICE THE BUDGET (items 31-32; lead SPEC v4.18; verifier reading pending): rows 54 and 55 continued for 21500 more iterations
    each (43000 since their transplants) end at L2 2.2009e-6 and 2.2121e-6, ratio 1.005 (1.206 at the single budget), both flattened (-0.15 and -0.34 percent over the
    last 1000); the whole-box maximum of the 5.5524653 row stays 1.9-2.0 times the 5.5604082 row's on my grids (next to P against the lobe), so on my scans both bracket
    quantities remain above and the rule reads "kept at twice the budget", with the objective margin reduced to 0.5 percent and the lower row still falling faster: the
    recorded order at this budget is 58 below 59, its persistence under further continuation is not established (a reversal in a third budget cannot be excluded), while
    the residual maxima keep the single-budget order by a factor two. The original single-budget profile and its readings remain unchanged: its tested minimum remains at
    5.5604082, its span of non-excluded tested exponents remains [5.5524653, 5.5793640] (the two continuations are not a new, uniformly continued exponent profile), the
    objective minimum among tested exponents stays inside the span and away from the candidate's value, and none of it is a determination of an exponent or a proof.
    VERIFIER G147 (11:06:52Z): "kept at twice the budget" CONFIRMED (L2 ratio 1.0051, whole-box N_f ratios 1.152 / 2.062), with the margin history (the L2 gap fell at
    every linearisation from 5.63e-7 to 1.12e-8) and the statement that the L2 order is a fact at 43000 iterations only; the continued 5.5604082 fit is below X3 (whole-box N_f 0.92 and
    near-P N_f 0.75 at 16875 x 512; J 0.80 at 16875 x 384 with eps 0.03, 0.774 with eps 0.01; not equal budget), so the report's C3 must name it too.
    Items 31-32 and this item were audited by the external referee (astra/shift8audit_c; 17 findings: all arithmetic, hashes and the provisional rule reading confirmed;
    corrections of the row-53 comparison, the "shared throughout" / x* / lobe wording, the budget attribution and the order statement applied 2026-10-19T10:56:21Z).
    (6) CLOSING OF THE LANE (shift 9, 2026-10-19T11:12:13Z onward, the last shift before the run cap; written 2026-10-19T11:32:05Z, corrected 2026-10-19T11:47:45Z). No further row was requested by the lead
    after 58 / 59 (gpu_next.txt unchanged since 06:18:36Z; NOTES_FOR_TEAM after 10:49Z addressed to the verifier only: the lead's report rounds C / F / F2 / H / G and their
    presentation pass, done at 11:34:55Z, with their tree reassembled at 11:36Z including this report), so no solver row ran on this lane's GPU after chain 10 ended at 10:46:40Z; the GPU was used only for the test reruns below. Done this shift:
    (i) the README's test commands rerun on a scratch copy of the artifacts tree (runs/smoke9/): test_basic, test_poisson, test_newton, test_ell, test_charac4, test_lsq and
    test_chargrad_cl (both versions) exit 0 (11:16:18Z-11:19:42Z; characteristics residual per point 5e-10 .. 3e-5 in absolute value at dt 0.005 and up to 2.3e-4 at dt 0.02, LSQ node equivalence 4.4e-15, Jacobian vs FD 2.8e-9 .. 9.9e-6,
    characteristic gradient vs FD 5.4e-9 / 4.4e-9); test_rayshape fails with its default arguments because the lead's reference export c6d_seg1_fields.npz was deleted for
    space after the shift-4 validation, and passes against this lane's domain-study export fxd300x (rho vs export 5.0e-15 of max |rho|, d_x rho vs the export's rho_x 2.3e-11
    relative where |rho_x| > 1e-6 and 2.0e-13 absolute against a maximum of 20, parities exact; runs/smoke9/rayshape_fxd300x.log); the scratch copy's tests import the lane's src/ by absolute path, so this verifies the current code and data
    in place, not a relocated tree. (ii) README: status paragraph for shift 9, a relocation note (74 / 33 / 15 / 22 / 9 files of src, tests, scripts refer to the lane's src,
    leadcode, runs and to the lead's work and astra directories by absolute path, the last count including one of the copied lead modules; 125 mention the lane root in some form), a paragraph listing what the tree does not contain,
    the rerun record, the lead's 20 CPU modules that gpu_long_solve.py imports copied verbatim into src/gpu/leadcpu (byte-identical to the lead's artifacts b_fit_domain),
    gzip handling in scan_ratio.py (the packaged scans are gzipped; checked: fxn24gb / fxn16gb whole-box N_f 1.865 at 32768 x 640), src/__pycache__ removed. (iii) An
    external referee audit of the README and of section 4 (astra/shift9final; copy in artifacts/data/astra/shift9final; 16 findings) recomputed the principal numbers of (p)
    from the packaged logs and scans (Q_200 1.6795, nsn8g / X3 0.8203, fxn24g / F2 0.7751, fixed / free at 9000 L 0.9762, 59 / 58 L2 1.00511, whole-box 1.865 / 1.985, interval
    width 0.0269 = 0.48 percent) and the md5 values, all agreeing, and found the following, all corrected at 2026-10-19T11:32:05Z: item 26 said 'roughly 8000' more iterations where
    G126 says about 7400 (constant rate assumed); item 30 repeated the phrase 'flat to 3e-4' that G141 withdrew (two band maxima agree to 3e-4; flatness was not measured);
    (p) (5) grouped J 0.80 with 16875 x 512 where G147 gives J at 16875 x 384 (eps 0.03); (p) (3) '0.771 at m <= 150' now names row 53 relative to X2 as its ratio; (o)'s
    'smallest observed objective at the lower end' is marked historical (the reading at row 54; after row 55 the tested minimum 5.5604082 is inside the span); in the README
    the c6h9000 'verifier pending' (G140 exists), 'nothing ran on the GPU after chain 10' (the test reruns did), the maxima claim for 5.5683739 (true for the whole-box and
    near-P maxima on resolved grids, not for every band: r <= 0.1 1.025, 10-100 1.17), the location of the CPU code in the lead's tree (b_fit_domain, not b_fit_gpu), two
    relocation counts (occurrences had been counted, not files), the test dependencies (CUDA and saved states for three tests) and the row-58 end time (10:45:23Z by the
    chain log). The referee's remaining remarks are the limits of artifacts-only verification, now stated in the README.
    A second audit of this paragraph and of the applied fixes (astra/shift9close, 23 findings, copy in artifacts/data/astra/shift9close) confirmed the fixes and the X3
    metadata read from the shape file, and found, all corrected at 2026-10-19T11:47:45Z: one relocation count (9, not 8, once the copied lead modules are counted), two ratios in item
    32 and (p) (5) to be taken from G148's exact values (N_v 0.924, J 0.774 at eps 0.01), item 32's 'each of the last four linearisations' to be worded as G148 requires
    (the four complete ones before the last), the smoke residual range, missing scope qualifiers in the verdict sentence (y-axis columns, formula-continued bands, the
    m <= 150 profile), the lead's presentation-pass time, the manifest (regenerated after this edit) and the T_end stamp, now the time of this edit.
    THE LANE'S FINAL VERDICT (unchanged from (p) (3) and (5)): X3 = c6g (m <= 200, 375 radial functions, c_l fixed at 5.575362610641546, 20750 LSQR iterations in its own fit, started from the end of the m <= 150 fit s2g,
    3.18 item 5; md5 15f8095f7e79dbfa0c50d75e5fe8997a) is the team's designated candidate by the pre-registered rule (G74); its sampled residuals, recomputed independently by the verifier
    and cross-checked by this lane's scans, are about 7e-7 next to P, 2e-7 for N_v inside r <= 1000 with the y-axis columns excluded (2.5e-7 with them, G120) and 1.1e-6 on the unfitted far
    continuation, which rows to 9000 L lower by a factor 30-40 in the formula-continued bands for the fixed and the free exponent alike (in the fits' own closure
    convention the N_v beyond 1e4 L is about 2.3e-5 for both, 3.18 item 9). The YES evidence for P_2 is numerical evidence of approximate profiles with small, independently recomputed
    residuals at every tested exponent of [5.5524653, 5.5793640]; on the tested profile (m <= 150, 21500 iterations from transplanted starts) the equal-budget objective
    among tested exponents has its minimum at 5.5604082 and the residual maxima theirs at 5.5683739, neither at the candidate's value, the one refinement step of the discriminating experiment is undecided, and the bracket at the lower end holds at
    twice the budget with a margin of 0.5 percent that shrank at every linearisation. These finite-budget computations do not pin the exponent, do not establish the proximity
    of an exact profile, and are not a proof; they provide no nonexistence argument. The team's endpoint (YES, numerical evidence, not a proof, for P_2 in the class of SPEC.md)
    is read by the verifier (G120 C1-C8: C2 and C7 met per G128, C1 and C3 per G131, C4 per G138, C6 interim per G144; C5 with the lead's presentation pass, C8 with the
    verifier's DONE audit, requested by the lead at 11:34:55Z); at 2026-10-19T11:47:45Z DONE is open (latest verifier entry G150) and this lane has nothing pending.
    TIMES. T0 = 2026-10-17T17:37:14Z (this lane's first shift start, shifts/shifts.log; the team T0 is the lead's 2026-10-17T17:37:12Z). T_end (this lane's last edit of this
    report) = 2026-10-19T11:47:45Z; elapsed T_end - T0 = 42.18 h. The 24-hour minimum of the prompt was exceeded at 2026-10-18T17:37:14Z; the run instructions waived it as a gate and
    set a 48-hour cap (2026-10-19T17:37Z), to which this lane worked (nine shifts of up to 6 hours, real times in shifts/shifts.log). Nothing in this section was produced
    after the stated T_end except, if a later line follows, the refreshed T_end stamp itself.

## 2026-10-28T14:21:51Z | Note 63: cross-read of V232 supplemental disks: CORRECT; lead values

I read phase_uniform_density/supplemental_disks/PROOF.md in full. Verdict: CORRECT as stated (conditional on the listed geometry,
which I also checked exactly for the candidate family).
- Geometry. The inner-lobe boundary (2t(1-t^2), 2t^2 sqrt(1-t^2)) is the curve r=sin(2 theta), t=sin(theta), and its squared distance from
  (c_i,0) minus a_i^2 expands to c^2-a^2-4ct+4t^2+4ct^3-4t^4 = P_i(t). With c+a=1 this is 2c(1-2t+2t^3)-(1-2t^2)^2, i.e. the accepted
  condition c>=H(t), so the region and the criterion are the same as for the main disk. c_i+a_i<=1 keeps the disk in the unit disk,
  P_i(0)=c_i^2-a_i^2>0 keeps out the origin, the centre lies in the lobe, and a connected disk avoiding the boundary stays inside.
- Couplings. The density q_r(v), the sign arguments for q_r' and q_r'' (only r<=a_i<c_i/2), the F-invariant minimum, the even-weight
  convexity and monotonicity steps, and the transverse identity giving 2 sqrt(a^2-x^2)/(c^2+2c|x|+a^2) nowhere use c+a=1. The factor
  2^(2n+2)/pi(-binom(alpha,2n)) s^(2n) I_(i,n) agrees with Atilde_n of the parent. Disjoint supports make the subdensities sum to at
  most mu_R, so the costs add and the marginals are kept. Cutoff: q_r>=1/(c_i+r)^2>=1>kappa. 2s max a_i<1 gives |2sx|<1.
- Exact geometry check, independent of geometry.json (scratch/crossread_v232/check.py, check.out): sympy Sturm counts give no real
  root of P_i on [0,3/4] for all five disks (main and four candidates); P_i(0)>0; a_i<c_i/2; c_i+a_i<=1; all ten pair separations
  >=0 exactly (smallest 0.001 between (9/40,3/125) and (29/100,1/25), and 0.00107 between (41/100,3/40) and the main disk).
  Numerical minima of P_i on [0,1/sqrt2]: 1.1e-3, 1.3e-4, 5.7e-5, 3.7e-5.
- Lead values (scratch/v232_eval/eval_v232.py, eval_v232.json; arb at 384 and 768 bits; I_n by the series with remainder and by acb
  quadrature, overlapping; eight terms per disk; V226 bases). The main-disk values reproduce V231 exactly. With the four supplemental
  pairs: 1/20 13.6146560118, 1/10 7.2859008968, 1/5 4.1825570225, 3/10 3.2166471427, 1/2 2.6450780506, 3/4 3.0973694678,
  9/10 5.4688705643, 99/100 42.6816709818; cutoff 1/1000 637.4271353298, 1/200 128.1421838120, 1/100 64.4938357721; uniform K_D
  2.7249328469. The extra saving is about 3.55 percent of the V231 saving (5.61e-6 at alpha=1/2).
If you certify V232 values, I will add them to the report as a further part of Theorem 3.10 with these numbers as the cross-check.

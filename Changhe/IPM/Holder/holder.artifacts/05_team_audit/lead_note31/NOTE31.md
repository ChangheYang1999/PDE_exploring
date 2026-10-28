## Note 31 (2026-10-28T10:33Z): cross-read of five verifier proofs, all without defect

To the verification work. I read each of the following in full, at the stated SHA-256, and re-derived every displayed inequality.
No defect found in any of them; you may treat my cross-read as complete.

1. pole_profile/quadratic_lower/PROOF.md (fa18c499...). Checked: d=(1/2-(1+2u_1)^a/2-lambda P)_+ vanishes for u_1>=0
   and is at most a C_e(-u_1) for u_1<0 (mean value of (1+2u_1)^a/2 on [-epsilon,0]); on K<0 with u_1<0, t=-u_1/r lies in
   (0,1/sqrt2), |cos 2theta|=1-2t^2 and P=r^a[1-(1-2t^2)^a]/2>=a r^a t^2 by s^a<=1+a(s-1); the two arcs give 2dt/sqrt(1-t^2);
   (1-2t^2)/sqrt(1-t^2)<=1; the inner integral up to T=C_e r^(1-a)/lambda is C_e^3 r^(3-2a)/(6 lambda^2) (C_e r T^2/2-lambda r^a T^3/3),
   and the radial integral gives E_c. The K>=0 part is nonnegative, so the lower endpoint needs only (1). E_b and E_s as in
   the parent (E_b: |K|<=|cos2theta|/(2pi r^2), d<=a C_e r|cos theta|, half-circle integral of |cos theta| is 2). Correct.
2. pole_profile/quadratic_clamp/PROOF.md (04a02956...). Checked: on |u_1|>=|u_2|, P>=r^a/2, so (3) kills the clamp there;
   the remaining support has K<0, hence -E_c<=int K d<=0 and the upper endpoint M+E_s. Correct.
3. homogeneous_tail/angular_error/PROOF.md (590fab6e...). Checked the exact decomposition
   nu f-d g_inf=d(f-g_inf)+(nu-d)(f-g_inf)+(nu-d)g_inf, int_0^2pi|cos3theta|=4, and the three radial integrals
   (4B/(pi R), B/(3R^3(1-q)^2), R^(a-3)/(2(3-a)(1-q)^2)). Correct; taking the minimum with the parent error is valid.
4. balanced_residual/PROOF.md (d7a8a12a...). Checked (1) from the Jordan split (balanced mass h=(V-|q|)/2 per disk at
   distance <=2s, unmatched |q| reflected at distance <=1+2s), the monotone form (2), the density w (own pole
   cos(2theta-phi)/(2pi), other pole -r^2 Re(e^(i phi)/(1+re^(i theta))^2)/(2pi), with the left density the negative central
   reflection), and int_0^2pi w dtheta=-r^2 cos phi by the mean value of (1+z)^(-2). Correct, including the optional
   atom paragraph (q-m for a right atom of mass -m).
5. balanced_residual/existing_certificates/PROOF.md (3298a04b...). Checked against paired_local_circles/PROOF.md lines 52-104:
   extraction there is a measure domination uniform in r with fixed sign per cell, so the residual variation per unit dr/r is
   at most v-sum|m|/U and its signed mass is -r^2cos(phi)-sum m/U; P_j<=L_j^+-R_j^- is the right way round. Correct.
   Optional small sharpening, not needed: the pairing can be done radius by radius, giving
   int_(r_k)^(r_(k+1)) [Vhat(r)(2r)^a+|q(r)|((1+2r)^a-(2r)^a)] dr/r with q(r)=-r^2cos(phi)-sum_l m_l/U; then |q(r)| is
   evaluated outward per bin (it is monotone in r^2, so its maximum over the bin is at an endpoint or 0).

Independent float recomputation (mpmath, 30 digits) at your selected radii, per pole:
  a=1/2, eps=.021345980: M=.07973597090, E_c=6.72582e-6, E_s=2.78030e-5, E_b=3.47225e-3; conditions .2464<=.35, .1431<=.5,
    (3) .0747<=.4897. These equal main_per_pole, clamp_error_per_pole, smooth_error_per_pole in a50_prefix376.
  a=3/4, eps=.011070101: M=.01132092786, E_c=3.53021e-5, E_s=1.55508e-6; conditions .0609<=.2, .0322<=.5, (3) .2446<=.4717.
  a=9/10, eps=5.011e-6: M=4.373301e-6, E_c=2.1013e-8; conditions trivially satisfied, (3) .2656<=.4545.
  The projection angular constant A(a) agrees with direct quadrature of int cos2theta P(theta)/(2pi) at all three exponents.
So V139 (2.4443606403, 2.8870680072, 5.2413008171) and V142 have my analytic cross-read; acceptance remains yours after
your coverage and recombination checks.

Status: a30v7 (alpha 3/10) running since 10:25:45Z, 4 of 18 chunks done at 10:31:34Z. a20v7 audit request of Note 30 stands.


## Note 33 (2026-10-28T11:01Z): cross-reads of radial_refinement and rotated_axis_family, both without defect

To the verification work. I read both in full at the stated SHA-256 and re-derived every displayed formula.

1. balanced_residual/radial_refinement/PROOF.md (fe6662e7...). Checked: per radius the residual on the circle of radius r
   has variation <= tau (v_phi bounds sum_l int_(I_l)|w| uniformly in r, and each extracted cell keeps a one-signed rest of
   mass int|w|-|m_l|) and exact signed mass q(r)=-r^2 cos(phi)-S (int_0^2pi w dtheta=-r^2 cos phi); the parent lemma on
   the circle (balanced part at distance <=2r, one-signed |q(r)| reflected at distance |2z|<=1+2r) gives
   tau(2r)^a+|q(r)|g_a(r); applying it to each angular integral before the dr/r integration needs no measurable coupling.
   int_s^t tau(2r)^a dr/r=tau 2^a(t^a-s^a)/a; g_a'<0 so g_a<=g_a(s); |q| convex in r^2;
   int_s^t (r^2-s^2)/(t^2-s^2) dr/r=1/2-s^2L/(t^2-s^2)=H and the complementary weight integrates to L-H; 0<H<L. The
   minimum with tau L and with the V152 aggregate row bound is valid (all bound the same residual functional). Correct.
   On acceptance (V158) I will put C_1/2<=2.1956570947, C_3/4<=2.6421664049, C_9/10<=5.0112069529 into the next version;
   only the sixth decimal of Table 1 at 1/2 changes, so this is low priority for you.
2. 11_lattice_pole_constraints/rotated_axis_family/PROOF.md (857eade5...). Checked: admissibility (signed distance,
   rotation, lambda K<=1, clamp by h with [h]<=k<=1, gluing k(s^a+t^a)<=(s+t)^a, central oddness, f=0 on X=0, f(x)=-1/2
   since h(x)=1/2 and F(x)<=-1/2 for every c); K_phi=cos(2theta-phi)/(2pi r^2) is T_phi, T_phi -+ I/2 both have norm D
   (rotation by phi/2, and T_xx+I/2=-(T_pi-I/2)), increments I_phi +- 1/2, so D>=|I_phi|+1/2; nu_phi centrally odd;
   nu_phi(w)=Re[e^(i phi)w/(pi(w^2-1/4)^2)] (from K_phi=Re(e^(i phi)/u^2)/(2pi) and (w+1/2)^2-(w-1/2)^2=2w), exterior bound
   2k R^(a-1)/((1-a)(1-1/(4R^2))^2) with |f|<=k r^a. Pole disks: x in Z (B(1/2)=0), |Q_delta x-x|=|sin(delta/2)|, (1) makes the
   projection branch active below h; d=(1/2-(1+2u_1)^a/2-lambda P_phi)_+ vanishes for u_1>=0, d<=a C_e(-u_1); the substitution
   u=Q_(phi/2)v turns K_phi(u)P_phi(u) into K_0(v)P_0(v), giving lambda A eps^a/a with A=(1/4pi)int|cos2theta|^(1+a)
   =Gamma(1+a/2)/(2 sqrt(pi) Gamma(3/2+a/2)); K_phi harmonic off 0 with K_phi(e_1)=cos(phi)/(2pi) gives cos(phi)eps^2/4 (sign:
   -(-1/2) times the mean); E_b and E_s as in pole_profile. Correct. Optional: the one-sided E_c of quadratic_lower carries
   over after the same substitution (P_phi(Q_(phi/2)v)=P_0(v), but the clamp d depends on u_1, which is not rotated, so the
   E_c argument would need the rotated half-plane; keep the symmetric E as written unless phi=0).


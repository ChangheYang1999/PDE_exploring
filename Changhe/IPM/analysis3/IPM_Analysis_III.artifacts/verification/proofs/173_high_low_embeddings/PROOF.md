# The full high space embeds in every required low transport domain

## Statement and spaces

Write r=|X|, t=log r, p(theta)=cos(theta)^2 sin(theta) and E beta=r^3 p beta(t). All densities are even in x and odd in y. Fix the smooth cutoffs, the exact normalized modal background and the order function of proof 123. In particular the order s on the cylinder has all derivatives bounded, is invariant under both reflections, satisfies 41/20<=s<=25/4 and equals25/4 on a fixed sector about each vertical axis. Let chi be an angular cutoff supported in that sector and equal to one in a smaller sector. Put

 sigma=25/4, delta=9/5, gamma=-1/2,
 b(t)=exp((3+delta)t) far left, b(t)=exp(gamma t) far right,
 a_H(t)=exp(-3t)b(t).

The interpolation defining b is fixed, positive and smooth with bounded logarithmic derivatives. Define

 X_s={h: v=h/b in H^{s(.)}, u=chi h/(b p) in H^sigma,
                    u(t,pi/2)=u(t,3pi/2)=0},
 Gamma_H=a_H H^sigma(R),
 B_H={J chi_0+a_H z: J real, z in H^{sigma+1}(R)},
 H_full=E B_H direct-sum X_s,
 Y_full=E Gamma_H direct-sum X_s.                         (1)

The norms are the natural Hilbert product norms, with the two indicated terms in the X_s norm. The scalar cutoff chi_0 is one far left and zero far right. The direct sums use the exact vertical cofactor; the zero traces in X_s make their coordinates unique.

There are two allowed low settings:

 (O): a_w=17/4, beta=17/2, eta=5/4;
 (N): any fixed a_w in[18/5,4], beta=17/2, eta=37/20.

In either case let

 w=|cos(theta)|^{-2a_w} r^{-beta} for r<1,
 w=|cos(theta)|^{-2a_w} r^{-eta} for r>=1,
 R_w=L2_P(w dX),
 G_w=L2(g_w(t)dt),
 g_w(t)=exp((8-beta)t) for t<0,
 g_w(t)=exp((8-eta)t) for t>=0,
 B_w={J chi_0+w_0: w_0,w_0' in G_w},
 X_w=E B_w direct-sum R_w, Y_w=E G_w direct-sum R_w.       (2)

The B_w norm in (2) is equivalent to the original integrating-factor norm, by topics166 and168. This equivalence retains the closed coordinate J.

Let V_h be one of the total transport fields on the sufficiently small H_full ball of proof 167 in (O), or proof 171 in (N), including its exact moving-tail variation. Put T_h=V_h.grad-1 and

 D_w(h)={f in R_w:T_h f in R_w distributionally}.        (3)

Then Y_full embeds continuously into Y_w and H_full embeds continuously into E B_w direct-sum D_w(h). The latter maps have norm bounds uniform on the stated small ball. In particular these embeddings apply to all of H_full, not just the high graph domain of a particular inverse.

Moreover H_full embeds continuously into the infimum Hilbert sum H_high^sigma=H_base^sigma+Q of proof 71, with delta=9/5, gamma=-1/2 and bulk order41/20. Consequently the low/high product and velocity derivative estimates of proof 71 apply on H_full in (O). The corresponding estimates in (N) are proved in proof 172.

## Weighted embeddings

For f=a_H z the scalar target integrand is g_w a_H^2 |z|^2. Its end factors are

 exp((2delta+8-beta)t)=exp(31t/10) at minus infinity,
 exp((2gamma+2-eta)t) at plus infinity.                 (4)

The latter exponent is-1/4 in (O) and-17/20 in (N). Both factors are bounded on their respective ends, and the transition interval is compact. Thus Gamma_H embeds into G_w. The same argument for a_H z and (a_H z)'=a_H(z'+(a_H'/a_H)z), using the bounded logarithmic derivative, proves B_H into B_w, including the free J coordinate.

The physical R_w measure of h=bv is

 |v|^2 b^2 r^2 r^{-beta or -eta}|cos(theta)|^{-2a_w}dt dtheta. (5)

The radial factors in (5) are exactly (4). On an angular set separated from the vertical axis they are bounded and the angular factor is bounded. The H^{s(.)} norm controls H^{41/20}, and hence L2 there.

In a smaller vertical sector h=bp u. Reflection in x makes u even in the normal angular variable phi. Its zero trace implies partial_phi u=0 there as well. Taylor's formula gives

 u(t,phi)=phi^2 integral_0^1(1-v) partial_phi^2 u(t,v phi)dv.

Since |phi| and |cos(theta)| are comparable in this fixed sector,

 sup_sector |u(t,theta)/cos(theta)^2|
                   <= C ||u(t,.)||_{H^3(S1)}.          (6)

One-dimensional H^3 controls the second derivative in supremum norm. The angular integrand after (6) is bounded by a constant times

 |cos(theta)|^{8-2a_w} sin(theta)^2 ||u(t,.)||_{H^3}^2. (7)

It is integrable because a_w<9/2. Its full angular integral is 2 Beta((9-2a_w)/2,3/2). The squared L2_t H^3_theta norm is bounded by H^sigma. Equations(4)-(7), with an angular partition, prove X_s into R_w. They also prove Y_full into Y_w.

## Membership in every low maximal domain

First take f in X_s. Work on two nested angular sectors where chi=1. On the smaller one, write f=bp u. Conjugating T_h by bp gives

 (bp)^{-1} T_h(bp u)
     =W_{h,t} partial_t u+W_{h,theta} partial_theta u
       +[(b'/b)W_{h,t}+(p'/p)W_{h,theta}-1]u.           (8)

The background coefficients and their divided angular components have the finite regularity proved in topics126 and163. The perturbation coefficients and their divided vertical component satisfy the sector H^sigma bounds of topics155,164 and167. Consequently (8) is in H^{sigma-1}=H^{21/4}; multiplication here is legitimate since these Sobolev orders are above the two-dimensional algebra threshold. The explicit smooth strain is treated separately from the square-integrable coefficient remainder. Its size and derivatives are uniformly bounded on the perturbation ball.

The output in (8) is even in phi. It has zero vertical trace: u and partial_t u vanish there, while W_{h,theta}=0 there by tangency. The apparently singular factor (p'/p)W_{h,theta} is a regular bounded sector coefficient, as proved by the divided-component estimate. Thus (6)-(7) apply to (8), since21/4>3, and place T_h f in R_w on the smaller sector.

Outside that sector the angular singularity is absent. There T_h(bv)/b is a bounded coefficient times v plus bounded coefficients times its first derivatives. The H^{41/20} norm controls these in L2. Angular cutoffs contribute only zero-order terms supported away from the vertical axis. Their coefficients are bounded. This proves T_h f in R_w globally, with a uniform bound by ||f||X_s. The distributional product rule is justified by the same Sobolev regularity and approximation. No boundary or axis delta distribution appears.

For the scalar component beta in B_H, its inclusion in B_w was proved above. The scalar transport row A_h beta belongs to G_w and the lift remainder Err_h beta belongs to R_w by the exact scalar and lift estimates of topics164,166 and171. In particular their treatment of J chi_0 uses the normalized central strain cancellation and the inner exponent31/10, rather than pretending that chi_0 belongs to G_w. Hence the full high element lies in the full low graph domain. The bounded nonlocal coupling and rank-one terms can then be added without changing this domain.

## Inclusion in the product space

Choose a reflection-invariant angular cutoff chi' equal to one near the vertical axis and supported where chi=1. For a remainder f=bv in X_s,

 f=r^3 p [a_H chi' u]+b(1-chi')v.                       (9)

The first coefficient chi' u belongs to H^sigma and is even under both coordinate reflections. The second normalized coefficient belongs to H^{41/20}, has the required density parity and is supported a positive angular distance from x=0. Thus the first term is in H_base^sigma and the second is in Q. The radial weight defining Q is exactly b; Q need not be compactly supported in t.

For the scalar component,

 E(J chi_0+a_H z)
   =r^3 p [J chi_base+a_H(z+J(chi_0-chi_base)/a_H)].     (10)

Here chi_base is the radial cutoff used in proof 71. Its difference from chi_0 is compactly supported in t, so the correction in parentheses is in H^sigma. Also H^{sigma+1}(R) embeds into H^sigma(R times S1) when extended constantly in theta. Equations(9)-(10) give a bounded decomposition in H_base^sigma+Q. The parameter inequalities required there are delta>1/4, delta<2, gamma<-3/8, sigma>6 and41/20>2. They are all strict.

## Scope and audit of the theory author statement

This proves Lemma Emb in the theory author's work/Exist_cond.md, with the nested angular cutoffs and the scalar lift step written explicitly. The proof also covers the new low family, without comparing the two low inverse constants. It asserts no actual inverse or smallness bound. The exact audited theory author revision and dependency hashes are recorded in evidence/check.json and evidence/lead_Exist_cond.md.

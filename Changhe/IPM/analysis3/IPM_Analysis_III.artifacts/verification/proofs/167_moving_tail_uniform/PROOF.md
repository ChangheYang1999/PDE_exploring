# Uniform inverse theory for the exact moving-tail family

## Exact family and statement

Use the exact normalized modal density rho_0, exponent k and scale ell_0=1/k, and the low and high spaces of topics123,165 and166. Write p(X)=x^2 y. Fix the same smooth radial cutoffs chi_0 and chi_infinity as in proof 59: chi_0 is one near0 and has compact support; 0<=chi_infinity<=1, it is zero on r<=1 and one for sufficiently large r. Let Theta be the exact leading angular factor of rho_0. For ell in a compact interval I about ell_0 set

 q=1/ell,
 rho_ell=rho_0+z_ell,
 z_ell=chi_infinity(r)(r^q-r^k)Theta(theta),
 F_ell(rho)=(ell X+U[rho]).grad rho-rho,
 n(ell)=3ell-1-c[rho_ell],
 H_0=chi_0 X.grad rho_0/3,
 B(ell)=F_ell(rho_ell)-n(ell)H_0.                         (1)

Choose I sufficiently small that there is a fixed q_* with

 max(k,sup_(ell in I)1/ell)<q_*<1/4.                     (2)

The symbol B(ell) in (1) is a residual family, not the scalar domain B. The exact scalar result of proof 59 gives n(ell_0)=0 and n'(ell)>=3. Define

 m(ell)=(B(ell)-B(ell_0))/n(ell),
 M(ell)=H_0+m(ell),                                    (3)

using the removable value at ell_0. For h in a sufficiently small ball of H_full=B_H direct-sum X_s, define ell(h) by n(ell(h))=c[h]. Let

 A_h f=(ell(h)X+U[rho_ell(h)]+U[h]).grad f-f
                      +U[f].grad rho_ell(h)+c[f]M(ell(h)). (4)

The domain of (4) is the full scalar/remainder graph domain of its total transport field. There are compatible low and high realizations

 A_h:B direct-sum D_L(h)->Y,
 A_h:B_H direct-sum D_H(h)->Y_H,
 Y=G direct-sum R, Y_H=Gamma_H direct-sum X_s.            (5)

For a sufficiently small high ball, both realizations are Fredholm of index zero and satisfy uniform estimates modulo fixed compact maps. If the base low operator A_0 is injective, then both are isomorphisms with uniform low and high graph inverse bounds on a smaller ball. Their inverses agree on Y_H. The base injectivity, a numerical radius and all quantitative closure constants remain unproved by this theorem.

The exact identity of proof 59,

 F_ell(h)(rho_ell(h)+h)=F_ell0(rho_0)+A_h h,               (6)

therefore has the qualitative uniform inverse theory required by its conditional iteration, subject to base low injectivity. Equation(6) and the inverse conclusions do not themselves meet that iteration's numerical smallness conditions.

## Smooth coefficient family for the tail velocity

Every fixed ell derivative of z_ell vanishes on r<=1. Outside a fixed disk it is a finite sum of r^q(log r)^j Theta and the fixed r^k Theta term. All angular factors have finite bandwidth. The canonical modal Green formulas, or the reflected kernel estimates with these powers, show

 U[z_ell]=c[z_ell](-x,y)+O(r^3) at0,
 U[z_ell]=O(r^(q_*)) at infinity,                        (7)

including every fixed number of cylinder derivatives, uniformly for ell in I after any fixed number of ell derivatives. In (7), a constant may depend on the derivative order. To justify the parameter derivatives, the far kernel moments are bounded by integrals of r^(q_*-2), and hence converge since q_*<1. The finite modal denominators stay separated from zero on I: for the density harmonics they are q+n+2 and q-n+2 with n odd and 0<q<1. The compact transition changes only smooth interior fields and decaying exterior multipoles. Thus all differentiations in ell under the canonical Green construction are justified. The mean-value formula gives a factor |ell-ell_0| since z_ell0=0.

In cylinder components let B[z]=(U[z].e_r/r,U[z].e_theta/r), and remove c[z]chi_0(-cos(2theta),sin(2theta)). The remaining Z[z] is O(r^2) at0 and O(r^(q_*-1)) at infinity, with all fixed cylinder derivatives. Consequently Z[z] belongs to every fixed cylinder H^m, including the vertical divided component Z_theta/cos(theta). These divisions preserve radial regularity because the angular bandwidth is finite and the relevant component is odd at the axis. The inner quotient chi_- Z[z]/a has order O(r^(2-delta)), where delta=9/5<2, and has the same Sobolev properties. The axis trace, after its c[z]chi_0 part is removed, has these estimates as well, in every fixed order.

It follows that the velocity and axis estimates of topics155 and164 hold for z_ell, with right side C|ell-ell_0|, even though the growing density z_ell itself is not in G_s. This conclusion is obtained directly from (7), not by putting z_ell in an inapplicable density space. In particular all C^(1,alpha), bulk H^{s(.)}, vertical H^sigma and weighted inner coefficient bounds used in topics158-166 hold uniformly for the sum of the h and z_ell(h) increments.

The scalar relation gives exactly

 3(ell(h)-ell_0)=c[h]+c[z_ell(h)],
 |ell(h)-ell_0|<=||c||_(X_0*)||h||X_0/3.                 (8)

Hence the total transport field in (4) is

 V+W[h]+W[z_ell(h)], W[f]=U[f]+c[f]X/3,                  (9)

and its coefficient perturbation is at most C||h||H_full. The normalized central linear part still annihilates x^2 y. Equations(7)-(9) are exactly the coefficient and cancellation hypotheses used in the perturbed transport, scalar, lift, energy and maximal-domain proofs of topics158-166. Those proofs therefore apply to this total transport. They never require that a coefficient perturbation have a unique density preimage in G_s. This establishes their fixed-coupling conclusions for (9), with uniform constants on a sufficiently small h ball.

## Coupling change on both low and high spaces

For any z=z_ell define

 C_z f=[U[f]+chi_0 c[f]X/3].grad z.                       (10)

The following smooth operator-valued families vanish at ell_0:

 C_z:X_0->Y,
 C_z:H_full->Y_H.                                      (11)

Their norms and their first ell-derivative norms are bounded uniformly on I; in particular ||C_z||<=C|ell-ell_0| in both displays.

Here are the estimates that permit reuse of the coupling proofs. On r<=1, grad z=0, so there is no origin cancellation obligation in (10). On each rescaled annulus, the coefficients of grad z have finite angular bandwidth and arbitrary Sobolev regularity, with magnitude at most C|ell-ell_0|r^(q_*-1) on the far end. These bounds, also for each ell derivative, meet the coefficient hypotheses in topics46-49 and123, with q_* in place of k and with zero inner density coefficients. The same-scale high estimate uses the order-zero localized U and the exact identity for U_1[x^2 w]/x. Its norm carries the displayed r^(q_*-1) factor. The separated-scale matrices (8) of proof 123 have the same exponents with k replaced by q_* on the far end, and all inner-output entries are zero except for the fixed compact cutoff transition. Their row and column sums remain finite because q_*<1 and q_*-4-gamma<0. These facts prove the bulk and vertical cofactor estimates before the exact axis subtraction.

For the high scalar row, the estimate of proof 113 on each unit cylinder interval becomes O(exp((q_*-35/8)t)) at infinity. After division by a its exponent is q_*-7/8<0. It is zero near0. Its local gain gives H^(51/8), and thus bounds into H^(25/4); local compactness and these decaying tails also give compactness if needed. Jet inputs obey the exact two-mode moment formulas (5)-(9) of proof 115. Multiplication by the finite-band coefficient of z gives the same high estimate, with inner contribution zero and outer multiplier O(r^(q_*-1)). Axis evaluation for those finite-band jet outputs preserves radial Sobolev order. This proves the second line of (11) on both components of H_full.

For low inputs, the local axis-subtraction estimate and the separated Hilbert-Schmidt bounds of topics46-48 apply with the same zero inner output and far exponent q_*<1. For example the remainder-to-axis bound has exponent q_*-35/8 before the G weight, which is integrable since q_*<1. The jet-input bound uses the same scalar Hardy space B and its fixed endpoint estimates. The arguments are linear in grad z and uniform for its ell derivatives. This proves the first line of (11) and the operator-norm smoothness asserted there. No derivative of an arbitrary low input is taken in this coupling estimate.

## Residual family in the exact high target

The family B(ell) of (1) is smooth into Y_H, and therefore into Y. This strengthens the low membership used in proof 59. We verify the three possible obstructions explicitly.

At0, rho_ell=rho_0=p+O(r^5). The change in the linear coefficient of F_ell(rho_ell) is [3(ell-ell_0)-c[z_ell]]p=n(ell)p. Since H_0=p+O(r^5), subtraction in (1) removes it. Thus B(ell)/p=O(r^2) at0, with every fixed cylinder derivative, uniformly after ell differentiation. Division by a leaves the integrable order r^(2-delta).

At infinity write rho_ell=r^q Theta+R_0, where R_0=rho_0-r^k Theta=O(r^(2k-1)). The leading linear term cancels exactly because ell q=1. The term (ell r partial_r-1)R_0 is O(r^(2k-1)), while U[rho_ell].grad rho_ell is O(r^(2q_*-1)). Ell derivatives introduce finitely many powers of log r, absorbed by choosing the strict q_* gap in (2). After division by the physical weight b~r^gamma, gamma=-1/2, the worst exponent is 2q_*-1-gamma=2q_*-1/2<0. These are cofactor estimates as well: finite angular factorization, as in proof 83 equation(1), takes place before dividing by p. Thus B(ell)/(p a) and all fixed cylinder derivatives decay at both ends.

On the finite knot interval the density rho_ell is C6 and piecewise smooth. The new tail is smooth there; the original finite joins are unchanged. The velocity has the same sufficient regularity. The residual uses one density derivative, so its cofactor is C5 and piecewise smooth across finitely many knots. The fractional jump argument of proof 75 gives H^sigma for every sigma<13/2, uniformly under every fixed ell derivative. The fixed value sigma=25/4 is strictly below this ceiling. There are finitely many angular modes independent of ell. Axis evaluation and subtraction therefore preserve the radial H^sigma norm, instead of losing a generic half derivative. It follows that the scalar part is in Gamma_H and the axis-subtracted remainder is in X_s. This proves smoothness of B:I->Y_H.

The quotient (3) is made explicit by

 m(ell)= [integral_0^1 B'(ell_0+t(ell-ell_0))dt]
             /[integral_0^1 n'(ell_0+t(ell-ell_0))dt].    (12)

The denominator is at least3, so (12) proves that m is smooth into Y_H, with bounded derivatives on I. Define

 zeta_ell=M(ell)-chi_0 X.grad rho_ell/3
          =m(ell)-chi_0 X.grad z_ell/3.                  (13)

The last subtracted function is smooth, compactly supported away from0, and finite-band, so belongs to Y_H. Consequently zeta_ell is smooth into Y_H and into Y, with ||zeta_ell-zeta_ell0||<=C|ell-ell_0|.

At the base point zeta_ell0=m(ell_0) is exactly the bordered vector in proof 83 with the same cutoffs. Indeed, with KP=chi_infinity r^k log(r)Theta,

 rho_dot=-k^2 KP,
 n'(ell_0)=3+k^2 c[KP],
 m(ell_0)=(X.grad rho_0-k^2 L_fix KP)/(3+k^2 c[KP])-H_0.

Multiplying numerator and denominator by ell_0 and expanding the definitions of gfar and yKP in proof 83 gives its zeta=(ell_0 gfar-k yKP)/(3ell_0+k c[KP]). Thus the base operator in this theorem is the already identified exact Schur complement.

## Full operators, compact estimates and inverses

Equations(9), (10) and(13) rewrite (4) without any separately nonintegrable cubic term:

 A_h=T_total(h)+C_ren,0+c[.]zeta_ell0+D_h,
 D_h=C_zell(h)+c[.](zeta_ell(h)-zeta_ell0).               (14)

By (8), (11) and(13),

 ||D_h||_(X_0->Y)+||D_h||_(H_full->Y_H)<=C||h||H_full.   (15)

The first three terms on the right side of (14) have the uniform fixed-compact estimates of topics165 and166, now with total transport (9). Shrink the h ball so the error from (15) is absorbed in the left side of each estimate. The compact maps remain fixed. For each h, the path obtained by replacing D_h with tD_h, 0<=t<=1, has the same maximal transport domain and remains upper semi-Fredholm by these absorbed estimates and their graph versions. At t=0 it has index zero by topics165 and166. The index argument of proof 44 therefore proves Fredholm index zero at t=1, in both realizations. This proves the unconditional assertions of (5).

Assume now that the base low A_0 is injective. The high base is injective because its domain embeds in the low one and the operators agree there. Topics165 and166, with the coefficient extension justified in (7)-(9), give uniform low and high inverses Q_h for the first three terms in (14), on a sufficiently small ball. Decrease its radius once more so that ||D_h Q_h||<1/2 in each target norm. The Neumann formula

 A_h^(-1)=Q_h(I+D_h Q_h)^(-1)                            (16)

then proves both uniform inverse bounds, including graph norms recovered from the equation. All maps in (16) use the same domain for that fixed h. No comparison of different unbounded-operator domains is involved. Since the high domain is contained in the low domain, low uniqueness identifies the two inverses on Y_H.

## Scope of the nonlinear consequence

The exact scalar normalization, the logarithmic tail variations, and the varying maximal transport domains have all been included. Together with the low/high difference estimate of proof 59 and the compatible mapping result of proof 71, this proves that base low injectivity is the remaining qualitative inverse hypothesis in the conditional two-norm iteration. Its high forcing norm, the numerical inverse constants, the bilinear constant and the smallness inequalities still need certification. The low residual norm certified in proof 154 is not a high forcing norm and cannot be substituted for it.

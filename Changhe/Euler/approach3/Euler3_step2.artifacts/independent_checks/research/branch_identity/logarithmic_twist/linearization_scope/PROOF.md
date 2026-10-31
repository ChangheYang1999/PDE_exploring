# Scope of homogeneous rotating transport and selected shell angles

Status: exact identities and counterexamples. No campaign field is evaluated here. These results qualify the interpretation of the numerical twist comparisons.

## Statement and notation

Fix c in (0,1), omega in R, alpha=(1-c)/c, and k=omega/c. Write J(x,y,z)=(-y,x,0), and let Q_gamma be rotation about the positive z axis. For a C1 vector field U define

L[U]=(1-c)U+c(y dot grad)U-omega((Jy dot grad)U-JU).

The momentum residual also contains (U dot grad)U+grad P. The following three statements hold.

1. On any domain where U and DU are bounded and P is C1 with bounded gradient,

   ||(U dot grad)U+grad P||_infinity
   <= ||U||_infinity ||DU||_infinity + ||grad P||_infinity,

   where vectors have their Euclidean norm and matrices their induced operator norm. A bound on ||U||_infinity alone does not imply that this discarded term tends to zero, even for smooth divergence-free U and a smooth pressure satisfying the Poisson equation -Delta P=tr((DU)^2).

2. On r=|y|>0 away from the z axis, the homogeneous solutions L[U]=0 have cylindrical components

   u(r,theta,phi)=r^(-alpha) F(theta,phi+k log r).

   In fixed Cartesian coordinates the equivalent formula is

   U(r,theta,phi)=r^(-alpha) Q_(-k log r) G(theta,phi+k log r),

   with G(theta,xi)=Q_xi F(theta,xi). Both F and G are C1 periodic component functions on the angular domain. Omitting the rotation factor in the Cartesian formula is generally incorrect.

3. For the homogeneous twisted fields and shell norm defined in ../PROOF.md, the exact conclusion is translation of the set of minimizing angles. Arbitrarily selected minimizers need not have the predicted consecutive increment. Uniqueness modulo a common period, or a fixed selection from the translated maximizing set, suffices for that increment after consistent unwrapping.

## Proof of the first statement

At each point, (U dot grad)U=DU U. The operator-norm inequality and triangle inequality give the displayed bound. Taking suprema proves it.

For 0<epsilon<=1 define on R3, in Cartesian coordinates (x,y,z),

U_epsilon(x,y,z)=(epsilon sin(y/epsilon^2), epsilon, 0),
P_epsilon(x,y,z)=0.

These fields are C-infinity. Their divergence is zero because the first component is independent of x, the second is constant and the third vanishes. Their only nonzero derivative entry is

(DU_epsilon)_(1,2)=epsilon^(-1) cos(y/epsilon^2).

Thus (DU_epsilon)^2 is the zero matrix, and P_epsilon satisfies -Delta P_epsilon=tr((DU_epsilon)^2)=0. Also ||U_epsilon||_infinity<=sqrt(2) epsilon, whereas

(U_epsilon dot grad)U_epsilon=(cos(y/epsilon^2),0,0)

has supremum norm one. At the origin it equals (1,0,0). At that same point,

L[U_epsilon](0)=epsilon(-omega,1-c,0).

Consequently the ratio of the discarded convection norm to the homogeneous-operator norm at the origin is

1 / (epsilon sqrt(omega^2+(1-c)^2)),

which tends to infinity as epsilon tends to zero. The denominator is positive because c<1. This disproves both absolute and relative neglect based on velocity smallness alone. The example is not a finite-energy or decaying velocity, not a campaign ansatz, and not an Euler solution; none of those properties is needed to refute the claimed implication for smooth fields. Additional tail or derivative hypotheses may justify an approximation, but must be supplied separately. A relative error estimate would also require a suitable nonzero comparison scale.

## Proof of the second statement

The cylindrical frame at angle phi is Q_phi applied to the fixed coordinate frame. Radial differentiation leaves this frame fixed. Differentiation in phi differentiates each horizontal frame vector by J. Therefore (Jy dot grad)U-JU has cylindrical components partial_phi u. The equation L[U]=0 is exactly

(1-c)u+c r partial_r u-omega partial_phi u=0.

With s=log r and v(s,theta,phi)=exp(alpha s)u(exp(s),theta,phi), this becomes partial_s v-k partial_phi v=0. The quantity v(s,theta,xi-k s) is constant in s, so v=F(theta,phi+k s). This proves the cylindrical formula and its converse by substitution.

Set xi=phi+k log r. Since U=Q_phi u and G(theta,xi)=Q_xi F(theta,xi),

Q_phi F(theta,xi)=Q_phi Q_(-xi)G(theta,xi)=Q_(-k log r)G(theta,xi).

This proves the Cartesian formula. For a direct counterexample to its unrotated version, assume omega is nonzero and take a constant horizontal vector v. The field r^(-alpha)v has

L[r^(-alpha)v]=omega r^(-alpha)Jv,

which is nonzero. In contrast, r^(-alpha)Q_(-k log r)v solves L[U]=0: its radial derivative contributes -c k JU, which cancels +omega JU. It cannot be expressed in the unrotated Cartesian form with an angular function independent of r: its independence of phi would force that angular function to be independent of its azimuthal argument, yet the displayed solution rotates with r.

## Proof of the third statement

The change of variables r=a t and an angular shift, detailed in ../PROOF.md, give

argmin_gamma d_a(gamma)=(k_a-k_b)log a+argmax_delta C(delta).

All equalities are on the angular circle. A fixed maximizing argument delta_* gives gamma(a)=(k_a-k_b)log a+delta_*, and replacing a by2a gives the stated increment. A unique maximizing class forces this choice modulo the period. Without such a selection condition, different maximizing classes can be chosen on different shells.

For an explicit example, take equal alpha and k for both fields and F_a=F_b=(0,0,1) as cylindrical components. Both physical fields equal r^(-alpha)e_z, so every axial rotation fixes them. On every finite shell a<r<2a their positive finite norms agree, their distance is zero for every angle, and the minimizing set is the whole angular circle. Choose angles0 and pi/2 alternately on consecutive shells. Their increments are nonzero modulo2pi, although the parameter-derived increment is zero. The translated-set identity remains true. It is the assertion about an arbitrary chosen minimizer that fails.

## Dependencies and scope

The proof uses elementary differentiation, induced matrix norms, characteristics and the shell correlation identity in ../PROOF.md. It introduces no new numerical tolerance. The independent high-pair angle values remain valid numerical observations. For regularized or corrected fields, the conditional asymptotic extension in ../PROOF.md still requires uniform convergence of the centered correlations, uniqueness of the limiting maximum and consistent unwrapping. No such continuum hypotheses are certified by a finite list of shell angles.

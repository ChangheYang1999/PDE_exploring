# Identities for a given vortical SRB measure and far-field sets

This audit treats C23 in the team records. It proves the precise identities below. Existence of the invariant probability and the two additional unstable-conditional hypotheses are assumptions, not consequences proved here.

## 1. First-order identities on any compact invariant probability

Let 0<c<1/2, omega be any finite real number, U,P be C1 on R3 and solve the profile equation. Put A=cI-omega J, B=Ay+U, X=cy+U, a=1-2c and r^2=y_1^2+y_2^2. Let mu be a compactly supported probability invariant under the full local flow Phi of B. Then

    int |X|^2 dmu = omega int Jy.U dmu,
    int Jy.grad P dmu = -a int Jy.U dmu,
    int (|B|^2+|X|^2) dmu = omega^2 int r^2 dmu,
    omega int Jy.B dmu = -int |B|^2 dmu.

For positive-entropy mu, both squared norms in these formulas have strictly positive integrals. In particular omega!=0, omega int Jy.grad P dmu<0 and the mean angular momentum of B has sign opposite to omega.

Write H=P+|U|^2/2+(Ay).U. The Lamb identity is B cross Omega=aU+grad H. Hence B.grad H=-a U.B and

    X.B=B.grad(c|y|^2/2-H/a).

The integral of B.grad f is zero for C1 f, by differentiating the full-flow invariance relation on the compact support. Thus int X.B=0, and X.B=|X|^2-omega Jy.U gives the first formula. Dotting the profile equation with Jy and differentiating Jy.U gives

    a Jy.U+B.grad(Jy.U)+Jy.grad P=0.

This proves the second. The last two are obtained by expanding B=X-omega Jy and using the first identity.

If int|X|^2=0, continuity gives X=0 on the entire invariant support. The carrier there is the rigid rotation -omega Jy, whose compact restriction has zero entropy. If int|B|^2=0, the flow is the identity on its support and also has zero entropy. This proves strict positivity. The identities also give the L2 sphere equation

    int |X-(omega/2)Jy|^2 dmu=(omega^2/4) int r^2 dmu.

No statement here treats c=1/2, where division by a is invalid. No sharpness assertion for positive-entropy measures follows from nondecaying affine examples with only zero-entropy compact invariant measures.

## 2. An integrable normalized unstable current

Now U is C2. Assume that nu is a compactly supported, full-flow ergodic probability for Psi_t=Phi_-t, with positive entropy, nu(Omega!=0)=1, Lyapunov exponents (a,0,-kappa), kappa=1+c, and stable line R Omega almost everywhere. Let alpha=(B cross Omega).dy. Assume additionally:

1. A measurable partition xi of a full-measure set has atoms parametrized by C1 embedded unstable arcs gamma_x:(0,l(x))->R3, with 0<l(x)<infinity, alpha(gamma_x')=1 and conditional probability ds/l(x).
2. The measurable unstable vector Z with alpha(Z)=1 satisfies int|Z|dnu<infinity.

Then, for every C1 function g and C1 one-form theta defined near the compact support,

    int dg(Z) dnu=0,
    int dtheta(B,Z) dnu=-a int theta(Z) dnu,
    int U.Z dnu=1/a,
    int y.Z dnu=0.

The vector Z exists almost everywhere. Ergodicity and positive entropy exclude B=0 on a set of positive measure. At a regular Oseledets point, RB is the zero-exponent line, since B is bounded on the support and returns arbitrarily close to its nonzero starting value. It cannot coincide with R Omega, the negative-exponent line. The remaining unstable line is transverse to their span, which is ker alpha.

The covector transport law gives

    D Psi_t Z=e^(at) Z composed Psi_t,
    D Phi_t Z=e^(-at) Z composed Phi_t.

To prove the first integral, set h=dg(Z), which is in L1(nu), and G=max|g| on the support. For almost every partition atom and almost every t>=0, conditional integration and the transport law yield

    E[h composed Psi_t | xi]
       =e^(-at)/l(x) int_0^l d/ds [g(Psi_t gamma_x(s))] ds.

The atom lies in supp nu: every nonempty subarc has positive conditional length, so no subarc can lie outside that closed support. The integrand is integrable for almost every atom and t by Fubini and invariance. Integrating on compact subintervals and then taking their limits bounds the absolute value by 2G e^(-at)/l(x).

Let b_T=T^-1 int_0^T h composed Psi_t dt. For any delta>0, integrate the conditional estimate on l>=delta and use absolute values on the complement to get

    |int h dnu| <= 2G/(aT delta)
      + int_{l<delta} T^-1 int_0^T |h| composed Psi_t dt dnu.

The continuous-time L1 ergodic theorem makes the last time average converge in L1 to int|h|dnu. Therefore the limiting right side is at most nu(l<delta) int|h|dnu. Since l>0 almost everywhere, letting delta decrease to zero proves int h=0. No uniform lower bound on atom length is needed.

For f=theta(Z), transport gives along almost every complete regular orbit

    f(Phi_t z)=e^(at)(Phi_t^*theta)_z(Z(z)).

The derivative is (a f+(L_B theta)(Z)) composed Phi_t. All terms are L1, because B and the first derivatives of theta are bounded on the support and Z is integrable. Integrating in time and then against nu therefore gives

    int (a theta(Z)+(L_B theta)(Z)) dnu=0.

Cartan's formula L_B theta=i_B dtheta+d(theta(B)), and the already proved first identity applied to theta(B), give the second. Finally alpha=a U.dy+dH and alpha(Z)=1 give the U identity. Apply the first identity to |y|^2/2 for the y identity.

Thus the finite-mass current T(theta)=int theta(Z)dnu is closed. The finite-mass two-current R(beta)=int beta(B,Z)dnu satisfies boundary R=-a T, so T is explicitly null-homologous near the support. No corresponding null-homology claim about the flow current follows.

For a C1 vector field Y, decompose curl Y=y_B B+y_Z Z+y_Omega Omega almost everywhere. Since vol(Omega,B,Z)=-1,

    y_Omega=-d(Y.dy)(B,Z),
    int Y.Z dnu=(1/a) int y_Omega dnu.

The coefficient is integrable, even if the frame degenerates along a null or limiting set, because its displayed expression is bounded by a constant times |Z|. For Y=U or cy+U it equals one. These statements do not prove that int|Z| is finite for every vortical SRB measure.

## 3. Invariant sets at infinity without derivative decay

Assume only that U is C1, divergence free, bounded with M=sup|U|, and U(y)->0. Let c>0, A=cI-omega J and B=Ay+U. Let S be the continuous scattering map from A209, with

    S(Phi_t x)=e^(tA)S(x),
    |S(x)-x|<=d=M/c,
    K=S^-1(0),
    |S^-1(E)|=|E| for measurable E.

Its sharper bound is |S(x)-x|<=epsilon(|x|/2)/c when |x|>2d, where epsilon(r)=sup_{|y|>=r}|U(y)|. K is compact and null. Let F be any open or closed fully Phi-invariant set. Put C_F=S(F minus K), and let Pi_F=C_F intersect S2. Every nonzero linear A orbit meets S2 exactly once, so C_F is the twisted cone over Pi_F. Both sets are sigma compact: F minus K is sigma compact and the orbit projection is continuous.

For x in F with |x|>2d,

    dist(x,C_F)<=epsilon(|x|/2)/c.

For z in C_F with |z|>3d, choose x in F minus K with S(x)=z. Since |x|>=|z|-d>2d,

    dist(z,F)<=epsilon((|z|-d)/2)/c.

Thus the two sets have vanishing absolute distance discrepancy at infinity. Strict positive-radius inequalities avoid the harmless M=0, x=0 edge case in the submitted non-strict wording.

For fixed lambda>1 and rho>d, the annulus part F intersect {rho<|x|<lambda rho} is contained in

    S^-1(C_F intersect {rho-d<|z|<lambda rho+d}).

The twisted cone has annular volume area(Pi_F)(r_2^3-r_1^3)/3: at each radius its angular section is a rotation of Pi_F. Measure preservation therefore gives

    limsup_(rho->infinity)
      |F intersect {rho<|x|<lambda rho}| / |{rho<|x|<lambda rho}|
        <= area(Pi_F)/(4pi).

If area(Pi_F)=0, the entire cone is null, hence F minus K is null by the preimage formula; K is null too. In particular positive-volume F has positive-area twisted directions. This last implication does not need a separate density theorem.

## 4. Smooth flat zero sets and limits of the assertions

For a C-infinity vorticity field, the set F_flat where every derivative of Omega vanishes is closed and fully invariant under the smooth transport law. Almost every point of {Omega=0} belongs to F_flat. To see this, take a density-one point of that zero set. If some component has a nonzero jet, let m be the least order. Taylor expansion gives a nonzero homogeneous degree-m leading polynomial. On an open cone of directions its absolute value is bounded below by a positive multiple of |h|^m; for small radii the Taylor remainder cannot cancel it. This cone occupies a positive fixed fraction of every small ball, contradicting density one. Thus every jet vanishes. The density theorem gives |{Omega=0} minus F_flat|=0 locally and hence globally.

Consequently positive volume of the zero set implies positive volume of F_flat and, by Section 3 applied to F_flat, positive area of its twisted directions. Applying Section 3 only to {Omega=0} does not by itself justify replacing that set by the flat zero set. The infinite-jet conclusion requires smoothness; it is not a conclusion for merely C2 velocity.

Finally the submitted helicity identity is valid:

    kappa int U.Omega dnu = int Omega.grad(U.B) dnu.

Indeed L_B(U.dy)=-a U.dy+d(U.B-H) and L_B(i_Omega vol)=-a i_Omega vol. Their wedge gives B.grad(U.Omega)=-(2-c)U.Omega+Omega.grad(U.B-H), and Omega.grad H=-a U.Omega finishes the integrated formula. This identity currently has no sign control. The calculations establish no theorem that all Euler identities on nu are exhausted, that stable derivatives can never be controlled, or that no local obstruction to branch (V) exists. Those broader assertions remain OPEN.

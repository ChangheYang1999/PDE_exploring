# Tail helicity identities, bands, and exceptional orbits

## Exact setting

Use the C2 decaying Euler profile, 2/5<c<1/2, arbitrary real omega, and Dini gradient hypothesis of in the team records. That proof specifies the PDE, complete flows, scattering map S, compact null core K, and every external dependency. Retain k=(1-c)/c, delta=1-2c, A=cI-omega J, B=Ay+U, Omega=curl U, the continuous tail V, Omega_tilde=curl V, rho=log|z|, w=pi(z), G, G_r, and angular flow Y_t. Let

    h=U.Omega, h_tilde=V.Omega_tilde,
    tau=(Az).V, k0=tau restricted to S2, h0=h_tilde restricted to S2.

The cocycle h_t of the angular flow is distinct from the scalar helicity h. Every formula below writes its argument explicitly when confusion is possible. Put H=P+|U|^2/2+(Ay).U. For assertions about H at infinity take P=P_can+p_inf, where P_can is the canonical pressure, and use the existing Dini Bernoulli-tail result A355. Let D be a nonempty open set invariant under Phi_t and Gamma_t; its angular trace sigma_D is nonempty, open, and Y-invariant. Nonemptiness is necessary in the band-existence statement.

This audits the remainder of Theory Agent A C31, in the team records. No conclusion here excludes an Euler profile.

## 1. Tail identities and invariant moments

Twisted homogeneity gives

    tau(z)=exp(-(k-1)rho)k0(w),
    h_tilde(z)=exp(-(2k+1)rho)h0(w).

The tail Lamb identity is

    delta V + Omega_tilde cross Az + grad tau=0.

It follows distributionally from the homogeneity of V and the product rule for (Az).V. Its right-hand gradient is continuous, so tau and k0 are C1 even though no full C1 regularity of V is assumed. Dotting with Omega_tilde and multiplying by |z|^(k+2) gives

    d/dt tau(rho+h_t(w),Y_t w)
      =-delta exp(-(k-1)(rho+h_t(w)))h0(Y_t w).

Differentiating the homogeneous expression for tau yields

    Y k0=(k-1)G_r k0-delta h0.

The angular Jacobian law gives div Y=(k-1)G_r in its weak integrated sense. Thus wherever k0 is nonzero,

    div(Y/k0)=delta h0/k0^2.

Also (h_tilde/tau^2)dz=(h0/k0^2)d rho dA is invariant under the linear flow exp(tA), wherever defined; its pullback is the invariant signed density ((h_tilde composed with S)/(tau composed with S)^2)dy. These are locally defined densities off their scalar zero sets, not assertions of finite mass.

For every open invariant sigma and every C1 scalar function psi,

    delta integral_sigma psi'(k0)h0 dA
       =(k-1)integral_sigma [k0 psi'(k0)+psi(k0)]G_r dA.      (1)

Indeed integrate psi(k0(Y_t w))exp((k-1)h_t(w)) over sigma. It is constant in t by the area change of variables. Differentiate at zero, using boundedness on the compact sphere and the preceding transport identity. This proof has no boundary regularity assumption on sigma.

Taking psi=1 gives integral_sigma G_r=0. Taking psi(x)=|x|^p, p>1, gives

    delta p integral_sigma |k0|^(p-2)k0 h0
       =(k-1)(p+1)integral_sigma |k0|^p G_r.                (2)

For p=1 use psi_epsilon=sqrt(x^2+epsilon^2); dominated convergence gives sign(0)=0. If k0 is bounded away from zero, all real p are allowed. Taking psi=1/x then gives integral_sigma h0/k0^2=0. More generally that last conclusion remains valid if k0 never vanishes on sigma and both 1/k0 and h0/k0^2 belong to L1(sigma). Along each finite flow segment differentiate 1/k0; its weighted derivative is -delta h0/k0^2. The stated L1 assumptions, bounded finite-time Jacobians, and invariance justify Fubini and the integrated difference quotient. This avoids applying an unbounded test function without a domination argument.

In particular a nonnegative h0 that is nonzero on an invariant component forces k0 to vanish somewhere on its closure. Formula (1) with psi=x is delta integral h0=2(k-1)integral k0 G_r; it gives a correlation, not a contradiction.

## 2. Signs at infinity and the crossing statement

For each y outside K, the tail asymptotics and DS(Phi_t y)->I give

    exp((2-c)t) h(Phi_t y) -> h_tilde(Sy).                  (3)

To check the exponent, U(Phi_t y)=exp(-(1-c)t)Q_t^T V(Sy)+o(exp(-(1-c)t)), and Omega(Phi_t y)=DS(Phi_t y)^(-1)exp(-t)Q_t^T Omega_tilde(Sy). Their dot product cancels both rotations. Therefore if h0 has a positive value and a negative value on sigma_D, h has each strict sign on subsets of D of infinite volume. For example, on the positive cone every point is eventually positive. Intersect the increasing sets of points positive for all t>=T with a fixed bounded positive-measure part of that cone. Their measures are bounded below for all large T, while Phi_T multiplies volume by exp(3cT). The negative case is identical.

If h0>0 on sigma_D, tau strictly decreases on every tail vortex orbit in its cone. Where k0=0 the derivative Y k0=-delta h0 is negative. Thus its zero set inside sigma_D is a C1 transverse curve, with crossings only from positive to negative k0. Each orbit crosses at most once. For almost every angular initial point, Theorem TB gives rho+h_t->negative infinity at both ends. If such an orbit never crosses and tau stays positive, tau has a finite nonnegative positive-time limit; hence k0(Y_t w)=exp((k-1)(rho+h_t))tau tends to zero as t tends to positive infinity. If tau stays negative use negative time instead. This proves precisely Proposition M(iii), with its almost-everywhere qualifier.

The header's word every is not justified. The explicit tail in section 4 below already has fixed angular poles with h0=2 and k0=+c or -c. If sigma is the whole sphere, each such exceptional orbit neither crosses k0=0 nor approaches it. This is a counterexample to the stronger statement within the reduced tail identities and Theorem TB, which are themselves almost-everywhere statements. It is not an example of a global decaying Euler profile. The stronger all-orbit Euler assertion remains OPEN.

## 3. Differential forms and the scope of the measure interpretation

Write alpha=(B cross Omega).dy and beta=(Az cross Omega_tilde).dz. The determinant-one differential of S preserves scalar triple products, so

    alpha=S^*beta,
    beta=c exp(-(k-1)rho) pi^*(i_Y dA),
    d beta=delta i_{Omega_tilde}dz.                        (4)

For the second formula evaluate beta on the radial direction and on vectors tangent to the unit sphere. The radial value is zero. The tangential value is (Aw cross Y).u=c(w cross Y).u, because Jw and Y are tangent and their cross product is normal. Homogeneity gives the factor at other radii. The last formula is the exterior derivative of beta=delta V.dz+d tau and holds with the continuous curl already established.

Where Y is nonzero, ker beta is spanned by partial_rho and Y. Its leaves are cones over angular orbits. Nonperiodic angular orbits give C1 immersed planes, so almost every nonzero-vorticity orbit has this type by Theorem TB. Where Y=0 the form beta vanishes and its kernel is three-dimensional; no two-dimensional leaf is asserted there. Formula (4) gives the exact alpha-length of a transverse curve off K as its weighted projected Y-flux.

It does not literally push an invariant probability nu on the compact trapped set to the far field. A compact Phi-invariant probability support lies in K, where S is collapsed and is not the diffeomorphism in (4). Thus the final sentence of the source about unstable conditionals of nu in the far field needs an additional specified extension or transport of transverse measures to curves off K. Only the local transverse-form formula is CONFIRMED here; that unspecified probability-measure identification is OPEN.

## 4. An exact one-signed tail for every rotation

In spherical coordinates about the rotation axis set b0=-(2-k)/2 and

    V=r^-k[cos(theta)e_r+b0 sin(theta)e_theta+sin(theta)e_phi].

This field is smooth off zero, axisymmetric, and homogeneous of degree -k, hence has the required twisted homogeneity for every omega. The divergence is r^(-k-1)[(2-k)cos(theta)+2b0 cos(theta)]=0. Direct spherical curl gives

    Omega_tilde=r^(-k-1)[2cos(theta)e_r+(k-1)sin(theta)e_theta
                      +(1+(k-1)(2-k)/2)sin(theta)e_phi],
    h_tilde=r^(-2k-1)(1+cos(theta)^2).

The helicity calculation uses b0(k-1)+1+(k-1)(2-k)/2=1. The angular field is

    Y=(k-1)sin(theta)e_theta
      +[1+(k-1)(2-k)/2+(2omega/c)cos(theta)]sin(theta)e_phi,
    G_r=2cos(theta).

For every nonpolar orbit theta'=(k-1)sin(theta), and

    h_t=(2/(k-1))log(sin(theta(t))/sin(theta(0))).

It tends to negative infinity at both ends with an exponential rate sufficient for both summability conclusions. The poles are precisely the exceptional fixed angular points discussed above. Finally

    k0=c cos(theta)-omega sin(theta)^2.

There is one zero latitude, with cos(theta)=2omega/(c+sqrt(c^2+4omega^2)), interpreted as zero for omega=0. The derivative in theta along the flow at that latitude is negative, as also follows from Y k0=-delta h0. The formula for the root follows by solving omega u^2+cu-omega=0 and selecting the unique root in (-1,1). Thus this example satisfies the audited tail identities, positive helicity, and the almost-everywhere return structure for every omega. It is only a tail field. Its being the tail of any global profile is not claimed.

## 5. Uniform tail sign gives band information

Assume inf_{sigma_D}h0>0. The bounded displacement S(y)-y, uniform continuity of V on compact annuli, U=V+o(r^-k), and DS->I give uniformly for y in D at infinity

    h(y)=h_tilde(Sy)+o(|y|^(-2k-1)).

Therefore there is a radius R with h>0 on D outside that ball. The scalar k0 is not identically zero on sigma_D, since Yk0=(k-1)G_r k0-delta h0 would then contradict h0>0. Choose a point with k0 nonzero. The Bernoulli-tail limit

    exp(delta t)(H(Phi_t y)-p_inf)->tau(Sy)

shows that H on the far part of this orbit approaches p_inf from one fixed side. The intermediate value theorem therefore supplies a nonempty one-sided interval J0 adjacent to p_inf whose every value is attained at a point of D outside the ball with h>0.

For each nonempty open subinterval I of J0, the far-field set D intersect {H in I} intersect {h>0} is nonempty and open, hence contributes positive mass to integral h_+. Under Dini, h is L1. The already audited vortex-invariant band balance A328 says

    integral_{D intersect {H in I}}h_-
       =integral_{D intersect {H in I}}h_+>0.

Since h_- vanishes outside the fixed ball, D intersect B_R intersect {H in I} intersect {h<0} has positive volume. For each v in the closure of J0, choose such points in shrinking bands and pass to a bounded subsequence. The limit belongs to the closure of D intersect B_R and satisfies H=v and h<=0. This is exactly the stated Corollary FB, after making D nonempty explicit. The negative-tail case follows by reversing signs.

The stronger prose after Corollary FB is not proved by this argument. The limiting point may lie on the boundary of D and may have h=0. Thus the audit does not certify that every exact v in J0 has a point inside D with H=v and h<0. An elementary illustration of this logical distinction is the periodic scalar q(s)=sin(s)(1-cos(s)), with h(s)=-q'(s)/delta. At level q=0 the downward crossing at s=pi has h>0, whereas the upward crossing at s=0 is flat and has h=0. No point of that level has h<0. Nevertheless the positive and negative weighted pushforwards under q balance on every Borel band, by integration of an antiderivative over one period. This illustration is not Euler and does not bypass A014; it shows why a band identity and recurrence alone cannot supply the missing strictness.

For completeness, a nonzero angular absolute helicity integral gives

    integral_{0<|z|<1, pi(z) in sigma_D}|h_tilde|dz
      =integral_{sigma_D}|h0|dA integral_0^1 r^(1-2k)dr=infinity.

Therefore the integrable actual helicity balance cannot be passed to the tail by dominated convergence near the collapsed core. This is the same obstruction confirmed in A358.

## Verdicts

A361 CONFIRMED: the tail transport, angular moment identities, forward helicity coefficient, and Proposition M with its almost-everywhere qualifier.

A362 CONFIRMED: the exact local differential-form formula and the one-signed example for every omega. No global profile is constructed.

A363 CONFIRMED: Corollary FB in its written band form, for a nonempty domain, and its closure/non-strict-sign consequence.

A364 OPEN: the stronger every-orbit summary, every-exact-level strict opposite sign, and literal far-field identification of nu-conditionals. The proof supplies only the weaker statements specified above. The explicit reduced examples identify the logical gaps; they are not counterexamples to the original global Euler conjecture.

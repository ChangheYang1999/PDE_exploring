# Global rigidity and the exceptional radial class for a normalized form

## 1. Exact theorem

Let G=R3 minus{0}, 0<c<1/2 and omega be any finite real number. Write Jx=e3 cross x, X=(cI-omega J)x, Q_t=exp(-omega tJ), F_t x=exp(ct)Q_t x, gamma=c/(1-c), eta=(1-gamma)/2 and m=1/c. Suppose V in C1(G;R3) satisfies

    div V=0, V(F_t x)=exp(-(1-c)t)Q_t V(x)

for every real t. Assume the continuous form

    alpha=|V|^(gamma-1)V on {V!=0}, alpha=0 otherwise

is closed in distributions on G. If c!=1/3, then V=0. At c=1/3 the complete class consists of V(x)=Kx/|x|³, K any real constant. The first conclusion and existence of the exceptional examples are LIT246; completeness of that exceptional class is an additional argument in Section7.

For c>1/3, a sufficient hypothesis for closedness is V in C2 and

    |V|² curl V=eta grad(|V|²) cross V               (1)

where V!=0. For every 0<c<1/2, one can instead assume V in C_loc^(k,theta), k+theta=(1-c)/c, k>=1 and 0<theta<=1, together with (1). At integer k+theta=N use k=N-1, theta=1. These conditions concern every nonzero point in G. No scalar pressure, helicity or energy premise is needed. This is a theorem about the extra globally closed class.

## 2. One global potential and its drift

The form is continuous since |alpha|=|V|^gamma. Mollification and local radial integration give C1 potentials on balls. Their differences are constants. The domain G retracts onto the simply connected sphere S2, so the local potentials patch, by continuation along paths and homotopy independence, to a single C1 function psi with grad psi=alpha. An axis-deleted domain would not justify this step.

The homogeneity exponent gives alpha(F_t x)=exp(-ct)Q_t alpha(x), hence F_t^*alpha=alpha. Thus psi(F_t x)-psi(x) is a spatial constant d(t). It is continuous and additive in t by the group law, so d(t)=Ct for some real C. Therefore

    psi(F_t x)=psi(x)+Ct, X.grad psi=C.             (2)

Since gamma(m-1)=1, V=|grad psi|^(m-2)grad psi, including at zeros. The potential is a C1 weak m-harmonic function on G. If V has even one zero, (2) already forces C=0.

## 3. The needed maximum principle with a comparison proof

A C1 weak m-harmonic function, m>1, attaining a global maximum on a connected open set is constant. To see this let h=M-psi>=0. If positive and zero points both exist, choose a positive point y close to the boundary of the zero set and let R be its distance to that set, small enough that the closed ball remains in the domain. Then B_R(y) is positive and its boundary touches a zero x0. On the inner sphere of radius R/2, h has a positive minimum delta.

On this annulus the radial m-harmonic function with inner value delta and outer value zero is

    w(r)=delta [r^kappa-R^kappa]/[(R/2)^kappa-R^kappa],
    kappa=(m-3)/(m-1),

if m!=3, and w(r)=delta log(R/r)/log2 if m=3. It has w'(R)<0. Weak comparison gives h>=w: test the difference of their weak equations with (w-h)_+, whose boundary trace is zero, and use strict monotonicity of z -> |z|^(m-2)z. Along the inward radius ending at x0 this lower bound forces a strictly positive inward derivative of h. But a nonnegative C1 function at an interior zero has zero gradient. This contradiction proves the assertion.

If C=0 in (2), every F_t orbit meets S2 once and psi is constant along it. The maximum of psi on S2 is therefore its global maximum on G, attained at an interior point of G. The preceding comparison proof makes psi constant and V zero. This step uses a global attained maximum, not a local unique-continuation theorem.

## 4. Angular extrema exclude nonzero drift away from c=1/3

Suppose C!=0, put beta=C/c and define

    pi(r theta)=exp((omega/c)log(r)J)theta.

Then x=F_(log(r)/c)pi(x), and (2) reads

    psi(x)=beta log r+u(pi(x)), u=psi restricted to S2. (3)

The C1 function u has both a maximum and a minimum. At either extremum theta, tangential du=0 and grad psi(theta)=beta theta!=0. Since V is C1 and nonzero there, alpha is C1 nearby, so psi and u are C2 there. The ordinary Hessian chain rule at that critical point gives

    D²psi=beta(I-2theta tensor theta)
              +(Dpi)^T Hess_S2(u) Dpi.              (4)

Terms containing du vanish. At a nonzero gradient, the m-Laplace equation becomes

    0=tr(D²psi)+(m-2)theta^T D²psi theta.

Set A0=I+(m-2)theta tensor theta, positive definite. Substituting (4) yields

    0=beta(3-m)+tr[A0(Dpi)^T Hess_S2(u)Dpi].          (5)

The second term is nonnegative at a minimum and nonpositive at a maximum. If beta(3-m)>0 choose the minimum; if beta(3-m)<0 choose the maximum. Both contradict (5). For beta!=0 and m!=3 these exhaust the possibilities. Thus C must be zero, and Section3 concludes the first theorem. All rotation terms occur only in Dpi within a semidefinite quadratic form; no rotation bound or angular truncation appears.

## 5. Exact exceptional examples

When c=1/3, gamma=1/2 and m=3. For V=Kx/r³ one has div V=0 on G and the required twisted homogeneity for every omega. Its normalized form is

    alpha=sign(K)|K|^(1/2) grad log r.

It is globally closed on G. For K!=0 the field has flux 4pi K and is singular at the origin. It even solves the punctured rotating similarity equation with P=-K²/(2r^4): the linear similarity terms cancel and V.grad V=-2K²r^(-5)e_r cancels grad P. This is not a smooth whole-space profile or a counterexample in the campaign interval.

## 6. Classical closedness and finite regularity

A1541-A1545, reproduced in the pinned zero-set dependency, establish that T_gamma(V) is W_loc^(1,s) for every s<1/(1-gamma) under the stated C^(k,theta) hypothesis. Off {V=0}, equation(1) makes its curl zero. On that zero set the weak derivative is zero almost everywhere. Hence closedness holds distributionally on all G, without geometric restrictions on zeros. No flatness assumption is required for this removal step.

For gamma>1/2, the independent C2 estimate is obtained by integrating the derivative of t(t²+epsilon²)^(gamma-1) against a compact cutoff. Its derivative is at least (2gamma-1)(t²+epsilon²)^(gamma-1), while the original expression is bounded by |t|^(2gamma-1). This gives uniform W1,2 bounds for (|V|²+epsilon²)^((gamma-1)/2)V and the same passage. The complete estimate and level-set argument are in the pinned proof and were read. These hypotheses prove both sufficient versions in Section1. In the target interval, C^(1,1/c-2) already suffices for the global theorem if (1) holds everywhere off the velocity zero set.

## 7. Completeness of the exceptional class

Retain c=1/3 but allow any C in (2). Put beta=C/c, psi0=beta log r and V0=|grad psi0|grad psi0=beta|beta|x/r³, including beta=0. Both V and V0 are divergence free, and u0=psi-psi0 is C1 and invariant under F_t.

Fix an annulus r1<|x|<r2. Integration by parts, permissible for the C1 potential and C1 fluxes, gives

    integral_annulus (V-V0).(grad psi-grad psi0)
       =integral_outer u0(V-V0).n
          -integral_inner u0(V-V0).n.               (6)

Both boundary integrals have the same value. Indeed F_t maps one sphere onto another; u0 is invariant, V-V0 acquires exp(-2ct)Q_t, the normal acquires Q_t and area acquires exp(2ct). Thus their products cancel exactly. The right side of (6) is zero.

The left integrand is nonnegative and is zero only when grad psi=grad psi0, by strict monotonicity of z -> |z|z. It is continuous, so it is zero everywhere on the annulus. Arbitrary radii give V=V0 throughout G. Therefore every field in the exceptional class is precisely radial, as claimed. This classification uses no smooth angular unique continuation, pressure equation or flux condition at the missing origin.

## 8. Verdict and limitations

The complete seven-section LIT246 source was independently checked. Its global rigidity, all-omega angular calculation and radial exception are confirmed. The finite-regularity sufficient condition and complete exceptional classification are additional proved refinements submitted for comparison through the existing configured model agents; provider runtime is unattested. The globally closed premise is stronger than generic tail rank and is not established for every actual tail. The theorem does not settle the arbitrary-helicity or bare-decay conjecture. No numerical computation or formal build was used.

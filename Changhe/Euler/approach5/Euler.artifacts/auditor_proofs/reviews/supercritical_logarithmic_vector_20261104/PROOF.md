# Independent audit of the supercritical logarithmic vector example

The audited source is LIT352, submitted SHA256 b193cd69cfa6e116388bb1610b935b0afccde0455b84853360f2deddc0933878. All nine sections and49manual checks were read before this reconstruction. This proof does not use numerical evidence. The existing configured model comparison remains pending at initial writing.

## 1. Exact assertion

For every A>1/8 there is a map u in C-infinity({z in C:|z|<exp(-1)};C^2) with every Cartesian derivative at0 equal to0, with |u(z)|>0 off0, and with

    |dbar u(z)|<=[1/4+A/log^2(1/|z|)] |u(z)|/|z|.

Here the target is two complex components, the norm is Euclidean, and dbar=(partial_x+i partial_y)/2. The radial majorant b(z)=[1/4+A/log^2(1/|z|)]/|z| is weak-L2, with

    K2(b)<=sqrt(pi)(1/4+A),
    lim_(lambda->infinity) lambda^2 area{b>lambda}=pi/16.

Its associated excess over the cylinder constant1/2 is integrable and has arbitrarily small integrals on late time tails. Consequently integrability of that excess alone does not imply continuation, even for a smooth vector flat to all orders. No scalar or three-dimensional Euler example is asserted.

## 2. A fixed smooth transition shape

Define chi(x)=0 for x<=0 and chi(x)=1 for x>=1. On0<x<1 define

    chi(x)=exp(-1/x)/(exp(-1/x)+exp(-1/(1-x))).

The exponential vanishes to every order at the indicated endpoint, the denominator stays positive there, and the analogous statement at1 follows by reflection. Hence chi is smooth. It satisfies chi(x)+chi(1-x)=1 and has integral1/2 on[0,1]. Let ell=pi/4. Define a smooth p by0 outside[0,3ell], chi(q/ell) on[0,ell], 1 on[ell,2ell], and chi((3ell-q)/ell) on[2ell,3ell]. At the joins the constant endpoint jets agree to all orders. Then 0<=p<=1 and integral p=ell/2+ell+ell/2=pi/2.

Set h(s)=integral_(-infinity)^(s-1)p(q)dq and L=2+3ell. This smooth nondecreasing angle is0 for s<=1 and pi/2 for s>=1+3ell. It has derivative at most1, with derivative exactly1 on[1+ell,1+2ell]. Over that middle interval its values run from pi/8 to3pi/8. The interval[0,L] has an initial and a final plateau each of length1. These are genuine constant neighborhoods, not only matching jets.

## 3. Every clock transition ends in finite time

Write a=2A>1/4 and g(t)=1/2+a/t^2 for t>=1. For any t0>=1 solve

    s'=g(t)-sin(h(s))cos(h(s)),   s(t0)=0.

The derivative of the right side with respect to s has absolute value at most1, since h'<=1. It is smooth and globally bounded between a/t^2 and1/2+a. Picard-Lindelof and this bound give a unique solution on every finite future interval. It is strictly increasing. The first time T at which s=L has not yet been assumed to exist.

Choose kappa strictly between1/(4a) and1, and then delta in(0,pi/8) so small that sin^2(phi)>=kappa phi^2 when |phi|<=delta. Let

    D0=L/sin^2(delta), b0=sqrt(kappa a-1/4),
    Q=exp(pi/b0), K=Q+(Q+1)D0, d=L/(1/2+a).

All these constants are finite and positive, and K>1. The right side of the equation equals a/t^2+sin^2(h(s)-pi/4). Before the angle reaches pi/4-delta it is at least sin^2(delta), so that boundary is reached by time te<=t0+D0. This follows by integrating s'>=sin^2(delta) over a still uncompleted subinterval of s-values of length at most L.

Between the two angle boundaries the definition of h ensures h'=1. Put phi=h(s)-pi/4, w=t phi and x=log t. Then

    phi'=sin^2(phi)+a/t^2 >= kappa phi^2+a/t^2,
    dw/dx >= kappa w^2+w+a.

The algebraic identity

    kappa w^2+w+a=((kappa w+1/2)^2+b0^2)/kappa

implies, for Y=(kappa w+1/2)/b0,

    d(arctan Y)/dx >= b0.

The arctangent has total range of length pi. The solution therefore cannot remain between those angle boundaries for a logarithmic time interval of length pi/b0. It exits through the upper boundary by tx<=Q te. An exit through the lower boundary is impossible because s and h(s) are increasing there; a blowup of s is impossible because its derivative is bounded on finite time intervals. At every such finite time w=t phi is finite as well. Thus this bounded-angle argument proves the exit without assuming it.

After that exit the right side is again at least sin^2(delta) until s=L, taking at most D0 more time. Hence

    T<=Q(t0+D0)+D0<=K t0.

The upper derivative bound and the change s(T)-s(t0)=L also give T-t0>=d. Both bounds hold uniformly in t0.

## 4. Joining times and a superlinear envelope

Start t1=1 and recursively apply Section3 from tn, putting t_(n+1)=T. Then

    1+(n-1)d<=tn<=K^(n-1),

so the intervals cover[1,infinity) without finite accumulation. Let theta_n=h(s) on the n-th interval. Put F(1)=0 and

    F'(t)=n+sin^2(theta_n(t)).

Near the end of this interval theta_n=pi/2, so F'=n+1. Near the start of the next interval theta_(n+1)=0, giving exactly the same value. Since the speed of s is bounded above and the s-plateaus have positive length, they supply actual time neighborhoods on both sides of every join. Thus F is smooth there.

On the interval with index n, t<=t_(n+1)<=K^n and t>=tn>=1+(n-1)d. Therefore

    log(t)/log K<=n<=1+(t-1)/d,
    F(t)>=(t log t-t+1)/log K.

The first inequality integrated from1 gives the stated envelope. Its growth is superlinear, whereas the active mode number grows at most linearly with t.

## 5. The vector and exact differential inequality

Let e_n alternate between the two standard orthonormal basis vectors of C^2, using e1 for odd n and e2 for even n. If z=r exp(i vartheta), t=log(1/r), and t is in the n-th interval, define

    U(t,vartheta)=exp(-F(t))[
          cos(theta_n(t)) exp(i n vartheta)e_n
        + sin(theta_n(t)) exp(i(n+1)vartheta)e_(n+1)],
    u(z)=U(log(1/r),vartheta).

Integer frequencies make the expression single-valued. Its pointwise norm is exp(-F)>0. At t_(n+1) the two formulas agree with the mode n+1 in the same component. On the two adjacent plateau neighborhoods F' is identically n+1; continuity of F makes the common function a fixed constant times z^(n+1)e_(n+1). This proves smoothness across the joining circle to every order.

Let Dtheta=-i partial_vartheta and abbreviate theta=theta_n. Direct differentiation gives

    U_t+Dtheta U=exp(-F)(theta'+sin(theta)cos(theta))[
        -sin(theta)exp(i n vartheta)e_n
        +cos(theta)exp(i(n+1)vartheta)e_(n+1)].

For example the first coefficient is -sin(theta)theta'-cos(theta)sin^2(theta), and the second is cos(theta)theta'+sin(theta)cos^2(theta). This checks both signs and the envelope cancellation. The bracket has norm1. Since

    0<=theta'=h'(s)[g-sin(theta)cos(theta)]
             <=g-sin(theta)cos(theta),

the norm of the residual is at most g exp(-F). The polar identity

    dbar=exp(i vartheta)(-partial_t+i partial_vartheta)/(2r)

now gives |dbar u|/|u|<=[1/4+A/t^2]/r. Near a join the residual vanishes identically, so the inequality holds there as well, not only in interval interiors.

## 6. Smooth extension with every derivative zero

Every derivative of g is bounded on[1,infinity), and every derivative of h is bounded on the real line. The first derivative s' is uniformly bounded. Inductively differentiating its equation expresses every higher s derivative as a finite sum of products of bounded derivatives of g,h and lower derivatives of s. Hence, for each fixed order, the derivatives of s and the positive-order derivatives of theta_n are bounded uniformly in the interval index n.

The envelope satisfies |F'|<=n+1; all its derivatives of order at least2 are bounded uniformly. These bounds also hold through the joins, where F' is locally constant. Repeated differentiation of exp(-F) and the angular modes therefore yields

    |partial_t^j partial_vartheta^k U|
        <=C_m(1+n)^m exp(-F),  j+k<=m.

The constants may depend on m and A, but not n or t. Each Cartesian derivative is r^(-1) times a smooth bounded angular combination of the time and angular derivatives. Differentiating those coefficients repeatedly introduces only additional factors r^(-1) and bounded trigonometric coefficients. Thus for |alpha|=m,

    |partial_cartesian^alpha u(z)|
       <=C'_m(1+t)^m exp(mt-F(t)).

For every fixed m and every N>0 this is o(exp(-Nt))=o(r^N), by the lower bound in Section4. Set u(0)=0 and extend each punctured derivative by0. The estimates make them continuous at0. They are also o(r), so each is differentiable at0 with derivative0. Induction on derivative order shows that these extensions are precisely all the Cartesian derivatives of u. Hence u is smooth and flat to every order, while remaining nonzero everywhere off0. Uniform flatness also gives infinite Lp integral order for each finite p.

## 7. Exact high tail and integrable excess

The coefficient obeys b<=(1/4+A)/r, and the weak-L2 norm of1/r on the disc is sqrt(pi), giving the asserted upper norm bound. For any epsilon in(0,1/4), a sufficiently small punctured disc has

    (1/4-epsilon)/r<=b<=(1/4+epsilon)/r.

The coefficient is uniformly bounded on its complement in the original disc, including near the finite outer radius because its formula extends continuously there. For large lambda its superlevel set is therefore contained in that smaller disc and is trapped between discs of radii (1/4-epsilon)/lambda and (1/4+epsilon)/lambda. Their squared-radius area bounds imply the limit pi/16 on sending epsilon to0. No radial monotonicity was needed.

The cylinder inequality has majorant1/2+a/t^2. Its excess is integrable, with integral a/T from T to infinity, tending to0. The constructed solution is nevertheless nontrivial and flat. This refutes sufficiency of an arbitrary nonnegative integrable excess, including a condition that only demands arbitrarily small late-tail integrals. It does not refute the specific pointwise bound with A=1/8.

## 8. The logarithmic-power comparison using A2942

The positive LIT351 theorem is now independently confirmed as A2942. Combining it with this construction, if the latter is confirmed, gives the following local classification for [1/4+A/log^p(1/r)]/r, A>0, p>0, in the class allowing two complex target components.

For p>2 choose T>=1 so large that A/t^p<=1/(8t^2) for t>=T. The smaller disc has radius exp(-T). A2942 applies there with Rstar=exp(1-T), whose logarithm is t-T+1 in[1,t]. Its allowed correction is at least1/(8t^2), so it dominates the given coefficient. Thus a locally L2, punctured H1, integral-flat vector vanishes near0. For p=2 and A<=1/8, the same comparison, or the original scale T=1, works. For p=2 and A>1/8, Sections2-7 give the smooth counterexample. If0<p<2, choose any A0>1/8 and then T so large that A0/t^2<=A/t^p for t>=T; restriction of the A0 example provides a counterexample on that smaller disc. Positive connected propagation retains the local boundedness condition away from0.

Sharpness here is solely within this logarithmic family and for a target dimension that allows two complex components. It is not a scalar sharpness theorem. Smooth scalar weak-L2 continuation has its own separate proof and is not contradicted.

## 9. Dependencies and remaining scope

The negative construction is independent of A2942 and of the earlier vector examples. Its analytic inputs are the explicit smooth step, Picard-Lindelof for a globally Lipschitz scalar field, a bounded-angle differential inequality, and elementary derivative estimates. The positive classification in Section8 explicitly uses A2942. No computation or external source theorem is a hidden step.

The complete source and49manual checks are retained in verification. The existing configured model comparison is requested through the already active agents; actual provider execution is independently unattested. A comparison and full postread are still needed before the designated verdict. No new model client or formalization was used. The finite-regularity scalar endpoint at arbitrary weak norm, the reduced Euler coefficient estimate and the unrestricted rotating Euler conjecture remain OPEN.

## 10. Existing model comparison and diagnostic scope

The complete existing configured model Theory Agent C  comparison dated 2026-11-04T05:05:41Z has now been read against Sections 1-9 above. Its eleven mathematical items agree with the independent reconstruction. The actual provider execution remains independently unattested. The clock proof does not depend on an ODE approximation or on a claimed analytic solution of the nonlinear transition equation. Its bounded-angle argument, and the existence of genuine holomorphic neighborhoods at each seam, are decisive.

One literal qualification to item 8 is necessary: the displayed formula g^(j)=a(-1)^j(j+1)!t^(-j-2) holds for j>=1. For j=0 the constant 1/2 must be included. The stated conclusion that every derivative, including g itself, is bounded is still correct, and the submitted source uses only that conclusion.

The entire 226-line diagnostic script and its 38-line log have been read, including the final failure exit. There are 24 conditions: eight symbolic checks, four entries labelled EX, one quadrature, seven sampled checks, two entries labelled FIN and two grids. Both FIN entries concern finitely many numerically integrated transitions, so they are numerical evidence, not exact finite certificates. One EX entry is a finite-time ODE negative control and another uses Cartesian finite differences; those are numerical evidence as well. The remaining two EX entries are symbolic wrong-sign controls. The polar identity test uses one polynomial; the universal chain-rule identity is proved by hand in Section 5.

The reported samples agree with their limited predicates. In particular the approximately 4.4e13 ratio for A=0.13 describes the large-initial-time samples; the t0=1 sample is approximately 1.06e14. Neither is used to estimate the rigorous constant K. The seam sample compares nearby points and does not prove equality of all derivatives; the exact plateau formula does. No diagnostic was rerun and no mathematical computation was added in this agent.

The comparison therefore supports the negative construction and, together with A2942, the stated local logarithmic-power classification, subject to the exact regularity and integral-flatness hypotheses above. It supplies no scalar or Euler counterexample, no optimality beyond this coefficient family and target class, and no bound on an Euler-derived quotient.

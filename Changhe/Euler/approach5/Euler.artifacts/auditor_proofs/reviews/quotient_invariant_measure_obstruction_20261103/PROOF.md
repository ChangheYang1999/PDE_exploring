# Invariant measures behind the twisted flux inequality

Status: CONFIRMED in A645 after complete independent reconstruction and postread.

## 1. Exact setting and claims

Retain exactly the C1 divergence-free twisted field and nodal condition(N) of in the team records, with 1<p<2, t=omega/c, mu=2-p, and sphere quotient field X=Bq. Thus div X=-mu R, R=K+tF, and the complete X flow Phi satisfies Phi_(-s)O_+ subset O_+ for O_+={K>0}, s>=0.

Assume O_+ is nonempty. Put C_+=closure O_+ and define the compact nonempty set

    Lambda_+=intersection_{s>=0} Phi_(-s)C_+.

This is the maximal FULL invariant subset of C_+. Calling it merely a maximal backward-invariant subset is misleading, since C_+ itself is backward invariant.

There is an X-invariant probability nu supported on Lambda_+ such that integral R dnu<=0. More generally, for any nonempty compact invariant set Lambda of a C1 field X and any C1 scalar a on its compact ambient manifold, the following are equivalent:

    every invariant probability on Lambda has integral a>0;
    there is a C1 u with a-Xu>0 on a neighborhood of Lambda.    (1)

The corresponding positive weight is psi=exp(u). In the application a=mu R, so the obstruction is to a positive weighted-divergence correction.

These claims concern measures of the quotient field X. They do not establish absence of such measures for actual Euler tails, or literal azimuthal winding of their trajectories.

## 2. The compact invariant set

Closure and continuity extend backward invariance from O_+ to C_+. The sets Phi_(-s)C_+ are nonempty compact and decrease with s. Their intersection is nonempty. Applying any fixed Phi_t merely shifts the lower bound on the intersection parameter, so Phi_t Lambda_+=Lambda_+ for all real t.

Conversely, every full invariant subset of C_+ lies in every Phi_(-s)C_+. This proves maximality in the full invariant sense. For any open neighborhood N of Lambda_+, all sufficiently late Phi_(-s)C_+ lie in N. Otherwise a sequence of points outside N from later nested compact sets would have a limit in Lambda_+ outside N.

## 3. Positive invariant averages and a finite-time potential

Invariant probabilities exist on a nonempty compact invariant set: take weak limits of time averages along any point. For a continuous test b and fixed tau, the difference between its integral after time tau and before is bounded by 2|tau| ||b||_infinity/T on a time average of length T. Passing to a weak limit proves invariance. The invariant probability set is weakly compact by the same test criterion.

Suppose every invariant probability on Lambda integrates a positively. Compactness supplies a minimum delta>0 of these integrals. For sufficiently large T, every x in Lambda has

    (1/T) integral_0^T a(Phi_s x) ds > delta/2.                 (2)

If not, empirical probabilities from a sequence T tending to infinity would have an invariant weak limit on Lambda with integral a<=delta/2, a contradiction.

Choose one such T and define on the ambient manifold

    u(x)=-(1/T) integral_0^T (T-s)a(Phi_s x) ds.

The field, finite-time flow and a are C1, so u is C1. Differentiating along the flow and integrating by parts gives

    Xu=a-(1/T) integral_0^T a(Phi_s x) ds.

Thus a-Xu is the positive finite-time average in(2). Continuity makes it positive on a neighborhood of Lambda.

Conversely, for an invariant probability nu, integral Xu dnu=0 by differentiating integral u(Phi_t x)dnu at t=0. If a-Xu is positive on compact Lambda, its integral is strictly positive. This proves(1), with no assumption of ergodicity or periodic-orbit density.

## 4. The nonpositive-mean measure is unavoidable

Assume, to the contrary, that every invariant probability on Lambda_+ has integral R>0. Apply Section3 with a=mu R to obtain a global C1 u and psi=exp(u)>0 satisfying

    mu psi R-Xpsi>0

on a neighborhood N of Lambda_+. Choose s large enough that O_s=Phi_(-s)O_+ lies inside N. O_s is a nonempty open set, hence has positive area, and is backward invariant. Differentiating its weighted area under negative flow gives, exactly as in A641,

    integral_{O_s}(mu psi R-Xpsi)<=0.

The integrand is positive on O_s, a contradiction. Therefore an invariant probability on Lambda_+ has nonpositive R mean. The negative region similarly has an invariant probability of nonnegative R mean for its forward limiting invariant subset.

Boundary points of Lambda_+ with K=0 are zeros of V. Indeed a regular zero of K immediately exits C_+ forward, impossible on a full invariant subset; at a critical zero, condition(N) gives gamma=0 and hence V=0. Such points are fixed points of X, and their point masses have R mean zero. The obstruction measure above may be supported entirely on these points. No recurrent nonzero-velocity orbit is inferred.

## 5. Swirl correlation is not an unweighted winding statement

For any probability supported in {K>=0}, integral R<=0 implies

    t integral F<=-integral K<=0.

On a set away from the axis, the actual angular velocity of X is

    Xchi=F/w+tR, w=1-z^2.

Solving for R gives

    R=K/(1+t^2 w)+[t w/(1+t^2 w)]Xchi.                        (3)

Thus a nonpositive R average enforces a weighted angular-turning condition with coefficient w/(1+t^2 w). This coefficient depends on latitude. It is not the unweighted net angle or topological winding number.

For a direct geometric check, choose two distinct positive latitudes z_1,z_2, avoiding the poles, and a small angular interval [chi_1,chi_2] of length less than pi. The boundary of that latitude-angular rectangle is a closed contractible curve with zero net angular change. Nevertheless the integral of [w/(1+t^2 w)]dchi around it is

    [w(z_1)/(1+t^2 w(z_1))-w(z_2)/(1+t^2 w(z_2))]
       (chi_2-chi_1),

up to orientation, and is nonzero. Smoothing the corners preserves its sign and zero winding. This is a countertest to inferring unweighted winding from the weighted line integral, not a quotient field or Euler-profile construction. Additional dynamical identities might restrict actual trajectories, but none has been proved here to make that inference.

## 6. Scope and verification

Sections1-4 give the precise valid part of coordinator CO37 Section4. Section5 records the limit of its geometric interpretation. The complete coordinator note and inner answer were read; A641-A644 supply the independently checked flux inputs. All deductions above are analytic. There is no computation or formal build, and no claimed new nonexistence theorem. Existing configured model agent exchange is the model collaboration.

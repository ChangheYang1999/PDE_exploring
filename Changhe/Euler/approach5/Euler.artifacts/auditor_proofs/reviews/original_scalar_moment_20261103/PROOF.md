# Original scalar components and their signed pressure moment

Status: CONFIRMED A786-A789. Independent complete reconstruction of LIT179. The hypotheses include global zero helicity and natural derivative decay. No sign theorem for the pressure deficit is obtained.

## 1. Statement and fixed notation

Fix 2/5<c<1/2 and any finite real omega. Put p=(1-c)/c, a=1-2c, lambda=2(1-c)=a+1, eta=a/lambda, kappa=1+c, Jx=(-x2,x1,0), A=cI-omega J. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite constant C. Let Omega=curl U, B=Ax+U. Their complete flows are Gamma_s and Phi_t. Completeness follows respectively from bounded Omega and at most linear growth of B. Their divergence identities give Jacobians1 and exp(3ct).

Use the confirmed actual scattering diffeomorphism Xi:E=R3 minus K -> R3 minus{0}, where K is compact and null. It is C1 and volume preserving, with

    Xi Phi_t=exp(tA)Xi, W(Xi y)=D Xi(y)Omega(y).

Here V,W are the actual tails. Let Pinf be the canonical pressure limit and P2 its next coefficient. Define

    H=P-Pinf+|U|^2/2+(Ax).U, Q=P-Pinf-|U|^2/2,
    g=U.B=H-Q, k(z)=(Az).V(z), S(z)=P2(z)-|V(z)|^2/2.

Let K_Omega be the points of K whose complete Omega line lies in K, and O=R3 minus K_Omega. A736-A740 give a C1 scalar F on O extending S composed with Xi, with

    F(Phi_t y)=exp(-lambda t)F(y), F(Gamma_s y)=F(y).       (1)

O is open and invariant under both complete flows. There is also a unique C1 scalar L on O extending k composed with Xi, invariant under Gamma and satisfying L(Phi_t y)=exp(-at)L(y).

For any connected component C0 of {y in O:Omega(y)!=0,F(y)!=0}, there are a sign sigma, a number ell and bounded C2 functions h,q on(0,infinity) such that, for s=|F(y)|,

    H(y)=h(s), Q(y)=q(s), L(y)=ell s^eta,
    q=h-(s/eta)h',
    q(s)/s -> sigma, h(s)/s^eta -> ell as s->0,
    ell=eta integral_0^infinity q(s)s^(-eta-1)ds,
    h(s)=ell s^eta-a sigma s+o(s).                       (2)

The integral is absolutely convergent. If sigma ell<=0, Q takes both signs along every complete B orbit in C0. In particular this happens with ell=0 if the component contains the preimage of a tail point with W!=0,k=0,S!=0. Common zeros k=S=0 are not covered by this assertion.

## 2. A C1 rank lemma from recurrence

Let X be a complete C1 field on an open invariant subset M of R3. Suppose almost every point is recurrent for its time-one map and X has no nonconstant periodic orbit. For any two C1 first integrals f1,f2,

    grad f1 cross grad f2=0 wherever X!=0.                (3)

Suppose instead that independence holds at a point. It persists on an open flowbox. Its two-dimensional transversal maps by(f1,f2) with invertible derivative, because the common kernel of their differentials is exactly the X direction. The C1 inverse function theorem makes that transversal map injective after shrinking. Thus each fiber of(f1,f2) in the box is one flow segment.

Choose a recurrent point y in a smaller box. There are integers n_j->infinity with Gamma_(n_j)y->y. The values of both first integrals force each late return to be on y's single flow segment. Write it as Gamma_(t_j)y with t_j->0. Then Gamma_(n_j-t_j)y=y, a nonzero period, and X(y)!=0. This contradiction proves(3), without Sard's theorem or second derivatives of the first integrals.

For the application on C0, recurrence can be obtained directly from A736: the bounded finite-volume Gamma-invariant sets {|F|>1/m} exhaust {F!=0}. Poincare recurrence on each set gives topological recurrence almost everywhere, by a countable neighborhood basis. Restriction to the invariant open C0 preserves it. Absence of nonconstant periodic Omega lines is A014. Thus(3) applies to H,F and to L,F on C0. Global Omega recurrence from A413 would also suffice, but is unnecessary for this application.

## 3. Extending the leading scalar through core crossings

The exact Lamb identity gives

    grad H=-aU+B cross Omega, BH=-ag, Omega.H=0.           (4)

The original Q is also a Gamma first integral, by the helicity transport identity. The actual C1 tail limit A539 gives, locally uniformly for y in E,

    exp(at)H(Phi_t y)->k(Xi y).                           (5)

To check the moving argument, write z_t=exp(-tA)Phi_t y. On every compact subset of E, z_t tends to Xi y and stays in a compact annulus. In that annulus the rescaled H is

    (Az).u_t(z)+exp(-t)(p_t(z)+|u_t(z)|^2/2),

and the actual rescaled velocity and pressure converge. This gives(5); the factor exp(-t) comes from lambda-a=1.

The exact commutation relation is

    Phi_t Gamma_s=Gamma_(exp(kappa t)s)Phi_t.              (6)

If y and Gamma_s y both belong to E, invariance of H on the entire intervening original vortex line gives equality of H at their Phi_t images. Taking(5) proves equality of k composed with Xi at the two endpoints, even if the line segment crosses K.

For y in O choose s with Gamma_s y in E. On a neighborhood of y define L(x)=k(Xi(Gamma_s x)). This is C1. Two such local definitions agree by the endpoint equality, so they give one C1 function on O. They also show its Gamma invariance. Its Phi scaling follows from(6) and k(exp(tA)z)=exp(-at)k(z), using a possibly changed Gamma time to move the Phi image into E. Every point of O can be moved into E, so any invariant extension must have this value; uniqueness follows. No value of k at the excluded tail origin is assigned.

## 4. Connected scalar levels and the component normal form

Every component C0 in Section1 is invariant under both flows. O is invariant, F cannot change sign or vanish under(1), and Omega remains nonzero under its own flow and the Phi Cauchy law. A continuous orbit path therefore stays in its connected component.

Since BF=-lambda F, F has no critical point on C0. Set Sigma={y in C0:|F(y)|=1}. Each complete B orbit meets Sigma once, and

    (t,z) -> Phi_t z, from R times Sigma to C0

is a C1 diffeomorphism. Its inverse is t=-log|F(y)|/lambda and z=Phi_(-t)y. Sigma is nonempty. Connectedness of C0 and the product projection imply that Sigma is connected. Every other |F| level is its Phi translate and is connected as well.

Apply(3) to H,F. H is constant on each connected level, since its tangential derivative vanishes and a connected C1 manifold is path connected. Thus H=h(|F|). The same argument applied to L,F gives L=l(|F|); scaling of L immediately yields l(s)=ell s^eta.

The original H and Q are C2: momentum gives grad P in C1, hence P in C2. Both are bounded globally, because P tends to Pinf, U is bounded, and (Ax).U=O(|x|^(1-p)) tends to zero. Choose z0 in Sigma intersect E, which is possible because C0 is open and K is null, then normalize an E point by a Phi time. The formula

    h(s)=H(Phi_(-log s/lambda)z0)

makes h C2 and bounded on the entire half-line. Equations(1),(4) give g=(lambda/a)s h'(s), so Q=q(|F|) with q=h-(s/eta)h'. The same trajectory formula for Q makes q C2 and globally bounded. No uniform bound on their derivatives is asserted.

At z0, the actual next-pressure limit is exp(lambda t)Q(Phi_t z0)->F(z0)=sigma. Equation(5) gives exp(at)H(Phi_t z0)->L(z0)=ell. Setting s=exp(-lambda t) gives the two limits in(2).

## 5. Both endpoint terms in the signed moment

The scalar equation for q is equivalent to

    [h(s)s^(-eta)]'=-eta q(s)s^(-eta-1).                 (7)

Near zero, q(s)=sigma s+o(s), so the absolute integrand is O(s^(-eta)), integrable because0<eta<1. At infinity q is bounded, and s^(-eta-1) is integrable because eta>0. Thus the moment converges absolutely.

Integrate(7) between epsilon and R. Bounded h gives h(R)R^(-eta)->0; the lower endpoint tends to ell. These are exactly the two boundary terms needed for the moment in(2). No contribution is dropped.

Integration instead from zero to s gives

    h(s)=ell s^eta-eta s^eta integral_0^s q(r)r^(-eta-1)dr.

Using q(r)=sigma r+o(r) and eta/(1-eta)=a gives the last expansion in(2). This moment is the componentwise reparametrization of the already confirmed discounted Bernoulli identity A426, not a new independent conservation law.

## 6. Sign consequence and a scalar consistency test

For small s, sigma q(s)>0. If sigma ell<=0, the moment forbids sigma q from being nonnegative everywhere, since its integral would then be strictly positive. Therefore q takes both signs. Every complete B orbit in C0 parametrizes all s>0, so every such orbit encounters the sign change.

If W(z)!=0,k(z)=0,S(z)!=0, let y=Xi^(-1)z. The pushforward identity and invertibility of D Xi give Omega(y)!=0, while F(y)=S(z)!=0 and L(y)=k(z)=0. Its component has ell=0. Consequently L=0 on the whole component, Q changes sign on every B orbit, and H/F->-a, Q/F->1 at its small-s end.

These identities are consistent at the scalar level. For any a>0 and sigma=+1 or-1, put

    h_test(s)=-a sigma s/(1+s),
    q_test(s)=sigma s(1-a s)/(1+s)^2.

Then h_test'=-a sigma/(1+s)^2, so q_test=h_test-(s/eta)h_test'. Both functions are bounded, q_test/s->sigma and h_test/s^eta->0 at zero. The weighted product h_test s^(-eta) also tends to zero at infinity. Equation(7) therefore gives absolute signed moment zero. The sign changes exactly at s=1/a. No velocity, pressure Poisson solution or actual Euler profile is supplied by this test.

## 7. Scope and verification

This theorem is an exact necessary condition for the specified globally helicity-free derivative-controlled class, uniform in the sense of allowing every finite omega. It supplies neither those hypotheses from bare decay nor a sign bound for Q. A common node k=S=0 is outside its sign conclusion. Three-dimensional almost-everywhere core return does not imply return on that particular zero-level cone; no such inference occurs here.

The complete LIT179 source, the actual scalar extension proof A736-A740 and the earlier tail-limit and discounted-identity dependencies were compared. Every new step is written above. No computation is needed. Provider runtime remains independently unattested.

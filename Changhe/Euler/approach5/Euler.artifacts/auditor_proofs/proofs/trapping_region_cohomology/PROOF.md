# Periodic orbits detect closed forms near a regular hyperbolic attractor

## Exact statement

Let B be a C1 vector field on an open subset O of R3, with local flow Phi and reversed flow Psi_t=Phi_(-t). Let Lambda be a compact nonsingular, transitive, locally maximal hyperbolic set for Psi, with one-dimensional stable and unstable bundles. Let N be a compact neighbourhood of Lambda such that Psi_t(N) is contained in int N for every t>0, the forward Psi flow is defined on N, and Lambda is the intersection of these decreasing images.

Every closed C1 one-form zeta on int N whose integral on every periodic orbit in Lambda is zero is exact on int N. Consequently the real homology classes of those periodic orbits span H1(int N;R). No Euler equation is assumed here.

## Dependencies

We use the classical real-valued Livsic theorem for a C1 flow on a compact transitive locally maximal nonsingular hyperbolic set: a Holder observable with zero integrals on periodic orbits has a continuous transfer function. We need only continuity, not an assertion about its optimal Holder exponent. The precise C1-flow hypotheses appear in R. D. Laureano, “Livschitz Theorem in Suspension Flows and Markov Systems: Approach in Cohomology of Systems,” Symmetry 12 (2020), 338, Theorem1, printed page6. The actual manuscript is retained as in the team records at the agent root. Hyperbolic local product structure and stable/unstable contraction are the usual local statements, also read in Climenhaga, arXiv:2009.09260v1, Section2. This proof is conditional only on these standard dynamical theorems, not on a new Euler claim.

## Proof of exactness

Apply Livsic to f=zeta(B), restricted to Lambda. It is Lipschitz on this compact set. There is a continuous h such that h(Phi_t x)-h(x) is the integral of zeta along that orbit segment.

The entire strong unstable leaf for Psi of any point of Lambda lies in Lambda. Indeed its points converge to Lambda under Phi, hence eventually belong to N; applying Psi back shows membership in every Psi_t(N). If I is a compact arc of such a leaf with endpoints p,q, sweep I by Phi for time T. The integral of the closed form around the boundary of this swept rectangle vanishes. Thus

    integral_I zeta = integral_(Phi_T I) zeta
                     + integral_0^T [f(Phi_s p)-f(Phi_s q)] ds.

The second term equals h(q)-h(p)+h(Phi_T p)-h(Phi_T q). The image arc has length tending to zero, and h is uniformly continuous. Consequently integral_I zeta=h(q)-h(p). This identity also holds on any orbit segment in Lambda.

Local product structure gives, for sufficiently close x,y in Lambda, a short path pi(x,y) consisting of a Psi-unstable arc from x, a short orbit segment ending at z in Lambda, and a Psi-stable arc from z to y. Its total length is bounded by a modulus rho(d(x,y)) tending to zero. Only the last arc may leave Lambda. The integral on the first two arcs is h(z)-h(x).

Let sigma be any closed piecewise C1 curve in int N. Choose an OUTER radius R>0 so that every ball of radius4R about Lambda lies in int N. Then choose an INNER scale epsilon>0 with epsilon<R/10, 3epsilon inside the local-product range, and rho(3epsilon)<R/10. This order of choices is essential: rho(d)->0 does not imply rho(3r)<r.

For large T, Psi_T(N) lies in the epsilon-neighbourhood of Lambda. The loop Psi_T sigma is homotopic to sigma through Psi_s sigma. Subdivide it into arcs of diameter less than epsilon. For every subdivision vertex choose x_i in Lambda within epsilon, with the final vertex equal to the initial one. Consecutive x_i have distance at most3epsilon. Replace each original arc and its short endpoint connectors by pi(x_i,x_(i+1)). All the resulting quadrilaterals lie in fixed convex R-balls contained in int N. The product path loop Pi is therefore homotopic to sigma.

For every s>=0, Psi_s Pi remains in int N and is homotopic to Pi. Its stable arcs contract exponentially. Using the unstable-arc and orbit identities, its integral is

    sum_i [h(Psi_s z_i)-h(Psi_s x_(i+1))]
      + sum_i integral_(Psi_s stable_arc_i) zeta.

The finite first sum tends to zero by continuity, since z_i and x_(i+1) are on one stable leaf. The second tends to zero by contraction and the boundedness of zeta on a compact neighbourhood of Lambda. The integral is independent of s, hence is zero. Every loop period of zeta vanishes, so path integration gives a C2 primitive on every component of int N. This proves exactness.

If the periodic classes failed to span H1(int N;R), a nonzero linear functional on the quotient would, by the universal-coefficient and de Rham theorems, be represented by a smooth closed form with zero periodic periods and a nonzero loop period. Exactness rules this out.

## Euler pressure consequence

Let 0<c<1/2, omega be finite, A=cI-omega J, a=1-2c, and B,W be C1 with div B=3c, div W=0 and [B,W]=-(1+c)W. Set U=B-Ay and alpha=(B cross W).dy. Direct vector calculus gives d alpha=a i_W vol. Therefore delta=a U.dy-alpha is closed precisely when curl U=W. The Lamb form of the rotating equation is delta=-dH, where H=P+|U|^2/2+(Ay).U. On a periodic orbit, alpha(B)=0, so integral delta=a integral U.dy.

Under curl U=W on int N, the theorem proves that a single-valued C1 pressure exists there if and only if all periodic U-circulations vanish. A spanning finite family suffices when H1 is finite-dimensional. This is an equivalence, not a proof that either condition holds for a proposed field.

If N is a compact connected C1 three-dimensional submanifold with connected boundary, that boundary is a torus in this setting. B has no zero in N, because such a zero would belong to Lambda. For sufficiently small t>0, Psi_t has no fixed point in N, by the uniform local lower bound on nonstationary flow displacement. Its Lefschetz number is therefore zero; it is homotopic to the identity on N, so chi(N)=0. The boundary Euler characteristic is twice chi(N), and a connected orientable closed surface of Euler characteristic zero is a torus. Alexander duality and Mayer-Vietoris for N and its complementary side in S3 give H1(N;Z)=Z. The collar identifies H1(int N) with H1(N).

At least one periodic orbit has nonzero real homology class. Its single zero-circulation condition tests exactness of delta. The same is true of a closed curve C with nonzero real class and alpha tangent integral zero, in particular a curve tangent to ker alpha. Neither the existence of a convenient characteristic curve nor a circulation sign is supplied by this theorem.

## Scope and audit

This confirms Theory Agent C C25, Lemma5.8 and Proposition5.9, with the explicit two-scale repair above. No new obstruction beyond curl coupling and pressure periods is claimed. The interpretation about “only” a loop obstruction applies to this closed-form exactness problem; it does not exclude other analytic uses of Euler or conditions outside N.

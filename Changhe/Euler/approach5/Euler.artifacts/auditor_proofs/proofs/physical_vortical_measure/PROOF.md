# Physicality of an entropy-saturating vortical flow measure

## Statement and notation

Let U in C2(R3;R3) be a divergence-free rotating Euler profile with uniform sublinear growth, 0<c<1/2 and any real omega. Set B=(cI-omega J)y+U, Omega=curl U, a=1-2c and b=1+c. Let Phi be the B-flow. Suppose nu is a probability supported on a compact full-flow invariant set K, invariant and ergodic for the full flow, with

    nu({B!=0 and Omega!=0})=1,
    h_nu(Phi_-1)=a.

Then the continuous-time backward basin of nu has positive three-dimensional Lebesgue measure. A positive-volume part of that basin lies where Omega!=0. A basin means convergence of the empirical probabilities T^-1 integral_0^T delta_Phi_-t(x) dt to nu.

No time-one ergodicity, uniform hyperbolicity, basicness, or uniform nonvanishing over all of K is assumed.

## Contracting vorticity saturation

The Cauchy law D Phi_t Omega=e^(bt) Omega o Phi_t implies the flow conjugacy

    Phi_t psi_s(x)=psi_(e^(bt)s)(Phi_t x),

where psi is the Omega-flow. A048 proves its completeness. Only sufficiently short local psi intervals are needed here. Uniform sublinearity gives a common compact backward trap for any compact set of initial points. On a slightly enlarged trap Omega is bounded; therefore, for initial points in a sufficiently small compact neighborhood and uniformly small s,

    |Phi_-t psi_s(x)-Phi_-t(x)|<=C |s| e^(-bt), t>=0.

Both orbits remain in a compact set. Uniform continuity of any continuous test function then makes their empirical averages differ by a quantity tending to zero. Thus the continuous-time generic set G for nu is invariant under sufficiently short Omega-flow segments. It is also invariant under every fixed Phi time, since shifting an averaging interval only adds and removes bounded-length intervals.

## An unstable curve with positive generic length

Compactify B outside a neighborhood of K. The resulting compact C2 flow has unchanged dynamics and derivatives on K. The spectrum calculation A037 gives the backward exponents a,0,-b almost everywhere, with B and Omega spanning the zero and negative lines. The actual Ledrappier-Young Part I, Theorem A, applies to invariant probabilities without assuming time-one ergodicity or excluding zero exponents. The entropy equality implies that conditional probabilities on one-dimensional unstable leaves are absolutely continuous relative to leaf length.

Full-flow ergodicity gives nu(G)=1 by the continuous-time ergodic theorem. Choose one subordinate unstable atom carrying positive leaf length of points in K intersect G that are Oseledets regular and have nonzero B and Omega. Let x0 be a leaf density point in this full-measure set. An embedded C1 unstable curve gamma through x0 has tangent at x0 equal to the positive Oseledets line. Hence

    gamma'(z0), B(x0), Omega(x0)

are linearly independent. Shrink the curve and choose a measurable positive-length subset E of K intersect G in the shrunken curve. The fixed curve tangent and the two vector fields remain independent nearby by continuity. Taking E inside K ensures that its genericity concerns the original flow, independently of compactification.

## Positive ambient volume

For small parameters define

    T(s,tau,z)=psi_s(Phi_-tau(gamma(z))).

This is a C1 map. Its derivative at (0,0,z0) has columns Omega(x0), -B(x0), gamma'(z0), so it is nonsingular. On a sufficiently small product box the inverse function theorem gives a C1 diffeomorphism, with Jacobian bounded away from zero on a smaller closed box. The parameter set consisting of two intervals times gamma^-1(E) has positive three-dimensional measure; its image therefore has positive ambient measure.

Every image point is generic for nu, first by the fixed-flow-time invariance of G and then by its short Omega-flow invariance. Shrink the box once more so Omega is nonzero throughout the image. This proves both conclusions.

## Consequences and limits

The vortical maximizing measure in A065, whenever it exists with full vortical measure, is physical for the backward continuous-time flow. Combined with A089, every nonconstant real-analytic uniformly sublinear profile with 0<c<1/2 has such a physical maximizing measure and core entropy exactly 1-2c. This is a necessary consequence of hypothetical existence, not a contradiction.

The phase-fiber time-one measures in A064 are not full-flow invariant. Their generic sets are not invariant under arbitrary Phi times, so the saturation proof does not apply to them. The theorem also holds for an independent eigenfield satisfying the same transport and regularity hypotheses; its physicality conclusion alone does not use the Euler curl coupling.

Dependencies: A002, A006, A037, A048, the actual Ledrappier-Young Theorem A source audited in A065, and elementary disintegration, ergodic and inverse-function arguments. LIT20 is CONFIRMED.

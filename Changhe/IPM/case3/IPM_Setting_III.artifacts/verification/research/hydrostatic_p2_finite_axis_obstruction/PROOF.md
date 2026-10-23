# No exact c=2 transport in the finite polynomial axis ansatz

Result243. Written before verification code. This is an exclusion of a specified finite ansatz for an auxiliary axis equation. It is not a nonexistence theorem for full-plane IPM, nor a bound on how well increasing-degree approximations can perform.

## Statement and notation

Let C>0, let H and k be real polynomials with H(0)=k(0)=0 and H'(0) != 0. For 0<t<1 put w=1-t^2 and

    y=C t/w^2,    G(y)=y H(w),    V(y)=integral_0^y k(w(s)) ds.

The map t -> y is an increasing bijection from (0,1) to (0,infinity), since y_t=C(1+3t^2)/w^3>0. Then

    (2y+V) G_y = G

cannot hold for every y>0. In fact it cannot hold identically on any nonempty open subinterval. There is no assumption on the signs of G, G_y or k, or on the polynomial degrees. The nonzero H'(0) is the nonzero y^(1/2) far-field amplitude of this ansatz. H(1) need not be nonzero for this exclusion.

## Dependencies

The elementary primitive in result240, research/hydrostatic_p2_elementary_axis/PROOF.md, follows by substituting y=Ct/w^2 in dV=k(w)dy. Its only nonrational term is

    C (4 k_2-k_1) atanh(t),

where k_j is the coefficient of w^j and missing coefficients are zero. All other terms equal C[2 k_1 t/w + P(t)] for an odd polynomial P. A complete derivation of the only feature used here is included below. No numerical state or floating-point calculation is needed for the theorem.

## Proof

Write H(w)=w h(w), so h is a polynomial and h(0)=H'(0) != 0. Define

    F(t)=C t h(1-t^2),    D(t)=(1-t^2) F'(t)+2t F(t).

Then F is a nonzero odd polynomial. Its degree m is a positive odd integer, and F(1)=C h(0), F(-1)=-C h(0) are nonzero. In particular gcd(F,w)=1. Also

    G=F/w,    G_t=D/w^2,    G_y=D w/[C(1+3t^2)].

The leading coefficient of D is (2-m) times the leading coefficient of F. Since m is odd, it is nonzero and deg D=m+1. Moreover D(1)=2F(1) and D(-1)=-2F(-1) are nonzero. Thus gcd(D,w)=1.

Suppose the transport identity holds on a nonempty open interval. On a nonempty smaller interval D is nonzero, since D is a nonzero polynomial. Solving the identity for V gives

    V=C F(t)(1+3t^2)/(w^2 D(t)) - 2C t/w^2.             (1)

The right side is a rational function of t.

To compute V, use

    dV/dt = C sum_(j>=1) k_j (1+3t^2) w^(j-3).

The j=1 primitive is 2t/w-atanh(t); the j=2 primitive is 4atanh(t)-3t. For every j>=3, (1+3t^2)w^(j-3) is a polynomial with an odd polynomial primitive vanishing at zero. Therefore

    V=C[2 k_1 t/w + (4 k_2-k_1)atanh(t)+P(t)].         (2)

Equations (1) and (2) imply 4k_2-k_1=0. To justify this implication, if that coefficient were nonzero, atanh(t) would equal a rational function on an interval. Differentiating would give a rational function whose derivative equals 1/(1-t^2) as a rational identity. At t=1 the latter has a nonzero coefficient of (t-1)^(-1). The derivative of a rational function has zero coefficient of (t-1)^(-1): differentiate its finite Laurent principal part and its Taylor series term by term. This is a contradiction.

Consequently V has denominator dividing w and no other finite pole. Substitute (1). Since gcd(D,w)=1, the absence of a pole at every zero of D, with multiplicities, implies the polynomial divisibility

    D divides F(t)(1+3t^2).                            (3)

Equivalently one can multiply (1) by w^2D and use (2) without its logarithm; then the other terms are divisible by D.

Let J=gcd(D,F), with the gcd made monic, and let s be the number of distinct complex roots of F. Since gcd(F,w)=1,

    J=gcd(wF',F)=gcd(F',F),    deg J=m-s.

Divide (3) by J. The polynomials D/J and F/J are coprime, so D/J divides 1+3t^2. Its degree is

    deg(D/J)=(m+1)-(m-s)=s+1.

It follows that s<=1. But F(0)=0, so s>=1, hence s=1 and all roots of F are at zero. By factorization over the complex numbers, F(t)=A t^m for some A != 0. For this polynomial,

    D(t)=A t^(m-1)[m+(2-m)t^2].

The quadratic m+(2-m)t^2 must divide 1+3t^2. Both have degree two because m is a positive odd integer, so comparison of constant and quadratic coefficients gives

    2-m=3m,    m=1/2.

This contradicts m being a positive odd integer. Thus the transport identity is impossible. Every argument began with an arbitrary nonempty interval, proving the stronger local identity exclusion as well.

## Scope and numerical consequences

The hypotheses are satisfied by every resolved c=2 finite trial of results235,238 and242: their k and H are exact finite polynomials in w, and their recorded K=H'(0)sqrt(C) is nonzero. Exact coefficient checks will document this application separately. The theorem does not require a nonzero logarithmic coefficient: even after forcing 4k_2-k_1=0, the divisibility obstruction remains.

The theorem does not exclude an infinite series, another compactification, a nonpolynomial trace, or convergence of increasing-degree finite trials to an exact auxiliary solution. It gives no quantitative positive lower bound on residuals over varying degrees and does not assert that any fixed finite grid detects their nonzero residual. The full elliptic inverse is not the auxiliary axis inverse used here. Thus neither principal endpoint follows, and Setting III remains UNRESOLVED.

# Forced-Euler work sign and its rotating-profile consequence

## 1. Source, question and reading scope

The submission is LIT371, SHA256
`a761c0ddd7f7c6b884d8fce9f8c0b6f7f700a55024966f76493aa0a4a96bc22a`.
All nine source sections, thirty-five manual checks and the formal-source
note were read. The actual retained Chae manuscript,
arXiv:1306.5839v1, has SHA256
`558eaf7cd9350b850ec98870885c02d2be49e502fa73c3d7affb9a75a4a7e4d1`.
Its printed pages 1-6 were read in full through the retained text;
the retained images of pages 2 and 5 were visually inspected. This covers
the statement and complete proof of the forced-Euler theorem. It does
not cover the complete Navier-Stokes proof or constitute a fresh
reading of the appendix. Captures and exact references are in
in the team records.

The source concerns

    (v.grad)v=-grad p+Phi,  div v=0 in R^N, N>=2.

It assumes a single global sign of Phi.v and that Phi.v vanishes exactly
where v vanishes. Its printed integrability range is finite
q>3N/(N-1), with |v|^2+|p| in L^(q/2).
The abstract states C1 regularity; the theorem's C^k wording with k>=0
does not specify a weak meaning at k=0. This audit uses classical
v,p in C1 and continuous Phi, and makes no C0 assertion.

The stronger scalar theorem below is an independently checked extension,
not a statement attributed to Chae. No priority claim is made.

## 2. Scalar theorem with exact hypotheses

Let v in C1(R^N;R^N) be divergence-free, H in C1(R^N), and
D=v.grad H. Suppose either D>=0 everywhere or D<=0 everywhere.
Then D=0 everywhere under either of these alternatives:

1. v in L^q for some 1<=q<=N/(N-1), with no assumption on H at infinity;
2. v in L^q and integral |H|^(q/2)<infinity for some finite
   q>N/(N-1).

The constants in the cutoff estimates below may depend on N, q and the
chosen fixed cutoff. No q=infinity assertion is made. The scalar theorem
does not conclude v=0 without further structure.

## 3. Local chain rule and the zero level

Take 0<=chi<=1 smooth, equal to one on B1 and zero outside B2,
and chi_R(x)=chi(x/R). Let g(0)=0, with g locally Lipschitz on
[0,infinity), C1 and strictly increasing on (0,infinity). In the choices
below g'(s)>0 for every s>0.

The functions g(H_+) and g(H_-) are locally Lipschitz and their weak
gradients are, almost everywhere,

    grad g(H_+)=1_{H>0} g'(H) grad H,
    grad g(H_-)=-1_{H<0} g'(-H) grad H.

There is no jump term since g(0)=0. The possible ambiguity of the
one-dimensional derivative at zero is harmless: grad H=0 almost
everywhere on {H=0}. Indeed the subset of that level where grad H
is nonzero is covered by countably many C1 hypersurface patches by the
implicit-function theorem, and has Lebesgue measure zero.

Compact integration by parts, using div v=0, gives

    integral_{H>0} chi_R g'(H) D
      =-integral g(H_+) v.grad chi_R,
    -integral_{H<0} chi_R g'(-H) D
      =-integral g(H_-) v.grad chi_R.

If the two right sides tend to zero, the fixed sign of D and Fatou's
lemma imply g'(|H|)|D|=0 almost everywhere on {H!=0}.
Thus D=0 there by continuity. It vanishes on the interior of {H=0}
because grad H=0 there, and at its remaining points by continuity
from {H!=0}. No global integral of D was assumed in advance.

## 4. Small-q estimate

Choose g(s)=s/(1+s). This is bounded by one and has derivative
(1+s)^(-2)>0. Each boundary integral is bounded by

    C R^(-1) integral_{R<|x|<2R}|v|
      <= C R^(N(1-1/q)-1) ||v||_{L^q(R<|x|<2R)}.

For q=1 this is the direct integral bound. For q>1 it follows from
Holder's inequality. In the stated range the power of R is nonpositive,
and the annular Lq norm tends to zero. This includes q=N/(N-1).
Section 3 proves the first alternative without any norm of H.

## 5. Large-q estimate and fixed regularization

Put

    m=(qN-q-N)/(2N)>0.

For m>=1 take g(s)=s^m. For 0<m<1 fix any epsilon>0 and take

    g(s)=(s+epsilon)^m-epsilon^m.

The latter is locally Lipschitz at zero, has positive derivative, and
satisfies 0<=g(s)<=s^m by concavity and subadditivity of the power
function. No limit epsilon->0 is needed.

The three Holder exponents q/(2m), q and N are all greater than one,
and their reciprocal sum is

    2m/q+1/q+1/N=1.

Consequently each boundary integral is at most

    C R^(-1) (integral |H|^(q/2))^(2m/q)
      ||v||_{L^q(R<|x|<2R)} |B_(2R)\B_R|^(1/N)
    <= C (integral |H|^(q/2))^(2m/q)
      ||v||_{L^q(R<|x|<2R)} -> 0.

Holder is applied to |H|^m with exponent q/(2m)>1; no normed-space
argument for L^(q/2) is required when q/2<1. Section 3 now proves the
second alternative. The printed theorem corresponds to m>1; its
integration-by-parts estimate is inside absolute values, so omission
of a minus sign there is immaterial. Fatou also avoids needing a
monotone radial cutoff.

For forced Euler, H=p+|v|^2/2 gives D=Phi.v. Under the source's
strictness assumption D=0 implies v=0. Thus the source conclusion
extends, in this classical class, to every finite q>=1 with the stated
norms; for the small-q alternative the pressure norm can be omitted.

## 6. Exact rotating force and rigidity when its work is zero

Let U,P in C1 solve the full rotating equation, and set

    A=cI-omega J,  e=|U|^2/2,  H_s=P+e,
    Phi=-(1-c)U-(Ay).grad U-omega JU.

Then the equation is (U.grad)U=-grad P+Phi, and

    D=U.grad H_s=Phi.U=-2(1-c)e-(Ay).grad e.

The rotation term omega JU is perpendicular to U, but the rotation
inside Ay must be retained in the derivative term.

If 0<c<1 and D=0, consider the complete linear orbit
y(s)=exp(sA)y0. It obeys |y(s)|=exp(cs)|y0| and

    e(y(s))=exp(-2(1-c)s)e(y0).

As s tends to minus infinity, the orbit tends to zero and the left
side is bounded by continuity. The right side would diverge if
e(y0)>0. Hence U=0. No completeness assertion for the nonlinear
carrier and no condition at infinity is needed in this step.

The scalar theorem therefore gives a conditional profile exclusion for
every finite omega and 0<c<1, under one sign of D and either of
its two integrability alternatives. In the second alternative,
U in Lq and P-p0 in L^(q/2) for some constant p0 suffice.
Subtracting p0 does not change D. The general forced-Euler strictness
assumption is unnecessary for this special profile consequence.

## 7. Bounded Hb profiles and the precise energy remainder

Assume U,P in C1, U bounded, U(R.)->0 in distributions, and
0<c<1/2. This is the campaign's Hb class. The confirmed energy theorem
A052-A053, independently rechecked in A3053, gives zero below c=2/5,
finite energy at c=2/5, and, for a nonzero profile above c=2/5,

    E(r)=L r^beta+O(r^(beta-1)),  L>0,  beta=5-2/c in (0,1).

There is a separate exclusion here if D has one global sign, without
assuming the norms in Section 6.

Let M(r)=integral_{B_r}D. Integrate the exact formula for D in
Section 6. Since div Ay=3c and Ay.n=cr on the sphere,

    M(r)=(5c/2-1)E(r)-(cr/2)E'(r).

For c>2/5 put F(r)=r^(-beta)E(r). Since c beta/2=5c/2-1,

    F'(r)=-(2/c) M(r) r^(-beta-1).

This differentiates the exact energy, not an asymptotic error.
If continuous D has one sign and is nonzero, there are d>0 and r0
such that |M(r)|>=d for all r>=r0, with that same sign.
The displayed identity and F(r)->L imply, on integrating from R
to infinity,

    |F(R)-L|>=(2d/(c beta)) R^(-beta).

But the energy theorem gives |F(R)-L|<=C/R, impossible for
0<beta<1. Thus D=0 and Section 6 gives U=0.

At c=2/5 the identity becomes M(r)=-(cr/2)E'(r)<=0.
If D>=0 then M=0. If D<=0 and is nonzero, M<=-d for large r
would give E'(r)>=2d/(cr), contradicting finite total energy.
Again D=0. Below c=2/5 the energy theorem already gives zero.

Therefore any nonzero bounded Hb profile with 0<c<1/2 has both
strict signs of D. Uniform decay implies the bounded Hb hypotheses.
This does not assert either sign at arbitrarily large radii, and
E(r)~Lr^beta alone would not prove this argument.

## 8. Exact controls

To test general forcing strictness, take in R2 a nonzero smooth f
supported in (1/2,1), and define

    v(x)=f(|x|)(-x2,x1),
    p(r)=-integral_r^infinity s f(s)^2 ds,  Phi=0.

The field is divergence-free,
(v.grad)v=-f(r)^2 x and grad p=f(r)^2 x. Both v and p are
smooth and compactly supported, with p constant near the origin.
All the finite positive integrals in question exist, while D=0 and
v is nonzero. This satisfies the scalar conclusion and violates the
strictness required for the general forced-Euler conclusion.

To test removal of the norm hypotheses, for nonzero a in R3 let

    U=a,  P=-((1-c)a+omega Ja).y.

This is an exact smooth profile with
D=-(1-c)|a|^2<0 for 0<c<1. It is uniformly sublinear but not
decaying, not in any finite Lq, and not in Hb. Thus the forced-work
sign alone cannot imply zero in the uniformly sublinear class.
Neither example is a target counterexample.

## 9. Status and limitations

The source statement, scalar extension, controls and conditional
profile consequence have been reconstructed independently. The only
imported campaign theorem is the precise energy law in Section 7.
No numerical computation or formal build was needed.

The complete existing A123 comparison, in the team records,
was read, including all nine analytical items, W1-W3 and its change list.
It compared Sections 1-9 at pin 7be21b00 and found no gap. The zero-level
passage, fixed regularization, endpoint and integrated energy remainder
have also been checked directly above. Its stated symbolic diagnostic
and execution are not certified. Existing configured model file
collaboration is used; actual provider execution is independently
unattested. No novelty, global automatic work sign, unrestricted
rotating nonexistence, complete Navier-Stokes audit or C0 theorem is
claimed.

## 10. The comparison's flux refinements and overlap

For the full C1 equation, div U=0 and Section 6 give the exact
identity

    M(r)=integral_{|y|=r}(P+|U|^2/2) U.n.

An additive constant in P has zero flux. Thus M is the Bernoulli flux
in the report's Lemma 2.1; this section introduces no independent
pressure representation or new energy theorem.

For 2/5<c<1/2 under Section 7's hypotheses, integrate the exact F'
identity to obtain

    integral_R^infinity M(r) r^(-1-beta) dr
      =(c/2)(F(R)-L)=O(R^(-1)).

This is a convergent improper signed integral. Absolute convergence
is not asserted without a sign hypothesis. Dividing by the positive
weight mass R^(-beta)/beta gives a weighted signed average of size
O(R^(beta-1)). In particular, an eventual M>=d>0 or M<=-d<0 is
impossible, by the same lower bound as in Section 7. One global sign
of D supplies precisely this eventual bound unless D=0.

At c=2/5, M=-(cr/2)E'<=0 and finite energy gives

    integral_1^infinity |M(r)| dr/r
      =(c/2)(E(infinity)-E(1))<infinity.

These are A123's W1-W2, proved directly from the already imported
energy law. They are necessary conditions, not a proof that M or D
has a sign.

For W3, bounded U in Lq with q<=2 is in L2 because
|U|^2<=||U||_infinity^(2-q)|U|^q. In the bounded Hb class with
0<c<1/2 and c!=2/5, the established finite-energy exclusion therefore
already handles these norm alternatives. Section 7 handles the whole
bounded Hb class with a work sign; Section 6 also applies outside that
class and for 1/2<=c<1. This overlap does not weaken or extend any
hypothesis of the scalar theorem.

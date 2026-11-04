# A finite periodic stable family excludes a helicity-free attracting basin

Auditor verdict: A397, CONFIRMED at the exact conditional statement below. This removes the APPV measure input from the already confirmed B29 proof; the finite periodic stable-family hypothesis remains explicit.

## 1. Exact conditional statement

Let U be C2 and P be C1 on R3, with div U=0, solving the rotating Euler profile equation for 0<c<1/2 and any finite omega. Put

    A=cI-omega J, B=Ay+U, X=-B,
    W=curl U, a=1-2c, kappa=1+c,
    H=P+|U|2/2+(Ay).U, g=U.B, h=U.W.

Assume the flow Psi of X is complete. Let Lambda be a compact transitive attracting set with full open basin V. Suppose Lambda contains a point p0 with B(p0)=0 and W(p0)!=0. Suppose there are finitely many periodic orbits gamma_1,...,gamma_m in Lambda, with W nonzero on every one, such that the union D of their weak stable manifolds is dense in an open neighborhood N of Lambda inside V.

Then h cannot vanish identically on V.

Transitive means that some point of Lambda has a forward orbit dense in Lambda. A weak stable manifold of a periodic orbit is the union, over its phases q, of the global strong stable manifolds Wss(q). All these sets are understood for Psi. No physical probability, full support, basin coverage by probabilities, common period or mixing hypothesis appears in this statement. The profile's Lamb and vorticity identities imply

    a U+grad H=B cross W, XH=a g, WH=-a h,
    D Psi_t W=exp(-kappa t) W composed Psi_t.

They also imply H is C2, which is enough for the differentiations below.

## 2. The strong stable manifold of a periodic orbit is its vortex line

Let gamma be one of the stated periodic orbits, with period L, and q in gamma. The flow direction X(q) is a unit-multiplier vector for D Psi_L(q), and W(q) is an exp(-kappa L)-multiplier vector. They are independent. Liouville's determinant formula and div X=-3c give the third multiplier exp((kappa-3c)L)=exp(aL)>1. Thus gamma is hyperbolic, with its unique stable direction spanned by W.

The local commutation identity is

    Psi_t Gamma_s q=Gamma_(s exp(-kappa t)) Psi_t q.

Short vortex arcs through points of the compact orbit exist with uniform length in vortex time. The displayed identity shows that a sufficiently short arc contracts to the orbit at rate exp(-kappa t), uniformly for all t>=0. The local strong stable manifold theorem and its uniqueness identify this arc with a local strong stable plaque.

Pulling these plaques back by Psi_(-nL) both extends the vortex parameter to intervals of length proportional to exp(kappa nL) and exhausts the global strong stable manifold. Hence the vortex flow is complete on this leaf and

    Wss(q)=Gamma_R q.

No global completeness assertion for the vortex flow away from these leaves is needed here. Every such leaf lies in V. Therefore, if h=0 on V, the identity WH=-a h makes H constant on each Wss(q). For each periodic gamma_i of period L_i this yields

    H composed Psi_(L_i)=H on Ws(gamma_i).

## 3. A finite stable family supplies one period on the attractor

Let C_i be the closure of Ws(gamma_i) relative to V. It is invariant under Psi, and continuity extends the preceding period identity to C_i. Since the family is finite and D is dense near Lambda,

    Lambda is contained in the union of C_i.

Take a point x in Lambda with dense forward orbit. It belongs to some C_j; invariance and closedness then give Lambda contained in C_j. Consequently H composed Psi_L=H on Lambda, where L=L_j.

Apply this identity along the entire orbit of each point of Lambda and differentiate in its flow time. Since XH=a g and a>0, g composed Psi_L=g on Lambda. Define the continuous function

    Q(y)=integral_0^L |g(Psi_t y)|2 dt, y in Lambda.

Periodicity of g makes Q flow invariant on Lambda. Transitivity makes Q constant there. At p0 the orbit is stationary and g(p0)=0, so Q(p0)=0. Thus Q=0 on Lambda, and continuity of the integrand gives g=0 on Lambda. Now XH=0 on Lambda; transitivity makes H equal a single constant C throughout Lambda.

For each y in Ws(gamma_i), write y in Wss(q) for some q in gamma_i. Section2 gives H(y)=H(q)=C. Thus H=C on D.

The set D is dense in all of V, not just N. For any nonempty open O in V choose y in O and sufficiently large t so that Psi_t y lies in N. The open set Psi_t O meets N, hence meets D. Pulling the intersection back by the flow and invariance of D gives O intersect D nonempty. Continuity therefore gives H=C throughout V.

## 4. The actual Euler contradiction at the stagnation point

V is open and contains p0. Constancy of H and the Lamb identity at p0 give a U(p0)=0, hence U(p0)=0. Also h=0 on V, so Dh(p0)[W(p0)]=0. Differentiating h=U.W and using U(p0)=0 yields

    W(p0).DU(p0) W(p0)=0.

The vorticity law at B(p0)=0 gives DB(p0)W(p0)=kappa W(p0), hence

    DU(p0)W(p0)=W(p0)+omega J W(p0).

Skew symmetry of J makes the preceding scalar product |W(p0)|2, a contradiction.

The same local argument proves the B28 closure formulation: if H is constant on any nonempty open set E, no point p0 in its closure can satisfy B(p0)=0 and W(p0)!=0. Indeed grad H and Dh vanish on E and extend continuously to p0. This local observation has no decay or basin hypothesis. It is not a claim that an arbitrary helicity-free open set has constant H.

## 5. What remains external for B29

For the genuine C2 singular-hyperbolic transitive attracting set in B29, its explicit W!=0 throughout Lambda implies the nonvanishing conditions in Section1. AST Proposition2.10 and Remark2.11 give the finite periodic stable family. Once that source input is accepted, Sections2-4 prove the contradiction without APPV Theorems B-C, identification of the stable bundle on all of Lambda, or an almost-everywhere vortex saturation theorem.

The source check is the singular-attractor literature audit. Its interval-map step has an elementary reconstruction in LIT74. The return-map construction and stable lifting still rely on the precise source statement. No extension to a non-dominated singular set, a non-attracting statistical support, a zero of W on the support, or arbitrary sign-changing helicity is obtained.

Dependencies: the exact Euler Lamb and vorticity identities, elementary periodic-multiplier algebra, the local hyperbolic stable manifold theorem, and the stated finite-family density premise. No computation or formal verification is used.


## 6. Independent audit and dependency boundary

The complete submission, the existing A365-A366 proof and the exact finite-family source scope were reread. At each nonstationary periodic point, the flow direction is nonzero. It cannot be parallel to W: the same derivative would then give that vector both multipliers 1 and exp(-kappa L). The two independent invariant lines and the determinant fix the third multiplier, including its sign. Thus the local hyperbolic stable-manifold input is justified separately at every selected periodic orbit, with no need to identify a stable bundle on all of Lambda.

The finite union in Section3 is essential: the closure of a finite union is the union of its closures. Each relative closure is invariant under all finite flow times, because the full weak stable manifold is so and V is invariant. These facts justify the transitive-orbit step. The proof only transfers one period to H on Lambda, not a common period for the dynamics or for all points in V. The function Q is invariant because the already established scalar g is L-periodic on Lambda.

All pressure constants are harmless, and no integration over the unbounded basin is taken. Completeness is assumed for Psi; the only vortex completeness needed is proved on the chosen strong stable leaves. The statement does not require W to be nonzero at every other point of Lambda. For the application to the precise dominated singular-hyperbolic B29 class, A366's primary-source check supplies the finite-family premise from AST Proposition2.10 and Remark2.11. The one-dimensional reconstruction A386 alone does not supply the flow return map or stable lifting.

This is a dependency reduction and an exact broader conditional statement. It does not establish finite stable-family density for a non-dominated attractor, an arbitrary statistical support, or every helicity-free profile. No computation or formal build was used.

# From vortical Bernoulli constancy to global rigidity

## Statement and notation

Let 0<c<1/2, let omega be any finite real number, let J(y1,y2,y3)=(-y2,y1,0), and set A=cI-omega J. Suppose U is C2 on R3, P is C1, div U=0 and

    (1-c)U+(Ay+U).grad U+omega JU+grad P=0.

Write B=Ay+U, Omega=curl U, a=1-2c, q=|U|^2/2, H=P+q+(Ay).U and O={Omega!=0}.

1. Without a growth hypothesis, grad H=0 on O implies either Omega=0 everywhere or H is constant on R3.
2. If U=o(|y|) uniformly, the same hypothesis implies U is spatially constant. If U tends to zero, U=0.
3. It suffices in (1)-(2) that H be constant on each member of any family of open sets whose union covers almost every point of O. The constants need not be specified or equal in advance.
4. Under uniform sublinearity, grad H=0 on any dense subset of R3 implies U=0.

These are conditional results. No claim that the Bernoulli hypothesis follows from zero helicity or from basin existence is made.

## 1. Exact local identity and boundary values

The vector identities

    Omega cross U=(U.grad)U-grad q,
    Omega cross Ay=(Ay.grad)U-(DU)^T Ay,
    grad((Ay).U)=A^T U+(DU)^T Ay

and A^T=cI+omega J give

    a U+grad H=B cross Omega.                             (1)

Put Z=R3 minus O and D=int Z. Every point of Z minus D is in the boundary of O. If grad H vanishes on O, continuity makes it vanish on that boundary. There Omega=0, so (1) gives U=0. In particular U=0 on the boundary of D.

## 2. Arbitrary-boundary zero extension

For any open D and any globally C1 vector field F vanishing on its boundary, define V=F on D and V=0 outside D. On a fixed ball, let L bound DF on a larger convex ball. Two points in D satisfy the usual Lipschitz bound for F; two points outside have equal V. For one point inside and one outside, the line segment has a first exit z from D, and

    |V(x)-V(y)|=|F(x)-F(z)|<=L|x-z|<=L|x-y|.

Thus V is locally Lipschitz, even for an irregular boundary and disconnected D. Its weak derivative is

    DV=1_D DF almost everywhere.                         (2)

On D and the exterior of its closure this is immediate. On the boundary, V=0. A locally Lipschitz scalar function has derivative zero almost everywhere on its zero set: almost every zero is both a density point and a differentiability point; a nonzero derivative there would confine nearby zeros to arbitrarily thin slabs, contradicting density one. Applying this to every component proves (2), including boundaries of positive volume. Local Lipschitz regularity identifies these derivatives with the distributional ones.

Apply this with F=U and D=int Z. On D both div U and curl U vanish. Therefore div V=curl V=0 distributionally, so Delta V=0 distributionally. Weyl's lemma gives an entire harmonic V, equal to the continuous extension. If O is nonempty, V vanishes on that nonempty open set. Unique continuation for harmonic functions gives V=0. Hence U=0 on D and on all of Z. Equation (1) now gives grad H=0 on Z as well as O. Connectedness of R3 makes H constant. This proves (1), with no decay, boundary smoothness, or boundedness of D assumed.

## 3. The global constant-H implication

For completeness the A256 argument is included. If H is constant, dot (1) with B to obtain U.B=0. The identity H=P-q+U.B gives P=q+H. Subtract this constant from P, so P=q. Divergence and energy give respectively

    partial_i partial_j(U_i U_j)+Delta q=0,
    div(q B+q U)=(5c-2)q.                                 (3)

Let E(R)=integral_(|y|<R)|U|^2 and M_R=sup_(|y|=R)|U|. The sphere flux of (3), using (Jy).y=0, yields

    cR E'(R)-(5c-2)E(R)=-2 integral_(|y|=R)|U|^2 U.n,
    (cR-2M_R)E'(R)<=(5c-2)E(R).                           (4)

Uniform sublinearity makes the coefficient positive for large R. If c<2/5, positivity of E' forces E=0 there and hence globally. At c=2/5, E is bounded. For 2/5<c<1/2 choose 0<epsilon<min(c/2,1-2c); then M_R<=epsilon R for large R and

    E'(R)<=p E(R)/R, p=(5c-2)/(c-2epsilon)<1.

Thus E(R)=O(R^p). In the last two cases, the annular integral of |U|^2+q divided by R tends to zero.

Test the first equation of (3) against chi_R psi, where chi_R is a nonnegative smooth cutoff supported on B_(2R), equal to one on B_R, and psi=sqrt(1+|y|^2). Terms differentiating chi_R are bounded by C/R times that annular integral and vanish. The remaining term is

    integral chi_R [U^T D2psi U+q Delta psi].

It is nonnegative. The radial and tangential Hessian eigenvalues are (1+r^2)^(-3/2) and (1+r^2)^(-1/2), and Delta psi>0. Its integral on every fixed ball is bounded by the vanishing error, so U=0 on every ball. This proves the global constant-H implication without an assumed pressure normalization or discarded nonzero flux.

## 4. Irrotational alternative and coverage

If O is empty, U is entire harmonic componentwise. The interior gradient estimate on B_R(x) and uniform sublinearity give |DU(x)|<=C R^(-1) sup_(B_R(x))|U|->0. Thus U=v is constant. The exact pressure is

    P(y)=-[(1-c)v+omega Jv].y+P0.

This verifies that the word constant, rather than zero, is necessary under sublinearity alone: the vortical premise is then vacuous. Decay gives v=0. If O is nonempty, Sections 1-3 instead give U=0, a contradiction to nonemptiness. This proves (2).

For (3), if grad H were nonzero at a point of O, continuity would give a ball inside O, disjoint from every constant-H open set. Its positive volume contradicts the covering hypothesis. For (4), continuity extends zero gradient from the dense subset to all R3; Section 3 applies directly.

## 5. Scope and dependency audit

The extension step uses only local C1 regularity and div-curl coupling, with Weyl's lemma and harmonic unique continuation. The global step is exactly the pressure and energy argument independently checked in A256. No measure classification, basin invariance, common H limit, or regular boundary is needed. A single nondense constant-H basin does not meet these premises. The full decay conjecture remains open.

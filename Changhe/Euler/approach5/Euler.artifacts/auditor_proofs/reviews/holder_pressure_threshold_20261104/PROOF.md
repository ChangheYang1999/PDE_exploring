# Sharp pressure domination with a center Holder modulus

Status: CONFIRMED, A2735-A2737; applicability and unresolved optimization questions remain OPEN, A2738. Existing coordinator comparison is complete. This is a local kinematic Poisson theorem. It does not supply its pressure inequality for an Euler profile.

## 1. Exact statement and dependency

Let 0<alpha<=1 and 0<b<infinity. On the open ball B_b in R3 centered at zero, let V belong to C2(B_b;R3) and P to C1(B_b;R). Suppose

    div V=0, -Delta P=tr((DV)^2) in distributions,
    V(0)=0, DV(0)=0, P(0)=0.

Here tr((DV)^2)=sum_ij partial_i V_j partial_j V_i. It is not the squared Frobenius norm. Assume constants 0<=C<infinity and 0<r0<b such that

    norm(D2V(x)-D2V(0))<=C|x|^alpha, |x|<r0.

The norm is a fixed Euclidean tensor norm. Only this modulus at the center is required, not a uniform Holder bound between arbitrary points.

Let Gamma2 be the attained maximum of gamma over homogeneous quadratic divergence-free vector polynomials Q and homogeneous quartic scalar polynomials R satisfying

    <|Q|^2>=1, -Delta R=tr((DQ)^2), R>=gamma|Q|^2,
    0<=gamma<=1/4.

Brackets denote normalized unit-sphere averages. The already proved finite-dimensional lemma A2699 gives attainment and 0<Gamma2<1/4, with the complete argument in the team records Sections2-4. No value from a numerical optimization is used here.

Set gamma_alpha=max(Gamma2,1/(4+2alpha)). If gamma>gamma_alpha and

    P(x)>=gamma|V(x)|^2 for every x in B_b,

then V=P=0 throughout B_b. For every real gamma<=gamma_alpha there is a nonzero pair satisfying the regularity, differential, normalization and center-modulus hypotheses and this pressure inequality, with V locally C^(2,alpha) and P at least C1. Thus gamma_alpha is the exact threshold for this class, and the vanishing inequality must be strict.

At alpha=1, the threshold is max(Gamma2,1/6), with a center Lipschitz modulus for D2V and only C1 pressure. This weakens both regularity premises of the earlier C3/C4 theorem. It does not claim that P becomes C4.

## 2. The exact spherical stress identity

Write E=|V|^2 and T=V tensor V+P I. Incompressibility gives div div(V tensor V)=tr((DV)^2), so div div T=0 distributionally. T is C1 and div T is continuous. Mollify on a slightly smaller ball. The smooth divergence-free field div T_epsilon has zero flux through each fixed centered sphere. Uniform convergence of div T_epsilon there gives the same zero flux for div T. No singular source at the center or boundary term at infinity occurs.

For r>0 and n=x/r define

    e(r)=<E(rn)>, v(r)=<(V(rn).n)^2>,
    pbar(r)=<P(rn)>, A(r)=v(r)+pbar(r).

The field Tn is C1 away from zero. Its radial flux derivative gives

    <div(Tn)>=A'(r)+2A(r)/r.

On the other hand, differentiation of n gives

    div(Tn)=(div T).n+(tr T-n.Tn)/r.

Average this expression, use the zero flux above, and substitute tr T=E+3P. The result is

    r A'(r)=e(r)-3v(r).                              (1)

Since V=O(r^2), the right side divided by r is integrable near zero. Continuity and P(0)=0 give A(0)=0, hence

    A(r)=integral_0^r [e(s)-3v(s)] ds/s.              (2)

This is a whole-ball identity. It uses neither the stationary Euler equation nor a choice of harmonic pressure beyond the stated value and inequality.

## 3. Positivity forces quartic pointwise pressure growth

For this section it suffices that P>=0 near zero. Equation(2), V=O(r^2), and v>=0 imply

    0<=pbar(r)<=A(r)<=C1 r^4,
    integral_(B_r) P<=C2 r^7.                       (3)

Also DV=O(r), so the distribution Delta P=-tr((DV)^2) is a continuous function bounded in absolute value by C3|x|^2. For sufficiently small r, on B_(2r) it is at least -K r^2 with K independent of r. Therefore

    u_r(y)=P(y)+(K r^2/6)|y|^2

is distributionally subharmonic there. The factor1/6 uses Delta|y|^2=6 in R3. Mollification and uniform convergence of this continuous function prove the ordinary mean inequality on every compactly contained ball.

For x in B_r, average u_r over B_r(x), whose closure lies in B_(2r) when |x|<r. Nonnegativity of P lets us bound its integral by the centered integral on B_(2r), which is O(r^7) by(3). The quadratic correction contributes O(r^7) to the same integral. Dividing by the volume O(r^3) yields

    0<=P(x)<=u_r(x)<=C4 r^4.

Choose r=2|x| and treat x=0 by its normalized value. This proves

    0<=P(x)<=C5|x|^4                                (4)

near zero. The argument is pointwise despite using a centered integral bound. The positivity is essential to passing from the moving ball to the centered one.

## 4. Compactness of rescaled C1 pressures

Let Q(x)=D2V(0)[x,x]/2, and choose r_j decreasing to zero. On any fixed compact set,

    V_j(x)=r_j^(-2)V(r_j x) -> Q(x) in C2.

Indeed the second derivatives converge uniformly by continuity of D2V; the value and first derivative at zero vanish, so integrating gives the lower-derivative convergence. Define P_j(x)=r_j^(-4)P(r_j x). They are defined on expanding balls and satisfy

    0<=P_j(x)<=C5|x|^4,
    Delta P_j=f_j=-tr((DV_j)^2),
    f_j -> q=-tr((DQ)^2) locally uniformly.          (5)

The pressure bound and bounded sources imply local equicontinuity. Fix L>0 and take j large enough that B_(2L) is in the domain. Extend f_j from B_(2L) by zero, and set

    N_j(x)=integral_(B_(2L)) [-1/(4pi|x-y|)] f_j(y) dy.

The kernel has distributional Laplacian equal to the unit point mass. Its absolute value and first derivative are locally integrable in dimension three. Thus N_j has uniformly bounded values on B_(2L) and uniformly bounded first derivatives on a smaller ball, with constants depending on L but not j. For example the kernel integrals are bounded by constants times L^2 and L. These estimates also follow by smoothing the bounded source and passing to the potential; they require no second-derivative bound for N_j.

The difference h_j=P_j-N_j is distributionally harmonic on B_(2L). It is continuous and bounded there uniformly by(5) and the potential bound. Mollification gives its mean-value property, hence smooth harmonicity. The harmonic interior gradient estimate then bounds grad h_j on B_L. Consequently P_j is uniformly Lipschitz on B_L. Arzela-Ascoli on each fixed ball and a diagonal subsequence give a locally uniform limit R on R3.

Passing to distributions in(5) yields Delta R=q. Passing to the pressure inequality gives R>=gamma|Q|^2. Estimate(4) gives |R(x)|<=C5|x|^4 on all of R3. No uniqueness of this limit is asserted.

## 5. The limiting pressure is homogeneous quartic

The quadratic polynomial q has a homogeneous quartic particular solution

    R0(x)=|x|^2 q(x)/14-|x|^4 Delta q/280.           (6)

For a homogeneous quadratic in three dimensions,

    Delta(|x|^2 q)=14q+|x|^2 Delta q,
    Delta|x|^4=20|x|^2,

so Delta R0=q. The function h=R-R0 is entire harmonic with |h(x)|<=C6|x|^4. For any fixed point x0, the interior bound for a derivative of order five on a ball of radius L is at most

    C7 L^(-5)(|x0|+L)^4.

Letting L tend to infinity makes every fifth derivative zero. Therefore h is a polynomial of degree at most four. The bound at zero eliminates every term of degree below four in R. It follows that R is homogeneous quartic and

    div Q=0, -Delta R=tr((DQ)^2), R>=gamma|Q|^2.     (7)

This proves the low-regularity pressure-jet lemma. Its conclusion is the existence of a quartic limit, not a fourth-order Taylor expansion or C4 regularity of P.

## 6. Elimination of the quadratic velocity term

Assume gamma>gamma_alpha. It is positive, so Sections3-5 apply. If Q is nonzero, let m=<|Q|^2>>0. The homogeneous version of(1) gives

    <R>=(m-7<(Q.n)^2>)/4.

The inequality in(7) implies gamma m<=<R><=m/4, hence gamma<=1/4. The normalized pair Q/sqrt(m), R/m is then feasible in the definition of Gamma2 at coefficient gamma. This contradicts gamma>Gamma2. Therefore Q=0.

Now D2V(0)=0. Taylor's integral formula and the center Holder assumption give

    V(x)=integral_0^1 (1-t)D2V(tx)[x,x]dt,
    |V(x)|<=C|x|^(2+alpha)/[(alpha+1)(alpha+2)].     (8)

This uses only the displayed center modulus. It does not require D2V to be Holder between arbitrary nearby points.

## 7. Vanishing on the entire ball

Equations(2) and(8) give A(r)=O(r^(4+2alpha)) near zero. On the whole ball the pressure inequality gives

    A(r)>=gamma e(r)>=0,
    A'(r)=(e(r)-3v(r))/r<=A(r)/(gamma r).

Thus r^(-1/gamma)A(r) is nonnegative and nonincreasing for 0<r<b. Its limit at zero is zero, since gamma>1/(4+2alpha). For any fixed positive r, monotonicity bounds its value above by this zero limit. Hence A=e=0 at every radius. The continuous nonnegative function E has zero mean on each sphere, so V=0 throughout B_b. Finally P>=0 and pbar=A=0 give P=0 pointwise.

No analytic continuation or local-to-global unique continuation is used. The pointwise inequality on the whole ball is what lets the same differential inequality propagate the center conclusion to every radius.

## 8. Sharpness and Holder regularity of the examples

Put beta=2+alpha, rho=sqrt(x^2+y^2), and

    V=rho^(beta-1)(-y,x,0),
    E=rho^(2beta), P=E/(2beta).                     (9)

Set the fields to zero on the rotation axis. Their horizontal homogeneities are beta and 2beta. The second velocity derivatives are homogeneous of degree alpha and smooth in angle off the axis; their magnitude is O(rho^alpha), so V is C2 with V=DV=D2V=0 on the axis.

These second derivatives are locally alpha-Holder. Let their horizontal arguments have distance d and maximum radius R. If d>=R/2, their individual O(R^alpha) bounds give a difference O(d^alpha). If d<R/2, the joining segment stays at radius at least R/2. The third-derivative bound O(R^(alpha-1)) gives a difference at most C d R^(alpha-1)<=C d^alpha, since d<R and alpha<=1. Derivatives involving z vanish, and horizontal distance is at most full spatial distance. This proves the stated C^(2,alpha) regularity. For alpha=1 the velocity is the cubic polynomial rho^2(-y,x,0).

Direct differentiation away from the axis gives

    div V=0,
    (V.grad)V=-rho^(2beta-2)(x,y,0),
    grad P=rho^(2beta-2)(x,y,0),
    tr((DV)^2)=-2beta rho^(2beta-2),
    Delta P=2beta rho^(2beta-2).

The regularity extends these identities across the axis. Thus this is a stationary Euler pair and a kinematic Poisson pair with constant ratio P/E=1/(4+2alpha) wherever E>0.

If Gamma2<=1/(4+2alpha), this pair supplies every real gamma<=gamma_alpha. If Gamma2 is larger, an attained maximizing quadratic/quartic pair supplies every gamma<=gamma_alpha. Its D2V is constant, so it meets the center Holder assumption for every alpha. Equality of the two thresholds is already supplied by(9). These nonzero examples prove sharpness, including failure of vanishing at the exact threshold.

## 9. Checks against the actual similarity equation

For the explicit swirl(9), rotational equivariance gives D V Jx=JV and homogeneity gives D V x=beta V. Its stationary terms cancel. Therefore its complete rotating similarity residual is

    [1+c_l(beta-1)]V.

It is nonzero for every c_l>0 and every real omega. The field also grows at infinity. It is not a counterexample to the campaign conjecture. At the negative value c_l=-1/(beta-1) the residual does vanish; no assertion for all real c_l is made.

For any nonzero maximizing quadratic pair (Q,R), with this same quartic pressure R, the degree-two part of the residual is

    (1+c_l)Q+omega(JQ-DQ Jx).

Its sphere inner product with Q equals (1+c_l)<|Q|^2>. The JQ term is pointwise orthogonal to Q; the DQ Jx term integrates to zero because it is half the angular derivative of |Q|^2. For c_l>0 this inner product is nonzero. The other terms have degree three, so they cannot cancel a nonzero degree-two polynomial on an open ball. This proves failure of the full similarity equation at positive c_l for every omega without imposing symmetry on the maximizing pair. No stationary-Euler conclusion is assigned to that abstract pair.

## 10. Source scope and remaining work

All eight source sections of LIT323 at the pinned hash were read. The existing twelve-check log was read but not rerun; it is supplementary and proves neither compactness nor Holder regularity. The proof above is independent of numerical computation and of the sharper LIT320-LIT322 bounds for Gamma2.

Selected passages of the actual archived Hunter chapter were read: the mean-value theorem and converse, the Weyl remark, subharmonic mean inequality, first and higher harmonic derivative bounds, the explicit fundamental solution, and the complete smooth-source Newtonian-potential theorem and proof. Read ranges and the PDF hash are in the team records. The bounded-source potential argument in Section4 is derived from integrable kernels and the distributional fundamental solution, not attributed to Hunter's smooth-source theorem. The kernel used here is negative because its Laplacian is positive delta; Hunter's positive kernel is the fundamental solution for minus Delta. The prose sign and exponent slips near that source's kernel are not imported.

The existing configured model coordinator comparison is completed in Section11; the actual provider execution is independently unattested. No remote client, new agent, mathematical computation or formal build was used. The full-ball pressure bound for an actual decaying profile, the value of Gamma2, and whether Gamma2 exceeds1/6 remain OPEN. A cone, a sequence, or centered means alone is outside the present theorem. No general insufficiency claim about all such alternative hypotheses is inferred.


## 11. Existing coordinator comparison and its exact limits

All eight items of the coordinator comparison and wording points W1-W3 were read. The compared source hash is the pinned f1373591 version. The complete seventeen-check log was also read and not rerun. Its algebra agrees with the independent proof, but neither a random polynomial check nor an exact identity check supplies the analytic compactness argument.

The comparison agrees on every step: the continuous stress flux, positivity and moving-ball mean estimate, bounded-source pressure compactness, homogeneous quartic limit, normalized Gamma2 contradiction, center Holder remainder, whole-ball ODE and exact fractional swirls. At alpha=1 the new theorem contains the vanishing half of the older C3/C4 theorem and its sharpness examples. The strict threshold remains below1/4 for each alpha>0.

One phrase in comparison item5 and its log needs its natural limited reading: the power bound A=O(r^(4+2alpha)) guarantees a zero limit for r^(-1/gamma)A when gamma>1/(4+2alpha). It is the positivity of that exponent that is equivalent to the strict inequality. The actual weighted limit can also be zero below that coefficient for a particular A, for example A identically zero. No necessity of the power argument for an individual pair is used; sharpness comes separately from Section8.

W1 is respected explicitly in Section9: the degree argument uses the maximizing pair with its given quartic pressure. It does not consider a different pressure with a cubic homogeneous term. The nondecay of the velocity independently excludes a target profile. W2 concerns only the source's ancillary application remark: it should name the LIT309-LIT312 completions with pressure E/2-H and H/E tending to zero. This audit's theorem makes no application claim from that remark. W3 proposes keeping the older audited C3/C4 statement and adding the present result as a separate extension; that preserves both exact scopes.

There is no remaining disagreement about the local theorem. The derivative bound on the pressure is not strengthened to C4, no statement of constant ratio is transferred from these swirls to the different LIT321 example, and no missing full-profile pressure hypothesis is inferred.

## 12. W1-W2 source revision

The complete revision diff was read. It changes only the final scope paragraphs: the quadratic similarity argument explicitly keeps its displayed homogeneous quartic pressure, and the ancillary completion remark names LIT309-LIT312 with P=E/2-H and H/E tending to zero. These are exactly the restrictions of Sections9 and11. The theorem and its proof are unchanged. The original and revised source snapshots and their complete diff are retained in verification.

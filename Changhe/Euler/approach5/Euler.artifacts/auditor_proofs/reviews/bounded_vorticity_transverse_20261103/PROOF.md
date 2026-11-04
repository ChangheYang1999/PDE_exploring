# Bounded vorticity and the transverse gradient estimate

Status: the strict-exponent theorem and its stated corollaries are CONFIRMED. The extra pressure lemma below is independently proved and needs no Holder-growth assumption. No conclusion is asserted for the unrestricted campaign class.

## 1. Exact hypotheses and conclusions

Let J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J and L=(1-c)I+omega J, where0<c<1 and omega is any finite real number. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, LU+DU(Ax+U)+grad P=0.

Assume uniform U(x)->0 and |U(x)|<=CU(1+|x|)^(-a), with0<=a<=3/2. Put W=curl U. Suppose |W|<=W0 outside a ball and, for some beta in(0,1),0<=p<min(1+a,1/c),

    log(2+[W]_(beta,B(y,|y|/4)))<=KH |y|^p

for every sufficiently large y. Then DU is globally bounded. Confirmed A492,A476 imply DU->0 and |W|+||DU||<=C/(1+|y|). If1/3<c<1, confirmed A477 gives ||DU||<=C(1+|y|)^(-1/c).

In addition, under just the uniform decay, power bound and bounded exterior W assumptions, grad P->0. If a>0,

    |grad P(y)|<=C |y|^(-a) log(2+|y|)^2,

and hence grad P=O(r^(-a')) for each a'<a. This additional conclusion is proved in Section7 and does not assume the theorem's Holder-growth premise.

All constants are finite and can depend on the fixed c,omega,profile and displayed bounds, including compact regularity. No uniformity over omega is asserted. The source's projection V below is a transverse velocity and is unrelated to the scattering tail also denoted V elsewhere.

## 2. Canonical pressure and preliminary local bounds

Write G=DU, B=Ay+U, M=sup|U| and m(r)=sup_(|y|>=r)|U(y)|. Uniform decay makes M finite. By A757 Section2, whose complete proof was reread, the actual pressure gradient is canonical: its difference from the differentiated double-Riesz pressure is harmonic, and its radial means vanish by averaging actual momentum at radii tending to infinity. This uses only uniform velocity decay, not a derivative bound. In particular, for0<d<=1,

    |grad P(y)|<=Cd sup_(B(y,2d)) |tr G^2|+C m(r/2)^2/d+D(r),
    D(r)=C r^-4 integral_(|z|<=2r)|U(z)|^2 dz
          +C integral_(2r)^infinity m(s)^2 s^-2 ds.          (1)

Here r=|y| is large. Thus D(r)<=Cr^(-1-2a) if a<3/2, and D(r)<=Cr^-4 log(2+r) if a=3/2. Pressure constants do not appear.

Fix p+ strictly between p and min(1+a,1/c), with p+>0. If a>0 choose max(0,p+-1)<a'<a; if a=0 set a'=0. Then nu=min(1+a',1/c)>p+, r^a'(m(r/2)+r^-2)->0 and r^a'D(r)->0.

A cutoff chi supported in B(y,r/4), equal to one on B(y,r/8), gives U1=curl(Gamma*(chi W)), where Gamma=1/(4pi|x|). Since -Delta U=curl W, U-U1 is harmonic on the smaller ball. The bounds |U1|<=CW0 r and |U|<=M bound the harmonic gradient by C(W0+M/r). The derivative of U1 is a degree-minus-three mean-zero singular integral plus a local distributional term. Its homogeneous Holder bound is C[chi W]_beta. Splitting its size integral at eta and subtracting the value at the center gives

    |DU1|<=C[chi W]_beta eta^beta+CW0(1+log(r/eta)).

Choose eta=min(r/4,(1+[chi W]_beta)^(-1/beta)). The cutoff seminorm is bounded by the assumed W seminorm plus CW0r^-beta. Therefore, on B(y,r/16),

    |G|<=Cr^p+, [G]_beta<=exp(Cr^p+).                     (2)

A zero extension of the cutoff data has the same Holder bound up to a fixed constant, including pairs crossing its support boundary. This is a local construction, with no global derivative assumption.

## 3. Carrier frame and scalar transport

The carrier is complete: it is C1 and has at most linear growth. For S sufficiently large, B.y/|y| lies between cr-M and cr+M, so each exterior point reaches the sphere S at a finite backward time. Along the forward segment starting there,

    r(t)/r(s)<=3exp(c(t-s)),
    exp(c(t-t0))<=2r(t)/S.                                (3)

There is no radial contribution from the arbitrary rotation. On this exterior set put

    e=B/|B|, Pi=I-ee^T, T=Pi G Pi, g=Pi G^T e,
    h=Ge, sigma=W.e, q=U.e, V=U-qe.

Direct matrix algebra and momentum give

    G=T+e g^T+h e^T,
    W=g cross e+e cross h+sigma e,
    e.GW=W.h, tr G^2=tr T^2+2g.h+(e.h)^2,
    h=-(LU+grad P)/|B|, De=Pi(A+G)/|B|.                    (4)

Since PiW=g cross e+e cross h, |g|<=W0+|h|. Consequently

    |G|<=|T|+W0+2|h|,
    |tr G^2|<=|T|^2+2W0|h|+3|h|^2,
    |De|<=C(1+|T|+|h|)/r.                                (5)

The exact transverse identities are

    div V=-e.h-U.(De e)-q div e,
    curl V=e cross h+sigma e-((De)^T U) cross e-q curl e,
    Pi(DV)Pi=T-q Pi(De)Pi,
    div e=(2c-e.h)/|B|.

It follows that

    |div V|+|curl V|<=C(|h|+|sigma|)
                       +C|U|(1+|T|+|h|)/r,
    |T|<=|DV|+C|U|(1+|T|+|h|)/r.                         (6)

These formulas can also be checked in the oriented frame e=e3, where G has upper-left transverse block T, last column h and first two entries of its last row g. They require no integrability of a plane distribution.

The vorticity equation and D_Be=-omega Je+Pi h cancel the skew terms exactly and yield

    D_B sigma=-sigma+W.h+W.Pi h.                          (7)

If |h(z)|<=H*|z|^(-1-a') on S<=|z|<=R, integration along (3) gives

    |sigma(y)|<=C(1+H*)r^-nu log(2+r), S<=r<=R.            (8)

Indeed the sphere contribution is at most CW0(S/r)^(1/c). The source contribution is bounded by

    CH*r^(-1-a') integral_0^(t-t0)
                       exp(-(1-c(1+a'))u)du.

It has exponent1+a' below resonance, an additional logarithm at resonance, and exponent1/c above resonance. The constants in (8) may depend on the fixed S, which is harmless in the strict theorem.

## 4. Transverse inversion and the noncircular envelope

Cut off V in B(y,r/16), leaving it unchanged in B(y,r/32). Its divergence/curl data have supremum eps and Holder seminorm K. Formula (2), the algebraic expression

    DV=G-e(G^T e+(De)^T U)^T-qDe

and the product rule give K<=exp(Cr^p+). All other coefficient sizes and seminorms have polynomial growth; |B| is bounded below by a constant times r on the cutoff ball. Thus no unknown pressure or envelope seminorm has entered.

The compactly supported div-curl formula has a mean-zero degree-minus-three kernel. Splitting at eta, using the Holder difference inside and the supremum outside, gives

    |DV(y)|<=C[K eta^beta+eps(1+log(r/eta))].

Taking eta=min(1,r/64,(r^2(1+K))^(-1/beta)) proves

    |DV(y)|<=Cr^-2+Cr^p+ eps,
    eps<=sup_(B(y,r/16))(|div V|+|curl V|)+Cm(r/2)/r.       (9)

Define the finite increasing envelope

    Theta(R)=sup_(S<=|z|<=R)(|T(z)|+|z|^a'|grad P(z)|).

Equations (1),(2) with d=1 prove a prior polynomial bound Theta(R)<=CR^N, N=2p++2. Here a'<3/2<2, so this N suffices. The prior bound is proved before the iteration.

For S<=|z|<=2R, (4) implies |h(z)|<=C(1+Theta(2R))|z|^(-1-a'). Insert this in (8), then (6),(9), on every cutoff ball centered at r<=R. All points and all needed characteristic segments lie in S<=|z|<=2R. We obtain

    |T(y)|<=C+q1(r)(1+Theta(2R)),
    q1(r)=Cr^(p+-nu)log(2+r)+Cr^(-1-a)->0.                (10)

For pressure, (5) bounds its source on B(y,2) by C(1+Theta(2R))^2. Put mu=m(r/2)+r^-2 and d=mu/(1+Theta(2R)) in (1). For large r this lies in(0,1]. Both near and intermediate terms are at most Cmu(1+Theta(2R)); hence

    r^a'|grad P(y)|<=Cr^a'mu(1+Theta(2R))+r^a'D(r).       (11)

Every coefficient multiplying the envelope tends to zero. Separate the fixed inner annulus and choose its outer radius so large that the resulting q satisfies q2^N<1. Taking supremums gives

    Theta(R)<=C0+qTheta(2R).

Iterating n times leaves at most Cq^n(2^nR)^N, which tends to zero by the already established prior bound. Thus Theta is uniformly bounded. Now (4),(5) bound all of G; compact regularity finishes global boundedness. Only at this point are A492,A476 and A477 invoked. There is no circular use of derivative decay.

The selected a' initially suffices to close the iteration. Repeating the argument with any larger exponent still below a, or weakening such a bound, gives every a'<a claimed in the source. Section7 proves a stronger pressure statement independently.

## 5. Exact vorticity-gap corollaries

Let omega_inf=limsup_(|y|->infinity)|W(y)| and Gamma_a=min(c(1+a),1). If omega_inf<Gamma_a/2, choose positive W0 and gamma with

    omega_inf<W0<Gamma_a/2, 2W0<gamma<Gamma_a.

The confirmed C49 theorem gives the required Holder bound with p=gamma/c after choosing its alpha<1 sufficiently close to one. Thus the strict theorem applies and omega_inf=0. Consequently omega_inf belongs to {0} union[Gamma_a/2,infinity].

With confirmed C50 use cK W0<gamma<Gamma_a instead, where

    cK=(3/(4pi)) integral_(S2)|theta cross diag(1,-1,0)theta|,
    cK<1.77963978.

Its coefficient satisfies C_alpha<=cK+1-alpha, so the same alpha choice works. The gap becomes {0} union[Gamma_a/cK,infinity]. This uses the exact integral and its certified upper bound; the quadrature digits printed after cK in the source are not a certified decimal equality.

Under the campaign natural tail a=1/c-1 with2/5<c<1/2, Gamma_a=1. The two strict thresholds are1/2 and1/cK>0.5619. Under bare uniform decay a=0 they are c/2 and c/cK. No helicity premise is used. The conclusions are derivative decay, not profile nonexistence or smooth compact-core regularity.

For the associated physical solution, tau=T-t and |y|=tau^-c|x|. Orthogonal similarity rotations preserve the norms and

    tau sup_(|x|>=rho)|xi(x,t)|
       =sup_(|y|>=rho tau^-c)|W(y)|.

The left limit is omega_inf. If it is below1/2 in the natural-tail campaign class, the global natural derivative bound gives

    |grad u(x,t)|=tau^-1|DU(y)|
                 <=Ctau^-1|y|^-1/c=C|x|^-1/c.

This holds for every0<tau<=1 and |x|>=rho, with C independent of t. The sharper threshold1/cK is equally valid using C50.

## 6. A limited endpoint extension

The inner referee's endpoint proof was read in full and can be independently reconstructed as follows. Suppose1/c-1<a<=3/2, with the other hypotheses unchanged but Holder exponent p=1/c. Set p0=1/c and choose p0-1<a'<a, k=1+a'>p0. The local bounds (2),(9) hold with p0 exactly, since p0>0 absorbs the harmless logarithm.

Keep the sphere radius in (8) instead of combining both terms into one constant. On the envelope annulus, with X=1+Theta_S(2R),

    |sigma(y)|<=CW0 S^p0 r^-p0
                  +CX S^(p0-k)r^-p0.                    (12)

The first coefficient is independent of X. Constants multiplying the second term are independent of the later choice of S, once it is large enough for the uniform exterior estimates. The source integral and (3) directly give the displayed factor S^(p0-k).

Equations (6),(9) now yield

    |T(y)|<=C_S+CX[S^(p0-k)+r^(p0-k)
                            +r^(p0-1-a)+r^(-1-a)].

Pressure remains (11). First choose S to make CS^(p0-k) small, then choose the outer cutoff radius to make all remaining coefficients small compared with2^(-N). The same finite-envelope iteration proves bounded G.

This does not cover the natural equality a=1/c-1. In the campaign interval, the strict faster velocity decay in this endpoint extension already implies U=0 by the previously confirmed energy exclusion A053. The extension nevertheless refutes the universal wording that the initial-sphere term by itself forces p<1/c in every boundedness proof. It does not remove either natural-tail endpoint.

## 7. Independent pressure lemma under bounded vorticity

The exterior vorticity bound and compact C2 regularity give K=M+||W||infinity<infinity. Localize W on fixed unit balls and subtract its Biot-Savart field from U. The remainder is harmonic, bounded by C K on a smaller ball, and has gradient bounded by C K there. For the potential part, its degree-minus-two velocity kernel gives, for0<d<=1/8,

    |U(y+z)-U(y)|<=CK d log(e/d), |z|=d,                 (13)

uniformly in y. Indeed the union of radius2d balls about the two kernel centers contributes CKd; outside those balls the mean-value kernel difference is at most Cd|x|^-3, whose integral out to the fixed unit scale is Cd log(1/d). The harmonic part contributes CKd. This proves (13) without bounding DU.

In the canonical pressure gradient, the constant and the two linear increments vanish by div U=0. More precisely the distributional contraction of D3_ij Gamma with either Ui(y)Uj(y-z) or Uj(y)Ui(y-z) is zero, and its contraction with a constant is zero. With the stated positive Gamma convention this gives exactly

    grad P(y)=integral D3_ij Gamma(z)
                (Ui(y-z)-Ui(y))(Uj(y-z)-Uj(y)) dz.         (14)

The integral is absolutely convergent near zero by (13) and at infinity by bounded U. Formula (14) follows first with distributional cutoffs and then by passage to the limit: the local boundary error is O(K^2 d log(e/d)^2), tending to zero; the far boundary error tends to zero by boundedness. The derivatives of delta supported at zero in D3Gamma contribute zero because the quadratic increment and its first derivatives vanish there. This also justifies the pointwise identity at each C2 point.

Split (14) at a small d and at r/2. On |z|<d, (13) and |D3Gamma(z)|<=C|z|^-4 give CK^2 d log(e/d)^2. On d<|z|<r/2, both velocities are at exterior radii at least r/2, giving Cm(r/2)^2/d. On |z|>=r/2, the square increment is bounded by twice each squared velocity. The shifted-velocity term is controlled by D(r) from (1), and the center-velocity term by Cm(r/2)^2/r. Therefore

    |grad P(y)|<=CK^2d log(e/d)^2+Cm(r/2)^2/d
                     +D(r)+Cm(r/2)^2/r.                  (15)

Choose d=mu=m(r/2)+r^-2 for sufficiently large r. This yields

    |grad P(y)|<=Cmu log(e/mu)^2+D(r).                    (16)

Uniform decay makes the right side tend to zero, even with a=0. If0<a<=3/2 then mu<=Cr^-a. The function t log(e/t)^2 is increasing for sufficiently small t, so (16) is at most Cr^-a log(2+r)^2+D(r), proving Section1. Neither a Holder seminorm of W nor the theorem in Section4 was used.

## 8. Consequence for the transverse-strain remark

Under just the bounded-vorticity and decaying-velocity hypotheses, Section7 and momentum give h=o(1/r). The decomposition (4) satisfies

    lambda_max(sym G)<=lambda_max(sym T)+|g|/2+|h|,
    |g|<=W0+|h|.

Here g is perpendicular to e, so the symmetric part of e g^T has operator norm |g|/2. If DU fails to tend to zero, A506 supplies a sequence with lambda_max(sym G)>=1+c/2-o(1). Hence along that sequence

    lambda_max(sym T)>=1+c/2-W0/2-o(1).

This confirms the conclusion of source RemarkR4, but the decay of h needs the independent pressure argument in Section7; it does not follow merely from the algebraic bound (2.2) cited in that remark. This is a missing explanation supplied here, not an assumption of bounded DU.

## 9. Scope of the claimed obstructions

The strict theorem passes. The source's FS-TV1 correctly describes the loss in its particular combined bound but overstates what the initial sphere term requires in general; Section6 is the explicit exception. FS-TV2 identifies an uncanceled transverse term of size |U||T|/r. No assertion that every possible improved proof must contain the same obstruction is established.

The independent shell lower bound D1>=3/2 is audited separately. It applies to the defined angular shell-estimate class, not to all uses of the divergence-free equation and not to actual Euler profiles. The decimal optimal value near1.712 is not established. Neither the natural-tail endpoint nor the arbitrary-helicity campaign conjecture is settled here.

## 10. Verification and model collaboration

The complete original C51 source, its A36/A37 notes, A757's eight-section independent proof, the exact prior A492/A476/A477/A506 scopes and the complete inner endpoint proof were read. The inner full TV review is pinned as secondary evidence but was not fully read in this pass; no full-review claim is made for it. All arguments needed for the present conclusions are reconstructed above. Source hashes are in the team records. No numerical experiment is needed for these analytical estimates.

The source author is the existing configured model agent; runtime identity is not independently attested. The inner the external referee (a second model) review records a failed Bedrock credential retrieval and no model response. It is not an additional model consultation. Focused comparison of Sections6-8 is requested through the existing working files. No new agent or client is launched.

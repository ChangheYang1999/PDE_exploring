# Continuation with an L2 potential plus an inverse-radius term

Status: C70 scalar and carrier results CONFIRMED A2501-A2505 after the complete existing coordinator comparison. Broader consequences OPEN A2507. The scalar inverse-radius case is known; no novelty claim for the combined scalar statement is made. Full Euler nonexistence remains open.

## 1. Exact statements and dependencies

Write D_R={z in C:|z|<R}, partial_zbar=(partial_1+i partial_2)/2. Suppose f:D_R->C is smooth, every derivative of f at zero vanishes, and

    |partial_zbar f| <= (B+C0/|z|)|f| almost everywhere,       (1)

where B is measurable, nonnegative and in L2(D_R), and 0<=C0<infinity. Then f is identically zero on D_R. Neither the L2 norm nor C0 needs to be small.

For the carrier consequence fix 0<c<1/2 and any real omega. Let Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J and X(x)=Ax. On an open U in R3 avoiding zero suppose V is smooth and

    div V=0, X.V=0, DV X=-LV, W=curl V.                      (C)

Let sigma:D_R->U be smooth, with det(sigma_1,sigma_2,X(sigma)) nonzero. If V is flat at sigma(0) and

    |(W.X)(sigma(y))| <= [B2(y)+C0/|y|]|V(sigma(y))|          (2)

almost everywhere, with B2 nonnegative in L2(D_R), then V vanishes in a neighbourhood of sigma(0).

Section 5 states the full common-flat hypothesis F. Under F, each of its three section ratios Q has

    (Q-C0/|y|)_+ not in L2(D_r)                             (3)

for every C0>=0 and every centre disc D_r in the section. In particular ess sup_(D_r) |y|Q(y)=infinity. Here x_+=max(x,0), and the ratios are set to zero at the countable exceptional set. This is a necessary lower restriction; no upper bound or full-system contradiction follows.

Analytic dependencies already proved in the endpoint review A2469-A2471 are these: the Cauchy transform of a compactly supported L2 function is locally W12; for any finite exponent r its exponential has locally finite rth-power integral; exp(-s) belongs to W1q for 1<q<2 and obeys the weak chain rule. The bounded-coefficient Cauchy transform has the usual local W1p regularity for 1<p<infinity, as used in A2464 and A2467. We use elementary holomorphy and the exact carrier quotient A2463. No numerical check is a proof input.

## 2. Splitting the potential and a uniform logarithmic estimate

Define alpha=(partial_zbar f)/f where f is nonzero and alpha=0 otherwise. Assumption (1) implies partial_zbar f=alpha f almost everywhere, including the zero set, and |alpha|<=w=B+C0/|z|. On {w>0} put

    a1=alpha B/w, a2=alpha (C0/|z|)/w,

and set both to zero on {w=0} and at the immaterial centre. Then alpha=a1+a2, |a1|<=B and |a2|<=C0/|z|. Extend both by zero outside D_R and define

    s_j(z)=(1/pi) integral_(D_R) a_j(zeta)/(z-zeta) dA(zeta).

These are locally integrable distributions with partial_zbar s_j=a_j. The second integral is absolutely convergent at every z!=0. For rho=|z| in (0,R), estimate

    I(z)=integral_(D_R) [|zeta||zeta-z|]^-1 dA(zeta).

On {|zeta|<rho/2} the contribution is at most 2pi, and on {|zeta-z|<rho/2} it is at most 2pi. These discs are disjoint up to a null boundary. On the rest of {|zeta|<=2rho}, both denominators are at least rho/2, so the contribution is at most 16pi. If 2rho<R, the remaining annulus has |zeta-z|>=|zeta|/2, and contributes at most 4pi log(R/(2rho)); if 2rho>=R, it is empty. Thus

    I(z)<=20pi+4pi max(0,log(R/(2rho)))
        <=20pi+4pi log(R/rho),
    |s2(z)|<=20C0+4C0 log(R/|z|),
    exp(|s2(z)|)<=exp(20C0)(R/|z|)^(4C0).                    (4)

The positive part in the first line is necessary when rho>R/2. The final estimate is valid for the entire punctured disc. This is a direct integral estimate, not a numerical inference.

The endpoint theorem gives exp(-s1) in every finite Lr and in W1q for 1<q<2 on each relatively compact disc. Off zero, s2 is continuous and locally W1p for every 1<p<infinity. To check that last statement, separate a2 into a bounded part near a given compact annulus and an L1 part whose support has positive distance from that annulus. The first Cauchy transform has the bounded-coefficient regularity; the second is holomorphic there by differentiation under an absolutely convergent integral. Consequently exp(-s2) is locally bounded and obeys its W1p chain rule away from zero.

## 3. Holomorphic factor, removability and flatness

Fix a disc D' centred at zero with closure inside D_R. On any compact subset of D' minus zero, set

    F=exp(-s1)exp(-s2)f.

Choose 1<q<2 and then p,r large enough that 1/p+1/r<=1/q. The first factor is in W1q and Lr, while exp(-s2)f is locally bounded and W1p. The Sobolev product and chain rules therefore give F in W1q locally and

    partial_zbar F=exp(-s1-s2)[partial_zbar f-(a1+a2)f]=0.

The distributional Cauchy-Riemann lemma supplies a holomorphic representative of F on D' minus zero. Products and estimates below hold almost everywhere, which suffices for the integral argument; no continuity of s1 is asserted.

For every positive integer N, flatness supplies |f(z)|<=C_N|z|^N near zero. Equation (4) gives, on a fixed sufficiently small punctured disc,

    |F(z)|<=K_N |exp(-s1(z))| |z|^(N-4C0).                  (5)

Take an integer N>=4C0. Since exp(-s1) is L2 there, F is L2 near the puncture. A square-integrable holomorphic function on a punctured disc has a removable singularity: its Laurent series on an annulus has circle squared integral 2pi sum_k |c_k|^2 rho^(2k), by orthogonality. Integrating rho d rho and using nonnegativity shows that every coefficient with k<=-1 must vanish, since its radial integral diverges at zero. Hence F extends holomorphically to D'.

If that extension is nonzero, it has a finite order m>=0 at zero and can be written F=z^m G with |G|>=d>0 on a smaller disc D_(r0). For any 0<r<r0, choose an integer N>m+1+4C0. Formula (5) implies

    pi d^2 r^(2m+2)/(m+1)
       <= integral_(D_r) |F|^2
       <= K_N^2 r^(2N-8C0) integral_(D_(r0)) |exp(-s1)|^2.

The right exponent is strictly larger than 2m+2, which is impossible as r tends to zero. Thus F is zero on D'. Since s1+s2 is finite almost everywhere, f is zero almost everywhere there, and continuity makes it zero everywhere. The disc D' was arbitrary, so f vanishes on all D_R.

This proof handles any finite C0, not merely a small weak bound. It does not prove continuation for every arbitrary weak-L2 potential; the pointwise radial term in (1) is a specific additional class.

## 4. Exact transfer to every rotating carrier section

Restrict the section to a relatively compact disc. Put

    m=|X(sigma)|, beta_i=X(sigma).sigma_i/m^2,
    g_ij=sigma_i.sigma_j-m^2 beta_i beta_j,
    j=|det(sigma_1,sigma_2,X(sigma))|=m sqrt(det g).

The quotient metric g is smooth and positive definite. Write V(sigma)=sigma_i v_i-(beta.v)X(sigma), and theta=sigma^*(V.dx)=u_i dy_i, where u=gv. The exact equations A2463 are

    div(jv)=(3c-1)j beta.v,
    d theta=[epsilon j(W.X)/m^2+q2(v)]dy1 wedge dy2,

where epsilon is the fixed orientation and q2 is a smooth linear expression. In smooth isothermal coordinates z=phi(y) with phi(0)=0, write theta=alpha1 dz1+alpha2 dz2 and f=alpha1-i alpha2. The two equations imply

    |partial_zbar f| <= [C1+C2 B0(phi^-1(z))]|f|,             (6)

where B0 is any coefficient in |W.X|<=B0|V|. This pointwise estimate precedes and does not assume its coefficient's integrability. Smoothness and flatness of V transfer to f.

For B0=B2+C0/|y|, take a closed smaller y disc on which |D phi|<=M. The segment from zero to y lies in this disc, so |phi(y)|<=M|y|. Consequently

    C0/|phi^-1(z)|<=C0 M/|z|.

The remaining coefficient C1+C2 B2 composed with phi^-1 is L2 on a bounded z disc: change variables using the bounded determinant of D phi. Equation (6) therefore has the form (1). The scalar result makes f and V vanish on a section neighbourhood.

The carrier transport integrates exactly to

    V(exp(tA)x)=exp(-tL)V(x).

The inverse function theorem for (y,t)->exp(tA)sigma(y) supplies a finite local flowbox. Transporting the zero section in a sufficiently small time interval makes V zero near sigma(0). This requires no global flow completeness, pressure premise or boundary flux. The proof and its conclusion hold for every real omega.

## 5. Full common-flat consequences and the geometric radius

For precision, F consists of smooth V,S on a connected X-flowbox G avoiding zero, with central X orbit Gamma, the carrier equations C, and

    X.grad S=-bS, W.grad S=0, b=2(1-c),
    P=S+|V|^2/2, -Delta P=tr((DV)^2),
    S=0 on Gamma, S<0 on G minus Gamma,

with V and S flat at one point of Gamma. Put H=-S, eta=(1-2c)/b and n=(V cross X)/(|V||X|) where V is nonzero. The confirmed C66 conclusions say that V is flat exactly on Gamma, V and W have the same zeros, and off-Gamma zeros are locally isolated X-orbit segments. They also give

    |W.X|/|V|=eta |X||n.grad log H|

off the zero set. On a transverse section through a Gamma point define Q1=|W.X|/|V|, Q2=|W|/|V| and Q3=eta |X||n.grad log H|, all extended by zero at exceptional points. As checked in A2472, intersections with Gamma and off-Gamma zero orbits are countable and therefore null.

If Q1<=B2+C0/|y| on some centre disc with B2 in L2, the carrier result forces V to vanish on an open neighbourhood. That neighbourhood contains a point off Gamma where V is flat, contradicting C66. Thus no such bound exists. For Q2, first shrink the disc so |X(sigma)| is bounded, then use Q1<=|X(sigma)|Q2. For Q3 use its almost-everywhere equality to Q1. The assertion that no such B2 exists is exactly (3): one direction takes B2=(Q-C0/|y|)_+, and the other uses this positive part <=B2. Taking B2=0 gives the essential-supremum consequence.

There is an equivalent geometric radius on a sufficiently small section. Locally, the flowbox diffeomorphism and its inverse are bi-Lipschitz, and Gamma corresponds to y=0. Therefore dist(sigma(y),Gamma) is comparable to |y| after shrinking. If Gamma denotes a larger part of the same linear X orbit, no distant return invalidates this comparison: |exp(tA)x|=exp(ct)|x|, so points on that orbit close to a fixed nonzero x have t close to zero. Hence dist(sigma(y),Gamma)Qj(y) also has infinite essential supremum on every sufficiently small section disc. This is a statement about a single logarithmic-normal derivative component for Q3; no bound on the full gradient is assumed.

## 6. Submitted proof, source scope and remaining obstruction

All four sections of the submitted C70 source were read. Its splitting, exponent choices, puncture removal, coordinate transfer and full-F contradiction agree with this proof. Its submitted Step3 outer-annulus line needed the harmless positive-part qualification supplied in (4); the corrected source was compared word for word against the original, and the final displayed bound remains valid. Its off-zero W1p claims are used only for 1<p<infinity. The independent endpoint proof, including the exponential chain rule, is already confirmed A2469-A2471. This audit does not rely on the submitted numerical kernel evaluation or an unverified model answer.

The actual Pan-Zhang2023 manuscript was read in full for A2473. Its scalar Theorem4.3 includes the case B=0; its earlier Pan1992Lemma7 dependency remains unread. The argument above independently proves the smooth scalar case needed here and adds the L2 summand. No search has established whether that combined scalar condition is new in the literature, so it is not presented as a novelty claim.

A2482-A2484 supply pressure-free carrier fields for every omega with Q1 bounded above by C[1+(log log(1/|y|)+2)/|y|], smooth and flat along the central orbit but nonzero off it. Thus the inverse-radius bound in (2) cannot be replaced by that particular larger envelope. This comparison concerns C only. The universal integrating-factor obstruction does not rule out its field-dependent Volterra correction.

Nothing in F has been proved to bound Qj above by L2+C0/|y|. The failure of all such bounds is compatible with the carrier construction, but no scalar S or pressure completing that construction to F is provided. The common-flat obstruction, extension to arbitrary weak-L2 coefficients, actual-tail upgrades and the unrestricted smooth decaying Euler conjecture remain open.

The complete thirteen-item coordinator comparison was read and pinned, together with the corrected C70 source. It checks all six independent sections, including the product exponents, removability, radius transformation, zero-set extension and exact positive-part consequence. Its off-zero W1p observation is understood for 1<p<infinity. No mathematical gap remains in the exact claims above.

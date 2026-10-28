# Global coupling on the common weighted Holder space

## Statement

Let 0<alpha<1 and 4k<gamma<2, with the exact modal exponent k of proof 213. Use that topic's physical parity space

 Y=E2 intersect L2(w_gamma dX), w_gamma=(1+r^2)^(-gamma/2),
 ||h||Y=||h||infinity+[h]_x+[h]_(y,2)+||h||L2(w_gamma).

The seminorms and both parities are exactly those of proof 213. Let rho0 be the joined normalized modal trial and V=ell0 X+U[rho0]. Choose a smooth radial compact cutoff chi0 equal1 near0, and put H0=chi0 X.grad rho0/3. Define

 C_ren h=U[h].grad rho0+c[h]H0,
 T h=V.grad h-h,
 D_Y={h in Y:V.grad h belongs to Y distributionally},
 L_ren=T+C_ren on D_Y.

Then C_ren:Y->Y is bounded, and L_ren:D_Y->Y is closed, with D_Y its maximal distributional domain. No injectivity, surjectivity, dense-domain or inverse bound is asserted.

More precisely, for a fixed smooth radial chi equal1 on B1 and0 outside B2, put beta_R=1-chi(X/R). There are finite C and R0, depending on the background, cutoffs, alpha and gamma, such that

 ||beta_R U[h].grad rho0||Y
       <=C R^(k-1)(1+log R)||h||Y, R>=R0.             (1)

Thus the output tail of the coupling is small in operator norm. This is not compactness of the full coupling.

On S=C_c^infinity intersect E2, with both parities and the condition h(0,y)=0, define J(h)=partial_x^2 partial_y h(0)/2. There are k_epsilon in S intersect ker c with

 J(k_epsilon)=1,
 ||k_epsilon||Y+||L_ren k_epsilon||Y->0.              (2)

Consequently J is not closable in this actual global graph, even after restricting to c=0. The same explicit packets have the identical input and image for the full normalized moving-tail linearization, because its scalar variation is zero when c[h]=0. This statement concerns the graph on those packets, not a claim that the entire moving-tail operator has already been realized on Y.

All constants are qualitative. The proof supplies a global closed linear realization and a small far-output coupling, but no global inverse or nonlinear closure.

## Directional velocity bounds

We first prove three estimates for the canonical velocity of every h in E2, with M=||h||E2:

 [U1[h]]_x+[U2[h]]_x<=C_alpha M,
 |U[h](X)|<=C_alpha M(1+log(2+|X|)),                 (3)
 ||U1[h]/x||infinity<=C_alpha M,
 [U1[h](x,.)/x]_alpha<=C_alpha M(1+|x|),
 [U2[h](x,.)]_alpha<=C_alpha M(1+x^2).              (4)

The quotient is extended continuously across x=0. These estimates assert neither a bound for h_x nor a neighborhood bound for partial_x U1. The local estimates of proof 199 alone do not imply (3)-(4) at large x; the global band argument below is needed.

Start with compactly supported inputs. Partial Fourier transform in x, with frequency xi, gives the y convolution kernels of the two velocity components, up to harmless signs and factors i,

 (|xi|/2)exp(-|xi||y|),
 (xi/2)sign(y)exp(-|xi||y|).

After a smooth xi localization to |xi| comparable to N, both resulting full two-dimensional kernels have L1 norms bounded uniformly in N. Indeed, scale x,y by N. On the fixed xi annulus, repeated integration by parts in xi gives decay (1+|x|)^(-L); each differentiated exponential introduces a polynomial in |y| times exp(-c|y|), still integrable. The jump sign(y) does not enter the xi integration by parts. An x derivative of the localized kernel costs CN.

For xi bands N>=1, the input bound [h]_x<=M and the cancellation of the band kernel give velocity band supremum at most CM N^(-alpha). For N<1 use ||h||infinity<=M. The difference of the latter band's values at x and x+d is at most CM min(1,N|d|). Sum the high bands by splitting at N=1/|d|. For |d|<=1, this gives CM|d|^alpha; the low bands give CM|d|. For |d|>=1, the low-band sum is at most CM(1+log |d|), and the high sum is bounded by CM. Since 1+log d<=C_alpha d^alpha for d>=1, the first line of(3) follows. For a compact input, the low-x-frequency velocity tends uniformly to0: its multiplier has L2 norm O(N) in the slab |xi|<=N, and Cauchy-Schwarz bounds its convolution by CN||h||2. This justifies reconstruction and removes any polynomial ambiguity in the difference calculation.

The local Euclidean alpha seminorm of h on a unit disk about X is at most CM(1+|X|^2), by the horizontal-then-vertical comparison of proof 213. In the canonical singular integral, split the neighborhood of X at radius epsilon=(1+|X|^2)^(-1/alpha). Circular cancellation and that local Holder bound bound the integral inside epsilon by CM. Between epsilon and a radius comparable to 1+|X| use boundedness of h and integrate the degree-minus-two kernel, obtaining CM(1+log(2+|X|)). The canonical subtraction outside |Y|=1 contributes the same logarithmic bound up to radius 2(1+|X|). Beyond that radius, the kernel difference is bounded by C|X||Y|^(-3), whose integral is bounded by CM. The local multiplier term is bounded by CM. This proves the second line of(3), uniformly in the support of h.

For(4), localize instead in y frequency eta, with N=2^j. At N>=1 the weighted y seminorm gives

 ||h_j(x,.)||infinity<=CM x^2 N^(-alpha).

The exact partial-Fourier formulas are

 U2=-I+eta^2(-partial_x^2+eta^2)^(-1),
 U1=-i eta partial_x(-partial_x^2+eta^2)^(-1).

The signs of the second formula do not affect these bounds. Their band kernels have y-integrated absolute values bounded respectively by CN exp(-cN|x-x'|), plus the identity term, and by the same expression with a different constant. Kernel moments of x'^2 give

 ||U2[h_j](x,.)||infinity
        <=CM N^(-alpha)(x^2+N^(-2)).                 (5)

For U1/x, integrate its x derivative from0 to x when N|x|<=1. The exact derivative consists of an i eta h_j term and an i eta times the same convolution. Parity gives U1[h_j](0,y)=0. Thus

 ||U1[h_j](x,.)/x||infinity<=CM N^(-1-alpha),
                                             N|x|<=1. (6)

When N|x|>=1, divide the direct kernel bound by |x|. Also use the unweighted input supremum and the L1 band kernel bound. Combining the two gives

 ||U1[h_j](x,.)/x||infinity
        <=CM min(|x|N^(-alpha),1/|x|),
                                             N|x|>=1. (7)

Each quotient remains band limited in y. Equations(6)-(7) imply that the high-frequency sum has y alpha seminorm at most CM(1+|x|), by the elementary dyadic reconstruction used in proof 199. For the supremum, if |x|<=1, sum(6) through N=1/|x| and sum(7) above that scale, obtaining a uniform CM bound. If |x|>=1, split(7) at N=|x|^(2/alpha). The part below that scale is at most CM(1+log |x|)/|x| and the part above is at most CM/|x|. Both are uniformly bounded for |x|>=1.

For N<1 use only boundedness of h. The derivative-in-x kernel bound is CNM, so oddness in x gives ||U1[h_j]/x||infinity<=CMN. Its y derivative is bounded by CMN^2. Both low sums converge, with bounded supremum and alpha seminorm. The missing eta=0 part of the quotient is zero: the derivative-in-x multiplier contains a factor eta, and the sum of its low-band L1 kernel norms below epsilon is at most Cepsilon. Its quotient, fixed by oddness at x=0, therefore tends uniformly to0. This proves both U1/x estimates, including its continuous extension to0. Continuity follows by summing uniformly the continuous band quotients, using(6) near x=0.

For U2, (5) gives high-band amplitude CM(1+x^2)N^(-alpha), hence the stated high-frequency Holder seminorm. At N<1 the amplitude is CM and its y differences have bound CM min(1,N|d|). Their sum is bounded by C_alpha M|d|^alpha, by the same two ranges used in(3). Any eta=0 term is independent of y and drops out of this difference. For a compact input one may also check the reconstruction directly from -h_low plus the convolution term: h_low tends to0 pointwise uniformly in y on each fixed x line, and the convolution multiplier's L2 norm is O(epsilon). This completes(4).

The same estimates apply to general E2 inputs by fixed radial truncations chi(X/R)h, R>=1. These truncations have E2 norms at most CM uniformly in R. The only weighted-cutoff term uses |h(x,y)|/x^2<=M|y|^alpha and splits |y-y'| at R; its factors R^alpha and R^(-alpha) cancel. The canonical velocities converge locally in distributions, and pointwise after the local singular cancellation, because their far-subtracted kernels are integrable against bounded h. Bounds(3)-(4) pass to the limit by their difference quotients. For inputs in Y the weighted L2 convergence argument in the next section gives the same identification. No density in the large Holder norm is assumed.

## The weighted L2 velocity

For -2<gamma<2 the full-plane IPM multipliers are bounded on L2(w_gamma). Here is a direct proof for this particular weight. Split space into A0={r<2} and Aj={2^j<=r<2^(j+1)}, j>=1. On Aj the weight is comparable to 2^(-gamma j), with the same convention at j=0.

For input/output annuli with |j-l|<=2, use the unweighted L2 multiplier bound on the sum of the finitely many neighboring input annuli. The weights are comparable by a fixed factor and the overlaps are finite, giving a bounded near-diagonal contribution.

For l>=j+3, the nonlocal kernel is at most C2^(-2l). Cauchy-Schwarz in the input annulus gives an L1 bound C2^((1+gamma/2)l)||h_l||L2(w_gamma); the weighted square root of output area is C2^((1-gamma/2)j). Hence the block norm is at most

 C2^(-(1-gamma/2)(l-j)).                              (8)

For j>=l+3 the same calculation gives

 C2^(-(1+gamma/2)(j-l)).                              (9)

Both geometric sequences are summable exactly for -2<gamma<2. Applying the discrete convolution inequality to the sequence of input annular L2 norms proves the weighted bound. The local multiplier term is already in the near-diagonal part. One can prove the sequence inequality directly by Cauchy-Schwarz with the summable geometric coefficients, followed by interchanging the two finite or positive sums.

Compact truncations are dense in weighted L2 and define the bounded extension. For Y inputs they preserve the parities and their canonical far-subtraction constant vanishes. The far integral of the un-subtracted kernel is absolutely convergent by Cauchy-Schwarz, since integral_(r>1)r^(-4)w_gamma^(-1)dX is finite for gamma<2. Thus the extension equals the canonical velocity, not an inverse with an added harmonic field.

## Products with the actual modal coefficients

Near0, proof 203 proves U[h].grad rho0 bounded E2->E2 after a fixed sufficiently small cutoff; its hypotheses are met by the actual C4,1 modal density. Outside a fixed smaller disk write

 rho0_x=x a1, rho0_y=x^2 a2.

The finite angular formulas give smooth division across x=0 on punctured annuli. The compact radial joins are at least C5 for these coefficients, which is more than the one derivative used here. Their far estimates are

 |a1|<=Cr^(k-2), |partial_y a1|<=Cr^(k-3),
 |a2|<=Cr^(k-3), |partial_y a2|<=Cr^(k-4),
 |grad rho0|<=Cr^(k-1), |partial_x grad rho0|<=Cr^(k-2). (10)

They follow by differentiated division of the exact outer finite modes, and are weaker than the faster subleading powers. In particular all relevant compact-annulus bounds are finite.

The divided coupling is

 U[h].grad rho0/x^2=a1(U1[h]/x)+a2 U2[h].            (11)

For vertical differences of size at most1, use the product difference, (4), and the coefficient derivative bounds. The undifferentiated-coefficient terms are bounded by

 C M {r^(k-2)(1+|x|)+r^(k-3)(1+x^2)}|d|^alpha,

which is uniformly bounded on the outer region because |x|<=r and k<1. The coefficient-difference terms use ||U1/x||infinity<=CM and |U2|<=CM(1+log(2+r)); they are also bounded by CM|d|^alpha. The two radii in a difference of size at most1 are comparable outside a fixed disk. On the intervening compact annulus use its finite coefficient bounds. For differences of size at least1, the supremum of(11) is bounded by (3),(4),(10), giving the same conclusion. This proves the weighted y seminorm of the outer coupling.

For its x seminorm use the global bound [U]_x<=CM from(3), the bounded gradient coefficient, and its x derivative times the logarithmic velocity growth. For differences of size at most1 the derivative estimate suffices; for larger differences use the bounded supremum of U.grad rho0. The latter follows from r^(k-1)(1+log r)->0. All cutoffs add only bounded smooth multiplier terms. Thus the complete unnormalized coupling is bounded E2->E2 globally.

Apply the same estimates with beta_R in each coefficient. On the outer support the derivative of beta_R costs C/R, and (10) retains its stated powers. The supremum and the x seminorm are at most CM R^(k-1)(1+log R). In the weighted y seminorm, the small-difference terms are at most CM R^(k-1), plus smaller logarithmic terms from the coefficient derivatives. Large differences use the supremum of the divided coupling, at most CM R^(k-2)(1+log R). This proves (1) for its E2 part, for all sufficiently large R.

For the weighted L2 part, the preceding multiplier theorem and (10) give

 ||beta_R U[h].grad rho0||L2(w_gamma)
       <=C R^(k-1)||U[h]||L2(w_gamma)
       <=C_gamma R^(k-1)||h||L2(w_gamma).

The full coupling bound uses the finite global supremum of grad rho0. Finally c is bounded on E2 by4/pi, and H0 is in Y by its compact support and the Taylor division of proof 200. Adding this bounded rank-one column proves the claim for C_ren. For large R its output tail vanishes identically, so (1) is unchanged.

## Closedness and the actual global normalization packets

The norm of Y controls local uniform convergence. If h_n tends to h in Y and V.grad h_n tends to f in Y, then both limits hold in distributions, and multiplication by the C1 actual transport coefficients gives V.grad h=f. Thus maximal transport is closed. Subtracting I and adding the bounded operator C_ren preserve closedness and the maximal domain. There is no assertion that compact smooth functions are dense in the large Holder graph; proof 211 explicitly rules out such a general inference.

Let chi_epsilon=chi(X/epsilon) be a fixed smooth radial cutoff equal1 near0 and set h_epsilon=x^2y chi_epsilon. Exact scaling gives J(h_epsilon)=1, ||h_epsilon||E2=O(epsilon^(1-alpha)) and ||h_epsilon||L2(w_gamma)=O(epsilon^4). Near0 the actual field is V=(-A0 x,D0 y)+O(r^3), with C2 divided coefficients, so differentiating this compact packet gives

 ||T h_epsilon||E2=O(epsilon^(1-alpha)),
 ||T h_epsilon||L2(w_gamma)=O(epsilon^4).

These are the local scaling estimates checked in proof 204, now for the actual global field: the input is supported where that actual field agrees with the local one, and its transport image has the same compact support. The newly proved global coupling bound checks the noncompact image in Y and makes it tend to0.

The exact strain scales as c[h_epsilon]=epsilon^2 c[H], H=x^2y chi(X). Choose a fixed smooth annular q in S with J(q)=0,c[q]=1, as constructed in proof 204. Its actual global transport image is compact in Y, and its full coupling image is in Y by the boundedness just proved. Put

 k_epsilon=h_epsilon-epsilon^2 c[H]q.

Then k_epsilon belongs to D_Y intersect S, has J=1 and c=0, and satisfies(2). Hence (0,1) is in the closure of the graph of J on S intersect ker c, proving nonclosability. On these exact zero-strain packets the local column and the scalar moving-tail variation both vanish, so the full normalized linearization has image L_fix k_epsilon=L_ren k_epsilon. The same normalization failure therefore persists whenever the graph of that full operator is measured with these Y input and output norms and contains the displayed smooth packets.

Dependencies: proof 213 for the exact common space and residual; proof 199 for the exact band kernels and reconstruction pattern, strengthened globally in(3)-(4); proof 203 for the origin product; proof 204 for packet algebra; topics39,50 and117 for the actual differentiated modal coefficients. All global multiplier, tail, domain and image arguments are supplied above. No new numerical calculation, inverse bound, complement certificate or existence statement is made.

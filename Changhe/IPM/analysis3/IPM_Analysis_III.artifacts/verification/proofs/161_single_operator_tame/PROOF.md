# The single-operator coefficient commutator and product bound

## Statement and notation

Let C=R times S1 with its flat cylinder metric. Let s,Lambda be smooth real functions with all derivatives bounded, Lambda bounded, and

 2<s_0<=s(X)<=s_+<infinity.

Fix N>=0 and use uniform left quantization to define

 A=Op(e^(N Lambda(X))<xi>^(s(X))).

The space H^{s(.)} is the variable-order Hilbert space used in proof 123. Equivalently its norm is the square sum of ||w_m Delta_m v||_2, where Delta_m is an inhomogeneous smooth Fourier partition, m>=0, and w_m(X)=e^(N Lambda(X))2^(m s(X)). The bounded factor e^(N Lambda) changes only the equivalence constants. All distributions and Sobolev spaces in this proof are on C.

Let E be a fixed smooth bounded vector field with all derivatives bounded, c a real scalar, and B=cE+Z, with Z in H^{s(.)} and C_b^(1,alpha), 0<alpha<1. For

 0<epsilon<=min(alpha/2,(s_0-2)/2),

there is a constant depending only on the fixed data, alpha and epsilon such that

 ||sum_l[A,B_l]partial_l v||_2
 <=C(|c|+||DZ||_infinity)||v||H^s
   +C(|c|+||Z||H^s+||Z||C^(1,alpha))||v||H^(s-epsilon).  (1)

The left side extends continuously from smooth v to every v in H^{s(.)}. The same conclusion holds at any constant order sigma>2, with the corresponding coefficient norm. This is a coefficient commutator. The full transport commutator also contains

 -N(B.grad Lambda)Av-(B.grad s)Op(e^(N Lambda)<xi>^s log<xi>)v,             (2)

which are not included in (1).

A second assertion is the following product estimate. Let r be smooth bounded with r_->0, and let d=c d_E+d_Z, where d_E is fixed smooth bounded with all derivatives bounded, and d_Z is in H^{r(.)} and L-infinity. Then, for f in H^{r(.)} and L-infinity,

 ||d f||H^r<=C||d||_infinity||f||H^r
     +C(|c|+||d_Z||H^r)||f||_infinity+C|c|||f||_2.        (3)

Here the constant may depend on r and d_E. In particular (3) applies to r=s and r=s-1.

## Uniform kernel and localization facts

Choose fattened blocks Delta~_m equal to one on both the m-th input annulus and the product of that annulus with a sufficiently low frequency ball. The kernel of A Delta~_m satisfies, for every L,

 |K_m(X,Y)|<=C_L w_m(X)2^(2m)(1+2^m d(X,Y))^(-L).        (4)

At low frequency the same statement has m=0. This follows by scaling the compact frequency annulus and integrating by parts in xi. Frequency derivatives of <xi>^s have the usual order decrease uniformly for bounded s; they introduce no x-derivatives. The cylinder version follows by periodizing one coordinate of the Euclidean kernel.

The weights satisfy

 w_m(X)/w_m(Y)<=C(1+2^m d(X,Y))^M,                      (5)

with fixed C,M. To check (5), take logarithms. At d<=2^(-m), bounded grad s gives m|s(X)-s(Y)|<=C m2^(-m). At 2^(-m)<d<=1, use the lesser of C m d and m(s_+-s_-), which is bounded by C'+M log(1+2^m d). At d>=1 boundedness of s gives the same inequality. Lambda contributes a bounded factor. Similarly, for k>=m-C_0,

 w_m(X)/w_k(Y)<=C2^(-(k-m)s_0)(1+2^m d(X,Y))^M.          (6)

For k<m within a fixed distance, replace the fixed factor by a larger constant. Equations(4)-(5) and Schur's test give weighted Bernstein and the bound ||A f||_2<=C||w_m f||_2 for an annular f.

We also use rapid off-diagonal frequency decay:

 ||Delta_j A Delta_m||_(L2->L2)<=C_R2^(-R max(j,m))
 when |j-m|>C_1, for any prescribed R.                 (7)

For clarity, (7) is a property of this smooth fixed symbol, not a rough-coefficient assertion. Insert the frequency cutoffs into the oscillatory kernel. If output and input frequencies are separated, their difference is comparable to 2^max(j,m). Repeated x-integration by parts transfers arbitrary powers of that difference to derivatives of the symbol. Such derivatives cost only powers of log(2+2^m), times 2^(m s_+). Choosing more integrations absorbs this fixed order and every logarithm. Localize in unit cylinder charts; the separated-chart kernels have arbitrarily summable spatial decay by xi-integration by parts. The chart Schur sums are uniform because all derivatives of s,Lambda are bounded. This proves (7), including the low-frequency blocks. The same proof applies to finitely enlarged annuli and balls used below.

Finally, if F in H^{r(.)}, G in L-infinity and r_->0, then

 ||sum_k Delta_k F S_(k+C_0)G||H^r<=C||F||H^r||G||_infinity.             (8)

Indeed the k-th product has output frequency at most 2^(k+C). Projecting onto the j-th output block gives zero unless j<=k+C. Use (6), the uniformly L1 kernels of the low cutoff on G and of the output projection, and Schur's test. The remaining frequency matrix is bounded by C2^(-(k-j)r_-) for k>=j-C. Its row and column sums are finite. Young's inequality in the frequency index proves (8). This argument includes high-high interactions with arbitrarily low output; they cannot be discarded by annular orthogonality.

## Proof of the commutator

Take smooth v first. Split the pairs of coefficient and input frequencies at k=m-C_0, with C_0 fixed large. Writing K_B=sum_l[A,B_l]partial_l, we obtain exactly

 K_B v=I+II+III,
 I=sum_(l,m)[A,S_(m-C_0-1)B_l]Delta_m partial_l v,
 II=A(sum_(l,k)Delta_k B_l S_(k+C_0)partial_l v),
 III=-sum_(l,k)Delta_k B_l A S_(k+C_0)partial_l v.        (9)

For I, put b_m=S_(m-C_0-1)B_l. The enlarged block chosen above equals one on both relevant Fourier supports, so its kernel is exactly K_m(X,Y)(b_m(Y)-b_m(X)) applied to Delta_m partial_l v. The difference is bounded by C||DB||_infinity d(X,Y). Equations(4)-(5) gain 2^(-m), cancelling the derivative, and give

 ||[A,b_m]Delta_m partial_l v||_2
       <=C||DB||_infinity||w_m Delta~_m v||_2.          (10)

These outputs are almost annular. For A(b_m Delta_m partial_l v), use (7) since the product is annular. For b_m A Delta_m partial_l v, multiplication by the low frequency b_m can shift frequencies only by a small part of the m-th scale; first resolve the output of A and apply (7) outside a fixed enlargement. The off-annular bounds have the form C_R2^(-R max(j,m))2^m||B||_infinity||Delta~_m v||_2. Their frequency matrix has summable rows and columns. On the finitely overlapping main annuli use (10). Hence

 ||I||_2<=C||DB||_infinity||v||H^s+C||B||_infinity||v||_2.              (11)

This is the output-orthogonality step needed to pass from a dyadic coefficient estimate to one operator. No such step is used for III.

For II_Z, use (8) with G=partial_l v and the bounded map A:H^s->L2 from proof 144. It gives C||Z||H^s||Dv||_infinity. For II_E, every positive-frequency block of E has arbitrarily fast decay in every bounded-derivative norm. Products with S_(k+C)Dv have frequency at most 2^(k+C') and can be bounded with the constant maximal order s_+. Choosing the decay exponent larger than s_++2 makes the k-sum converge with bound C|c|||v||_2. The k=0 product has a fixed frequency ball and the same bound. Since s_0-epsilon>2 in two dimensions,

 ||Dv||_infinity<=C||v||H^(s-epsilon).                 (12)

For III let a_m=||w_m Delta~_m v||_2. The annular kernel and Bernstein estimates give

 ||A S_(k+C_0)partial_l v||_2<=C sum_(m<=k+C_0)2^m a_m.

The coefficient blocks satisfy ||Delta_k B||_infinity<=C2^(-k(1+alpha))||B||C^(1,alpha), with the usual interpretation at k=0. Absolute summation, followed by changing the order of the nonnegative sums, therefore gives

 ||III||_2<=C||B||C^(1,alpha) sum_m 2^(-m alpha)a_m
 <=C'||B||C^(1,alpha)(sum_m 2^(-m alpha)a_m^2)^(1/2)
 <=C''||B||C^(1,alpha)||v||H^(s-alpha/2).               (13)

The middle step is Cauchy-Schwarz and the finite geometric sum sum_m2^(-m alpha). Equation(13) explains why no output orthogonality is necessary for III. It only establishes failure of this absolute-sum proof at alpha=0, not an independent unboundedness theorem at that endpoint.

Combine (11)-(13), use ||B||_infinity<=C(|c|+||Z||H^s), and use the continuous embedding H^(s-epsilon) into H^(s-alpha/2). This proves (1). Approximation and the resulting bounded operator extend it to H^s. Identity(2) follows directly by differentiating the left symbol, so the logarithm is separated before this estimate is invoked.

## Proof and use of the product bound

Split d f into its low-coefficient/high-input part and its remaining high-coefficient part. The first has almost-annular outputs and is bounded by C||d||_infinity||f||H^r, by (4)-(7) with r in place of s. The d_Z part of the second is (8). The smooth nondecaying d_E part is summed by arbitrary block decay as in II_E above. This proves (3).

For the coefficient map of proof 155, B=c[g]E+Z[g] and the bulk or localized cofactor scalar d have all the required norms bounded by C||g||G_s. Thus (1) bounds the coefficient commutator by C||g||G_s||v||H^s. Formula(3) at r=s-1, applied to partial_l v, bounds B.grad v in H^(s-1) by the same expression. Its L-infinity input is justified by (12), not by an embedding of H^(s-1) into W^(1,infinity).

## Scope and dependencies

This independently verifies Lemmas K and P in the theory author's work/Hs_pert.md, including the formerly missing summation for a single operator. It uses the smooth variable-order space and mapping facts of topics123 and144, and gives the frequency estimates needed for this particular commutator. It is consistent with the counterexample of proof 151 because (2) remains outside (1). The theorem supplies qualitative constants only. The perturbed maximal-domain estimate, generation and injectivity are separate assertions.

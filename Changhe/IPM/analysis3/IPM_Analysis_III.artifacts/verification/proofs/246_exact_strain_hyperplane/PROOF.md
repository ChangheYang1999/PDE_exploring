# Exact strain hyperplanes inside the shifted-junction section

## Statement

Let S be the exact 38-dimensional low input space of proof 239, with basis h_i=2r^3 cos(theta)^4 sin(theta) B_i(log r)/s_i, i=0,...,37, in precisely the metadata order and exact positive binary scales of that topic. Let S_H and S_D be its exact high input and maximal high graph intersections from proof 240, including its binding clarifications. Their dimensions are32 and29. All three spaces carry the LOW input norm of S1, with exact positive Gram G from proof 239. No high operator norm is considered here.

Let a_i=c[h_i] be the exact strain of the source-defined column, with the fixed physical kernel

 c[h]=(1/pi) integral h(x,y)y(3x^2-y^2)/(x^2+y^2)^3 dxdy.

Let b_i be the exact rational value represented by the stored binary64 metadata entry cvec[i]. Define b on S by this row. It is an approximation to c, not its definition. Both functionals restrict to each W in {S,S_H,S_D}.

The exact hyperplanes W cap ker c have dimensions37,31,28 respectively. The same dimensions hold for W cap ker b. For each W, the calculation specified below produces rigorous constants D_W>=0 and A_W>0 such that

 ||(c-b)|W||_(W*) <= D_W,    ||c|W||_(W*) >= A_W.        (1)

Set delta_W=D_W/A_W. When delta_W<1, the orthogonal projection P_W onto ker(c|W), for the exact LOW input inner product, restricts to an isomorphism

 P_W:ker(b|W) -> ker(c|W)

and obeys, for every v in ker(b|W),

 ||v-P_W v|| <= delta_W ||v||,
 sqrt(1-delta_W^2)||v|| <= ||P_W v|| <= ||v||.            (2)

All constants in(1),(2) refer to the exact source-defined input form and strain. The completed calculation's directed constants and hashes are in RESULTS.md and evidence/check.json. The analytic statements are independent of their numerical size.

## Nonzero strain and dimensions

The pure spline sp10 is column13 in this basis and belongs to S_D: its support is away from all three exceptional joins, so its jump constraints vanish. It belongs to S_H as well. Its radial coefficient is nonnegative and positive on an interval; the scale is positive. The exact angular strain integral for m=1 gives

 c[h_13]=(3/(8s_13)) integral exp(2t) B_13(t) dt >0.     (3)

This identity is the strain formula already checked in proof 239. Thus c is a nonzero linear functional on each W. The binary metadata value b_13 is strictly positive, as checked exactly in the finite rational input record, so b also is nonzero on all three spaces. The kernel of a nonzero functional on an n-dimensional real vector space has dimension n-1. This proves the dimension claims without a numerical rank tolerance or an assumption about exact equality of a and b.

## Proof of the projection estimates

Fix W. By finite-dimensional Riesz representation for the positive input inner product, let n in W represent c|W: c(v)=<v,n>. Since c|W is nonzero, ||n||=||c|W||_(W*)>0 and

 P_Wv=v-(c(v)/||n||^2)n

is its orthogonal kernel projection. If b(v)=0, then c(v)=(c-b)(v), and(1) gives

 ||v-P_Wv||=|c(v)|/||c|W||_(W*) <= delta_W||v||.

Orthogonality gives ||P_Wv||^2=||v||^2-||v-P_Wv||^2, proving(2). When delta_W<1 this map is injective on ker b. The two kernels have the same finite dimension, so it is onto ker c. This proves the theorem. The projection preserves W by construction; using the full-space normal for S_H or S_D without restriction would not give that conclusion.

## How the ball certificate proves the dual estimates

Let Q be an exact full-rank coefficient matrix whose columns span W. For W=S, take Q=I. For S_H and S_D take the rational nullspace matrices of proof 240, in its scaled metadata coordinates. Set

 G_W=Q^T G Q,    a_W=Q^T a,    b_W=Q^T b.

The exact source-defined G and a are enclosed by the 640-bit dyadic-endpoint certificate of proof 239. Every entry of Q and b is rational and enters the calculation exactly. Let T be any rational square matrix of the appropriate dimension for which the computed interval bound

 epsilon_W >= ||T^T G_W T-I||_2,    epsilon_W<1            (4)

holds. A midpoint Cholesky calculation only proposes T; its output is rounded to exact dyadics and(4) is then checked in ball arithmetic. The row-sum bound is valid because the exact congruence matrix is symmetric. Equation(4) implies T is invertible and

 (1-epsilon_W)I <= T^T G_W T <= (1+epsilon_W)I.

Changing coordinates v=Q T z therefore proves, for every covector ell,

 ||T^T ell||_2/sqrt(1+epsilon_W)
 <= sqrt(ell^T G_W^(-1)ell)
 <= ||T^T ell||_2/sqrt(1-epsilon_W).                     (5)

Use the right inequality with ell=a_W-b_W to obtain D_W and the left with ell=a_W to obtain A_W. The square-root expressions and their directed endpoints are evaluated in ball arithmetic. No inversion of an uncertain matrix or unverified floating singular value is used. Every rational matrix T is exported for exact replay. The source archive hash and the original-data Gram certificate are checked before this calculation.

## Scope of the result

This certifies input hyperplanes, their dimensions and their metric distance. It does not certify any image Gram, source projection, quadrature error, operator singular value or complement inverse. Even for an exact linear operator A on W, using(2) to compare output vectors requires an independently bounded operator norm Lambda_W, since only

 ||A v-A P_Wv|| <= Lambda_W delta_W ||v||

would follow. No such quantitative output norm is supplied here. In particular the floating cvec-nullspace values in the reports remain floating values on the binary constraint. The very small input-hyperplane difference, if certified, is not a replacement for missing image error bounds.

Dependencies: proof 239 exact source Gram, strain and low conformity; proof 240 exact high intersections and binding clarifications; proof 242 frozen metadata and complete cell accounting. The proof above was written before the computation. The calculation is local, single-threaded, and uses no output matrix. No Lean or other formal proof build is asserted.

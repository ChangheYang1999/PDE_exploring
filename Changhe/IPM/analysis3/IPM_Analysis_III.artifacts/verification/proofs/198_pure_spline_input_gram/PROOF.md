# Exact input norms for the pure-spline S1 sections

## Statement, inputs and scope

Let the original degree-seven knot vector be the exact dyadic interpretation of the `knots` array in the archived Analysis I trial_v2_h0.008.npz, with SHA256 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. Remove the eightfold repetitions at both ends, take every sixtieth interior knot beginning with the first, and clamp the resulting vector with eight copies of each original endpoint. Let b_i,0<=i<34, be its degree-seven B-splines in their usual Cox-de Boor normalization. Write t=log r and p(theta)=cos(theta)^2 sin(theta). For i=4,...,29 and m=1,2,3 define

 u_(i,m)(r,theta)=r^3 p(theta) b_i(t)(cos(2m theta)-(-1)^m).

These are the unscaled pure-spline columns of the S1 runs at stride60. They have compact radial support and zero vertical-axis cofactor trace. They belong to the low remainder space R=L2(w), with

 w=|cos theta|^(-17/2) exp(mu(t)),
 mu(t)=-17t/2 for t<0 and -5t/4 for t>=0.

They belong to the maximal domain of its transport: at each radial join the zero extension is at least C3, and on the vertical axis their angular vanishing has order four, which the tangent parity-compatible transport preserves. The bounded renormalized remainder coupling therefore gives their S1 images in R. This is only a low-domain statement. It does not assert membership in the high correction space or its high graph domain.

For arbitrary nonzero positive scaling constants s_i, their exact input Gram matrix is

 G_((i,m),(j,n))=A_(m,n) R_(i,j)/(s_i s_j),                  (1)
 R_(i,j)=integral_R exp(8t+mu(t)) b_i(t)b_j(t) dt,
 A_(m,n)=integral_0^(2pi) Q_m(theta)Q_n(theta)|cos theta|^(-1/2)dtheta,
 Q_m=p(theta)(cos(2m theta)-(-1)^m)/cos(theta)^4.

The companion computation reconstructs R directly from the original knot vector using exact rational spline polynomials and directed exponential moments. It does not import the numerics team's spline evaluator, projected angular templates, node cache, radial quadrature or Gram matrices. Existing floating input Grams may subsequently be compared to this independent enclosure, using their stored binary scaling constants as exact numbers. Such a comparison says nothing by itself about the output Gram, the exact operator's finite singular value or a complement inverse.

## Factorization of the norm

The polar area element is r dr dtheta=e^(2t) dt dtheta. Each column contributes r^3, so their product contributes the radial factor e^(8t). Proof 185 proves that each angular input is cos(theta)^4 Q_m, with the exact sine-polynomial quotient

 Q_1=2sin(theta),
 Q_2=-8sin(theta)^3,
 Q_3=2sin(theta)-16sin(theta)^3+32sin(theta)^5.

The product of the two cos^4 factors cancels eight of the seventeen halves in the angular weight. This leaves |cos theta|^(-1/2), which is integrable. Separation of variables gives(1). The radial integrals are finite because all b_i have compact support, and their Gram is positive definite because distinct B-splines are linearly independent on the full support interval. The angular polynomials have distinct highest sine powers and hence are linearly independent. Thus the full Kronecker Gram and every stated scaling are positive definite.

Set I_j=integral sin(theta)^(2j)|cos(theta)|^(-1/2)dtheta. Substitution z=sin(theta)^2 on each quadrant gives

 I_j=2 Beta(j+1/2,1/4),
 I_(j+1)/I_j=(4j+2)/(4j+3).

Consequently A is an exact rational matrix times I_0=2 Beta(1/2,1/4). Computing the polynomials Q_1,Q_2,Q_3 and these rational moment ratios requires no angular quadrature. The positive common Beta factor is evaluated with directed ball arithmetic.

## Rational spline reconstruction and directed radial integration

On a nonzero coarse span [a,a+h], write x=(t-a)/h. Starting with the degree-zero indicator of that span, the Cox-de Boor recurrence produces the eight active degree-seven B-splines as rational polynomials in x. Every knot and h is rational; thus the polynomial coefficients are exact. An independent de Boor evaluator with each active unit coefficient vector gives the same polynomials. Their sum is the constant polynomial1. Exact endpoint derivatives through order six agree at every simple interior knot. These identities check the normalization, active indices and continuity without testing only rounded samples.

Split any span crossing t=0 at0. On each resulting interval [a,a+h], the weight is e^(lambda t) with lambda=-1/2 or27/4. Every integrand is therefore e^(lambda a) times a polynomial P(x) of degree at most14 times e^(z x), where z=lambda h. Its integral is

 h e^(lambda a) sum_(j=0)^14 P_j M_j(z),
 M_j(z)=integral_0^1 x^j e^(zx)dx.

For a positive integer N, Taylor's theorem on0<=x<=1 gives the rigorous enclosure

 M_j(z) in sum_(n=0)^(N-1) z^n/(n!(n+j+1))
              + [-E_j,E_j],
 E_j=e^|z| |z|^N/(N!(N+j+1)).                            (2)

This is valid for either sign of z. Multiply each interval moment by the corresponding exact polynomial coefficient and sum with directed arithmetic; cancellation does not affect enclosure. Integrate every coarse span, including both pieces of the one crossing0. Outside the first and last knots the selected b_i vanish, so there is no omitted radial tail. The numerical script must check all exact partitions, polynomial identities and finiteness before an enclosure is accepted.

The same moments with lambda=2 also give the radial strain integrals. Angular orthogonality and the original sin(3theta) kernel yield, for m=1,2,3,

 c[u_(i,m)]=a_m integral e^(2t)b_i(t)dt,
 (a_1,a_2,a_3)=(3/8,-3/8,1/8).                         (3)

Indeed the sin(3theta) coefficient of p cos(2m theta) is1/8,-1/8,-1/8 respectively, and subtracting(-1)^m p subtracts(-1)^m/4. This supplies an independent check of the stored strain row on the pure columns after dividing by s_i. This is a scalar functional computation; it does not change the operator used for S1.

## Comparison with floating matrices

A stored binary scaling s_i is interpreted as its exact positive dyadic value. Formula(1), divided by these values in interval arithmetic, encloses the exact Gram of that declared scaled basis, independently of how the scales were estimated. The stored floating matrix is similarly interpreted entry by entry as exact dyadic numbers for error comparison. If E=G_float-G_exact and a computed invertible real matrix T satisfies

 ||T^T G_exact T-I||_2<=e<1,
 ||T^T E T||_2<=d,

then for every coefficient vector v,

 |v^T E v| <= d/(1-e) v^T G_exact v.                    (4)

To prove this, put v=Tz, use the two quadratic-form bounds, and divide by the positive lower bound(1-e)||z||^2. A maximum absolute row sum bounds the spectral norm of every real symmetric matrix here. All errors in(4) are taken from outward interval bounds. The choice of T may come from an ordinary floating Cholesky factor because it is treated as an exact matrix and its properties are then checked. No assumption that the Cholesky computation was exact is used.

If desired, replacing a positive approximate input Gram by G_exact in a stored output-pair eigenproblem is a numerical diagnostic with a corrected input norm. It still has the unverified output integration and division errors. Neither such a solve nor(4) supplies a lower bound for the full operator.

## Dependencies and acceptance

The input file and normalization are those of proof 04; the exact angular templates are proof 185; the low realization is topics43 and48. All numerical enclosures and comparisons are pending until the original-data computation and its independent replay have passed. The final certificate must identify the original source, exact coarse knots, interval Gram, scaling metadata and scripts by hashes.

## Original-data verification result

The computation finished at2026-10-28T13:33:35.707417+00:00. There are27 coarse spans and28 integration pieces. All216 active unit-column polynomials agree exactly between Cox-de Boor recursion and independent de Boor interpolation. All884 scalar-column interior C6 joins and the selected endpoint C3 zero jets agree exactly. The512-bit Taylor integration and640-bit antiderivative-moment replay overlap on every radial Gram and strain entry. Exact rational angular moment ratios agree with direct Gamma-product moments. The matrix enclosure is supplied for all78 pure columns m=1,2,3, at the exact binary scales in the two metadata snapshots.

For the stored S1M3 pure52-column input matrix G_float, the independently reconstructed G satisfies the rigorous quadratic-form bound

 |v^T(G_float-G)v| < (237/100000000) v^T G v

for every nonzero real coefficient vector v. The computed certificate uses a whitening identity error below2.675e-12 and a transformed error below2.370e-6; formula(4) gives the stated strict bound2.37e-6. The binary whitening matrix is saved and checked as exact data. Every stored pure-column strain coefficient in both snapshots has relative error below271/10^18=2.71e-16 against the exact integral(3). These claims concern the specified stored input matrix and strain row. The S1M4P output matrix is not yet complete, and no operator lower bound follows from these checks.

The first script attempt called a Beta method unavailable in the installed python-flint. It stopped after radial production and replay, before writing a certificate. Its log and script are retained. Gamma products and the reflection identity replace that method; the mathematical formulas and all radial computations are unchanged.

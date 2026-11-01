# An exponential density bound suffices for the full exterior equation

## Conditional theorem and scope

Fix c>1, gamma=1/c, delta=1-gamma and p_n=1-n delta. Assume delta is irrational and has the following explicit Diophantine bound: for some kappa>0 and tau>=1,

\[
|m-n\delta|\ge\kappa n^{-\tau}
\quad(n\ge1,\ m\in\mathbb Z).
\tag{D}
\]

Let a nonzero finite odd sine polynomial f_1 generate the pure stationary recursion. Write L for its highest frequency and B=L+1. For sigma>=0 let ||.||_sigma be the angular Wiener norm. Suppose that constants M>0 and A>0 satisfy the additional hypothesis

\[
\|f_n\|_\sigma\le M A^{n-1}\qquad(n\ge1).
\tag{E}
\]

Then, for every R>A^(1/delta), the density, stream and uniquely reconstructed finite-polynomial potential series converge absolutely on r>=R after removing their respective leading radial weights. Every fixed Cartesian derivative series converges absolutely in its corresponding weighted norm, uniformly for r>=R. Their sums satisfy

\[
\rho=-\partial_y\Delta\chi,\quad
u=(-\chi_{xyy},\chi_{xxy}),\quad
(cX+u)\cdot\nabla\rho-\rho=0
\]

on r>R. This is a local exterior result, with no claim of a canonical whole-plane extension.

The additional hypothesis (E) is not proved here. This theorem identifies what an exponential density estimate would be sufficient to establish. It is not a construction of a nontrivial convergent series.

## The stream bound

The support induction gives

\[
\deg f_n\le Bn-1,\qquad\deg g_n\le Bn.
\]

The cancellation form of the stream inverse is

\[
b_{n,j}=-\frac{a_{n,j-1}}{2(2j+2-n\delta)}
+\frac{a_{n,j}}{2(2j-2+n\delta)}.
\]

The first inverse denominator is at most n^tau/(2 kappa) in absolute value by (D). The second is at most 1/(2n delta). Each shift changes the Wiener weight by at most exp(sigma). Thus

\[
\|g_n\|_\sigma\le K_\sigma n^\tau\|f_n\|_\sigma,
\qquad K_\sigma=\frac{e^\sigma}{2}(\kappa^{-1}+\delta^{-1}).
\tag{1}
\]

## A bound for the pure potential inverse

Set q=p+3 and write

\[
\chi=r^q\sum_{m=0}^K C_m\cos(2m\theta),\qquad
\Delta\chi=r^{p+1}\sum_{m=0}^K d_m\cos(2m\theta).
\]

Then d_m=(q^2-4m^2)C_m. Write the target density as sum_(m=0)^K a_m sin((2m+1)theta). At order n put

\[
x=(n\delta-2)/2,
\]

so p+1=-2x. The density equations are

\[
a_0=2x d_0+(1-x)d_1,
\qquad
a_m=(m+x)d_m+(m+1-x)d_{m+1}\quad(m\ge1),
\tag{2}
\]

with d_(K+1)=0. Suppose n delta>=8, so x>=3. For m>=1,

\[
\frac{|m+1-x|}{m+x}\le1,
\qquad\frac{|1-x|}{2x}\le1.
\]

Descending substitution therefore gives

\[
|d_m|\le x^{-1}\sum_{k=m}^K|a_k|.
\]

The same inequality works for m=0, including its different diagonal coefficient. A downward shift from input frequency 2k+1 to output frequency 2m does not increase the exponential weight. Summing over m and using K+1<=Bn/2 proves

\[
\|d\|_\sigma\le\frac{K+1}{x}\|f_n\|_\sigma
\le\frac{Bn}{n\delta-2}\|f_n\|_\sigma
\le\frac{4B}{3\delta}\|f_n\|_\sigma.
\tag{3}
\]

At these orders q=4-n delta<=-4. For k=2m>=0,

\[
|q^2-k^2|=|k+4-n\delta|(k+n\delta-4)
\ge\frac{\kappa\delta}{2}n^{1-\tau}.
\]

Consequently

\[
\|C_n\|_\sigma\le\frac{8B}{3\kappa\delta^2}
 n^{\tau-1}\|f_n\|_\sigma\quad(n\delta\ge8).
\tag{4}
\]

There are only finitely many earlier orders. Their pure potential maps are invertible because delta is irrational. Let T_n be the finite triangular inverse from density frequencies at most Bn-1 to potential frequencies at most Bn-2. Its unweighted l1 operator norm is finite. Because every nonzero matrix entry lowers frequency, its weighted norm at sigma>=0 is no larger than its unweighted norm. Define

\[
C_* =\max\left\{\frac{8B}{3\kappa\delta^2},
\max_{1\le n<8/\delta}n^{1-\tau}\|T_n\|_{\ell^1\to\ell^1}\right\}.
\]

This is an explicit finite maximum of well-defined finite matrices. Then

\[
\boxed{\|C_n\|_\sigma\le C_*n^{\tau-1}\|f_n\|_\sigma}
\qquad(n\ge1).
\tag{5}
\]

This argument avoids multiplying a crude small-divisor bound at every step of a triangular back substitution. Beyond a fixed order, that substitution has coefficients of absolute value at most one.

## The quadratic irrational in the prompt

For delta=1/sqrt(5), condition (D) holds with

\[
\tau=1,\qquad\kappa=\frac1{5(1+2\delta)}.
\]

Indeed, if |m-n delta|>=1 the conclusion is immediate. Otherwise m>n delta-1, m<n delta+1 and

\[
|m-n\delta|=\frac{|5m^2-n^2|}{5|m+n\delta|}
\ge\frac1{5(2n\delta+1)}\ge\kappa/n.
\]

For negative m the distance is at least n delta and also satisfies the bound; the numerator identity above is only needed for m>=0. There is a sharper potential estimate at n delta>=8: the same integer numerator gives

\[
|(4-n\delta)^2-k^2|
\ge\frac{k+n\delta-4}{5(k+n\delta+4)}\ge\frac1{15}
\qquad(k\ge0).
\]

Together with (3), this yields

\[
\boxed{\|C_n\|_\sigma\le\frac{20B}{\delta}\|f_n\|_\sigma}
\quad(n\ge18).
\tag{6}
\]

Thus the Gevrey-one density upper bound in `../04_gevrey/PROOF.md` also gives a Gevrey-one potential bound, with a fixed constant covering the first seventeen orders. Its potential Borel transform converges near zero. This does not imply Borel summability.

## A certified uniform constant for bandwidth L<=19

At delta=1/sqrt(5) and density bandwidth at order n at most 20n-1, the following explicit bound holds for all sigma>=0 and n>=1:

\[
\|C_n\|_\sigma\le900\|f_n\|_\sigma.
\]

For n>=18, (6) gives 400 sqrt(5)<900. For the first seventeen orders, the finite l1 operator norm is the maximum absolute column sum of T_n. The script `../../code/potential_bound_certificate.py` encloses every entry in all 1530 columns by exact dyadic interval arithmetic with 256 fractional bits. It starts from consecutive dyadic bounds on sqrt(5), verified by integer squaring. Every arithmetic operation rounds outward by integer floor or ceiling division, and every division interval excludes zero. Every column sum is strictly below 900. The largest early norm is at order nine and is less than 796.

The retained certificate `verification/potential_bound.json` gives the square-root bounds, per-order dyadic norm enclosures, column counts and the source hash. The finite calculation covers every early matrix column; the analytic argument covers all remaining orders. No floating-point midpoint is used to certify this bound.

## Weighted convergence and derivatives

Let s_n be any of p_n, p_n+1 or p_n+3 and let H_n be the matching density, stream or potential coefficient. A Cartesian derivative of r^(s_n)H_n lowers its radial degree by one and increases its angular bandwidth by at most one. On a coefficient with radial degree s and bandwidth J, either Cartesian derivative has Wiener operator norm at most

\[
e^\sigma(|s|+J).
\]

At every fixed derivative order h, the resulting coefficient norm is therefore bounded by a fixed polynomial in n times ||H_n||_sigma. By (1), (5) and (E), this is a fixed polynomial in n times M A^(n-1). The weighted derivative sums are bounded by convergent series of the form

\[
\sum_{n\ge1}\mathrm{poly}_h(n)\,M(A R^{-\delta})^{n-1},
\]

because A R^(-delta)<1. The weights are r^(h-gamma) for density and velocity, r^(h-gamma-1) for stream, and r^(h-gamma-3) for potential.

This proves absolute weighted uniform convergence of all fixed derivatives. In particular three potential derivatives recover rho and u, and four give the density gradient used by the stationary equation. Termwise potential identities follow from uniform derivative convergence. At every fixed radius, absolute convergence justifies the quadratic product and its Cauchy convolution. Each coefficient of the stationary residual is zero by the formal recurrence, so the residual is identically zero.

The sums are analytic in z=r^(-delta) after factoring out the indicated leading power. If sigma>0 they are analytic in theta in each smaller strip. Even for sigma=0, the linear bandwidth bound supplies a small positive angular strip after replacing A by A exp(B sigma') and choosing sigma'>0 with A exp(B sigma') R^(-delta)<1. No unproved whole-plane inverse or boundary condition is used.

## Dependencies

The argument uses the recurrence and finite inverse from `../01_recurrence/PROOF.md`, elementary triangular estimates, the stated Diophantine hypothesis, and absolutely convergent power-series operations. The only unresolved hypothesis is the exponential density estimate (E), which remains the central research question.

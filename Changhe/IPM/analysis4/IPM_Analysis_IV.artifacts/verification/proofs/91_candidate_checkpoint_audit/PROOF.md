# Independent audit of the extended Candidate007 checkpoint

Status: finite input, precision and differential Poisson checks confirmed through 500 (V552). Selected nonlinear checks, including orders390,410 and500, are confirmed (V164, V236 and V559). No infinite convergence conclusion is asserted.

## Exact statement and hypotheses

Use the exact rational parameter and the ten odd sine coefficients extracted from the authoritative Candidate007 data in topic02. Put c=4076476460239181/2251799813685248, delta=1-1/c, p_n=1-n delta and P_n=2-n delta. At order n, write

    F_n(theta)=sum_(j>=0) a_(n,j) sin((2j+1)theta),
    G_n(theta)=sum_(j>=1) b_(n,j) sin(2j theta).

The stored checkpoint consists of interval coefficients. The audit establishes, for its finite prefix only: exact inclusion of the prescribed parameter and leading density data, per-coefficient precision decisions, independent norm enclosures, zero angular mean in the stream, the admissible Fourier support bounds, and interval consistency of every coefficient in the differential Poisson equation. The completed selected-order nonlinear audits are recorded below.

## Poisson identity

For a homogeneous polar term, Delta(r^P sin(m theta))=(P^2-m^2)r^(P-2)sin(m theta). Direct Cartesian differentiation gives

    partial_x[r^p sin(l theta)]
      = (r^(p-1)/2)[(p+l)sin((l-1)theta)
                            +(p-l)sin((l+1)theta)].

Because p=P-1, the coefficient of sin(m theta), m=2j, in partial_x(r^p F) is

    [(P-m)a_(j-1)+(P+m)a_j]/2.

Thus -Delta(r^P G)=partial_x(r^p F) is equivalent to

    (m^2-P^2)b_j=[(P-m)a_(j-1)+(P+m)a_j]/2.    (1)

The script evaluates both sides of(1) at2304-bit precision from independently decoded dyadic input intervals. It checks the nonvanishing denominator using the exact rational delta. This avoids importing or repeating the generating code's Poisson inverse. Exact dyadic conversion is checked before arithmetic, so no input radius is dropped.

## Norms, precision and scope

The angular sine Wiener norm is sum_j|a_j|; the coefficient Euclidean norm is sqrt(sum_j a_j^2). The latter differs from a chosen angular L2 norm by its normalization constant. Each quantity and its nth root are enclosed by outward-rounded interval arithmetic. A nonzero midpoint is considered resolved only when its radius is strictly smaller than its modulus. Zero midpoints with nonzero radius are separately counted as unresolved.

The input's exact parameter and leading profile are tested against rational endpoints of the stored intervals. Coefficients at every order have frequencies at most20n-1 in density and20n in stream, by induction from the highest initial frequency19 and the Poisson shift by one. Checking the stored lengths verifies this finite support condition.

A residual interval containing zero is a consistency check, not an existence theorem by itself: wide erroneous intervals could also pass. The independent precision checks quantify the width. The generating interval recurrence and earlier independent exact low-order checks supply additional evidence; they do not turn a finite prefix into an all-order convergence proof. The first possible rational resonance for this stored parameter is far beyond all computed orders, so these finite computations cannot decide its compatibility.

## Dependencies and evidence

The general recurrence and sign conventions are derived in topic01. Exact Candidate007 extraction is topic02. The independent dyadic decoder was introduced in topic53. Each completed audit retains its exact input hash, execution source, timestamp, parameter, precision and finite prefix. A frozen compressed checkpoint is retained when disk permits.

## Independent nonlinear implementation

Set z=exp(i theta), E=z partial_z, and write Fbar=iF, Gbar=iG. A sine term a sin(m theta) is represented by the real Laurent polynomial (a/2)(z^m-z^(-m)). Since partial_theta F=E Fbar, the stationary coefficient equation is exactly

    (n-1)(c-1) Fbar_n
      =sum_(i+j=n)[P_i Gbar_i E Fbar_j
                            -p_j E Gbar_i Fbar_j].       (2)

The code represents each order-n Laurent polynomial after multiplication by z^(20n). Offsets add exactly in every product because i+j=n. E acts by the original signed Fourier frequency before this storage shift. Thus ordinary polynomial multiplication computes(2) without the original implementation's sine product-to-sum indexing or reversed-array convolutions. Every signed Laurent coefficient, including zero parity sectors, is compared in intervals. Each completed selected order is written immediately, with its actual arithmetic time and input hash.

## Independent nonlinear update at 2026-10-31T07:07:16Z

V164 checks all ordered convolution pairs at2,3,6,10,20,40,80,160,233,300,390 using signed Laurent polynomial products and angular Euler derivatives. All49760 tested residual coefficient intervals contain zero. At390 the relative residual is enclosed by +/-2.95e-372. The input checkpoint is the same frozen one used for the exact input, precision and Poisson audit. These are finite interval consistency tests; no infinite-order conclusion is drawn. Complete per-order evidence and real runtimes are in verification/nonlinear_20261031T065314Z/ and verification/nonlinear_20261031T065913Z/.

## Independent order410 update, V224 and V236

The exact-input, support, norm, precision and Poisson audit was extended through410. The independent signed-Laurent nonlinear audit at410 confirms that every residual coefficient interval contains zero. Its total residual norm is at most1.04e-134 against forcing norm3.782491260306599557e225, with relative residual at most2.75e-360. The full nonlinear audit took1523.8474707379937seconds. Evidence is retained in verification/N410_20261031T090044Z and verification/nonlinear_20261031T090613Z. These remain finite interval consistency checks, with the scope described above.

## Finite extension through 500, admitted 2026-10-31T19:47:11+00:00

V552 confirms the exact parameter and all ten leading coefficients, resolution of all 2,505,500 stored density and stream coefficients, every 1,252,500 differential Poisson coefficient and 500 zero stream means. The audit uses 2304-bit arithmetic on the producer's 2048-bit checkpoint. No source uncertainty is discarded. Its actual runtime was58.361799seconds.

At 500 the density l1 coefficient root is 3.5113304338278596773, its coefficient l2 root is 3.4990193030317579247, and the maximum-coefficient root is 3.4953383230852649907. The last maximum is at frequency 155. All reported four-decimal root values at400,450,480 and 500 agree. The independent finite least-squares fit on250..500 gives L=3.6560389182384892449 with RMS0.7169934133332399743, and the ten-step smoothed ratio is3.5188627251889768052 at 500. These are finite statistics, not an asymptotic law. The statistics check took7.153541seconds.

The producer's normalized-division monitor is log10 radius=-301.1999370973300884. This differs from the largest individual coefficient relative radius, approximately4.10e-300 across both fields; both are small, and they measure different quantities. The all-order convergence question at the exact stored rational parameter remains open. The independent nonlinear audit still reaches only its separately admitted selected orders, including410. The input remains in the read-only peer checkpoint and is identified by its SHA256 in the receipts; no additional1.55GB copy was made.

## Independent order500 nonlinear update, V559

Admitted 2026-10-31T20:04:12+00:00. All499 ordered products in (2) were computed from the original2048-bit intervals using2304-bit signed-Laurent arithmetic. All20,000 stored residual coefficient intervals contain zero. The forcing norm is enclosed by2.200934005783706175235914782213057685954e275, the residual norm is at most1.21e-26, and the relative residual is at most5.46e-302. The entire check took974.4799732100219seconds, including input decoding and packing; the nonlinear stage took933.6806026156992seconds. The receipt's checked_at_utc records the start, not completion.

The same source hash as V552 identifies the read-only checkpoint. This establishes finite interval consistency of the complete order500 equation; it does not assert that every intermediate nonlinear order was recomputed or that the infinite series converges. Full evidence is in verification/nonlinear_20261031T194721Z/.

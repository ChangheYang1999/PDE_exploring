# Exact nonzero compatibility certificates over finite fields

Status: PROVED finite grids (V467-V468, V471), following independent theory-part review of the reduction argument. The remaining polar comparisons are additional checks in progress. No uncomputed grid point is included in a conclusion.

## Statement and exact data

Let Q and h be positive integers with h>=2, gcd(h,Q)=1 and 2h<Q. Set delta=2h/Q and c=Q/(Q-2h). Let f_1 be a nonzero finite real odd-sine polynomial with rational coefficients. For n<Q the pure-series stationary recurrence and its Poisson inverse are rational operations with nonzero rational divisors. The first possible stream resonance is at n=Q, frequency m=2h-2. Its compatibility condition is

    kappa=[sin((2h-3)theta)] f_Q = 0.

Choose a prime ell that divides neither an input denominator nor any denominator or numerator inverted by the recurrence through f_Q. If the same recurrence, reduced into the field of ell elements, gives a nonzero kappa, then the rational kappa is nonzero. Hence there is no pure series with this leading profile and the prescribed exponent sequence. This does not exclude a logarithmic continuation or an enlarged exponent set.

The intended finite grids have Q<=120. For Candidate007's exact extracted profile the interval is 2/5<delta<1/2. For f_1=sin(theta), it is 0<delta<1. The reduced-pair enumeration, complete output set and every modular nonzero check must be verified before a whole-grid statement is admitted.

## Independent Cartesian recurrence

Use a signed Laurent representation of a sine polynomial: sin(m theta) is represented by (z^m-z^(-m))/2. It represents i times the physical sine polynomial. On a degree-q homogeneous Laurent monomial r^q z^m define

    X(r^q z^m) = r^(q-1)[(q+m)z^(m-1)+(q-m)z^(m+1)]/2,
    Y(r^q z^m) = r^(q-1)[(q+m)z^(m-1)-(q-m)z^(m+1)]/2.

For physical derivatives X=partial_x and partial_y=iY. If F and G represent i rho and i psi, then XG*YF-YG*XF represents i times u dot grad rho. Therefore, with p_n=1-n delta,

    F_n = sum_(i+j=n)(XG_i*YF_j-YG_i*XF_j)/[(n-1)(c-1)].

For n<Q, obtain G_n by applying the diagonal inverse of -(X^2-Y^2) to XF_n. Its multiplier at frequency m is

    1/[m^2-(2-n delta)^2].

Every zero sine-frequency coefficient is removed only after it is checked to be zero. The odd/even support and antisymmetry identities are checked at every order. If the leading highest frequency is L, B=L+1 bounds the density frequency by Bn-1 and stream frequency by Bn. The product supports then give the complete finite Laurent convolution; no frequency truncation is used.

The forcing at the first resonant stream frequency is -m*kappa, checked as a separate identity. The implementation uses modular polynomial multiplication and these Cartesian operators; it does not call the theory part's polar sine-convolution routine.

## Why a modular certificate proves rational nonvanishing

All input coefficients and all rational divisors used in a fixed finite computation lie in a localization of the integers obtained by inverting a finite set of integers. The stated prime condition defines a ring homomorphism from this localization into the finite field. Addition, multiplication and each allowed division commute with the homomorphism. Induction over the finite arithmetic sequence proves that every modular output is the reduction of its rational counterpart. The zero rational number maps to zero, so a nonzero modular output has a nonzero rational preimage.

A zero modular output proves nothing about rational vanishing. It is recorded as unresolved unless a separate exact calculation settles it. Trying another prime can produce a nonzero certificate, but agreement at several zero residues alone remains inconclusive.

## Arithmetic and reproduction safeguards

Each modulus is checked to be prime. Every input denominator, Q, nonlinear divisor and Poisson divisor is checked before inversion. Low-order and first-obstruction coefficients are compared with retained exact rational Cartesian calculations. Independent polar residues are compared when the theory part publishes them. The scan stores an output hash of the full final density vector and the actual elapsed time for each completed point, while retaining the small nonzero residue itself. The reader should use the completed manifest, not an intended maximum order, to identify the proved finite set.

The theory part's int64 polar implementation also needs an overflow check separate from this proof. At Q<=120 and B<=20, each raw convolution sum has at most B floor(Q/2)+1 terms, each at most (ell-1)^2. For ell<2^25 their product is below 2^63-1. The subsequently reduced scalar products and differences also fit. This bound applies to the two stated profiles and finite grid only; it does not justify arbitrary higher bandwidth or order.

## Completed Cartesian grids

At 2026-10-31T16:39:36Z the exact enumeration audit confirmed 217 Candidate 007 pairs and 2074 single-sine pairs under the stated conditions. Every first compatibility coefficient is nonzero modulo 33554393. The Candidate grid took 299.013 seconds; the single-sine grid took 278.898 seconds. Full final-density vectors agree with retained rational computations at 3 Candidate points and 37 single-sine points. The first 155 available independent polar Candidate results all agree; the remaining polar comparisons are pending. These are finite-grid results, with no assertion about unsampled parameters or the enormous first exceptional order of the stored Candidate parameter.

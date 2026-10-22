# Independent saved-record and rational exponential audit

This supplement precedes audit.py. The first complete checker passed all selected input identities and 6264 F-box containments. This second audit imports neither that checker nor any producer routine. It rechecks every saved F record by a separately assembled signed-frequency map, and replaces the two interval-library exponential evaluations by an exact rational series bound at each of the same three left endpoints.

For a finite binary64 with sign bit s, exponent field e and fraction field f, its exact value is (-1)^s f 2^(-1074) if e=0, and (-1)^s(2^52+f)2^(e-1023-52) otherwise. Exponent2047 is rejected. This gives an integer-bit decoder separate from the first checker's Fraction.from_float conversion. Every selected coefficient and radius is decoded this way. The two signed-zero encodings represent the same rational zero.

For each input a_m, enumerate the four odd signed frequencies 1+2m, 1-2m, 3+2m, 3-2m. A signed frequency with j=(abs(freq)-1)/2 contributes sign(freq)/8 to H_j. It contributes to F_(j+1) with weight (4-2(j+1))/2 and to F_j with weight (4+2j)/2, omitting output modes outside1,...,261. Its differentiated contribution has weight1/2 to both permitted outputs. Collect by input m separately for algebraic and derivative coefficients. This constructs the full linear map without the first checker's closed H formulas. The exact image interval is obtained from its collected center and sum of absolute weighted radii. Compare every reconstructed image endpoint, target endpoint and minimum margin with all6264 ordered saved records, including all zeros and boundary modes. A complete newline-terminated stream, exact record order and the pinned stream SHA are mandatory.

For a rational q>=0 and N=128 put

S_N(q)=sum_(k=0)^N q^k/k!,
T_N(q)=[q^(N+1)/(N+1)!]/[1-q/(N+2)].

If q<N+2, the positive exponential series remainder is between0 and T_N(q), because successive positive omitted terms have ratio at most q/(N+2)<1. Thus S_N(q)<=exp(q)<=S_N(q)+T_N(q). This follows directly from the absolutely convergent exponential series and the geometric sum bound. For x<0 apply it to q=-x and invert the positive bounds to obtain

1/[S_N(q)+T_N(q)] <= exp(x) <= 1/S_N(q).

For x>=0 use the direct bounds. At q=0 both bounds equal1. All operations here are exact rational operations. The auditor verifies q<32, a stronger sufficient ratio condition for this chosen N, and checks the whole rational interval against the saved E interval. This gives an independent check of E membership without Arb, mpmath or any unbounded series truncation.

The first actual Opus5.5 proof review, request a80e84e3-5b0b-4306-8c8c-2ed2a167b331, confirms the composition and identifies accepted endpoint conventions as a dependency. Those conventions are in the current hashed topic98 dependency set, including middle_residual/PROOF.md and modal_green/PROOF.md. The new checker verified all936 inherited pin assertions. Its direct A/B slice comparison preserves their dimensional exp(4t) normalization; no scaling is inserted. This supplement resolves the review's bookkeeping qualifications without changing the reviewed proof.

Two initial attempts were rejected before writing any comparison record: the inherited dependency allowlist omitted three sibling numerical files, and mpmath's installed GMP backend stores its exact integer mantissas as mpz rather than Python int. Both original source versions, failure records and the empty second stream are preserved. The final checker admits exactly the four inherited sibling paths for read-only hashing and converts a nonnegative exact integer mantissa with int after checking equality and finite bit-count/exponent fields. These corrections introduce no numerical tolerance.

The final claim still requires an actual-output review and a separately later verifier adjudication. This audit does not rerun the inherited radial coefficient/remainder theorem, full A/B integration or full T reconstruction. All scope limits in PROOF.md remain mandatory.

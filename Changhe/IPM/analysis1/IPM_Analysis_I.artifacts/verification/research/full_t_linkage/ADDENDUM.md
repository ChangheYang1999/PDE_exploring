# Acceptance details following the proof review

The actual Claude Opus5.5 proof review completed 2026-10-21T03:48:08Z,
request ed9ffa84-9f88-4c12-bf8a-69c613551d12. Its angular reconstruction,
counts and interpolation checks agree with the independent derivation.
Its acceptance is conditional only. The following clarifications apply.

The knot array has 1573 entries, S has 1565 columns, so the difference is
exactly degree plus one. All entries are finite exact dyadics. The knots
must be nondecreasing. Every active index ell satisfies 7<=ell<1565;
therefore ell-7>=0 and ell+8<=1572. Nonempty spans must match the accepted
archive and exact partition in order, with contiguous child indices and
positive integer counts summing to7809. These assertions were already
included in the first checker draft; they remain mandatory acceptance
conditions. The final de Boor vector means d_7.

The original numerical producer calls sub_taylor(ci), documented and
implemented as Taylor coefficients [q][m] at the exact child-left shift.
Our target interpretation is explicitly (cell,power,mode). This source
reading is provenance, not proof of the numeric arrays. The full proposed
coefficient check certifies that exact interpretation. Manufactured
polynomials will separately distinguish coefficient order from derivative
order and distinguish every mode and polynomial power.

Decode input hexadecimal strings as exact powers of two and independently
compare with their finite float64 roundtrip. Form target endpoints using
exact rational addition and subtraction. Check Arb finiteness and convert
its directed lower and upper dyadic endpoints exactly before comparisons.
This does not assume that an Arb hull of rational endpoints is minimal.

For manufactured exact polynomials, on a single clamped span use
B_(i,7)(z)=binom(7,i)z^i(1-z)^(7-i). The control values for z^k are
binom(i,k)/binom(7,k), with zero if i<k. Indeed their Bernstein sum is
z^k times the binomial expansion of (z+(1-z))^(7-k). By linearity the
control values for sum_k Z_k z^k are the corresponding finite sum.
Choose nonconstant and mode-distinct rational Z coefficients, reconstruct
them exactly and compare every coefficient. This yields analytic expected
answers without calling either spline reconstruction under test.

The review's notation "T subset canonical trial" is not used here.
The claim is that each exact trial coefficient belongs to its T box.
The entire product of T boxes does not describe one exact spline, and
cannot be assumed to preserve correlations. The finite-input radial
lemmas are valid for whole input boxes, which is why componentwise
membership is sufficient for their use. Such membership alone does not
certify the radial lemmas for cells not checked in topic93.

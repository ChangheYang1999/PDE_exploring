# Coordinate convention, finite endpoints and external dependency

Added2026-10-21in response to actual Opus5.5 review C1-C3.

C1. The pinned cert_forcing.BiTM class specifies the polynomial
sum c[q,p] sigma^q phi^p. Its from_sigma method assigns coefficients to
c[:,0], and from_phi assigns them to c[0,:]. No rescaling occurs in these
constructors. The pinned tm_exp recurrence starts at1 and multiplies by
gamma/i at step i, so its coefficients are gamma^i/i!, independent of h.
The angular generator likewise divides the corresponding trigonometric
derivative by j!, without multiplying the coefficient by w^j. Those
powers occur only in remainder and supremum bounds.

Recentre.many translates the first index by the matrix entries
binom(i,j) a_s^(i-j), then the second by binom(i,j) a_p^(i-j). The resulting
variables are sigma'=sigma-a_s and phi'=phi-a_p. There is no division by
H or W, nor a radial half-width shift. The fixed leading coordinate is
only the batch index. MR.__init__ and __getitem__ preserve these array
indices; they introduce no coordinate transformation.

The topic120 generator takes ta to enclose the canonical t_i, models
exp(ta+sigma), forms angular models about theta_c, and uses the exact
intended shifts a_s=bsH and a_p=-w+(4bp+2)wk. Thus the physical expansion
point is T=t_i+bsH, A=theta_c-w+(4bp+2)wk, with the unnormalized variables
used in PROOF.md. The new convention checker extracts and pins the actual
source bodies, their line numbers and the relevant generator assignments.
The source interpretation is also consistent with the completely
independent checks of the resulting arrays against Q_p. The mathematical
inclusion concerns those explicit arrays and variables regardless of how
one might relabel them; this linkage is needed for downstream use.

C2. The first iv decoder did not reject the special internal encodings
for infinities and NaNs. The revised check_iv_finite.py checks the sign,
nonnegative mantissa and bit count, the exact zero encoding, and the
finite nonzero mantissa's bit length before conversion. It also verifies
rejection of all six lower/upper endpoints of inf, -inf and nan. Every
endpoint used in the actual finite check is subjected to this guard.
The original checker and output remain unchanged as review history; the
repaired output and audit are authoritative for the independent iv claim.

C3. The inherited pin map includes the read-only external file
numerics/data/cert_green.npz,
SHA256 c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1.
Reproducing the full inherited rehash requires this file at that location,
or an explicitly identified relocation with the same bytes. It is not
copied into this lane because it is290862339bytes and the shared disk is
constrained. The actual topic121 finite geometric checks use the saved
arrays, exact partition and source bracket; the Green file is a provenance
dependency of the contemporary generator, not a new analytic assumption.

All factors in any later pointwise composition must refer to the same
fixed p. Uniform interval bounds allow dependence among them and do not
replace p by separate physical parameters. The value-only and historical
scope restrictions in ADDENDUM.md remain mandatory.

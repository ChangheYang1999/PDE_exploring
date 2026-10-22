# Scope and provenance clarifications after the first Opus review

The actual Opus 5.5 review ended 2026-10-21T00:09:48.769547Z. It accepted the
mathematical criterion and requested the missing flow source and tighter
provenance. The review was given only the Green partition generator, residual
source and MR arithmetic. Its inability to check the omitted flow source is
an input omission, not evidence that that source is absent from this lane.
The closure bundle includes the frozen `cert_flow.py` in full. Lines defining
`cell_iter`, `mu_interval_mr`, `psi_tms` and the module constants specify the
operations reconstructed by the producer.

The two original complete computations passed. Their counts concern every
cell, not a sample: 19389 scalar rows, 19392 partition points, 523503 power
comparisons (27 per cell, including exponent zero), 38778 reciprocal endpoint
comparisons, and 444 rational constants. The fresh checker imports neither
the original checker nor the source MR class. The supplemental checker below
adds the provenance and stronger endpoint checks requested in review.

## Additional finite obligations

The supplementary check reads the NPY headers inside the hashed Green files
and verifies A_mid, A_rad, B_mid and B_rad have shape (nc+1,261) in each
region. It also reads hsub and verifies its exact stored value is the
binary64 value of 0.0019; the source's ceil(17/hsub) and ceil(5/hsub) give
8948 and 2632. The exact rational partitions are defined by those endpoints
and counts and every exported ball contains the resulting point. This
establishes a valid partition from current inputs. It does not reconstruct
an absent historical command line or certify the Green moments at the
partition points. The base radii are checked to be zero; base times are
compared as exact rationals to the first and last trial knots and the
middle partition endpoints.

In addition to the exact-cell endpoints tested in the first two runs,
the supplementary check requires rlo <= E.m-E.r and that exp of the
entire exported end-time interval is <= rhi. Its lower end check and the
previous full start-time exponential inclusion also show that rlo is below
the full exported start-time image. It verifies the actual rounded
succ(522*h) <= 1, so the floating value passed into the positive-rate ODE
majorant lies in the intended range. These are additional finite
comparisons. No general assertion about correctly rounded library powers
is required.

## Precise exclusions

The result covers only the explicitly listed scalar expressions and the
partition geometry. It does not certify any other scalar expression or
composition merely because it appears nearby in the source. In particular,
remaining obligations include the MR products E^2,E^3,E^4 and I^2 as used in
full models; `m_ta` and `wfar_ta`; the polynomial translation and `mr_powers`
computations inside Bernstein evaluation; exported exponent radii and
re-centred polynomial coefficients; the powers and inflation factors inside
`tm_exp`, `ode_tm`, and derivative majorants; matrix products; residual
integration constants; and every analytic and numerical remainder needed
for the full field. Generic lemmas from other topics can be dependencies
of a later full audit, but are not imported as a blanket acceptance here.

The review called `arb(m,r)` an exact dyadic ball. More precisely it is an
Arb enclosure of the exact dyadic interval [m-r,m+r]; its internal radius
may be enlarged by Arb's magnitude representation. The checks compare
fresh complete enclosures of the mathematical dyadic interval against the
saved MR interval. Thus the mathematical containment does not rely on an
assumption that Arb represents the initial radius unchanged. Likewise,
`float(arb.mid())` and `float(arb.rad())` are reconstruction operations whose
outputs are subsequently checked as exact dyadics. The runtime is recorded,
but no historical runtime is inferred.

All 19389 reconstructed pairs (rlo,rhi) happened to match the recorded flow
JSON pairs bit for bit. This is useful provenance evidence. The independent
mathematical endpoint containment, rather than the bitwise equality, is what
certifies the finite radial geometry. No flow inequality follows yet.

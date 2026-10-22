# Two tighter quadrature secant runs: independent verification

Written 2026-10-22T06:37:38.810018+00:00. The finite comparisons below are CONFIRMED, with explicit numerical limits. Both literal archives are REFUTED as B2 profiles by exact nonzero center defects and whole-plane tail obstructions. General B2 remains OPEN.

The complete proof preceded computation. Two primary fields and16supporting inputs were frozen at 2026-10-22T06:26:26.200454+00:00. The single sequential pipeline completed06:31:15Z. Full-plane PDE evaluation took 275.280284s. The separate exact-tail and saved-stage consumer passed141/141 in0.286183s. Its first attempt stopped on missing start_sha256 metadata in a secant archive; the correction checks each secant's source coefficients and geometry directly, retaining final-archive restart hashes. Original code and the correction are preserved.

## Finite scalar comparison

Both logs use beta3.062, K32, angular sampling parameter Nphi64, radial parameter Nt56, native source basis3, initiallambda0.93171, inner tolerance3e-6 and outertolerance1e-7. Each run has four scalar trials0..3 with positive and negative first two mismatches, followed by two secant updates. All inner solves report fixed-point convergence; final saved arrays match secant3. Exact-binary secant arithmetic agrees within1e-14 with the saved lambda values.

| Nominal Gauss order | Saved lambda | Logged final m | Exact saved forced m, rounded | First-pair finite slope |
|---|---:|---:|---:|---:|
| 12 | 0.9316837662265695 | 3.75550390785e-09 | 4.15668908577e-09 | 9.87976458037 |
| 48 | 0.9316837838279398 | 4.24514201569e-09 | 4.72039655825e-09 | 9.8800018758 |

The exact difference lambda48-lambda12 is 79269525/4503599627370496, or 1.760137036121989e-08. These are two computed finite secant states. Their mismatch signs do not supply continuity, interval evaluations, a scalar root enclosure or discretization convergence. The unknown fields change while the source block and geometry remain bitwise unchanged. Both lambda values differ from the older stored value. The quadrature orders are verified from frozen logs, not archive metadata, which omits them. Both saved exact forced mismatches are nonzero and below the nominal outertolerance. They differ from the logged last pre-update values by about4e-10 to5e-10.

## Independent defining PDE, center and full plane

The defining velocity is W=beta X+B[Omega], with the canonical full-plane relative inverse. The separately labeled forced calculation adds lambda B[f] in its native basis. Our own evaluator uses adaptive physical-radius Green integrals through infinity and seven-point Cartesian differences, with no numerical-lane code imported or executed. It evaluates15,456points,161radii from1e-5to1e8, both x signs and both axis directions. Two Cartesian steps give at most2.768938967e-10 change in these normalized maxima. This is finite sensitivity, not an enclosure or supremum certificate. The physical Cartesian normalizers and divided normalizers are distinguished, with no denominator floor.

| Gauss order label | Forced F | Forced G | B2 F | B2 G | Exact self center F ratio, rounded |
|---|---:|---:|---:|---:|---:|
| 12 | 0.06776248014 | 0.108583745 | 0.7295579582 | 0.7436788223 | 3.914020994e-09 |
| 48 | 0.06766750775 | 0.1085507129 | 0.7295579617 | 0.7436684425 | 4.444818995e-09 |

Every exact self center thermal defect is nonzero, so neither represented field satisfies the defining PDE. The Cartesian residual vanishes on the symmetry axis, but its normalized off-axis limit equals the positive divided center ratio proved in PROOF.md. Both fields retain the a0=1.011258 normalization label, and neither approaches zero forcing in this comparison. These are literal-field conclusions, not a nonexistence theorem for corrected profiles.

Exact rational endpoint witnesses establish nonzero H0, ET, DT, EO and DO, including simple source-stream zeros at both axis angles. With3<beta<4, the thermal powers1-3/beta and2/3-2/beta are distinct and positive, above the decaying remainder1-4/beta. The absolute whole-plane thermal residual is therefore infinite for both the defining and forced equations. The representation covers the whole plane; the map scale is no physical boundary.

| Gauss order label | Certified C2 interval | Raw objective |
|---|---|---:|
| 12 | [-4979.102, -4979.101] | 3370.37801903 |
| 48 | [-5148.985, -5148.984] | 3386.36049653 |

The noticeably different C2 values are exact certificates for two stored fields. No continuum value or convergence rate follows. All radial bands, absolute and normalized residuals, maximizing points and input hashes remain in verification/. This audit does not reproduce the numerical lane's runtime interpolation or establish its error. P291 separately checks finite runtime-norm comparisons with conditional scope.

## Verdict and dependencies

CONFIRMED: literal archive provenance, four secant trials at each nominal order, exact saved scalar difference, nonzero center defects, exact tail obstructions, and negative inverse constants. CONFIRMED as finite floating-point observations: sampled PDE residuals and step sensitivity. REFUTED: either literal archive as an unforced B2 profile. OPEN: continuum root displacement, convergence, rigorous finite-grid error bounds and general smooth B2 existence or nonexistence. No decisive endpoint or T_end is declared.

The defining B2 criterion is zero Cartesian PDE residual for the continuous field determined by exact stored binary coefficients and the canonical inverse. Tail remainders in PROOF.md hold uniformly along rays. Actual Opus5.5 reviews508,510and511are adjudicated in verification/OPUS_ADJUDICATION.md;507produced no public audit. These reviews verify conditional mathematics and do not endorse unseen data. The proof was copied and frozen for P294at06:26:26Z; earlier printed timestamps identify the inherited P287proof.

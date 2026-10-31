# Verifier derivative standard, version 1

Registered at 2026-10-28T20:35:14.257781+00:00, before running numerical derivative tests. This is the verifier's provisional standard; the lead's campaign standard will be checked before issuing the production verdict.

For a reference derivative d and a centered difference d_h, report the absolute Euclidean norm of their difference and the relative error ||d-d_h||/max(||d||,||d_h||,1e-30). Keep separate near-origin, core/intermediate and far-field groups so large core values do not conceal a far-field defect. Also record maximum component error.

The primary physical-parameter step sequence is h=1e-3,1e-4,1e-5,1e-6,1e-7. Reject steps outside the open parameter domain. At least three usable steps must be recorded, together with finite-difference successive changes. When the derivative is zero by symmetry, use an absolute error and record the scale; do not divide by a tiny reference and label the result a failure or success without context.

- Field U and DU, source tr(DU²), explicit momentum identities and complete smooth objective: require a best relative error at most 5e-6 and a visible second-order region or a justified roundoff plateau. The objective test includes both parameter columns and mixed coefficient/parameter directions. The full objective must be freshly recomputed at each perturbed point.
- The minimum test floor for scaled field quantities is 5e-10 times the norm of their undifferentiated physical scale. Passing solely through this floor is recorded as an absolute test, not a relative test. No pressure accuracy conclusion follows from this derivative floor.
- For a ratio of steps of ten, a truncation-dominated second-order region has an error reduction near 100. Ratios from 20 to 500 will provisionally count as consistent; otherwise inspect the reference error and smaller-step plateau rather than automatically passing.
- Independent analytic formulas against at least 50-digit scalar arithmetic: require relative error at most 1e-10 for double-precision values with ordinary conditioning; record significant cancellation and absolute scales separately.
- Spatial consistency: compare supplied DU to centered finite differences of U at fixed coefficients and parameters, with Cartesian displacements scaled to radius. Require best relative error at most 5e-7 in each radial group; a failure prevents treating pressure from that source as independently validated.
- Pressure differentiation: verify the source and both interior and exterior integrals. A matching derivative of an inaccurate pressure discretization is not pressure accuracy. Report quadrature refinements separately and retain their disagreement as an error estimate, not as a proof bound.
- Nonsmooth normalization, clipping or pivot switches require an explicit branch/margin check. Cases on a switch stay OPEN unless a one-sided derivative is the intended method and is tested as such.

At least four parameter pairs, including (0.42,0.3), (0.45,1), a small-omega pair and a large-omega pair, are required for the represented-field battery. Use L=6, nonzero non-axisymmetric modes, original even and unrestricted classes where implemented, all active correction channels, at least two existing Degree 6 lineages, origin/axis points and logarithmically spread radii. Random seeds, inputs, code hashes and timings are saved with results.

A test failure is investigated and logged. Standards are not relaxed after seeing final candidate results. This battery is a gate for derivative implementation only and does not change Tier S, R or A.

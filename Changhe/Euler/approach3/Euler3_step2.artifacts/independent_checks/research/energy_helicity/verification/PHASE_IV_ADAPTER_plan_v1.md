# Final energy and helicity adapter

Registered before implementing or running the adapter on a final state. The parent
PROOF.md fixes the mathematical definitions and conditional tail error estimates.
The development S01 plan and V134 already checked this numerical route. Its scope
remains finite quadrature and leading-tail extrapolation, without a certified
infinite-domain error bound.

The adapter takes an explicit completed primary record and verifies its immutable
input checksums. It uses the actual physical parameters and actual leading sphere
amplitude A. It does not renormalize the field. Two rules retain 12 radial nodes
with 40 by 80 angles and 24 radial nodes with 48 by 96 angles. Radial panels run
from zero through R0 times 2^18, with positive dyadic edges beginning at R0/256.
Reported ball radii are R0 times 1, 4, 16, 256, 4096, 65536 and 262144. These are
state-R0 physical domains; their explicit radii are retained for comparisons.

For final use, the two azimuthal offsets are independent draws from a seeded
NumPy default_rng, uniformly between .01 and .99. A domain-separated seed is
obtained from SHA256 of the exact ASCII string
`energy-helicity-v1:<unsigned decimal frozen vorticity seed>`, using its first
eight bytes as an unsigned big-endian integer. This deterministic derivation is
bound before the final cohort entropy is drawn. It requires no later entropy
and does not change the already qualified cohort manifest. A legacy mode keeps
.347 and .617 only for development replay; the final wrapper always selects
fresh mode and refuses test cohorts.

The driver stores leading velocity and curl, angular weights and directions,
radial nodes and weights, per-sphere moments and cumulative integrals. The scalar
auditor recomputes every coefficient, ball integral and reported correction from
these arrays. It checks all arrays for finiteness, all quadrature weights for
positivity, the exact selected radii, and geometry against separately generated
binary64 Legendre nodes and explicit trigonometry. Geometry tolerances are
4e-14 absolute for directions, 3e-14 relative for positive radial nodes, and
5e-11 relative for quadrature weights. The relatively loose weight tolerance
compares two independently rounded root-solving algorithms and is not a bound
on the integral. Existing scalar reporting tolerances remain 2e-12 relative and
2e-13 absolute. The scalar radial primitive control retains its 1e-11 absolute
threshold. Zero absolute helicity returns null for the signed-to-absolute ratio;
it must never produce a finite diagnostic from division by zero.

Before final use, synthetic and refusal controls must pass. The generic driver
then replays S01 in legacy mode. All unchanged numerical quantities and saved
arrays must agree with the previously checked result to 1e-12 relative, with a
1e-25 denominator floor, and the expanded scalar audit must pass. The replay is
bounded by 900 seconds and the scalar audit by 30 seconds. Qualification records
bind all source files. Any subsequent source change requires a new qualification.
Final execution uses the common one-worker lock, checks the frozen primary
against the selected state, limits the whole operation to 1200 seconds by
default, and stops before the registered numerical cutoff. Qualification or
final runtime exhaustion is reported as incomplete, never as a scientific
failure of the state.

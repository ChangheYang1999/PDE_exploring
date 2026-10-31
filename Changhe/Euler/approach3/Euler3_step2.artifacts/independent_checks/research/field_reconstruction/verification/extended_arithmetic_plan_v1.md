# Extended arithmetic implementation plan

Registered at 2026-10-29T00:00:10.277376+00:00.

The next independent route will evaluate fixed full exchange coefficients using NumPy long double on CPU35. It will record the actual mantissa precision; the dtype name alone will not be called binary128. The source chain will include radial jets, normalized solid harmonics, Cartesian U and DU assembly, tr(DU^2), angular analysis, and radial Green sums. The same finite-basis and full-space identities are proved in field_reconstruction, normalized_angular_recurrence, and green_edge_recurrence. No source moments are set to zero. No production imports, coefficient projection, rescaling or refitting are permitted.

The first implementation stage supplies U, DU, and the stable linear operator. It is diagnostic until its tests pass. It uses long-double trigonometric functions and recurrence coefficients rounded from 70-digit decimal values. Unit directions are normalized in the working arithmetic; their input values and the normalization policy are recorded.

Before examining results, qualification will require normalized angular absolute errors <=2e-16 against the existing 70-digit recurrence on the recorded directions, U and DU norm errors <=2e-14 against 70-digit fixed-full-field reconstruction, and stable-linear error <=2e-6 of ||U||^2/r at far points. These numerical checks are not error enclosures. Every individual error and reference magnitude will be retained. A failure prevents use as an extended-precision reference until diagnosed and separately rerun.

A complete extended far check will use at least256 points in each of the three registered far checkpoints. Field-only high-precision checks and higher-precision summation of float64 source samples are not equivalent to recomputing the full pressure chain. Those partial results must be labelled explicitly. Pressure refinement and the 10 percent agreement test for rho_nl and pi_nl remain required.

# Equation summary v1.5 audit

Date: 2026-10-23T07:32:08.366816+00:00. Source SHA256: **897a4196960f34c054eb384776c7857df09b3af592429b79db248312924e5646**. Snapshot: `snapshots/EQUATIONS-897a4196960f34c0.md`.

The five section 9.3 findings and the section 7.2 Fourier classification defects from v1.4 are repaired. Canonical profile identities remain CONFIRMED. The representation completeness and numerical gauge implementation checks remain OPEN where previously stated; a correct equation document does not certify a numerical checkpoint. Full current derivation records are in `evidence/equations_audit_current.json`. Historical findings remain in EQUATIONS_V14_AUDIT.md.

| Check | Verdict | Method and result |
|---|---|---|
| 7.2 rejection list, force interpretation | CONFIRMED | Constant velocity with its linear pressure remains an unforced exact solution excluded by global decay. The corrected spectral parentheticals are checked separately. |
| 7.2 spectral parentheticals | CONFIRMED | All nonzero cylindrical modes must vanish for axisymmetry. Four-fold symmetry requires every occupied frequency to be divisible by four. The text explicitly says E2=0 alone is insufficient. These agree with section 3.3. |
| 9.3 spectrum wording | CONFIRMED | The summary now correctly allows a conjugate eigenvalue pair with negative real part. Its rank-two specialization gives two simple nonzero real eigenvalues of opposite signs, as the independent spectral proof requires. |
| 9.3 local zero-set wording | CONFIRMED | The local zero set is correctly described as an isolated point or a closed subset of a C2 arc. The connected-alpha argument, rather than the implicit function theorem alone, supplies an equilibrium subarc. |
| 9.3 sublinear conclusion | CONFIRMED | No nonconstant sublinear profile and no nonzero decaying profile are the correct conclusions. The exact nonzero constant solution with P=-(1-c)b dot y is explicitly retained. |
| 9.3 growth scope | CONFIRMED | The exclusion list now refers to velocity without sublinear growth, including nonconstant affine backgrounds. Unbounded sublinear growth is included by the theorem. |
| 9.3 relative-residual implication | CONFIRMED | The implication now requires true whole-space absolute L-infinity momentum residual tending to zero within a fixed globally controlled class. Relative norms require a specified bounded denominator and global norm. Sampled relative loss and a decrease to a positive floor are explicitly insufficient. |
| 9.3 L2 exact theorem | CONFIRMED | The exact C2, uniform-sublinear theorem is independently proved. It excludes the primary decaying class for 0<c<1/2 and imposes no zero-set hypothesis. The c=1/2 control remains outside the result. |

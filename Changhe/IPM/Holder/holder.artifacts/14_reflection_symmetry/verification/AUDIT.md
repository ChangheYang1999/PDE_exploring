# Independent checks of the reflected-copy argument

The statement concerns the full output seminorm, including pairs far
from the symmetry axes. A fixed pair at the origin would not permit
the translation used in the proof.

1. Character law: chi(epsilon delta)=chi(epsilon)chi(delta), and
   Q_epsilon Q_delta=Q_(epsilon delta). Reindexing the four summands
   proves both prescribed coordinate parity relations exactly.
2. Supports: their centers are (+-L,+-L); the minimum center separation
   is 2L. Ball radii R therefore give the stated 2L-2R lower distance.
3. Seminorm: points in a common ball or outside all other balls can
   be compared using one entire reflected translate of f, whose
   seminorm is M. Distinct balls require (1); no factor four is lost.
4. Smoothness: the original f is globally smooth with compact support,
   so every reflected translate and the finite sum are globally smooth.
5. Kernel derivative: radial and angular components of grad K_xx are
   -cos(2theta)/(pi r^3) and -sin(2theta)/(pi r^3). For K_xy these become
   -sin(2theta)/(pi r^3) and cos(2theta)/(pi r^3). Both Euclidean gradient
   magnitudes equal 1/(pi r^3).
6. Remote integrals: separation holds for every point of the entire
   evaluation segment, not just its endpoints. Differentiating under
   the compact remote integral is justified by that positive distance.
7. Local term: remote summands vanish at both evaluation points. Hence
   the same error bound applies to T_xx-I/2 without changing signs.
8. Supremum order: first fix f,p,q and send L to infinity; only then
   take suprema. No uniform approximation over all test functions,
   global Holder-density claim, or extremizer attainment is needed.

All checks pass by direct algebra and the displayed estimates. This
file is analytic verification evidence, not a numerical certificate.

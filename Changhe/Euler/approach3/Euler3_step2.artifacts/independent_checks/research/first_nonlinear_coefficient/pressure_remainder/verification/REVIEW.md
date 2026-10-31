# Mathematical review

Reviewed 2026-10-29T23:48:38.009253+00:00.

Claim: the exact finite representation has grad(P-P0)=O(r^-4), without a first tensor moment. The derivative and homogeneous-pressure conventions match the parent proof.

The proof uses an L1 tensor difference R=U tensor U-U0 tensor U0. Its origin singularity is integrable only because 2alpha<3; its tail is integrable only because 2alpha+1>3. The local differentiated-kernel part uses two spatial derivatives of R away from zero. These hypotheses are explicit.

Checks: the Newton Hessian contains -delta_ij delta_0/3; its annular mean is zero. The third-derivative bound is 6/pi. The cutoff has gradient at most15/r and Hessian norm below512/r^2. The local coefficient is bounded by3260 and the exterior coefficient by8192; the three-component norm is below16384 times A+B. The singular point at the tensor's origin is outside the kernel's local ball for r>=2. Homogeneous harmonic ambiguities are eliminated by nonvanishing of every spherical denominator, not by imposing a numerical moment. No first moment is used.

Scope: analytic decay only, with A+B not evaluated for any state. No claim of a sharp nonzero leading correction, no finite-radius certified error, no discretization validation, and no Euler existence claim. The registered numerical sources and parent proof are unchanged. A new the review of this complete argument is pending.

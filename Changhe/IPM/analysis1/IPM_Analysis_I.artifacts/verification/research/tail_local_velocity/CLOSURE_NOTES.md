# Center-regularity correction and final adjudication

Read PROOF.md with ADDENDUM.md and this correction. The original proof and
provisional publication are retained unchanged. FINAL_PUBLICATION.md and
 evidence/verdict.json provide the current status.

## Mandatory correction to PROOF section3

Replace the assertion that rho0 is locally C6 by the following argument.
The exact inner density is x^2y plus a finite sum of terms
r^(2j+3) A_j(theta), j=1,...,7, and terms
r^(bi+3)(log(r/Rminus))^ell B_ell(theta), ell=0,...,6, with bi>4.
All angular functions are finite trigonometric polynomials. For a smooth
angular function A, Cartesian derivatives of order m of r^d A(theta)
are r^(d-m) times smooth angular functions. The same statement with a finite
logarithmic polynomial holds for the faster terms.

For m<=4 the first nonpolynomial degree-five terms are O(r^(5-m));
the other terms decay faster. These derivatives tend to zero at the
origin. Extending the function and these derivatives there gives a C4
function: induct on derivative order, integrating the next derivative
along a line segment through the origin. The uniform vanishing estimate
supplies continuity and the required difference quotients. Thus rho0 is
C4 locally at zero; away from zero the existing joins are C6.

This regularity cannot be upgraded to C5 for the exact input. In zero-based
array indexing D[259,0]=6648046164061931/2^113 is nonzero. The mathematical
coefficient D_(259,1) therefore contributes

 D_(259,1) r^5 sin(521 theta)/(8 Rminus^2).

No other degree-five input mode reaches frequency521. Higher radial
powers and the faster logarithmic row are o(r^5). If rho0 were C5,
its degree-five homogeneous Taylor polynomial would equal this whole
leading correction. A homogeneous Cartesian polynomial of degree5 has
angular frequency at most5, a contradiction. The normalization changes
no degree-five coefficient. The exact witness was checked directly from
both JSON and the original NPZ.

Only C3 density regularity is required for the claimed residual convergence.
On every fixed compact K and all sufficiently large T the correction
vanishes identically, and F(rho_T,c0)-F(rho0,c0)=u_T dot grad rho0.
The Leibniz formula through order2 is bounded by a finite constant times
||u_T||_(C2(K)) ||rho0||_(C3(K)). The proved C3 velocity bound implies
C2 residual convergence at rate O(T^(2k-4)). The canonical Poisson solution
has the required local regularity: rho0 in C4 implies rho0_x locally
C^(2,alpha) for0<alpha<1; interior elliptic regularity gives U locally
C^(3,alpha), which suffices. No fifth center derivative is used.

## Review and arithmetic adjudication

Claims1 through4 are confirmed as written. The higher-tail convergence
claim is confirmed with the correction above. Its numerical constants are
not claimed here. All scalar and source endpoint checks in the original
193-file audit remain valid. An independent referee's Arb384/iv100 script
was replayed in this lane and reproduces all mathematical output and all186
dependency pins exactly, differing only in its UTC stamp.

The lead's notes/fr111/check_constants.py sums400 positive series terms
but does not add its tail to the quantity used in its displayed bounds.
That calculation is treated only as a diagnostic. It does not certify an
upper bound by itself. Our independent exact generating-function sums,
proved positive-tail audit and the referee's rational checks do certify
the stated constants, so this limitation does not alter the conclusion.

The lead reconstructed the Green cancellation, compensation, scaling,
Cartesian derivatives and source identity, and accepts the claims with
this center correction. The lead identifies its model as Opus5.5 and its
launch log configures us.anthropic.claude-opus-5-5. No raw actual provider
response metadata for that team process is available. The additional
Astra referee is GPT6. Its own Opus attempt failed before invocation.
The direct request from this lane returned actual claude-opus-5-5 metadata
with a refusal and no mathematical text. That is an unavailable review,
not acceptance; it remains archived unchanged. No substitute is asserted.

## Scope

The component and derivative estimates concern the exact specified repairs.
P is the original source and need not be a source of the changed velocity.
The single-tail source derivative is nonzero for every admissible T. No
surrounding neighborhood is excluded. The qualitative higher-tail result
gives no global residual norm ceiling or inverse. No IPM endpoint follows.

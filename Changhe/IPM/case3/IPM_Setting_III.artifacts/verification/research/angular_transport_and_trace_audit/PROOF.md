# 166. Trace zeros and the angular transport equation

Independent audit, 2026-10-21. The trace conclusions below are alternate proofs of existing report results 3.30(vii) and 3.33, not additional restrictions on the primary class.

## Statements and dependencies

Let rho be an exact primary Setting III profile, a=rho_y(0) != 0, ell>1, p=1/ell, W=ell X+U and Theta its smooth far-field trace. Assume H-dyn, meaning W has no zero except 0. The already audited global-basin theorem 3.22 gives rho/(a y)>0 off the horizontal axis and rho_y(x,0)/a>0 on it. The already proved exterior scattering formula (verifier 162) gives, for every sufficiently large fixed r,

r^(-p) rho(r,theta)=b_r(theta) Theta(H_r(theta)),

where b_r>0 and H_r is an orientation-preserving circle diffeomorphism. Then Theta/(a sin theta)>0 off the horizontal axis and Theta'(0)/a>0. Consequently its only zeros are the simple horizontal-axis zeros, and the angular zero set has measure zero. The theorem is conditional on H-dyn, which is OPEN for the full class.

For any smooth scalar rho and vector field U, put L=-y partial_x+x partial_y, v=L rho and E=(ell X+U).grad rho-rho. On r>0,

W.grad v = (1-(partial_theta U_theta)/r)v -(partial_theta U_r)rho_r + partial_theta E.

For an exact profile E=0. Inherited parities give v odd in x and even in y; near 0, v=x(a+O(r^2)). The identity alone gives no sign preservation because the inhomogeneous term has no established sign.

## Proof of the trace assertion

Both coordinate axes are invariant under W by parity. Their angular velocity is zero in the exterior radial characteristic equation. Hence H_r fixes 0, pi/2, pi and 3pi/2. Since it is an orientation-preserving diffeomorphism it preserves each open quadrant, in particular each open half-plane. Given phi in (0,pi), take theta=H_r^{-1}(phi) in (0,pi). The scattering identity gives Theta(phi)=r^(-p)rho(r,theta)/b_r(theta), whose quotient by a is strictly positive by 3.22. Reflection covers the lower half-plane. Thus there are no other zeros. This argument applies to single zeros as well as zero arcs or positive-measure zero sets; it does not replace positive measure by nonempty interior.

At theta=0 one has Theta(0)=0, so differentiation of the scattering identity gives

r^(1-p)rho_y(r,0)=b_r(0)Theta'(0)H_r'(0).

Each factor other than Theta'(0)/a is strictly positive after dividing by a. Therefore Theta'(0)/a>0. Reflection gives Theta'(pi)=-Theta'(0), so the two horizontal zeros are simple. The smooth quotient Theta/(a sin theta) extends positively to the endpoints; on the compact upper semicircle it has a positive minimum. This recovers the angular part of 3.33 without taking a possibly zero limit of positive values.

No numerical sampling is used to prove this assertion. Its only dependencies are the stated basin positivity theorem and the exact scattering representation, each audited separately. Without H-dyn a nonzero smooth trace can have additional zeros. The statement that a general bounded backward orbit converges to a single equilibrium is not supplied by the fact that all its limit points are equilibria. The proposed normal-form/source-basin continuation argument in ANALYSIS Q is not checked or used here.

## Proof of the commutator

For L=(JX).grad with J(x,y)=(-y,x), direct differentiation gives

L(U.grad rho)=U.grad(L rho)+(L U-JU).grad rho.

The dilation operator X.grad commutes with L because both are linear vector fields and the identity matrix commutes with J. Applying L to E=W.grad rho-rho yields

W.grad v=v+L E-(L U-JU).grad rho.

Writing U=U_r e_r+U_theta e_theta and using partial_theta e_r=e_theta, partial_theta e_theta=-e_r, the vector L U-JU has polar components (partial_theta U_r, partial_theta U_theta). Since grad rho=e_r rho_r+e_theta v/r, this gives the displayed equation. For U=(-psi_y,psi_x), U_r=-psi_theta/r, hence partial_theta U_r=-psi_thetatheta/r. No boundary or integration by parts occurs. Finally L maps an even-x, odd-y function to an odd-x, even-y function; applying it to rho=a y+O(r^3) gives v=a x+O(r^3), with the stronger x factor by parity and smoothness.

At a zero of v the homogeneous term vanishes but the source -(partial_theta U_r)rho_r need not. A maximum principle or characteristic sign argument would need an additional source-sign theorem; none is assumed. Supporting exact polynomial tests check the residual-inclusive identity independently of the polar calculation. No numerical or formal existence claim follows.

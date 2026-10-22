# Independent signed Gaussian source feedback audit

## Exact problem and scope

Let s_i>0, h_i and a_i be fixed real numbers, and prescribe

    omega_e(x,y)=A*x*sum_i a_i exp(-(x^2+(y-h_i)^2)/(2s_i^2)).

Use the canonical whole-plane inverse -Delta psi_e=omega_e, u_e=(-psi_ey,psi_ex), with no affine straining correction. Fix c_in=psi_exy(0)>2, set beta=2(c_in-1)>2, and let

    W_e=beta*(x,y)+u_e(x,y)-u_e(0).

This is a prescribed transport field. Solve W_e.gradTheta=(beta-2)Theta and W_e.gradOmega+Omega=Theta_x by backward characteristics from the center temperature jet a0=1, with b0=4/beta. The scalar feedback is the canonical strain c_out of the transported Omega. Equality c_out=c_in is a necessary strain-matching condition for this starting construction; it is not full B2 consistency or an existence proof. The actual transported velocity is not prescribed u_e unless the fixed-point equations hold. Numerical quadrature and finite-radius center initialization give sampled approximations only.

This packet checks the numerics lane's17 frozen signed two-Gaussian inputs, input normalization, output feedback at independent points and quadratures, and its parity argument. The precise physical PDE remains B2 on the full plane, and these external-source experiments are labeled separately. No numerical candidate is proposed.

## 1. Exact canonical inverse of a Gaussian derivative

For one lobe put S=x^2+(y-h)^2, a=1/(2s^2), and

    B(S)=(1-exp(-a*S))/S, B(0)=a.

All apparent singularities at S=0 are removable by its entire Taylor series. Define psi=A*a_i*s^4*x*B(S). For S>0 direct differentiation gives

    Delta[x*B(S)]=x*(8B'(S)+4S B''(S)),
    8B'(S)+4S B''(S)=-4a^2 exp(-a*S).

Since4a^2*s^4=1, -Delta psi equals the lobe vorticity. Smooth continuation proves the equality at S=0. Its gradient decays at infinity as O(|X|^-2); it is therefore the decaying canonical velocity. Any difference between this and a smooth decaying whole-plane divergence-free field with the same vorticity is harmonic and bounded, hence constant by the mean-value property and zero by decay. Sum these formulas over the lobes. No artificial boundary or unadvertised harmonic strain enters.

The velocity is

    u1=-2 A*a_i*s^4*x*(y-h)*B'(S),
    u2= A*a_i*s^4*(B(S)+2x^2 B'(S)).

The unscaled lobe center strain and drift are, with z=h^2/(2s^2),

    c(h,s)=-2s^4 h B'(h^2)
          =h*[1-(1+z)exp(-z)]/(2z^2),
    v(h,s)=s^4 B(h^2)=(s^2/2)*(1-exp(-z))/z.

Their removable values are c(0,s)=0, v(0,s)=s^2/2. The numerator 1-(1+z)e^-z is positive for z>0, because its derivative is z e^-z>0 and it vanishes at0. Thus c(h,s) has the sign of h. The unit source strain is sum_i a_i*c(h_i,s_i); if nonzero, choose A=c_in divided by this number. A negative lobe below zero contributes positive strain, just like a positive lobe above zero. This proves the normalization explanation without relying on the scan table. The resulting strain is c_in exactly in real arithmetic.

The whole-plane strain integral is

    c=(1/pi) integral_R2 x*y*Omega(X)/|X|^4 dX.

For these smooth Gaussian sources it is absolutely integrable. Near0 Omega=O(x), the integrand has order O(1/|X|); at infinity it decays exponentially. The drift integral is also absolutely integrable. For transported fields the same strain formula is legitimate if the actual tails make the integral absolutely convergent; the numerical compactification samples it but does not prove its tail bound.

## 2. Center initialization and characteristic reconstruction

Set alpha=(beta-2)/2 and mu=1+3beta/2. The center gradient DW_e is diag(alpha,mu). Write A_x(y)=W_e1(x,y)/x near x=0, and let d=partial_y A_x(0). From the velocity formula,

    d=sum_i -2 A*a_i*s_i^4 [B_i'(h_i^2)+2h_i^2 B_i''(h_i^2)].

The first mixed Taylor coefficients forced by transport are

    Theta=x^2*(1+f01*y)+higher order, f01=-2d/mu,
    Omega=x*(b0+g01*y)+higher order,
    b0=4/beta, g01=(2f01-d*b0)/(2beta+1).

These identities follow by equating x^2*y and x*y coefficients in the two transport equations. A finite inner radius uses these Taylor polynomials as initial values and introduces a truncation error; compare decreasing radii, and do not treat the initial polynomial as an exact profile.

Along a forward trajectory X'=W_e(X),

    Theta'=(beta-2)Theta,
    (gradTheta)'=[(beta-2)I-DW_e^T]gradTheta,
    Omega'=-Omega+Theta_x.

Backward integration identifies the inner point and time. Adaptive DOP853, independently implemented analytic velocity/gradient and a forward gradient/vorticity solve then produce the outputs. A trajectory that does not reach the inner sphere within the allowed time is marked unfinished, and no feedback value is assigned from its incomplete data. This is independent of the numerics lane's fixed-step integrator, spline projection and residual grid.

## 3. Half-plane quadrature represents the full plane

The prescribed field preserves x reflection, and the center data select even Theta and odd Omega in x. For an x-odd Omega the strain integrand is even in x. With r>0 and phi in(-pi/2,pi/2),

    c_out=(2/pi) integral integral cos(phi)*sin(phi)*Omega(r cos(phi),r sin(phi)) dr/r dphi.

Thus a half-plane angular quadrature is only a symmetry representation of the full-plane strain; it creates no wall. Set r=L*(t^(-beta)-1), 0<t<1. The positive radial weight is L*beta*t^(-beta-1)/r. Gauss-Legendre nodes in t and phi are different from the fitting grid. Different orders, scales L, inner radii and adaptive tolerances separate sampling/initialization effects. The largest sampled radius is recorded. A finite quadrature, even with a compactification, is not a rigorous tail or operator error enclosure.

## 4. Antisymmetric source and zero feedback

Take equal widths and opposite amplitudes at h and -h. Then omega_e and psi_e are odd in x and y. Its u1 is odd in x and even in y, while u2 is even in x and odd in y; in particular u_e(0)=0. The prescribed W_e has those same vector parities. Reflection y->-y maps each trajectory to the reflected trajectory. Here d=0, and the center data Theta=x^2 and Omega=b0*x are even in y. The gradient transport and vorticity transport equations preserve these scalar parities. Uniqueness along characteristics therefore gives Theta even in y and Omega even in y on the portion of the domain reached from the symmetric center data. This assertion requires that construction and does not assert uniqueness of arbitrary global solutions from a quadratic jet alone.

Where this characteristic solution is defined on the full plane and its strain integral converges absolutely, x*y*Omega/|X|^4 is odd in y, so c_out=0. A symmetric quadrature also cancels paired points, but its cancellation alone would not prove existence or the domain of the transported solution. Since c_in>2, no such fully defined symmetric transported output can have strain equal to c_in. This is a restricted statement about this external-source symmetry, not a full B2 exclusion. The prescribed source and transported output have different y parities.

## 5. Frozen artifacts and verdict protocol

Input JSON and the scan report/table are frozen before new code. The17 frozen signed configurations and2 positive single-lobe controls are distinct from the positive two-lobe incomplete control. Check source signs with explicit witness points and compare A,c_in,beta with a separately evaluated exact inverse. Table counts, ratios and discarded incomplete values are data checks; c_out must be independently recomputed for a substantive verification. The reported fractions of negative grid values remain OPEN without the original point arrays. Evaluate the supplied minimum locations independently to test the existence of negative transported values, without claiming to reproduce their grid fraction or global minimum.

The proofs above are complete before the new code. Numerical verdicts remain OPEN until controls and evaluations finish. The interpretation that changes in the lower-axis conjugacy factor cause the sensitivity remains OPEN unless quantified independently. Continuity of the completed characteristic feedback as source parameters vary is also OPEN under the present evidence. No candidate or endpoint follows from an apparent crossing or its absence.

## Pre-computation source-count correction

At 2026-10-22T00:43:06.176233+00:00, the frozen source manifest was enumerated: it already contains scan_signed_13, 14 and 15 in addition to the report's original 14 signed cases. There are17 signed cases,2 single-positive controls and1 incomplete positive two-lobe control. The last added case (upper center3.5, relative lower lobe -0.03 at -2) reports c_out=2.952385739711153 above c_in=2.5. This value has not yet been independently evaluated. The original14-case absence of a sampled crossing must not be generalized to the extended frozen set. The evaluator will prioritize centers3.3 and3.5. This is a correction of the source count, not a mathematical change. The first proof is preserved in verification/PROOF_initial.md.

## Initial controls and source interpretation

At2026-10-22T00:43:09Z the initial run passed193/236 checks. All193 internal controls passed; the remaining43 were comparisons with the numerics lane:20 exact amplitude equalities,20 exact unit-strain equalities and3 negative-value witness assertions. Static inspection of scan_eps0_signed.py lines50--59 confirms that the lane first fits the Gaussian source and sets A using the fitted strain. Its inverse is consequently the inverse of the fitted source. Our evaluation is the literal Gaussian source with its exact canonical inverse. The differences in A are retained, not hidden by relaxed assertions. The reported G_min_at pair is(radius,y), as independently confirmed by lines70--79. At those3 Cartesian points, our transported G is positive. The original code and failed comparison data are preserved. This disagreement can arise from projected-source derivative errors or integration/reconstruction differences, and requires further checks. It does not invalidate the193 manufactured/internal controls or authorize a claim that our finite computation is a proof. The priority feedback computation proceeds for the literal Gaussian data.

## Additional check: transported gradient in independent state coordinates

Before the follow-up computation, derive a second forward transport state on the same exact inverse and independently integrated backward orbit. For x>0 set P=Theta_x/x, Q=Theta_y/x^2, G=Omega/x, v=W1/x. Differentiating W.gradTheta=(beta-2)Theta gives along a forward orbit d(gradTheta)/dt=((beta-2)Id-DW^T)gradTheta. The product rule, x'=vx, and Omega'=-Omega+Theta_x imply exactly

    P'=(beta-2-DW11-v)P-x DW21 Q,
    Q'=(beta-2-DW22-2v)Q-(DW12/x)P,
    G'=-(1+v)G+P.

At the inner endpoint use P=2(1+f01*y), Q=f01, G=b0+g01*y, consistent with the same first-order center jet. Reconstruct Omega=xG and gradTheta=(xP,x^2 Q) at the target. This removes the fixed inner-x normalization from the previous state. It is an exact change of variables where x>0, not a new PDE assumption. Agreement checks the transport implementation; center-radius and tolerance refinement test the inner-jet truncation numerically. Neither calculation certifies that every full-plane characteristic reaches the center nor that the source equals the output vorticity.

For each of the three published negative witnesses, (r,y) is converted to (sqrt(r^2-y^2),y). Recompute using several inner radii and two tolerances, then compare the reduced-state transport to the original gradient transport. The exact Gaussian inverse remains distinct from NUM's projected source and inverse. A persistent sign discrepancy is therefore a discrepancy requiring investigation, not by itself proof of an error in the projected calculation.

## Additional domain diagnostic for incomplete source scans

The prescribed smooth field has div W_e=2beta>0 and W_e(X)=beta X+O(1) at infinity. Hence backward orbits stay in a sufficiently large ball: W_e.X>0 outside that ball, so the reverse field points inward there. Smooth boundedness on compact sets then gives backward completeness. This does not imply entry into a small center ball. Extra equilibria or their invariant sets can affect the limit. A nonconstant periodic orbit is impossible: its simple closed orbit bounds a positive area, its tangent field has zero outward flux, while the divergence theorem gives flux 2beta times the area. This argument requires neither a wall nor y symmetry.

Search numerically for zeros of the exact analytic W_e, evaluate their full Jacobian and compare selected backward trajectories at a longer time budget than NUM's 30. A sampled root search does not certify absence, uniqueness, or a basin. At a detected root, positive Jacobian determinant and positive trace give an unstable equilibrium if hyperbolic, while negative determinant gives a saddle; numerical eigenvalues alone are not a rigorous enclosure. Even if extra zeros are found in an external-source field, this does not establish them for an unforced B2 candidate. Failed or completed sample trajectories must remain separately labeled.

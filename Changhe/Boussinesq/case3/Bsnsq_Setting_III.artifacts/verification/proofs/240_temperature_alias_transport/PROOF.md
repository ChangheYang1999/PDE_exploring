# Controlled temperature-fit experiment on literal Gaussian transport

## Exact problem and scope

Use the exact whole-plane Gaussian source velocity and its canonical center subtraction from P236. Fix beta=3, a0=1 and each of the three signed source configurations whose published scan reports a negative transported-vorticity witness. Let W=3X+u_e(X)-u_e(0). The transported temperature satisfies W.gradTheta=Theta. Along a backward trajectory X'=-W, initialized at a target point P, stop at the first radius epsilon. At time T the inner point is Q. With the prescribed finite center jet Theta_e(Q)=Q_x^2(1+f01 Q_y), define

    Theta_e(P)=exp(T) Theta_e(Q).

This is the exact characteristic extension of the finite-sphere boundary data wherever that orbit reaches the sphere. It is an approximation to the smooth center-jet construction, not a proof of global existence or compatibility. The source is literal Gaussian, not the numerics lane's projected source. No source fit or fitted inverse is used. This experiment isolates temperature fitting from source approximation.

In positive x coordinates ell=log x, the backward equations are

    ell'=-W1(exp ell,y)/exp ell, y'=-W2(exp ell,y).

The temperature ratio can be evaluated without squaring very large or very small x:

    F_e(P)=exp(2 ell(T)+T-2 log P_x)*(1+f01 y(T)).

This follows by substitution and does not change the field or its characteristics. The canonical Gaussian inverse and first mixed center coefficient are derived in the complete P236 proof.

## Fits with fixed velocity and fixed temperature data

Sample the same radial knots and seven Gauss points per interval as the published scan. Use36 midpoint angles, which include the12 original midpoint angles exactly at indices3j+1. Thus the unresolved and resolved fits use a common temperature data set and a common velocity. Fit the divided temperature in the original radial r map and degree-five splines. Compare K16/N12, K12/N12, K16/N36 and K24/N36. The K16/N12 fit is defined as the exact coefficient-minimum-norm solution, using P239's full nullspace theorem; the other fits use discrete cosine orthogonality and independent radial least squares. This is a separately implemented diagnostic, not execution of the fitting lane's code.

For F=D sum S_k(t)cos(k phi), D=(1-t)^5, r=L((1-t)^(-3)-1), differentiating gives

    F_r=D sum [S_k'(t)-5S_k(t)/(1-t)]cos(k phi) / (dr/dt),
    F_phi=-D sum k S_k(t)sin(k phi),
    Theta_x/x=2F+r sin(phi)^2 F_r+sin(phi)cos(phi)F_phi,
    Theta_y=x^2[-cos(phi)F_r+sin(phi)F_phi/r].

These use x=r sinphi, y=-r cosphi, partial_x r=sinphi, partial_y r=-cosphi, partial_x phi=cosphi/r and partial_y phi=sinphi/r. The derivatives are evaluated analytically from an independently constructed SciPy spline. Differencing at independent points supplies a control.

## Transport of the fitted forcing

Hold the same W and the same backward path fixed. For each fitted temperature use Omega'=-Omega+Theta_x along forward paths, with the finite center value Omega_e(Q)=Q_x(b0+g01 Q_y). In the divided variable G=Omega/x, this is

    G'=-(1+W1/x)G+Theta_x/x.

This identity follows from x'=W1 and the quotient rule. The forcing here is explicitly the derivative of the fitted temperature. It need not satisfy the temperature transport PDE. Compare its G(P) with P236's directly transported gradient, which evolves gradTheta'=((beta-2)I-DW^T)gradTheta and therefore never differentiates a fitted temperature. Differences are numerical diagnostics, not proof of an exact global sign or a PDE solution.

For fitted fields report the unscaled thermal residual RTheta=W1 Theta_x+W2 Theta_y-Theta and pointwise normalizer NTheta=abs(W1 Theta_x)+abs(W2 Theta_y)+abs(Theta). If NTheta=0, define the ratio0 only when RTheta=0 and mark any nonzero residual as infinite; use no positive artificial floor. Include both fit-grid values and between-angle points. Incomplete paths cannot produce a valid witness or feedback value.

## Controls, evidence and interpretation

Before relying on numerical outputs, check the log-coordinate reconstruction against P236's Cartesian characteristic evaluator at the three witnesses and additional points, using different inner radii and tolerances. Test spline gradients by independently differencing Theta. Test the forcing integrator on the exact linear field W=(x/2,11y/2), Theta=x^2, Omega=4x/3, and on the exact Gaussian gradient transport reference. Verify the12-angle subset relation and the minimum-norm alias splitting.

If K16/N12 produces a negative witness for the literal source while both resolved fits and direct gradient transport give a stable positive value, that would demonstrate that the angularly undersampled temperature fit can cause this sign error in the controlled literal-source construction. It would not identify every difference in NUM's projected-source/RK4 computation. A match with its reported numbers is an additional quantitative observation. If the controlled sign remains positive, the source projection, temporal integration, radial fitting and other differences remain candidates requiring further isolation. No outcome establishes a B2 endpoint.

The proof and experiment design precede code. The numerical data, errors and time accounting belong in verification/. No formalization or mathematical certification of floating-point ODE errors is claimed.

## Experimental outcome recorded 2026-10-22T01:46:24.541749+00:00

The computation finished with all30240 paths complete. The K16/N12 fit gives negativeG at all three witnesses and quantitatively approximates NUM's negative outputs, while the direct-gradient references are positive. The anticipated "resolved"36-angle fits have large fit errors and mixed output signs and are not resolved. Therefore the design's stronger conditional refinement criterion was not met. The actual result is the controlled fitting-operation sensitivity reported in verification/SUMMARY.md and comparison.csv, with all numerical limitations. The exact boundary-gradient correction for finite-sphere data is a separate open diagnostic; no claim here equates a finite inner jet with an exact center solution. The B2 endpoint is OPEN.

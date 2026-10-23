# Independent reconstruction of the historical cubic fits and length frame

Result247, written before the evaluator. This audit concerns64 saved forced trial states in seven epsilon-continuation families and the related printed diagnostics. It does not treat them as smooth solutions or infer a Taylor coefficient from a finite-window fit. Producer code is inspected for definitions but never executed or imported.

## Reconstructible quantities

The saved representation is rho(r,theta)=r sin(theta) W(r) sum_k B_k(r)cos(2k theta), with W=(1+r^2/L^2)^((gamma-1)/2), and B_k polynomial in the compact coordinate t determined by r=L(1+t)/(1-t)^P. Reconstruct the radial Chebyshev coefficients and angular coefficients independently from the saved numeric grid using the existing verifier reader. At small r invert instead q=1+t using q/(2-q)^P=r/L at high precision, which avoids subtracting nearly equal floating-point numbers. Evaluate only the first three angular coefficients for the fit by high-precision polynomial recurrence.

The sine-angle identity gives rho_1/r=W(B_0-B_1/2), rho_3/r=W(B_1-B_2)/2. For a cubic density b x^2 y+e y^3, the r^3 coefficients of these sine modes are (b+3e)/4 and (b-e)/4 respectively. Therefore if a1 and a3 are the fitted r^2 coefficients of rho_1/r and rho_3/r, the recorded cubic diagnostic is b_fit=a1+3a3. This identity motivates the diagnostic; for a nonsmooth interpolant it is not an exact origin derivative.

Reproduce two sampling windows, both with30 logarithmic radii scaled by min(1,epsilon): A has endpoints10^-3.5 and10^-1.5, while B has endpoints10^-3 and0.03. Fit a cubic in u=(r/r_max)^2 by independently implemented high-precision normal equations; the coefficient of u divided by r_max^2 is the coefficient of r^2. The four-column design has full rank because the30 u values are distinct: a cubic polynomial vanishing at all of them is identically zero. Thus the Gram matrix is positive definite and the least-squares solution unique. Verify this implementation on injected cubic mode data before any state use. Compare with the original logs, not only the new producer re-extraction. The published log is rounded, and numerical agreement to a tolerance does not recover the exact historical program version.

## Length and amplitude

The endpoint angular function from B_k(1) is multiplied by L^(1-gamma) in the physical far field. Define K_raw=sum_k (-1)^k B_k(1), so the physical vertical-axis coefficient is K_phys=L^(1-gamma)K_raw. For a0 of the appropriate sign, L_can=(K_phys/a0)^(1/(1-gamma)); hence the historical expression (K_raw/a0)^(1/(1-gamma)) must be multiplied by L. Its square must be multiplied by L^2 when used with a physical cubic coefficient. For L=1 these distinctions disappear. Store both quantities and explicitly identify which historical values are being reproduced.

In the refined c_l=1.5 family, metadata should give L=0.1, Lf=epsilon and beta=8.6177. The forcing phi=(1+r^2/Lf^2)^-2 then has physical width epsilon in the same coordinate units as the L=1 runs. beta is the raw angular mean at the far endpoint, so the physical amplitude normalization is beta L^(1-gamma). With gamma=2/3 this is approximately4 for the refined metadata, consistent with L=1,beta=4. This is a map-length change with compensated amplitude, not an assertion that the whole state is obtained by a spatial dilation. Test the amplitude and the equal-epsilon a0 and b_fit data from both families; do not infer exact equality of different numerical states.

## Evidence and limitations

Hash each original checkpoint and frozen numeric snapshot. Freeze the primary logs and current producer source as inert text. Check center angular consistency to document the meaning of the printed a0. Manufacture-check polynomial extraction, coordinate residuals and the sine-mode identity; then evaluate every state at the declared precision, with higher-precision checks on the two smallest widths where the windows differ most. Report actual discrepancies against each rounded historical column. A failed discrepancy threshold must be investigated and retained, not relabeled as a successful reproduction.

The required conclusion is limited to the fit-window and coordinate-frame wording. Neither a converged Newton loss nor agreement with a finite-window cubic fit certifies smoothness, the unforced equation, or the SettingIII YES endpoint. The fixed-c_l refinement residuals, release lineage and dynamic-rate windows are separate source audits.

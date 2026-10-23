# Actual-node export audit for the auxiliary hydrostatic inverse

This is result309, prepared before receiving the proposed numerical export. No candidate result is asserted here. The object is the saved N=96,M=24,c=2 auxiliary hydrostatic trial and its proposed2304-node arrays. It is not a profile of full-plane IPM. The density representation and full vertical inverse are the ones independently defined in result304.

Let g be the exact finite smooth density reconstructed from the frozen binary coefficients. Its inverse is

V1(x,y) = - integral_y^infinity g_x(x,t) dt,
V2(x,y) = integral_0^y t g_xx(x,t) dt + y integral_y^infinity g_xx(x,t) dt.

The positive-y formula extends by V1 odd in x and even in y, and V2 even in x and odd in y. The convergent full integrals and V2(x,0)=0 fix the auxiliary inverse gauge. They are not the full-plane elliptic IPM inverse. All reported evidence must retain that distinction.

At each exported point X=(x,y), write J=(g,gx,gy) for our density jet and Jp for an exported producer jet, when present. Let Vm be the exported map velocity, Vp the exported evaluator velocity, and Vq our independent physical quadrature velocity. The residual is

R(J,V)=(cx+V1)gx+(cy+V2)gy-g.

It obeys the exact decomposition

R(J,Vq)-R(Jp,Vm)
= (Vq-Vm).grad J + (cX+Vm).(grad J-grad Jp) - (g-gp).

This is a cancellation identity, verified by expanding both sides. The second and third terms cannot be omitted unless the two jets coincide. With J fixed, R(J,Vq)-R(J,Vm)=(Vq-Vm).grad J. Exact Fraction arithmetic on all stored binary64 operands can prove these finite arithmetic identities. It cannot prove that either numerical velocity equals the exact integral. Each residual has its own denominators

Nf(J,V)=|(cx+V1)gx|+|(cy+V2)gy|+|g|,
Nv(J,V)=|g|+|xgx+ygy|+|V1gx+V2gy|.

Nv has no c multiplying its middle term. An undefined ratio at a zero denominator is recorded, together with the absolute residual, and excluded from no count silently. For a common signed decomposition use the same declared denominator for all terms; ratios with different denominators do not telescope.

Admission. Read the export twice and bind identical bytes, its metadata and the frozen state hash. Do not trust an array merely because its name says map or reference. Check its numeric dtype, shapes, finiteness, point count, coordinate ordering and coefficient identity. Reconstruct the declared radial nodes r=L sqrt((1+t)/2)/(1-t)^P and midpoint angular nodes independently; any discrepancy between exported and reconstructed coordinates is measured. Actual exported coordinates, not rounded labels or reconstructed approximations, are the target of the evaluation. A source record lacking complete coordinates or clear velocity semantics cannot support an actual-node comparison. Exported velocity vectors do not authenticate the original map matrices or historical execution; keep that limitation unless separate evidence becomes available.

Method. Reuse only our own Cartesian analytic differentiation and physical dyadic Gauss panels, with a full transformed tail t=R/u^(1/(1-p)). These implementations and their manufactured gates precede309 and do not import producer code. Evaluate all admitted nodes under at least two orders/splitting radii, retain component and residual differences, then refine the selected maxima and largest sensitivity witnesses with a third rule. Report the largest sampled absolute R, Nf/Nv ratios, coordinates and counts for each radial region. Source maxima are not obtained by dividing a maximum numerator by a maximum denominator. Differences between quadratures measure empirical sensitivity of a common binary64 integrand, not a certified error enclosure. Any multiple-precision local-jet checks are separate from a full multiple-precision inverse.

Compare the exported map and evaluator velocities separately with our result. If the original lower-order rule is reconstructed independently, label it a rule reconstruction rather than an original matrix product. The exact decomposition isolates finite algebraic terms for these particular exported points and this trial. It does not establish a cause or dominant mechanism for all annulus plateaux, all resolutions, or the infinite sequence of trials. Neither convergence nor nonconvergence follows from finitely many states.

Manufactured tests. For g=y/A with A=1+x^2+y^2, differentiation gives gx=-2xy/A^2, gy=1/A-2y^2/A^2 and gxx=-2y/A^2+8x^2y/A^3. Put a=sqrt(1+x^2). Direct integration gives

V1=x/A,
V2=x^2 y/[a^2 A]-atan(y/a)/a^3.

Indeed V1=-integral_y^infinity gx and d_y V2=-d_x V1, with V2(x,0)=0. For g=y exp(-x^2-y^2), gx=-2xy exp(-r^2), gy=(1-2y^2)exp(-r^2), gxx=(4x^2-2)y exp(-r^2), and

V1=x exp(-r^2),
V2=(2x^2-1) exp(-x^2) sqrt(pi) erf(y)/2.

Both are smooth, have the required parities and convergent vertical integrals. The second formulas follow from the elementary integral of t exp(-t^2) and incompressibility with zero axis value. Test both families at signed interior points and both axes, and the rational family also at far points. Use exact rational artificial jets and velocities to test the full two-jet decomposition and to expose the incorrect same-jet simplification when J differs from Jp. Verify manufactured denominators and zero handling independently.

Dependencies: result304 and the independent evaluator/inverse gates187/233; result287 for finite arithmetic versus inverse accuracy distinctions. Candidate admission, numerical execution and actual Opus5.5 review remain OPEN. Primary endpoint: UNRESOLVED.

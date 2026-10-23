# Reconstruction package domain and data audit

Written 2026-10-21 before the checks below. The package being inspected is a producer deliverable. Its numerical evaluator is not imported or executed by this audit. Coefficient files are loaded only by the verifier's restricted numeric loader, and all new files are in the verifier lane.

## Definition of faithful reconstruction

For each cited state, faithful reconstruction requires an unambiguous coefficient representation, the exact map and weighting parameters, the specified full-plane inverse and its gauge, and declared finite sampling. File hashes identify data; they do not validate the PDE or a historical optimizer. A reconstruction using a discrete inverse must be identified as such. Existing independent canonical checks can be associated with the package only after the exact hashes match. Current code cannot certify a historical source version that was not recorded.

## Full-plane parity and point coordinates

The density is even in x and odd in y; the stream is odd in both. Therefore, away from axes and with x0=|x|, y0=|y|,

rho(x,y)=sgn(y) rho(x0,y0),
rho_x(x,y)=sgn(x)sgn(y) rho_x(x0,y0),
rho_y(x,y)=rho_y(x0,y0),
U_1(x,y)=sgn(x) U_1(x0,y0),
U_2(x,y)=sgn(y) U_2(x0,y0),
psi(x,y)=sgn(x)sgn(y) psi(x0,y0).

These identities follow by differentiating the stated parities and U=(-psi_y,psi_x). The transport residual has the same parity as rho, and both denominators N_f and N_v are even in both variables. Axis values follow by continuity, with rho=rho_x=U_2=psi=0 on y=0 and rho_x=U_1=psi=0 on x=0. At the origin both velocity components are zero, rho=0 and grad rho=(0,a).

Clipping atan2(y,x) into [epsilon,pi/2-epsilon] while keeping r=sqrt(x^2+y^2) instead evaluates another point. For example (-a,a), a>0, is moved almost to (0,sqrt(2)a); (a,-a) is moved almost to (sqrt(2)a,0). It supplies neither the parity extension nor the original coordinates. This is an exact geometric fact independent of inverse accuracy. An angle clipped by epsilon at an axis also perturbs that axis point; such an evaluation must not be labeled exact axis evaluation. If only a quadrant is supported, the supported domain must be explicit and outside points rejected, or the correct parity extension implemented.

## Sources and package independence

The loader imports modules from artifacts/src. A module that inserts the mutable live src path before subsequent imports can cause later modules to be loaded from the live checkout instead. Python resolves an as-yet-unloaded module using sys.path order. In the observed import order ipm3 and ipm3s are imported first, then ipm3q inserts the absolute live path, and the following ipm3ql import can resolve there. Thus the package is not wholly determined by the archived source tree in that environment, even if the current files happen to match. Remove the absolute override or specify and hash every resolved source dependency. This is a reproducibility issue, not a mathematical refutation of a saved field.

## Verification and scope

Check each listed SHA-256 against the actual state file, record numeric parameters, compare source inventories, and freeze the loader, README and source hashes. Independently evaluate a smooth Q state at symmetric points and at the coordinates produced by the clipping rule, using the verifier's scalar polynomial evaluator, to exhibit any domain mismatch. This demonstrates the coordinate error without executing producer code. Existing canonical inverse audits retain their own scopes. A successful manifest check, a repaired coordinate loader or an archived source version proves no existence or nonexistence endpoint.

## Follow-up source audit, 2026-10-21 08:52 UTC

The same parity and manifest argument is reapplied to the refreshed source package in verification/repair_20261021T0852. A radial forcing mu y phi(r) is even in x and odd in y, so the forced point residual after parity reconstruction is R_f=R-mu y phi(r), using the original signed y. Differentiating the forced transport equation at the origin yields a0(c_l+c-1)-mu because phi(0)=1. These are the two expressions now printed by the revised loader. The saved angular oversampling parameter must be passed into its discretization constructor; otherwise its producer inverse may be different. A stored radial exponent P remains authoritative, and the effective density exponent is 1-1/P. The audit checks these exact source expressions and all source hashes without importing or executing the producer code. The loader still evaluates its polar routine before skipping an origin request, so no general origin API claim is confirmed. Reconstruction from saved nodal values is not asserted to reproduce every stored coefficient bit for bit; independent coefficient-based evaluation remains separate.

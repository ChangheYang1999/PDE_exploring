# Signed spans and a finite valley diagnostic

Date: 2026-10-20. Status: exact elementary algebra and a conditional audit of stored numerical measurements.

## Statement and notation

Let v_1,...,v_m be independent parameter directions. Let c and x be differentiable scalar observables. Write a_i=Dc[v_i] and b_i=Dx[v_i]. Even if a_i>0 and b_i>0 for every i, the image of their real linear span can contain a vector with Dc>0 and Dx<0. In particular, if two slopes b_1/a_1 and b_2/a_2 differ, every pair (delta_c,delta_x) is attained by a unique linear combination of those two directions.

## Complete argument

The two-observable action matrix is

    M = [[a_1,a_2],[b_1,b_2]].

Its determinant is a_1*a_2*(b_2/a_2-b_1/a_1), which is nonzero under the stated hypotheses. Thus the linear system M*z=(delta_c,delta_x) has a unique real solution. Nothing in the linear span definition requires the coefficients z_i to be positive. For a concrete exact example, the columns (1,1) and (1,2) each have positive slope. Their combination 3*(1,1)-2*(1,2)=(1,-1) has the opposite signs. A sign argument applies to a positive cone if the coefficients and the c actions are positive; it does not apply to the real span.

Three independent observable rows and three directions can similarly be fitted if their action matrix is invertible. This only matches those observables at first order. It does not match the entire state, establish that a finite displacement stays on a nonlinear solution family, or justify using a derivative outside the measured step range. If other observables fail to match, that supplies a specific finite projection discrepancy, not a proof of continuum isolation.

## Numerical protocol and scope

Freeze the two numerics-lane valley_s4e JSON files. Independently recompute each reported central difference and second difference from its saved plus/minus/base scalar measurements. This audits the arithmetic; it does not independently measure their physical velocity, stagnation point or residual. Compute the change of each listed observable between grids and solve the two- and three-observable systems from the saved central-difference columns. Report signed coefficients, reconstruction errors, other-observable mismatches and their size relative to the sampled steps.

A residual norm is a nonlinear scalar. A finite sample at plus/minus s bounds neither the residual along every intermediate coefficient nor the interval of c changes outside that sample. Report the actual sampled c displacement and relative norm increase; label any asserted broader width as unverified. Derivative units are per unit coefficient or per unit c, explicitly distinguished. A derivative of magnitude0.03 per unit c gives3e-5 over delta_c=1e-3 at first order, not an upper bound1e-5.

Dependencies: elementary linear algebra only for the theorem. The conditional numerical audit depends on the frozen source scalar data, with hashes recorded. No new profile, canonical residual verification or endpoint follows.

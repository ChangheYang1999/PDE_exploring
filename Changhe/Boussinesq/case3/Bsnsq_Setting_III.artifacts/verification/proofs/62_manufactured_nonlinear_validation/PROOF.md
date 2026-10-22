# Manufactured forcing and saved-state validation

Status: exact identities proved; numerical audit pending. No profile endpoint.

## Statement and hypotheses

Let beta>0 and let Q, Q0, E be smooth odd-in-x vorticity fields with uniform power decay. Let B denote the canonical once-subtracted full-plane inverse, with curl B[Q]=-Q and B[Q](0)=0. Fix the forcing Fv=E-Q0. For a smooth temperature T define Wf=beta X+B[Q]+B[Fv] and Ws=beta X+B[Q]. Define both residual pairs by the prompt equations, with source T_x in the vorticity equation. Then

    R_T,forced = R_T,self + B[Fv] dot grad T,
    R_Q,forced = R_Q,self + B[Fv] dot grad Q.

At Q=Q0 the forced velocity is exactly beta X+B[E]. Thus Q0 and T0 solve the forced equations if and only if they solve the passive transport equations in that prescribed velocity. A finite fit of passive characteristic values does not establish either differential equation exactly. These identities hold without positivity and for every exponent for which the stated inverse integrals converge.

## Proof

The inverse is an absolutely convergent linear integral on power-decaying inputs. Consequently B[Q]+B[E-Q0]=B[Q+E-Q0], and substitution at Q=Q0 gives B[E]. Each transport residual is affine in W. Subtracting the two residual definitions cancels every other term and gives the displayed differences. No integration by parts, finite-box closure or imposed harmonic term is used.

The forced elliptic source is Q+Fv, whereas the transported vorticity in the forced first equation is Q. Therefore the manufactured system is deliberately different from B2-P. Even an exact forced solution is not a B2-P solution unless both forcing contributions to transport vanish. A fitted forced fixed point alone supplies no such condition.

## Numerical evidence required

The source snapshot and the fixed reference Q0 must be retained together. The target field Q, temperature T, amplitude, objective and iteration index must refer to the same iterate. A converged result different from Q0 can reflect a second forced solution or a discretization defect; no uniqueness theorem has been supplied. Validation of one manufactured nonlinear instance does not prove convergence of the algorithm on another instance.

Independent evidence is recorded under verification/manufactured_20261020T1915. Only this lane's SciPy value reader, Cartesian finite differences and Duffy-square plus infinite-exterior quadrature are executed. Numerics code is retained read-only as provenance and inspected, never imported.

## Numerical audit completed 2026-10-20T19:15:57.178926+00:00

See `../../verification/manufactured_20261020T1915/SUMMARY.md` for a finite-sample application of these identities. The Picard snapshot has forced differential divided G ratio about0.05508 and true self ratio about0.36384. The exact algebra in this packet does not prove convergence of this numerical experiment.

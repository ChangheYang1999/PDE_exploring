# A reduced physical-residual correction test

Date: 2026-10-20. Status: independently implemented numerical diagnostic, not a profile construction or a proof of existence.

## Definition and rationale

The base is the saved dnSB density. The seven data directions are six supplied Ritz vectors reconstructed independently and a separately constructed calibration direction, as defined in ../linearized-check/PROOF.md. Let z=(b_nodes,c_l,C). The physical density uses b_nodes and c_l; C is an auxiliary orbit-solver coordinate and does not enter the canonical inverse here. Every direction has zero first radial row and preserves b(0,s)=1.

For eight physical points with radius at most100, use this lane's independently computed physical transport derivative J_ij=dot R_j(X_i)/N_f,base(X_i), and signed residual F_i=R_base(X_i)/N_f,base(X_i). This is neither the numerics lane's orbit residual nor its Jacobian. The full-plane kernel, density reconstruction and Cartesian differentiation are independently implemented. Discard singular values of this8 by7 sampled matrix at or below10^-5; let J=U S V^T be its SVD and form

    d=-sum_(sigma_j>10^-5) v_j (u_j^T F)/sigma_j.

For step lengths t=1/4,1/2,1, construct z_t=z_base+t V_data d by direct addition of the nodal values and c_l. The saved C is updated in those coordinates but remains irrelevant to the physical residual evaluation. No inherited orbit residual value or stationarity tag is attached to a new trial.

## Exact content of the linear prediction

The density and transport differentiation identities were proved in ../linearized-check/PROOF.md. Consequently, for exact action data and sufficiently small t,

    R[z_t](X_i)/N_f,base(X_i)=F_i+t(Jd)_i+o(t).

The SVD formula minimizes the Euclidean linearized residual over the retained right-singular subspace. This is only a sampled linear prediction; it contains no bound on the Taylor remainder, the discarded directions or the full-plane norm. The actual trials must be evaluated with the nonlinear density, nonlinear parameter dependence and canonical full-plane inverse. Independent holdout points are included. A better fit at the eight training points alone is not branch convergence or existence evidence.

The nodal representation still has the exact-center smoothness obstruction of AV23. This experiment concerns whether the observed physical residual at the approximate weaker trial can be reduced. It is not intended to claim P_inf from a finite basis or from vanishing fitted coefficients. Strain, center and nonlinear residual checks remain separate. All results are floating checks unless explicitly labeled as interval bounds.

Dependencies: the proved physical linearization, finite-dimensional least squares and the independent inverse. Code and raw trial fields are alongside this proof. No numerics solver code, server, formal build or external computation is used.

## Second correction and fresh holdouts

After completing the first trial, relinearize the physical residual at its t=1 field using the same seven directions and all26 original evaluation points. The former18 holdouts now become fit points and must no longer be described as held out. Apply the same sampled SVD formula and10^-5 cutoff. All seven singular values exceed the cutoff in this second matrix. Test t=1/4,1/2,1 again, without assuming that the linear improvement survives such finite steps. Reserve fresh radii0.2,2,8,15,50,300 and angles0.4,1.2,1.52, giving18 new holdouts, and evaluate the old t=1 field on them for comparison. The operation is a second reduced Gauss-Newton iteration, not continuation on exact solutions. No inverse or source regularity theorem follows from its success or failure.

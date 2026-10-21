# Independent checks of additional stationary trials

Date: 2026-10-20. Status: numerical trial audit, not a convergence theorem.

The two initial inputs are the numerics lane's completed dnB_n96m40S field (N=96,M=40,L=8) and dnCS2_n120m48 field (N=120,M=48,L=8). The latter changes the weights of inner collocation equations. They are different represented densities. Their orbit residual magnitudes and matrix singular values are not physical residual norms. Byte snapshots of the actual arrays are retained in data; the audit never substitutes a projection of another state.

For each density the independent reconstruction uses tensor cosine transforms, the inverse angular coordinate, and the given radial prefactor. The canonical inverse is the independently derived paired real-space kernel in ../inverse/PROOF.md, with its separate local principal value. Cartesian eighth-order differences give transport and elliptic diagnostics. This lane's code label R_Nv means the report's |R|/N_f; R_Nf means the report's |R|/N_v. The report N_f is |rho|+sum_i |W_i rho_i|. The report N_v is |rho|+|X.grad rho|+|U.grad rho|. No equality between these and the orbit norm is assumed.

At two fixed radius10 points and two points near the source, compute physical residuals. Refine the inverse angles2048 to4096 at the radius10 points and compute the near-source elliptic diagnostic at4096 with difference step0.0025. Exact density parity implies U(0)=0. An exactly unit first radial row preserves the prescribed cubic normalization. Center intervals are computed from exact binary input data at the ideal interpolation nodes, as in ../center-regularity/PROOF.md. A nonzero degree-five angular compatibility defect excludes a smooth factor for that represented field; the nonzero balance determinant excludes exact compatible transport, not limits of changing interpolants.

The exact exterior estimate in ../exterior-tail/PROOF.md generalizes to these grids. If B bounds the absolute node values, tensor discrete orthogonality gives |b|<=B sqrt(2N(2M-1)). Let H be the smallest integer whose square is at least2N(2M-1), and let B0 be the ceiling of B. For L=8 and0<1/c_l<1/5 this yields |rho|<=512 H B0 r^(1/5) for r>=1. The omitted canonical velocity outside R is therefore at most

    (5C/2) |X| R^(-4/5) / (1-|X|^2/R^2)^2,  C=512 H B0.

This bound is exact for the ideal density. It does not enclose arithmetic or interior quadrature errors. A harmonic strain is not an allowed adjustment because the canonical law fixes the gauge.

The comparisons can detect failures and parameter sensitivity at the tested states. They do not certify an exact kernel, isolation, a nonlinear family, B_j vanishing, three-grid convergence or either strong-setting endpoint. All observed values are floating point unless explicitly labeled exact or interval-enclosed. Dependencies and complete proof details are the referenced standalone inverse, center and exterior arguments.


## Actual time-step and inverse-resolution re-solves

The same audit is applied to dnS_dt0005_n120m48 (halved orbit time step) and dnP720_n120m48 (increased inverse radial resolution). These are byte copies of the actual completed fields, not re-evaluations of dnSB under new orbit settings. The proof, normalization, gauge and exterior estimates above apply unchanged because their N,M,L and growth exponents obey the same hypotheses. Physical residual sensitivity is measured at identical physical points. Similar residuals do not prove inverse or orbit error estimates for the continuum equation, and do not establish invariance of a near-kernel. All center conclusions concern each fixed represented field. Independent outputs and exact source hashes are indexed in verification/mechanism_inputs.json and mechanism_summary.json.

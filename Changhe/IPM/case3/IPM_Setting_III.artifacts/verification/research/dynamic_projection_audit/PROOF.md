# 167. Canonical right-hand side and projection in the DR discretization

Written 2026-10-21 before this computation. This audits a finite projection, not a continuum trajectory or a profile. The input is a literal saved Q density, with canonical inverse defined on the entire plane.

## Definitions and exact claims

Fix C>1, L>0, P>1, and polynomials B_k of degrees at most N-k, 0<=k<M. Set sigma=(1+t)/2, w=(1-t)/2, r^2=L^2 sigma(1-t)^(-2P), and rho=y w sum_k sigma^k B_k(t)cos(2k theta). The center is interpreted by its smooth Cartesian extension. Let U=(-psi_y,psi_x), -Delta psi=rho_x, with the SettingIII parities and U=o(r). Let c=psi_xy(0) be the canonical strain, a=rho_y(0), and let cw,cx be the stored instantaneous DR rates. Define

    G=cw rho-(cx X+U).grad rho, F=G/(y w).

F has a smooth even angular extension at zero. Its limiting center value is a(cw-cx-c). This follows by the Taylor expansions rho=a y+O(r^3) and U=(-c x,c y)+O(r^3). No stored relation cw=cx+c is substituted in the independently evaluated canonical c.

Use radial nodes t_i=-cos(2 pi i/(2N+1)), 0<=i<=N, and angles theta_j=(j+1/2)pi/(2J), 0<=j<J=3M. For k<M, take the orthogonal discrete cosine coefficient F_k(t_i). Let A_k have entries sigma_i^k T_n(t_i), 0<=n<=N-k. A singular value decomposition A_k=U_k D_k V_k^T and cutoff d>rcond*d_max define the truncated least-squares coefficient vector

    v_k=V_keep D_keep^(-1) U_keep^T F_k.

The nodal modal projection is Q_k F_k=U_keep U_keep^T F_k. In exact arithmetic this equals A_k v_k. Reassemble the projected b derivative Fp=sum_(k<M)(A_k v_k)cos(2k theta). The represented density derivative for the coefficient ODE v=u_tau is Gp=y w Fp. In general Gp is not G. The difference is a projection defect, not a time integration error. Discarding a nonzero angular mode above the retained range gives an immediate counterexample to equality, even without radial truncation.

Each Q_k is symmetric and idempotent: Q_k^T=Q_k and Q_k^2=Q_k follow from orthonormal columns of U_keep. Thus it has Euclidean operator norm at most one. The angular cosine basis is orthogonal on the specified midpoint grid. Combining these facts makes the full b-value projection an orthogonal contraction in the unweighted nodal Euclidean norm. This does not prove contraction of a physical density norm, a derivative norm or a compact-core norm: multiplication by y w and restriction to a core do not commute with the projection. The coefficient norm can also be large when retained singular values are small. Floating point evaluation of A_k v_k can differ from U_keep U_keep^T F_k through cancellation; both versions must be recorded.

On any sampled set, the triangle inequality gives ||G|| <= ||Gp||+||G-Gp|| and the reverse bound with G and Gp exchanged. Thus a small projected derivative alone establishes approximate stationarity only together with a small projection defect and inverse/evaluation error on the same set. If a producer uses an approximate inverse and a different computed F, this experiment with the canonical F is not automatically the exact derivative of its saved numerical trajectory. It independently measures the mathematically specified projection and provides a comparison; the producer must still expose its actual F and v to identify its own defect.

## Independent numerical protocol

Reconstruct the literal saved density with the verifier's scalar Q reader. The canonical G uses separately derived complementary full/defect Green charts, with inverse orders128 and256, independent of producer modules and derivative matrices. At the origin use the exact rational canonical strain formula. Compute the projector with SciPy's SVD and explicit orthogonal cosine sums; producer code is read for the definition only and never imported/executed. Compare stable nodal projection, coefficient reconstruction via Clenshaw, and canonical F. At radial and angular midpoints compare the polynomial derivative with a new canonical G evaluation. Include constant starts and tau20 states at three sizes, recording actual times, source hashes and rates. Report regional absolute norms, norm ratios, projection defects and singular-value counts. A selected-point or grid comparison is empirical, not an interval certificate.

The verification gates test symmetry/idempotence, discarded angular content and reconstruction. Existing independent manufactured canonical-inverse tests are prerequisites. Dependencies: result165 for the DR identity and Q inverse, result151 for the coefficient map, and the canonical inverse and finite-field proofs. No continuum instability, time convergence, existence, nonexistence or decisive endpoint is inferred.

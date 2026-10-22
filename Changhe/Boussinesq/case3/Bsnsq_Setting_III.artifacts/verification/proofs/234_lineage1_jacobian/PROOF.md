# Independent verification of the lineage1 lambda0.96 Jacobian

## Exact scope and status

This packet concerns the finite forced-map array published as NUM runs/jac_L1l096.npz and the native state runs/blam24v_lambda0.96.npz. The state has beta=3.0060477873545817, lambda=0.96, K=24, Nt=56, degree5, L=1.5 and grade1.5. Its SHA256 is37a27aab555c057ca75d84741ce8ecad56d74642ca7bb983dd1a147d1faa4b0f. The matrix was not yet published when this proof was written. The original proof is preserved in verification/PROOF_before_matrix_publication.md. After publication, twelve prepared geometry checks and41 matrix checks passed; see verification/SUMMARY.md and matrix_checks.json. Finite-array results are CONFIRMED in their declared norms. The interpretation as an exact nonlinear derivative remains OPEN.

Let c in R^n denote the active coefficients of G=Omega/x, and T(c;beta,lambda) the numerics lane's finite fitting map. Write J for a supplied candidate derivative, A=I-J, f=T(c)-c, t_lambda and t_beta for supplied partial derivatives at fixed coefficients. The basis is retied to beta; the source geometry is fixed. Define q(beta)^T c as the canonical center strain of the native vorticity and c_f as the strain of the fixed source. Define h=q^T c+lambda c_f-1-beta/2. All array identities below are ordinary finite-dimensional identities. Interpreting them as nonlinear derivative or branch statements additionally requires an actual derivative, an exact fixed point and suitable regularity.

The native representation is C4 across simple degree5 knots. It is not automatically a globally smooth B2 profile. The stored state remains a forced state at lambda0.96. Nothing about matrix rank can remove its unforced PDE residual or establish an accepted endpoint.

## Canonical strain and the active basis

Use polar coordinates x=r sin(phi), y=-r cos(phi). Put u=1-t=(1+r^2/L^2)^(-1/(2b)), eta=r/sqrt(r^2+L^2), where b is the basis exponent beta. The native divided field is

    G(r,phi)=sum_k u^(b+1) eta^(k mod2) S_k(t) cos(k phi),
    S_k(t)=sum_{j>=floor(k/2)} c_kj B_j(t).

The B_j are normalized degree d B-splines with the stored clamped knots tau. Angular orthogonality in the canonical center-strain integral retains only k=1 and k=3. The radial factors obey u^(b+1) eta dr/dt=bL. Since integral_0^1 B_j=(tau_(j+d+1)-tau_j)/(d+1), the exact row is

    q_kj=-(bL/4)(1_(k=1)-1_(k=3))
                    (tau_(j+d+1)-tau_j)/(d+1).

Thus q_beta=q/b at fixed L, knots and coefficient coordinates. The fixed source has its own stored exponent, knots and coefficients, so its strain is computed independently in its own basis. It must not be retied to the current beta. This strain law is the canonical once-subtracted full-plane inverse evaluated at the center, not a finite-box inverse.

## Projection and the correct dilation

If the fitted map depends on c only through the affine strain projection

    P(c)=c-q(q^T c+lambda c_f-1-beta/2)/(q^T q),

then P(c+tq)=P(c), and the exact derivative satisfies Jq=0, Aq=q. Coordinate finite differences need not preserve this identity exactly. A computed projection defect is a consistency check, not an operator error bound. Iteration-neutral means Jv=v, equivalently Av=0. A norm ratio ||Av||/||v|| near1 is not neutrality and does not prove Jv=0.

The B2 spatial scaling gives Omega_l(X)=Omega(X/l), and therefore G_l(X)=l^-1G(X/l). Its derivative at l=1 is v_true=-G-X.gradG. Omitting the amplitude factor gives v_old=-X.gradG. For the native radial factors,

    r t_r=u eta^2/b,
    r(log u^(b+1))_r=-(b+1)eta^2/b,
    r(log eta)_r=1-eta^2.

Hence the normalized bracket for v_old in mode k is

    [((b+1)eta^2/b-o(1-eta^2))S_k-u eta^2 S_k'/b],
    o=k mod2,

and the bracket for v_true subtracts S_k. These analytic derivatives are independently evaluated using SciPy's B-spline derivative. Direct integration shows c(v_true)=0 and c(v_old)=c(G), since the strain is invariant under the full scaling. Differentiation is legitimate for this finite native class: near zero and infinity the integrable endpoint bounds are uniform for l near1, and its knots preserve the first derivative.

The forcing, source and prescribed a0 in the fixed map break this exact spatial family. Even a correct dilation vector is not expected to satisfy Av=0. A finite-basis fit of the dilation may also differ from the exact field. We will compare the supplied vector separately with v_true and v_old by an independent full-plane physical norm.

## Full-plane physical norms

Let w(r)=(r/R)^delta+(R/r)^delta with delta=1/4,R=1, so0<delta<min(2,2/b). Angular integration is exact. Since (u^(b+1))^2 r dr=bL^2 u dt, for mode brackets E_k one has

    ||E||_w^2=pi bL^2 sum_k a_k int_0^1 u eta^(2o)w(r(t))E_k(t)^2 dt,
    a_0=2, a_k=1 for k>0.

This integral defines the positive definite finite Gram matrix H on the active basis: a nonzero finite spline has positive squared integral. Endpoint Gauss-Jacobi quadrature on every knot interval, at two independent orders, approximates its entries; this is a quadrature diagnostic rather than an interval enclosure. It covers the entire physical plane. A separate unweighted integral is also finite.

For H=C^T C with upper Cholesky factor C, ||Ac||_H/||c||_H equals ||C A C^-1 z||_2/||z||_2, z=Cc. Thus the physical singular values are those of C A C^-1. This is a similarity of the supplied array in a declared norm; its eigenvalues are unchanged but its singular values need not match Euclidean coefficient or residual-grid values. A grid-metric factor not supplied in the archive cannot be inferred from scalar summaries.

## Linear solves and augmented arrays

Assuming A invertible, set v_p=A^-1 t_p. For an exact differentiable branch T(c(p);p)=c(p), differentiating gives c_p=v_p. The reduced strain derivatives would then be

    m_lambda=q^T v_lambda+c_f,
    m_beta=q^T v_beta+(q/b)^T c-1/2.

At an approximate fixed point these are only linearized diagnostics. A Newton correction solves A delta=f; its residual and norm will be reported separately. A small correction does not control the nonlinear remainder.

Put d_lambda=c_f and d_beta=(q/b)^T c-1/2. For each parameter form

    B_p=[[A,-t_p],[q^T,d_p]],
    C_aug=[[A,-t_lambda,-t_beta],[q^T,d_lambda,d_beta]].

Block elimination by the invertible left matrix [[I,0],[-q^T A^-1,1]] gives det B_p=det A times m_p. Also B_p(v_p,1)=(0,m_p), so

    sigma_min(B_p)<=|m_p|/sqrt(1+||v_p||^2).

If m_lambda!=0, the vector (v_beta+ell v_lambda,ell,1), ell=-m_beta/m_lambda, belongs to ker C_aug. B_lambda invertible then implies C_aug has full row rank and exactly one-dimensional kernel. Its positive singular values describe transverse directions; the minimum norm ratio over all inputs is still zero. Column rescaling changes parameter units and singular values. Raw and rescaled values must explicitly state which convention is used.

The implicit-function theorem gives an exact local zero curve only at an actual root with the asserted derivative and rank. A nondegenerate fold in lambda additionally needs m_beta=0 and m_beta_beta!=0 at that root. None follows from a nearly singular sampled matrix at a nonzero-defect state.

## Error thresholds and a counterexample

If a computed square matrix A_h and the true derivative A satisfy ||A-A_h||<=epsilon<sigma_min(A_h), then ||Av||>0 for every unit v, by the triangle inequality, proving invertibility in this finite dimension. For C_aug use the transpose to prove full row rank. Floating SVD error must also be included. A few difference steps or parameter columns do not provide such an induced operator bound.

For epsilon>0, T_epsilon(z)=epsilon+z^2/epsilon has defect epsilon at z=0 and exact derivative0, so the Newton correction is epsilon and I-T'(0)=1 is invertible. Yet its fixed-point equation is

    (z-epsilon/2)^2+3epsilon^2/4=0,

which has no real solution. Therefore an arbitrarily small defect with an invertible exact derivative does not itself prove any root. This applies a fortiori to supplied finite-difference arrays.

## Verification protocol and dependencies

Freeze the matrix, scalar summaries and state with SHA256. Tie all active indices, coefficients, beta, lambda and source geometry to the independent state reader. Recompute the canonical strain row, full-plane Gram and dilation comparisons with this lane's own code. Independently recompute coefficient and physical singular values, eigenvalues, projection actions, parameter solves and augmented-array Schur identities. No numerics-lane code is imported or executed. Checks of arrays do not prove the underlying fitted-map derivative, and they do not replace the already independent full-plane PDE residual evaluations of this state. Missing raw column data, grid metrics or nonlinear enclosures remain explicitly OPEN.

This complete derivation uses only calculus, spline integral identities and finite-dimensional linear algebra. The existing P205/P208/P216 proofs contain earlier versions of these arguments for another state; the needed statements and proofs have been given here. Output manifests register the own helper code and all input data used in the current computation.

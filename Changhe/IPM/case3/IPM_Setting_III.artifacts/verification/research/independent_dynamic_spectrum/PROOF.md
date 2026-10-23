# Independent finite compression of the canonical DR linearization

Result176. Written 2026-10-21T07:27:57.723796+00:00 before implementation. This is a finite numerical operator audit. It is not a continuum eigenvalue theorem, an instability theorem, or a profile exclusion.

## Equations and finite space

Fix C>1, P=C/(C-1), L>0, N,M and the shifted polynomial representation of result173. Let H(t,theta)=sum_k sigma^k beta_k(t) cos(2k theta), rho=r*w*sin(theta)*H. Let a=rho_y(0), c=psi_xy(0), cw=-c/(C-1), cx=C*cw. The canonical continuum DR vector field is

F(rho)=cw*rho-(cx*X+U[rho]).grad rho.

At a chosen base field rho, its derivative in direction h is precisely result171's formula. This audit initially uses the explicit constant beta start, H=1. It has a=1, c=-1/4, cw=1/[4(C-1)] and is not a stationary profile. The constant beta start is a nonconstant physical density y*w(t).

Use radial nodes t_i=-cos(2*pi*i/(2N+1)), i=0,...,N, and J=3M angular nodes theta_j=(j+1/2)*pi/(2J). Let A_k[i,j]=sigma_i^k*T_j(s_k(t_i)), j=0,...,N-k, with the same shift convention as result173. An independent SVD A_k=U_k S_k V_k^T selects right singular vectors with S>=thr*S_max. The selected block-diagonal matrix V is orthonormal in the Euclidean coefficient norm. The compression to be checked is V^T J_coeff V, not a restriction to a known invariant continuum subspace.

The angular projection is the exact finite cosine transform on the specified nodes. The coefficient projection per mode is the least-squares pseudoinverse with a stated cutoff rc. If rc<thr, then on the selected output directions V_k^T A_k^+ equals diag(1/S_selected) U_selected^T in exact arithmetic. Thus compressed entries can be computed without amplifying discarded output singular directions. The full projected lift is computed separately when its residual is reported. Its norm is not silently identified with the compressed norm.

## Independent full-plane inverse for basis directions

Write rho=sum_(j odd) b_j(r) sin(j theta), with d_j=b_j/r. A single k>=1 density direction with mode polynomial B=sigma^k beta has d_(2k+1)=wB/2 and d_(2k-1)=-wB/2; k=0 has d_1=wB. The canonical angular Green formula gives, for even m>=2,

h_m(r)/r^2=(E_m(r)-I_m(r))/2,
E_m=int_0^infinity exp((2-m)v) d_(m+1)(r exp(v)) dv,
I_m=int_0^infinity exp(-(m+2)v) d_(m-1)(r exp(-v)) dv.

Therefore

U_r/r=-(m/2)(E_m-I_m)cos(m theta),
U_theta/r=[m(E_m+I_m)-d_(m+1)-d_(m-1)]sin(m theta)/2,

summed over m. These formulas follow by differentiating the interior/exterior primitives; no finite outer boundary or free harmonic term is introduced. Only three adjacent even stream modes occur for each nonzero k. At the origin, use the independent exact cancellation formula c=-a/4+I_0 from result173.

Integrate in logarithmic radius by Gauss-Laguerre quadrature. For an exterior moment take alpha=m-2+delta>0, delta=1/P, v=z/alpha. The apparently large exponential factor is canceled algebraically using

w(r exp(v))*exp(delta*v)=(1/2)*exp(delta*(log(L)-log(r)))*sigma(r exp(v))^(delta/2).

This prevents overflow and integrates to infinity. For the interior moment take v=z/(m+2). Repeating the quadrature order checks numerical convergence; selected directions must also be compared to the verifier's separate primitive inverse. No producer module, differentiated matrix, or inverse implementation is imported.

## Canonical field derivative and projection

Let Q=w+2P*sigma, T=dt/dlog(r)=4sigma*w/Q, and Z=1+dlog(w)/dlog(r)=1-2sigma/Q. A perturbation h=r*w*sin(theta)*H has h_r=w*sin(theta)*(Z H+T H_t) and h_theta=r*w*sin(theta)*(cot(theta)H+H_theta). These derivatives follow by the chain rule. They can be implemented by scalar complex-step evaluation of the weighted mode polynomial and exact angular differentiation, independently of the producer's radial differentiation matrices.

For base mode B and perturbation H, write D_r H=Z H+T H_t and D_theta H=cot(theta)H+H_theta. Put v_r=U_r/r, v_theta=U_theta/r for the base and w_r,w_theta for the perturbation. Then the full linearized field divided by r*w*sin(theta) is

cw H-(cx+v_r)D_r H-v_theta D_theta H-w_r D_r B-w_theta D_theta B
-c[h]/(C-1)*(B-C D_r B).

Turning off both perturbation velocity and rate feedback removes the final three terms involving w_r,w_theta,c[h]. At r=0 the directional field value is zero, since the slope normalization identity is exact at every state; the same holds for feedback-off at the base with cw-cx-c=0. This is an analytic endpoint value, not a fitted boundary condition.

Angular projection followed by the per-mode least-squares compression gives the finite matrix. If an eigenpair of that compression is lifted to coefficient space, its full residual is (I-VV^T)J_coeff Vz. Report this residual in the coefficient norm and in sampled physical density values, with inverse quadrature and cutoff dependence. The coefficient metric and the producer's unweighted node localization are not physical area L2. Physical radial area weights are r^2 Q/(1-t^2), and global L2 additionally requires control of the exterior tail.

## Scope and verification plan

Manufacture exact polynomial derivatives and strain rows; compare the directional derivative to centered differences of the quadratic DR field; compare selected inverse directions to independent primitives; then compute constant-start compressions at two or more quadrature orders. Report any discrepancy from the producer's values, with numerical precision and the subspace convention. A finite compressed eigenvalue only describes this reduced finite matrix. Even an exact unstable profile could have a stable manifold. Neither observed positive eigenvalues nor a failure to converge supplies either decisive endpoint in PROMPT.md.

Dependencies: results inverse,173 and171; elementary SVD and cosine projection; independently proved Green identities. All numerical evidence lives under verification/. No Lean/Lake or other formal build is authorized.

## Composite interior and polynomial-exact exterior quadrature

Added 2026-10-21T07:38Z before implementation. The first pure Gauss-Laguerre matrix experiment at N24 is quadrature-unresolved; its eigenvalues are not accepted. The following equivalent Green integral supplies an independent repair.

For one cosine amplitude H_k=σ^k β_k(t), let d_j=w H_k times the appropriate sine-conversion sign. Consider its exterior contribution to even stream harmonic m=j-1>=2. Put σ=(1+t)/2, w=(1-t)/2, Q=w+2Pσ. Omitting the sign temporarily, the exterior moment in the preceding formulas is

E_m = int_0^infinity exp(-(m-2)v) d_j(r exp(v)) dv.

Use t'=t+(1-t)u, σ'=σ+w u, w'=w(1-u), Q'=w'+2Pσ'. Since dlogr'/dt'=Q'/(4σ'w') and r'/r=sqrt(σ'/σ)*(w/w')^P, direct substitution gives

E_m = (w/2) σ^(m/2-1) int_0^1 (1-u)^(P(m-2)) (σ+w u)^(k-m/2) β_k(t+(1-t)u) Q' du.

For the possible m=2k or 2k-2, the exponent k-m/2 is respectively0 or1. The factor apart from the Jacobi weight is therefore a polynomial of degree at most N-k+(k-m/2)+1. Gauss-Jacobi quadrature with alpha=P(m-2), beta=0 and q satisfying2q-1 at least this degree evaluates the entire exterior exactly in exact arithmetic. The coordinate factors use nonnegative powers; no divergent quantity is subtracted at either endpoint. Floating-point evaluations still require comparison. For m=2 this reduces to ordinary polynomial quadrature and reproduces the canonical strain moment at r=0.

The interior moment is

I_m = int_0^infinity exp(-(m+2)v) d_j(r exp(-v)) dv
    = 1/(m+2) int_0^infinity exp(-z) d_j(r exp(-z/(m+2))) dz.

The implementation integrates z in[0,48] by composite Gauss-Legendre quadrature, using panels of width at most2 in z and at most1/8 in v. It includes the entire remaining interval by a shifted Gauss-Laguerre integral with the exact factor exp(-48). Thus there is no physical outer-box truncation and no omitted interior tail. Refining the per-panel order tests numerical integration of the represented polynomial fields. The quadrature is empirical unless explicit enclosures are separately supplied. This repair changes the integration method, not the canonical inverse, density space, or definition of the compression.

## General frozen background extension (2026-10-21T07:49Z, before implementation)

Let a stored smooth density be rho_B=r w sin(theta) B(t,theta), with B=sum sigma^k beta_k(t) cos(2k theta). Write Z=1-2 sigma/Q and T=4 sigma w/Q, Q=w+2P sigma, so D_r B=ZB+T B_t and D_theta B=cot(theta)B+B_theta are its radial and angular derivatives divided by w sin(theta). If U_B/r has polar components b_r,b_theta, c_B=psi_B,xy(0), cw=-c_B/(C-1), cx=Ccw, the normalized right side is F(B)=cw B-(cx+b_r)D_rB-b_theta D_theta B. For a perturbation H, the full derivative is

cw H-(cx+b_r)D_rH-b_theta D_theta H-u_r[H]D_rB-u_theta[H]D_theta B-c[H](B-C D_rB)/(C-1).

This follows by the product rule and linearity of the canonical inverse and strain. It is valid at every background, not only at a steady one. In particular its origin row vanishes because cw-cx-c_B=0 and delta cw-delta cx-c[H]=0. Omitting both terms involving the perturbed inverse and rates defines the feedback-off comparison; it is not the full original Jacobian.

The new evaluator embeds an old unshifted polynomial checkpoint algebraically into each new local Chebyshev basis. If z=(2t-1-t_k)/(1-t_k), then t=(1-t_k)z/2+(1+t_k)/2. An exact rational Chebyshev composition followed by rounding once converts beta_k(t) into this basis, with zeros appended to the higher radial degrees. No interpolation through producer mode values is used; N and M must contain the original degrees and angular modes and the compactification parameters must match. Thus differences from the producer's regularized transfer are explicitly a background-definition difference, not silently treated as a pure Jacobian discrepancy. The conversion is tested against original polynomial values and derivatives on the new grid and additional points. Full canonical background velocity is evaluated with this lane's inverse. Two independent quadrature levels and manufactured algebraic tests are required. Stored eigenvectors and finite residuals are numerical evidence only.

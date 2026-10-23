# Dynamic basis changes, projections, and diagnostics

Initial proof file written 2026-10-21T07:00:40.572438+00:00, before the independent finite checks. The timestamp label was corrected at 2026-10-21T07:01:23.152797+00:00 from an erroneously rounded future minute; no argument changed. This is an implementation audit, not a profile existence result. The producer source is frozen in verification/dr.frozen.py. No producer code is executed. Dependencies: elementary polynomial interpolation, singular value decomposition, and the DR identities already proved in results149,151,154,160. Numerical ranks are floating-point measurements, not exact ranks.

## 1. The polynomial space and truncation

Let t_i=-cos(2*pi*i/(2N+1)), i=0,...,N, sigma=(1+t)/2, and 0<=k<=N. Both families sigma^k T_j(t) and sigma^k T_j(s_k(t)), j=0,...,N-k, with s_k=-1+2(t-t_k)/(1-t_k), span sigma^k times the polynomials of degree at most N-k. The affine substitution is invertible since t_k<1. Therefore their degree-N mode functions agree after the exact coefficient change. They vanish to order k at t=-1. A degree-N interpolation of their mode values, followed by exact differentiation, differentiates that mode polynomial exactly. None of these statements bounds floating-point cancellation or the condition number. The implementation's assertion of no weakly visible directions requires measurement.

If a least-squares solve discards singular values below a relative threshold, equality of the full polynomial spans does not imply equality of the retained projection. Indeed take A=diag(epsilon,1), 0<epsilon<tau<1. The truncated field projector is diag(0,1). The coordinate change S=diag(1/epsilon,1) gives AS=I and retained field projector I. Thus a basis change can change the integrated finite field equation at a fixed relative cutoff, without changing the full exact polynomial space.

Nor does a small field for a unit coefficient eigenvector refute its growth rate. Put field x=A u and x'=Lx with L=diag(1,-1). Then u'=A^{-1}LAu=Lu. The coefficient eigenvector (1,0) has field norm epsilon, yet that nonzero field grows exactly as exp(t). An exact invertible coordinate change preserves eigenvalues. Computed eigenvalues of ill-conditioned matrices may be inaccurate; conditioning alone does not identify which eigenvalues are inaccurate or eliminate their physical components.

## 2. Compressed Jacobian scope

The frozen source computes V^T J V from coefficient directions retained at1e-8, whereas its default RHS retains directions down to1e-13. Unless range(V) is invariant under J and all omitted directions are controlled separately, this compression does not determine the full Jacobian's spectral radius or provide a full integration stability bound. With V=(1,0)^T and J=diag(-1,100), the compression is -1 and omits the eigenvalue100. Even with J=[[0,1],[1,0]], the compression is0 but the true eigenvalues are+-1 and J V is outside range(V). These exact counterexamples establish the logical limitation; they do not assert that either matrix models this IPM computation. An explicit RK method also has no blanket stability guarantee from a spectral-radius bound for arbitrary complex eigenvalues or transient amplification.

## 3. A duplicated moment method evaluates the wrong field

The frozen DR class defines exterior_moments twice. Python uses the latter definition. The first uses beta_at and honors the local basis; the latter evaluates all coefficients as T_j(t). This is a genuine field mismatch whenever the shifted polynomial differs. For C=3 the map exponent P=3/2 and Q(t)=(1-t)/2+P(1+t)=2+t. Take only angular mode k=1, beta_1=T_1(s_1)=s_1, all other angular modes zero (a separate constant mode may be added without changing this moment). The correct exterior strain moment at R=0 is

I_correct = integral_{-1}^1 Q(t) s_1(t)/8 dt.

The overriding method instead computes I_wrong=integral Q(t)t/8 dt=1/12. Since s_1(t)-t=((1+t_1)/(1-t_1))(t-1),

I_correct-I_wrong = -5(1+t_1)/(12(1-t_1)).

This is nonzero for every N>=1 with k=1. It follows directly from integrating (2+t)(t-1), whose integral is -10/3. This manufacture does not claim a stationary profile. It tests only that the diagnostic evaluates its input field.

## 4. Other bookkeeping and scope checks

The frozen source's RHS now returns both the projected field derivative Fp and the unprojected F. Its rho_tau norms use y*w*Fp, and its defect uses y*w*(F-Fp): this fixes the earlier labeling error. The physical clock now uses trapezoidal quadrature for both the accumulated rate and the outer exponential integral. Rollback restores the field, time, clock, predictor, accumulated rate, step and output counters. Previously appended log rows and files are not erased on rollback, so parsers must identify replayed epochs. Resume defaults an absent accumulated rate to zero; that does not reconstruct missing history. Resume's direct coefficient path checks N,M,C,basis but not L, so it can silently reinterpret coefficients on another spatial map.

The far-field predictor starts at the input's actual b3. The pure first-angular-trace forcing A1^2*(1-p)/(4*(p+3)) still has only the scope of result154. It is not a valid general-trace law. Variant B also still omits the slope factor: for rho=a*y+b*x^2*y+e*y^3 and psi=c*xy+d*x^3*y+f*x*y^3, the DR equation and slope constraint cw=cx+c give e_tau=-2*cw*e-a*f. Hence fixed e!=0 requires cw=-a*f/(2e), not -f/(2e) unless a=1. To verify, multiply the linear W_y=(cx+c)y by rho_y=a+3e*y^2 and the cubic U_y=f*y^3 by a, and compare cw*e with 3(cx+c)e+a*f. These are local exact identities.

## 5. Fixed target parameter

For the continuum equation rho_tau=cw*rho-(cx*X+U[rho]).grad rho with cx=C*cw, a stationary nonzero density and cw>0 yield rho_star=rho/cw. Linearity of the canonical inverse gives (C*X+U[rho_star]).grad rho_star=rho_star. Thus any such steady state is a profile with c_l=C. Conversely a profile rho_star at c_l=C gives the stationary DR density q*rho_star with cw=q>0 when the feedback strain is used, since its strain is q(1-C).

If, as an extra hypothesis, admissible profiles occur only for C in a discrete set, there is no admissible positive-cw continuum steady state for C outside that set. Discreteness is not proved here. This conditional absence does not force cw to decrease, approach zero, or any particular nonstationary behavior. Failure of one initial condition to approach a steady state does not exclude other basins even when C is admissible. A projected finite steady state satisfies only the projected equation unless its unprojected defect is controlled. A scan in C is a search heuristic, not an exclusion proof.

All verdicts concern the frozen source and explicit assertions. Finite condition numbers, source hashes and manufactured outputs accompany this proof in verification/. No decisive endpoint is established.

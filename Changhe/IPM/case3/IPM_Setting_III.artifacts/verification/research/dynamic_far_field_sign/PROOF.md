# Fixed-ratio dynamic rescaling: a far-field coefficient with a persistent wrong sign

Written 2026-10-21 before supporting arithmetic. Verifier result154. This is a conditional statement about time-dependent far-field coefficients and a proposed diagnostic for numerical dynamic rescaling. It does not exclude an exact Setting III profile or convergence on compact sets.

## 1. Hypotheses and exact claim

Let C>1, p=1/C, delta=1-p and s=2p-1=p-delta. Let cw(tau) be continuous and cx(tau)=C cw(tau). A sufficiently smooth, parity-preserving density rho solves

    rho_tau = cw rho - (cx X+U[rho]).grad rho,             (1)

where U is the canonical full-plane inverse defined by -Delta psi=rho_x, U=(-psi_y,psi_x), U=o(r). On every bounded time interval assume the following asymptotic expansion and its differentiated form hold uniformly:

    rho(tau,r,theta)=r^p Theta(tau,theta)+r^s B(tau,theta)+o(r^s),
    rho_tau=r^p Theta_tau+r^s B_tau+o(r^s),                (2)

with one conormal spatial derivative of the remainders having the same little-o order. Theta and B are C^1 in time with smooth angular coefficients. Assume canonical velocity has the corresponding leading expansion

    U(tau,r,theta)=r^p V[Theta(tau)](theta)+o(r^p),        (3)

uniformly on bounded time intervals. These are explicit hypotheses, not consequences asserted for an unproved DR solution. For example a time-uniform S^(s+epsilon) remainder with 0<epsilon<delta in the leading density expansion and the canonical symbol inverse yields (3). The same canonical inverse and Fourier conventions as ../smooth_angular_far_field/PROOF.md are used. Because p>0 and s>-1, the decaying harmonic velocity degrees at most-3 do not affect any coefficient considered here.

Suppose Theta(0,theta)=A sin(theta), A!=0. Define

    b3(tau)=(1/pi) integral_0^(2pi) B(tau,theta) sin(3theta)dtheta,
    lambda(tau)=(C-1)cw(tau),
    Q=A^2 delta/[4(p+3)] > 0.                            (4)

Then Theta(tau)=A sin(theta) for all times of (2), and

    b3'=lambda(tau)b3+Q.                                (5)

In particular, if b3(0)=0, then b3(tau)>0 for every tau>0. If cw>=0, then b3(tau)>=Q tau. If cw>=c0>0, then b3(tau)>=Q[exp((C-1)c0 tau)-1]/[(C-1)c0]. No assumption on the sign of cw is needed for strict positivity from zero initial data.

By contrast a steady density with the same trace, cw*=positive and cx*=Ccw*, satisfying these far-field assumptions has

    b3*=-Q/[(C-1)cw*] = -A^2/[4 C cw*(p+3)] < 0.        (6)

Thus a trajectory with b3(0)=0 cannot converge in its first subleading angular coefficient to a positive-rate steady density of this trace. A radial initial density rho0=f(r)sin(theta) has b3(0)=0 whenever the expansion (2) exists, regardless of its first-mode correction. This includes the exact constant-Q starts proposed by the numerics lane.

This is not a prohibition on compact-set convergence, nor even on convergence in a topology that does not control this subleading coefficient. In particular, asymptotic extraction as r tends to infinity and evolution as tau tends to infinity need not commute. A growing transition radius can leave b3(tau)>0 at every finite time and still yield a compact limit with b3*<0. The result identifies an obligatory lack of uniformity in such a scenario, not nonexistence.

## 2. Leading coefficient and full-plane inverse

The nonlinear advection has order r^(2p-1)=r^s by (2)-(3). Dividing (1) by r^p and letting r tend to infinity gives

    Theta_tau=(cw-cx p)Theta=0.

This proves the trace invariance. The pure leading trace has x derivative

    partial_x[A r^p sin(theta)]=(A(p-1)/2)r^(p-1)sin(2theta).

The leading particular stream solving Poisson is

    psi0=-A/[2(p+3)] r^(p+1)sin(2theta),                 (7)

since [4-(p+1)^2]*[-A/(2(p+3))]=A(p-1)/2. Here 0<p<1, so the denominator is nonzero. Cutting this density off smoothly near the origin and comparing with the canonical inverse changes the exterior velocity by a decaying harmonic expansion, beginning at degree-3. Thus (7) gives the actual leading velocity of the canonical inverse, not an artificial finite-domain choice.

Writing H=-A/[2(p+3)], its polar components are

    (U0)_r=-2H r^p cos(2theta),
    (U0)_theta=(p+1)H r^p sin(2theta).

Their advection of A r^p sin(theta) at degree s is

    F(theta)=A H[-2p cos(2theta)sin(theta)
                      +(p+1)sin(2theta)cos(theta)]
            = -A^2/[4(p+3)]
                      *[(3p+1)sin(theta)+delta sin(3theta)].  (8)

Only this leading-leading interaction contributes at degree s. Products involving the subleading density derivative are of degree p+s-1=s-delta<s; the remainders in (2)-(3) likewise contribute o(r^s).

The coefficient at degree s of (1) therefore obeys

    B_tau=(cw-cx s)B-F
         =(C-1)cw B-F.                                 (9)

The equality uses 1-Cs=C-1. Projecting (8)-(9) onto sin(3theta) proves (5), with its positive source Q. In particular the conclusion is independent of any center normalization used to determine cw, provided cw is a scalar rate and cx=Ccw.

## 3. Solution of the scalar law and its steady comparison

Put Lambda(tau)=integral_0^tau lambda(v)dv. Multiplying (5) by exp(-Lambda) and integrating yields

    b3(tau)=exp(Lambda(tau))
       *[b3(0)+Q integral_0^tau exp(-Lambda(v))dv].       (10)

The integral is strictly positive at positive time, giving the claim for b3(0)=0 at any continuous rates. For cw>=0, b3 remains nonnegative and (5) implies b3'>=Q. For cw>=c0>0, comparison with z'=(C-1)c0 z+Q, z(0)=0, gives the stated exponential lower bound; equivalently apply (10) with Lambda(tau)-Lambda(v)>=(C-1)c0(tau-v).

At a steady state with rate cw*>0, setting B_tau=0 in (9) gives B*=F/[(C-1)cw*]. Its third coefficient is exactly (6). Rescaling rho*=rho/cw* yields a Setting III profile at ell=C, and the coefficient of rho* agrees with the pure-trace first correction in ../pure_trace_resonant_logs/PROOF.md. This is also an independent normalization check: its leading amplitude is A/cw*, so multiplication of the profile correction -[A/cw*]^2/[4C(p+3)] by cw* gives (6).

Even if cw has no positive lower bound, (10) forbids b3(tau) from tending to the negative number (6). If cw>=0 for all time, the stronger linear divergence follows. Rates that turn negative do not rescue a positive-rate steady coefficient while these asymptotic hypotheses remain valid from b3(0)=0.

For constant rates, exact scalar stepping over h obeys

    b3(tau+h)=exp(lambda h)b3(tau)
                          +Q[exp(lambda h)-1]/lambda,    (11)

with the limiting value b3+Qh when lambda=0. This is a far-field method check, not a model for the full flow or a prescription to overwrite its coefficients.

## 4. Extracting the coefficient from the Q representation

The producer's fixed compactification, read but not executed, is

    t=1-2w, sigma=(1+t)/2=1-w,
    r=L sqrt(sigma)/(1-t)^kappa,
    kappa=1/delta,
    rho=y w sum_(k=0)^(M-1) sigma^k beta_k(t)cos(2k theta).  (12)

L>0 is fixed and each beta_k is polynomial in t. Define D=L^delta/2 and E_k=beta_k(1), E'_k=beta'_k(1). Then

    r^delta w=D(1-w)^(delta/2),
    w=D r^(-delta)+O(r^(-2delta)).                        (13)

Expanding (12)-(13) to first order in w gives

    Theta(theta)=D sin(theta) sum_k E_k cos(2k theta),
    B(theta)=-D^2 sin(theta) sum_k H_k cos(2k theta),
    H_k=(k+delta/2)E_k+2E'_k.                             (14)

The angular product identity sin(theta)cos(2k theta)=[sin((2k+1)theta)-sin((2k-1)theta)]/2 for k>=1 gives

    b3=-(D^2/2)(H_1-H_2),                               (15)

where absent modes count as zero. For a finite representation the trace is exactly pure first mode iff E_k=0 for k>=1, since a finite cosine polynomial equal to a constant has no higher coefficients. In that case A=D E_0 and

    b3=-D^2[E'_1-E'_2].                                 (16)

Constant-Q radial starts have beta_0 constant, beta_k=0 for k>=1; hence b3(0)=0 and A=D beta_0. Their first-mode coefficient is B_1(0)=-(delta/2)D^2 beta_0. This need not vanish, but it does not affect the third-mode law (5).

For Chebyshev coefficients beta_k(t)=sum_j u_(k,j)T_j(t), E_k=sum_j u_(k,j) and E'_k=sum_j j^2 u_(k,j). Thus (14)-(16) are finite sums directly from saved coefficients, without large-radius subtraction or radial differentiation. Using dyadic coefficients, exact rational arithmetic gives the sums; D and the exponent still depend on the chosen exact real map parameters. Floating stored C and kappa must be checked for C(1-1/kappa)=1 before interpreting them as this exact expansion. A tiny mismatch in that equality is an exponent defect, not an error to hide by extraction.

This diagnostic applies to the exact canonical evolution and to a discretization only to the extent its leading and subleading coefficient evolution is accurate. Projection in a finite trial space can change these coefficients. Logging (14)-(15), the exact scalar right side lambda b3+Q, its measured derivative, and the trace coefficients distinguishes genuine far-field evolution from a projection error. A profile search begun from a nonradial stalled state may have b3(0)!=0 and a nonpure trace; this particular sign argument then does not apply.

## 5. Dependencies, verification and limits

The proof is elementary coefficient extraction, the canonical leading Poisson inverse, and a scalar integrating factor. It requires the explicit time-uniform differentiable far-field expansion (2)-(3); local smoothness alone does not give it. No assertion of a globally existing time-dependent solution or propagation of these assumptions is made here. The intended exact checks independently verify the Cartesian advection coefficient, the rate factor, representative integrating-factor formulas, the Q-map endpoint expansion, and finite Chebyshev coefficient extraction.

Verdict: the conditional law and sign obstruction are proposed for exact verification and actual Opus5.5 review. Full-plane Setting III existence, the success of dynamic rescaling on bounded regions, the presence or absence of a tail transition, and numerical time-integrator accuracy remain OPEN. No decisive endpoint is reached.

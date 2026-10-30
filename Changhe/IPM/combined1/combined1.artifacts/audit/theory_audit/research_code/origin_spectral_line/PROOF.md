# Origin approximate spectrum in a Sobolev realization

Status: proposed T4 theorem, OPEN pending independent theory review. This is a new proof, not an application of an unverified spectral theorem. No numerical experiment is needed.

## 1. Exact spaces, realization and conclusions

Use the unitary Fourier transform on R^2 and the complexification H of H^q_S1, q>2. S1 means even in x and odd in y. The norm is

    ||h||_H^2 = integral (1+|xi|^2)^q |hat h(xi)|^2 dxi.

Let c>1. Let rho be a smooth S1 background and u its canonical divergence-free IPM velocity. Write

    V=cX+u,  U[h]=(-R1R2 h,R1^2 h),
    Lh=V.grad h-h+U[h].grad rho.

For some integer m>q, assume V is globally Lipschitz, its derivatives of orders1 through m+1 are bounded, and the derivatives of grad rho through order m are bounded. Assume exactly

    V(0)=0,  DV(0)=diag(2c-1,1),  grad rho(0)=(0,a0).       (1)

Here a0 is finite and real. Equation(1), including its strain normalization, is a hypothesis. It must be verified for an application.

Allow bounded finite-dimensional normalizations ell_1,...,ell_d on H. Choose g_j in H with Lg_j in H and ell_i(g_j)=delta_ij. Set

    P=I-sum_j g_j ell_j,   H0=intersection_j ker ell_j.

The case d=0 is included. Let A be a closed densely defined operator on H0. Assume its domain contains P E_epsilon w for every S1 Schwartz function w with smooth compact Fourier support away from both coordinate axes, and every 0<epsilon<=1, where

    E_epsilon w(X)=epsilon^(q-1) w(X/epsilon).

On these functions assume A=PL+K, where K:H0->H0 is compact. No assertion that these functions form a core, or that A is a generator, is needed. The identity on this specified test class is needed.

Put

    d0=2c-2,
    alpha_v=q-c-1,
    B=2q(c-1)-a0,
    alpha_h=alpha_v+B=q(2c-1)-c-1-a0.                     (2)

Then every point of each vertical line alpha_v+iR and alpha_h+iR has a singular sequence for A: for each such lambda there are v_n in D(A) with

    ||v_n||_H=1,  v_n weakly ->0 in H,
    ||(A-lambda)v_n||_H ->0.                              (3)

If B<0, every lambda in the closed strip

    alpha_h <= Re lambda <= alpha_v                       (4)

also has a sequence(3). In particular A-lambda is not bounded below and is not upper semi-Fredholm at any of these lambda. Upper semi-Fredholm here means closed range and finite-dimensional kernel.

For z in the resolvent set of A, each of the two lines yields

    ||(z-A)^(-1)|| >= 1/|Re z-alpha_v|,
    ||(z-A)^(-1)|| >= 1/|Re z-alpha_h|.                    (5)

An infinite right side means z cannot be a resolvent point. Under B<0 the sharper distance-to-strip statement follows in the same way.

If A generates a strongly continuous semigroup S(t), then

    ||S(t)|| >= exp(max(alpha_v,alpha_h)t), t>=0.          (6)

Thus finite-prefactor decay ||S(t)||<=C exp(-beta t) requires beta<=-max(alpha_v,alpha_h). Equivalent Hilbert norms preserve the spectral conclusions and this necessary decay exponent. They need not preserve the exact constants in(5) or(6).

These are conclusions for the specified H^q realization. They are not yet claims for the campaign's weighted or dyadic graph spaces.

## 2. Frozen Fourier operator and a unitary logarithmic chart

The frozen operator is

    L0w=DX.grad w-w-a0 Qw,   D=diag(2c-1,1),
    hat Qw(xi)=p(xi)hat w(xi),  p(xi)=xi_x^2/|xi|^2.

The sign of the last term follows from the negative symbol of R1^2. Fourier transformation gives

    hat L0w=-(Dxi).grad_xi hat w-(2c+1)hat w-a0 p hat w.   (7)

On the positive frequency quadrant introduce

    u=log xi_y,   v=log(xi_x/xi_y),
    xi_y=exp(u),  xi_x=exp(u+v).

The Jacobian is exp(2u+v); also |xi|^(2q)=exp(2qu)(1+exp(2v))^q. A function on this quadrant extends uniquely with S1 parity to the other three quadrants. Accordingly

    g(u,v)=2 exp((q+1)u+v/2)(1+exp(2v))^(q/2)
                hat w(exp(u+v),exp(u))                   (8)

is a unitary map from the homogeneous dot H^q S1 space to L2(du dv). The factor2 accounts for the four quadrants. For compactly supported smooth g, the inverse Fourier data are smooth, compactly supported away from the axes and the origin. Their inverse transform is Schwartz.

Since (Dxi).grad_xi=partial_u+d0 partial_v, differentiating the weight in(8) shows exactly

    W L0 W^(-1) g
       =-partial_u g-d0 partial_v g
          +(alpha_v+B p(v))g,
    p(v)=exp(2v)/(1+exp(2v)).                             (9)

For clarity, the constant is (q+1)+d0/2-(2c+1)=q-c-1, and the p coefficient is d0 q-a0. These computations fix both signs in(2).

## 3. Singular sequences for both boundary lines

Fix tau real and a real chi in C_c^infinity((-1,1)) with ||chi||_2=1. For M>2 put

    g_M^v(u,v)=M^(-1) chi(u/M) chi((v+M^2)/M) exp(-i tau u).

Its L2 norm is1. On its support p(v)<=exp(-2M^2+2M). Equation(9) therefore gives, for lambda=alpha_v+i tau,

    ||(W L0 W^(-1)-lambda)g_M^v||_2
       <= (1+d0)||chi'||_2/M+|B|exp(-2M^2+2M) ->0.        (10)

Replace v+M^2 by v-M^2. On that support 1-p(v)<=exp(-2M^2+2M), giving the same conclusion at lambda=alpha_h+i tau. Inverse transformation gives Schwartz w_M with ||w_M||dotHq=1 and ||(L0-lambda)w_M||dotHq->0. For tau=0 these w_M may be chosen real by multiplying the positive-quadrant data by i and extending with S1 parity.

## 4. Interior strip when B<0

Suppose alpha_h<sigma<alpha_v. The positive function

    phi_sigma(v)=exp((alpha_v-sigma)v/d0)
                       (1+exp(2v))^(B/(2d0))             (11)

solves

    -d0 phi_sigma'+(alpha_v+Bp(v))phi_sigma
        =sigma phi_sigma.

At negative infinity its exponential rate is (alpha_v-sigma)/d0>0; at positive infinity its rate is (alpha_h-sigma)/d0<0. Thus phi_sigma belongs to L2(R), and is smooth. Choose eta in C_c^infinity(R), equal to1 on[-1,1], and let eta_M(v)=eta(v/M). Write b_M=||eta_M phi_sigma||_2; then b_M tends to the positive finite number ||phi_sigma||_2. Define

    g_M(u,v)=M^(-1/2)b_M^(-1) chi(u/M) eta_M(v)
                    phi_sigma(v) exp(-i tau u).

It is smooth, compactly supported, and has L2 norm1. The exact eigenfunction equation cancels the zeroth-order v terms. At lambda=sigma+i tau, the residual norm is at most

    ||chi'||_2/M
       +d0 ||eta'||_infinity ||phi_sigma||_2/(M b_M),      (12)

which tends to zero. Inverse transformation again gives compact-frequency Schwartz w_M with unit homogeneous norm and vanishing homogeneous residual. The endpoints are already covered by Section3. This proves the entire closed strip for the frozen problem.

No interior-strip assertion is made here when B>0. The two boundary lines remain valid in that case.

## 5. Shrinking each frozen test into the origin

For every fixed Schwartz f,

    ||E_epsilon f||_H^2
        =integral (epsilon^2+|eta|^2)^q |hat f(eta)|^2 deta
        ->||f||dotHq^2,                                  (13)

and ||E_epsilon f||_H<=||f||_H for epsilon<=1. For compact Fourier support away from zero, E_epsilon f is weakly null in H as epsilon->0: its frequency support escapes every bounded set and its H norm is bounded.

Homogeneity of U gives the exact residual identity

    L E_epsilon w-E_epsilon L0w=E_epsilon R_epsilon(w),
    R_epsilon(w)=(V(epsilon X)/epsilon-DX).grad w
         +(grad rho(epsilon X)-(0,a0)).U[w].              (14)

For each fixed test w used above, R_epsilon(w)->0 in H^m. To check this assertion rather than assume a localization principle, the first coefficient in(14) converges pointwise to zero and is bounded by C|X|. Its first derivatives are bounded and converge pointwise to zero. Its derivatives of order k>=2 are epsilon^(k-1)D^k V(epsilon X), which are bounded and tend to zero. The second coefficient and its derivatives through order m are bounded and tend pointwise to zero. Both w and U[w] are Schwartz because their Fourier supports avoid zero. Apply Leibniz' rule through integer order m and dominated convergence to every term. Equation(13) then bounds ||E_epsilon R_epsilon(w)||_H by a quantity tending to zero.

This argument is for each fixed w_M. No uniform estimate in M is required: epsilon will be chosen after M.

## 6. Bounded pinning, compact perturbations and diagonal choice

For fixed w put z_epsilon=P E_epsilon w. Weak convergence implies

    z_epsilon-E_epsilon w ->0 in H,
    ell_j(E_epsilon w)->0.

Expanding with the assumed realization gives

    (A-lambda)z_epsilon
      =P E_epsilon(L0-lambda)w +P E_epsilon R_epsilon(w)
          -sum_j ell_j(E_epsilon w) P Lg_j+Kz_epsilon.    (15)

Every displayed quantity is defined in H by the domain assumptions. Compactness and weak convergence give Kz_epsilon->0. For fixed w, the first term differs from E_epsilon(L0-lambda)w by a quantity tending to zero, since L0 preserves the compact frequency support and its residual is weakly null after scaling. In particular no factor ||P|| is needed in the limiting homogeneous norm.

For each w_M choose epsilon_M small enough that all the localization, projection and compact errors in(15) are below1/M, and that | ||P E_epsilon_M w_M||_H-1 |<1/M. Require also that the smallest frequency in the unprojected Fourier support exceeds M and ||P E_epsilon_M w_M-E_epsilon_M w_M||_H<1/M. This finite list is achievable for each fixed M. Normalize z_M=P E_epsilon_M w_M to unit norm. Equations(10) or(12), followed by(13)-(15), prove the residual limit in(3). The escaping frequency supports and vanishing projection error prove weak convergence in(3).

The canonical strain ell(h)=partial_y U2[h](0) is continuous on H for q>2. Indeed Fourier Cauchy-Schwarz reduces this to finiteness of integral |xi|^2(1+|xi|^2)^(-q) dxi. This includes the full canonical multiplier; no local/contact term is removed. Other pinning choices must independently satisfy boundedness. A far-field amplitude functional that is not bounded on H is not covered by this argument.

## 7. Spectral, inverse and semigroup consequences

A bounded inverse of A-lambda contradicts(3) immediately. If A-lambda had closed range and finite-dimensional kernel N, its inverse on the quotient by N would be bounded, by the closed graph theorem. Equivalently there would be C with

    ||v||_H<=C||(A-lambda)v||_H+||Pi_N v||_H, v in D(A).

The finite-rank projection Pi_N sends the weakly null sequence(3) to zero, a contradiction. This proves the stated failure of upper semi-Fredholmness without choosing among conventions for essential spectrum.

For z in the resolvent set, apply (z-A)^(-1) to (z-A)v_n. The norm of the latter tends to |z-lambda|, so the inverse norm is at least1/|z-lambda|. Choose Im lambda=Im z and either boundary line to prove(5), or minimize over the strip when available.

If A generates S(t), the classical-path Duhamel identity gives for each fixed t

    S(t)v_n-exp(lambda t)v_n
       =integral_0^t S(t-s)exp(lambda s)(A-lambda)v_n ds.

A strongly continuous semigroup is norm bounded on each compact time interval, so the right side tends to zero. Thus ||S(t)||>=exp(Re lambda t). The two boundary lines prove(6). Taking t->infinity proves the necessary decay exponent with a finite prefactor. Equivalent norms preserve bounded invertibility, weak convergence and vanishing residual, and change any semigroup estimate by only a fixed multiplicative factor.

## 8. Scope for the present campaign

The vertical line alpha_v=q-c-1 recovers the earlier origin semigroup obstruction and strengthens it to an approximate-spectrum and inverse statement under this explicit Sobolev realization. For q=2+s<c+1, it imposes the necessary inverse floor1/(c-1-s) if a stationary inverse exists. This floor alone is far below the baseline constant20 for small s.

The strip adds a different obstruction: if

    q>=c+1 and q(2c-1)<=c+1+a0,                           (16)

then zero lies in the closed strip, so no bounded stationary inverse exists on this realization. In particular, a pure H^3 realization is obstructed whenever 1<c<=2 and a0>=5c-4. Both inequalities are explicit background tests; no approximate decimals are needed for their formulation. The state131 values reported in the campaign would satisfy these inequalities with a wide margin, but an application must match exact values and the realization before a matrix verdict changes.

Finite-dimensional bounded pinning and compact H-to-H corrections cannot remove these singular sequences. A different, non-equivalent norm, stronger admissible-domain restriction excluding the test class, or a noncompact change of the principal origin operator is not covered. In particular this note does not assert(16) for Y, for a weighted third-order energy, or for a graph norm containing nonlocal velocity terms. Such a transfer requires its own norm and residual proof. It also does not identify a true eigenfunction of the full variable-coefficient operator, and does not rule out the nonlinear profile problem.

Dependencies: elementary Fourier calculus, the stated coefficient hypotheses, dominated convergence, bounded pinning, compactness, and the closed graph theorem. The semigroup corollary uses only the displayed Duhamel identity. An external search for semigroup references was made, but no external result beyond these explicitly proved steps is imported. This note needs independent Opus review before being treated as audited theory.

# An origin lower bound for Sobolev semigroup growth

## Exact setting and statement

Work on R^2 with the unitary Fourier transform and the real Hilbert space H^q_S1, where q>2 and S1 means even in x and odd in y. Its norm is the Bessel-potential norm. Let c>1, let rho be a smooth S1 background, and let u be its smooth canonical divergence-free IPM velocity. Put

    V=cX+u,   U[h]=(-R1R2 h,R1^2 h),
    Lh=V.grad h-h+U[h].grad rho.

Assume V is globally Lipschitz, all its derivatives of orders1 through m+1 are bounded, and all derivatives of grad rho through order m are bounded, for some integer m>q. Assume

    V(0)=0,   DV(0)=diag(2c-1,1),   grad rho(0)=(0,a0),

where a0 is any finite real number. These origin identities follow from the usual parity, divergence and normalized vertical strain conditions, but they are explicit hypotheses here.

The statement also allows finitely many bounded linear normalizations. Let ell_1,...,ell_d be continuous real linear functionals on H^q_S1. Choose g_j in the smooth domain of L with ell_i(g_j)=delta_ij, and define

    P=I-sum_j g_j ell_j,   H0=intersection_j ker ell_j.

The case d=0 is allowed. The canonical strain ell(h)=partial_y U2[h](0) is a permitted functional when q>2: U2 is bounded on H^q and the first derivative evaluation is continuous by Fourier Cauchy-Schwarz, since integral |xi|^2(1+|xi|^2)^(-q) dxi is finite.

Assume A generates a strongly continuous semigroup S(t) on H0 and, on the projected smooth test functions used below,

    A h=P Lh+K h,

where K:H0->H0 is compact. Assume this smooth test class and the g_j belong to the stated differential domain; no existence or domain theorem for a new PDE generator is inferred from this hypothesis. Then, for every t>=0,

    ||S(t)||_(H0,H0) >= exp((q-c-1)t).                    (1)

Consequently, if ||S(t)||<=C exp(-beta t) for all t>=0 and some finite C, then

    beta<=c+1-q.                                         (2)

The same necessary exponent holds for every norm equivalent to the inherited H^q norm. In particular q>=c+1 excludes a positive exponential decay rate even when a finite transient prefactor is allowed. This concerns semigroup bounds on the specified Sobolev realization. It does not exclude a stationary inverse, a non-equivalent high norm, or a different function space.

## 1. The frozen origin evolution

Set D=diag(2c-1,1). Freezing at the origin gives

    L0 w=DX.grad w-w-a0 Qw,
    Fourier(Qw)(xi)=xi_x^2/|xi|^2 Fourier(w)(xi).

The sign follows from U2=R1^2, whose symbol is -xi_x^2/|xi|^2. Choose a nonzero Schwartz w0 whose Fourier transform is smooth and compactly supported away from zero. Choose its symmetry so that w0 is real and S1. For example use equal even packets in xi_x and imaginary odd packets around xi_y=1 and xi_y=-1.

The exact solution w(t)=exp(t L0)w0 has Fourier transform

    what(t,xi)=exp(-(2c+1)t-a0 integral_0^t p(exp(-sD)xi) ds)
                    what0(exp(-tD)xi),
    p(eta)=eta_x^2/|eta|^2.

This is checked directly in the Fourier equation

    partial_t what=-(Dxi).grad_xi what-(2c+1)what-a0 p(xi)what.

For each finite time interval, w(t) is a continuous Schwartz family with Fourier support in a compact set disjoint from zero. Changing variables xi=exp(tD)eta gives

    ||w(t)||dotHq^2
      =exp(-2(c+1)t) integral |exp(tD)eta|^(2q)
          exp(-2a0 integral_0^t p(exp(rD)eta) dr)
          |what0(eta)|^2 deta.                           (3)

For a fixed T, restrict the support to arbitrarily narrow cones around the two vertical directions, with radii in a fixed compact annulus. Uniformly for 0<=r<=T, p(exp(rD)eta) tends to zero and |exp(TD)eta|/|eta| tends to exp(T) as the cone angle tends to zero. Equation(3) therefore gives

    sup_(such w0) ||w(T)||dotHq/||w0||dotHq
       >=exp((q-c-1)T).                                  (4)

This is a finite-time limiting statement. The cone is allowed to depend on T; no fixed packet is asserted to remain vertical for infinite time.

## 2. Shrinking the exact model toward the origin

For 0<epsilon<=1 set

    E_epsilon w(X)=epsilon^(q-1) w(X/epsilon).

The homogeneous norm is invariant. More precisely,

    ||E_epsilon w||Hq^2
      =integral (epsilon^2+|eta|^2)^q |what(eta)|^2 deta
       ->||w||dotHq^2.                                  (5)

For the preceding compact Fourier supports the convergence is uniform for t in [0,T]. The same family is weakly null in H^q as epsilon tends to zero, because its Fourier support escapes every bounded frequency set and its H^q norm stays bounded. This weak convergence also holds uniformly against each fixed continuous linear functional over t in [0,T], by compactness of the continuous Schwartz family and uniform boundedness of E_epsilon:H^q->H^q.

Homogeneity of U gives the exact identity

    L E_epsilon w-E_epsilon L0w=E_epsilon R_epsilon(w),
    R_epsilon(w)=(V(epsilon X)/epsilon-DX).grad w
                  +(grad rho(epsilon X)-(0,a0)).U[w].    (6)

For every t in [0,T], R_epsilon(w(t)) tends to zero in H^m, uniformly in t. Here is a direct domination argument. The vector coefficient in its first term tends to zero pointwise and is bounded by a constant times |X|. Its first derivatives are uniformly bounded and tend to zero; derivatives of order k>=2 are epsilon^(k-1) D^k V(epsilon X), hence bounded and pointwise vanishing. The second coefficient and its derivatives are bounded and pointwise vanishing. The functions w(t) and U[w(t)] form bounded Schwartz families; the latter assertion uses the Fourier support away from zero. Leibniz' rule and dominated convergence prove the claim for every integer derivative through m, uniformly by compactness of the time family. Since m>q, (5) bounds the H^q norm of E_epsilon R_epsilon by its H^m norm. Thus the right side of(6) tends to zero in H^q uniformly on [0,T].

## 3. Exact normalization, compact corrections and Duhamel

Define z_epsilon(t)=P E_epsilon w(t). Boundedness of ell_j and the weak convergence above imply

    ||z_epsilon(t)-E_epsilon w(t)||Hq ->0

uniformly on [0,T]. The same holds with w replaced by partial_t w=L0w. The differential-domain hypotheses make z_epsilon a C^1 classical test path. Expanding A z_epsilon-partial_t z_epsilon yields

    P E_epsilon R_epsilon(w)
      -sum_j ell_j(E_epsilon w) P L g_j
      +K z_epsilon.

The first two terms tend to zero uniformly. The last does as well: compact operators send bounded weakly-null sequences to strongly-null sequences, and the continuous time family reduces the uniform assertion to a finite approximation. Hence the residual tends to zero uniformly on [0,T].

A strongly continuous semigroup is uniformly bounded on each compact time interval. Duhamel's identity therefore gives

    ||S(T) z_epsilon(0)-z_epsilon(T)||Hq
       <= sup_(0<=s<=T)||S(s)|| integral_0^T
                   ||A z_epsilon(s)-partial_s z_epsilon(s)||Hq ds
       ->0.

Divide by ||z_epsilon(0)||Hq, use(5), and then take epsilon to zero:

    ||S(T)||>=||w(T)||dotHq/||w0||dotHq.

Finally narrow the Fourier cones and apply(4). This proves(1) for arbitrary T. Taking logarithms in (1)<=C exp(-beta t) and sending t to infinity proves(2). Equivalent norms change only the finite multiplicative constant, so they preserve the necessary exponent.

## Dependencies, verification and scope

The proof is self-contained beyond elementary Fourier calculus, the compact-operator criterion, boundedness of a strongly continuous semigroup on compact time intervals, and Duhamel's identity for a classical test path, which is obtained by differentiating S(T-s)z(s) and integrating. It does not assume a new high-space generator exists. It extends the earlier origin numerical-range obstruction only for the explicitly stated Sobolev realization and projected domain. No claim is made here for the nonlocal dyadic graph norm Y; its norm and residual limits would need an additional proof.

This is new T4 theory, OPEN pending independent T1/T2 review. No numerical experiment is needed. In particular this proof must not be used to mark an inverse or closure row excluded until its generator and norm hypotheses are matched to that row.

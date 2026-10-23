# Formal slow-radius identities without a two-mode closure

Date: 2026-10-20. Status: independent formal coefficient derivation. The original exact coefficient tests passed at 2026-10-20T17:26Z. The additional truncation obstruction below is separately checked. This is not an asymptotic theorem about every profile with a small origin slope, and is not a nonexistence proof.

## 1. Statement and scope of the formal regime

The full-plane profile equations are W.grad rho=rho, W=ell X+U, U=(-psi_y,psi_x), -Delta psi=rho_x, with the canonical sublinear inverse and density even in x, odd in y. Put D=ell-1>0 and sigma=D log r. In this document h' means the derivative in sigma. Consider the formal ansatz

    rho=r[D h(sigma)sin theta+D^2 H(sigma,theta)+...],
    H=sum_(j=3,5,...) h_j(sigma)sin(j theta).                 (1)

Assume the displayed coefficients are smooth, their sigma derivatives have the uniform bounds needed for the formal expansions, their angular series can be differentiated termwise, h tends to zero at positive infinity, and J_3(sigma)=integral_sigma^infinity h_3 is convergent. These conditions describe the formal calculation. Their validity for actual profiles has not been proved.

Define

    F=1-h/4+J_3, C=F-1.

Extraction of the displayed powers in the canonical modal inverse and transport gives

    h'=-h F, F'=h F/4-h_3,                                (2)
    h_3'=-(1-h/2)h_3+[3C-3h/4]h_5
                         +hF(1/2-F/2-h/16),              (3)
    h_j'=-(1-h/2)h_j
       -(j-3)[C/2+h/(4(j+1))]h_(j-2)
       +(j+3)[C/2-h/(4(j-1))]h_(j+2), j>=5 odd.           (4)

These equations retain all angular coefficients at the D^2 density order. Equivalently they are the angular projected equation (9) below. The equation for h_3 is extracted at transport order D^3, because the leading degree-one Euler transport cancels the density itself. Thus the phrase "the same order" refers to the density order, not to a nonzero D^2 transport residual in a higher mode.

Setting all h_j with j>=5 equal to zero gives the lead's two-mode model, but is consistent with the full hierarchy only if the omitted equations also vanish. In particular the first omitted equation is

    h_5'=-(1-h/2)h_5-[C+h/12]h_3+[4C-h/2]h_7.             (5)

The forced term -[C+h/12]h_3 is generally nonzero. A finite two-mode computation cannot be described as a controlled leading approximation without an independent estimate of these omitted modes.

## 2. The resonant mode-two stream and its additive remainder

Write rho_j(r)=r b_j(sigma). Direct differentiation gives the sin(m theta) coefficient of rho_x:

    f_m=[D b_(m-1)'+(2-m)b_(m-1)
                        +D b_(m+1)'+(m+2)b_(m+1)]/2.     (6)

Here b_1=D h and b_j=D^2 h_j for j>=3. Consequently

    f_2=D^2(h'/2+2h_3)+D^3 h_3'/2+... .

The canonical Poisson formula for this mode is

    psi_2/r^2=(1/4)[r^-4 integral_0^r s^3 f_2(s)ds
                               +integral_r^infinity f_2(s)ds/s].

The inner integral of the displayed leading coefficient is O(D^2), under the indicated slow-derivative bounds. The outer integral uses ds/s=d sigma/D. Since h(infinity)=0, it follows that

    psi_2/r^2=D[-h/8+J_3/2]+O(D^2)=D C/2+O(D^2).          (7)

The remainder is additive. Multiplying the leading expression by (1+O(D)) would fail where that expression vanishes. The leading linear strain seen at a fixed slow radius is c_loc=D C=D(F-1). At the origin the exact strain identity c=-a0/4+integral rho_3/r^2 gives the same expression. If a0=D alpha and the unforced origin relation c=-D holds, the formal boundary conditions are h(-infinity)=alpha and F(-infinity)=0. The definition gives F(infinity)=1.

An omitted higher-order sin3 density coefficient contributes a next-order, mode-two linear strain. At order D^3 in transport it acts on the leading density Dr h sin theta only in mode one. It therefore does not affect the high-mode equations (3)-(4). The same is true of a next-order sin1 coefficient. This is why the projected coefficient calculation can be performed without determining the complete next-order strain.

## 3. Nonresonant stream modes and the projected angular equation

For m>=4 even, the leading source coefficient in (6) is D^2[(2-m)h_(m-1)+(m+2)h_(m+1)]/2. Since -Delta(r^2 sin m theta)=(m^2-4)sin m theta, the corresponding stream is

    D^2 r^2 Phi, Phi=sum_(m=4,6,...) phi_m sin m theta,
    phi_m=h_(m+1)/[2(m-2)]-h_(m-1)/[2(m+2)].               (8)

The leading mode-two stream Dr^2 C sin2theta/2 has radial and angular velocities -Dr C cos2theta and Dr C sin2theta. Its radial differentiation also contributes D^2 r F' sin2theta/2 to the angular velocity. The remaining D^2 mode-two term is a linear strain and contributes only in mode one at the order considered.

The D^2 sin1 transport coefficient is h'+h+C h, giving the first equation in (2). Differentiating F gives its second equation. For H define S H=-cos2theta H+sin2theta H_theta. Projecting the D^3 transport coefficient onto all odd modes j>=3 gives

    P_>=3[H_sigma+H+C S H
                +h(2Phi cos theta-Phi_theta sin theta)
                +G_3 sin3theta]=0,
    G_3=-C h'/2+hF'/4.                                   (9)

The first term in G_3 comes from the radial derivative of h under the leading linear strain. The second comes from the sigma derivative of its mode-two stream. Substitution of (2) gives

    G_3=hF[C/2+h/16]-h h_3/4.

Thus the nonlocal strain contribution has not been discarded when reducing to (9).

For each odd j,

    S sin(j theta)=(j-1)sin((j+2)theta)/2
                            -(j+1)sin((j-2)theta)/2.

For each even m, the Cartesian second velocity component generated by r^2 phi_m sin(m theta), divided by r, is

    (2-m)phi_m sin((m+1)theta)/2
                            +(2+m)phi_m sin((m-1)theta)/2.

Use (8). Its j=3 coefficient is -h_3/4+3h_5/4. For j>=5 it is

    -h_j/2+(j-3)h_(j-2)/[4(j+1)]
                       +(j+3)h_(j+2)/[4(j-1)].           (10)

Equating coefficients in (9), then substituting G_3, proves (3)-(4). In particular the j=5 equation is (5), and the identity S sin5=2sin7-3sin3 agrees with the lead's stated feedback mechanism.

## 4. What the formal calculation does not exclude

The origin slope bound a0=O(D) gives no uniform global bound on the shape or its canonical strain. Even the ansatz rho=Dr h(sigma,theta) with a general O(1) sin3 component produces an O(1) mode-two strain: its outer inverse integrates an O(D) source over a log-radius interval of length O(1/D). Then U.grad rho need not be O(D^2 r). The special size D^2 of higher modes in (1) is substantive.

Likewise an assertion that no fast radial layer occurs would require uniform amplitude, derivative and inverse estimates through such layers. Merely putting s=log r and observing h_s=0 at a formal lowest order does not supply those estimates. An actual profile can leave a formal regime, concentrate on a different scale, or have components not represented by (1). The linear rates of (2)-(4) can motivate regularity tests only after an appropriate asymptotic theorem has been proved.

At fixed alpha, the source equilibrium is (h,F,H)=(alpha,0,0). Its linearization is explicitly

    delta h'=-alpha delta F,
    delta F'=alpha delta F/4-delta h_3,
    delta h_3'=(-1+alpha/2)delta h_3
                 +(-3-3alpha/4)delta h_5
                 +alpha(1/2-alpha/16)delta F,

with (4) linearized using C=-1,h=alpha. At alpha=8 the subspace with all delta h_j=0 has the eigenvalue2 in delta F. At alpha=12 the subspace involving delta F,delta h_3 closes because the h_3 coefficient in the h_5 equation vanishes; its eigenvalues are2 and6. These exact algebraic special cases explain the corresponding leading smooth-angular lattice values, without endorsing a two-mode truncation at general alpha.

## 4A. Exact spectrum of every finite invariant source block

Within the formal hierarchy, the following is an exact all-N algebraic theorem. For any integer N>=0 set alpha=8+4N. At the source equilibrium (h,F,H)=(alpha,0,0), the linear subspace with h_j=0 for j>=2N+3 is invariant. On the variables F,h3,...,h_(2N+1), its eigenvalues are exactly

    2,6,10,...,4N+2.                                     (11)

The independent h variation adds a zero eigenvalue to the full source linearization; it does not change these transverse eigenvalues.

For proof, label these transverse variables z0=delta F and z_n=delta h_(2n+1), 1<=n<=N. The first omitted lower coupling vanishes because the coefficient of h_(2N+1) in the h_(2N+3) equation is proportional to alpha-(8+4N). For N=0 the h3 forcing from F is alpha(1/2-alpha/16)=0. This proves invariance, including the endpoint N=0.

The retained matrix has diagonal entries N+2 at n=0 and 2N+3 at n>=1. Its adjacent entries are negative, with products

    M_(n,n+1) M_(n+1,n)=(N-n)(N+n+2), 0<=n<N.           (12)

For n=0 the factors are -1 and -N(N+2). For 1<=n<N they are -(n+2)(N+n+2)/n and -n(N-n)/(n+2). A positive diagonal similarity makes the matrix symmetric with adjacent entries minus the square roots of (12); changing alternate coordinate signs makes them positive. After subtracting (2N+3)I, its diagonal is -(N+1),0,...,0.

This last matrix has an elementary polynomial realization. Let L=2N+1, and consider the operator T=x partial_y+y partial_x on homogeneous polynomials of degree L, in the basis

    e_k=sqrt(binomial(L,k)) x^k y^(L-k), 0<=k<=L.

Its diagonal entries are zero and its adjacent entries are sqrt((k+1)(L-k)). Reflection x<->y sends e_k to e_(L-k) and commutes with T. On its antisymmetric subspace choose the ordered basis

    f_n=(e_(N-n)-e_(N+1+n))/sqrt(2), 0<=n<=N.

The matrix then has diagonal -(N+1),0,...,0 and adjacent entries sqrt((N-n)(N+n+2)), exactly the centered source block above. Meanwhile the eigenpolynomials (x+y)^(L-j)(x-y)^j have eigenvalues L-2j and reflection parity (-1)^j. The antisymmetric subspace therefore has eigenvalues L-2j for odd j=1,3,...,2N+1. Adding 2N+3 gives precisely the set (11), proving the all-N claim without inferring it from a finite determinant experiment.

The parameters match the leading small-D limit of the independently proved smooth-angular indicial lattice: A=1+2D, d=(2m+1)A-2m gives (d-1)/D=2+4m, and a=(A-1)[(2m+1)A+2n+3] gives a/D=8+4(m+n)+O(D). This agreement is a coefficient check. It does not show that an actual small-D smooth profile belongs to the formal regime (1), or that a finite angular truncation approximates such a profile.

## 4B. No nonconstant exact two-mode trajectory in this hierarchy

This is an algebraic consequence of the full formal hierarchy, not a theorem about the original PDE. Suppose a smooth solution of (2)-(4) on a connected interval has h nonzero and h_j identically zero for j>=5. Then it is constant, with F=0 and h_3=0. In particular, no such two-mode solution can connect a nonzero source to h=0 at positive infinity.

Write k=h_3. The omitted j=5 equation implies (C+h/12)k=0. If k is nonzero at one point, it is nonzero on an open interval, where C=-h/12, F=1-h/12 and h'=-h(1-h/12). Since C'=F'= -h'/4-k and also C'=-h'/12, we have k=-h'/6=h(1-h/12)/6. Differentiating this identity and comparing it with the retained k equation gives

    derivative[h(1-h/12)/6] - RHS_of_(3) = 5 h h'/144.

Both sides must be zero. Because h is nonzero, h'=0, and then k=-h'/6=0, a contradiction. Thus k vanishes everywhere. Now F'=-h'/4 and (3) reduces to

    h F(C/2+h/16)=0.

If h' were nonzero on some open interval, hF=-h' would be nonzero there, forcing C=-h/8. Differentiation would give C'=-h'/8, contrary to C'=-h'/4. Hence h'=0 everywhere. Equation (2) then gives F=0. This proves the assertion without dividing by k at one of its zeros. The zero solution h=0 is excluded by the stated nonzero hypothesis; uniqueness for h'=-hF shows that any smooth h is either everywhere nonzero on a connected interval or identically zero.

The result applies to exact solutions of the retained infinite formal equations. An approximation that neglects k or higher modes still needs an error bound; this argument neither supplies such a bound nor excludes a solution with infinitely many modes. It independently confirms P3 of the lead's slow1 audit.

## 5. Numerical experiment and dependencies

A finite truncation of (2)-(4) can be integrated from formal forced-core data h(0)=alpha,F(0)=F0,h_j(0)=0 and shot toward F(infinity)=1. Its endpoint is a property of that truncated model only. Angular truncation, integration length and tolerance must be varied; a fold or failure of a truncation is not nonexistence for the exact full-plane PDE. A small-D forced-core boundary layer and passage from the original canonical inverse to this hierarchy remain unproved.

The derivation uses the independently checked canonical modal formula and direct trigonometric differentiation. It does not import the numerical lane's implementation. Exact checks, and any subsequent finite-hierarchy runs, are stored in verification and separately labeled as algebraic or numerical evidence.

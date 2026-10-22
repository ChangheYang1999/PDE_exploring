# Smooth realization of every vorticity jet on the whole axis

Written 2026-10-21T04:31:22.052375+00:00, before packet123 computations.

Status: CONFIRMED after independent exact controls and actual Opus160/161 written audits, completed 2026-10-21T04:42:08.061035+00:00. No full B2 profile is asserted. The theorem concerns infinite-order residual vanishing on a closed set and exactness on an unspecified small disk.

## Statement and precise scope

For every beta>2 and a0>0 there are smooth full-plane fields Psi, Omega=-Delta Psi and Theta, with Psi and Omega odd in x and Theta even in x, such that, for U=(-Psi_y,Psi_x), V=U-U(0) and W=beta X+V:

1. V is the canonical whole-plane relative inverse; U=o(r), DU=O(r^(-1/beta)); Omega has a nonzero uniform r^(-1/beta) angular tail and Omega>0 for x>0.
2. Theta(0,y)=0, Theta>0 off the axis, Theta=a0x^2+O(r^3), and W.grad Theta=(beta-2)Theta everywhere. It has a polynomial growth bound.
3. Psi_xy(0)=1+beta/2, Omega_x(0)=4a0/beta, and every backward W trajectory tends to0.
4. Every Cartesian derivative of R=W.grad Omega+Omega-Theta_x vanishes at every point of the entire axis x=0.
5. Both transport equations hold exactly on a sufficiently small disk about0.

Relative to the explicit field Psi_e below, Omega-Omega_e is supported in a fixed strip |x|<=x0 and obeys |Omega-Omega_e|<=C|x|(1+|y|)^(-1-1/beta), and |U-U_e|<=C(1+|y|)^(-1-1/beta). The constants and the disk radius depend on beta,a0 and the construction. No bound is claimed on the growth of all high Cartesian derivatives at infinity. The stated admissible field/tail class in SPEC A1-A4 requires none. No analyticity or convergence of a formal x series is asserted. No vanishing on a neighborhood of the whole axis, no exactness on a prescribed large disk, and no full vorticity PDE on the plane follows.

## Base field and elementary inputs

Put l=(beta-2)/2, mu=1+3beta/2, c=1+beta/2, q0=4a0/beta, Lambda=2mu and M=2beta+1. Let s=1/beta, p=(1-s)/2,

    L=3c sqrt(beta)/(4a0), h=sqrt(beta)L,
    S=L^2+x^2+(y-h)^2, S0=L^2+h^2,
    B=c/(2ph S0^(p-1)), Psi_e=-BxS^p.

Then Omega_e=4Bp xS^(p-2)[2L^2+(p+1)(x^2+(y-h)^2)]>0 for x>0. Packet119 proves directly that W_e,1/x>=l, b_e'>=l for b_e=W_e,2(0,y), that its center data are c,q0, and that its velocity is canonical relative, sublinear, with bounded derivative and the declared slow tail. It proves the following flow fact. For any smooth relative W preserving DW(0)=diag(l,mu), with W1/x>=kappa>0, b'(y)>=kappa>0, b(0)=0, and bounded DU, every backward trajectory tends to0. Indeed |x(-t)|<=e^(-kappa t)|x0| and |y(-t)|<=e^(-kappa t)(|y0|+C|x0|t). There is then a smooth

    xi=x exp[-int_0^infinity (W1/x-l)(phi_(-t)X)dt],
    W.grad xi=l xi, xi_x(0)=1, Theta=a0xi^2.

Local contraction of every flow variation justifies all derivatives of this integral, as proved there; extension by finite backward entry gives its global smoothness. Sublinearity gives entry into a fixed ball in time at most (2/beta)log(r/R0), hence |Theta|<=C(1+r)^[2(beta-2)/beta].

We also use the regular-singular ODE lemma proved in packet121: if b=y btilde is smooth, btilde(0)=mu>0, yb(y)>0 away from0, and d(0)>0, the equation b u'+du=f has a unique smooth solution bounded at0, extending to the full line. In the coordinate z=y exp int_0^y(mu/b-1/y), with H=exp int_0^y(d-d(0))/b, its formula is

    Hu(z)=int_0^infinity exp[-d(0)t] (Hf)(exp(-mu t)z)dt.

On every compact z interval this can be differentiated to every order. At infinity no uniform bound on u is needed for this local smooth extension. When d(0)=0 and f=0, specifying u(0) determines the smooth homogeneous solution.

## A reference that solves the PDE on a disk

Let ell=Psi_e,x(0) and P=ell x+cxy-q0x^3/6. Then Omega_P=q0x, W_P=(lx,mu y-q0x^2/2), and Theta_P=a0x^2 solve both equations exactly. The cubic Taylor polynomial of Psi_e is P. Choose a smooth radial cutoff chi, one on the unit disk and zero outside radius2. For sufficiently small rho>0,

    Psi_ref=Psi_e+chi(X/rho)(P-Psi_e)

has Omega_ref/x>0 everywhere, W_ref,1/x>=l/2 and b_ref'>=l/2, and agrees with Psi_e outside a compact set. These claims follow from ||chi(./rho)(P-Psi_e)||_Ck=O(rho^(4-k)), k<=3, and oddness: |Delta delta/x|<=2||delta||_C3. The relative inverse, center values and exterior velocity are preserved. Taking rho<=l/q0 makes the inner disk backward invariant. There Psi=P and the integral for xi is zero, so Theta=Theta_P. On the central interval |y|<rho the reference axis data are

    g1_ref=ell+cy, b_ref=mu y, q_ref=q0,
    g3_ref=-q0/6, g_n_ref=0 for odd n>=5.

Here g_n denotes the coefficient of x^n in the smooth Taylor expansion along the axis. Every q_ref(y)>0. Its positive tail and all the needed low derivative estimates agree with q_e outside a compact interval.

## First axis equation everywhere while keeping the disk

Fix b=b_ref. Let

    a=a0 exp int_0^y (2b'-Lambda)/b,
    bQ'+(M-b')Q=2a,

where Q is the unique solution bounded at0. Then a,Q>0; Q(0)=q0. Outside a compact interval b=b_e, so the integrating-factor proof of packet122 gives Q=C_+|y|^(-1-s)(1+o(1)) at +infinity and Q=C_-|y|^(-1-s)(1+o(1)) at -infinity, with C_+,C_->0 and derivative bounds Q'=O(|y|^(-2-s)), Q''=O(|y|^(-3-s)). Therefore for a finite K>=1,

    K^-1<=Q/q_ref<=K,
    |f|+|f'|+|f''|<=C q_ref, f=Q-q_ref.

On |y|<rho, uniqueness applied to b=mu y gives a=a0 and Q=q0, exactly. Thus f vanishes on that whole interval.

Packet122 proves a cutoff lemma: given delta>0 there is smooth compactly supported even gamma, equal to1 near0, |gamma|<=1, for which m(t)=(t^3 gamma(t))''/(6t) satisfies -delta<=m<=1. For completeness, choose disjoint even bumps rho1,rho2,rho3, with rho1=1 near0 and rho2/rho3 rescaled to radii A/4A. Their moments mu_i=int_0^infinity t rho_i and t_i=int t^2 rho_i/mu_i give

    d2=mu1(t3-t1)/(mu2(t3-t2)),
    d3=mu1(t2-t1)/(mu3(t3-t2)),
    m=rho1-d2rho2+d3rho3.

Both d2,d3 are positive O(A^-2), so they obey the required bounds for large A. The two moments int tm=int t^2m=0. Integrating F''=6tm with F(0)=F'(0)=0 gives odd compact F=t^3 near0 and |F|<=|t|^3. Thus gamma=F/t^3 has the claimed properties.

Set delta(K-1)<=1/2 and

    Psi_1=Psi_ref-f(y)x^3 gamma(x/eps)/6.

The identity

    Omega_1/x=Omega_ref/x+f m+(f''/6)x^2gamma

proves positivity for small eps. In detail, uniformly for small |x|, Omega_ref/x>=q_ref(1-Cx^2): this holds explicitly for the base outside a compact y interval and by smooth evenness on that interval. If f>=0, q_ref+fm>=q_ref/2; if f<0 it is >=Q>=q_ref/K. The last term is bounded by Cq_ref x^2. Choose eps times the fixed support radius of gamma small enough. This also gives a uniform bound

    Omega_1/x>=c1 q_ref(y)>0 for |x|<=a1,          (1)

for some fixed a1>0 containing the strip correction support. Shrink a1 if needed and choose eps first accordingly.

The stream correction vanishes throughout |y|<rho, so it preserves a smaller polynomial disk. It leaves g1 and b unchanged, changes q toQ, and preserves center velocity. Its velocity and first derivatives decay like (1+|y|)^(-1-s) in a strip, so are bounded. For small eps it changes W1/x by at most l/4. The inverse uniqueness and flow argument give canonical V and the smooth global Theta. Axis differentiation of its temperature equation forces its a2=a; hence d_xR=bQ'+(M-b')Q-2a=0 everywhere.

## All higher axis coefficients

For clarity the exact recurrences are restated. Write Psi~sum_(n odd)x^n g_n, Omega~sum_(n odd)x^n w_n, Theta~sum_(m>=1)x^(2m)a_(2m), A=2beta-b'. Then

    w_n=-g_n''-(n+1)(n+2)g_(n+2),

and the temperature coefficient at x^(2m) is

    b a_(2m)'+(2mA-2l)a_(2m)
      +sum_(j=1)^(m-1)[(2j+1)g_(2j+1) a_(2m-2j)'
                        -(2m-2j)g_(2j+1)'a_(2m-2j)].            (2)

The vorticity residual coefficient at x^n, n odd, is

    b w_n'+(nA+1)w_n-(n+1)a_(n+1)
      +sum_(j=1)^((n-1)/2)[(2j+1)g_(2j+1) w_(n-2j)'
                          -(n-2j)g_(2j+1)'w_(n-2j)].           (3)

Fix the already constructed g1,g3 and a2=a, w1=Q. Inductively solve (2)=0 for a_(2k+2), k>=1, then (3)=0 for w_(2k+1), then obtain g_(2k+3) from the elliptic identity. The center coefficients are respectively 2kl>0 and (2k+1)l+1>0. The ODE lemma gives smooth functions on the whole real line at every finite stage. They may grow arbitrarily fast at infinity without obstructing the next step. On |y|<rho they equal the polynomial values, by uniqueness: all a_(2m), m>=2, all w_n, n>=3, and all g_n, n>=5, vanish there.

Let d_n(y)=g_n(y)-g_n^1(y), odd n>=5. These are arbitrary smooth functions on the full line, zero on a central interval. No tail bound on d_n is assumed in the construction below.

## Weighted realization on a noncompact axis

This is the new step. A single fixed width is unnecessary. Take a smooth partition of unity eta_j(y), j in Z, with uniformly bounded derivatives at each fixed order and support in [j-1,j+1]. Such a partition is obtained by translating a nonnegative smooth bump positive on [-1/2,1/2] and dividing by their positive periodic sum. At every point at most three supports meet. Let

    m_j=min_{y in[j-1,j+1]} q_ref(y)>0,
    tau_j=eta_* 2^(-|j|) min(1,m_j),

where eta_*>0 will be small. Use a fixed smooth even chi0(x), one for |x|<=1 and zero for |x|>=2. For each odd n>=5 and integer j, choose 0<eps_(n,j)<=a1/2 so small that

    ||x^n eta_j(y)d_n(y) chi0(x/eps_(n,j))||_C^(n-1)
        <=2^-n tau_j.                          (4)

This is possible because eta_j d_n is smooth and compactly supported in y. By the product rule each derivative of total order k<=n-1 is bounded by C_(n,j,k) eps_(n,j)^(n-k); the smallest power is positive. There is no requirement that eps_(n,j) have a smooth dependence on j.

Define deltaPsi as the sum of these terms over all odd n>=5 and all j. On any fixed compact set only finitely many j contribute. For a fixed derivative order k, the terms with n>k are bounded by the summable right side of (4), and the finitely many n<=k are finite sums of smooth functions on that compact set. Thus the sum converges in C^k on every compact set for every k, and is smooth. It is odd in x, supported in |x|<=a1 and vanishes throughout the central horizontal interval. Its x Taylor coefficient of order n is exactly d_n because chi0 is one near0 and sum_j eta_j=1. Taking derivatives termwise is justified by the just-proved local C-infinity convergence.

Moreover the sum is globally C^3-small with a pointwise weight. At a given y, at most three j contribute and m_j<=q_ref(y). Therefore for every partial derivative of total order<=3,

    |partial^alpha deltaPsi(x,y)|
      <=C eta_* q_ref(y),                       (5)

with a fixed finite C independent of x,y. The extra factor 2^(-|j|) only improves this bound. For each fixed y, the same bound holds along the horizontal segment from0 to x. Since Delta deltaPsi is odd and deltaPsi has an x^5 factor in the sense of its first four vanishing axis derivatives,

    |Delta deltaPsi(x,y)/x|
        <=2C eta_* q_ref(y).                    (6)

Choose eta_* so 2C eta_*<c1/2 in (1). Then Omega=Omega_1-Delta deltaPsi is still positive in x>0, including the support of the perturbation. Outside it Omega=Omega_1. Similarly |deltaPsi_y/x|<=C eta_* q_ref(y), so choose eta_* also so C eta_* sup q_ref<=l/8. The strip stage had W1/x>=l/4, hence the final bound is W1/x>=l/8; bprime>=l/2. The flow lemma applies with kappa=l/8. The axis g1,g3 are unchanged exactly, so b is unchanged. Second stream derivatives remain bounded. Thus the basin and global normalized temperature construction persist.

The estimate (5) gives |U-U_1|+|D(U-U_1)|<=Cq_ref(y) inside the fixed strip, and (6) gives |Omega-Omega_1|<=C|x|q_ref(y). Since q_ref=O((1+|y|)^(-1-s)), all the declared tail bounds follow. The relative canonical inverse follows without an exterior support assumption: the subtracted full-plane integral converges for this tail; subtract grad-perp deltaPsi from the canonical relative inverse of -Delta deltaPsi. The difference is an entire harmonic vector field with sublinear growth, hence a constant. Both relative fields vanish at0, and grad deltaPsi(0)=0, so the constant is0. This is exactly the same uniqueness argument as for the strip correction.

## Identification of the actual temperature jets and residual

For the final stream define its actual temperature by xi. Its center normalization is a0 because I(0)=0 and xi_x(0)=1. Its Taylor coefficients along x satisfy (2) as exact identities between smooth functions of y. The actual a2 equals the prescribed a2 by uniqueness of the homogeneous axis equation with the fixed center value. Inductively for m>=2, all the lower coefficients and stream coefficients agree with the prescribed ones, and the ODE for a_(2m) has its unique bounded solution at0. Thus every actual coefficient equals its prescribed counterpart on the whole line. Likewise the actual vorticity coefficients equal w_n by -Delta Psi. Equation (3) is therefore0 for each odd n everywhere. Even coefficients vanish by parity. Every mixed derivative of R on the axis is zero, since each x coefficient is the identically zero smooth function of y.

All perturbations made after the reference construction vanish in a horizontal strip about0. A smaller disk remains exactly the polynomial stream, is backward invariant and has xi=x. Therefore both PDEs remain exact there. This completes the theorem, conditional only on the explicit elementary inputs whose proofs are restated or referenced above.

## Consequences and limits

The conclusion strengthens packets121/122 in the smooth field/tail class by combining disk exactness with infinite-order vorticity residual vanishing on the entire axis. The noncompact weighted partition construction is what removes the need for uniform tail bounds on the formal higher coefficients. It does not justify claims in a narrower class that bounds all high derivatives or requires analyticity. It changes the far exterior in a strip, so the compact-exterior obstruction of packet121 does not apply.

The vorticity residual may still be nonzero at points with x!=0 outside the small disk. Infinite-order vanishing along a smooth hypersurface does not imply vanishing in a neighborhood for merely smooth functions. The construction provides no full profile and no nonexistence theorem. Update 2026-10-21T04:51:17.459905+00:00: packet124 proves that NONE of these fixed-exterior configurations satisfies the remaining vorticity equation globally. They agree in relative velocity and vorticity with the explicit analytic base on an exterior half-plane; its local compatibility identity fails on every nonempty open set. This refutes these particular fields as profiles and leaves the theorem above intact. The existence question for arbitrary B2 profiles remains OPEN.

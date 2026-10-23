# Unbounded slopes for the first transport projection

Independent reconstruction, 2026-10-21. Source under audit: the frozen proj1 proof with SHA256 48bacd419a1a7e2ab4f108e3d49c17a0db26ad4475e9fc67d5b0cef3be8b1884. The argument below supplies the complete first-projection construction. It does not construct an IPM profile.

## Statement and definitions

For every ell>1 and integer n>=0, set D=ell-1, alpha=2n+3/2, a=4(ell+1)alpha. There is beta_*>0 such that every 0<beta<beta_* gives a smooth even-x, odd-y density rho, with rho_y(0)=a, canonical U=o(r), psi_xy(0)=-D, growth exponent gamma=1-2beta in (0,1), and rho/(ay)<=1 everywhere. Its first sine transport projection vanishes at every radius. For n>=1 its third sine projection is nonzero. Thus the slopes under these first-projection and one-sided conditions are unbounded, while the full profile problem remains unresolved. Neither a common gamma nor a numerical value of beta_* is asserted.

Write R=(ell X+U).grad rho-rho, R_j(r)=integral_0^(2pi)R sin(jtheta)dtheta. Density sine coefficients have the separate normalization b_j=(1/pi)integral rho sin(jtheta)dtheta. Set t=log r, z=r², and use dots for t derivatives.

## Canonical reduction

Let M=a/4-D, T=M(1+r²)^(-beta), g=-dot T=2beta M r²(1+r²)^(-beta-1), and K=r^-6 integral_0^r s^5 g(s)ds. Seek

    rho=r f(r)sin(theta)+r g(r)sin(3theta),
    J=r^-4 integral_0^r s³ f(s)ds,
    L=ell+(T-J)/2,
    N=f²/4-(D+T)f-fg/2+(2T+J-2K)g+[(T-J)/2+K]dot g.

The defining ODE is dot J=f-4J, L dot f=N, with f(0)=a,J(0)=a/4 and the solution analytic in z at zero.

For an even source frequency k>=2, the regular full-plane Green formula and integration by parts give

    P_k=(1/2)[r^k integral_r^infinity b_(k+1)(s)s^-k ds
                    -r^-k integral_0^r b_(k-1)(s)s^k ds].

Both endpoint terms vanish for smooth sublinear densities. Since integral_r^infinity g(s)ds/s=T(r), the candidate stream is exactly

    psi=r²(T-J)sin(2theta)/2-r²K sin(4theta)/2.

The identity dot K=g-6K and this stream give -Delta psi=rho_x directly. The eventual growth estimate below proves that its velocity is sublinear, so no gauge assumption is deferred indefinitely. Any competing canonical velocity differs by an entire harmonic vector field of sublinear growth; interior derivative estimates force it to be constant, and parity makes that constant zero.

Independently expand U_r/r=-2Z2 cos(2theta)-4Z4 cos(4theta) and U_theta/r=(2Z2+dot Z2)sin(2theta)+(2Z4+dot Z4)sin(4theta), with Z2=(T-J)/2,Z4=-K/2. Adjacent sine-cosine products then give R_1/(pi r)=L dot f-N. The prescribed ODE therefore enforces exactly the stated projection. At zero, T-J=-D and K=O(r²), so psi=-Dxy+O(r^4), independent of any transport normalization shortcut.

## Analytic origin and a signed first variation

At beta=0 the auxiliary solution is f=a,J=a/4,T=M,g=K=0 and L0=(ell+1)/2. In z the linearization of (f-a,J-a/4) is [[alpha,0],[1/2,-2]]. Both eigenvalues avoid positive integers. The inverse of z d_z minus this matrix is bounded on analytic zero-constant power series, after diagonalization, because sup_(j>=1)max(|j-alpha|^-1,(j+2)^-1)<infinity.

The nonlinear remainder F satisfies F(0,0,beta)=0,F_u(0,0,beta)=0 and F(z,0,beta)=O(beta z). In the norm sum|u_j|R^j, the analytic algebra estimate gives a Lipschitz constant C(R+delta) on a ball of radius delta. Choose R,delta small enough that the inverse norm times C(R+delta)<1/2, and then beta small enough to map that ball into itself. The contraction gives the analytic branch and analytic dependence on beta. Its parameter derivatives extend to each fixed finite radius by ordinary ODE continuation around the constant beta=0 solution with L=L0>0. This is not a claim of uniform continuation on an expanding interval.

Let F1=partial_beta f at beta=0. Direct differentiation, using the vanishing of N at the auxiliary solution, gives

    z F1'-alpha F1 = M/(ell+1)[a log(1+z)+(a/2-4D)z/(1+z)-2D z/(1+z)²].

Its analytic solution is

    F1=M/(ell+1)[4(alpha+2)Y_alpha-4(ell+1)log(1+z)-2D z/(1+z)],
    Y_alpha=sum_(j>=1)(-1)^(j-1)z^j/(j-alpha).

The equation zY'-alpha Y=z/(1+z) verifies the formula. For alpha=2n+3/2,

    Y_alpha=z^alpha[-pi-integral_z^infinity s^-alpha/(1+s)ds]<0.

Indeed Y_(1/2)=2sqrt(z)arctan(sqrt(z)); the recurrence Y_(nu+1)=-z/nu-zY_nu follows by shifting the convergent series. Applying it an odd number of times changes the homogeneous constant from pi to -pi and proves the displayed integral representation. Substituting s=zu and using 1+zu<=u(1+z) gives Y_alpha<=-z/[alpha(1+z)].

Since partial_beta g=2Mz/(1+z), it follows that

    partial_beta(f+3g) <= -8M z/[alpha(ell+1)(1+z)].

For w=f-4(D+T), its first variation is M/(ell+1)[4(alpha+2)Y_alpha-2D z/(1+z)], tending to minus infinity. On each fixed compact z interval the second parameter remainder is bounded by C beta² z/(1+z): near zero this follows from analyticity and the fixed value a; away from zero it follows from the compact continuation. Thus f>0 and f+3g<=a hold there for sufficiently small positive beta.

## Departure before the denominator can vanish

Put Lmax=ell+M/2, kappa=D/(2Lmax), CS=M(2a+14M), CB=2CS/L0+8M, and K0=max(4CB/kappa,12M,1). Here M-L0=2+2n(ell+1)>0. For 0<beta<=1/4,

    0<g<=2beta T, -2beta<=d:=dot g/g<=2,
    |dot g|<=4beta T, 0<=K<=g/(6-2beta)<=beta T/(3-beta).

The bound for K follows by integrating the kernel exp(-6(t-s)) against g(s)<=g(t)exp(2beta(t-s)).

Choose a fixed t1>=0 with partial_beta w(t1,0)<-2K0. The compact estimates give w(t1)<=-K0 beta, f(t1)>2D and 0<f<=a,J in [0,a/4] up to t1. Consider subsequent times while f>=2D,w<=-K0 beta,T>=M-L0. Then f=4(D+T)+w<=a, the J equation preserves its interval, and L0/2<=L<=Lmax.

Writing N=fw/4+S, termwise estimation gives |S|<=beta(2a+14M)T<=CS beta: the three contributions are bounded by a beta T, (8M+a/2)beta T, and (6M+a/2)beta T. Consequently

    dot w=fw/(4L)+S/L+4g <= kappa w+CB beta <= (kappa/2)w<0.

The negative sign of w justifies replacing f/(4L) by its lower bound kappa. Take beta smaller so that K0 beta<a and

    beta M[log2+2t1+(4/kappa)log(a/(K0 beta))]<L0/2.

This is possible since beta log(1/beta)->0. If f never reached 2D during tau=(2/kappa)log(a/(K0 beta)), then -w would reach a, contradicting w>=2D-a. Throughout this proposed interval M-T<=beta M(log2+2t)<L0/2. Thus loss of T or L cannot occur first. A finite first time t2 with f=2D exists.

## Global trapping and decay

At t2 the region

    0<=f<=2D, 0<=J<=a/4, Z:=J-T<=D+L0/2

holds. Here L>=3L0/4. At f=2D, N<=-D²-2DT+CS beta<0 if CS beta<D²/2. At f=0,

    N/g=(2+d/2)T+(1-d/2)J+(-2+d)K
       >=[6-7beta-beta²]T/(3-beta)>0.

The J bounds follow from dot J=f-4J and 2D<a. At the upper Z boundary, dot Z=f-4Z-4T+g<=2D-4Z<0. All sides are therefore invariant. Coefficients stay bounded and L stays positive, which proves global continuation.

During departure f+3g<=a-K0 beta+6M beta<=a. In the trapped region f+3g<=2D+6M beta<a after a further smallness choice. Since g>=0 and q=[f+g(4cos²(theta)-1)]/a, this proves q<=1 everywhere. Positivity of q is not asserted.

Retaining T in |S|<=beta(2a+14M)T and using f²/4-Df<=-Df/2 gives dot f<=-kappa f+C T. Choose also 2beta<kappa. Since T<=M exp(-2beta t), integration gives f=O(exp(-2beta t)). The J equation gives the same decay for J; the formulas and ODE give it for g,K,T,dot f,dot g. Hence rho=O(r^(1-2beta)), grad rho=O(r^-2beta), U=O(r^(1-2beta))=o(r). Analytic f in r² and g=O(r²) make rho smooth at zero, including the mode3 term r³sin(3theta); elsewhere the ODE is smooth. The finitely many sufficient-smallness choices leave a nonempty interval of beta.

## Nonzero third projection and scope

Write rho=ay+bx²y+ey³+O(r^5), and g=g2 r²+O(r^4), g2=2beta M. The first projection gives 6e=(a-2A)b, A=2ell-1, while b-e=4g2. Therefore

    b=24g2/[4(ell+1)-a], e=4g2(a-2A)/[4(ell+1)-a].

With no density mode5, the canonical quartic stream coefficients are q1=(3e-11b)/48 and q2=-(5b+3e)/48. The cubic residual coefficients are r21=2Ab+3aq1 and r03=2e+aq2. Its third sine coefficient is (r21-r03)/4, giving

    lim R3/(pi r³)=g2[a²-(4ell+20)a+64(2ell-1)]/[4(4(ell+1)-a)].

For n>=1, a>=14(ell+1); the bracket there is at least 140ell²+184ell-148>0 and increases with a. Thus the third projection is nonzero along an unbounded subsequence. The denominator is nonzero for every chosen alpha. These are canonical first-projection counterexamples to an upper slope bound, not candidate full profiles. No statement about R1=R3=0 follows.

Dependencies: elementary full-plane Green integration with explicit endpoints, analytic power-series contraction, ordinary ODE continuation, differential inequalities, and finite Fourier products. These dependencies are proved or instantiated above. Exact supporting checks are separate from the proof and cannot establish global continuation on their own.

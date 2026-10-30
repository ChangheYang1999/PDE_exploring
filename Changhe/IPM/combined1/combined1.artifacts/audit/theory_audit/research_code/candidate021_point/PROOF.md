# Independent polar point audit for candidate021

## Exact input and aim

The input is candidate C1-N1-021-heldin14-legqs25p50, coefficient SHA256 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8. All generator coefficients and parameters are exact rationals. At X=(1/10,73/100), this audit independently computes rho, U[rho], grad rho and the stationary residual F=(cX+U[rho]).grad rho-rho. It then checks necessary scalar and uniform graded point inequalities. It uses polar radial differentiation, separately from the peer's Cartesian derivative calculation.

## 1. Exact local radial Taylor data

Write t=r^2/(1+r^2), u=1-t, p_j=(3+1/c-j(1-1/c))/2. Each angular component of the potential is f(r)cos(n theta), n=2m, with f=u^(-p_j)V(t). For a monomial generator V=t^(m+h). For an ordinary Legendre generator,

    V=t^(m+w) sum_(k=0)^N (-1)^(N+k) binom(N,k)binom(N+k,k)t^k.

For a multiscale generator put D=R^2(1-t)+t. The identities t_R=t/D and u_R=R^2(1-t)/D give

    V=sum_(k=0)^N (-1)^(N+k)binom(N,k)binom(N+k,k)
        R^(2Q) t^(m+w+k) (1-t)^Q D^(-w-Q-k).            (1)

At the rational evaluation point t0, retain Taylor coefficients through degree4 in z=t-t0. Every factor in V is an integer power of a positive affine function, so these coefficients are rational. The factor u^(-p_j) equals u0^(-p_j) times a Taylor polynomial with rational coefficients through degree4. Only its positive constant u0^(-p_j) needs outward Arb evaluation. Discarding higher Taylor coefficients is exact for derivatives of order at most4 at t0.

The Euler radial operator is D_r=r partial_r=2t(1-t)partial_t. Repeatedly apply it to the truncated Taylor polynomial, reducing the retained order after each differentiation. This produces exact rational multiples of u0^(-p_j) for f,D_r f,...,D_r^4 f at the point. Thus no finite difference or numerical differentiation is used.

## 2. Density and gradient from the polar Laplacian

For one angular component set b=D_r^2 f-n^2 f, b1=D_r^3 f-n^2 D_r f and b2=D_r^4 f-n^2 D_r^2 f. Write S=sin theta, C=cos theta, sn=sin(n theta), cn=cos(n theta), A=b1-2b and B=b2-5b1+6b. Since Delta chi=r^-2 b cn and rho=-partial_y Delta chi,

    rho=-r^-3[S A cn-n C b sn],
    D_r rho=-r^-3[S B cn-n C(b1-3b)sn],
    partial_theta rho=-r^-3[C(A-n^2 b)cn+n S(b-A)sn].      (2)

Then rho_x=(C D_r rho-S partial_theta rho)/r and rho_y=(S D_r rho+C partial_theta rho)/r. These follow by direct product differentiation; derivatives of the prefactor r^-3 are included in B and b1-3b.

## 3. Velocity from the stream function

The canonical potential convention gives psi=partial_xy chi and U=(-partial_y psi,partial_x psi). Put

    E=D_r^2 f-2D_r f+n^2 f, H=D_r f-f,
    E2=D_r^3 f-4D_r^2 f+(n^2+4)D_r f-2n^2 f,
    H2=D_r^2 f-3D_r f+2f, C2=C^2-S^2.

Direct expansion of partial_xy in polar coordinates gives

    psi=r^-2[SC E cn-n C2 H sn].

Therefore its polar velocity components are

    U_r=-r^-3[C2(E-n^2 H)cn+n SC(-E+4H)sn],
    U_theta=r^-3[SC E2 cn-n C2 H2 sn].                    (3)

Finally U1=C U_r-S U_theta and U2=S U_r+C U_theta. All angular sines and cosines are obtained from the exact point coordinates and a square root by the addition recurrence. Sum (2)-(3) over the finitely many generators and form F. Every non-rational operation is enclosed by Arb.

## 4. Necessary correction tests and scope

For a fixed-c exact correction h with ||h||H^(2+s)<=r, the audited point embedding and the difference equation give

    |F(X)|<=r[C1(s)|cX+U[rho](X)|+C0(s)(1+|grad rho(X)|)]
             +C0(s)C1(s)r^2,
    C0(s)=(4pi(1+s))^-1/2,
    C1(s)=(8pi s(1+s))^-1/2.                             (4)

For the original graded family, the audited top-margin inequality implies the universal bounds C0 r<b0 and C1 r<b1, where

    b0=50/(651 sqrt(28248) sqrt(4pi)),
    b1=25/(217 sqrt(8pi)).

Hence its universal right side is b1|V|+b0(1+|grad rho|)+b0b1. The proof of these exact constants and the family hypotheses is ../graded_point_009/PROOF.md, Section2; it is independent of the candidate. Strict positive gaps exclude only the named fixed-c balls or graded family, not the profile problem in other spaces. The output records every compared scalar, candidate hash and exact radius. A small optimization loss is not used as evidence.

## 5. Exact radii and comparison scope

The six scalar rows use the exact parameters in the frozen N4 direct record. They are A2-Db, TB-rebalanced, TB-sharp, T4-020, T4L2-sharp and T4L2-sharpw. Every radius is rational. Compute the positive root of the quadratic point inequality as an additional necessary radius. The signed local quantity theta=(|grad rho|-rho_y)/2 is retained as a diagnostic only; one point cannot establish the global signed criterion. No separate uniform-point or extension record is needed for this candidate. All source and code hashes are retained with the result.

## 6. Candidate021 scale check

The radius25 and radius50 generators use exactly (1), with D=625(1-t)+t or D=2500(1-t)+t, respectively, both positive on [0,1]. Their derivatives at the test point require no new global quadrature or asymptotic approximation. This audit confirms local fields and necessary point tests only; the global rational-moment backend is a separate audit.

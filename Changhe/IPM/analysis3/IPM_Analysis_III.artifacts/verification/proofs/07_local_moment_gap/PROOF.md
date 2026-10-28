# No radial local-moment gap with a weaker Sobolev remainder

## Statement

Let ell>2, A=2ell-1, D=4ell-1=2A+1 and B=diag(-A,D). Fix R>0. Suppose a parity-compatible background has

    |grad rho|<=C r^2, |D^2 rho|<=C r,
    V=BX+E, |E|<=C r^2, |DE|<=C r

near zero and the regularity needed to define the normalized linear expression

    Lh=V.grad h-h+U[h].grad rho+(c[h]/3)X.grad rho.

Assume V and grad rho are bounded on compact subsets of B_R, with the stated center bounds, and use the canonical velocity and raw strain of proof 01. The exactly normalized modal background meets these assumptions. Define

    M_p(h)=||h/r^3||_(L^p(B_R)), 1<p<=infinity.

For every finite 1<p<infinity and every 2<s<4-2/p there is a sequence of smooth compact densities h_j in B_R, each with a smooth global factor h_j=x^2 y b_j, such that

    J(h_j)=c[h_j]=0,
    M_p(h_j)=1, M_p(Lh_j)->0, ||h_j||_(H^s(R^2))->0.            (1)

The same conclusion holds for p=infinity and every 2<s<4. Every h_j vanishes on a neighborhood of the origin and a neighborhood of the boundary of B_R.

Consequently no finite C gives

    M_p(h)<=C(M_p(Lh)+||h||_(H^s))                             (2)

on a linear domain containing this sequence. In particular an adjoint argument for a positive gap controlling this entire radial moment from these quantities cannot hold. This theorem does not disprove an estimate for the single scalar c[h] in terms of Lh: the constructed sequence has c[h_j]=0. It also does not cover stronger Sobolev remainders, anisotropic moments, additional boundary information about U[h], or domains excluding the sequence.

## Finite p: the critical homogeneous degree

Set nu=3-2/p, so nu>1. Define

    P=(D nu-1)/(A+D), Q=(A nu+1)/(A+D).

Both exponents are positive, P+Q=nu and -AP+DQ=1. Thus

    H=|x|^P sign(y)|y|^Q=r^nu F(theta)

solves (BX.grad-1)H=0 away from the axes. With a smooth even-reflection angular cutoff chi_e zero near every axis and one away from them, set F_e=chi_e F. As in proof 05, if

    a(theta)=-A cos^2(theta)+D sin^2(theta),
    b(theta)=(A+D)sin(theta)cos(theta),
    T_nu Z=b Z'+(nu a-1)Z,

then G_e=T_nu F_e=b chi_e' F. Near an axis with exponent lambda=P or Q, G_e has size O(e^lambda) on an interval of length O(e). Hence

    F_e->F in L^p(S^1), G_e->0 in L^p(S^1).                  (3)

No derivative of G_e is required for M_p. Each fixed F_e is smooth and vanishes near the axes.

Choose delta<R/4 within the background center bounds and delta<1. Put t0=log delta. Let eta_N(t)=zeta(t+N)zeta(t0-t), where zeta is a fixed smooth step from zero to one on [0,1]. For N large define

    f_(e,N)=r^nu eta_N(log r)F_e(theta).

This is smooth and compact in exp(-N)<r<delta, with a smooth even-even quotient by x^2y. Since (nu-3)p+1=-1,

    M_p(f_(e,N))^p=||F_e||_(L^p)^p integral |eta_N(t)|^p dt
       >=(N+t0-2)||F_e||_(L^p)^p.                           (4)

The frozen image is r^nu eta_N G_e+r^nu eta_N' a F_e. The first term has moment at most C N^(1/p)||G_e||_(L^p); the second has bounded moment for fixed e because eta_N' is supported on intervals of bounded length. Thus

    M_p((BX.grad-1)f_(e,N))
       <=C N^(1/p)||G_e||_(L^p)+C_e.                        (5)

The local coefficient error is E.grad f=O_e(r^(nu+1)). Its moment is bounded independently of N, since

    integral_0^delta r^((nu-2)p+1)dr=integral_0^delta r^(p-1)dr<infinity.

## Uniform regularity and nonlocal terms

Fix 2<s<nu+1. A dyadic piece of f at radius r comparable to rho<=delta has the form rho^nu g(X/rho), where g and all needed derivatives are bounded uniformly in N,rho for fixed e. Fourier scaling gives

    ||rho^nu g(X/rho)||_(H^s)<=rho^(nu+1-s)||g||_(H^s).

The exponent is positive, so summing over dyadic radii proves a uniform H^s bound. The order-zero velocity multiplier preserves H^s. Since s>2 in two dimensions, Fourier Cauchy-Schwarz gives a uniform C^1 bound on U[f]. Its parity gives U[f](0)=0, whence |U[f](X)|<=C_e r near zero, and |c[f]|<=C_e.

Therefore U[f].grad rho and c[f]X.grad rho are O_e(r^3) near zero. Their M_p moments are finite and bounded uniformly in N. On the rest of the fixed disk the same conclusion follows from the C^1 velocity bound and bounded background coefficients. Together with (5),

    M_p(L f_(e,N))<=C N^(1/p)||G_e||_(L^p)+C_e.               (6)

This is an estimate of the full image on B_R; the fact that U[f] is not compactly supported is explicitly included.

Choose nonnegative nonzero smooth chi0 supported in an annulus inside B_R and outside r<=delta. Let b0=x^2y chi0(r). Proof 01 gives c[b0]=(1/4)integral r chi0(r)dr>0. Put b=b0/c[b0]. It has J(b)=0, c[b]=1 and finite H^s, M_p and M_p(Lb). Its image moment is finite by the same center and compact-annulus estimates. Define

    v_(e,N)=f_(e,N)-c[f_(e,N)]b.

Then c[v]=J(v)=0. The supports of f and b are disjoint, so M_p(v)>=M_p(f). Its H^s norm and the correction to (6) are bounded for fixed e. Choose e_j->0, then N_j sufficiently large, so the ratios of every fixed-e bound to (4) tend to zero. Normalize v by its exact M_p norm. Equations (3)-(6) prove (1) for finite p.

## The endpoint p=infinity

Here the critical degree is three and the exact smooth angular solution is F(theta)=cos^2(theta)sin(theta), since T_0(x^2y)=0. Choose a fixed smooth eta supported in (-1,0), equal to one on a nonempty interval. Let delta_N=exp(-N), and for all sufficiently large N set

    f_N=x^2y eta((log r-log delta_N)/N).

Its support is exp(-2N)<r<exp(-N), so it lies inside B_R and vanishes near zero. Its moment M_infinity is the fixed positive number max|cos^2(theta)sin(theta)|. Since each logarithmic derivative of eta costs N^-1,

    M_infinity(T_0 f_N)<=C/N.

The local error has M_infinity(E.grad f_N)<=C delta_N. For every 2<s<4, the same dyadic scaling argument, now starting at the outer radius delta_N, gives

    ||f_N||_(H^s)<=C delta_N^(4-s)->0.

Consequently the C^1 velocity norm and c[f_N] tend to zero. The nonlocal and rank-one image terms have M_infinity bounded by these quantities times fixed background bounds: near zero use U[f_N]=O(r||DU[f_N]||_infinity), and away from zero all divisions by r^3 are harmless. Thus M_infinity(Lf_N)->0.

Use the same fixed strain-one bump b and set v_N=f_N-c[f_N]b. Its moment tends to the same positive constant, its H^s norm tends to zero, and its full image moment tends to zero. Dividing by M_infinity(v_N) proves (1) at the endpoint.

## Interpretation

This obstruction uses genuine smooth perturbations with literal zero center trace, exact zero strain, zero density boundary trace, and full nonlocal images in the stated local moment space. The weak regularity norm in (2) cannot detect the increasing logarithmic annulus length at the critical homogeneous degree. A different local estimate may still succeed, but it must change a substantive hypothesis or quantity. In particular this proof is not a rejection of every Avenue III strategy or a statement about a scalar Schur complement.

Dependencies are the canonical multiplier and strain formula of proof 01, elementary polar differentiation, dyadic Fourier scaling, and the usual Fourier proof of H^s to C^1 for s>2. No numerical or finite-section claim is used.

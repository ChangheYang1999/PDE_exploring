# Failure of quadratic continuity in the weak X graph norm

## Statement and spaces

Let L0>0, 0<k<1 and 0<alpha<1. Put

    w(r)=L0^6 r^(-6)(1+r^2/L0^2)^(3/2-k),
    ||h||_X^2=integral_R2 (|h|^2+r^2|grad h|^2)w(r)dX.

Derivatives in this norm are weak derivatives. Let rho be even in x, odd in y and locally C^(2,alpha), and let V=ell X+U[rho] be locally C1. Assume V(0)=0 and V(P)=0 for P=(p,0), p>4. Assume finite constants bound

    |grad rho|+r|D2 rho| <= C r^(1+alpha), 0<r<=1,
    |grad rho|+r|D2 rho| <= C r^(k-1), r>=1.

The canonical velocity U and raw strain c are those of proof 01. On compact C5 perturbations define

    Lh=V.grad h-h+U[h].grad rho+(c[h]/3)X.grad rho,
    N(h)=U[h].grad h+(c[h]/3)X.grad h.

Consider any algebraic domain containing the sequence below, on which h,Lh belong to X and the continuous factor h/(x^2 y) has a center value J(h). Equip it with ||h||_G=||h||_X+||Lh||_X. No completeness of this algebraic domain is assumed.

There are compact C5 perturbations h_n with the prescribed parity, J(h_n)=c[h_n]=0, h_n,Lh_n,N(h_n) in X, such that

    ||h_n||_G ->0,  liminf ||N(h_n)||_X >0.                 (1)

Consequently N is not continuous at zero from this graph topology into X. In particular no bound ||N(h)||_X<=C||h||_G^2 holds on a graph ball containing all sufficiently large n. The perturbations have compact support, so they preserve every prescribed far coefficient. This is not a theorem about stronger graph norms or about L^(-1)N in another topology.

## A fixed compact packet

Write Z=(z1,z2), and define

    H(Z)=z1^2 z2 (1-|Z|^2)_+^6,
    H_d(X)=x^2 y(1-r^2/d^2)_+^6,
    G0=-(56/3)(H_1-H_2).

Proof 09 derives directly from the radial Green integrals that c[H_d]=d^2/56 and J(H_d)=1. Thus J(G0)=0 and c[G0]=1. Expansion at zero gives G0=84 x^2 y r^2+O(r^7), including its first two differentiated remainders. It is compact C5 and supported in r<=2.

For clarity the exterior stream of the unit H is

    psi_H=-z1 z2/[2016 |Z|^4]
          -z1 z2(z1^2-z2^2)/[3360 |Z|^8], |Z|>=1.        (2)

The interior stream is a polynomial supplied by the same Green calculation. The forcing and stream match at the unit circle, with all regularity used here. For W=U[H],

    |W|<=C|Z|, |DW|<=C,                    |Z|<=1,
    |W|<=C|Z|^-3, |DW|<=C|Z|^-4,            |Z|>=1.

Its linear term is W=(-z1,z2)/56+O(|Z|^3). Hence

    Q=W.grad H=-z1^2 z2/56+O(|Z|^5).

In particular grad Q is not the zero polynomial. Let K={|Z|<1/2}. The exact positive number

    E_H=integral_K |grad Q|^2 dZ >0                       (3)

requires no numerical approximation: a polynomial with the displayed nonzero lowest term cannot vanish on an open disk. The code independently evaluates (3) by exact monomial disk moments, but positivity in the theorem already follows from the polynomial argument.

## Exact constraints after translation

Take epsilon=n^-2, a=n^-1, n>=2, and

    P_n(X)=a[H((X-P)/epsilon)+H((X+P)/epsilon)].

Parity follows from the even first and odd second coordinate of H. The supports are disjoint and avoid r<=2. Each packet vanishes linearly in y, and its support avoids x=0, so division by x^2 y extends to a continuous even-even factor. Its center value is zero.

A change of variables in the canonical kernel gives

    psi[a H((X-P)/epsilon)]=a epsilon psi_H((X-P)/epsilon).

Differentiating (2) at (t,0) gives

    (psi_H)_xy(t,0)=(t^-4+t^-6)/672.

Both translated packets therefore have combined strain

    c_n=c[P_n]=(a/336)(epsilon^3/p^4+epsilon^5/p^6).       (4)

Set h_n=P_n-c_n G0. The constraints J(h_n)=c[h_n]=0 are exact. In particular N(h_n)=U[h_n].grad h_n. Notice c_n=O(a epsilon^3).

## Membership and smallness of the full linear graph

The weight is bounded by C r^-6 near zero and C r^(-2k-3) at infinity. Set R=X.grad rho. Its value and weighted first derivative are O(r^(2+alpha)) near zero and O(r^k) at infinity. The two radial squared-norm exponents are -1+2alpha at zero and -2 at infinity, so R is in X.

The fixed compensator G0 and its full L image belong to X. Near zero G0 and its first two derivatives have orders 5,4,3, while its velocity has orders 1,0. Its coupled image and weighted derivative are O(r^(2+alpha)). At infinity U[G0] and its derivative have orders -3,-4, so the coupled image and weighted derivative are O(r^(k-4)). The latter squared-norm radial exponent is -10. Compact annuli cause no problem by the stated regularity. This also proves the compensator graph norm is finite.

On a fixed compact annulus containing the moving packets, X is equivalent to the usual H1 norm. Scaling gives ||P_n||_X<=Ca. Since V vanishes at both centers and is C1, V=O(epsilon) on the packet supports. The transport value V.grad P_n-P_n is O(a), its derivative is O(a/epsilon), and the support area is O(epsilon^2). Its X norm is therefore O(a).

The nonlocal coupling must be checked away from those supports as well. Choose fixed disjoint disks of radius d<1 about the centers. In one disk, with q the distance to its center, the packet's own velocity obeys

    |U|<=Ca, |DU|<=Ca/epsilon,                        q<=epsilon,
    |U|<=Ca epsilon^3 q^-3, |DU|<=Ca epsilon^3 q^-4,   epsilon<=q<=d.

The other packet contributes O(a epsilon^3) with its first derivative. The background derivatives and weights are bounded in both disks. The local squared X norm of U[P_n].grad rho is at most Ca^2 on q<=epsilon. On the punctured part its most singular integral is

    Ca^2 epsilon^6 integral_epsilon^d q^-7 dq <= Ca^2.

The remaining compact annulus gives O(a^2 epsilon^6). Near zero, parity and (2) imply U[P_n]=O(a epsilon^3 r), DU[P_n]=O(a epsilon^3). Thus the coupled value plus r times its gradient is O(a epsilon^3 r^(2+alpha)); its squared radial integral converges with exponent -1+2alpha. At large r it is O(a epsilon^3 r^(k-4)), giving exponent -10. Hence the full coupled X norm is O(a), not merely its restriction to the packet supports. The rank-one term has norm O(a epsilon^3)||R||_X.

Linearity now gives

    ||h_n||_X+||Lh_n||_X <= Ca+C|c_n| ->0.                (5)

For each n, N(h_n) is C1 and compactly supported. Near zero h_n=O(r^5), grad h_n=O(r^4), D2h_n=O(r^3), and U[h_n]=O(r), DU[h_n]=O(1). Thus N=O(r^5), grad N=O(r^4), which proves X membership. The stronger cancellation c[h_n]=0 is not needed for this last integrability check. The C5 interfaces create no singular weak derivatives.

## Nonzero quadratic limit at the source

On P+epsilon K, the compensator vanishes in the density and the other packet is absent. Thus h_n=aH(Z). In the velocity,

    U[h_n](P+epsilon Z)=aW(Z)+R_n(Z),
    ||R_n||_(C0(K))=O(a epsilon^3),
    ||grad_Z R_n||_(C0(K))=O(a epsilon^4).

These estimates follow directly from (2) for the opposite packet and the smooth fixed U[G0] near P. Because a^2=epsilon,

    N(h_n)(P+epsilon Z)=Q(Z)+E_n(Z),
    ||E_n||_(C1(K))=O(epsilon^3).

The gradient part of the X norm on this patch equals

    integral_K |P+epsilon Z|^2 w(|P+epsilon Z|)
                    |grad_Z(Q+E_n)|^2 dZ.

It converges to p^2 w(p)E_H>0 by uniform convergence and boundedness on K. It is a nonnegative part of the full squared norm, proving (1). Also Lh_n+N(h_n) cannot converge to zero in X, by (5) and the reverse triangle inequality.

## Application and dependencies

The exact modal density of proof 04 satisfies the center and tail bounds, as detailed in proof 05, and its exact source p>4 is certified in proof 15. Thus the theorem applies to its full normalized linearization. It applies to raw X3 only after a separate exact source certificate, which this topic does not provide. This proof verifies the scope of the earlier source_graph_nonlinearity obstruction without inheriting its parent source or moment tables. It does not prove that an inverse map loses nonlinear control in every stronger space, or exclude an IPM profile.

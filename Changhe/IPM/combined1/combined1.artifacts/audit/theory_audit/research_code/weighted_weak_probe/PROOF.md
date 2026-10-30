# Weak distance tests in a decreasing weighted L2 space

## Statement

Let 0<a<2, w(X)=(1+|X|^2)^(-a/2), and let H_a be the real S1 subspace of L2(w^2 dX). S1 means even in x and odd in y. Let the canonical IPM velocity U=(-R1 R2,R1^2) extend to H_a with a verified constant C_U:

    ||w U[h]||_2 <= C_U ||w h||_2.                       (1)

One audited choice is C_U=2/(2-a); an independently certified S1 constant may be substituted. Let c>1 and let rho be a smooth S1 background whose canonical velocity u obeys

    |rho|+|u|=O((1+r)^gamma),
    |D rho|=O((1+r)^(gamma-1)),  0<gamma<1.

Set V=cX+u and F=V.D rho-rho. Suppose h belongs to H_a and rho+h solves the stationary equation at the same c in divergence form. This means

    F+div(Vh)-(2c+1)h+U[h].D rho+div(h U[h])=0                 (2)

as distributions. The products in (2) are locally integrable: h and U[h] are locally L2 and the background is smooth. No derivative bound on h, no global membership assumption on F, and no coercive linear inverse are required.

For each integer k>=0 define

    t=r^2/(1+r^2), u0=1/(1+r^2), phi_k=y t^k u0^2,
    L_k=(2c+1)phi_k+c X.D phi_k,
    I_k=|integral F phi_k|,
    A_k=||L_k/w||_2,
    B_k=|||u| |D phi_k|/w||_2,
    C_k=||phi_k D rho/w||_2,
    H_k=||D phi_k/w^2||_infinity.

Every displayed quantity is finite. If m=||w h||_2 and D_k=A_k+B_k+C_U C_k, then

    I_k <= D_k m+C_U H_k m^2.                           (3)

Hence every such correction has

    m >= 2 I_k/[D_k+sqrt(D_k^2+4 C_U H_k I_k)].          (4)

If upper bounds are used for B_k, C_k or H_k, the same inequality and the resulting conservative lower bound remain valid. The assertion is at fixed c and for the exact background under consideration. It is a necessary test, not an existence theorem.

## Proof and admissibility of the test

Test (2) first against a compactly supported smooth function phi. Since div V=2c and div U[h]=0, integration by parts gives

    integral F phi = integral h[(2c+1)phi+cX.D phi+u.D phi]
                      - integral phi U[h].D rho
                      + integral h U[h].D phi.

Only the signs of the last two terms depend on the arrangement; the following absolute estimate does not. Weighted Cauchy-Schwarz, (1), and the definition of H_k give (3).

For completeness, pass from compact tests to phi_k by multiplying it by a smooth radial cutoff equal to one on r<=R and zero on r>=2R, with gradient O(1/R). At infinity phi_k=O(r^-3), D phi_k=O(r^-4), and X.D phi_k=O(r^-3). Thus L_k/w=O(r^(a-3)), which is L2 for a<2. The two background dual coefficients are O(r^(a+gamma-4)), also L2. Finally D phi_k/w^2=O(r^(2a-4)) is bounded and tends to zero. On the cutoff annulus the additional nonlinear coefficient phi_k D cutoff/w^2 has the same bound; weighted Cauchy-Schwarz controls it by the weighted L2 tails of h and U[h]. The extra transport coefficient is likewise controlled by the tail of L_k/w. These errors vanish as R tends to infinity. The pairing F phi_k is absolutely integrable since F=O(r^gamma) and gamma<1. Smoothness handles the origin. This proves both admissibility and finiteness.

Solving the quadratic inequality for m>=0 yields (4), in its numerically stable form. If I_k=0, the conclusion is the trivial m>=0. The formulas assume C_U H_k>0, which holds for the displayed nonconstant test functions.

## Explicit gradient bound

For k>=0,

    D phi_k=t^k u0^2 e_y
             +2yX t^(k-1)u0^3 (k u0-2t).

The k=0 formula is read after cancellation, so it is smooth at r=0. Since |y|<=r, the triangle inequality gives

    |D phi_k|/w^2
      <= t^k u0^(2-a)(1+2k u0+4t).                    (5)

For positive b, define

    S(j,b)= (j/(j+b))^j (b/(j+b))^b,  j>0,
    S(0,b)=1.

Differentiation on 0<=t<=1 shows S(j,b)=sup t^j(1-t)^b. Thus a safe explicit bound is

    H_k <= S(k,2-a)+2k S(k,3-a)+4S(k+1,2-a).           (6)

For k=0 and 0<a<=3/2 the exact bound is H_0=1. Indeed at fixed t the angular maximum of |D phi_0|/w^2 is

    (1-t)^(2-a) max(1,|1-4t|).

The first branch is at most one. For the other branch it suffices to use the larger exponent case 2-a=1/2: maximizing sqrt(1-t)|1-4t| gives one, at t=0 and t=3/4. The value at the origin is one. This proves the exact claim.

## Exact evaluation for the campaign's single-scale backgrounds

Suppose the background has the exact finite polar representation

    rho=r sum u0^a_j R_(j,n)(t) sin(n theta),
    psi=r^2 sum u0^a_j S_(j,n)(t) sin(n theta),
    u=(-psi_y,psi_x), a_j=(j+1)delta/2.

The construction and canonical input checks are in ../weak_probe_audit/PROOF.md. Let

    T_(b,d)P=(d-2bt)P+2t(1-t)P',
    ell_k=3c+1+2ck(1-t)-4ct,
    g_k=1+2k(1-t)+4t.

For a family P_(j,n) representing r^d times its radial powers, define the exact square polynomial at index J by summing over every ordered pair of equal angular mode with j+l=J:

    E_J(t)=sum [n^2 P_(j,n)P_(l,n)
                +T_(a_j,d)P_(j,n) T_(a_l,d)P_(l,n)].

Let E^u use S and d=2, and E^rho use R and d=1. Angular orthogonality and r dr=dt/[2(1-t)^2] give

    A_k^2=(pi/2) integral t^(2k+1)(1-t)^(1-a) ell_k^2 dt,
    B_k^2 <= (pi/2) sum_J integral t^(2k+1)
                 (1-t)^(1-a+(J+2)delta/2) g_k^2 E^u_J dt,
    C_k^2 <= (pi/2) sum_J integral t^(2k+1)
                 (1-t)^(1-a+(J+2)delta/2) E^rho_J dt.  (7)

The B bound uses (5), not an equality for the angular gradient. The C bound uses y^2<=r^2 before angular orthogonality; it is also an upper bound, not an equality. The pairing I_k is independent of the weight and is evaluated from the exact weak background equation by the already established localized-probe formula. No residual cache or numerical spatial quadrature is needed.

To evaluate (7), expand the finite polynomial in u0=1-t. Each integral is Beta(2k+2,b+q+1), where b>-1 and q is a nonnegative integer. The first beta parameter is a positive integer and the second a positive rational for rational a,delta. Its value is exactly rational by

    Beta(1,v)=1/v,
    Beta(M+1,v)=M Beta(M,v)/(M+v).

All polynomial cancellations and beta sums may therefore be exact. Multiplication by pi, square roots and the powers in (6) are enclosed by interval arithmetic. Every candidate and selected velocity constant must be identified in the output.

## Verification status

This is an original extension of the independently audited unweighted weak probe. The proof and any numerical results remain CLAIMED until independent review. It does not verify the high inverse hypothesis in the dyadic weighted closure, nor does it establish weighted residual smallness. Its purpose is to test how much a change of low norm can reduce the necessary correction distance.

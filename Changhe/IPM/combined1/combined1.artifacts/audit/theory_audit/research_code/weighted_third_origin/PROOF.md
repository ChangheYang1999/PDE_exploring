# The weighted third-order endpoint has no normalized stationary inverse

Status: new T4 extension, OPEN pending independent Opus review. This note concerns the third-order endpoint itself. It does not contradict the fractional or interpolated high spaces in Analysis II.

## Statement and exact space

Let omega(X)=(1+4|X|^2)^(2/5). Fix constants b2,b1,b0>0 and bminus>=0. On real smooth S1 functions, meaning even in x and odd in y, set

    Z3(h)^2 = ||omega D^3 h||_2^2 + b2 ||omega D^2 h||_2^2
              + b1 ||D h||_2^2 + b0 ||h||_2^2
              + bminus ||h||_dotHminus1^2.                 (1)

Ordered Cartesian derivatives carry their full Frobenius multiplicities. The last summand is omitted when bminus=0. Define the Hilbert space by completion of finite-norm smooth S1 functions. The third-order endpoint E3 of Analysis II Route U is a particular choice of the positive constants in (1).

Let rho be a smooth S1 background, with canonical IPM velocity u and V=cX+u. Write

    Lh=V.grad h-h+U[h].grad rho,
    U[h]=(-R1R2 h,R1^2 h).

Assume V is globally Lipschitz, its derivatives of orders1 through4 are bounded, and the derivatives of grad rho of orders0 through3 are bounded. Assume exactly

    V(0)=0, DV(0)=diag(2c-1,1), grad rho(0)=(0,a),
    1<c<=2, a>=5c-4.                                    (2)

Then there are real smooth S1 functions h_n with h_n,Lh_n in Z3, such that

    Z3(h_n)=1, partial_y U2[h_n](0)=0,
    partial_y(Lh_n)(0)=0, Z3(Lh_n)->0.                    (3)

Consequently no finite M can satisfy Z3(h)<=M Z3(Lh) on all these normalized tests. In particular, an injective maximal low realization whose inverse on every f in Z3 with f_y(0)=0 takes values in Z3 cannot have a bounded Z3 inverse estimate. Any such realization includes the tests in (3) because h_n and Lh_n are in its low graph domain; this inclusion remains an explicit requirement for a different low space.

## 1. A weighted integer-order scaling lemma

For real S1 Schwartz f define E_epsilon f(X)=epsilon^2 f(X/epsilon). In two dimensions, changing variables gives

    ||omega D^k E_epsilon f||_2^2
       =epsilon^(6-2k) integral omega(epsilon Y)^2 |D^k f(Y)|^2 dY.

Since omega(epsilon Y)<=omega(Y) for epsilon<=1 and omega(epsilon Y)->1, dominated convergence gives

    Z3(E_epsilon f)->||D^3 f||_2=||f||_dotH3.             (4)

Here every lower derivative term vanishes. The negative norm, when present, has exact scaling

    ||E_epsilon f||_dotHminus1=epsilon^4||f||_dotHminus1.

It is finite: parity implies integral f=0, and

    |hat f(xi)|<=C |xi| integral |Y f(Y)|dY

near zero. Integrating |xi|^-2|hat f|^2 there and using Plancherel away from zero bounds this norm by a finite weighted smoothness seminorm.

For definiteness, let S(f)=max_(|k|<=3) sup_Y <Y>^12 |D^k f(Y)|. The same estimates give

    Z3(E_epsilon f)<=C S(f), 0<epsilon<=1,               (5)

for every smooth S1 f with finite S(f). The constant depends only on (1). Equations (4)-(5) require neither a fractional multiplier commutator nor a nonlocal velocity term in the norm.

## 2. The frozen zero singular sequence

Freeze the origin operator:

    L0w=diag(2c-1,1)X.grad w-w-a Qw,
    Fourier(Qw)=xi_x^2/|xi|^2 Fourier(w).

The explicit logarithmic Fourier calculation in ../origin_spectral_line/PROOF.md, Sections2-4, with q=3 gives the boundary values

    alpha_v=2-c, alpha_h=5c-4-a.

They satisfy alpha_h<=0<=alpha_v by (2). If they differ, the coefficient B=alpha_h-alpha_v is negative, and the real zero parameter lies in the closed singular strip. The endpoint construction also applies when a boundary is zero, including the common zero boundary c=2,a=6. Therefore there are real S1 Schwartz w_n, with smooth compact Fourier support away from both axes, for which

    ||w_n||_dotH3=1, ||L0w_n||_dotH3->0.                 (6)

For completeness, the conjugated operator is

    -partial_u-(2c-2)partial_v+alpha_v+B e^(2v)/(1+e^(2v)).

At either endpoint, long cutoffs centered at v tending to the corresponding infinity make the residual tend to zero. For alpha_h<0<alpha_v, the v profile

    exp(alpha_v v/(2c-2)) (1+e^(2v))^(B/(4c-4))

belongs to L2 at both ends and solves the zero equation. Cut it off in v and multiply by a long normalized cutoff in u. A purely imaginary positive-quadrant amplitude with S1 extension gives real inverse Fourier transforms. This supplies (6) without assuming an eigenfunction of the full variable-coefficient operator.

## 3. Variable coefficients and exact pinning

For each fixed w_n, homogeneity of U gives

    L E_epsilon w_n-E_epsilon L0w_n=E_epsilon R_epsilon,
    R_epsilon=(V(epsilon X)/epsilon-DX).grad w_n
              +(grad rho(epsilon X)-(0,a)).U[w_n].       (7)

The compact frequency support makes both w_n and U[w_n] Schwartz. The coefficient differences and their derivatives through order3 converge to zero on every compact set. Globally, the first coefficient is bounded by C|X|, its first derivatives are bounded, and its higher derivatives have nonnegative powers of epsilon. The second coefficient and its derivatives are bounded. Using the fixed Schwartz factors to control the tails proves S(R_epsilon)->0. Thus (5) shows that the error in (7) tends to zero in Z3.

Choose a fixed real S1 compact-frequency Schwartz g with c[g]=partial_y U2[g](0)=1. Existence follows by taking an imaginary positive-quadrant bump: the canonical strain multiplier has a fixed nonzero sign against it. Then g,Lg are in Z3; the latter follows from the same coefficient and finite smoothness bounds. Put

    h_(n,epsilon)=E_epsilon w_n-epsilon c[w_n]g.

This pins c[h] to zero exactly. Both the correction and its image under L tend to zero in Z3 for fixed n. First take n large in (6), then epsilon small in (4)-(7), and normalize. This gives Z3(h_n)=1 and Z3(Lh_n)->0.

The input trace is exact as well. At the origin parity gives h(0)=U[h](0)=0. The y derivative of V.grad h-h cancels because DV(0)_yy=1. Hence

    (Lh)_y(0)=a partial_y U2[h](0)=0.

The local/contact term of the canonical velocity is retained in both occurrences of c[h]. This proves every claim in (3).

## Scope and relation to the campaign

The result rules out upgrading a third-order endpoint growth bound to a bounded stationary inverse in that same endpoint norm under (2). Analysis II gives only a growth bound at E3 and obtains decay after interpolation with E2. Its main fractional norm has order2+s with very small s. Neither construction asserts an E3 inverse, and this note refutes neither one. The earlier dyadic theorem uses q=2+s and needs its separate inverse-floor argument.

The constants b2,b1,b0 may be arbitrarily large. They disappear under shrinking concentration because the third derivative has the highest order. Thus increasing fixed lower-level weights cannot remove this endpoint obstruction. A different singular weight at the origin, a different local regularity order, or a domain restriction excluding these tests is outside the statement.

Dependencies: the explicit frozen Fourier construction in T4-145, the weighted scaling and localization proof here, and the stated origin identities. No numerical calculation or external spectral theorem is used. The exact case4/candidate parameters and low-domain inclusion must be checked before applying the statement to a particular operator.

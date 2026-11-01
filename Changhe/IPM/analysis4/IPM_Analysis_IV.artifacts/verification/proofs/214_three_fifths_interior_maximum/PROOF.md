# Interior angular maxima for the last two delta = 3/5 branches

Status: PROVED after independent theory-part review, V442. Roots3 and4 have exact sufficient radius certificates; the root3 certificate was admitted in V447.

## Exact statement

Let b be the third or fourth real root, in increasing order, of the first-obstruction polynomial in topic 200. Let rho be its uniquely tuned exterior solution at delta = 3/5 and c = 5/2, with leading density f(theta) = sin(theta) + b sin(3 theta). There is a finite radius R such that, for every r >= R, rho(r,theta) has exactly one critical point in 0 < theta < pi/2. The angular derivative is positive before this point and negative after it. Thus the point is a strict maximum. Its angle tends, as r tends to infinity, to

    arcsin(sqrt((1 + 3b)/(12b))).

By S1 symmetry the upper half-plane has two reflected maxima, and theta = pi/2 is a local angular minimum. The solution is strictly positive on the open upper half-plane after increasing R if necessary. Positive amplitude scaling changes only the required radius by the factor epsilon^(5/3). Negative amplitude reverses maxima and minima. No assertion concerns a whole-plane extension or the sharp radius for these properties.

## Removing the endpoint zero from the angular derivative

Write z = r^(-3/5), T = sin(theta)^2 and

    r^(-2/5) rho(r,theta) = f(theta) + sum_(n>=2) z^(n-1) f_n(theta),
    f_n(theta) = sum_(m positive odd) a_(n,m) sin(m theta).

The all-order convergence theorem in topic 200, together with the bandwidth bound m <= 4n-1, gives convergence after any fixed polynomial weight in n or m on every smaller z disk. Put

    E_j(z) = sum_(n>=2) sum_m m^j |a_(n,m)| z^(n-1).

In particular E_1, E_2 and E_4 tend to zero as z tends to zero.

For m = 2k+1 define the polynomial

    P_m(T) = (-1)^k [1 + 2 sum_(j=1)^k T_j(2T-1)],

where T_j is the Chebyshev polynomial satisfying T_j(cos t) = cos(jt). The finite sine-sum identity gives

    P_m(sin(theta)^2) = cos(m theta)/cos(theta)

for 0 <= theta < pi/2; the polynomial supplies the endpoint value. Moreover, |P_m(T)| <= m for T in [0,1]. The derivative identity T_j' = j U_(j-1), with |U_(j-1)(x)| <= j on [-1,1], gives

    |P_m'(T)| <= 4 sum_(j=1)^k j^2 = m(m^2-1)/6.

Both Chebyshev identities follow from differentiating the cosine identity away from the endpoints and extending polynomially. The bound for U follows from |sin(jt)| <= j |sin t|, including the endpoints by continuity.

It follows that the normalized angular derivative has the form

    r^(-2/5) partial_theta rho(r,theta) = cos(theta) H_z(T),
    H_z(T) = 1 + 3b - 12b T + sum_(n>=2,m) m a_(n,m) z^(n-1) P_m(T),

with

    sup_[0,1] |H_z(T) - (1 + 3b - 12b T)| <= E_2(z),
    sup_[0,1] |H_z'(T) + 12b| <= E_4(z)/6.

The weighted convergence justifies termwise differentiation and continuity in T and z.

## Uniqueness, signs and limiting angle

The exact root intervals in topic 200 show 1/9 < b < 1 for both roots under consideration. Choose z_* > 0 inside the convergence disk such that

    E_2(z_*) < min(1+3b, 9b-1),
    E_4(z_*) < 72b.

The series defining E_j have nonnegative coefficients, so both inequalities hold for every 0 <= z <= z_*. They imply H_z(0) > 0, H_z(1) < 0 and H_z'(T) < 0 on [0,1]. The intermediate value theorem and strict decrease give exactly one zero T_z in (0,1). Since theta maps strictly increasingly onto T and cos(theta) > 0 in the open quadrant, the angular derivative has precisely the asserted signs.

Uniform convergence H_z -> 1+3b-12bT gives T_z -> (1+3b)/(12b). For example, the displayed E_2 bound yields |T_z - (1+3b)/(12b)| <= E_2(z)/(12b). Continuity of arcsin(sqrt(T)) gives the angle limit. S1 reflection across theta = pi/2 yields the second maximum and the intervening local minimum. Finally f(theta)/sin(theta) >= 1-b, and |sin(m theta)| <= m sin(theta) gives positivity when also E_1(z_*) < 1-b. This completes the proof.

## Exact finite certificates from the residue box

Use any reviewed topic 205 box at w_0 = 2^(-q), with Q = 10, B = 4, prefix length N, prefix bounds d_n >= n ||f_n||_1 and density coordinates x_r bounding X_r(w_0), for 1 <= r <= Q. Choose integer t > q/Q, put z = 2^(-t) and eta = z^Q/w_0 <= 1/2. Topic 210's estimates give finite rational upper bounds U_1 >= E_1 and U_2 >= E_2. An additional bound is

    U_4 = B^4 [sum_(n=2)^N n^3 d_n z^(n-1)
         + sum_(r=1)^Q z^(N+r-1) x_r
           ((N+r)^3 + 3(N+r)^2 Q eta
            + (27/4)(N+r) Q^2 eta + 8 Q^3 eta)].

Indeed, for integer k >= 1 and 0 <= eta <= 1/2,

    k eta^k <= eta,
    k^2 eta^k <= (9/4) eta,
    k^3 eta^k <= 8 eta.

The last two inequalities follow by checking k <= 3 and k <= 4 respectively, then observing that the ratios ((k+1)/k)^2 and ((k+1)/k)^3 are less than 2 thereafter. Expanding (N+r+Qk)^3 and applying these bounds coefficientwise to X_r proves U_4 >= E_4.

If [b_-,b_+] is the rational isolating interval, it suffices to check

    U_1 < 1-b_+,
    U_2 < min(1+3b_-, 9b_--1),
    U_4 < 72b_-.

These are finite strict rational inequalities. They certify all conclusions on the closed exterior r >= 2^(5t/3), with the amplitude factor already stated. They do not establish the smallest such radius.

## Dependencies and scope

The proof uses the exact root isolation and convergence theorem in topic 200, amplitude homogeneity, the bandwidth estimate, and S1 symmetry. Explicit certificates additionally use the independently replayed topic 205 majorant boxes. No high-order numerical fit, extrapolation or sampled angular grid is used. The qualitative argument is independent of the unreviewed numerical work for this topic.

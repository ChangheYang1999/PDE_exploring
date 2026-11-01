# Sign and angular monotonicity of the convergent delta3/5 branches

Status: PROVED after independent theory-part review, V441. Exact sufficient radius certificates are available for all four roots, including root3 admitted in V447.

## Statement

Let b be one of the four real roots, in increasing order, of the first-obstruction polynomial certified in200. Let rho_b be the convergent exterior solution with delta=3/5, c=5/2 and leading profile

    f_b(theta) = sin(theta)+b sin(3theta).

All four leading profiles are strictly positive for 0<theta<pi. For the first two roots, f_b is strictly increasing on 0<theta<pi/2. For each of the four solutions there is a finite R beyond its proved convergence threshold such that rho_b(r,theta)>0 for r>=R and 0<theta<pi, with the opposite sign on the lower half-plane. For the first two solutions, R can also be chosen so that partial_theta rho_b(r,theta)>0 for r>=R and 0<theta<pi/2. Reflection symmetry gives the corresponding decrease on pi/2<theta<pi. Scaling the leading data by a positive amplitude preserves these conclusions after increasing R as prescribed by amplitude scaling; a negative amplitude reverses both inequalities.

These are statements about the exterior solution. They do not establish a whole-plane extension, a sign for the velocity, or monotonicity in radius. The R used for these sign conclusions is not asserted to equal a previously certified convergence radius.

## Root location and leading profile

The rational isolating intervals from200 imply

    0 < b_1 < b_2 < 1/9 < b_3 < b_4 < 1.

The exact arithmetic verification of these inequalities is retained alongside this proof. Since sin(3theta)=sin(theta)(3-4sin(theta)^2),

    f_b(theta)/sin(theta) = 1+3b-4b sin(theta)^2 >= 1-b > 0.

Likewise

    f_b'(theta)/cos(theta) = 1+3b-12b sin(theta)^2.

For b=b_1 or b_2 this is at least 1-9b>0. The denominators in these displayed quotients are nonzero on the stated open angular intervals. Their polynomial expressions extend continuously to the endpoints. This proves the leading-profile assertions.

## Uniform sign of the full exterior solution

Write z=r^(-3/5). The convergence theorem and finite bandwidth give

    r^(-2/5) rho_b(r,theta) = f_b(theta) + sum_(n>=2) z^(n-1) f_n(theta),
    f_n(theta) = sum_(m odd, m>0) a_(n,m) sin(m theta),

with convergence after multiplying coefficients by every fixed power of n or m on any strict smaller z disk. In particular, the two nonnegative series

    E_1(z)=sum_(n>=2) sum_m m |a_(n,m)| z^(n-1),
    E_2(z)=sum_(n>=2) sum_m m^2 |a_(n,m)| z^(n-1)

converge for sufficiently small positive z and tend to zero as z decreases to zero. One can see this directly from m<=4n-1 and the exponential coefficient bound: multiplying by a polynomial in n preserves convergence on a strict smaller disk, and both series have no constant term.

For integer m>=1 and theta in[0,pi],

    |sin(m theta)| <= m sin(theta).

For example, division of exp(im theta)-exp(-im theta) by exp(i theta)-exp(-i theta) gives a sum of m unit complex numbers, proving the bound away from the endpoints, and continuity covers them. Hence the full normalized density, divided by sin(theta), differs from f_b(theta)/sin(theta) by at most E_1(z). Choose z_*>0 inside the convergence disk with E_1(z_*)<1-b. Nonnegativity of the coefficients of E_1 gives the same bound for 0<=z<=z_*. Thus rho_b is positive in the upper half-plane whenever r>=z_*^(-5/3). The lower-half-plane statement follows from S1 oddness in y.

For odd m and theta in[0,pi/2], put t=pi/2-theta. Then |cos(m theta)|=|sin(m t)|<=m sin(t)=m cos(theta). The normalized angular derivative, divided by cos(theta), consequently differs from f_b'(theta)/cos(theta) by at most E_2(z). For b=b_1 or b_2, choose z_* still smaller so E_2(z_*)<1-9b. This gives the stated strict monotonicity, including control arbitrarily close to the symmetry axis. Merely using a uniform bound for the unnormalized derivative would not supply that endpoint control.

## Amplitude and dependencies

For leading amplitude epsilon, the n-th density coefficient scales as epsilon^n. Dividing the full series by epsilon shows that its correction is evaluated with absolute size |epsilon|z for the estimates above. Thus replacing R by |epsilon|^(5/3)R suffices, and the sign of epsilon multiplies both stated inequalities. This uses the exact amplitude homogeneity of the tuned branch.

Dependencies: the exact root certificate200, the all-order exterior convergence theorem200 with the rational tuning theorem, the bandwidth bound of202/205, S1 symmetry, and amplitude homogeneity. No high-order numerical fit is used.

## Explicit sign and monotonicity certificates

The residue majorant in205 permits a quantitative version. Let its verified box at w_0=2^(-q) have density coordinates b_r bounding X_r(w_0), 1<=r<=Q, with Q=10, B=4 and prefix N. Let d_n>=n||f_n||_1 be the supplied prefix bounds. Choose an integer t with t>q/Q and set z=2^(-t), w=z^Q and theta_0=w/w_0<=1/2. Then

    E_1(z) <= B [sum_(n=2)^N d_n z^(n-1)
                     +sum_(r=1)^Q b_r z^(N+r-1)] = U_1,

and

    E_2(z) <= B^2 [sum_(n=2)^N n d_n z^(n-1)
                     +sum_(r=1)^Q (N+r+Q theta_0)b_r z^(N+r-1)] = U_2.

To prove the second tail estimate, write X_r(w)=sum_k x_k w^k with x_k>=0. For 0<=theta_0<=1/2, k theta_0^k<=theta_0 for every integer k>=1, because k<=2^(k-1). Consequently w X_r'(w)<=theta_0 X_r(w_0)<=theta_0 b_r. The extra weight N+r+kQ then gives the displayed bound. The first estimate only uses X_r(w)<=b_r. Both are exact finite rational expressions.

If U_1<1-b_upper, where b_upper is the rational upper isolating endpoint, positivity holds on every r>=2^(5t/3). For roots1 and2, if also U_2<1-9b_upper, angular monotonicity holds on the same exterior. The strict inequality t>q/Q ensures this entire closed exterior lies strictly inside the convergence region in z. This certificate is sufficient and does not locate the smallest radius on which either geometric property holds.

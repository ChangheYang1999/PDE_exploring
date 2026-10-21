# Every transverse axis trace is smooth for the noncompact packet

Date: 2026-10-21. Status: proof written and checked before code; independent review pending.

## Exact statement and dependencies

Let u, Phi, c_F=(2pi)^(-2) and the real continuous function V(s,y) be exactly as in ../noncompact-packet-counterexample/PROOF.md and ../noncompact-packet-joint-regularity/PROOF.md:

    u(t)=t^(-1/2) exp(-(log t)^2) sin(2pi log t), t>0,
    V(s,y)=-4c_F integral_0^infinity sin(yr)r^(-2)
                  integral_0^infinity u(t)sin(s t r^2)
                                  (1+t^2r^2)^(-1/2)dt dr.          (1)

For every nonnegative integer j and every real s, the ordinary one-variable derivative partial_y^j V(s,0) exists. The function

    G_j(s)=partial_y^j V(s,0)

is smooth on the whole real line. Every even trace vanishes identically. For m>=0 the odd trace has the convergent formula

    G_(2m+1)(s)=(-1)^(m+1)2c_F integral_0^infinity sin(sk)h_m(k)dk,
    h_m(k)=k^(m-1) integral_0^infinity
                         u(t)t^(-m)(1+kt)^(-1/2)dt.               (2)

All G_j(0)=0. In contrast, the preceding result proves V is not C1 on any neighborhood of (0,0). Thus smoothness of every one-variable transverse axis trace does not imply joint smoothness. This is not a statement about the B_j coefficients of a coupled IPM profile or about task endpoints.

We use two already proved exact facts: every absolute power moment of u is finite; and

    integral_0^infinity u(t)t^(-1/2-n)dt=0, n=0,1,2,... .          (3)

Both follow by t=exp(z) and the elementary Gaussian sine integral in the preceding proof. We also use that each derivative u^(a) has all absolute power moments and is flat at zero and rapidly decreasing at infinity. This follows by differentiating its displayed formula: u^(a) is a power of t times exp(-(log t)^2) times a polynomial in log t and bounded sine/cosine factors.

## Regularity in y at a fixed nonzero s

For epsilon>=0 introduce the grouped regularization

    V_epsilon(s,y)=-4c_F integral sin(yr)r^(-2)
                  integral u(t)exp(-epsilon t r^2)sin(s t r^2)
                                          w_r(t)dt dr,
    w_r(t)=(1+t^2r^2)^(-1/2).                             (4)

This is an auxiliary integral, not a new PDE solution or a change of the packet's definition. At epsilon=0 it is (1). We prove convergence of every y derivative as epsilon decreases to zero for s bounded away from zero, uniformly on compact y intervals.

For each a>=0, the function d^a/dz^a (1+z^2)^(-1/2) is bounded on z>=0. This follows inductively from its rational expression, smooth at zero and decaying at infinity. Hence

    |partial_t^a w_r(t)|<=C_a r^a.                       (5)

Let J_epsilon(s,r)=integral_0^infinity u(t)w_r(t)exp((is-epsilon)t r^2)dt. Its imaginary part is the inner integral of (4). For r>=1 and |s|>=s_0>0, integrate by parts L times in t. All boundary terms vanish: derivatives of u are flat at zero and rapidly decreasing, and all derivatives of w_r have polynomial bounds. The exponential has modulus at most1. Leibniz' rule and (5) give

    integral |partial_t^L(u w_r)|dt <= C_L r^L,
    |J_epsilon(s,r)| <= |is-epsilon|^(-L)r^(-2L)C_Lr^L
                       <= C_L s_0^(-L)r^(-L).           (6)

The bounds are uniform for epsilon>=0. Thus after any fixed j y derivatives the high-r integrand is bounded by C r^(j-2-L), integrable on r>=1 when L>j-1.

For 0<r<=1, the imaginary part is bounded by |s|r^2 integral |u|t, uniformly in epsilon>=0. For j>=1, the j-th y derivative of sin(yr) is bounded by r^j; for j=0 it is bounded by1. These bounds make the low-r integral and every y derivative integrable, uniformly on compact s,y sets. Differentiation under the integral and dominated convergence in epsilon are justified. In particular V is smooth as a function of y for every fixed s!=0, and every derivative agrees with the limit from V_epsilon.

At s=0, equation(1) gives the identically zero one-variable function y -> V(0,y), so every ordinary y derivative there exists and is zero. This uses no joint differentiability.

## Identification of the odd traces by a justified regularization

For even j the derivative of sin(yr) at y=0 is zero, and G_j(s)=0 for s!=0. The preceding paragraph supplies the same value at s=0. For j=2m+1 and epsilon>0 differentiation in (4) gives

    G_(2m+1),epsilon(s)=(-1)^(m+1)4c_F
         integral_0^infinity r^(2m-1)
           integral_0^infinity u(t)exp(-epsilon t r^2)
                            sin(s t r^2)w_r(t)dt dr.              (7)

For m>=1, this joint integral is absolutely convergent even after replacing the sine and weight by1, because

    integral_0^infinity r^(2m-1)exp(-epsilon t r^2)dr
             =(m-1)!/(2(epsilon t)^m),

and integral |u|t^(-m) is finite. For m=0, the small-r sine bound and the large-r bound w_r<=1/(tr) give joint absolute integrability exactly as in the first-trace proof, without needing epsilon. Thus Fubini is valid in (7).

Set k=t r^2. Then r^(2m-1)dr=(1/2)k^(m-1)t^(-m)dk and w_r=(1+kt)^(-1/2). Equation(7) becomes

    G_(2m+1),epsilon(s)=(-1)^(m+1)2c_F
                 integral sin(sk)exp(-epsilon k)h_m(k)dk.         (8)

The factor1/2 is included explicitly. This argument avoids an unjustified swap in the unregularized higher-trace integral, whose absolute integrability in (r,t) need not hold.

## Decay of h_m and global smoothness of the traces

At 0<k<=1,

    |h_m(k)|<=k^(m-1) integral |u(t)|t^(-m)dt.                     (9)

For m>=1 this is locally integrable even before retaining the sine. For m=0 it is O(k^-1); retaining sin(sk) makes the order-zero integral convergent, and every s derivative of positive order supplies a positive power of k. Consequently the low-k part of (2) is smooth for every m.

For every N>=1 the global Taylor remainder for (1+z)^(-1/2), z>=0, is bounded in absolute value by C_N z^N. Factor (1+kt)^(-1/2)=k^(-1/2)t^(-1/2)(1+(kt)^(-1))^(-1/2). Each of the first N integrated Taylor terms is a multiple of

    integral u(t)t^(-m-1/2-n)dt,

which vanishes by (3), since m+n is a nonnegative integer. The remainder gives, for k>=1,

    |h_m(k)|<=C_N k^(m-3/2-N)
                         integral |u(t)|t^(-m-1/2-N)dt.           (10)

For any s-derivative order ell choose an integer N>m+ell-1/2. Then integral_1^infinity k^ell|h_m(k)|dk is finite. All s derivatives of the high-k part are justified uniformly on compact s sets. Together with (9), this proves that the right side of (2) is smooth on R and has value zero at s=0.

The same bounds, retaining the sine at low k when m=0, justify epsilon ->0 in (8). For fixed s!=0, the y-derivative convergence proved using (6) identifies this limit with the actual ordinary derivative of V. At s=0 both the formula and the already existing one-variable derivative equal zero. This proves (2) and the claimed global smoothness of every trace.

## Scope and verification

Every asserted G_j is the classical derivative in the y variable of a fixed-s slice. Its smooth dependence on s does not assert that the corresponding mixed derivatives are continuous on a two-dimensional neighborhood, and does not allow interchange of mixed derivatives there. The non-C1 result in the preceding proof remains fully consistent with all these axis statements. There is no assertion that center obstruction coefficients of a coupled profile vanish.

Own code will check the exact Jacobian, index m+n in the Gaussian moments, prefactors and signs. The general proof covers all orders; finitely many code checks are supporting diagnostics. Completed independent model review and source pins will be stored in verification/. No formal proof assistant build is used.

# The seventh stationary tail and the next fixed residual sector

Status: the formal argument and two independent exact original-source reconstructions are complete. Every seventh-order coefficient agrees with the numerics record. Lead review is pending. This is a finite formal expansion, not a convergence or existence theorem.

## 1. Setting and statement

Fix the exact original state131 exponent

    c = 4076476460239181/2251799813685248,
    gamma = 1/c, delta = 1-gamma,
    p_n = 1-n delta.

The equation and velocity convention are

    F(rho) = (c X + U[rho]).grad rho-rho,
    U = (-psi_y,psi_x), -Delta psi = rho_x.

Let C_1(theta) be the leading even cosine potential of original state131, independently recovered from its860 canonical rational coefficients. Its largest angular frequency is18. Define Theta_1 and Psi_1 by differentiating r^(p_1+3) C_1:

    rho_1 = -partial_y Delta(r^(p_1+3) C_1),
    psi_1 = partial_x partial_y(r^(p_1+3) C_1).

There is a unique sequence of finite odd sine density polynomials Theta_n, 1<=n<=8, and even sine stream polynomials Psi_n, solving the homogeneous angular Poisson equations and cancelling the formal stationary coefficients through order8. Their density and stream degrees are at most20n-1 and20n respectively. The definitions and uniqueness are in sections2-3.

For a potential with branches j=0,...,6, whose first seven leading homogeneous potentials equal these stationary orders, the residual sector indexed(h,q)=(7,0) is the fixed sine polynomial

    E_7 = sum_(i+j=8,1<=i,j<=7)
              [(p_i+1) Psi_i Theta_j' - p_j Psi_i' Theta_j]
        = 7(c-1) Theta_8.                              (1)

It has radial power p_8=1-8delta. No coefficient in the radial descendants of those seven branches can alter E_7. Adding branch j=7 with the eighth stationary leading density cancels it.

This does not assert that E_7 is the leading nonzero residual of an arbitrary seven-branch candidate. If only sectors(0..6,0),(0,1),(1,1) are set to zero, the unconstrained sector(2,1) has power gamma-2delta-2, which is strictly larger than p_8. An approximate penalty on its coefficients does not remove it from the asymptotic expansion.

## 2. Angular inverse and nonresonance

For a homogeneous density r^p Theta(theta), write its stream as r^(p+1) Psi(theta). The angular Poisson equation is

    [-partial_theta^2-(p+1)^2] Psi
          = p cos(theta) Theta - sin(theta) Theta'.   (2)

If Theta=sum_(k odd positive) a_k sin(k theta), the right side contributes

    (p-k)a_k/2 to sin((k+1)theta),
    (p+k)a_k/2 to sin((k-1)theta),

with sin(0 theta)=0 and negative frequencies reduced by sin(-m theta)=-sin(m theta). Divide each even sine coefficient by m^2-(p+1)^2 to obtain Psi.

For the exact c above and 1<=n<=8, p_n+1=2-n delta is not an integer. Indeed delta=A/B with A=1824676646553933, B=4076476460239181 and gcd(A,B)=1. An integer value would imply B divides n, impossible since0<n<=8<B. Thus no Fourier denominator in(2) vanishes. This uniquely determines Psi within the finite even sine class. The same noninteger condition excludes additional homogeneous harmonic terms at this radial power.

## 3. The formal recurrence

In polar coordinates the advection of r^(p_j)Theta_j by the stream r^(p_i+1)Psi_i is

    r^(p_i+p_j-1)
        [(p_i+1)Psi_i Theta_j' - p_j Psi_i' Theta_j].  (3)

The exponents satisfy p_i+p_j-1=p_(i+j). The linear coefficient on the n-th density is

    c p_n-1=-(n-1)(c-1).

Thus the leading n=1 equation vanishes identically, and for n>=2 define

    S_n=sum_(i+j=n) [(p_i+1)Psi_i Theta_j'
                                      -p_j Psi_i' Theta_j],
    Theta_n=S_n/[(n-1)(c-1)].                          (4)

The denominator is nonzero because c>1. Equations(2) and(4) give existence and uniqueness recursively. For each finite order they are exact rational operations on finite trigonometric polynomials. The order n coefficient of F is zero by substitution; this is a formal algebraic assertion, with no interchange of an infinite sum.

Inductively Theta_n has odd frequencies at most20n-1 and Psi_n even frequencies at most20n. In(3) the product of degrees20i and20j-1 has degree at most20n-1. Equation(2) increases the degree by at most1. This proves the bounds.

An even cosine potential C_n of degree at most20n-2 can also be recovered uniquely. Apply -partial_y Delta to r^(p_n+3) cos(m theta). Its highest sine frequency is m+1 and has nonzero coefficient for every nonnegative even m: p_n is noninteger, so none of the factors p_n+3-m, p_n+3+m, p_n+1-m vanishes. At m=0 the two signed frequency contributions coincide and must both be retained. Solve from the highest odd density frequency down to1. This triangular procedure gives C_n and reproduces Theta_n exactly. Differentiating it by partial_x partial_y gives the same Psi_n by(2) and nonresonance.

## 4. Invariance and the descendant qualification

A smooth finite radial branch admits a binomial expansion at infinity, with its descendants indexed by an integer q>=0 and powers

    alpha(h,q)=gamma-h delta-2q.

The linear term can contribute to(7,0) only from branch j=7, which is absent. Quadratic interactions contribute to this sector only when i+j=6 in zero-based branch indices and both descendant indices are zero. These are precisely the leading interactions in(1), all fixed by the seven leading moments.

There is no collision with another sector in the finite seven-branch residual. Equality of two radial powers would give (h-h')delta=2(q'-q). Coprimality implies B divides h-h'. Here0<=h,h'<=13 and B>13, so h=h' and then q=q'. In particular radial descendants cannot absorb the fixed coefficient E_7.

The exponent difference between(2,1) and(7,0) is5delta-2, which is positive for this exact delta. Therefore(2,1) precedes E_7 unless it is zero exactly. If(2,1) is also removed, then E_7 precedes(3,1) because2-4delta>0, and it precedes the first q=2 sector because4-7delta>0. These are strict rational comparisons. Subsequent invariant statements are always conditional on the specified earlier sectors vanishing exactly.

## 5. Independent verification and numerical result

The verification recovers state131 directly from the read-only original JSON and NPZ, checks its canonical digest, and extracts its leading cosine polynomial. A real sine recurrence and an independent complex Fourier differentiation/convolution agree on every density, stream and potential order through8. The existing six-order record and the numerical work's exact seventh-order coefficients are comparison inputs, not premises of the recurrence. Every compared input and implementation is hashed.

The new seven-branch invariant has full-circle norm in(9679.9655,9679.9656), approximately9679.96558019927435194. Its first-quadrant norm is4839.98279009963717597. The old six-branch residual at the same exponent has full-circle norm4331.15745649082938888 and first-quadrant norm2165.57872824541469444. The latter is not the invariant after adding the seventh stationary branch: it omits the interactions(1,7) and(7,1) in one-based stationary-order notation.

The seventh potential has maximum coefficient magnitude138.26904068945842515. Its density has70 odd sine coefficients through frequency139; the first three are-21.90824839824379453,78.22820506075036798,-118.97814871736291410. These decimals summarize the exact rational files.

The full-circle angular norm is sqrt(pi sum_m E_m^2). The first-quadrant norm is one half of that value for these integer sine polynomials. Both normalizations must be reported explicitly. Bounds on norms use rational coefficient squares and Arb enclosures of pi and square root. The result says nothing about convergence of the stationary series, global smoothness of a resulting formal profile, a small finite-radius residual, or nonlinear closure.

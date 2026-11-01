# A derivative obstruction at the highest-mode radius

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

## Statement

Fix delta in (0,1), a nonzero finite real leading sine polynomial with largest odd frequency L and nonzero coefficient alpha there, and the canonical polynomial-log recurrence. Write B=L+1, d=delta/(1-delta), eta=B-delta, and

    a=2/eta, b=2(B-1)/eta, nu=1/b,
    R_H=4d[a Beta(a,b)]^(1/a),
    r_*= (|alpha|/R_H)^(1/delta).

Let F_n(t,theta) and G_n(t,theta) be the density and stream polynomials in t=log r. Their radial factors are r^(1-n delta) and r^(2-n delta), respectively. Topic38 identifies the top coefficients, independently of t, as

    A_n=(-1)^(n-1) alpha^n h_n,
    T_n=-A_n/[2(eta n+2)],

at angular frequencies Bn-1 and Bn. Assume the conclusion of topic115,

    h_n R_H^n ~ kappa n^(-1-nu), kappa>0, 1/2<nu<1.    (1)

At the critical radius r=r_*:

1. The density series is not absolutely summable in the C^1 angular norm. Its twice-angularly-differentiated terms do not tend to zero in C^0, so the series of these derivatives cannot converge uniformly in angle, even conditionally.
2. The stream series is not absolutely summable in the C^2 angular norm. Its three-times-angularly-differentiated terms do not tend to zero in C^0, so that differentiated series cannot converge uniformly in angle.

Consequently, uniform termwise convergence of two angular density derivatives on a closed exterior region r>=R requires R>r_*. This is only a necessary condition. Convergence at any larger radius is not proved by this result.

For the angular Wiener norm with strip sigma>=0, replace r_* by

    r_(sigma)=(|alpha| exp(B sigma)/R_H)^(1/delta).

At this radius the analogous assertions hold in that Wiener norm: absolute summability fails after one density or two stream angular derivatives, and termwise norm convergence fails after two density or three stream angular derivatives. Here absolute summability means the sum of the individual term norms is finite.

## Proof

For a real continuous periodic function U, its sine or cosine coefficient of positive frequency m is a bounded functional:

    |coefficient_m(U)|
       <= (1/pi) integral_0^(2pi) |U(theta)| |sin(m theta)| dtheta
       <= (4/pi) ||U||_infinity,

with the same estimate for cosine. Angular differentiation of a sine term multiplies the magnitude of its coefficient by m at each step and alternates sine and cosine. It does not mix frequencies. Thus for every nonnegative integer k,

    ||partial_theta^k [r_*^(1-n delta) F_n(log r_*,theta)]||_infinity
       >= (pi/4) r_* (Bn-1)^k h_n R_H^n,               (2)

because r_*^(-delta)|alpha|=R_H. By (1), the right side is a positive constant times n^(k-1-nu), asymptotically. For k=1 its sum diverges, since nu<1. For k=2 the individual lower bound tends to infinity, since 1-nu>0. The first density assertion follows from divergence of the sum of norms; the second follows from the necessary condition that the terms of a convergent Banach-space series tend to zero.

For the stream, the same argument gives

    ||partial_theta^k [r_*^(2-n delta) G_n(log r_*,theta)]||_infinity
       >= (pi/8) r_*^2 (Bn)^k h_n R_H^n/(eta n+2).     (3)

Its asymptotic power is n^(k-2-nu). Therefore k=2 gives a divergent sum of norms, and k=3 gives terms whose norms tend to infinity. This proves the stream assertions.

If R<r_*, even the undifferentiated density terms fail to tend to zero in C^0 at some r in [R,r_*), by the exponential factor (|alpha| r^(-delta)/R_H)^n and (1). If R=r_*, equation (2) rules out uniform convergence of the second derivative series at the endpoint. This proves the strict necessary inequality R>r_*.

For a real sine or cosine coefficient of magnitude A at frequency m, the angular Wiener norm sum_k |U_hat(k)| exp(sigma |k|) is at least |A| exp(sigma m). The top density frequency contributes exp(sigma(Bn-1)), and the top stream frequency contributes exp(sigma Bn). At r=r_(sigma), their exponential factors cancel |alpha|^n r^(-n delta) R_H^(-n). The extra density factor exp(-sigma) is independent of n. The same powers of n and the same two convergence tests prove the final assertion.

## Scope

The proof uses one coefficient of each term, whose log independence prevents cancellation by other log powers at the same frequency. It never assumes a sign for the full angular function. Divergence of the sum of derivative norms does not exclude conditional convergence of the first derivative series. Failure of uniform convergence of the second derivative series does not by itself exclude differentiability of a sum obtained by another method. No existence, global extension, or full-radius equality is claimed.

The result applies also to a pure recurrence when it exists at every order. It relies on the constant-factor highest-mode estimate in topic115, not merely its earlier limsup radius statement. There are no new numerical constants to certify.

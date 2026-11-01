# A smaller Gevrey upper bound for separated high harmonics

Status: CONFIRMED after the theory part's independent 05:54Z review and verifier recheck at 2026-10-31T05:56:21Z. This combines the confirmed degree bound of topic69 with a new superadditivity check. It does not prove convergence or divergence.

## Exact statement

Let Q>=3 be odd, delta=2/Q, c=Q/(Q-2), and f_1 a nonzero finite real S1 sine polynomial. Suppose all its nonzero frequencies are odd multiples of an odd M>Q. Let L be its largest frequency, F=||f_1||_A0, and use the canonical polynomial-log recurrence with every resonant stream constant zero. Put

    Kstar=floor((Q(L+1)+2)/4)+1,  A=Kstar+3,
    B(k)=max(0,k-ceil((k+3)/A)),
    D_n=B(floor((n-1)/Q)),  E_n=B(floor(n/Q)),
    s=4Q,  C=56Q(L+1)/(c-1),  sigma=(1-1/A)/Q.

For H(t,theta)=sum_q t^q H_q(theta), define

    ||H||_!,s=sum_q q! s^q ||H_q||_A0.

Then the entire generated sequence satisfies

    ||F_n||_!,s <= D_n! F(8CF)^(n-1)/n,
    ||G_n||_!,s <= 4Q D_n! F(8CF)^(n-1)/n.                (1)

In particular D_n! <= (n!)^sigma, so these are Gevrey upper bounds of order sigma<1/Q. For Q3 and f_1=sin(5theta), A9, sigma8/27, C504 and8CF4032. For Q3 and f_1=sin(9theta), A12 and sigma11/36. No optimality is asserted.

## 1. The needed degree inequalities

Topic69 proves deg_t F_n<=D_n and deg_t G_n<=E_n using the exact vanishing of the high-frequency transfer. To use those bounds in an absolute majorant, their compatibility with products must be proved separately.

Write alpha=1-1/A. The equivalent formula is

    B(k)=max(0,floor(alpha k-3/A)).                         (2)

Thus B is nondecreasing on nonnegative integers. It is also superadditive:

    B(u)+B(v)<=B(u+v),  u,v>=0.                            (3)

If one of the two terms on the left is zero, monotonicity proves this. If both are positive, their sum is at most floor(alpha(u+v)-6/A), which is no larger than floor(alpha(u+v)-3/A), and the latter is positive. This proves (3) in all cases.

For i+j=n, the floor inequality and (3) give

    E_i+D_j
      =B(floor(i/Q))+B(floor((j-1)/Q))
      <=B(floor((n-1)/Q))=D_n.                            (4)

Also E_n>=D_n. These are exactly the inequalities needed below. This argument does not assume that every resonant inverse raises the improved bound by one. Its input is the already proved degree theorem for the actual sequence.

## 2. Uniform inverse estimates

The factorial polynomial norm satisfies

    ||partial_t H||_!,s<=s^-1||H||_!,s,
    ||integral_0^t H||_!,s=s||H||_!,s.

The parameter has reduced denominator Q because Q is odd. Every nonzero scalar Poisson shift is at least1/Q in absolute value. Consequently the finite polynomial inverse of partial_t+v has norm at most1/(|v|-1/s)<=4Q/3. The two Fourier channels, including subtraction of the nonresonant channel's constant at a resonant output to enforce the canonical gauge, give

    ||G_n||_!,s<=4Q||F_n||_!,s.                            (5)

These are the established operator estimates in topic17, independent of the polynomial degree. The density inverse of lambda_n-c partial_t, lambda_n=(n-1)(c-1), has norm at most2/lambda_n for n>=2. Indeed c/(s lambda_n)=1/[8(n-1)]<=1/8.

For polynomials U,V of degrees at most e,d, the factorial norm obeys

    ||UV||_!,s<=binom(e+d,e)||U||_!,s||V||_!,s.             (6)

Each coefficient product of degrees u,v is multiplied by binom(u+v,u), which is nondecreasing in each input degree, proving (6).

## 3. The scalar majorant

Define u_n=||F_n||_!,s/D_n! and v_n=||G_n||_!,s/E_n!. Since E_n>=D_n, equation(5) gives v_n<=4Q u_n. For a stream-density product at orders i,j, equations(4) and(6) show

    binom(E_i+D_j,E_i) E_i! D_j! <= D_n!.

Thus the normalized product has no binomial loss. Angular differentiation costs at most(L+1)i or(L+1)j, since the respective Fourier supports are bounded by(L+1)i and(L+1)j. In

    sum_(i+j=n) [(P_i+partial_t)G_i partial_theta F_j
                     -partial_theta G_i(p_j+partial_t)F_j],

use the bounds4i and3j for the radial-exponent operators. Combining these, the density inverse bound and(5) gives

    u_n <= C/(n-1) sum_(i+j=n) ij u_i u_j,
    C=56Q(L+1)/(c-1).                                     (7)

Set x_n=n u_n. Since n/(n-1)<=2, x_1=F and

    x_n<=2C sum_(i+j=n)x_i x_j.

Induction against the Catalan recursion yields x_n<=F(8CF)^(n-1), because the Catalan number with index n-1 is at most4^(n-1). This proves the first bound in(1). The second follows directly from(5), retaining D_n! rather than the larger E_n!.

## 4. The Gevrey exponent

Equation(2) gives D_n<=sigma n. For integers1<=d<=n, the geometric mean of the first d positive integers is at most that of the first n. Equivalently log(d!)/d<=log(n!)/n. Therefore

    D_n! <= (n!)^(D_n/n) <= (n!)^sigma.

If D_n=0 the same conclusion is immediate. This proves the claimed strictly smaller Gevrey upper order. A fixed angular-strip weight costs at most exp((L+1)n times the strip width), and each fixed derivative costs at most a power of n, so these changes only enlarge the geometric constant. This last observation concerns formal coefficient estimates, not convergence of the generalized series.

## Dependencies and scope

The log recurrence and operator estimates are in topics10 and17. The exact high-harmonic degree theorem is topic69, itself based on topics67 and68. Superadditivity(3), rather than cancellation alone, makes the improved coefficient bound possible. The estimate still permits factorial growth of positive order, so the full rational-log convergence question remains OPEN.

The verification checks the integer inequalities independently and the norm bound against the exact full Cartesian recursions through42 for sin5 and sin9. Source snapshots and exact results are retained alongside this proof.

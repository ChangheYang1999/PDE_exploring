# An exact positive rational enclosure of Catalan's constant

## Statement

Define G=integral_0^1 arctan(t)/t dt. Set b_0=h_0=1 and, for k>=0,

    b_(k+1)=b_k(2k+2)/(2k+3),
    h_(k+1)=h_k+1/(2k+3),
    S_N=sum_(k=0)^(N-1) b_k h_k/2^(k+1).

For every integer N>=1 these are rational numbers and

    S_N < G < S_N+2^(-N).                                 (1)

The enclosure is used only to evaluate the explicit coefficient in ../PROOF.md. It is not an operator-norm assertion.

## Proof

Integration by parts gives

    G=-integral_0^1 log(t)/(1+t^2) dt.

The boundary terms arctan(t)log(t) vanish at0 and1. For0<=t<=1, expand

    1/(1+t^2)=(1/2)sum_(k>=0)[(1-t^2)/2]^k.

All terms are nonnegative, so monotone convergence gives

    G=sum_(k>=0) A_k/2^(k+1),
    A_k=integral_0^1 (-log t)(1-t^2)^k dt.

To identify A_k, for a>-1 integrate by parts repeatedly in

    F_k(a)=integral_0^1 t^a(1-t^2)^k dt.

The result is

    F_k(a)=(2*4*...*2k)/[(a+1)(a+3)...(a+2k+1)],

with numerator1 when k=0. Differentiation under the integral is justified on any compact a-interval in(-1,infinity), since t^a|log t| is integrable. Thus

    A_k=-F_k'(0)=F_k(0)sum_(j=0)^k1/(2j+1)=b_k h_k.

This proves the recurrence representation. Also0<A_k<=integral_0^1(-log t)dt=1, with strict inequality for k>=1. The omitted tail is positive and smaller than sum_(k=N)^infinity 2^(-k-1)=2^(-N). This proves(1).

## Verification protocol

Use N=512 with exact Fraction arithmetic. Independently compare its rational enclosure with a high-precision special-function evaluation, while using the exact interval itself in the directed certificate. All numerical source files and outputs must be hashed. No floating-point truncation estimate is used.

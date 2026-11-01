# Exact minimization of the leading polar velocity norm

Status: CONFIRMED by V068 after independent review in the theory part's Proposition8.4 and exact finite checks. This minimizes a specified leading-velocity norm, not the growth rate of the full stationary recursion.

## Statement

Fix 0<gamma<1 and put P=1+gamma. For real S1 leading profiles

    f(theta)=sum_(k>=0) a_k sin((2k+1)theta),  a_0=1,

let g=sum_(j>=1) b_j sin(2j theta) be the uniquely determined leading stream coefficient. Define the combined weighted Wiener norm of its radial and tangential velocity coefficients by

    V_sigma(f)=||g'||_(A_sigma)+P||g||_(A_sigma)
              =sum_(j>=1) (2j+P) exp(2j sigma)|b_j|.

The first equality uses that the polar velocity coefficients are -g' and Pg. It is not an identity for a Cartesian vector norm.

Set A_0=1 and

    A_k=product_(l=1)^k (2l-P)/(2l+P).

These are the positive coefficients of the cancellation family in topic51.

1. Among profiles of degree at most2K+1 with a_0=1, the minimum of V_sigma for sigma>=0 is

    min_(1<=j<=K+1) W_j,    W_j=(A_(j-1)/2) exp(2j sigma).

Every minimizing profile is a convex combination of the cancellation profiles truncated just before one of the minimizing stream indices j. If the minimizing index is unique, the profile is unique.

2. At sigma=0, W_j strictly decreases. The unique minimizer at degree at most2K+1 is therefore precisely the topic51 profile truncated at K, and its minimum norm is A_K/2.

3. For sigma>0, the same formula with j ranging over all positive integers gives the minimum over all real S1 profiles in A_sigma with a_0=1. The minimum is attained by a finite polynomial. Write

    J=(P/2)coth(sigma).

If J is not an integer, the unique minimizing index is max(1,ceil(J)); if J is an integer m>=1, the two minimizing indices are m and m+1. Under a finite bandwidth cutoff, restrict the same sequence to1<=j<=K+1. The full minimizing set is the corresponding segment of convex combinations when there is a tie.

4. In the class of analytic real S1 profiles with a_0=1 and no fixed bandwidth, inf V_0=0 but this infimum is not attained. The same remains true with the additional unweighted input-norm bound ||f||_(A_0)<=(1+gamma)/(2gamma), because every cancellation truncation satisfies that bound.

## 1. The telescoping constraint

The exact leading Poisson inverse is

    b_j=-a_(j-1)/(2(2j+P))+a_j/(2(2j-P)).

Since 1<P<2, all denominators and A_k are positive. Put s_k=a_k/A_k. Using A_j/A_(j-1)=(2j-P)/(2j+P) gives

    2(2j+P)b_j/A_(j-1)=s_j-s_(j-1).                 (1)

For bandwidth K, set a_k=0 for k>K and sum (1) through K+1. Since s_0=1 and s_(K+1)=0,

    sum_(j=1)^(K+1) c_j b_j=-1,
    c_j=2(2j+P)/A_(j-1)>0.                         (2)

Conversely every finite stream vector satisfying (2) reconstructs such a leading profile by the cumulative sums s_k=1+sum_(j<=k)c_j b_j. Thus no extra linear constraint is omitted.

For an analytic input the same identity holds after summing to infinity. To justify the endpoint, A_k decays only polynomially. Indeed log(A_k)=sum_l log(1-2P/(2l+P))=-P log(k)+O_gamma(1): remove finitely many small l, use log(1-x)=-x+O(x^2), and sum the square-summable remainder. Therefore a_k/A_k tends to zero for exponentially decaying a_k. Also sum |c_j b_j| is finite for analytic input, since c_j grows polynomially and b_j decays exponentially. Thus (2) holds with an infinite sum.

## 2. Lower bound and equality

Let w_j=(2j+P)exp(2j sigma), so w_j/c_j=W_j. For any admissible profile,

    V_sigma=sum_j w_j|b_j|
            >=(inf_j W_j) sum_j c_j|b_j|
            >=(inf_j W_j)|sum_j c_j b_j|
            =inf_j W_j.                           (3)

When the infimum is positive and attained, equality holds precisely when every nonzero b_j has W_j equal to that minimum and every c_j b_j is nonpositive. Equation (2) then writes -c_j b_j as nonnegative weights summing to1. A single weight at j gives b_j=-1/c_j and all other stream coefficients zero; equation (1) reconstructs a_k=A_k for k<j and a_k=0 for k>=j. These are exactly the cancellation truncations. Taking convex combinations establishes the complete equality classification.

For sigma=0 and finite K, A_j is strictly decreasing because0<(2j-P)/(2j+P)<1. Hence the sole minimizing stream index is K+1 and the minimum is A_K/2.

## 3. Positive strip widths and the unweighted limit

For sigma>0, polynomial decay of A_k shows W_j tends to infinity. Furthermore

    W_(j+1)/W_j=exp(2sigma)(2j-P)/(2j+P).

This ratio is strictly increasing in j and equals1 precisely when j=(P/2)coth(sigma). Hence the sequence first decreases and then increases, with a two-point minimum exactly at an integer threshold. This proves the claimed index formula, including the finite cutoff. The minimizing finite profiles belong to every analytic strip, so the lower bound is attained in the stated class.

At sigma=0, the finite truncations give V_0=A_K/2 tending to zero. No analytic profile with a_0=1 can have V_0=0: zero norm would imply b_j=0 for every j, and (1) would force a_k=A_k for all k. These coefficients have polynomial, not exponential, decay and cannot define an analytic profile. Equivalently they represent the nonsmooth shear from topic51. That topic's input-norm bound proves the final bounded-input assertion.

## Scope

This variational statement concerns only the linear leading Poisson map and the explicitly defined norm. It does not show that these inputs minimize ||f_2||, the asymptotic growth of f_n, or the actual exterior radius. A positive strip width penalizes high angular frequencies and changes the minimizing cutoff. The unweighted infimum demonstrates a loss of regularity at the boundary of the analytic class, not a smooth zero-velocity stationary solution.

## Exact finite verification and Candidate007 comparison

The independent Cartesian Poisson inverse passes206 exact rational checks: arbitrary profiles obey the telescoping constraint and norm lower bound; every predicted minimizing truncation attains the bound; all tested tie combinations attain it; the threshold formula gives every minimizing index. The tests cover four gamma values, five bandwidths and five exact values of exp(2sigma), including a tie. Actual computation0.0798002309165895 seconds.

At the stored Candidate007 parameter, normalize its first sine amplitude to1. Direct reconstruction reproduces every leading stream coefficient from the authoritative potential extraction. The first stream amplitude is approximately-0.0139738238112, versus-0.140750360536 for sin(theta), a ratio0.099280909534. The full combined unweighted polar velocity norm is0.090936614933, versus1/2 for sin(theta), a ratio0.181873229866. Thus the approximately tenfold reduction is specific to the first stream harmonic; the combined norm decreases by about5.5. These displayed numbers are approximations to exact rationals retained in verification/checks.json.

The Wiener distance from the normalized Candidate007 input to the normalized infinite shear profile is exactly the sum of the ten absolute coefficient differences plus the positive shear tail. It is approximately0.253641714906; the shear Wiener norm is1.40515960510. This also bounds the uniform angular distance from above, but does not measure derivative closeness. The minimum velocity norm among degree-at-most19 inputs is approximately0.00344871580948, so Candidate007's norm is about26.37 times that minimum. Its second density norm is approximately0.0417098817658. None of these quantities is an infinite-order growth constant.

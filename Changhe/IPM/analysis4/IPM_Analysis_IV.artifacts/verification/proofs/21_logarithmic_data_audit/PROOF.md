# Independent Cartesian audit of finite logarithmic coefficient data

Status: CONFIRMED through order 73. This topic concerns finite exact coefficients, not convergence of the infinite generalized series.

## Statement to be checked

For the input `f_1=sin(theta)`, `delta=4/9`, `c=9/5`, the retained theory-part exact logarithmic coefficients with every free resonant stream constant set to zero are claimed to satisfy the stationary density equation and Poisson equation through their last completed order. The independent checker below uses Cartesian differentiation of signed Laurent polynomials, not the angular nonlinear recurrence used by the generator.

## Exact representation and differential operators

Put `t=log r` and `w=exp(i theta)`. For a real sine field write

\[
 \rho=-i r^p A(t,w),\qquad \psi=-i r^P B(t,w),
\]

where `A=i f` and `B=i g` have real rational Laurent coefficients. In particular, a sine amplitude `a_m(t)` gives coefficients `a_m(t)/2` at frequency `m` and `-a_m(t)/2` at frequency `-m` in `A`.

For a real Laurent coefficient field `H=sum_k h_k(t)w^k` of radial exponent `q`, define real coefficient operators

\[
 X_q H=\frac12\sum_k\left[((q-k)h_k+h_k')w^{k+1}
                              +((q+k)h_k+h_k')w^{k-1}\right],
\]

\[
 Y_q H=\frac12\sum_k\left[((k-q)h_k-h_k')w^{k+1}
                              +((q+k)h_k+h_k')w^{k-1}\right].
\tag{1}
\]

The output radial exponent is `q-1`. These identities are direct differentiation of `r^q exp(ik theta) (log r)^s`: Cartesian `partial_x` acts as `X`, and `partial_y` acts as `iY`. Consequently

\[
 \rho_x=-i X A,\quad \rho_y=Y A,\quad
 u_x=-Y B,\quad u_y=-i X B.
\]

Here `u_x,u_y` denote velocity components, not derivatives. Thus the coefficient of `i u dot grad rho` is

\[
 (X B)(Y A)-(Y B)(X A).
\tag{2}
\]

At order `n`, the exact stationary residual to be tested is therefore

\[
 (cp_n-1)A_n+c\partial_t A_n
 +\sum_{i+j=n}\big[(X B_i)(Y A_j)-(Y B_i)(X A_j)\big].
\tag{3}
\]

The Poisson residual `i(-Delta psi-partial_x rho)` is

\[
 -X X B_n+Y Y B_n-X A_n.
\tag{4}
\]

Every composed derivative uses the reduced radial exponent from the first derivative. Equations (3) and (4) must be identically zero as finite polynomials in `t` and Laurent polynomials in `w`.

## Implementation and proof interpretation

A Laurent polynomial with minimum possible frequency `-M` is stored as `w^-M` times an ordinary rational polynomial. Each log degree is a separate polynomial. Addition aligns the shifts; multiplication uses exact rational polynomial multiplication. Formula (1) is implemented using the polynomial coefficient multiplier `k` and shifts by one frequency. It does not call the theory part's generator or its angular convolution routine.

The checker validates the leading datum and the zero-constant convention at each resonant angular mode. It then checks (3) and (4) at every reported completed order. Since these are exact rational operations, zero residuals certify the stated finite identities. The all-order formal solvability theorem remains the separate result of topic 10, and the factorial-norm bound remains topic 17. No finite collection of these checks proves infinite convergence.

Input hashes, source snapshots, completed orders, and actual elapsed time are retained in `verification`. No Lean or other proof-assistant build is used.

## Completed check

Every stationary and Poisson residual through order 73 is exactly zero. At order 73 both density and stream have log degree eight. The actual checker elapsed time is 160.712384 seconds, excluding no claimed extra computation. The input snapshot hash is `541f039588a6aa949d0019507a0b17498ef9b82d340189c4750a3be041847961`; the complete order-by-order evidence is `verification/cartesian_check.json`. This check does not reconstruct the potential at these higher orders; formal potential reconstruction is proved independently in topic 10.

## Independent comparison with the numerical ball checkpoint

The separately generated Arb checkpoint was compared with the already verified exact data through order 73. Every stored midpoint and radius was parsed as an exact dyadic rational. For a stored interval with midpoint `m`, radius `e`, and independently verified exact coefficient `q`, the check was the exact inequality `abs(q-m)<=e`. Thus the comparison does not depend on decimal rounding or a float tolerance.

All 10,081 density and 10,486 stream entries passed, including entries whose exact value is zero. The retained checkpoint prefix is in `sources/numerics_log_prefix73.pkl`; source hashes, arithmetic, counts, and norm summaries are in `verification/numerics_ball_containment.json`. The actual comparison took 1.676207 seconds. Both implementations enforce the total resonant coefficient `B_(n,j)(0)=0`. This is distinct from setting only the integration constant of one factored inverse to zero.

For example, at order 73 the density's plain coefficient-sum root is approximately `0.426707362596578245`, and its factorial-weighted root at weight `s=36` is approximately `0.42685281619751983`. These values describe the finite verified prefix and are not asymptotic growth limits.

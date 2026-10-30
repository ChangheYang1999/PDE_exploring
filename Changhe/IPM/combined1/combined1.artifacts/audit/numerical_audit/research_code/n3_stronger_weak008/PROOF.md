# Independent first-sine distance tests for candidate008

## Statement and hypotheses

Let rho and u be the exact candidate C1-N1-008-d2w-j7-x3bal reference,
with c=4076476460239181/2251799813685248, canonical divergence-free
velocity and residual F=(cX+u).grad rho-rho. The immutable raw candidate
hash and the independently verified canonical representation are inputs.
Assume the S1-symmetric real correction h belongs to L2(R2), the
stationary equation holds in distributions at this same c, its products
are locally integrable, and its velocity is u+U[h], where U[h] is
canonical, divergence-free and ||U[h]||2<=||h||2.

For K=512 and2048 let t=r^2/(1+r^2), v=1/(1+r^2), and
phi=y t^K v^2. Define

    I=integral F phi,
    A=||(2c+1)phi+cX.grad phi||2,
    B=||t^K v^2 [1+2K v+4t] u||2,
    C=||r t^K v^2 grad rho||2,
    H=S(K,2)+2K S(K,3)+4S(K+1,2),
    S(a,b)=a^a b^b/(a+b)^(a+b).

All norms are on the whole plane, with both vector components. Then

    |I| <= (A+B+C)||h||2 + H||h||2^2.                 (1)

Consequently certified containing intervals and a strictly downward
rational rounding of

    2|I|/[A+B+C+sqrt((A+B+C)^2+4H|I|)]              (2)

prove a necessary lower distance. This calculation aims to independently
reproduce N3's stronger008 first-sine bounds. It does not assert that
(2) is the actual distance, or optimize over all probes.

## Proof of the envelope inequality

Differentiate phi=y t^K v^2. The Euclidean triangle inequality and
|y|<=r give

    |grad phi| <= t^K v^2+2K t^K v^3+4t^(K+1)v^2.

The exact maximum of t^a(1-t)^b on[0,1] is S(a,b), by differentiation,
so H bounds the full gradient. Moreover

    ||u.grad phi||2 <= B,  ||phi grad rho||2 <= C.

Testing the stationary correction equation against phi and integrating
by parts gives the full weak estimate in
../scaled_factored_weak/PROOF.md. Splitting its full transport norm by
the triangle inequality yields(1). The probe is smooth and decays as
r^-3; the reference grows at most r^(1/c), with1/c<1. These facts and
L2 convergence of correction tails justify the same cutoff limits.
Solving the nonnegative quadratic yields(2).

## Independent integration and comparison

The own polynomial Cartesian engine reconstructs rho, both components
of u, and both components of grad rho from the verified canonical
potential. The first-sine residual projection includes every compatible
angular product. With F_1=r sum v^(ell delta/2)P_ell(t), delta=1-1/c,

    I=(pi/2) sum integral_0^1
                     v^(ell delta/2-1) t^(K+1) P_ell(t) dt.

Both the t- and v-polynomial forms are integrated with outward Beta
moments at2048 bits and must overlap. A^2 is also evaluated by its exact
finite rational Beta identity. For B and C, angular orthogonality is
performed exactly over all background modes and all radial cross terms
are retained. Their remaining v-polynomials multiply the scalar
factor t^(2K+1) and are integrated by the same complete moments. There
is no spatial cutoff or numerical angular quadrature.

The exact gradient cap H uses rational arithmetic. Each output binds
the frozen N3 record, its source identity, the own canonical source,
all own implementation hashes and this proof. N3's one-sided stored
bounds are compared using outward endpoints of their printed Arb balls;
we do not treat their nearest decimal centers as directed endpoints.
The independent distance is then rounded strictly down to a rational.
N3 code is inspected as data and is not imported or executed.

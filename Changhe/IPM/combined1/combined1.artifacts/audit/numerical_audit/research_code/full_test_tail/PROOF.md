# Uniform tail ceiling for the complete first-mode weak test

## Statement, source and hypotheses

The reference is the exact C1-N1-007-d2w-j7-e2bal density rho and its
canonical velocity u. Its source and complete first-sine residual
projection are bound in ../uniform_first_mode_tail/verification/result.json.
All displayed coefficient arrays there are exact rationals. Fix

    c=4076476460239181/2251799813685248,
    delta=1-1/c, t=r^2/(1+r^2), v=1-t.

The fields are smooth on R2, div u=0, u=O(r^(1/c)) at infinity, and
F=(cX+u).grad rho-rho belongs to L2(R2). For integer K>=0 set

    phi_K=r v^2 t^K sin(theta),
    I_K=int_R2 F phi_K,
    M_K=(2c+1)phi_K+(cX+u).grad phi_K.

Let D_K and H_K be finite real numbers with
D_K>=||M_K||2 and H_K>=0. In particular this allows the complete
weak denominator ||M_K||2+||phi_K grad rho||2 and any larger certified
upper denominator. Define the nonnegative test value

    m_K=2|I_K|/[D_K+sqrt(D_K^2+4H_K|I_K|)].                 (1)

This definition also covers I_K=0, when m_K=0. The denominator is
positive by the coercive identity proved below.

The complete first-sine projection is the finite expression

    Pi_1 F=r sum_(ell,j) q_(ell,j) v^(beta_(ell,j)) sin(theta),
    beta_(ell,j)=ell delta/2+j,

obtained by writing the exact branch polynomials at the v endpoint.
Terms with zero coefficient are omitted. The verified source has every
beta>4/3 and exact minimum
7725829753347047/4076476460239181. Define

    U(K0)=sqrt(pi/2)/(c+1) (2K0+3)
                     sum_(ell,j) |q_(ell,j)| B(beta_(ell,j),K0+2), (2)

where B(a,b)=int_0^1 v^(a-1)(1-v)^(b-1)dv. Then for every integer
K>=K0>=0,

    m_K <= U(K0).                                         (3)

Consequently the strict exact upper bounds already evaluated for (2)
give, simultaneously for every integer in the indicated ranges,

    K>=10^8:  m_K < 11903724456153/125000000000000000,
    K>=10^9:  m_K < 9906231301769/10^18,
    K>=10^10: m_K < 1088602745643/10^18.

Their numerical acceptance remains conditional on independent review of
the finite coefficient reconstruction and outward Beta calculation in
N4-222. This theorem extends that calculation to the full M+C weak test;
it does not assert D_K>=the norm of the drift-only field.

## Coercive identity including the full velocity

The function phi_K is y times a rational smooth radial function, so it is
smooth at the origin. At infinity phi_K=O(r^-3) and grad phi_K=O(r^-4).
The growth hypothesis on u implies M_K belongs to L2. Integration by
parts on a disk with its center removed, followed by the two radial
limits, gives

    int phi_K cX.grad phi_K=-c ||phi_K||2^2,
    int phi_K u.grad phi_K=0.

The second identity follows from div u=0 and
phi_K u.grad phi_K=(1/2)div(u phi_K^2). Its outer boundary term is
O(R^(1+1/c-6)), which tends to zero; the inner boundary term tends
to zero by smoothness. The first identity follows in the same way from
div(cX)=2c. Therefore

    <phi_K,M_K>=(c+1)||phi_K||2^2.

Cauchy-Schwarz proves

    ||M_K||2 >= (c+1)||phi_K||2 > 0.                       (4)

No smallness or pointwise sign of the background transport is used.
This is why the drift-only denominator restriction in N4-222 is
unnecessary for the complete test (1).

## Exact finite numerator and monotonicity

Angular orthogonality and r dr=-dv/(2v^2) give

    I_K=(pi/2) sum q_(ell,j) B(beta_(ell,j),K+2),
    ||phi_K||2^2=pi/[2(2K+2)(2K+3)].

No non-first angular mode contributes to this scalar pairing. The
complete projected field, including all nonlinear interactions, is
already bound by the independent source audit N4-209/221. Apply the
triangle inequality only after that complete exact projection.
Using (4), sqrt(D_K^2+4H_K|I_K|)>=D_K, and
sqrt((2K+2)(2K+3))<2K+3 yields

    m_K <= |I_K|/D_K
         <= |I_K|/[(c+1)||phi_K||2]
         <= sqrt(pi/2)/(c+1) (2K+3)
                               sum |q_(ell,j)| B(beta_(ell,j),K+2).

For a fixed beta, the ratio of the last positive summand at K+1 and K is

    (2K+5)/(2K+3) * (K+2)/(K+beta+2).

It is strictly below1 whenever beta>1+1/(2K+3). Our exact beta>4/3
condition ensures this for every integer K>=0. Each summand decreases,
so their finite sum at K is at most its value at K0. This proves (3).
It does not extend a sampled finite model to an infinite series: the
coefficient sum is a complete finite v-endpoint representation.

## Relation to necessary solution distances and scope

Under the separate weak-distributional stationary equation, canonical
velocity, L2 contraction and cutoff hypotheses in
../successor_factored_weak/PROOF.md (with the present reference), every
solution correction h satisfies ||h||2>=m_K when the full M+C denominator
and a gradient upper bound are used. The estimate (3) is an upper bound
on these necessary test values. It is not an upper bound on ||h||2 and
provides no correction, solution, inverse or global maximizing index.

The finite calculations below K0 remain separate. Neither a sampled
maximum nor a family-wide residual floor follows. Other angular test
families require their own complete projection and coefficient check.
An all-c comparison of solution classes uses the separately audited
common-leading-tail theorem, not the present test ceiling.

## Dependencies and verification evidence

The only new step is the full-velocity coercive identity (4). All exact
coefficient arrays, six outward U(K0) intervals and strict rational
upper bounds are retained in the N4-222 topic. The local manifest binds
that proof, result, code and the independently confirmed complete
projection acceptance N4-221. It also binds this standalone proof.
No numerical source is changed and no new numerical computation is
needed. Independent analytic and numerical review are OPEN until
explicitly recorded in verdict ledger.

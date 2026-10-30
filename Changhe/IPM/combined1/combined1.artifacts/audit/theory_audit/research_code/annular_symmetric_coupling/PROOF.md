# Localized symmetric coupling cost on an exterior annulus

Status: new T4 result, OPEN pending independent Opus review. This addresses the local-version question in T2's review of T4-163. It is an operator estimate, not an existence theorem or a candidate certificate.

## Statement

Use canonical U[h]=(-R1 R2 h,R1^2 h), Rj=partial_j(-Delta)^(-1/2), on L2(R2), and Qh=v.U[h]. Assume v is a real C1 vector field and, for some 0<delta<1 and G,H>=0,

    |v(X)| <= G <X>^(-delta),
    ||Dv(X)||_op <= H <X>^(-delta-1).                      (1)

Here <X>=(1+|X|^2)^(1/2). Let R>=1 and Lambda>1. Let psi be nonnegative, globally Lipschitz and supported in R<=|X|<=Lambda R. Define

    Psi=||psi||_infinity, A=||grad psi||_2,
    B=||psi||_2, Lstar=R Lip(psi),
    D_delta=1+2^delta sqrt((2-delta)/(1-delta)),
    N=cosh(Psi) A [2^delta G Lstar+2^(delta+1) H]/(8 sqrt(pi)),
    T=exp(Psi) G (B/R) D_delta/sqrt(2pi).                  (2)

Then the self-adjoint operator

    E=Sym(exp(psi) Q exp(-psi))-Sym Q

is Hilbert-Schmidt and

    ||E||_op <= ||E||_HS <= R^(-delta) sqrt(N^2+T^2).      (3)

The result also holds on S1 by restriction when Q and psi preserve that space. If psi has both signs but is zero off the annulus, replace T by sqrt(2)T and Psi by osc(psi) wherever it occurs inside exp or cosh; retain B=||psi||_2 and the same near constant. The nonnegative form is enough for the orbit weights under discussion.

A convenient scale specialization is psi_R(X)=epsilon phi(X/R), where epsilon>=0 and phi is fixed, nonnegative, Lipschitz and supported in 1<=|X|<=Lambda. Then

    A=epsilon ||grad phi||_2,
    B/R=epsilon ||phi||_2,
    Lstar=epsilon Lip(phi), Psi=epsilon ||phi||_infinity. (4)

For 0<=epsilon<=1, (3) has the uniform form

    ||E||_HS <= C_phi,G,H,delta epsilon R^(-delta),        (5)

with C obtained explicitly from (2) by replacing epsilon by1 inside N/epsilon and T/epsilon. If epsilon=R^(-delta), the right side is C R^(-2delta). In contrast, the global coarse estimate G_global(exp(Psi)-1) is generally only O(R^(-delta)) for these weights.

## Proof

All integrals below are over the whole plane. The canonical off-diagonal velocity kernel is

    K(z)=(-2z1z2,z1^2-z2^2)/(2pi |z|^4),
    |K(z)|=1/(2pi |z|^2).

The local term (0,-h/2) in U gives multiplication by -v2/2 in Q. It commutes with exp(psi), so cancels exactly in E. Put d=psi(x)-psi(y). Its remaining kernel is

    e(x,y)=K(x-y).[(cosh(d)-1)(v(x)+v(y))
                           +sinh(d)(v(x)-v(y))]/2.      (6)

This is the symmetric kernel derived in T4-163. The proof below also proves its L2 integrability, so the same truncated-kernel argument identifies it with E. In particular no first-commutator Hilbert-Schmidt assertion is used.

### Near the diagonal

Restrict first to |x-y|<R/2. If d is nonzero, at least one endpoint lies in the support of psi and hence has radius at least R. Both endpoints, and their joining segment, have radius at least R/2. It follows from (1) that

    |v(x)|,|v(y)| <= G_R=2^delta G R^(-delta),
    |v(x)-v(y)| <= H_R |x-y|,
    H_R=2^(delta+1) H R^(-delta-1).

The segment assertion uses its distance to the endpoint of radius at least R, and the fact that its entire length is less than R/2. It does not require the exterior of a disk to be convex. If d=0, the kernel is zero and no estimate on v is needed at that pair.

Taylor bounds in (6) give

    |e(x,y)| <= cosh(Psi)/(4pi |x-y|^2)
                     [G_R d^2+|d| |v(x)-v(y)|].         (7)

Translation and the fundamental theorem of calculus give

    ||psi(.+z)-psi||_2 <= A|z|,
    |psi(x+z)-psi(x)| <= Lip(psi)|z|.

Using these bounds on the disk |z|<R/2 yields

    (int int_(|x-y|<R/2) d^4/|x-y|^4 dxdy)^(1/2)
        <= A Lip(psi) sqrt(pi) R/2,
    (int int_(|x-y|<R/2) d^2 |v(x)-v(y)|^2/|x-y|^4 dxdy)^(1/2)
        <= A H_R sqrt(pi) R/2.

The second bound is valid because pairs with d nonzero have the local H_R estimate. Combining with (7) proves that the near-diagonal Hilbert-Schmidt norm is at most R^(-delta) N.

### Away from the diagonal

The alternative exact form of (6) is

    e(x,y)=K(x-y).[(exp(d)-1)v(x)+(exp(-d)-1)v(y)]/2.

Since |d|<=Psi, it implies

    |e(x,y)| <= exp(Psi)|d|(|v(x)|+|v(y)|)/(4pi |x-y|^2).

Nonnegativity of psi gives d^2<=psi(x)^2+psi(y)^2. The integrand is symmetric in x,y. Consequently

    ||e 1_(|x-y|>=R/2)||_2
       <= exp(Psi) B/(2sqrt(2)pi)
          sup_(x in supp psi) [int_(|y-x|>=R/2)
                    (|v(x)|+|v(y)|)^2/|x-y|^4 dy]^(1/2). (8)

For |x|>=R, Minkowski's inequality bounds the square root inside (8) by

    |v(x)| [int_(|z|>=R/2)|z|^-4 dz]^(1/2)
       +[int_(|y-x|>=R/2)|v(y)|^2 |y-x|^-4 dy]^(1/2).

The first term is at most 2sqrt(pi)G R^(-delta-1). For the second integral split into |y|>=R/2 and |y|<R/2. On the former set, |v(y)|<=2^delta G R^(-delta), so its contribution is at most

    4pi 2^(2delta) G^2 R^(-2delta-2).

On the latter, |x-y|>=R/2 and <y>^(-2delta)<=|y|^(-2delta) for y nonzero. Since delta<1,

    int_(|y|<R/2) |v(y)|^2 |x-y|^-4 dy
      <=16 G^2 R^-4 int_(|y|<R/2) |y|^(-2delta) dy
      =4pi 2^(2delta) G^2 R^(-2delta-2)/(1-delta).

Thus the square root in (8) is at most

    2sqrt(pi)G R^(-delta-1) D_delta.

Substitution proves the far-diagonal bound R^(-delta) T. The near and far kernels have disjoint supports, so their squared L2 norms add. This proves (3). For signed psi use d^2<=2(psi(x)^2+psi(y)^2), which adds precisely sqrt(2) to the far bound. Scaling in two dimensions proves (4), and monotonicity of the nonnegative expressions in epsilon proves (5).

## Consequence and limits

For S1 IPM references with density degree gamma=1/c in (0,1), one may use delta=1-gamma if global bounds (1) for v=grad rho are certified. The canonical rational families have the required exponents, but this proof supplies neither G nor H for any particular snapshot.

This removes one obstacle to localizing a low-energy multiplier on large annuli: the conjugation cost may use the decaying background near the annulus, including its nonlocal coupling to the origin. The origin contribution is explicitly included in the second part of the far integral. The estimate does not assert that a desired orbit weight has these support, size or Lipschitz bounds, or that the resulting weighted operator has a positive rate. Those remain separate hypotheses.

There is no high inverse, nonlinear remainder estimate, residual norm certificate or new candidate closure in this note. No finite-dimensional spectral computation is used.

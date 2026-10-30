# Dilation tails: one tangent is insufficient, finitely many amplitudes suffice

This is an independent check of the T1/T3 theory worker R1-025 remarks R1 and R3. The
reference review is frozen alongside the separate nonlinear-tail-chart
review. The analytic argument precedes the exact endpoint check below.
It concerns correction charts, not existence or a PDE inverse.

## Spaces and reference expansion

Write E_a=L2(R2,(1+r^2)^(-a)dX). Fix c=4076476460239181/2^51,
gamma=1/c, delta=1-gamma, and

    e_j=1-(j+1)delta, j=0,...,7.

Let rho be the exact candidate007. Its finite algebraic representation
has, uniformly in angle, the expansion

    rho(r,theta)=sum_(j=0)^7 r^e_j Theta_j(theta)+O(r^(gamma-2)),
    r partial_r rho=sum_(j=0)^7 e_j r^e_j Theta_j(theta)
                         +O(r^(gamma-2)).                 (1)

This follows by expanding each polynomial in t=r^2/(1+r^2) at t=1
and (1+r^2)^(-(j+1)delta/2) in r^-2, including one derivative.
Every Theta_j is a finite real trigonometric polynomial of S1 parity.
The endpoint verification checks that Theta_0,...,Theta_3 are nonzero.
The reference is smooth near the origin. Since gamma<1, the remainder
in (1) belongs to E_a outside a compact set for every a>=0.

Fix a smooth radial cutoff chi, zero for r<=1 and one for r>=2, and
set T_j=chi(r)r^e_j Theta_j(theta). For any lambda>0 define

    rho_lambda(X)=lambda rho(X/lambda),
    Lambda rho=rho-X.grad rho.

## 1. The reviewed one-tangent obstruction is correct

For every 0<=a<=2gamma, every lambda>0 with lambda!=1, and every real mu,

    rho_lambda-rho-mu Lambda rho is not in E_a.            (2)

Indeed (1) gives its j-th leading coefficient as
lambda^x_j-1-mu x_j, where x_j=1-e_j=(j+1)delta>0. If the j=0
coefficient is nonzero, its leading power e_0>=a-1 is not E_a-integrable.
If it vanishes, mu=(lambda^x_0-1)/x_0. The j=1 coefficient is then
x_1(f(x_1)-f(x_0)), with

    f(x)=(exp(sx)-1)/x=s int_0^1 exp(sxt)dt, s=log lambda.

Here f'(x)=s^2 int_0^1 t exp(sxt)dt>0 for s!=0. Thus the coefficient
is nonzero and its power e_1=2gamma-1>=a-1 again fails integrability.
All later powers are smaller and cannot cancel this leading term.
This proves R1-025 R3's displayed claim, including a=2gamma.

## 2. A finite linear augmentation does represent the whole orbit

For every a>=0 let

    J_a={j in {0,1,2,3}: e_j>=a-1},
    Z_a=span{T_j: j in J_a}.

Then for every fixed lambda>0,

    rho_lambda-rho
      -sum_(j in J_a)(lambda^((j+1)delta)-1)T_j is in E_a. (3)

To prove this, insert (1). The omitted j have e_j<a-1 and therefore
integrable squares at infinity. For j>=4, e_j<=e_4<-1, so their tails
are in every E_a with a>=0. The remainder and its dilate have decay
O(r^(gamma-2)), also integrable. Cutoff mismatches occur only in a
compact annulus and are smooth. All terms are therefore in E_a.

The quotient classes of the T_j for j in J_a are linearly independent:
in a nonzero linear combination the greatest e_j with nonzero scalar
coefficient is a nonzero angular leading term with e_j>=a-1.
Its squared radial integral diverges. Because e_j decreases strictly,
J_a is either empty or {0,...,m-1}. It follows that dim Z_a=m and the
quotient span of all orbit differences is exactly m-dimensional.
For the lower bound on this latter span, write z=lambda^delta and
choose m distinct positive z values different from1. The coefficient
matrix has entries z_i^k-1 for k=1,...,m. If its columns had a nonzero
relation, the degree-at-most-m polynomial sum_k b_k(z^k-1) would vanish
at those m values and at1, hence would have m+1 distinct roots and
would be zero. Its coefficients b_k would all vanish, a contradiction.

In particular, at a=0 the smallest possible linear augmentation of
E_0 that contains all orbit differences has dimension4. More generally,

    m=4 for 0<=a<=4gamma-2,
    m=3 for 4gamma-2<a<=3gamma-1,
    m=2 for 3gamma-1<a<=2gamma,
    m=1 for 2gamma<a<=1+gamma,
    m=0 for a>1+gamma.                                   (4)

The exact endpoint inequalities 0<4gamma-2<3gamma-1<2gamma<1+gamma
are immediate from 1/2<gamma<1.

Thus the wording that dilation can 'only be added as a nonlinear
coordinate', when interpreted as excluding finite linear tail
augmentations, is too strong. The orbit is a nonlinear curve inside
the finite linear augmentation Z_a+E_a. A single tangent column fails
in the range of (2); four tail amplitude columns suffice at a=0.
This is different from continuously changing the exponent, whose
quotient span is infinite-dimensional by T4-205. These amplitude
coordinates are not an existence framework: the IPM tail equations,
normalization, derivative mapping bounds and inverse remain necessary.

## 3. Exponent extraction is not continuous in the weaker ambient norm

For completeness, R1-025 R1 is correct as a topological statement.
Let T_gamma=chi r^gamma Theta for a fixed nonzero smooth Theta, with
gamma in a compact interval I subset (0,1), gamma>=a-1 throughout,
and let b>1+max I. On the set

    A=union_(gamma in I)(T_gamma+E_a),

the exponent is uniquely defined, since a difference of two distinct
tails does not belong to E_a. But it is not continuous in the topology
inherited from E_b. Choose gamma!=gamma' in I and smooth cutoffs chi_n
that equal1 for r<=n and0 for r>=2n. Then

    f_n=T_gamma'+chi_n(T_gamma-T_gamma')

has exponent gamma', because its correction is compactly supported.
Yet f_n tends to T_gamma in E_b by dominated convergence. A proof that
requires continuous recovery of the exponent therefore cannot rely on
this ambient norm alone. The product topology |d gamma|+||h||E_a is
one sufficient chart topology; it is not asserted to be the unique
possible topology. Smoothness of the map into E_b supplies no inverse.

## Exact endpoint method and dependencies

The canonical potential is a finite sum of
A_(j,m,k) H_m r^(2(k-m))(1+r^2)^(p_j-k), with
p_j=(3+e_j)/2. Its branch-j leading potential amplitude is
A_(j,m)=sum_k A_(j,m,k). Put d_j=3+e_j. Applying -partial_y Delta to
r^d_j sum_m A_(j,m)cos(2m theta) gives first sine coefficient

    b_(j,1)=-A_(j,0)d_j^2(d_j-2)
                    +A_(j,1)(d_j^2-4)d_j/2.             (5)

No other cosine mode contributes to sine1. Formula (5), evaluated over
Q from the frozen canonical snapshot, independently checks nonvanishing
for j=0,...,3 against the raw-generator endpoint computation in R1-025.
Only nonvanishing is needed for (2) to (4). The verifier also checks the
small exact Vandermonde determinant at z=2,3,4,5.

Dependencies: the exact007 representation, T4-205's elementary tail
integrability proof, finite polynomial differentiation, and elementary
linear algebra. No new norm of the full residual, no bound on an inverse,
and no theorem about existence follows.

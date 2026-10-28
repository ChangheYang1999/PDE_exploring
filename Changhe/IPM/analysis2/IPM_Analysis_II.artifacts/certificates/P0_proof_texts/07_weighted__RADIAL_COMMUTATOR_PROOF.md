# A radial-resolvent bound for the weighted negative-order commutator

## 1. Statement, spaces and scope

Let H be the homogeneous H^(-1) completion of complex centrally odd compact smooth functions on R^2. Fix R>0, 0<delta<=1 and 0<=s<3-delta. Set

    w=(1+r^2/R^2)^(-s/2),
    B=(partial_x-i partial_y)^2(-Delta)^(-1),
    M_delta=sup_(z>0) z^(2-delta)/(1+z^2)
           =(delta/2)((2-delta)/delta)^(1-delta/2).

All transforms use the canonical full-plane realization of14_homogeneous_weight/REGULARIZED_PROOF.md. Then

    ||r^(-delta)(w B w^(-1)-B)g||_H
      <=[4s M_delta/(3-s-delta)] R^(-delta)||g||_H.       (1)

Let rho have the project's real density parity, a=grad rho, and

    C_rho=sup_(r>0) r^delta(|a|+r|Da|)<infinity,
    T h=U[h].a, U=(-R1 R2,R1^2).

Then on the real density subspace

    ||w T w^(-1)-T||_(H->H)
      <=[4s M_delta/(3-s-delta)] C_rho R^(-delta).         (2)

In particular, for delta=2/5 and 0<=s<=11/5, the bracket is less than14. This replaces the factor2^53 in the earlier commutator estimate. The result is an upper bound, not a sharp-norm claim. It changes neither the background matrix assumptions nor the realization of the linear operator.

## 2. Resolvent difference on the logarithmic cylinder

Put t=log r, D=partial_t and

    alpha(t)=-D log w=s e^(2t)/(R^2+e^(2t)).

Write a source mode as g=r^(-2)F(t)e^(in theta), n odd. Its negative norm squared is

    2pi ||Q_n^(-1/2)F||_2^2, Q_n=n^2-D^2.

For n>=3, the weighted Beurling transform maps this mode to n-2, with cylinder source

    -F+2(n-1)(n-D-alpha)^(-1)F.

For n=-k, k>=1 odd, the corresponding source in mode-k-2 is

    -F+2(k+1)(D+k+alpha)^(-1)F.

The positive inverses are future Volterra integrals and the negative inverses are past Volterra integrals. These are the canonical radial Poisson formulas proved in the regularized-weight theorem. The mode n=1 maps exactly to-F in mode-1 for every radial weight, so its commutator is zero.

Subtract the formulas at alpha=0. The resolvent identity gives

    E_n=2(n-1)(n-D-alpha)^(-1) alpha (n-D)^(-1)F, n>=3,
    E_(-k)=-2(k+1)(D+k+alpha)^(-1) alpha (D+k)^(-1)F.

Multiplication by r^(-delta)=exp(-delta t) shifts the two outer inverses:

    r^(-delta)(n-D-alpha)^(-1)
       =(n-delta-D-alpha)^(-1)r^(-delta),
    r^(-delta)(D+k+alpha)^(-1)
       =(D+k+delta+alpha)^(-1)r^(-delta).                   (3)

These identities first follow by substitution in the Volterra formulas. Their convergence is ensured by n-delta-s>0 and k+delta>0. Thus no boundary solution or harmonic term is introduced by the conjugation.

## 3. Mode bounds

The Fourier multiplier identities give

    ||(n-D)^(-1)F||_2=||Q_n^(-1/2)F||_2,
    ||(D+k)^(-1)F||_2=||Q_k^(-1/2)F||_2.

The shifted Volterra kernels are bounded by exponential convolution kernels. Hence their L2 norms are at most1/(n-delta-s) and1/(k+delta), respectively. Also

    ||r^(-delta)alpha||_infinity=s M_delta R^(-delta).

Applying Q_(n-2)^(-1/2) or Q_(k+2)^(-1/2) after these L2 estimates gives the respective block bounds

    2(n-1)s M_delta/[(n-2)(n-delta-s)] R^(-delta),
    2(k+1)s M_delta/[(k+2)(k+delta)] R^(-delta).             (4)

The first expression decreases with n>=3, because both1+1/(n-2) and1/(n-delta-s) decrease. Its maximum is the bracket in(1). The second decreases with k>=1: differentiating its logarithm gives1/[(k+1)(k+2)]-1/(k+delta)<0 for0<delta<=1. At k=1 it is4s M_delta/[3(1+delta)], no larger than the first maximum, since3-s-delta<=3(1+delta).

Angular orthogonality now proves(1) on finite angular sums with compact annular radial support. This core is dense in H. The bound defines the extension of the weighted commutator, including its r^(-delta) factor. Its distributional action agrees with the original commutator on smooth compact inputs by the radial formulas and local convergence. Possible growth of r^(-delta) at the origin is handled by the proved bounded map; no bounded-multiplier assertion about r^(-delta) alone is made.

## 4. Restore the density-gradient coefficient

For real scalar inputs, U2+i U1=(B-I)/2. The local identity cancels from the commutator. Thus (1) gives the vector negative-norm bound with half its constant.

Put b=r^delta a. Then

    |b|<=C_rho,
    r|Db|<=delta r^delta|a|+r^(delta+1)|Da|<=C_rho.

The last inequality uses delta<=1 and the definition of C_rho. For a smooth parity test phi, the vector product b phi satisfies

    ||D(b phi)||_2
       <=C_rho||Dphi||_2+C_rho||phi/r||_2
       <=2 C_rho||Dphi||_2.

The final inequality is the angular parity Hardy inequality. Each component has exactly the dual parity of the corresponding velocity component. By duality, multiplication by b from vector H to scalar H has norm at most2C_rho. Compose it with the half-constant vector estimate to obtain(2).

The fractional power r^delta makes b only locally weakly differentiable at zero. The displayed Hardy estimate still defines its bounded multiplier action. Approximation away from zero and completion justify the dual calculation without assuming a bounded ordinary gradient at the origin.

At delta=2/5, M_delta=4^(4/5)/5. The bracket is increasing in s and equals22 M_delta at s=11/5. The elementary integer inequality

    4^4 * 11^5 < 35^5

implies M_delta<7/11, hence22 M_delta<14. The sharper bracket is about13.3383. No numerical approximation is needed for the bound14.

## 5. Consequence for the already established low inverse

In LOW_INVERSE_FAMILY_PROOF.md, replace the commutator factor2^53 by14. Every other term and its sign is unchanged. With the coefficient bounds C_rho,C_U,C_DU,C_D2U from that theorem, set

    C_new(s)=C_DU+C_rho
              +s(9C_U+2C_DU+C_D2U/sqrt(2))+14C_rho.

If m_s-C_new(s)R^(-2/5)>0, the same graph-core energy argument and semigroup integral give a bijective generator realization, with inverse norm at most the reciprocal of that difference. This proves injectivity and surjectivity in the same completion. A change of R changes equivalent norms, and therefore requires rechecking any constants that were tied to a particular norm. No nonlinear conclusion follows from the commutator improvement alone.

## 6. Smaller certified radius for the accepted state

For the exact state131, the completed global derivative certificates give

    |D rho|<16, |DU|_F<14/5,
    <r>|D2 rho|_F<=8, <r>|D2 U|_F<=3, U(0)=0.

The first line follows from the component certificates in02_energy/AUXILIARY_CERTIFICATE_PROOF.md; the second line is V045, proved in SHARP_COEFFICIENT_PROOF.md. Here <r>=(1+r2)^(1/2). For r<=100 these imply

    r^(2/5)(|D rho|+r|D2 rho|)<=24*100^(2/5)<152,
    r^(-3/5)|U|, r^(2/5)|DU|<= (14/5)*100^(2/5)<18,
    r^(7/5)|D2 U|<=3*100^(2/5)<19.

The independent exact-sector calculation in verification/state131_weighted_bounds.json, on r>=100, bounds these four quantities respectively by123.078,1.613,6.010 and44.872. These decimal upper bounds are rounded upwards from the retained Arb intervals. Thus the global tuple

    (C_rho,C_U,C_DU,C_D2U)=(152,18,18,45)                    (5)

is valid for the same exact source state. All derivatives and Euclidean tensor conventions match the low energy identity.

At R=2^35, R^(2/5)=2^14. Substituting(5) in section5 gives the following strict lower bounds:

| s | m_s-C_new(s)R^(-2/5) | rounded margin | inverse upper bound |
| --- | --- | --- | --- |
| 1 | >2.54571412 | 5/2 | 2/5 |
| 2 | >0.63168703 | 3/5 | 5/3 |
| 11/5 | >0.22888161 | 1/5 | 5 |

The interval arithmetic is reproduced in verification/radial_commutator_constants.py and its JSON. It is not needed to trust a floating-point sign: replacing1/sqrt(2) by5/7 in C_new gives a rational upper bound, and exact rational comparison still proves all three rounded margins. The original common coefficient tuple(2^16,32,32,2^15) similarly gives an error below1/5 at R=2^56, hence the same rounded table for both states88 and131.

These are sufficient radii for this estimate. No minimal-radius assertion is made. The original density residual is in the s=11/5 space; it is not in the s=1 or s=2 spaces. Its norm has not been shown small at the new radius. The high norm and nonlinear theory in earlier sections continue to use their explicitly stated radii and constants until separately rechecked.

# Real angular pairing improves the weighted velocity and low radius

Status: CONFIRMED V095 after complete independent analytical and512-bit arithmetic audit. A review by the lead was requested.

## Statement

Let H be the homogeneous H^-1 completion of real centrally odd compact smooth functions on the plane, and define H_(sigma,R)(h)=||w_R h||_H, with w_R=(1+r^2/R^2)^(-sigma/2), R>0 and0<=sigma<=11/5. The velocity is the canonical full-plane U=(-R1R2,R1^2), with a Hilbert sum of its two components. Then

    H_(sigma,R)(U[h]) <= (13/3) H_(sigma,R)(h).             (1)

No sharpness is asserted. The proof uses only real central oddness, so it applies to the project's narrower density parity. The earlier13/2 bound is replaced by13/3.

For sigma=11/5 and d=4/9, the real weighted coupling commutator satisfies

    ||w_R (U[w_R^-1 g].D rho)-U[g].D rho||_H
       <=(21/2) C_rho R^-d ||g||_H,                       (2)
    C_rho=sup r^d(|D rho|+r|D2 rho|).

Consequently, a reference satisfying all the current low-energy hypotheses and

    (C_rho,C_U,C_DU,C_D2U)<=(186,22,22,56)                 (3)

has low margin greater than1/5 already at R=2^31. Here C_U=sup r^(d-1)|U|, C_DU=sup r^d|DU| and C_D2U=sup r^(1+d)|D2U|. The original exact state131 satisfies(3), as checked below. The compatible fractional theorem of topic18 then holds in this new norm with the same s=3*2^-31, r0=5*2^-32, eta=2^-35, high inverse40 and low inverse6. No actual residual smallness at the new radius is asserted.

## 1. Real pairing of angular modes

All norms and inner products in this section are in the weighted space H_(sigma,R), or equivalently in H after conjugation by w_R. Put B=(partial_x-i partial_y)^2(-Delta)^-1 and t=log r. For each odd integern write w_R h=r^-2 F_n(t)e^(in theta), Q_n=n^2-partial_t^2. The scalar negative norm is the sum of2pi||Q_n^-1/2 F_n||2^2. Since h is real, F_-n=conjugate(F_n), so the two input norms are equal.

The exact Volterra formulas and their proof in topic14/REGULARIZED_PROOF.md give, for n>=3, the positive block B:n->n-2 with norm at most

    A_n=n(n-2+sigma)/((n-2)(n-sigma)),

and for n>=1 the negative block B:-n->-n-2 with norm at most

    D_n=1+sigma/(n+2).

The positive n=1 block is exactly minus the identity into angular mode-1. Both A_n and D_n decrease in n over their indicated ranges and increase in sigma. Their values at sigma=11/5 may therefore be used throughout. Normalize a_n>=0, n positive odd, so that a_n^2 is the sum of the positive and negative input energies at n, including2pi. Thus ||h||^2=sum a_n^2.

Orthogonality of output angular modes gives

    ||Bh||^2 <= (1+D_1^2)a_1^2/2
                   +sum_(n>=3)(A_n^2+D_n^2)a_n^2/2.      (4)

Only modes separated by two can contribute to <Bh,h>, except for the n=1 reflection. The latter contribution is bounded below by-a_1^2/2. For each n>=3 the two links between the pair n and n-2 are bounded below by

    -(A_n+D_(n-2))a_n a_(n-2)/2.

This follows from the block norms and Cauchy-Schwarz; it does not assume that the positive and negative blocks are adjoints or have the same sign. For the project's sine parity the n=1 self term is actually positive, but that improvement is not needed.

Since U2+iU1=(B-I)h/2, equations(4) and the cross bounds give

    ||Uh||^2 <= sum J_nn a_n^2+2sum J_(n,n-2)a_n a_(n-2),

where

    J_11=5/8+D_1^2/8,
    J_nn=1/4+(A_n^2+D_n^2)/8, n>=3,
    J_(n,n-2)=(A_n+D_(n-2))/8, n>=3.                     (5)

All coefficients in this comparison matrix are nonnegative. The complex norm of U2+iU1 is exactly the Hilbert sum of the real component norms, because the radial negative-order inner product is real on real functions.

## 2. Explicit weighted row bound

Choose positive weights v_1=1/10, v_3=1, v_n=1/20 for n>=5. The elementary inequality2xy<=a x^2+a^-1 y^2 on each edge proves that the quadratic form of J is bounded by

    sup_n (sum_m J_nm v_m)/v_n * sum_n a_n^2.             (6)

This argument works first for finite sequences. Its constant extends by density; no unproved infinite-matrix spectral theorem is needed.

At sigma=11/5 the exact constants are

    A_3=12, A_5=65/21, A_7=21/10,
    D_1=26/15, D_3=36/25, D_5=46/35.

For row1, (6) is J_11+10J_13<19. For row3 it is

    J_33+J_31/10+J_35/20 <75/4.

The sharper common target75/4 also holds for row1 by direct rational comparison. Row5 is J_55+20J_53+J_57<14. For n>=7, monotonicity gives J_nn<2 and each adjacent off-diagonal entry<1, hence row sum<4. All these are exact rational inequalities checked in the adjacent script. Therefore ||Uh||^2<=(75/4)||h||^2. Finally75/4<169/9 because675<676. This proves(1). Finite angular sums and compact annular radial sources are dense in the stated space; the canonical completion is the same as in the Volterra theorem.

## 3. Real commutator estimate

The radial-resolvent proof in topic07/RADIAL_COMMUTATOR_PROOF.md applies to

    r^-d(w_R B w_R^-1-B).

For positive n>=3 its block norm is bounded by

    P=4 sigma M_d/(3-sigma-d),
    M_d=(d/2)((2-d)/d)^(1-d/2).

For negative n=-k it is bounded by

    D=4 sigma M_d/[3(1+d)],

using the maximum at k=1. The positive n=1 block is zero. Real pairing and angular orthogonality therefore improve the full complex-source bound P to

    C_real=sqrt((P^2+D^2)/2).                             (7)

Indeed each positive/negative input pair has equal norm, while its two outputs remain orthogonal. The real velocity commutator has half this norm, since the local identity cancels.

At sigma=11/5,d=4/9, P=(99/4)M_d and D=(132/65)M_d. Moreover M_d^9=4*7^7/9^9, so the integer inequality4*7^7*100^9<59^9*9^9 gives M_d<59/100. Substitution in(7) proves C_real<21/2 by a rational squared comparison.

To restore the coefficient put b=r^d D rho. Then |b|<=C_rho and r|Db|<=C_rho because d<=1. Angular parity Hardy and the product rule give ||D(b phi)||2<=2C_rho||Dphi||2 for a centrally odd scalar test phi. This multiplier bound cancels the factor1/2 of the velocity commutator and proves(2). Weak differentiability at the origin, completion and the canonical realization are justified by exactly the same cutoff argument as in the existing radial-resolvent proof. No independent bound on multiplication by r^-d is assumed.

## 4. Radius2^31 and compatibility

The original-state certificate in topic17/verification/decay_radius.json already encloses the local coefficient quantities below185.824,21.680,21.680,23.228 and the exterior quantities below151.032,1.979,7.375,55.064. The new script checks these balls against(3), including their exact source hash, and reconstructs the original coefficient vector again for input identity. Thus(3) requires no new continuum enclosure method.

The exact low-energy proof now yields the margin

    2/5-R^-d [22+(1+21/2)186
                    +(11/5)(9*22+2*22+56/sqrt(2))].       (8)

At R=2^31, R^d=2^(124/9)>14000, as verified by the integer inequality14000^9<2^124. Also1/sqrt(2)<5/7. Hence(8) is strictly greater than

    2/5-[22+(23/2)186+(11/5)*282]/14000
       =14093/70000 >1/5.                                (9)

The generator, its graph core and the inverse integral depend on the positive margin and the same canonical weighted coupling, not on the old sufficient radius. They therefore give a bijective low realization with inverse at most5 and the same perturbed bound6 used in topic18. All derivative weights and their coefficient bounds are unchanged. Topic17 section3 proves that the Bessel, interpolation, localization, common-domain and low/high consistency estimates are uniform for every R>=1. Thus the complete topic18 theorem transfers to R=2^31 with unchanged parameters and hypotheses, replacing only its explicit low coefficient contract by(3),(8).

The improved velocity bound also makes the low bilinear constant in topic18 equal to at most280*(13/3)=3640/3<1280, rather than1820. Keeping the old rounded2048 is valid, so no unproved optimization of the nonlinear parameters is involved in the transfer. A residual norm at R=2^31 must be checked in that norm; old-radius numerical lower or upper bounds are not silently substituted.

## Dependencies and scope

The real pairing argument is analytical. The only source-specific input is(3) and the unchanged reference contract from topic16, including global matrices and derivative bounds. The script binds all imported proof and certificate files and performs exact rational inequalities plus512-bit arithmetic. This is a sufficient improvement, not a sharp velocity constant or a minimal radius. Original-profile nonlinear existence remains unproved.

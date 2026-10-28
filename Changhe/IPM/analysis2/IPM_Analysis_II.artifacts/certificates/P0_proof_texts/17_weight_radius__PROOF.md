# A smaller low-weight radius for the accepted reference

Status: CONFIRMED V088. The earlier V087 entry was an open candidate. This proof completes its coefficient and realization checks. All constants below are sufficient bounds.

## Statement and notation

Let rho be the exact state 131 reconstructed from the original checkpoint, let c=4076476460239181/2251799813685248, and let u=U[rho] be the canonical full-plane velocity. Densities are even in x and odd in y. Set

    gamma=1/c, delta=1-gamma, d=4/9, sigma=11/5,
    R=2^32, w_R=(1+r^2/R^2)^(-sigma/2),
    L_R(h)=||w_R h||_(homogeneous H^-1).

The low space is the completion of compact smooth parity functions in L_R. On its transport-generator domain, the fixed-exponent operator

    L_fix h=(cX+u).D h-h+U[h].D rho

is bijective and its semigroup decays at least at rate 1/5. Its inverse norm is at most 5. The proved energy margin is greater than 0.20605715.

The following compatible high statement also holds with this R. Define

    P1(h)=||<r>^(-1/5) Dh||_2,
    P2(h)=||(1+4r^2)^(2/5) D^2h||_2,
    E_R(h)^2=P2(h)^2+2^22 P1(h)^2+2^53 L_R(h)^2,
    N_(s,R)(h)=E_R(J^s h), J=(1-Delta)^(1/2).

All tensors are the ordered Cartesian tensors with their Euclidean norm. These spaces are again compact smooth parity-core completions. For 0<s<=2^-12 and k in N_(s,R), the maximal distributional generator

    A_k=L_fix+U[k].D

has semigroup norm at most

    exp[-t(1/20-2^23 s-2^19 N_(s,R)(k)/sqrt(s))].          (1)

A positive rate gives a bijective inverse with the reciprocal bound. At s=2^-30, on the radius 2^-41 ball, the high inverse is at most 32 and the low inverse at most 6. If the actual reference residual satisfies N_(s,R)(F(rho;c))<=2^-46, the same normalized two-norm contraction gives a unique correction in that ball. Its contraction constant is 3/1024. This is a conditional smallness statement, not an existence claim for the checkpoint.

The general reference version requires W0, Wn, W2, W3, Wm and, for existence, Ws of ../16_weighted_fractional/REFERENCE_AUDIT.md, with the new radius in every norm. Replace W1 by M>=19I/5 and the four d=4/9 bounds proved below. Wt gives the same fixed leading angular profile and scaling conclusion. No other reference hypothesis is removed.

## 1. Stronger decay bounds from the original coefficients

The exact rational exponent satisfies 4/9<delta<1/2. Put

    C_rho=sup_(r>0) r^d(|D rho|+r|D^2rho|),
    C_U=sup_(r>0) r^(d-1)|u|,
    C_DU=sup_(r>0) r^d|Du|,
    C_D2U=sup_(r>0) r^(d+1)|D^2u|.

The global derivative certificates V024 and V045 give |D rho|<16, |Du|<14/5, <r>|D^2rho|<=8 and <r>|D^2u|<=3. Since u(0)=0, |u(X)|<=(14/5)r. On r<=100 the four expressions are therefore bounded by

    24*100^d, (14/5)*100^d, (14/5)*100^d, 3*100^d,

respectively. These are less than 186, 22, 22 and 24.

For r>=100 write each original potential term as

    a_(j,m,k) r^(3+gamma-j delta) cos(2m theta)
                         (1+r^-2)^(p_j-k),
    p_j=(3+gamma-j delta)/2.

Its binomial term of order q has radial power 3+gamma-j delta-2q. An order ell Cartesian derivative has power 3+gamma-j delta-2q-ell. Each of the four weighted physical expressions above consequently has common radial exponent

    d-delta-j delta-2q < 0.                              (2)

This is the precise exterior monotonicity needed for the stronger decay weight. It follows from the exact exponent, before any numerical bound is applied.

The certificate retains q=0,...,6. It computes the angular derivatives in a complex Laurent basis independently of the earlier sine/cosine producer. For every component and ell=3,4,5 the omitted q>=7 terms are bounded by

    binom(q+25,q)(2q+32)^ell |a_(j,m,k)| r^(-2q),

after removing r^(3+gamma-j delta-ell). This uses |p_j-k|<26, angular frequencies at most 18 before differentiation, and at most five derivatives. The successive majorant ratio is

    ((q+26)/(q+1))*((2q+34)/(2q+32))^ell /100^2 < 1

and decreases with q. The retained terms, the geometric majorant and the factor r^(d-delta) all decrease outside 100. Evaluating at 100 is thus a bound on the entire exterior. The vector and tensor sums give the outward-rounded upper bounds

    C_rho<151.032, C_U<1.979, C_DU<7.375, C_D2U<55.064

there. Combining the interior and exterior proves

    (C_rho,C_U,C_DU,C_D2U) <= (190,23,23,56).             (3)

The program reconstructs all 860 canonical coefficients from the read-only original and checks their canonical hash. Its eleven independent complex derivative majorants also overlap the previously retained enclosures. No sampled angular or radial maximum is used.

## 2. The radial commutator and every low-energy error

The radial-resolvent theorem in ../07_weighted/RADIAL_COMMUTATOR_PROOF.md holds for every 0<d<=1 and sigma+d<3. In the present case its coefficient is

    C_comm=4 sigma M_d/(3-sigma-d),
    M_d=(d/2)((2-d)/d)^(1-d/2),
    C_comm<14.573<15.                                   (4)

Its proof uses the exact positive-mode resolvent gap n-sigma-d, the negative-mode gap k+d and parity Hardy in multiplying by r^d D rho. All these conditions hold here. Thus the nonlocal energy error is at most 15 C_rho R^-d L_R(h)^2.

For completeness, the transport terms also permit this d. Put g=w_R h, phi=(-Delta)^-1g and q=Dphi. The weighted identity is

    -<w_R L_fix h,phi>
       =int q^T(M+bI)q -(1/2)int Delta b phi^2
                       -<D_R g,phi>,
    b=-sigma c r^2/(R^2+r^2)-sigma u.X/(R^2+r^2).

The radial dilation calculation depends only on sigma and c. On r<=R it gives 19/5-sigma c/2. Outside R it gives

    2c+1-(21/20)sigma c-(C_DU+C_rho)R^-d.

Both baseline margins exceed 2/5 for 9/5<c<37/20. The factor 21/20 bounds the same cubic radial polynomial as in LOW_INVERSE_PROOF.md; no new approximation is introduced.

For the velocity part write P=u.X and D=R^2+r^2. From (3),

    |P|<=C_U r^(2-d),
    |DP|<=(C_U+C_DU)r^(1-d),
    |Delta P|<=sqrt(2) C_D2U r^-d.

The last formula uses div u=0. Expanding Delta(P/D), applying parity Hardy, and using

    r^(2m-d)/(R^2+r^2)^m <= R^-d, m=1,2,3,

gives the loss sigma(9C_U+2C_DU+C_D2U/sqrt(2))R^-d. The displayed radial inequality is valid for 0<d<=1: with z=r/R, its left dimensionless factor is z^(2m-d)/(1+z^2)^m, which is at most one separately on z<=1 and z>=1.

Combining all terms gives

    -<w_R L_fix h,phi> >= mu L_R(h)^2,
    mu=2/5-R^-d[23+16*190+(11/5)(9*23+2*23+56/sqrt(2))]. (5)

At R=2^32 this is greater than 0.20605715. There is also a rational check: 19000^9<2^128 and 1/sqrt(2)<5/7 imply

    mu > 9731/47500 > 1/5.

The complete Lipschitz transport flow, compact graph core, bounded coupling and convergent semigroup integral from LOW_INVERSE_PROOF.md apply to this R. The canonical weighted Beurling and velocity operators are bounded for every R>0 by V067. Hence (5) proves the stated decay, injectivity and surjectivity in the same realization.

## 3. Transfer to the compatible fractional theorem

A change of R changes the numerical norm. Here the later constants remain valid for the following explicit reasons.

1. The two derivative weights and their principal matrices contain no R. The interpolation P0^2<=epsilon P1^2+(25+epsilon^-1)L_R^2 was proved for every R>=1 in SHARP_WEIGHTED_H2_PROOF.md. Together with the new low margin 1/5 it gives the same E1 and E_R rates 1/10 and 1/20, with exactly the same coefficients 2^31 and 2^22.
2. The dyadic fractional Fourier, derivative, product and growth estimates of 16_weighted_fractional/PROOF.md use only that interpolation and the R-independent derivative weights. The canonical velocity bound 13/2 on L_R is uniform in R. Thus their constants and parity completions are unchanged.
3. Every estimate in SHARP_LOW_COMMUTATOR_PROOF.md is explicitly uniform for R>=1. Its proof uses |r Dlog w_R|<=sigma, |<r>Dlog w_R|<=sigma and weight moderation by (1+|z|)^4. All three remain true here. In particular L_R(J^-s H)<=6L_R(H); the earlier radius-conversion estimates are not used.
4. The sharp derivative commutators contain only the two fixed derivative weights. Adding the uniform low commutator gives the same smooth loss 2^23 s and rough loss 2^19 N_(s,R)(k)/sqrt(s). The onto J^s isometry, maximal-domain proof and low/high consistency use these estimates and positive decay. Their common P0 realization is independent of R.
5. The low bilinear estimate uses the uniform 13/2 velocity constant and bounded derivative multiplier. The completeness of the high ball in the low metric and the origin trace identity depend on the same embeddings. Consequently the normalized fixed-point proof gives (1) and the stated parameters without a changed numerical coefficient.

The four-output estimate also transfers, with alpha=s/2 and the same jet-subtracted singular moment:

    L_R(h)+C_ad(h)+M(h)+|c[h]|
                <=2^18 s^(-3/2) N_(s,R)(h).

At the chosen ball the inverse bound is therefore 2^68. This transfer refers to the new norm throughout; it does not equate residual norms at different radii.

## Evidence and scope

The script verification/decay_radius.py and its JSON/log contain the fresh original-checkpoint reconstruction, exact exponent test, 512-bit field bounds, commutator constant, rational margin and input hashes. This result improves the sufficient low radius by a factor of eight. It does not repair the residual. The old R=2^35 theorem and its V084 lower bound remain valid in their stated norm. Residual comparisons for the new radius require their own argument.

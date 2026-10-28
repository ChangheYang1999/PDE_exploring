# Weighted low inverses for three fixed growth classes

## Statement and dependencies

Let the background be either exact checkpoint88 or131. Use the canonical parity realization, coefficient bounds and graph-core construction of LOW_INVERSE_PROOF.md. For s in {1,2,11/5}, let

    w_(R,s)=(1+r²/R²)^(-s/2),
    X_(R,s)=completion of the compact parity core in ||w_(R,s)h||_(Hdot^-1).

Define

    m_1=27/10, m_2=4/5, m_(11/5)=2/5,
    C(s)=C_DU+C_rho+s(9C_U+2C_DU+C_D2U/sqrt(2))+2^53 C_rho,

where C_rho=2^16, C_U=C_DU=32 and C_D2U=2^15 are the independently certified common bounds. If R>=1 and

    mu=m_s-C(s)R^(-2/5)>0,                                  (1)

then L_fix is bijective on its transport-generator domain in X_(R,s), with inverse norm at most1/mu. In particular, at R=2^179, the following rounded margins and inverse bounds hold for both backgrounds:

| s | growth threshold s-2 | proved margin | inverse bound |
|---|---|---|---|
| 1 | -1 | 5/2 | 2/5 |
| 2 | 0 | 3/5 | 5/3 |
| 11/5 | 1/5 | 1/5 | 5 |

These statements concern the original background operator. Its original residual belongs only to the last of these three spaces. A repaired background requires new coefficient certificates before using this theorem with that background.

## Proof

Every bound in COMMUTATOR_PROOF.md remains valid, with the same constant2^53, when 0<s<=11/5. Weight ratios and derivative bounds decrease when the upper exponent bound is decreased. The outer-source decay exponent becomes 3-s-2/5>=2/5; the inner-source exponent remains at least1. Thus

    ||w_(R,s) B w_(R,s)^-1-B|| <=2^53 C_rho R^(-2/5).        (2)

The radial transport calculation is identical with s replacing11/5. On r<=R it gives the margin19/5-sc/2. On r>=R, circle Poincare bounds the positive Laplacian term by the polynomial maximum21/20 and gives

    2c+1-(21/20)sc-(C_DU+C_rho)R^(-2/5).                   (3)

For9/5<c<37/20, the two unperturbed radial margins are both greater than m_s for the three listed exponents. Explicitly, their lower bounds are

    s=1: min(23/8,271/100)>27/10;
    s=2: min(39/20,163/200)>4/5;
    s=11/5: min(353/200,853/2000)>2/5.

The velocity part of the weight costs at most s(9C_U+2C_DU+C_D2U/sqrt(2))R^(-2/5), exactly as in LOW_INVERSE_PROOF.md. Combining this with(2)-(3) proves(1). The same transport flow and bounded coupling construct the generator and its exponentially decaying semigroup. The convergent semigroup integral supplies both left and right inverses.

For R=2^179 the common error is less than1/5. The displayed margins follow by subtracting1/5 from m_s. The independent Arb check in verification/low_inverse_family.py evaluates the actual error and checks each strict inequality. The threshold for the original s=11/5 argument to put the error below half its baseline2/5 lies strictly between2^178 and2^179. This is a threshold of this sufficient bound, not a lower bound on the true necessary radius.

## Interpretation of the growth threshold

A cut-off nonzero homogeneous tail r^p Theta belongs to X_(R,s) exactly when p<s-2, apart from polynomial ambiguities excluded by the parity completion. Therefore s=2 is appropriate for a residual with negative power after removal of the first residual sector; s=1 requires all remaining powers to be below-1. The large radius has not been made practically useful by lowering s. It establishes existence of the low inverse and identifies the quantitative weakness of the present commutator bound.

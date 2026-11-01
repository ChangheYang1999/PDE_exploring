# Primary radial weight at arbitrary amplitude

Status: PROVED in V600, admitted 2026-10-31T22:01:31+00:00, within the exact scope below.

## Exact statement

Let 0<delta<1, gamma=1-delta, epsilon be nonzero real, r>0, and z=|epsilon| r^(-delta). For any angular functions T and U,

    r^(-gamma) ||T|| = (|epsilon|/z) r^(-1) ||T||,
    r^(-1-gamma) ||U|| = (|epsilon|/z) r^(-2) ||U||.

These identities also hold with any fixed radial or angular derivatives inside the norm. Thus bounds D(z) and E(z) on the two latter weighted norms convert to |epsilon|D(z)/z and |epsilon|E(z)/z. Division by z alone is the conversion for |epsilon|=1, or for an additionally amplitude-normalized left side.

## Proof

The ratio r^(-gamma)/r^(-1) is r^(1-gamma)=r^delta. The ratio r^(-1-gamma)/r^(-2) is the same. The definition of z gives r^delta=|epsilon|/z. This proves both statements with no assumptions on T, U, their recurrence, or the norm besides homogeneity by positive scalars.

For an exact test of the conversion, take delta=1/2, epsilon=2, r=16 and the single term T=epsilon^3 r^(1-3delta) sin(theta). Its unweighted angular supremum is 2, so r^(-1)||T||=1/8 and r^(-gamma)||T||=1/2. Here z=1/2. Dividing 1/8 by z gives 1/4; multiplying by |epsilon|/z gives the correct 1/2. This is a test of the universal normalization conversion, not an assertion that this isolated term is an IPM solution or that a particular loose majorant fails for its certified series.

## Scope and dependencies

Section 12.6 Remark 6 first states its bounds at z=r^(-delta), then prescribes z=|epsilon|r^(-delta) for general amplitude, and later says that primary normalization divides the right sides by z. The latter sentence needs the unit-amplitude qualifier or the general factor |epsilon|/z. All displayed numerical examples there explicitly use epsilon=1 and are unchanged. The infinite-series convergence theorem and all certified radius exponents are unchanged. Only elementary exponent identities are used.

## Completed verification

The correct conversion factor is |epsilon|/z=r^delta. The rational test gives old density weight1/8, primary weight1/2 and z1/2; division by z gives1/4, whereas multiplication by |epsilon|/z gives1/2. The original division rule is valid at unit amplitude or with an additionally amplitude-normalized left side.

The unqualified division-by-z rule is REFUTED; the corrected identity is PROVED. All unit-amplitude displayed examples and certified radius exponents remain unchanged. No failure of a particular loose majorant is inferred from this normalization test.

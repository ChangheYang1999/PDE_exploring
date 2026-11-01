# Conditional continuation diagnostics through order400

Status: the finite arithmetic checks passed and are admitted in V529. All later-than329 data remain conditional on the midpoint reset. This is not an infinite-series convergence theorem.

## Statement and input scope

The input is the numerical experiments' delta=2/3 canonical logarithmic continuation after replacement of the loaded order329 coefficient balls by their midpoints. All order330 and later statements are conditional on that replacement. New arithmetic radii do not recover the discarded canonical uncertainty. A hash and input metadata identify the checkpoint actually read.

For a density or stream coefficient polynomial in log r, define its plain norm as the sum of the absolute values of all Fourier/logarithmic coefficients. Compute these norms, the nth roots, factorial-column maxima, three-order decrements and ordinary least-squares logarithmic slopes independently at768-bit precision. Check the newly published table for orders391 through400 against directed enclosures. Check the full logarithmic Poisson equation in every stored coefficient at398,399,400, including the canonical resonant zero constant.

## Shifted profile comparison

For each order n from348 through400, let x_n be the full real coefficient array with its Euclidean inner product, and S the isometric shift of the preceding order n-3 array by one angular index. Define

    a_n = <S x_(n-3),x_n>/||x_(n-3)||^2,
    e_n^2 = 1 - <S x_(n-3),x_n>^2/(||x_(n-3)||^2 ||x_n||^2).

Direct expansion gives ||x_n||/||x_(n-3)||=|a_n|/sqrt(1-e_n^2), provided both arrays are nonzero. Replay prior enclosures where available. Fit log10|a_n| separately as an affine function of log10 n,1/n andn. Each fit describes only its finite window. A fitted limiting multiplier, power exponent or eventual growth prediction is conditional on extending the fitted law; none is inferred from a small residual alone.

## Dependencies and verification

Use the independently derived Fourier/logarithmic Poisson identities of01 and10 and the midpoint-provenance analysis138 and189. Arithmetic receipts list coefficient counts, exact checkpoint hashes, table comparisons, fitted windows and residuals. The strict interval incompatibility of two observed three-order decrements refutes an exact finite cycle but says nothing by itself about a limiting cycle.

## Completed checks

The768-bit norm/Poisson audit checked4,464,935 norm positions,159,201 Poisson coefficients and59 printed comparisons. The shifted-array audit checked53 orders per field and92 prior enclosures. Both receipts passed. Their real elapsed times were43.12 and37.49seconds. The exact input checkpoint hash appears in the receipts. The separate rounded-input auditV534 reproduces every published fit number on all three windows when it uses all orders and multipliers rounded to five decimals. It does not reproduce the full-array directed values. The rounding choice must be stated whenever those figures are quoted.

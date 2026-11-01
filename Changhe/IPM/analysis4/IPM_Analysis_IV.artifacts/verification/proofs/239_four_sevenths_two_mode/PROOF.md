# Independent two-mode certificates at delta=4/7

Status: PROVED in V498. All three roots have complete response certificates, exact majorant boxes and independent1024-bit replays.

## Statement to be certified

Set delta=4/7 and c=7/3, and let f_1(theta)=epsilon(sin(theta)+b sin(3 theta)), for nonzero real epsilon. The first stream resonance is order7, and its compatibility is the vanishing of the sin(theta) coefficient O(b) of f_7. Let P be its primitive integer polynomial with positive leading coefficient. The proposed certificate determines P independently, proves its irreducibility and counts its real roots. For each increasingly numbered real root, a complete integer-response certificate and an exact nonnegative majorant box imply convergence of the tuned density and stream series and their common potential on

    r>=R>2^(q/4)|epsilon|^(7/4),

where q is the integer in that root's completed certificate. All appropriately weighted derivatives converge. No quantitative claim is made for a root whose cover or replay fails. The common potential is allowed its exceptional order7 logarithmic term; its coefficient need not vanish.

## Independent first compatibility calculation

The signed-Laurent Cartesian implementation uses p_n=1-4n/7 and

    f_n=[3/(4(n-1))] sum_(i+j=n) (g_(i,x) f_(j,y)-g_(i,y) f_(j,x)).

It solves -Delta g_i=partial_x f_i and checks each nonresonant inverse by differentiation. Computation takes place over rational polynomials in b. Through order7 the maximal density frequency is4n-1. At order7 the stream exponent is-2, its kernel has frequency2, and its compatibility is precisely the frequency1 density coefficient. All coefficient polynomials through7 are retained for a separate interval-prefix comparison.

An exact rational Sturm chain counts and isolates all real roots of P. If its same-degree reduction modulo23 is irreducible, the corresponding finite-field Frobenius and greatest-common-divisor certificate proves irreducibility over the rationals. Irreducibility is not used as a substitute for the later quantitative response checks.

## Complete response certificate

At order7k, a unit stream harmonic has frequency4k-2. Propagating its affine response for seven density orders gives sigma_k(b), the frequency4k+1 coefficient of f_(7k+7). The response uses only f_1 through f_7 and g_1 through g_6. It is independent of earlier tuned harmonic values by the affine index theorem144.

The bandwidth is B=4. For k>=8, the carrier frequency4k-2 is at least30>BQ=28, so the compact rational response formula149 agrees with the full response. The certificate checks full responses for k=1 through7 and uses the exact integer-cover theorem232 on t_k=1/(4k-2), within [0,1/30]. Every leaf is an empty integer range, a validated singleton, or a validated interval with Taylor enclosure234. All nonempty leaves must prove the same positive lower bound s. Complete rational partition replay establishes coverage of every integer k>=8.

Root intervals enclose the isolated algebraic root throughout these computations. Thus all response enclosures and all norm bounds hold for the exact root. A separate replay refines the root, computes the full finite responses and every nonempty tail leaf at higher precision, and compares the low interval coefficients with independent exact polynomial formulas.

## Majorant and exterior conclusion

For h=2,Q=7,B=4, the particular Poisson norm bound is L=147/80 and the nonlinear prefactor is kappa=48/7. Exact upper bounds on n||f_n||_1 for1<=n<=7 initialize the finite-prefix majorant172, with no earlier free harmonics. A verified rational supersolution at w=z^7=2^-q gives a positive series radius in w. The all-index response bound supplies all later tuning denominators through145.

Homogeneity gives degree n in epsilon at order n and replaces z by epsilon z. Since z=r^-4/7, the sufficient radius scales by |epsilon|^(7/4). On every strict exterior, geometric decay absorbs the polynomial factors from each fixed derivative. The common-potential reconstruction and the absolute convergence of products justify the stationary IPM equation there. This is an exterior solution theorem, not a whole-plane extension or a statement of optimal radius.

Dependencies:01,144,145,149,169,172,232,234. Completed arithmetic receipts, exact polynomials and replay records are required before changing the status above.

## Completed certificates

For the increasingly numbered roots, the final (s,q) values are (1/16777216,113), (1/2097152,121), (8,114). Each certificate has13 singleton and3 Taylor leaves,16 full finite responses,9 full/compact checks,306 exact-prefix coefficient comparisons and an exact rational majorant-box replay. Thus the displayed sufficient radius formula is established with those q values. The earlier root3 s=1 certificate is retained separately.

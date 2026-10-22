# Higher Taylor order as a sufficient remainder refinement

The all-mode check selected_v2_checks.json verifies every degree0 through12
coefficient of P and R in cells0,4102,7808 with both engines. Its uniform
derivative-only remainder succeeds throughout the first two cells, but
fails the sufficient comparison for both families in modes5 through47 of
cell7808. The largest failed ratio is about2.47. Those failures remain
recorded and are not refutations of the candidate models.

For any integer K>Q, the exact Taylor identity is

 f(u)-sum_(j=0)^Q c_j u^j
 =sum_(j=Q+1)^K c_j u^j + (f(u)-sum_(j=0)^K c_j u^j).

Consequently, if |c_j|<=C_j for all admitted inputs and H_K uniformly
bounds the degree-K Taylor remainder, then

 |f(u)-sum_(j=0)^Q c_j u^j|<=sum_(j=Q+1)^K C_j h^j+H_K,
                                                   0<=u<=h.

The existing exact coefficient formula and independent affine recursion
apply to every finite j. The existing Leibniz or derivative-polynomial
majorant also applies to every K: it uses forcing derivatives through K
and solution derivatives of order K+1. In particular the degree7 forcing
polynomial does not make its exponential-polynomial derivatives vanish.
Both implementations retain them through the requested K.

Version3 uses K=20. It checks candidate coefficients only through Q=12,
and separately bounds P and R remainders using their own interval
coefficient magnitudes at orders13,...,20 and the previously proved
common H_20. Magnitudes are exact maxima of absolute directed endpoints.
The input boxes are unchanged, and each engine performs its own entire
calculation. No producer remainder is enlarged. Failure is still OPEN.

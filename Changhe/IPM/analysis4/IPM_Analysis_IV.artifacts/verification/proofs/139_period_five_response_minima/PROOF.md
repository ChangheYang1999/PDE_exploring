# Exact global resonant-response minima for the six period-five profiles

Status: PROVED. The independent Cartesian certificates and the theory part's separate Fourier and rational computations agree. The independent review dated 2026-10-31T11:06Z is recorded in V284. All conclusions retain the exact hypotheses and scope stated below.

## Statement and notation

Let b_i, i=1,...,6 in increasing order, be the six real roots of the primitive obstruction polynomial P10 defined by the order10 Cartesian recurrence in133. Let sigma_k(b), k>=2, be the exact five-step response of130. The unique global minimizers of |sigma_k(b_i)| are k_i=(5,8,5,6,5,5). The exact minima are the positive algebraic numbers s_i=|sigma_(k_i)(b_i)|. All response definitions, normalization, radial exponents delta=2/5, c=5/3 and the exact isolating intervals are those of130/133.

## Complete certificate argument

For every i retain a rational isolating interval I_i for b_i. Evaluate the polynomial sigma_(k_i) on I_i by rational interval Horner arithmetic. Its interval excludes zero; let e_i be its constant sign. Thus s_i=e_i sigma_(k_i)(b_i)>0. For every2<=k<K other than k_i, exact interval evaluation must give a strict gap between the lower bound for |sigma_k| and the upper bound for e_i sigma_(k_i). These finitely many inequalities prove strict minimality below K. Use direct response polynomials up to10 and the generic rational formula above10.

For k>=11 the proved stable-frequency formula is sigma_k=N(k,b)/D(k), with N polynomial in k,b and D polynomial in k only. Let e_infinity be the sign of its nonzero limiting response on I_i. Choose an integer K>=11, write k=K+t, and check that every coefficient of D(K+t) is positive. Check also that each coefficient, as a polynomial in t, of

    e_infinity N(K+t,b)-e_i sigma_(k_i)(b)D(K+t)

has a strictly positive rational interval lower bound for every b in I_i. Consequently this expression is strictly positive for every real t>=0. Since D>0 there, e_infinity sigma_k>s_i>0 at b_i. It follows at once that the sign of sigma_k is e_infinity and that |sigma_k|>s_i for every integer k>=K. Combining with the finite list proves unique global minimality over all k>=2. It also gives rational lower bounds on s_i suitable for the already proved majorant131 and component certificate134.

Every polynomial shift uses exact binomial coefficients and rational arithmetic. Interval Horner multiplication takes all four endpoint products, so the negative first root is treated correctly. No positivity claim about an unevaluated coefficient or inference from a finite long sample is needed. Dependencies are the independently reproduced response formulas130, the exact root certificates133, and elementary polynomial positivity on a nonnegative ray. A failure of this chosen positive-coefficient certificate would not by itself refute the proposed minimum.

## Completed certificate

Every tail starts at K=11 and all30tail coefficient lower bounds per root are strictly positive. Every finite gap is strict. Thus the six minima are attained uniquely at the stated indices over all integers k>=2. Decimal values below are approximate; the exact minima are the signed algebraic polynomial values and their rational enclosing intervals in verification/checks.json.

| Root | Unique minimizing k | Minimum, approximate | Certified uniform lower bound |
| --- | --- | --- | --- |
| 1 | 5 | 0.4013105971105664 | 401/1000 |
| 2 | 8 | 2.177019704309086e-06 | 217/100000000 |
| 3 | 5 | 0.0001581860941501006 | 79/500000 |
| 4 | 6 | 0.0004178288358760034 | 417/1000000 |
| 5 | 5 | 0.001152157295351338 | 23/20000 |
| 6 | 5 | 0.006849248686871733 | 171/25000 |

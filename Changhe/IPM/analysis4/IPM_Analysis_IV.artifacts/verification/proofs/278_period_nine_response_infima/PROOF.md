# Global response infima at the ten period-nine roots

Status: PROVED, independently reviewed and admitted in V569 on 2026-10-31T20:26:57+00:00. The proof preceded computation and every required inequality passed. No floating-point sample establishes a global infimum.

## Statement and notation

Set delta=2/9, c=9/7 and f_1=sin(theta)+b sin(3theta). Let b_1<...<b_10 be the ten real roots of the irreducible compatibility polynomial P_18 from topic267. Let sigma_k(b) for integer k>=2 be the affine response defined and independently reconstructed in277. Write sigma_infinity(b)=lim_(k->infinity) sigma_k(b). All amplitudes in this statement are one.

The exact conclusion is that the unique minimizing indices for |sigma_k(b_i)|, in increasing root order, are

    8, 7, 4, 7, no finite minimizer, no finite minimizer, 9, 9, 8, 8.

At roots5 and6 the infimum is |sigma_infinity(b_i)| and is not attained at a finite index. At every other root the infimum is the positive value at the stated index. The finite decimal values in a receipt are enclosures for these algebraic quantities, not their definitions.

The prerequisites are the exact root isolation in267 and the exact response identity in277. For k>=19 it supplies sigma_k(b)=N(k,b)/D(k), where D is monic of degree89 and N has degree at most89 in k and at most9 in b. The small responses sigma_2,...,sigma_18 and sigma_infinity are rational polynomials of degree9 in b. No producer floating-point recurrence is used in this check.

## Positive polynomial certificate for the infinite tail

For one root b_i, let I_i be its closed isolating rational interval, and let e_i be the sign of sigma_infinity throughout I_i. If the proposed minimum occurs at k_i, define T_i(b)=s_i sigma_(k_i)(b), where s_i is the constant sign on I_i. Otherwise define T_i(b)=e_i sigma_infinity(b). Require T_i to be strictly positive on I_i. In the finite-minimum case require |sigma_infinity(b)|>T_i(b) on I_i.

Define the exact rational polynomial

    P_i(k,b)=e_i N(k,b)-T_i(b)D(k).

Choose an integer K_i>=19. Substitute k=K_i+x in D and every b coefficient of P_i using exact polynomial arithmetic. Require every coefficient of D(K_i+x) to be strictly positive. Require every nonzero polynomial coefficient of P_i(K_i+x,b) in x to have strictly positive lower interval bound for all b in I_i. Coefficients which vanish identically as rational polynomials are allowed, but the constant coefficient must be strictly positive. The test for an identically zero coefficient is exact, before interval evaluation.

For every real x>=0 and b in I_i, these inequalities imply D(K_i+x)>0 and P_i(K_i+x,b)>0. Since T_i(b)>0, they imply e_i sigma_(K_i+x)(b)>T_i(b)>0. Consequently |sigma_k(b_i)|>T_i(b_i) for every integer k>=K_i. The certificate does not assert that sigma_k is monotone in the tail; the comparison alone is sufficient.

## Finite comparison and attainment

Evaluate each exact small or generic response polynomial at I_i for integers2<=k<K_i. Prove its sign is fixed and |sigma_k(b)|>T_i(b) for every k other than the proposed minimizing index. At that index the defining algebraic equality is exact. These finitely many strict inequalities and the tail certificate prove uniqueness of a finite minimizer.

For roots5 and6, every finite response has modulus strictly greater than T_i(b_i). The rational expression from277 tends to sigma_infinity(b_i), whose modulus is T_i(b_i). It follows directly from the definition of infimum that the positive global infimum is T_i(b_i), with no finite minimizer.

For the separate finite claim through index2000, an attained global minimizer already lies in this range. For roots5 and6, compare the directed value at2000 with every earlier integer2 through1999. Strict interval comparisons certify that the finite minimum occurs at2000. This finite check is independent of the infinite-infimum argument and is explicitly counted in the receipt.

## Arithmetic and scope

Exact rational polynomial composition produces the shifted coefficients. Directed interval Horner evaluation contains each coefficient for the entire closed rational root interval. A strict positive lower endpoint certifies its sign. Unresolved signs fail the proposed certificate; they are not replaced by rounded midpoint signs. Store the candidate indices, shifts, root intervals, coefficient bounds, exact-zero indicators, finite comparisons, input hashes and actual elapsed time.

This proves a global minimum or infimum of the affine response sequence at each fixed algebraic root. It does not determine the growth of the tuned harmonics, the sharp convergence boundary of the density series, or a whole-plane extension. Previously admitted sufficient convergence radii remain valid without any use of these sharper infima.

# Exact global response infima at period ten

Status: PROVED in V589, admitted 2026-10-31T21:23:49+00:00, within the exact scope below.

## Statement and definitions

Set delta=1/5, c_l=5/4 and f_1=sin(theta)+b sin(3theta). Let b_1<...<b_14 be the fourteen simple real compatibility roots from281, and let sigma_k(b), k>=2, be the affine response defined and exactly reconstructed in282. Put sigma_infinity(b)=lim_(k->infinity)sigma_k(b). Amplitude is one throughout.

For each root, the intended conclusion is either a unique finite minimizing index k_i, or the nonattained global infimum |sigma_infinity(b_i)|. The exact candidate and its definition are recorded in the certificate. A finite sample only proposes a candidate. No global claim is made unless the following proof applies.

## Complete proof criterion

Let I_i be the closed rational isolating interval for b_i. For k>=21 use the exact rational expression sigma_k=N(k,b)/D(k), with the normalized monic denominator D of degree109 and numerator degree at most109 in k and at most10 in b. For 2<=k<=20 use the independently computed rational response polynomials. The scalar in the factored denominator is absorbed into N when making D monic; both are taken from the reduced response record.

Choose T_i(b) to be either eta_i sigma_(k_i)(b), with eta_i its fixed sign on I_i, or e_i sigma_infinity(b), where e_i is the fixed limiting sign on I_i. Prove T_i>0 throughout I_i. In the finite case, also prove |sigma_infinity|>T_i. Form the exact polynomial

P_i(k,b)=e_i N(k,b)-T_i(b)D(k).

For a finite integer K_i>=21, expand D(K_i+x) and P_i(K_i+x,b) in powers of x. Verify that every coefficient of the first is strictly positive. Each nonzero coefficient polynomial of the second must be strictly positive on the entire I_i, and its constant coefficient must be nonzero. Exact zero coefficients are allowed. For x>=0 this proves D>0 and e_i sigma_(K_i+x)>T_i>0. Consequently |sigma_k(b_i)|>T_i(b_i) for every integer k>=K_i. The implication uses polynomial positivity only; it does not assume monotonicity of the response sequence.

For every integer 2<=k<K_i prove that sigma_k has a fixed sign on I_i and that its modulus exceeds T_i throughout I_i, apart from the proposed defining equality at k_i. In the finite case these comparisons prove a unique global minimum. In the limiting case they prove that every finite modulus strictly exceeds T_i, whereas the rational expression tends to a value of modulus T_i. Thus T_i is the global infimum and is not attained.

## Arithmetic and verification

A directed sample through index3000 and the limiting response may propose k_i or the limiting case. It has no role in the infinite proof. Exact rational polynomial shifts and directed1024-bit Horner evaluation implement the criterion. Every strict sign and exact-zero assertion is retained, together with source hashes, root intervals, counts and real elapsed time. The admission rechecks source hashes and all saved inequalities at increased precision. A failed positivity or finite-comparison check leaves that proposed conclusion open.

## Dependencies and scope

The exact polynomial and root data are281. The rational response identity, small responses and nonzero limiting polynomials are282. This specializes the elementary certificate argument independently reviewed in278. A response minimum supplies a possible denominator bound for a convergence majorant, but does not determine the growth of its numerator, the sharp density convergence boundary or a global stationary extension. No explicit exterior radius follows from this certificate alone.

## Completed verification

The fourteen ordered roots have global minimizing indices [9, 9, 8, limit, 8, 4, 7, 7, limit, 9, 9, limit, 9, 9], where limit means a positive nonattained limiting infimum. Exact shifted-polynomial positivity and all smaller integer comparisons pass. A separate1536-bit replay reconstructs every comparison polynomial: 1537 positive tail coefficients, 3 exact zero leading coefficients, 255 strict finite comparisons and 11 defining equalities. Producer computation took4.837315seconds and the independent algebraic replay took0.430268seconds.

The global response-infimum statement is PROVED. Neither tail monotonicity, an eventual coefficient growth rate nor a sharp exterior radius is asserted.

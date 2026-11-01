# Exact minimum of the tuned resonance responses

Status: PROVED. The complete argument and finite certificates were independently reviewed and confirmed by the theory part at2026-10-31T10:07Z. Exact hypotheses and scope remain as stated below.

## Statement and arithmetic hypotheses

Let b be either of the two real roots of the sextic P6 in topic119, and let sigma_k(b), k>=2, be its independently derived cubic resonance responses. Write sigma_k=N(k,b)/D(k) for k>=7, with the exact numerator and denominator of119. Let I be an exact rational isolating interval for b. Assume the following finite rational inequalities hold on I:

1. sigma4<0.
2. For k2,3,5,6, verify a constant sign for sigma_k and |sigma_k|+sigma4>0. In the positive case this is sigma_k+sigma4>0; in the negative case it is sigma4-sigma_k>0.
3. Every coefficient in t of D(t+7) is positive.
4. Every coefficient in t of sigma4(b)D(t+7)-N(t+7,b) is positive.

Then

    inf_(k>=2) |sigma_k(b)| = -sigma4(b)>0,

and the minimum is attained only at k4. In particular the uniform response bound in TheoremT can use this exact positive algebraic number.

## Proof

The first hypothesis identifies |sigma4|=-sigma4. The second gives |sigma_k|>|sigma4| at each remaining small index. For k>=7 set t=k-7>=0. The third hypothesis makes D(k)>0. The fourth, evaluated at nonnegative t, implies sigma4 D-N>0. Divide by D to obtain sigma_k<sigma4<0. Thus |sigma_k|>|sigma4| for every such k. These alternatives cover all k>=2 and prove the claim, including uniqueness.

To make the check exact, expand each expression as a polynomial in b. All isolating endpoints are positive. A polynomial sum c_j b^j has a rational lower bound formed by replacing b^j by the lower endpoint power when c_j>=0 and by the upper endpoint power when c_j<0. Upper bounds reverse these choices. Positivity of these computed lower bounds proves the stated interval inequalities. A Sturm variation drop of one certifies the root in each I. No finite scan over k is used for the infinite conclusion.

Dependencies: the exact response formula and real-root isolation in topic119; elementary polynomial positivity. The certificate must retain every rational lower and upper bound and all small-index comparisons. The certificate passes for both roots, with all24 tail-coefficient lower bounds strictly positive and all8 small-index modulus gaps strictly positive. The minima are enclosed by 3.8124461471579738967812172858936328046129831204856710313889347431e-5 +/- 6.90e-71 and 0.0015683872596407812855005339801904926709747880298726108994068286633 +/- 4.45e-68. The authoritative balls are in verification/checks.json. The mathematical conclusion remains proposed until independently reviewed.

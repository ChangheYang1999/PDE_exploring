# Exact angular coefficients and two review notation corrections

Date 2026-10-22T02:21:16.172411+00:00. This addresses only the wording of the complete actual follow-up review585d22d2-7263-46f6-9dfb-7199f0eedc4b. The proof and executed code remain unchanged.

The review writes "m alpha + q - 1 = 0 and m beta - p - 1 = 0" for the angular coefficients. Taken literally, this is false with p,q as defined in PROOF.md. The correct equations are

    m alpha + d q - 1=0,
    m beta - d p - 1=0,      d=beta-alpha.

Indeed F'/F=-p tan(theta)+q cot(theta) on the first quadrant, so

    (T_m F)/F=(m alpha-1+d q)cos^2(theta)
                  +(m beta-1-d p)sin^2(theta)=0.

The reflection extension gives the same identity on every open quadrant. Since d q=1-alpha m and d p=beta m-1, both coefficients vanish exactly. In compute.py and independent.py, the polynomial variables named qn and pn are these NUMERATORS d q and d p. The checked polynomial identities m alpha+qn-1=0 and m beta-pn-1=0 are therefore correct. No code or stored result uses the incorrect unscaled equations in the review prose.

The same review refers to the operator acting on "r^m |x|^p |y|^q". The actual homogeneous function is H=|x|^p sign(y)|y|^q=r^m F(theta), of degree m, without an additional radial factor. The proof states this correctly. These two review notation errors do not affect the norm estimates, Green moment cancellation, Gram argument, actual input enclosures or exact counterexample in REVIEW_RESPONSE.md. I do not accept the erroneous review formulas as claims.

The review's statement that r^(9-2m) is integrable exactly for m<=4 applies to this majorant. From an upper O(r^(9-2m)) bound alone one cannot infer divergence of an actual image for m>=5. Its explicit refusal to make a conclusion at m>=5 is retained. Our counterexample asserts only membership at m=3,4. No higher-m nonmembership is claimed.

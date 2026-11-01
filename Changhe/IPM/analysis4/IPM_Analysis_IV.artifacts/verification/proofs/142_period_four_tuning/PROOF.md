# The first obstruction and resonant responses at period four

Status: PROVED. V278 confirms the independent Cartesian formulas, exact root and irreducibility certificates, and comparison with the theory part Fourier formulas. Quantitative radii are treated separately in143.

## Objects and finite claims

Set delta=1/2, c=2, p_n=1-n/2 and f_1=sin(theta)+b sin(3theta). The first stream resonance is n=8 at angular frequency2. With the nonresonant stream inverse at earlier orders, let O8(b) be the coefficient of sin(theta) in f_8. The first compatibility condition is O8(b)=0. This polynomial has rational coefficients and degree at most8.

For k>=2 set n=4k and let e_k=sin((2k-2)theta) be a unit free stream mode at order n. Holding earlier tuned coefficients fixed, differentiate the next four density coefficients with respect to this free coefficient. Write these responses as phi_1,...,phi_4. For r=1,...,4 they satisfy

    lambda_(n+r) phi_r = T_(n,r)(e_k,f_r)
       + sum_(s=1)^(r-1) [T_(r-s,n+s)(g_(r-s),phi_s)
                          +T_(n+s,r-s)(Pi_(n+s) phi_s,f_(r-s))],

where lambda_m=m-1 and T is the Cartesian advection bilinear form. Set sigma_k equal to the sin((2k-1)theta) coefficient of phi_4. The next compatibility obstruction is affine, R_k+sigma_k H_(4k). These definitions agree with130 and the general period theorem131 at Q=4. The intermediate orders n+1,n+2,n+3 are nonresonant in the even stream-frequency class, including the odd-integer radial exponent at n+2.

## Complete derivation and certificate method

Use the signed Laurent Cartesian representation of128. Starting from f_1, ordinary interval-free rational arithmetic constructs

    f_n=(n-1)^(-1) sum_(i+j=n) (Xg_i Yf_j-Yg_i Xf_j).

Applying -Delta to each computed stream term recovers partial_x rho. This checks the Poisson sign without using the source sine-product formula. Up to7 all even-mode Poisson denominators are nonzero; at8 only the sin(theta) density coefficient determines the resonant forcing. Every field has the required odd sine symmetry and bandwidth at most4n-1. Bilinearity proves degree at most n in b, hence the stated degree bound for O8.

To differentiate in H_n, two factors depending on H_n would first have total order at least2n+1, which is larger than n+4 for n>=8. The dependence through n+4 is therefore affine. Differentiating the ordered bilinear sums gives precisely the four displayed response equations, with no omitted orientation. The low-order fields f_1,...,f_4 and g_1,...,g_3 suffice. The resulting response is a polynomial of degree at most4 in b.

For k>=9 all signed frequencies stay away from zero and from changes of absolute-frequency branch: the greatest possible offset from2k-2 through four response steps is4*4-1=15, and2k-2>=16. Consequently symbolic arithmetic in rational functions of k computes one exact formula N(k,b)/D(k) valid throughout this range. Direct responses at the endpoint and subsequent integer values provide additional checks. Finite lower values of k are computed separately so that omitted zero modes and folded frequencies are handled exactly.

If the primitive obstruction polynomial is irreducible over Q with degree greater than4, every nonzero response polynomial of degree at most4 is nonzero at any of its roots. The same holds for a nonzero limiting response polynomial of degree at most4. The finitely many low responses and the common coefficient gcd of N in b decide whether any response polynomial is identically zero for an integer k>=9. A finite nonzero limit together with nonvanishing at every integer gives a positive response infimum, so131 and132 would then prove a compatible convergent exterior solution for each real root. The certificates below verify every premise. A zero limit would require a different argument and is not concealed by finite tests.

## Dependencies and evidence

The recurrence and Cartesian operators are the independently checked ones of01,119and128. The affine period argument is130, the conditional convergence theorem131, and the common potential theorem132. Exact JSON records the obstruction, low-order fields, small responses, symbolic response and limits. Source files and actual timings accompany the output. This finite calculation does not prove a global stationary extension.

## Completed theorem and exact certificates

Let P8 be the primitive integer polynomial with positive leading coefficient proportional to O8 defined above. It has degree8 and exactly six simple real roots. They lie in the respective open rational intervals

    (-280,-279)/1000, (39,40)/1000, (77,78)/1000,
    (187,188)/1000, (351,352)/1000, (626,627)/1000.

For each exact root b_i and each real epsilon!=0, the leading profile epsilon[sin(theta)+b_i sin(3theta)] admits a unique pure S1 density/stream series with every compatibility obstruction cancelled by its harmonic stream coefficient. The series and every weighted derivative converge absolutely and uniformly on a sufficiently large closed exterior. They give a smooth stationary self-similar IPM solution at c=2. The common potential has the same strict geometric radius and logarithmic corrections only at orders4and8. The sufficient radius scales as |epsilon|^2. No global stationary extension is claimed.

To prove the algebraic premises, the rational Cartesian recurrence computes all28ordered products and seven Poisson identities exactly. The primitive O8 polynomial has the leading coefficient82668272572218361620942808786146; its full exact coefficient array is in verification/root_response_certificates.json. An independently implemented primitive Sturm chain has variations7and1at the two infinities, and drops by exactly one on each of six disjoint rational isolating intervals. This proves the exact real-root statement without using floating approximations.

Modulo5the polynomial factors into irreducibles of degrees2and6; modulo29it factors into irreducibles of degrees1and7. Exact multiplication checks both factorizations and independently implemented Frobenius power and gcd tests prove every modular factor irreducible. Since both primes preserve degree, any proper rational factor would have a degree that is a nonempty proper subset sum in both patterns. The first allows2or6; the second allows1or7. There is no common degree. Gauss's lemma therefore proves P8 irreducible over Q.

Every direct response k=2,...,11 is a nonzero polynomial of degree4. The stabilized numerator for k>=9 has common coefficient factor (k-1)(2k-1)^2 and no other common factor, so it is never the zero polynomial at an integer in that range. All roots of its denominator lie below9. Its limit is the nonzero quartic

    (12202257438 b^4-17091025028 b^3+8372349062 b^2
       -1322335916 b+60806735)/28049387520.

Irreducibility and degree8>4 imply that no finite response and no limiting response vanishes at any b_i. Since sigma_k(b_i) converges to its nonzero limit, its absolute value is bounded below on a tail and on the remaining finite set. Thus inf_(k>=2)|sigma_k(b_i)|>0. Theorems131and132 give all the asserted convergence and reconstruction conclusions. Homogeneity gives the amplitude scaling.

Finally, O8, the generic rational response and all direct responses2through11 agree exactly with the theory part's independent Fourier code. Its additional direct responses12through14 agree with the independent generic expression. The source output and hashes are retained. The exact computation took59.8696733seconds; the separate root, modular and cross-formula certificate took0.3085203426890075seconds.

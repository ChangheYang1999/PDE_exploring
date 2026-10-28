## Note 39 (2026-10-28T11:35Z): cross-read of the chordal periodic Hilbert note (V166): no error found

To the verification work. I read 04_literature/hilbert_chordal/PROOF.md (sha256 3581c67ca5cdc1450da02d301dc172cdbd92a0a56612269b8a730f4c4b003340)
against the saved source text sources/conjugate_sharp_2014.txt (Theorem 1(2), Remark 3). Every step checks:

1. Normalization. The source's conjugate function -(1/pi) pv int f(t)/(2 tan((t-x)/2)) dt equals (1/(2pi)) pv int f(t) cot((x-t)/2) dt,
   the note's H. The source formula is Omega~_0(omega,h) = (2/pi) int_0^{h/2} sin(h/2)/(cos u - cos(h/2)) omega(rho(u)-u) du.
2. Modulus. omega = (2 sin(t/2))^alpha on [0,pi], 2^alpha after: x^alpha is increasing concave and 2 sin(t/2) is concave on [0,pi],
   so the composition is concave; its left derivative at pi is alpha 2^{alpha-1} cos(pi/2) = 0, so the constant extension is
   concave; Dini since omega(t)/t ~ t^{alpha-1}. H^omega = unit ball of [.]_{alpha,ch}: for |x-y| <= pi the chord is
   2 sin(|x-y|/2) = omega^{1/alpha}; for |x-y| > pi the chord is at most 2; conversely reduce y mod 2pi to |x-y'| <= pi.
3. Substitution. With b = tan(h/4), u = 2 arctan(bs): cos u - cos(h/2) = 2b^2(1-s^2)/((1+b^2 s^2)(1+b^2)), sin(h/2) = 2b/(1+b^2),
   du = 2b ds/(1+b^2 s^2), so the kernel weight is exactly 2 ds/(1-s^2) and the prefactor becomes 4/pi. The antiderivative of
   2 ds/(1-s^2) is log|(1+s)/(1-s)|, so the matching equation of the source becomes (1+s_u)/(1-s_u) = (s_rho+1)/(s_rho-1), i.e.
   s_rho = 1/s_u, i.e. tan(rho/2) tan(u/2) = b^2, with 0 < s < 1 and rho = 2 arctan(b/s) in (h/2, pi). So rho-u is in (0,pi) and
   omega(rho-u) = (2 sin(arctan(b/s) - arctan(bs)))^alpha.
4. Q_b. sin(A-B) with tan A = b/s, tan B = bs is b(1-s^2)/sqrt((s^2+b^2)(1+b^2 s^2)); sin(2 arctan b) = 2b/(1+b^2); the ratio is the
   stated Q_b, and the output chord 2 sin(h/2) cancels the factor 2 of omega. The identity
   (s^2+b^2)(1+b^2 s^2) - s^2(1+b^2)^2 = b^2(1-s^2)^2 expands correctly (b^2 s^4 + b^2 - 2 b^2 s^2), so Q_b <= (1-s^2)/(2s) with
   the limit as b -> 0.
5. Integral. The dominating function 2^{-alpha} s^{-alpha} (1-s^2)^{alpha-1} is integrable for 0 < alpha < 1; with u = s^2,
   int_0^1 s^{-alpha} (1-s^2)^{alpha-1} ds = (1/2) B((1-alpha)/2, alpha), so the limit is (2^{1-alpha}/pi) B((1-alpha)/2, alpha); the
   duplication formula gives Gamma(alpha/2) Gamma((1-alpha)/2)/pi^{3/2}.
6. Suprema and complex inputs: increments with h in (pi, 2pi) reduce to 2pi-h by periodicity and the chord is symmetric; scaling
   reduces the ratio to the unit ball; the complex reduction by a unit multiple and real parts is correct (H is real).

Remarks, not errors: (a) the result depends on Babenko's Theorem 1(2), an announcement without proof in the source, as the
note says; (b) the sentence "their exact Hilbert operator constants are equal" relies on ../hilbert_periodic/PROOF.md (V050);
(c) the supremum is not attained at any fixed increment (Q_b < (1-s^2)/(2s) for b > 0), only approached as h -> 0, as stated.

If you record V166 as CONFIRMED, I will change Section 2 item 2 of the report: instead of "and it is not a statement for the
chordal metric" it will say that the same constant is the exact norm for the chordal seminorm |f(x)-f(y)|/|e^{ix}-e^{iy}|^alpha,
with the same dependence on Babenko's announced theorem.

Correction to Note 38: the a10v7 result will be Note 40 (p3 chunk r4096_6144 started 11:34:57Z, 5 chunks remain after it).


# Note 108-109 repairs and formatting audit

## 1. Frozen text and scope

This audit uses the report captured at 2026-11-03T19:35:23.270456+00:00, sha256 c8963e479699102a824f26f5c5d129ddc71f78a09d020e8fe40fbd587914b41d. this report and this report are identical. The independent splitlines count is 6592, while the coordinator's displayed map counts an additional trailing line. The README and theorem-attempt ledger are byte-identical to the previous audited pin. The obstruction ledger has the one LIT289 addition inspected below.

The mathematical changes are the supported-zero repair, the pressure-sign quantifier repair, the LIT289 insertion, and the corresponding references. Formatting is checked separately. This audit does not certify still-unread regions of the assembled report.

## 2. Supported nonzero-pressure zeros

The LIT288 application in Section 10 and its appendix row now requires a zero p of V in supp curl V, with k=0 and S>0 on a neighborhood of p. This is the exact condition needed to exclude the identically zero branch of the local theorem. On a connected small neighborhood the theorem says either V=0 identically, or all its zeros have finite order and the whole neighborhood is in the relative support of curl V. The supported-zero premise forbids the first alternative. The actual-tail law then gives order at least two, allowing the LIT286 Hessian test. Smoothness, global zero helicity and both natural bounds remain explicit or are inherited through the precise row cross-reference.

The text also records why support matters: locally take V=0, S=P2=Re(z^nu)>0 near z=x1+i x2=1, nu=-b/(c-i omega), with p1=0. This is harmonic and has X.grad S=-bS. Every remaining vector or next-scalar equation vanishes, but all velocity zeros are unsupported. The report treats this as a local countertest, not an actual global profile. The A2173 repair and A2174 explanation are confirmed.

The drift in the local scalar equation is now described as smooth and locally bounded, matching what S!=0 supplies on an arbitrary open G. It is not asserted to have one bound over a noncompact G.

## 3. Pressure means and the existential sign conclusion

The C60 appendix row now states T>0 at points arbitrarily close to x0 in the nonrotating zero-period case. This matches A2130: there is no claim that T is positive throughout a punctured neighborhood. The whole-circle condition that gives zero period is retained. The main Section 10 paragraph already had this quantifier.

The row also records that T<=0 implies positive spherical means, while a converse from the scalar Poisson identity is refuted by A2161 and a full-system converse remains open A2162. No converse is used in the report. These statements are consistent with the smooth flat scalar countertest P=exp(-1/r^2)(1+2x3/r), which has positive spherical means and both signs of -Delta P. That scalar is not asserted to solve the full reduced system.

## 4. The exact axial LIT289 family

The new paragraph, appendix row and obstruction-ledger addition all retain the exact axial LIT287 Cauchy data. For n=N+1>=3 and lambda=b/c in (2,3), f(u,0)=u^n/n, f_v(u,0)=0, h(u,0)=1-lambda(lambda+1)u^2/4 and h_v(u,0)=0. The forced fourth coefficient is lambda(lambda+1)(lambda+2)(lambda+3)/64-delta, with delta=1 for n=3 and zero otherwise. The next-scalar source has an uncancellable mode |n-4| at degree n, so no C1 scalar solves all three next equations. This matches A2154-A2158.

The actual-profile consequence retains full momentum, divergence, zero helicity, natural bounds and the supported-zero context; the nonresonant and averaged scalar constructions are inherited from the preceding LIT286 row. Other pressure data and off-axis members remain open in this pin. The subsequently confirmed LIT290 improves a restricted part of those alternatives but is not yet inserted here. No general positive-pressure arc exclusion is asserted.

## 5. Formatting preserves the audited mathematics

An independent comparison of Sections 2A, 2B, 2C and 2D against the previous ba3784e4 pin finds identical whitespace-delimited token sequences. Section 2D is byte-identical; the other sections move line breaks around operators. The Section 7 rewrite also has exactly the same token sequence. Thus A2148-A2152, A2142-A2146, A2040-A2043 with A2062, and A2072-A2076 transfer at their exact scopes. The displayed differences were inspected, including all eleven lines whose leading comparison sign or plus sign could be read as Markdown syntax.

The coordinator's intermediate repaired pin aa0eb697 was independently compared to the frozen current report with a linear token comparison that preserves internal punctuation and case. After discarding only list markers and punctuation at token edges, both have 161310 tokens. All 23 differences are the assembly timestamp and 22 capitalizations of ordinary prose at the starts of newly separated list items. No variable, exponent, inequality sign or word changes in that comparison. The current Section 10 was also read in full, so the confirmation does not rely on punctuation normalization alone.

A first attempt used a general sequence matcher with automatic filtering disabled; it was terminated as unnecessary. Its affinity was CPU55 and its nice value was 19. The replacement linear comparison took 0.1196223208680749 actual seconds. This is file comparison evidence, not a numerical proof or a new mathematical test.

## 6. Remaining work and verdict boundary

The preamble, summary, notation, main theorem section and proof guide of the ba3784e4 pin have now been read completely, as have the current full Section 10 and the changed appendix rows. The foundational Sections 2A-2D have complete independent audits and the token identity above. Coverage progress is retained in the separate assembly-coverage folder.

Whole-report approval remains OPEN. In this c8963e47 pin, Theorem 3(g) and the formal-Lyapunov appendix row still refer to the unshifted H at omega=0, refuted by A2177. They need the corrected H0 and an explicit nonpositive formal derivative, as proved in A2178. Remaining Sections 3-9 and Appendix A/B coverage must also be completed. The unrestricted nonexistence conjecture is not certified. These repairs and formatting checks do not change that verdict.

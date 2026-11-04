# Report assembly 78e4ddbd at cutoff A3165

## 1. Exact object and comparison method

This audit covers the front matter, main Sections 0-10 and Appendix A of SHA256 78e4ddbdec084779b60688b6ec1e48c7e4e5870c4ccaaccfdb0d404ef7eca443, assembled at 10:27Z, with 8053 newline-terminated lines and 1279160 bytes. Its cutoff is A3165. The preceding report 32c9fd3c was approved in A3164 at cutoff A3160. The complete old and new bytes are retained in verification, together with the declared 145-line normal diff fa9bd013 and an independent unified diff.

An initial comparison of the two tools' added and removed line sequences failed because they grouped repeated lines differently. The stronger check parsed each of the eleven normal-diff commands, verified its removed text against the old file, and applied it. The reconstructed bytes exactly equal the submitted report, with the stated SHA256. All declared changes and their surrounding mathematical statements were read, including the full long table rows. No unlisted change is inferred from either diff's grouping.

## 2. Mathematical transfers

Theorem 8(p) transfers A3161-A3162 with the exact kinematic hypotheses: U is C^1, divergence-free, E(R)/(L R^beta) tends to 1, L>0 and 0<beta<1. Put t=(beta-3)/2, k=(beta+1)/2, m=2-beta and H=t^2(k^2+4)/(k^2+2). The normalized endpoint constants are

    C_s=m t^2/(k^2+2),
    C_n=2k t^2 sqrt(k/(k+3))/(k^2+2), C_p=C_s+C_n.

These are exactly the three endpoint limits in 8(o). With G_a the integral of |y-a|^(2-beta)|DU|^2 over 1<|y-a|<R, a budget limsup G_a/(beta L log R)<=H+delta, 0<=delta<=beta, gives the stated lower and upper bounds C(1-delta/beta)-e_beta(delta) and C+e_beta(delta), where

    e_beta(delta)=sqrt(10delta/beta)(sqrt(H+delta)+sqrt(H)).

I_a and N_a take the positive and negative parts of q=tr((DU)^2) before angular integration. J_a takes the positive part of the spherical integral. The distinction is explicit and essential. The negative pointwise moment has liminf at least 1/16 for delta<=beta/10000. Its vanishing logarithmic liminf implies limsup G_a/(beta L log R)>=H+zeta_beta, allowing infinity, with zeta_beta the root stated in the report and zeta_beta>beta/10000. No finite-gradient assumption is needed in the already-infinite case. A bounded N_a, in particular exterior pointwise q>=0, supplies this premise. Positivity of only the spherical mean does not.

The amplitude D in 8(o) is the full spatial limsup of |y|^((5-beta)/2)|DU(y)|, allowing infinity. For finite D, eventual spherical integration gives limsup G_0/log R<=4pi D^2, so D^2>=beta L(H+zeta_beta)/(4pi); the infinite case is immediate. A3162 permits the same gradient limsup at every fixed center, with the same L. The clause added to 8(n) transfers exactly that fact.

For the profile application the report keeps bounded U, U and P in C^1, the full equation, and distributional blow-down U(R.) tending to zero. A3053 supplies beta=5-2/c in the target range. Hence 2-beta=2/c-3 and (5-beta)/2=1/c, verifying every weight and exponent in Theorem 3(p). This application is valid for every finite omega. Its extra source and gradient premises are retained; no derivative bound is inferred from velocity decay.

The outline correctly cites a mean-square matrix error of at most (10delta/beta) beta L log R, a frozen degree-one energy of at least (1-delta/beta) beta L log R, and o(log R) remainders. The trace inequality and Cauchy-Schwarz give the displayed error. The two cutoff families are needed for opposite bounds and do not assume control of derivative energy on boundary strips.

## 3. Source versions and scope language

The LIT384 pronoun is clarified to say that positive exterior source is compatible with the energy ratio. Its status-only current version e322fa77 is accurately credited to A3165. The preceding strict amplitude result in 8(o) has no explicit unconditional gap at this cutoff; the new 8(p) gap has the extra negative-source premise. Reading the sentence in 8(o) in that local scope is consistent. An optional future clarification is to say explicitly "No explicit unconditional gap is proved here" until LIT385 is decided.

The current LIT386 source has SHA256 b453b1e9b869d881f6419fd126fadca55c2cd19fe53d293010e80bc5caf4933b. Its complete difference from the retained bef4f788 source changes only the status sentence to A3161, A3162 and A3163. No hypothesis, calculation or proof changes. The report accurately cites the originally reviewed version.

The new Section 5 paragraph and Appendix A row preserve the distinction between conditional consequences and automatic hypotheses. The front matter correctly credits A3164 for the 10:19Z assembly at cutoff A3160. The new history is consistent. The submitted object has zero NUL bytes, zero em-dash characters and zero prohibited absolute local path prefixes; the two changed table rows each have six delimiter characters. These are file checks, not mathematical evidence.

## 4. Conclusion and limitations

The new transfers are faithful at cutoff A3165. Cumulative approval covers exactly the front matter, main Sections 0-10 and Appendix A of 78e4ddbd, using A3164 for unchanged material. Historical Appendices B and C are not collectively certified. Subsequent changes require their own check.

The source-status revision preserves A3161-A3163 without enlarging them. No optimal constant, automatic source premise, automatic finite gradient budget, or unrestricted rotating nonexistence theorem has been established. The main arbitrary-omega conjecture stays open. No mathematical script or formal build was executed in this review.

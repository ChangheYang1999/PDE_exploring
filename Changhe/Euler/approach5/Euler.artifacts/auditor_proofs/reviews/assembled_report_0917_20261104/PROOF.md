# Report6dd51f88: corrected localization and pointwise-source sharpness

## 1. Exact object and approval scope

This audit concerns the retained report in the team records, SHA256 6dd51f888db7e34d3d45279ace06eb02fe60bca4978df5072018797aa2044439, with7750 lines and1225451 bytes. At capture it agreed byte for byte with both coordinator report copies and the Theory Agent A pin. The complete175-line unified difference from report8534ae9c was read, including its long table rows in a separate untruncated display. The new claim contexts in the front matter, Theorem3(m), Theorem8(l), its proof outline and the ledger were read.

The prior approved assembly is report86286d44, A3083, at cutoffA3077. The intermediate reports b2d9c61c and8534ae9c were checked separately; their requested corrections are preserved in the team records and in the team records. The present verdict is cumulative for the front matter, sections0-10 and AppendixA, at the present report's cutoffA3120. It does not collectively certify historical AppendicesB/C, a future revision, or an unreviewed source theorem. No claim is made that every unchanged line was reread in this pass.

## 2. Localized convexity correction

For 0<beta<1 let m=2-beta and f(y)=|y|^m. The uncut weight is C1, locally W^(2,1), and

    D^2f=m r^(-beta)(I-beta e_r tensor e_r).

It is convex because its radial and tangential eigenvalues are m(1-beta)r^(-beta)>0 and mr^(-beta)>0. For a smooth radial cutoff 0<=chi<=1 equal to1 on B1 and0 outsideB2, the localized weight f chi(y/R) is not convex. A globally convex compactly supported function on R3 is zero, by restriction to each line. Its extra Hessian terms are

    grad f tensor grad chi_R + grad chi_R tensor grad f + f D^2chi_R.

They are supported on R<r<2R and bounded by C R^(-beta). For a C1 divergence-free U and q=tr((DU)^2), the distributional identity q=partial_i partial_j(U_i U_j) gives their pairing error at most C R^(-beta)E(2R). Approximation in local W^(2,1), with U bounded on compact sets, justifies the uncut singular Hessian at the origin. The report now states exactly this separation in its proof outline and LIT374 row. Thus the localized-convexity error refuted in A3116 has been corrected.

## 3. Additive signed-pairing correction

Let E(R)=int_(|y|<R)|U|^2 and F(R)=int_(|y|<R)r^(-beta)|U|^2. Since E(r)=O(r^3) near0,

    F(R)=R^(-beta)E(R)+beta int_0^R r^(-beta-1)E(r)dr.

The ratio E(R)/(LR^beta)->1 gives F(R)=beta L log R+o(log R). The stronger remainder E(R)=LR^beta+O(R^(beta-1)) gives F(R)=beta L log R+O(1), because its integrated tail error is O(int_1^infinity r^(-2)dr). With the annular cutoff error retained, the compact signed pairing lies between m(1-beta)F(R)-C and mF(R)+C. Therefore the stated coefficients have bounded additive errors only under the stronger energy law. The revised statement and ledger now distinguish these hypotheses explicitly.

The displayed countertest is also correct. A tangential radial swirl may be chosen with E(R)=LR^beta(1+(log R)^(-1/2))+O(1) for large R. The derivative of the prescribed energy is positive eventually, so its amplitude is well defined and smoothly extendible across an inner ball. Because U_tan=U, its compact pairing is mF(R)+O(1), hence

    beta m L log R+2beta m L sqrt(log R)+O(1).

This violates a bounded upper additive error under the ratio premise alone. The countertest is kinematic and is not called an Euler profile. The second A3116 correction is complete.

## 4. Sharpness and tangential fraction

The new LIT377 material faithfully transfers A3118-A3119. For every beta in (0,1), L>0 and epsilon>0, a smooth uniformly decaying divergence-free control has exact origin energy LR^beta after radius2, shifted energy LR^beta+O_a(R^(beta-2)), a smooth Poisson pressure, and pointwise positive-source coefficient less than k_beta+epsilon, where k_beta=beta m(1-beta). Its compact swirl core equals a0 Jy with a0!=0 on a ball. The full rotating momentum residual there has curl2a0 e3 for every real c and omega, so no pressure makes it a full profile. This proves a kinematic infimum, without claiming actual-profile optimality or single-field attainment at this cutoff.

The spherical positive-source moment is at most the pointwise positive-source moment, because [int_S2 q]_+ <= int_S2[q]_+. Together with the common lower bound this also prevents raising the spherical coefficient, if Theorem3(m)'s sentence is read as applying to both displayed moments. The stronger separate LIT376 result was not needed for this implication and is not imported into this cutoff.

Here H_a(R)=int_(1<|y-a|<R)|y-a|^(2-beta)[q(y)]_+dy, F_a(R)=int_(2<|y-a|<R)|y-a|^(-beta)|U(y)|^2dy and F_tan,a(R) is the same integral with the squared component tangent to the spheres centered at a. The retained tangential term is beta m F_tan. Dividing

    H_a(2R) >= m(1-beta)F_a(R)+beta m F_tan,a(R)-C

by log R and using F_a(R)/(log R)->beta L shows that limsup H_a(R)/(L log R)<=k_beta+epsilon implies

    limsup F_tan,a(R)/F_a(R) <= epsilon/(beta^2 m).

The report states a logarithmic energy fraction, not pointwise radiality. Including or excluding a fixed inner ball changes these moments by O(1), so its two notational conventions agree at the coefficient level.

## 5. Other transfers and remaining scope

The critical weight 2/c-3 and radial weight 2/c-1 are respectively 2-beta and4-beta for beta=5-2/c. The exact pressure conversion remains

    (r^2 Pbar_a')'=-r^2 Q_a/(4pi).

All source, gradient and work conditions remain additional assumptions when used for nonexistence. The earlier corrected constant-profile sentence remains unchanged. The natural derivative majorant alone supplies only a nonintegrable upper bound; the report does not use that upper bound to prove divergence. Its actual divergence conclusion uses the independently proved energy/source lower bound.

The ordinary omega=0 theorem and the conditional helicity/pressure theorems retain their previously approved hypotheses. No finite angular truncation, universal escape assumption, finite energy, derivative decay or pressure normalization is added silently. The main arbitrary-omega conjecture stays UNRESOLVED. The single-field attainment question remains open at cutoffA3120; the later LIT380 submission has no role in this approval.

## 6. Evidence and conclusion

A138, from the existing configured model agent, independently checked both corrections and the LIT377 transfer. Its complete note was read and compared with the actual pin, not accepted on trust. The prior C comparison is part of A3119. Actual provider execution is independently unattested. The mathematical checks above are analytic; file hashing, text comparison and structural scans are not numerical proof computations.

The complete delta and affected contexts agree with the confirmed dependencies. Report6dd51f88 is CONFIRMED as a cumulative mathematical assembly of its front matter, sections0-10 and AppendixA at cutoffA3120, preserving every conditional and open qualification. Historical AppendicesB/C are not collectively approved. The later ledger entries must be transferred and reviewed separately if the report changes.

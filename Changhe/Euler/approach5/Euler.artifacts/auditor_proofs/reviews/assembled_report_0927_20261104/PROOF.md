# Report eb89620e: source and gradient transfers with one scope correction

## 1. Object and coverage

The retained report in the team records has SHA256 eb89620ebf8237eba47c56c5992ff4f0123bc92705ddb10c6d79ec7b5dade603, 7842 lines and 1242704 bytes. At capture it equaled the two coordinator report copies and its coordinator pin. The full 237-line delta from report6dd51f88 has been read, with the long table rows displayed separately. The affected theorem statements and their surrounding hypotheses have also been read. The base report was approved in A3131 at cutoff A3120 for front matter, sections 0-10 and Appendix A. Unchanged material retains that scope; this pass does not claim to reread every unchanged line or collectively certify historical Appendices B/C.

The new transfers concern A3121-A3130. No later LIT379-LIT382 conclusion is imported into this report's cutoff. In particular its single-field attainment questions remain open at that cutoff even though a later construction is under review.

## 2. Spherical source coefficient and tangential fraction

Let U be a C1 divergence-free vector field on R3, let q=tr((DU)^2), let 0<beta<1, L>0, m=2-beta and K_beta=beta m(1-beta), and suppose E(R)=integral_(|y|<R)|U|^2=LR^beta+O(R^(beta-1)). For each fixed center a define Q_a(r)=integral_S2 q(a+r theta), with sphere measure 4pi, and

    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+ dr,
    F_a(R)=integral_(2<|y-a|<R)|y-a|^(-beta)|U|^2,
    T_a(R)=integral_(2<|y-a|<R)|y-a|^(-beta)|U_tan,a|^2.

Ball inclusions transfer the same energy remainder to every fixed center. For a smooth nonnegative radial f equal to r^m outside radius2, zero below radius1 and bounded above by r^m, its Hessian on r>2 is

    D^2f=m r^(-beta)(I-beta n tensor n).

The distributional identity q=partial_i partial_j(U_i U_j), tested against f chi(y/R), therefore gives J_a(2R)>=m[(1-beta)F_a(R)+beta T_a(R)]-C_a. The derivatives of chi contribute at most C R^(-beta)E_a(2R)=O(1), and each fixed-ratio annulus has bounded weighted energy. Replacing 2R by R consequently gives

    J_a(R)>=K_beta L log R+beta m T_a(R)-C_a.

Here F_a(R)=beta L log R+O(1) follows by integration by parts. With only E(R)/(LR^beta)->1, the error is o(log R), which yields the corresponding liminf statement.

If integral_2^infinity r^(4-beta)[-Q_a(r)]_+ dr is finite, the compact signed pairing differs from J_a(R) by O(1): its negative contribution is bounded, and its transition annulus is bounded by the signed Hessian identity plus that negative bound. Thus the displayed lower expression is an equality up to O(1) under the strong energy remainder. Under the ratio alone the explicit logarithmic expression has only an o(log R) error. The report's table A makes this distinction correctly. The prose in 8(l) should attach the words "under the stated remainder" to its O(1) sentence, since the intervening ratio clause otherwise permits an ambiguous reading.

A3121-A3122 construct smooth decaying controls approaching K_beta, and controls attaining the least coefficient beta m(1-beta+beta tau) at each prescribed logarithmic fraction T_a/(beta L log R)->tau in (0,1]. The report accurately keeps these kinematic, distinguishes pointwise positive part from positive part after spherical integration, and does not certify the full momentum equation for the mixtures. Its failure-of-momentum assertion for the poloidal approximating controls is the separately checked A3121 assertion.

## 3. Gradient coefficient and its localization

Write t=(beta-3)/2, k=(beta+1)/2 and H_beta=t^2(k^2+4)/(k^2+2). A3125 establishes for the same energy class

    G_a(R)=integral_(1<|y-a|<R)|y-a|^(2-beta)|DU|_F^2
          >=beta H_beta L log R-C_a.

The report's proof outline preserves the reason this applies despite an infinite weighted norm. In logarithmic radius z, U=r^t v, the weighted gradient is the integral of |v_z+tv|^2+|grad_S v|^2. Zero flux excludes the radial degree-zero mode. For every remaining spherical harmonic of degree ell, Lambda=ell(ell+1), divergence gives g=(f'+kf)/Lambda. The localized quadratic identity has nonnegative bulk coefficients, minimized at Lambda=2, and errors bounded uniformly in ell by the weighted energy on fixed-width end strips. Their O(1) bound uses only E(2R)=O(R^beta), not traces of DU. Finite-mode approximation and local H1 convergence justify C1 fields and the full angular sum. This is the localization proved in A3125, not a direct use of a finite-norm theorem on an infinite-norm profile.

A3129 checks that the known primary Hardy-Leray coefficients agree at gamma=1-beta/2 in their distinct classes. The report states the compact-support, symmetry and finite-norm distinctions and limits its primary-source approval to the checked theorem pages. It does not claim a new Hardy constant or a full-paper audit. The known smooth degree-one control has the exact energy law, attains the gradient coefficient, has a smooth Poisson pressure and fails full momentum because its core curl is 2a0 e3, a0>0, independently of c and omega. These are correctly transferred.

## 4. Full-profile consequence

For a bounded nonzero C1 velocity and C1 pressure satisfying the full rotating profile equation, divergence freedom, U(R.)->0 in distributions and 2/5<c<1/2, A3053 gives beta=alpha=5-2/c and L>0. Hence

    t=1-1/c, k=3-1/c, 2-beta=2/c-3,
    H=(1-1/c)^2[((3-1/c)^2+4)/((3-1/c)^2+2)].

If D is the limit superior at spatial infinity of r^(1/c)|DU|_F and is finite, then for each D0>D the eventual bound |DU|_F<=D0 r^(-1/c) implies G_0(R)<=4pi D0^2 log R+C. The lower bound gives D0^2>=alpha H L/(4pi). Taking D0 down to D proves D>=sqrt(alpha H L/(4pi))>0; an infinite D also satisfies it. Thus the extra condition DU=o(r^(-1/c)) forces U=0. No claim is made about every sphere or direction. The stronger conclusion D<infinity retains the separate C2 and DU=o(sqrt r) assumptions of A3102.

The conversion, the section 8 row and the summary's conditional label are correct. Boundedness, the distributional condition and the full PDE remain inherited from Theorem 8's heading; only the regularity is relaxed in part (m). The coefficient comparison H_beta-m(1-beta)>=11/12 is the analytic A3126 calculation, not numerical evidence. None of these steps restricts omega or assumes symmetry.

## 5. Required scope correction

Immediately after part (m), the report says: "No helicity, symmetry, decay rate or derivative decay is assumed." As a description of the enlarged Theorem 8, this is false: part (m) explicitly assumes DU=o(r^(-1/c)) for its nonexistence criterion, and separately assumes DU=o(sqrt r) for its finite-amplitude conclusion. The lower-bound portion of (m) needs neither assumption, but this does not make the criterion unconditional.

Replace that sentence, for example, by:

    No helicity or symmetry condition is imposed. Each part retains its stated additional hypotheses; in particular part (m) uses derivative decay for its nonexistence criterion. Proof outline.

Also make the finite-negative-source sentence of 8(l) explicitly read "under the stated energy remainder, the two sides differ by O(1); under the ratio alone the error is o(log R)." This is a clarification of its intended statement and agrees with its table A row. The preceding 6dd51f88 approval is not an approval of the new unqualified scope sentence after a derivative criterion was added.

## 6. Verdict boundaries

The mathematical transfers of the source and gradient bounds, sharp kinematic controls, primary-source scope and conditional profile criterion are confirmed at the exact hypotheses above. The unqualified no-derivative-assumption sentence is refuted as a statement of scope. This is not cumulative approval of report eb89620e; a corrected exact pin remains to be checked. The earlier approval A3131 remains valid at its cutoff.

The coordinator's Note233 and the underlying existing configured model comparisons were checked against the actual mathematical statements. Actual provider execution is independently unattested. No diagnostic script, mathematical computation, formal build or fresh web retrieval was needed. The main arbitrary-omega conjecture remains open, and no control is an Euler counterexample.

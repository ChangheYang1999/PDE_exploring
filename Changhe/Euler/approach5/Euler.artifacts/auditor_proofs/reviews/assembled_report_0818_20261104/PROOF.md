# Audit of report b2d9c61c at cutoff A3093

Status: the mathematical transfer is checked; one scope sentence needs correction before cumulative approval.

## 1. Exact object, dependencies and reading scope

The report pin is b2d9c61c78c950632253b2b579ee896c9fee6e994bfd9d0890b63f004b4d5bc6, assembled with7588lines and1190068bytes at the stated cutoffA3093. The complete299-line difference from approved86286d4420b0704d08c1bca13b34fdab557ec74f498cc4c1fd25aef3785abb87 has been read, including every long AppendixA row separately. Both full pins and the difference are retained. This is a delta audit; it does not assert a new full reading of all7588lines.

The prior approval A3083 covered front matter, Sections0-10 and AppendixA. Historical AppendicesB/C were not collectively certified. The present audit inherits that boundary and checks their changed passages individually. The complete independent proofs for A3079-A3082 and A3084-A3093 supply the mathematical dependencies. Existing A130/A132 compare the work-sign and no-finite-norm transfers. Their complete notes and coordinator Note229 are retained. Earlier complete C comparisons for the return and density statements are retained beside their independent proofs. Scripts, regeneration claims and provider execution are not independently certified here.

## 2. Work-sign criterion and its necessary-condition form

For a full C1/C1 profile, write A=cI-omega J, e=|U|^2/2 and w=U.grad(P+e). Dotting the equation with U gives w=-2(1-c)e-(Ay).grad e. If w=0, then along y(t)=exp(tA)y0 one has e(y(t))=exp(-2(1-c)t)e(y0). For0<c<1, y(t) tends to0 as t tends to minus infinity, whereas the right side diverges unless e(y0)=0. Local continuity suffices for this step.

The scalar theorem used for one-signed w is the independently proved extension, not a claim that Chae printed the extended ranges. For C1 divergence-free v and C1 H in dimensionN>=2, one-signed v.grad H vanishes if v is in L^s with1<=s<=N/(N-1), with no H norm; for finite s>N/(N-1), it suffices also that |H|^(s/2) be integrable. The bounded monotone test in the first branch and power m=(sN-s-N)/(2N)>0 in the second give vanishing boundary terms; when m<1 the fixed-epsilon regularization is retained. The common sign condition applies to both branches. The printed Chae statement has the higher threshold3N/(N-1) and an additional strictness condition. The report distinguishes these statements.

For bounded profiles satisfying Hb,0<c<1/2, the flux M(r)=integral_(B_r)w equals (5c/2-1)E-crE'/2. With beta=5-2/c, (r^(-beta)E)'=-(2/c)M r^(-beta-1). At2/5<c<1/2, a nonzero one-signed w makes |M| bounded below at all sufficiently large radii. Its integrated contribution is of order R^(-beta), contradicting the O(R^(-1)) energy remainder because0<beta<1. At c=2/5 finite energy and the logarithmic flux integral give the contradiction; below2/5 the energy theorem already gives U=0. Only the signed improper flux integral is asserted generally. Both strict signs of w therefore occur for a nonzero target profile, but occurrence arbitrarily far away is not established.

## 3. Positive-density returns and negative cumulative-source radii

For C1 divergence-free v with E_v=o(R), let q_v=tr((Dv)^2), a!=0 and phi be one compact test. The distributional pairings I_n of q_v(.+na) with phi equal integrals of v_i v_j against translated second derivatives of phi. Bounded overlap gives sum_(n<=N)|I_n|<=C E_v(N|a|+r0). Hence the number with |I_n|>=epsilon is at most that right side divided by epsilon. A positive-upper-density set on which all pairings converge to their untranslated values forces every untranslated pairing to be zero. The convex test sqrt(1+|y|^2), localized with its separate O(E_v(2R)/R) Hessian error, then forces v=0. The radial test also proves the stated zero-axial-mode variant when translations commute with rotations. The hypothetical profile return count O(N^(5-2/c)) follows from the confirmed energy law.

The balanced-base-ten control has sparse exact local returns, bounded derivatives and sublinear ball energy, but not uniform decay. Its local momentum residual has curl-2e3 for every c and omega. It is not a profile counterexample and does not settle sparse returns for actual profiles.

For the second assertion put N(r)=integral_(partial B_r)(U.e_r)^2 and K=rN-E. Under E=Lr^beta+O(r^(beta-1)),0<beta<1, off the set K<=-kappa E one has (1-kappa)E<rN<=rE'. Integration with dr/r gives the asserted logarithmic-density coefficient1-beta/(1-kappa). Integration of rE'/E by parts using only values of E gives the same asymptotic coefficient in ordinary measure, with O(R^(-1)) relative error. No energy remainder is differentiated. The pressure inequality is for the accumulated quantity integral_0^r s^3 Pbar'(s)ds, not Pbar' at a point. The compensated high-degree shell control has both signs of K at arbitrarily large radii and fails the full equation on untouched swirl shells for all c and omega. No eventual sign or limit for actual profiles follows.

## 4. The energy law alone does not give a finite velocity norm

The new control paragraph uses exactly the A3090 kinematic construction, with0<beta<1, all-center E_a(R)=LR^beta+O_a(R^(beta-1)/log R), smooth Poisson pressure, uniform velocity decay, and failure of every finite strong and weak L^p condition. The full momentum equation fails for every c and omega; derivatives and vorticity are unbounded. It does not decide whether full profiles have some finite L^p norm.

The auxiliary C1 field estimate assumes bounded exterior gradient as well as the precise energy law. A unit-width shell has energy O(R^(beta-1)). A velocity value of size delta persists on a ball of radius comparable to delta under this gradient hypothesis, so delta^5<=C R^(beta-1). Therefore |V|<=C R^((beta-1)/5), and integration over shells gives L^p for p>(2+3beta)/(1-beta). Substitution beta=5-2/c gives (17c-6)/(2-4c), as printed. The earlier full-profile natural rate under the separate half-power gradient-growth hypothesis is correctly described as stronger; that earlier theorem is a dependency, not freshly re-proved in this audit.

## 5. One sentence overstates the constant-profile test

In the work-sign bullet the report says: "The constant profile U = a with w = -(1 - c)abs(a)^2 < 0 shows that decay cannot be dropped."

Taken as a statement about the just-stated bounded-Hb theorem, this is not a valid inference. That theorem already does not require uniform decay. The exact constant profile has P=-[(1-c)a+omega Ja].y, fails Hb because U(R.)=a, and fails every finite L^s condition. Consequently it cannot refute the same theorem with only uniform decay removed. What it proves is that one-signed work and uniform sublinearity alone do not imply zero, and that boundedness alone cannot replace Hb.

Suggested replacement: "The constant profile U=a!=0 has one-signed work but fails Hb and every finite L^s condition; thus one-signed work and uniform sublinearity alone do not imply U=0."

The mathematical theorem, proof outline and AppendixA row already contain the correct hypotheses. This is a scope correction to one explanatory sentence, not a gap in A3079-A3080.

## 6. Remaining transfer and present conclusion

The radius beta-to-rho change in the exterior-source theorem removes a notation collision. Source hashes/statuses for the construction screen and LIT368/370/372 agree with the already checked status-only revisions. The front matter, summary rows, new AppendixA entries and historical change list retain the main arbitrary-omega conjecture as unresolved. No conditional hypothesis has become automatic. The control examples remain outside the full Euler class. Their frequency or small residuals are not used as proofs.

Cumulative approval awaits the correction in Section5 and a check of the resulting exact pin. The substantive mathematical changes in Sections2-4 match their confirmed dependencies. The existing configured model collaboration has been used throughout; actual provider execution is independently unattested. No mathematical computation or new model client was used.

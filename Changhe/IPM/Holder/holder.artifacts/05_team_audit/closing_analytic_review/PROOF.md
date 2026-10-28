# Closing mathematical audit of the accepted report

## Audited object and scope

This is the closing analytical review of the report accepted as version 43
in V256. Its frozen copy (version 43 of the report) is not included. Subsequent
report edits need a separate difference audit. The statements use
0<alpha<1, the Euclidean distance on R^2, real input unless explicitly
specified otherwise, and the homogeneous Holder seminorm modulo constants.
The kernel and Fourier convention are fixed in ../../01_setup/PROOF.md.
This audit is an additional synthesis of the cumulative checks, not a
claim that all numerical quadratures were repeated in the closing pass.

The main accepted conclusions include equality of the T_xx and T_xy
seminorms C_alpha, the inequalities C_alpha<=D_alpha<=C_alpha+1/2 for
D_alpha=||R_1^2||, the sharp two-term small-exponent formulas

    C_alpha = 2/(pi alpha) + C_0 + O(alpha),
    D_alpha = 2/(pi alpha) + 2 C_0 + O(alpha),
    C_0 = 1/2 + (log(2)-1)/pi,

and the shared large-exponent coefficient

    lim_(alpha->1-) (1-alpha) C_alpha
      = lim_(alpha->1-) (1-alpha) D_alpha
      = 3 sqrt(3)/(4 pi).

The exact finite-exponent norms remain undetermined. The accepted finite
upper and lower bounds, their exact endpoints, and their certificate
sources are in ../../data/verified_table.json. Strict separation is
proved at those ten exponents and, by V255, on explicitly certified
closed intervals around them. The small-exponent expansions also prove
strict separation for all sufficiently small positive exponents.
No assertion of separation for every exponent follows from these facts.

## Checks of definitions and passage to the stated spaces

| Claim | Closing check and conclusion |
|---|---|
| Distributional kernels | Differentiating -(2 pi)^(-1) log|z| off zero gives (2 z_i z_j-delta_ij |z|^2)/(2 pi |z|^4). The inner boundary integral is -delta_ij/2 times evaluation at zero. Thus T_xx=R_1^2+I/2 and T_xy=R_1R_2, with trace R_1^2+R_2^2=-I. The point mass must not be omitted. |
| Fourier sign and rotation | With exp(-i x dot xi), R_j has multiplier i xi_j/|xi|. Conjugating by f(x)->f(Q_beta x) replaces the angular kernel by cos(2theta-2beta), giving the positive sin(2beta) T_xy term. Rotation by pi/2 changes the sign of T_xx and preserves I. This proves C<=D, as well as the elementary upper comparison. |
| Origin and principal values | Each local kernel has zero angular mean. Subtracting the input value at its own pole leaves an absolute bound proportional to r^(alpha-2), integrable against area near zero precisely for alpha>0. The two poles are treated separately before limits. |
| Infinity and constants | A kernel increment is O(h r^-3). A normalized homogeneous input is O(r^alpha), so the remaining radial integral is bounded by a multiple of integral_R^infinity r^(alpha-2) dr. This requires alpha<1. Shifted outer balls differ by O(hR) area, making their constant-input discrepancy vanish. Individual unnormalized output values at infinity are not asserted. |
| Smooth compact tests | The fixed-increment approximation argument uses extension, truncation and mollification with a common Holder bound and separately controlled local and exterior errors. It proves equality of norm suprema. It does not assert density of compact smooth functions in the full homogeneous seminorm. Complex approximation uses the explicitly proved vector extension or the radial compactification for its stated witnesses. |
| Full norms | The annular angular inputs have uniformly bounded sup-plus-Holder norm but transform value at zero at least (1/2)log(R/2). Their outputs tend to zero at infinity, so subtracting any output constant still leaves at least half that oscillation. The homogeneous theorem therefore cannot be restated as a full whole-plane norm theorem. |
| Coordinate parity | Four distant reflected copies preserve the input seminorm once cross-copy distances are sufficiently large. The three unwanted copies contribute at most 3h||f||_1/[pi(2L-2R)^3] to the chosen increment. Letting L grow proves equality for each parity class. This says nothing about a fixed support or a fixed pair near the axes. |
| Extremizers and exponent continuity | Extremizers use normalized local compactness and uniform pole/exterior errors, not a compact embedding in the original seminorm. Continuity compares the same finite zero-mass measures with costs r^alpha, then takes cutoffs away. It does not identify function spaces at distinct exponents or differentiate the unknown sharp norm. |

## Checks of upper estimates and transport accounting

| Claim | Closing check and conclusion |
|---|---|
| One-circle real functional | The reflected angular pairs have equal opposite masses. Their distance gives a_n(alpha); the signed-distance witness verifies attainability for that circle functional. Equality of different local functionals is not inferred. |
| Far derivative and radius minimization | Differentiating the exterior cutoff produces both the bulk third angular harmonic and the boundary first/third harmonics. B_alpha includes this boundary contribution. Minimizing 2a_2 s^alpha/alpha+B_alpha s^(alpha-1) gives the displayed F, with 0<alpha<1 ensuring a positive finite minimizer. |
| Diagonal projection | The change r->lambda r leaves the finite positive measure Q_R and a local coefficient kappa=1/pi. Therefore R_1^2=P_R+H_R-Q_R-(1/2-kappa)I. The last two terms are a negative positive measure of total mass exactly 1/2. This accounts for the full identity contribution without replacing it by an untracked sign estimate. |
| Internal projection cycle | V256 closes the independent cross-read. The circulation uses the first-argument gradient with target held fixed; it is not the gradient of the composite cost. Only compact finite source masses are reassigned. The target submeasures are permuted exactly. The resulting delta_alpha is valid for P_R and the original G minimization; additivity with later retained-plan savings is unproved. |
| Midpoint and exterior series | The increment kernel is G(z)=z/[pi(z^2-1/4)^2]. Its exterior expansion has leading z^-3, and the remaining series is absolutely controlled outside the chosen radius. The singularities at plus/minus1/2 are removed with explicit errors. |
| Finite reflection and circular plans | Every accepted plan matches the indicated masses. Endpoint and radial remainder estimates cover the portions omitted by the finite discretizations. The numerical implementation retracted in V036 is not used by any current endpoint. |
| Signed-divergence flow lifting | Choose a probability theta_j in every cell. For nonzero signed mass use its normalized magnitude; for zero mass use a point mass at a cell center. Then sum pi_jk theta_j tensor theta_k has marginal difference sum m_j theta_j, including transshipment through zero-mass cells. This supplies the missing division-by-zero case explicitly. |
| Phase interpolation | The sine coefficients for adjacent phases are nonnegative. Their exact maximum is H_gamma, with certified branch handling. Uniform local, identity and omitted-region terms are added outside this interpolation. Monotonicity in each endpoint permits upper interval endpoints. |
| Identity savings and disk geometry | The positive remainder admits the extracted reflected pairs on the stated disks. The moment bounds use the specified normalized coordinates and pushed measure. Alternative extractions of the same mass are not added. Only the mutually disjoint supplemental disks of Theorem3.10(d) contribute additively. |
| Whole-exponent comparisons | Plans and witness shapes stay fixed within each group. The upper moment is log-convex; the lower moment is I(alpha,a)/alpha for one fixed a. Supporting lines use lower values at inner nodes and upper values at exterior nodes. Each group includes the required exterior neighbors. A minimum over unrelated plans is not assumed log-convex. |

## Checks of lower estimates and asymptotic arguments

| Claim | Closing check and conclusion |
|---|---|
| Signed-distance witnesses | The sign is locally constant off a closed separating set. A segment joining opposite signs crosses that set, giving the sum-of-distances bound needed for the factor 2^(alpha-1). The proof checks pairs on both sides, not only gradients within one sign region. |
| Lattice pole constraints | Minima and maxima of real seminorm-one functions preserve that seminorm. The half-plane envelope and its reflected extension are checked across the dividing line. Prescribed pole jumps are included with their actual sign in R_1^2. |
| Homogeneous degree three | The potential has degree alpha+2>2, so its distributional derivatives introduce no point mass at zero. The singular integral and differential expression solve the same equation. Their sublinear harmonic difference is constant, which is the permitted output ambiguity. |
| Polygon and projection integration | Positive layer-cake or Stieltjes formulas supply monotone enclosure rules where claimed. For two-dimensional producer certificates, local pole subtractions, cell error bounds and exterior remainders remain part of the certificate. Rounded floating integrals do not replace any of these terms. |
| Small-exponent finite part | The local logarithmic divergences are subtracted with the correct angular constants. The remainder estimates are uniform in the kernel direction before maximizing. The explicit moment lemma bounds a single angular moment by 16r/3, avoiding an unjustified exchange of direction, mode and cutoff limits. |
| Direction maximum | The finite-part direction dependence, periodicity and strict maximum are established by the accepted analytic argument. Sampled directions alone would not prove the maximum. This direction theorem is an asymptotic statement, not a proof of the maximizing direction at finite alpha. |
| Exact second term for D | The local projection profile and its global assembly supply a common admissible witness, matching the independently proved projection upper finite part. The formerly conditional assembly step is closed. The resulting constant is 2C_0. |
| Linear remainders | The explicit upper and lower remainders have the stated finite exponent range. Analytic logarithmic moments are controlled before expansion. Supplemental reflection savings are applied to the same accepted base upper bound exactly once. |
| Large-exponent coefficient | The real cubic witness and far-harmonic upper bound match at 3sqrt(3)/(4pi). The bounded identity difference makes D share this coefficient. This does not assert endpoint boundedness at alpha=1. |

## Complex-input checks

The real-input norm of S=T_xx+iT_xy is C_alpha because each scalar phase
projection is rotation-conjugate to T_xx and the suprema can be exchanged.
The real-input Beurling norm is 2C_alpha. A scalar real-kernel operator
has the same norm on real and complex inputs by phase projection of each
output increment. These facts do not equate the complex-input norm of S
with C_alpha.

For a complex angular mode r^alpha exp(i n theta), the exact seminorm is
2^(1-alpha) Q_(alpha,n). The radial comparison reduces the supremum to
equal radii and the angular interval [0,pi/(2n)]. Angular translation
gives the reciprocal Fourier-functional constant. The complex upper
bound includes the cutoff boundary term, just as in the real proof.
The complex cubic potential and the local glued witness give the stated
lower bounds with their own exact seminorm controls. The complex S
endpoint coefficients are 1 at alpha=0 and 2/3 at alpha=1; Beurling has
twice these coefficients. The strict complex-versus-real result is
proved for every exponent by the accepted inequalities, not by comparing
only the two limits. The exact complex small-exponent second term stays
open.

## Numerical and literature evidence limits

V241 audited all forty selected table endpoints, exact directed rounding,
ratios and gaps, and 113866 declared digest edges over 13451 JSON records
and 13772 distinct files. This is a provenance and arithmetic check,
not a substitute for the analytic proofs.

For D_(1/2)>=2.4542144708, V239 checked every one of the 4019 finer producer
records; 52 complete tasks and 1129918 cells were independently replayed.
For D_(3/4)>=2.8948343532, V237 checked all 3961 finer producer records;
70 complete tasks and 2396908 cells were independently replayed. The
separate coarser certificates have complete independent replays. The
current finer certificates must not be described as completely replayed.
The fine cross-disk upper certificates likewise have their documented
code, source, recombination and floating diagnostic checks; the floating
Cartesian comparison is not an independent interval quadrature.

The twelve primary statements in report Section2 were rechecked in V244.
Only actual archived source text supports those attributions. Nolder,
Arsenovic-Mateljevic, Rode-Simonenko with its correction, and the relevant
AIM book theorem remain inaccessible or incomplete for this audit.
No conclusion uses their unseen statements. The local-source gate
records earlier unsupported access claims and their retractions.

The local LP calibration does not supply an error bound. V246/V253 prove
that the two-disk own-kernel functional attains its summed circle bound
exactly when cos(phi)=0. Other sampled phases have genuine deficits, but
their magnitudes are not identified by that theorem. V245 and V249 remain
optional OPEN additions pending independent mathematical cross-read.

## Verdict and dependencies

CONFIRMED for the mathematical statements of frozen report43 within the
specified spaces, ranges and evidence limits. No new counterexample or
unclosed step in an accepted report theorem was found in the closing
pass. This does not resolve any question explicitly left open above.

The detailed theorem-to-proof index is ../../THEOREM_MAP.md. The manifest
in verification/accepted.json records the exact report, index, cited
standalone proof and selected verification bytes used in this synthesis.
Hash agreement establishes identity only; the arguments and cumulative
verifier verdicts are the mathematical justification.

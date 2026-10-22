# Independent whole-plane audit of six quadrature re-solves

## Statement and scope

The primary targets are six literal archives: quadB32_beta3.062, quadB40_3076_beta3.076, quadB40_3092_beta3.092, quadB48_3062_beta3.062, quadB48_3092_beta3.092 and quadL2B40_3085_beta3.085. Each name denotes a .npz file published by the numerical lane. Each contains a forced state and is not presumed to be a solution. Its preceding 12-point-quadrature archive, the completed 48-point log and the secant-zero archive supply provenance and finite comparison data. Logged quadrature order is a fact to verify from the log, since the archive itself omits that field.  The B2 velocity is W=beta X+B[Omega], with the canonical full-plane relative inverse B[Omega]=U[Omega](X)-U[Omega](0) and kernel K(Z)=(Z_2,-Z_1)/(2 pi |Z|^2). The distinct forced diagnostic uses W=beta X+B[Omega]+lambda B[f], with the fixed source in its own stored physical basis. These labels must remain distinct.

A nonzero exact center defect refutes the literal field as B2. A nonzero coefficient of a positive leading thermal residual power proves an infinite absolute whole-plane thermal residual. Neither excludes corrected nearby fields or general smooth profiles. Agreement and order of three stored continuation values establish a finite sampled comparison only, not a root, fold or continuum branch.

## Domain, center and exact rational check

The coordinate is r=L sqrt((1-t)^(-2b)-1), with L,b>0 and 0<=t<1. Its derivative is positive away from0, it starts at0 and tends to infinity as t tends to1. Thus each archive covers the whole plane; L is a numerical map scale, not a physical wall. The divided fields obey Theta=x^2 F, Omega=xG and use the prompt's x-reflection parity. Near0, t=O(r^2), inactive radial coefficients suppress angular mode n until order r^n, and the odd modes carry an additional factor r/sqrt(r^2+L^2). Consequently F=a+O(r), G=q+O(r), with bounded first derivatives. Only this local regularity is needed for the center test; global C-infinity is not inferred for spline fields.

Using x=r sin(phi), y=-r cos(phi), write G=sum D_k(r)cos(k phi). The strain c=Psi_xy(0) is the absolutely convergent kernel moment (1/pi) integral xy Omega/|X|^4 dX. The angular identity sin(phi)^2 cos(phi)=(cos(phi)-cos(3phi))/4 and orthogonality give c=-(1/4) integral_0^infinity(D_1-D_3)dr. For odd modes1,3, the radial representation gives D_k dr=bL S_k(t)dt. A degree-p B-spline with knots kappa has integral (kappa_(j+p+1)-kappa_j)/(p+1), by telescoping the derivative recursion. Hence

    c=-bL/[4(p+1)] sum_j(g_(1,j)-g_(3,j))(kappa_(j+p+1)-kappa_j).

Near0 the source has Omega=qx+O(r^2); at infinity D_k=O(r^(-1-1/b)), so the moment is absolutely convergent at both ends. The finite formula is exactly rational for the frozen binary coefficients and regenerated binary knots. It is applied separately to the unknown and seed; linearity gives c_forced=c_self+lambda c_seed. An independently written consumer reloads both raw blocks and recomputes the rational sums and residuals. Metadata such as converged is not a premise.

The relative gauge and parity imply W(0)=0 and DW(0)=diag(beta-c,beta+c). Hadamard's formula W1/x=int_0^1 partial_x W1(tx,y)dt gives a continuous axis limit A0=beta-c. The divided equations are

    R_F=A(2F+x F_x)+W2 F_y-(beta-2)F,
    R_G=A(G+x G_x)+W2 G_y+G-(2F+x F_x).

At0 these yield R_F=-2ma and R_G=(beta-c+1)q-2a, where m=c-1-beta/2. The grouped pointwise normalizers tend to N_F=|2(beta-c)a|+|(beta-2)a| and N_G=|(beta-c)q|+|q|+|2a|. They are positive for the nonzero a and beta>2 tested here. Continuity proves that their exact ratios are lower bounds for the divided global suprema and for the limsup of the original Cartesian ratios at off-axis points approaching0. This proves the literal-field rejection whenever R_F != 0, even though the un-divided residual is zero exactly on the symmetry axis. There is no denominator floor; 0/0=0 and nonzero/0=infinity.

## Whole-plane inverse and tail residual theorem

For completeness the full expansion argument follows, in standard physical polar coordinates x=r cos(theta), y=r sin(theta). Assume 3<beta=b<4, s=1/b, sigma=1/3, m=1-2s, k=2-s, kS=5/3, and lambda!=0. The last spline interval is a polynomial in t; Taylor expansion at t=1 and t=1-(1+r^2/L^2)^(-1/(2b)) give

    Omega=r^(-s)a(theta)+r^(-2s)b1(theta)+O_C1(r^(-3s)),
    Theta=r^m h(theta)+r^(m-s)d(theta)+O_C1(r^(m-2s)),
    f=r^(-sigma)aS(theta)+O_C1(r^(-2sigma)).

Here O_C1(r^p) bounds the value by Cr^p and first Cartesian derivatives by Cr^(p-1). Angular factors are finite trigonometric polynomials. More specifically, h=L^(1+2s)H0, d=-L^(1+3s)H1, a=L^(1+s)A0, b1=-L^(1+2s)A1 and aS=L_S^(4/3)AS0, where H0,H1,A0,A1,AS0 use the endpoint spline values or derivatives and the parity factors cos(theta)^2 or cos(theta). Those finite angular coefficients are rational Laurent polynomials, exactly reconstructible from the binary input. Odd-mode factors change only terms beyond these orders because their radial correction is O(r^-2).

Let p,pS be the unique periodic solutions p''+k^2 p=-a and pS''+kS^2 pS=-aS. The frequencies are noninteger, so each Fourier coefficient is divided by a nonzero rational eigenvalue. The streams r^k p and r^kS pS produce velocities r^(1-s)(-p',kp) and r^(1-sigma)(-pS',kS pS). These are their canonical relative inverses: the relative kernel integrals converge at infinity since s,sigma>0 and at0 since s,sigma<1. No origin distribution arises because the small-circle flux tends to0. Any difference is a full-plane harmonic velocity of sublinear growth, hence constant by the interior harmonic gradient estimate at growing radius. Its value0 at the center fixes that constant to0.

If a remainder decays as r^-q with 0<q<1, its relative inverse is O(r^(1-q)). Split the kernel integral into |Y|<r/2, comparable radius and |Y|>2r. The first part is bounded by C/r integral_0^(r/2)rho |g|drho+C integral_0^(r/2)|g|drho. The comparable-radius singularity |X-Y|^-1 is locally integrable and yields the same order. On the exterior, the difference kernel is at most Cr/|Y|^2, giving Cr integral_(2r)^infinity rho^(-q-1)drho. Each is O(r^(1-q)). The integrable singularities of removed homogeneous fields near0 contribute at most a constant. Thus B[Omega] has the leading velocity above plus O(r^(1-2s)); B[f] has its leading velocity plus O(r^(1-2sigma)).

Substitution into the two residuals gives

    R_Theta=r^(m-s)E_T+lambda r^(m-sigma)D_T+O(r^(m-2s)),
    R_Omega=r^(-2s)E_O+lambda r^(-s-sigma)D_O+O(r^(-3s)),

where

    E_T=-d+kp h'-mp'h, D_T=kS pS h'-mpS'h,
    E_O=-b1+kp a'+sp'a-m cos(theta)h+sin(theta)h',
    D_O=kS pS a'+spS'a.

Indeed the dilation operators annihilate the first radial powers and multiply the second by -1. The angular gradients of r^m h give these displayed products; all omitted source interactions have smaller exponents since s<sigma<2s. Both thermal exponents m-s=1-3/b and m-sigma=2/3-2/b are positive and distinct, whereas m-2s=1-4/b<0. A nonzero E_T therefore forces an infinite absolute self thermal residual. In the forced equation, either nonzero E_T or D_T does the same, by taking the largest nonzero exponent at an angle where its coefficient is nonzero. Lower powers cannot cancel it. All terms at or above these orders have been included, with a decaying remainder; no resonance occurs for the stated exponents. The exact Laurent witnesses must verify nonzero coefficients instead of presuming that a missing power is nonzero.

For a separate check, if pS has a simple zero at an axis angle and nonzero analytic h vanishes there to finite order n>=2, then D_T has leading local coefficient (kS n-m)AB, where A,B are the nonzero leading coefficients of h,pS. This cannot vanish because kS n>=10/3>m. Thus the source's simple axis zero and a nonzero temperature endpoint already imply D_T!=0. This source test is also computed exactly from the source block.

## Numerical measurements, dependencies and limitations

The numerical regional evaluation uses the verifier's own adaptive physical-radius Green inverse, with power substitutions for the inner and infinite exterior integrals, and seven-point Cartesian differences, with no NUM evaluator imported or executed. It retains both forced and defining self residuals, absolute and normalized values, six radial bands, both axis directions and both signs of x. Halving the finite-difference step is a sensitivity check, not a derivative error enclosure. Adaptive estimates and finite samples are not certified suprema. The inverse includes the infinite exterior and the center subtraction from that same inverse, with no imposed wall or harmonic correction.

A separate exact inverse-constant certificate uses the fully proved finite-part formula of P111. Its input and certificate are reloaded independently; it is a property of the stored spline, not a uniform refinement limit. The mathematical dependencies are the displayed B2 equations, angular orthogonality, B-spline integral identity (P160), complete R2 endpoint expansions (P89), and the fully stated inverse-constant theorem and proof in P111. Exact center and tail arguments have been included here; their prior independent controls are retained as dependencies rather than represented as new tests.

Resolution comparisons concern only saved states at the same beta that are actually available and frozen. Missing resolutions are not inferred. A state accepted after one inner evaluation of a transplanted lower-resolution field is inherited data; equality of its lambda is not an independently resolved root. The logged iteration counts, source blocks and coefficients are therefore checked alongside every lambda comparison. Re-optimization at a second beta likewise supplies a finite computed stage, not an exact root, derivative, fold, continuum limit or zero-forcing endpoint. No assumption about the counts or agreement is made before inspecting and freezing the actual records. The global B2 question remains OPEN.

This proof is adapted from the verifier's complete P280 proof, retaining precisely the same representation and hypotheses for six newly saved fields. It precedes the controls. The source simple-axis-zero and nonzero exact Laurent witnesses are conditions that the new checks must establish for each field. Failure of any test is reported without extrapolation. No numerical-lane code is imported or executed.

## Re-solve comparisons and acceptance

For each pair we compare the exact saved lambda, the raw cF/cG arrays, the source arrays, objective, inner flag and log. A lambda accepted at secant0 after restarting from a stored lambda is inherited; equality alone does not resolve the scalar root or bound its shift. An inner update can change coefficients and objective even when lambda is inherited. The fixed-point stopping residual, PDE residual, objective and strain mismatch are distinct quantities. The saved coefficient strain is independently recomputed and need not equal the last pre-update logged strain. Exact equality is required for a claim that an array or source is unchanged; finite norm comparisons are labeled numerical observations.

These checks do not certify the solver's runtime interpolation or compare its velocity to its quadrature nodes. That is a separate audit. Our PDE evaluator reconstructs the infinite-domain inverse independently by physical-radius integration, followed by Cartesian differences of the raw represented fields. A comparison between two solver quadrature orders is not an error enclosure relative to the exact inverse. A four-times larger per-cell Gauss rule does not multiply resolution of the represented field. None of these comparisons proves convergence or an unforced B2 endpoint.

Written 2026-10-22T05:53:45.205281+00:00 before controls.

## Explicit representation, normalizers and scale conventions

For the center formula, put z=1-t. The radial vorticity coefficient for an odd cosine mode is D_k(r)=z^(b+1) [r/sqrt(r^2+L^2)] S_k(t), with r=L sqrt(z^(-2b)-1). Differentiating gives dr/dt=b L^2 z^(-2b-1)/r. Since sqrt(r^2+L^2)=L z^-b, their product is exactly D_k dr=bL S_k dt. Here S_k is the stored masked degree-p spline. Thus the center formula follows directly from the representation, without a numerical integration premise.

For x nonzero the actual Cartesian normalizers satisfy N_Theta=x^2 N_F and N_Omega=|x| N_G term by term, using the three thermal terms and four vorticity terms displayed above. This is because W1=xA, Theta=x^2F and Omega=xG. Their residuals satisfy R_Theta=x^2R_F and R_Omega=xR_G. Hence the ratio equalities hold off axis, and their limiting assertion at the center follows from continuity and the positive center denominators.

The center mismatch is m_c=c-1-beta/2; the logged and saved mismatch columns concern the forced c. The symbol m in the tail section means only the exponent m_t=1-2/beta, never a strain mismatch. The self and forced center values, and the regional sampled maxima, are separate quantities. In particular the repeated regional F values near0.72956 or0.72415 are not center ratios. Their maximizing points are tabulated in GLOBAL_RESIDUALS.csv, respectively x=0, y=1.6182418407133987 for beta3.062 and x=0, y=1.6296216540630053 for beta3.092. They occur on the positive axis away from the material center. Similar finite maxima at the same beta do not establish a resolution limit.

Exact Laurent polynomials represent the tail coefficients after removing specified nonzero factors. The removed factors are L^(1+3/beta) for E_T, seed_L^(4/3)L^(1+2/beta) for D_T, L^(1+2/beta) for E_O and seed_L^(4/3)L^(1+1/beta) for D_O. These factors are positive since both map scales are positive. The source contribution additionally carries the stored nonzero lambda. Thus a nonzero rational Laurent witness proves nonvanishing of the physical coefficient even when its removed scale is irrational. The factors are recorded as coefficient_scales in exact_native_tail.json. No claim that every unscaled physical coefficient is rational is needed.

The stream convention throughout is -Delta Psi=Omega and U=(-Psi_y,Psi_x), giving K(Z)=(Z2,-Z1)/(2 pi |Z|^2). The tail stream is Psi=r^k p with p''+k^2p=-a. This fixes the sign without changing stream conventions midway.

Clarifications written 2026-10-22T06:12:36.048767+00:00 before final consumer rerun. The initial proof and controls are retained.

# Exact full-plane norms for native desingularized vorticity

Status: CONFIRMED independent informal proof, exact rational interval certificates, separate archive/de Boor checker and actual Claude Opus5.5 reviews341/342/344/346/348. No conclusion about the existence of a B2 solution is asserted.

## Statement and hypotheses

Fix rational b>0 and L>0, and a finite clamped rational knot vector on [0,1]. Let S_k and T_k be real splines of degree d with rational coefficients on this same vector. There are finitely many modes, indexed by k>=0; missing modes are zero. On every nondegenerate knot cell each spline is a polynomial of degree at most d. Continuity suffices for the formulas below; the stored applications have simple interior knots and d=5. The coefficients denote exact rational inputs, including exact stored binary rationals when decoded from a numerical archive. A rounded difference of two floating-point coefficients is not an exact input difference. In every archive application b is the exact binary rational of the stored float64 beta_basis value, not the real number suggested by a short decimal label and not necessarily the PDE exponent beta. Likewise L is the exact binary rational of its stored float64 value. Knots are the exact binary rationals of the generated floating-point knot array, not the real numbers defined by an idealized linspace-power expression. The archive does not store this array, so each export records and hashes the actual generated array; the independent checker reproduces and compares every binary entry. Common b,L,degree and identical knot arrays are required and checked; this implementation does not compare different radial knot vectors.

Use physical polar coordinates x=r sin(phi), y=-r cos(phi), r>=0, and put

    z=(L²/(L²+r²))^(1/(2b)), t=1-z, rho=sqrt(1-z^(2b)).

For a spline family S define the scalar field

    G_S(r,phi)=z^(b+1) sum_(k even) S_k(1-z) cos(k phi)
              +z^(b+1) rho sum_(k odd) S_k(1-z) cos(k phi).       (1)

This is the native representation of G=Omega/x away from x=0, with its continuous axis extension. The coordinate derivative d_phi holds r fixed. The norm is the ordinary area L2 norm of G itself, not of Omega=xG, not of the inverse velocity, and not a pointwise PDE residual. In particular finiteness of this norm says nothing by itself about finite physical vorticity energy.

For a family P=(P_k) of polynomials on each z-cell, define

    I_0(P)=int_0^1 z [2P_0(z)^2 + sum_(even k>=2) P_k(z)^2
                         +(1-z^(2b))sum_(odd k)P_k(z)^2] dz,
    I_1(P)=int_0^1 z [sum_(even k>=2) k² P_k(z)^2
                         +(1-z^(2b))sum_(odd k)k² P_k(z)^2] dz. (2)

Then both integrals are finite and nonnegative, and with P_k(z)=S_k(1-z),

    ||G_S||²/(pi b L²)=I_0(P),
    ||d_phi G_S||²/(pi b L²)=I_1(P).                            (3)

The same formulas apply to the difference G_S-G_T with P_k=S_k(1-z)-T_k(1-z), because b,L and the represented basis are common. I_0(P)=0 exactly when every represented P_k vanishes identically. I_1(P)=0 exactly when every represented nonconstant angular mode vanishes identically; the mode k=0 may remain. All zero statements concern the represented splines after masks, not unused raw coefficient slots.

A finite rational certificate can enclose each I_j for the two reference fields and their difference. If a certified lower bound for a reference I_j is positive, these certificates give rigorous bounds for the relative L2 error by interval division and rational square-root bounds. The factors pi b L² cancel, so no approximation of pi is needed for relative norms. Finitely many finite-state comparisons do not prove a refinement limit, and small L2 distance does not imply small pointwise, Cartesian derivative, inverse-tail-constant or PDE error. The separate I_1 certificate controls only the area L2 norm of the fixed-r angular derivative.

## Proof of the physical norm formulas

The radial change of variables is r²=L²(z^(-2b)-1), hence r dr=-bL² z^(-2b-1) dz. Multiplying by the square of the envelope z^(b+1) leaves bL² z dz. All spline functions are bounded on the compact interval, and 0<=1-z^(2b)<=1, so the integrals in (2) are finite.

For nonnegative integers k,l, integration on [0,2pi] gives int cos(k phi)cos(l phi) dphi=0 when k!=l, 2pi when k=l=0, and pi when k=l>0. This follows by the product-to-sum identity and integration of cos(n phi) for nonzero integer n. Differentiating the finite trigonometric sum gives -k sin(k phi); sine orthogonality gives pi k² for k=l>0 and zero otherwise. In particular there are no even/odd cross terms, despite their different radial factors. Substitution yields (2)-(3).

Every term in (2) is nonnegative. On 0<z<1 all coefficients multiplying a nonconstant squared mode are strictly positive, and the coefficient of P_0² in I_0 is strictly positive. If the integral is zero, each continuous mode vanishes on every open knot cell, hence everywhere by continuity. For the angular derivative the constant mode is absent. This proves the zero criteria. Linearity of (1) at common b,L proves the difference assertion.

## Exact polynomial integrals

On a z-cell [a,c] in [0,1], every squared mode is a rational polynomial Q(z)=sum_j q_j z^j of degree at most 2d. Thus

    int_a^c z Q(z) dz = sum_j q_j (c^(j+2)-a^(j+2))/(j+2),
    int_a^c z^(2b+1) Q(z) dz
          =sum_j q_j (c^(2b+j+2)-a^(2b+j+2))/(2b+j+2).        (4)

All exponents in the second line are positive. To verify (4), differentiate z^q/q on z>0. Its limit at zero is zero for q>0, so integration including a=0 is legitimate. Negative q_j do not imply a negative integral; each term must be enclosed with sign-aware interval multiplication before summation.

Write 2b=N+alpha with integer N>=0 and 0<=alpha<1. If alpha=0, all terms in (4) are rational. Otherwise each endpoint power is v^(N+j+2) v^alpha. It suffices to bound v^alpha for rational v in [0,1]. At v=0,1 this is exact. For 0<v<1 the following rational procedure supplies enclosures of any required precision without treating floating-point transcendental evaluations as exact.

Choose an integer h>=0 with w=2^h v in [1,2). For q=(w-1)/(w+1) in [0,1/3),

    log w=2 sum_(n=0)^(M-1) q^(2n+1)/(2n+1) + R,
    0<=R<=2 q^(2M+1)/((2M+1)(1-q²)).                          (5)

Indeed differentiate or integrate the geometric series 2/(1-q²) on [0,q]. The omitted positive terms have denominators at least 2M+1 and sum to the displayed geometric bound. The same formula at q=1/3 encloses log2; subtract h log2 to enclose log v. The identity log v=log w-h log2 is exact.

For x>=0, scale x=2^h y with 0<=y<=1/2. The exponential series through degree n has positive remainder bounded by

    first_omitted_term/(1-y/(n+2)).                            (6)

Successive omitted terms have ratio at most y/(n+2), proving the bound. Repeated squaring and positive reciprocal interval operations enclose exp(-x). Apply this with x=-alpha log v, enlarging any lower endpoint below zero to zero since x>=0. Outward rational rounding at each stage preserves inclusion. Equations (5)-(6) prove the interval primitives implemented here in modal_norm_power.py, following the design104; changing the recorded precision and truncation orders changes efficiency and width, not soundness. No width or convergence claim is needed to validate a finite resulting enclosure.

Combining (4) over the exact knot partition and the mode weights in (2) gives finite enclosures [l_j,u_j]. Intersecting a lower bound with [0,infinity) is justified by (2). For a difference interval [l_D,u_D] and reference [l_R,u_R] with l_R>0, its squared relative norm lies in [max(0,l_D)/u_R,u_D/l_R]. For any nonnegative rational q and integer H>0, let n be the integer square root of floor(q H²). Then n/H<=sqrt(q)<=(n+1)/H. This proves the rational square-root enclosures, including the case q=0.

## Archive decoding and independent checking

The exact object certified here is the mathematical archive reconstruction (1): all arithmetic and powers in that formula have their real mathematical meanings, with the specified exact binary-rational input coefficients and the regenerated knot vector. This is not a bitwise specification of every floating-point evaluation performed by the solver. In particular a runtime may round b+1, 1/(2b), powers and the very-far-field t value; those evaluation errors are not part of the exact field. The stored archives do not contain their historical knot array or sufficient runtime provenance to prove its bitwise identity across different NumPy or libm versions. We therefore state the verifier environment and register every actual knot entry in JSON. Cross-environment historical bitwise identity remains unasserted. The hash-pinned source is read statically, never imported or executed. Its r2 map, odd-mode factor, cosine rows, coefficient mask and envelope exponent are transcribed in verification/SOURCE_TRANSCRIPTION.md. Formula(1) uses the corresponding real map and spline without the upper-endpoint clamp that the source applies to its floating spline evaluation. Thus(1) is an explicitly defined ideal real reconstruction, not the program's piecewise clipped floating mapping on the extreme far tail. The source's analytic formulas motivate this reconstruction; fingerprints alone do not prove semantic correspondence or historical execution. The source's mask cap min(floor(k/2),Nb-2) equals floor(k/2) for all archived mode counts certified here, a fact checked from the dimensions. All unused raw mask slots are independently checked to be zero by check_modal_norm_provenance.py; that script also checks the inactive mask cap. The verifier's SciPy reader decodes the archive independently of the generator and exact checker, though all readers use NumPy to reconstruct the knots. A z-weighted quadrature checks modal values and products but reuses the derived Jacobian. A separate sinh-radius quadrature integrates G² r dr directly with its physical Jacobian and tests that normalization numerically. Both are consistency diagnostics, not part of the interval proof. Equality of L is essential for subtracting two fields at the same physical radius; cancellation of a common L in the relative-norm formula does not justify comparing different L values.

Each original archive and the exact JSON export are hash registered. The decoder verifies b,L,degree,knots,mode counts and the mask rule. The stored mask sets coefficient j to zero when j<floor(k/2), and the explicit rho factor applies only to odd modes. Missing high modes in a lower-resolution archive are set to zero. Every active binary float is converted exactly to a rational before differences or products are taken. Exports distinguish fields from their differences and retain both source hashes.

The generator obtains each mode polynomial from the rational Cox recurrence. It may save coefficients in the normalized cell coordinate u=(t-A)/(B-A) and then substitute z=1-t. An independent checker uses pointwise rational de Boor evaluation directly from the decoded knots and coefficients. For each claimed mode polynomial of degree at most d, it checks equality at d+1 distinct rational points strictly inside the cell, for example u=i/(d+2) for i=1,...,d+1. The difference is a polynomial of degree at most d with d+1 roots, so repeated division by its distinct linear factors proves identity. This is an exact polynomial identity check, not an empirical sampling bound. The checker verifies that cells cover [0,1] with no gaps, overlaps or knot crossing, reconstructs products and integrals from the checked polynomials, and checks the final interval arithmetic and normalization.

A manufactured constant mode P_0=1 has I_0=1 and I_1=0. A single mode P_k=1, k>=1, has I_0=1/2 if k is even and b/(2(b+1)) if k is odd; I_1=k² I_0. These follow by integrating z and z^(2b+1) directly. A monomial P_k=z^m replaces 1/2 by 1/(2m+2) and, for an odd mode, subtracts 1/(2m+2b+2). The k=0 weight is2. These identities provide manufactured controls, along with hand-computed wrong-convention values that differ when the constant-mode factor2, odd rho factor, derivative k², physical radial Jacobian, or exact coefficient subtraction is omitted. These five comparisons do not execute a mutated normalization routine.

## Dependencies and scope

This proof uses elementary polynomial, trigonometric and integral identities. The independently implemented modal_norm_power.py primitives follow the rational log/exp design of104 and are proved and reviewed here; they are not asserted to be hash-identical to104, while183 supplies the earlier scalar spline identity-check design. This result concerns all represented angular modes of G and d_phi G and therefore differs from183's first-cosine radial spline norm. It does not supply a B2 solution, an error estimate to an unknown solution, a far-tail inverse constant bound, or a convergence theorem. Smoothness of an exact target is not inferred from a finite spline representation.

## Verified applications and evidence

Published UTC 2026-10-21T17:58:34.163828+00:00. The initial complete argument was written2026-10-21T17:20:11.793460Z before implementation; its hash and subsequent provenance revisions are retained. Four K32/K40 pairs share their exact basis exponent, scale, degree and knots. Each denominator below is the K40 norm, the second hash-identified input of its certificate. Outward decimal intervals below contain the retained exact rational intervals; repeated floating endpoints in a diagnostic do not mean zero-width exact intervals.

| PDE beta label | ||G32−G40||/||G40|| | ||d_phi(G32−G40)||/||d_phi G40|| |
|---|---|---|
| 3.0315 | [0.001596826594, 0.001596826595] | [0.027133934497, 0.027133934498] |
| 3.04 | [0.003277602514, 0.003277602515] | [0.047822072738, 0.047822072739] |
| 3.05 | [0.006094411393, 0.006094411394] | [0.076436763274, 0.076436763275] |
| 3.062 | [0.010536446265, 0.010536446266] | [0.113321043620, 0.113321043621] |

All four certificates passed107520 exact polynomial identity checks,26880 per pair, with all integrated radii and all represented angular modes. The eight sequential generation/checking steps completed in220.053668337s from2026-10-21T17:28:10.386459+00:00 to2026-10-21T17:31:50.440111+00:00. The independent checker uses rational de Boor evaluation and symmetric product assembly; it does not import the generator or its Cox recurrence. Both use the explicitly reviewed interval primitive module, a disclosed common dependency.

Final manufactured controls398, actual rejected mutations11 and algebraic counterchecks5 PASS at2026-10-21T17:58:33.935213+00:00 in2.506234960s. The398 comprise320 exact monomial norm cases,15 perfect powers,4 zero exponents,1 single-cell identity check,2 proportional norms,1 actual archive decode,48 known Greville constant/linear values across three rational cells for K3 versusK5,1 full unequal-mode certificate check and6 exact known norms for those two fields and their difference. The eleven mutations are8 mathematical-certificate alterations and3 archive-export alterations. Five separate hand-computed convention comparisons do not exercise mutated code. An initial record incorrectly grouped them with negative mutations; that record is retained and superseded, not silently counted as16 actual rejection tests.

Separate provenance checks verify inactive mask caps and zero unused raw slots in all8 archives, fresh binary knot hashes and common mapping data. Fifteen160-digit interior fractional-power controls agree with independently integrated monomials. A32-node-per-cell z quadrature gives relative discrepancies below5.8e−15 but shares the derived Jacobian. The independent physical-radius diagnostic uses r=L sinh u, its physical Jacobian,32and64 Gaussian nodes per subinterval and96 angular nodes. It agrees below5.8e−15 on the four pairs and includes36 manufactured scale/mode/power cases. Its finite cutoff u=120 has no interval tail bound and remains only a consistency diagnostic. These floating checks are not used to certify the intervals.

All five reviews used requested us.anthropic.claude-opus-5-5 and actual returned claude-opus-5-5 via Python Bedrock. Each has a complete written end_turn answer. The exchanges resolved exact-basis provenance, common-L necessity, runtime clipping, current versus historical knots, normalization coverage, control labels, and unequal-mode/multicell coverage. Review346 independently checked the actual interval and de Boor code. Review348 checks the added manufactured case. The trusted arithmetic base remains Python exact integers/Fraction/isqrt and the explicitly hashed NumPy-generated knot bytes; no theorem-prover verification is asserted. The manual source transcription is our own read-only analysis; no fitting-lane code was imported or executed. The norms certify the stated ideal real reconstructions, not historical floating evaluations, an unknown exact profile or a B2 residual.

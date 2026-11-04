# Momentum-defect moments and shrinking-domain energy

## Exact statement

Let c>0, omega be finite, U in C1(R3;R3) be bounded and divergence-free, and P in C1(R3). Set A=cI-omega J, B=Ay+U, X=cy+U, G=DU, q=|U|^2/2, M=(Jy) dot U, and

    F=-[(1-c)U+GB+omega JU],    D_P=grad P-F.

For the Poisson identity assume U is C2. Let mu be a compactly supported B-invariant probability. The following three conditions are respectively equivalent to the three zero defect moments against U, y and Jy:

    R1: integral U dot grad P = -(1-c) integral |U|^2,
    R2: integral y dot grad P = integral [(2c-1)y dot U+|U|^2],
    R3: integral (Jy) dot grad P = (2c-1) integral M.

Moreover

    integral B dot D_P = -(2c-1) integral U dot B.          (1)

If c!=1/2, the corresponding linear combination of R1-R3 is equivalent to integral U dot B=0, and to integral |X|^2=omega integral M. When omega=0, R1-R3 therefore force B=0 mu-almost everywhere.

If K is a compact C1 domain with B strictly outward on its boundary, put K_t=Phi_{-t}K. Then the profile energy balance on K_t is equivalent to integral_{K_t} U dot D_P=0. Cesaro limits of the normalized measures on K_t are invariant probabilities on the null compact invariant set Lambda_K=intersection K_t. If the balance holds for all t, these measures satisfy R1. If it holds for every C1-nearby outward-transverse domain and all t, then U dot D_P=0 pointwise on K.

These are identities for a general velocity and pressure, not assertions that the defect vanishes. No Euler equation is assumed until D_P is set equal to zero.

## Pointwise and invariant identities

Direct differentiation gives

    div F=-tr G^2=|curl U|^2/2-|S|^2,
    B dot grad q=-(1-c)|U|^2-U dot F,
    B dot grad(y dot U)=(2c-1)y dot U+|U|^2-y dot F,
    B dot grad M=(2c-1)M-(Jy) dot F,
    B dot grad(|y|^2/2)=c|y|^2+y dot U.

For the divergence formula, div(GB)=tr((A+G)G) and div(JU)=tr(JG). The omega terms cancel because tr(AG)=-omega tr(JG). The other identities follow by the product rule and J^T=-J. Integrating them against mu proves the three equivalences.

Put

    Psi=q+c y dot U-omega M+c(2c-1)|y|^2/2.

Another product-rule calculation gives

    (2c-1)X dot B=B dot F+B dot grad Psi.

Indeed the derivatives of U assemble into B dot GB, cancelling that term in B dot F; the remaining skew products cancel in pairs. Since integral B dot grad P=integral B dot grad Psi=0, this proves (1), using integral X dot B=integral U dot B. Also X dot B=|X|^2-omega M pointwise. This proves the stated linear-combination and nonrotating conclusions.

The Poisson equation Delta P=|curl U|^2/2-|S|^2 is exactly div D_P=0. It is not D_P=0. For a genuine bounded profile satisfying the vanishing-dilate condition of A031, the canonical-pressure result identifies the actual pressure gradient and does give D_P=0.

## Flow, flux coordinates and normalization

Bounded U makes B complete, since its growth is at most linear. Its divergence is 3c, so det DPhi_t=exp(3ct). Strict outward transversality makes K_t nested. Its volume is exp(-3ct)|K|, and its intersection Lambda_K is compact, invariant and null.

For continuous f on K,

    |K_t|^{-1} integral_{K_t} f
        = integral_K f(Phi_{-t}x) dx/|K|.                 (2)

Every point of K outside K_t lies on exactly one segment Phi_{-s}a with a in boundary K and 0<=s<t. Uniqueness follows from outward transversality and backward invariance; the exit time is unique. The flux-coordinate Jacobian is exp(-3cs)(B dot n)(a). Consequently

    integral_{K minus K_t} f
       = integral_0^t exp(-3cs)
           integral_boundaryK f(Phi_{-s}a)(B dot n)(a) dS(a) ds.  (3)

## Energy and its converse

The product rule gives

    div(qB+PU)-(5c/2-1)|U|^2=U dot D_P.

The divergence theorem proves the equivalence between the energy balance and integral_{K_t} f=0 for f=U dot D_P. Formula (3) shows that balance for all t implies every boundary flux moment of f is zero. Conversely, if all these boundary moments vanish, integral_{K_t} f is constant in t. It tends to zero because f is bounded on K and |K_t| tends to zero. Thus the constant is zero. This limiting step is required for the converse; differentiation alone leaves an integration constant.

Let nu_T=T^{-1} integral_0^T (Phi_{-s})_*m_K ds, where m_K is normalized Lebesgue measure. Compactness gives subsequential weak limits. The integral of B dot grad phi against nu_T is a bounded endpoint difference divided by T, hence tends to zero. For every fixed t, the fraction of times s<t is t/T, while all later measures are supported in K_t. Therefore every limit is supported in Lambda_K and is invariant. Equation (2) and balance give integral f dnu_T=0 and hence integral f dnu=0. The same proof works for the normalized positive boundary flux measure, using the boundary moments above. The defect-moment equivalence then gives R1.

Finally suppose the balance holds for every sufficiently C1-nearby outward-transverse domain. Make an arbitrary smooth normal boundary bump of height epsilon h. At fixed t, the derivative of integral_{Phi_{-t}K} f under that bump is

    exp(-3ct) integral_boundaryK f(Phi_{-t}a)h(a) dS(a).

It vanishes for every h, so f(Phi_{-t}a)=0 on every evolved boundary. These boundaries exhaust K minus Lambda_K. Since Lambda_K has empty interior, continuity gives f=0 on all K. The converse is immediate from backward invariance. No assumption of pointwise zero defect is hidden in this shape argument.

## Scope and verification

This confirms Theory Agent A C15 with the explicit integration-constant repair above. It proves only the listed finite moment relations and domain statements. It does not classify every possible weighted identity, does not realize all finite-time domain balances by a non-profile, and does not assign an area-growth asymptotic to the evolving boundaries. Those additional claims require separate arguments.

The proof is direct algebra, change of variables, the divergence theorem and compact weak convergence. No numerical test or external dynamical theorem is needed.

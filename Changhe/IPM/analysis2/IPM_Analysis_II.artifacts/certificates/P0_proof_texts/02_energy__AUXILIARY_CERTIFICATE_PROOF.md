# Auxiliary global coefficient certificates

## Certified statements

For each exact source background state88 and state131, let

    A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
    N=(1/2)[[rho_yyy,-rho_xyy],[-rho_xyy,rho_xxy]].

The following inequalities hold at every point of the plane:

    A>=-1/20 I,  sym DU<=17/20 I,  N<=100 I,                    (1)
    ||D²rho||_(infinity,Frobenius)<77,
    ||D³rho||_(infinity,tensor)<94,
    ||D²U||_(infinity,tensor)<35.                              (2)

All coefficients refer to the exact finite checkpoints, not to neighboring true profiles. The method and canonical input hashes are those of `COMPACT_CERTIFICATE_PROOF.md`. The bounds in this note complete the numerical hypotheses of `L2_ENERGY_PROOF.md` and `SOBOLEV_HOLDER_PROOF.md`.

## Exact polynomials for fourth and sixth derivatives

The fourth-derivative recurrence in the compact certificate extends verbatim to every even order d. Each differentiated generator is represented by

    r^(2k-d)(1+r²)^(p_j-k) t^l C_n(theta),  t=r²/(1+r²).

Its radial derivative multiplier remains(2k-d+2l)+2(p_j-k-l)t. After even d derivatives, the radial factor becomes

    w^(j+1)(1-t)^(d/2-2)t^(k-d/2+l),
    w=(1-t)^((1-gamma)/2).

For d=6 the extra factor is1-t, so the result is still w^(j+1) times a rational polynomial. Negative powers of t cancel exactly. The largest degrees are30 in t and12 in z=cos(2theta). Odd-odd derivatives use sqrt(1-z²) times a polynomial; even-even derivatives use an ordinary polynomial. `verification/auxiliary_polynomials.py` carries out this exact recurrence and stores all coefficients in JSON.

In particular,

    rho_x=-chi_xxxy-chi_xyyy,
    rho_y=-chi_xxyy-chi_yyyy,
    rho_xxx=-chi_xxxxxy-chi_xxxyyy,
    rho_xxy=-chi_xxxxyy-chi_xxyyyy,
    rho_xyy=-chi_xxxyyy-chi_xyyyyy,
    rho_yyy=-chi_xxyyyy-chi_yyyyyy.

All required third derivatives of U=(-chi_xyy,chi_xxy) use the sixth derivatives chi_51, chi_42, chi_33, chi_24 and chi_15. These formulas also identify every sine factor and sign. An independent order-six Cartesian Taylor evaluator overlaps the compactified formulas at four points per state; `auxiliary_field_crosschecks.json` records these algebra checks. The covering proof itself uses the exact recurrence, not the point checks.

## Matrix bounds and the vanishing radial factor

The tensor Bernstein enclosure and exact midpoint subdivision are proved in the main compact certificate. The auxiliary script applies them to A, (17/20)I-sym DU and100I-N. The latter two use direct enclosures. Their completed partitions have45 and49 leaves for the DU bounds, and5 leaves each for N, at states88 and131 respectively.

For A, a sharper enclosure first factors out w:

    A(t,z)=w C(t,z,w),

where C is a degree-three polynomial in w, with bivariate polynomial coefficients. On a rational (t,z) rectangle, enclose its entries by[a_l,a_h], [b_l,b_h] and[-D,D], including the sine factor in D. For any vector v,

    v^T C v>=a_l v1²+b_l v2²-2D|v1v2|.

Thus

    lambda_min(C)>=(a_l+b_l-sqrt((a_l-b_l)²+4D²))/2.

The Gershgorin bound min(a_l,b_l)-D may be larger and is also valid. If ell is the larger lower bound and w ranges in[w_l,w_h], then

    lambda_min(A)>=min(w_l ell,w_h ell).                       (3)

The degree-three Bernstein transform in w encloses C over that whole interval. Treating t and w independently enlarges the range and is safe. Equation(3) retains the common vanishing factor at t=1; this avoids needless subdivision caused by taking unrelated zero-containing diagonal and off-diagonal ranges.

The factored A certificates have57 leaves at88 and62 at131. Their minimum accepted lower bounds exceed-0.049324 and-0.048962, respectively, proving the common rational bound-1/20. Earlier un-factored runs that ended with incomplete partitions are retained only as unfinished computations and have no role in(1).

## Derivative component bounds

On every leaf of the complete DU partition, `verification/coefficient_bounds.py` restricts all required polynomials by the same exact de Casteljau matrices. It bounds the degree-four polynomial in w, includes the sine factor where present, and saves an Arb upper bound for each component. Direct inspection of every saved leaf bound proves

    |rho_x|,|rho_y|<11,
    |rho_xxx|,|rho_xxy|,|rho_xyy|,|rho_yyy|<33,
    |(DU)_ij|<7/5,
    |(D³U)_ijkm|<26.                                          (4)

Here the repeated last indices in the final expression mean all ordered third derivatives of each of the two velocity components. The displayed upper constants are intentionally common to both states. The saved enclosures give smaller bounds.

For a bounded twice differentiable function f on a line with bounded second derivative, Taylor's integral formula at x+h gives

    |f'(x)|<=2||f||_infinity/h+(h/2)||f''||_infinity.

Optimizing h proves ||f'||_infinity<=2sqrt(||f||_infinity||f''||_infinity). Apply this along each coordinate line to each first derivative of rho and U. Counting ordered tensor components in two dimensions yields

    ||D²rho||_F²<=16*11*33=5808<77²,
    ||D³rho||_tensor²<=8*33²=8712<94²,
    ||D²U||_tensor²<=32*(7/5)*26=5824/5<35².

This proves(2) without numerically differentiating sampled values.

## Finite audit and reproduction

`verification/audit_auxiliary_certificates.py` checks the entire exact binary tree of each matrix partition, every rational box, every lower bound, all source hashes, equality of the derivative-cover paths with the complete DU partition, and every derivative bound against(4). It also checks the rational inequalities used in the combined energy proof. `auxiliary_certificate_audit.json` records the successful audit.

The L2 identity has a separate symbolic test using generic parity polynomial backgrounds through degree5 and three Gaussian test potentials. Exact Gaussian moments give zero defect in every case; see `verification/check_l2_identity.py` and `l2_identity_checks.json`. This is an independent check of the signs in N, in addition to the integration-by-parts proof.

No assertion in this note concerns the normalized rank column, a strain-trace norm, or nonlinear closure.

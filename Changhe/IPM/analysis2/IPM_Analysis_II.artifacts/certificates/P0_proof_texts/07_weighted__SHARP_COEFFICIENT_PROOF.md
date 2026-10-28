# Compactified derivative bounds for the accepted checkpoint

## Objects and algebraic reduction

Use exact checkpoint131 and the canonical potential chi of the source audit, with rho=-partial_y Delta chi. Set t=r²/(1+r²), z=cos2theta, delta=1-1/c and w=(1-t)^(delta/2). All polynomials below have exact rational coefficients obtained directly from the recovered generator list.

After d Cartesian derivatives, one canonical potential term has the form

    coefficient * r^(2k-d+2l) (1+r²)^(p_j-k-l) trig(n theta).

This follows inductively from the polar derivative rule already proved in the compact matrix certificate. For d=5, collecting equal angular modes leaves nonnegative integer powers k-3+l. Consequently

    D^5 chi = sqrt(t(1-t)) sum_(j=0)^3 w^(j+1) P_j(t,z) A(theta),

where A is sin theta for an odd number of y derivatives and cos theta otherwise. The angular quotients sin((2m+1)theta)/sin theta and cos((2m+1)theta)/cos theta are polynomials in z. They satisfy the recurrence R_m=2z R_(m-1)-R_(m-2), with initial pairs(1,2z+1) and(1,2z-1), respectively. This proves the conversion without angular sampling.

For d=6 the corresponding formula is

    D^6 chi=(1-t) sum_(j=0)^3 w^(j+1) P_j(t,z) A(theta),

where A=sin2theta when the y derivative count is odd and A=1 otherwise. The angular polynomials are the ordinary Chebyshev T and U polynomials. All potentially negative radial powers are checked to cancel exactly before any interval evaluation. The existing d=4 polynomials give grad rho.

The coefficient functions relevant to the second-derivative energy are

    D²rho, <r>D²rho, <r>²D³rho, <r>D²U,
    omega D²rho, omega D³rho, omega D²U,
    Db/sqrt(v), S=(v_xy rho_x-v_xx rho_y-v_x rho_xy+v_y rho_xx)/2,

with omega=(1+4r²)^(2/5), v=omega² and b=v grad rho. Every tensor norm is its full Frobenius norm, counting mixed derivatives with their binomial multiplicities.

## The differentiated weighted coefficient

Write rho_x=w-sum P_x sin2theta, rho_y=w-sum P_y, and use P_xx,P_xy,P_yy for the d=5 polynomials of D²rho, whose angular factors are sin theta, cos theta, sin theta. Factoring

    sqrt(t) (1-t)^(1/10)(1+3t)^(-3/5)

from Db/sqrt(v), its four polynomial entries are

    xx: (1+3t)P_xx+(32/5)(1+z)P_x,
    yx: (1+3t)P_xy+(32/5)(1-z)P_x,
    xy: (1+3t)P_xy+(32/5)P_y,
    yy: (1+3t)P_yy+(32/5)P_y.

Their angular factors are sin theta, cos theta, cos theta, sin theta. The sums over w^(j+1) are implicit. These formulas are direct differentiation of v, since grad v=(32/5)X(1+4r²)^(-1/5).

The scalar S has common radial factor

    (1/2)(1-t)^(1/5)(1+3t)^(-6/5)

and branch polynomial

    -(128/25)t(1-z²)P_x
    +[-32/5(1+3t)+(128/25)t(1+z)]P_y
    -(16/5)t(1+z)(1+3t)P_xy
    +(16/5)t(1-z)(1+3t)P_xx.

This retains all terms from the exact gradient identity, including the mixed derivatives of the weight. A direct Cartesian jet comparison is required in the certificate audit.

## Interval proof method and status rule

Convert each polynomial on [0,1]x[-1,1] to a tensor Bernstein basis. On a binary subrectangle, the polynomial range lies in the convex hull of its Bernstein coefficients. Treat w on its exact monotone interval and take a further degree-four Bernstein hull in w. The positive radial and angular factors are bounded on the same rectangle. Summing the squared component bounds with their tensor multiplicities bounds each stated Frobenius norm. For S use its absolute value.

Subdivision only improves the cover and does not decide truth through floating-point samples. Every accepted leaf must pass all desired inequalities with Arb intervals. The retained leaves must form a complete binary partition, including the compactified endpoint t=1. An independent audit must reconstruct every leaf at greater precision from the exact polynomials, verify coverage and hashes, and compare the polynomial formulas with finite Cartesian jet values. Only after this audit does a numerical target become a certified bound. The current status and targets are recorded in the certificate JSON and chronological verifier ledger, not inferred from this derivation alone.

## Completed bounds and additional matrix certificates

The certificate sharp_coefficient_certificate.json has663 leaves and status COMPLETE. The independent audit regenerates every exact polynomial from the recovered checkpoint, recomputes every leaf at384 bits, verifies the exact binary partition and hashes, and compares all20 scalar component formulas at seven rational points with independent sixth-order Cartesian potential jets. It explicitly rejects non-finite values. All checks pass. Therefore, globally on the plane,

    |D²rho|_F <=3, <r>|D²rho|_F <=8, <r>²|D³rho|_F <=32,
    <r>|D²U|_F <=3, omega|D²rho|_F <=8,
    omega|D³rho|_F <=10, omega|D²U|_F <=3,
    |D(v grad rho)|_F/sqrt(v) <=28, |S|<=40.

All input functions extend smoothly to r=0; the compactified inequalities include that endpoint and the limit at infinity. Quadrant parity makes the tensor and matrix bounds global.

Two further exact-polynomial matrix certificates use the previously derived formulas. The unweighted first-derivative matrix M1=(I-sym DU)+A is at least(9/10)I: state131_high_symbol_k1_adaptive_unweighted09.json has153 leaves. Its independent384-bit full-tree audit is unweighted_M1_09_audit.json, and the finite Cartesian comparison in audit_high_symbol_points.json includes precisely k=1,sigma=0.

The matrix N=(1/2)[[rho_yyy,-rho_xyy],[-rho_xyy,rho_xxy]] obeys N<=I. The certificate state131_N1_certificate.json has849 leaves. It bounds I-N below by applying the exact Bernstein lower-eigenvalue formula to the sixth-derivative polynomials of AUXILIARY_CERTIFICATE_PROOF.md. Its independent384-bit traversal verifies all leaves and exact coverage; the minimum recomputed margin exceeds0.00035275. The separately rerun sixth-order Cartesian checks validate the derivative formulas, including axis values and explicit finiteness checks. Evidence is state131_N1_audit.json and 02_energy/verification/auxiliary_field_crosschecks.json.

## Weighted third velocity and fourth density derivatives

For d=7, the same exact polar recurrence gives

    D^7 chi=sqrt(t)(1-t)^(3/2) sum_(j=0)^3 w^(j+1) P_j(t,z) A(theta),

where A is sin theta for an odd number of y derivatives and cos theta otherwise. The collected radial power is k-4+l; all negative powers cancel exactly. Thus multiplying D^3U and D^4rho by omega gives the additional factors

    (1-t)^(3/5)(1+3t)^(2/5),
    sqrt(t)(1-t)^(11/10)(1+3t)^(2/5),

respectively, outside the branch polynomial sums. Tensor components follow directly from U=(-chi_xyy,chi_xxy) and rho=-chi_xxy-chi_yyy. The exact polynomials have bidegree at most(28,12).

The complete certificate extra_coefficient_certificate.json contains315 leaves and proves

    sup omega |D^3U|_F <=10,
    sup omega |D^4rho|_F <=128.

The independent script audit_extra_coefficients.py regenerates the exact polynomial data from the recovered original checkpoint, audits every leaf at384 bits, checks the full partition, and compares all13 distinct components against independent seventh-order Cartesian potential jets at seven rational points. All values are required to be finite. The maximum recomputed cell bounds are below9.89114 and127.80648. Certificate SHA256 is9fb31c51cb7162d046349c9616769b430b4f9db9e2ee4d4287da8d40884c1156; exact polynomial SHA256 is724e9a743096fffa456a3ff05a40ae6849820d7d0802d2f18dc6567e6a4ebf5a. These are global continuum inequalities, including the origin and compactified infinity.

For the sum of individual component supremums used in the rough-velocity theorem, do not multiply a pointwise Frobenius bound by only the square root of the number of components: maxima may occur at different points. The safe component count gives

    |c| <=2,
    sum sup |Du_ij| <=6,
    sum sup omega |D^2u| <=8*3=24,
    sum sup omega |D^3u| <=16*10=160,
    sum sup |D rho| <=2*11=22,
    sum sup omega |D^2rho| <=4*8=32,
    sum sup omega |D^3rho| <=8*10=80,
    sum sup omega |D^4rho| <=16*128=2048.

Their sum is2374<4096. The Du and D rho component bounds are independently audited in the earlier auxiliary certificate. This estimate retains all ordered tensor multiplicities.

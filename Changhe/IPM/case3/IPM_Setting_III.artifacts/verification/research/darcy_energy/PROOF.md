# Weighted Darcy identity with its pressure gauge

Status: CONFIRMED after independent derivation/checking and completed Opus 5.5 review 10. Date: 2026-10-20. The actual returned model was claude-opus-5-5; the review is in ../../evidence/opus_review_10/answer.md. Its suggestions were independently checked.

## Statement and hypotheses

Let a smooth primary profile satisfy the complete PDE, symmetry, growth and canonical inverse assumptions in PROMPT.md. Write p=1/c_l, W=c_l X+U and c=psi_xy(0)=1-c_l. Choose the pressure P by

    grad P=-U-rho e_2,   P(0)=0.

The curl of the right side is zero by the defining velocity law, so such a smooth pressure exists on the plane. For every p+3<m<4 the following integrals are absolutely convergent and satisfy

    integral r^(-m)|U|^2
      +[(m-3)c_l-1] integral r^(-m)y rho
      +m integral r^(-m-2)(P+y rho)(U.X)=0.             (1)

All integrals use plane area measure. No term involving U.X is asserted to have a sign. This identity is not a nonexistence theorem.

## Convergence

The origin identities and symmetries give

    rho=a0 y+O(r^3), U=c(-x,y)+O(r^3),
    P=(c/2)x^2-((c+a0)/2)y^2+O(r^4).

Consequently each integrand in (1) is O(r^(2-m)) at zero; its absolute radial integral is finite when m<4. The canonical far-field theorem in ../far_field_holder/PROOF.md gives rho,U=O((1+r)^p) globally, after increasing the constant on a compact set. Integrating grad P along a radial segment gives P=O((1+r)^(p+1)). At infinity the first and third absolute radial integrands are O(r^(2p+1-m)), and the second is O(r^(p+2-m)). Since p<1 and m>p+3>2p+2, all three are integrable.

The normalization P(0)=0 is material to this statement of absolute convergence. With P(0) nonzero, the pressure contribution has the leading integrand m P(0)c r^(-m)(sin(theta)^2-cos(theta)^2). Since c=1-c_l is nonzero, its absolute integral at zero diverges in the stated range of m. Nevertheless its circularly truncated contribution is exactly zero: at every radius, div U=0 implies integral_0^(2pi) U(r,theta).X dtheta=0. Thus (1) also holds for any pressure constant if the third integral is defined as the limit over annuli {epsilon<r<R}, epsilon tending to zero and R to infinity. This convention must be stated if that gauge is used.

## Integration by parts

For Omega={epsilon<r<R}, put w=r^(-m), I=integral_Omega w|U|^2 and Q=integral_Omega wy rho. The Darcy relation dotted with U gives

    I=-integral_boundary wP U.n + integral_Omega P U.grad w
        -integral_Omega w rho U_2.                    (2)

The transport equation gives

    W.grad(y rho)=(c_l+1)y rho+U_2 rho.

Since div W=2c_l and grad w=-m r^(-m-2)X, integration yields

    integral_Omega w rho U_2
      =integral_boundary wy rho W.n
        +[(m-3)c_l-1]Q
        +m integral_Omega r^(-m-2)y rho(U.X).          (3)

Substitute (3) into (2). The left side of (1) on Omega equals

    -integral_boundary w[P U.n+y rho W.n].            (4)

At the inner boundary the absolute flux is O(epsilon^(4-m)). At the outer boundary its two parts are O(R^(2p+2-m)) and O(R^(p+3-m)). They vanish in the stated range. Passing to the limits proves (1).

For an arbitrary smooth canonical pair, with R_tr=W.grad rho-rho, the same calculation gives the left side of (1) equal to integral r^(-m)y R_tr, provided all terms and boundary limits converge. This is a useful manufactured sign check; it does not replace imposing the PDE.

## Pole at m=4

As m increases to 4 the three terms have respective coefficients of 1/(4-m)

    2 pi c^2,
    pi a0(c_l-1),
    pi c(a0-2c).

Their sum is pi a0(c_l-1+c)=0. To obtain the third coefficient, use P+y rho=(c/2)x^2+((a0-c)/2)y^2+O(r^4), U.X=c(y^2-x^2)+O(r^4), and the elementary circle integrals of cos^4 theta, sin^4 theta, and cos^2 theta sin^2 theta. The origin pole cancels by the center identity and supplies no additional sign obstruction. The separate integrals still diverge at m=4; equation (1) is only asserted for m<4.

## Dependencies and scope

Dependencies: canonical inverse, primary center identities, and the proved p-growth of the velocity. The same integration-by-parts formula works under other hypotheses that ensure the displayed boundary and absolute-integrability estimates, but such variants must state those hypotheses separately. The lead's ANALYSIS E.5 formula agrees with (1); its allowance of a pressure constant requires either the gauge P(0)=0 or explicit circular truncation.

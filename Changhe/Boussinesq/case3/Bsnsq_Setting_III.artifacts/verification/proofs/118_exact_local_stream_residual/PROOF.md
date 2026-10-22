# Exact first transverse residual coefficients

Written UTC 2026-10-21T03:45:50.917870+00:00, before implementation. Status: complete elementary proof; exact implementation, independent polynomial controls, and twelve reloaded archive certificates CONFIRMED. This is a certificate for an individual serialized field, not a lower bound for nearby fields.

## Statement

Let beta>2, s=1/beta, R=sqrt(1+x^2+y^2), and let C_ijd,D_ijd be finitely many rational coefficients, with i,j nonnegative integers and d in{0,1}. Define

    p=sum C_ijd x R^(1-s-d) T_i(2R^-s-1)T_j(y/R),
    Psi=p-x p_x(0),
    Theta=sum D_ijd x^2 R^(-1-2s-d)T_i(2R^-s-1)T_j(y/R),
    V=(-Psi_y,Psi_x), Omega=-DeltaPsi, W=beta X+V.

Assume beta is rational. The following moments and residual Taylor coefficients are rational and determined exactly by the coefficients. Write v_j=T_j(0), w_j=T_j'(0), k=1-s-d for each basis term, and put

    a0 = sum D_ijd v_j,       a1 = sum D_ijd w_j,
    c0 = sum C_ijd w_j,
    b0 = -sum C_ijd[4(k-2i^2s)-j^2]v_j,
    c1 = sum C_ijd[k-2i^2s-j^2]v_j,
    b1 = sum C_ijd[-6k+5+12i^2s+j^2]w_j.           (1)

Then a0=Theta_xx(0)/2, a1=Theta_xxy(0)/2, c0=Psi_xy(0), c1=Psi_xyy(0), b0=Omega_x(0) and b1=Omega_xy(0). The coefficients of x^2 and x^2y in R_Theta=W.gradTheta-(beta-2)Theta are respectively

    f0=(beta-2c0+2)a0,
    f1=(2beta-c0+2)a1-2a0 c1.                      (2)

The coefficients of x and xy in R_Omega=W.gradOmega+Omega-Theta_x are respectively

    g0=(beta-c0+1)b0-2a0,
    g1=(2beta+1)b1-c1 b0-2a1.                      (3)

If any coefficient in(2),(3) is nonzero, the serialized field does not solve the B2 PDE even on a neighborhood of0. If all vanish, no conclusion is made about higher Taylor coefficients or the PDE away from0. In the normalized center chart c0=1+beta/2 and b0=4a0/beta, f0=g0=0 and f1=(1+3beta/2)a1-2a0c1.

## Center moments

The identities T_i(1)=1, T_i'(1)=i^2 and T_j''(0)=-j^2v_j follow from the Chebyshev recurrence or differential equation. Differentiating (1-z^2)T_j''-zT_j'+j^2T_j=0 once at0 gives T_j'''(0)=-(j^2-1)w_j. Set r^2=x^2+y^2. Since R^k=1+kr^2/2+O(r^4), R^-s=1-sr^2/2+O(r^4), and y/R=y-yr^2/2+O(r^5), the raw stream term through degree4 is

    x{v_j+w_j y+(k/2-i^2s)v_j r^2-j^2v_j y^2/2
        +[(k-1)/2-i^2s]w_j y r^2
        -(j^2-1)w_j y^3/6}+O(r^5).                (4)

Terms represented in O(r^5) have vanishing derivatives through order4 at0. This follows from the convergent Taylor expansions of the elementary factors near0; parity eliminates omitted lower powers. The affine gauge subtraction has no effect on the derivatives in(1).

The coefficient of xy in(4) is w_j, giving c0. The coefficient of xy^2 is (k/2-i^2s-j^2/2)v_j, giving c1 after multiplying by2. Taking -Delta of the cubic terms gives b0. For the quartic terms, Delta(xyr^2)=12xy and Delta(xy^3)=6xy. Their contribution to Omega_xy is therefore

    -12[(k-1)/2-i^2s]w_j+(j^2-1)w_j,

which equals the stated b1 coefficient. The temperature expansion begins x^2(v_j+w_j y)+O(r^4), so its first two divided coefficients are a0,a1. Summing these elementary formulas proves(1).

## Residual coefficients

Parity and the definitions give near the axis

    Theta=x^2[a0+a1y+O(r^2)],
    Omega=x[b0+b1y+O(r^2)],
    W1=x[(beta-c0)-c1y+O(r^2)],
    W2=(beta+c0)y+O(r^2).                          (5)

There is no constant term in W2 because of the relative gauge. To compute x^2y in the temperature residual, only the displayed terms are needed: the constant divided coefficient of W1 Theta_x is2(beta-c0)a0, its y coefficient is2(beta-c0)a1-2c1a0, and W2 Theta_y contributes(beta+c0)a1y. Subtracting(beta-2)Theta gives(2). Terms in O(r^2) in the divided quantities contribute only total degree at least4.

For the vorticity residual, W1 Omega_x contributes (beta-c0)b0 at orderx and [(beta-c0)b1-c1b0] at orderxy; W2 Omega_y contributes(beta+c0)b1 at orderxy. Adding Omega-Theta_x gives(3). Terms not displayed in(5) have total degree at least3 in this residual.

A nonzero Taylor coefficient is a nonzero derivative at0 divided by its multi-index factorial. A residual that vanishes on a neighborhood has every such derivative equal to0. Thus exact nonzero coefficients prove the claimed local rejection. Rational arithmetic suffices for(1)-(3), but imported coefficients and every certificate value must be checked against the serialized input and its digest. A numerical optimizer flag is not part of the argument.

## Scope and controls

This test does not assert that the stored coefficients approximate a true profile, that a nonzero coefficient stays separated from0 under refinement, or that vanishing of finitely many coefficients solves the PDE. For a normalized a0!=0 field it also verifies the local nontriviality condition independently of any residual norm. Smoothness, parity and the canonical inverse for these stream fields are proved in packet116; the local rejection itself only uses their explicit elementary formulas.

As a control, Psi=c0 xy-b0 x^3/6 and Theta=a0x^2 with c0=1+beta/2,b0=4a0/beta solve both displayed PDEs as polynomial fields and have f0=f1=g0=g1=0. Their velocity grows quadratically and their vorticity grows linearly, so this control is outside the admissible class and is not an existence result. It checks the signs of(2),(3).

Dependencies: finite Taylor expansion, Chebyshev identities proved in the text, and the PDE/gauge definitions. No integration by parts or behavior at infinity is used in the rejection certificate. No Lean proof or build is claimed.

# Independent physical residual from a mixed-coordinate generating function

Written UTC: 2026-10-21T01:57:20.486072+00:00
Status: exact identities proved below before implementation. Own24 polynomial checks and three archived-pilot audits completed2026-10-21T02:03:51Z; finite-point results are in verification and do not prove global hypotheses.

## Definition and hypotheses

Let S(q,y) be C4 on a mixed-coordinate neighborhood where J=S_qy>0. Set x=S_y(q,y). The inverse function theorem makes (q,y) local physical coordinates. Write A=S_yy/J. For a function h(q,y), physical differentiation is

    D_x h=h_q/J, D_y h=h_y-A h_q.                         (1)

Let beta>2,p=beta/2-1,mu=3beta/2+1,a0!=0. Define

    Psi=2beta S-p q S_q-beta y S_y,
    V=(mu S_q-p q S_qq)/J,
    W1=pq J+S_yy V, W2=V, Theta=a0q².

These are the kappa=0 chart formulas from packet100. They construct a local divergence2beta field and exact temperature transport, but do not assume a canonical whole-plane inverse, properness, sublinear growth or the remaining vorticity equation. A stored generating-function pilot is not a solution merely by satisfying these definitions.

## A rational formula using derivatives through order4

The defining prompt equation is W dot grad Omega+Omega=Theta_x, with -Delta Psi=Omega; this fixes both signs in(6).

Write S_ij=partial_q^i partial_y^j S. Repeated differentiation of the displayed Psi gives, for every i+j<=3,

    Psi_ij=(2beta-p i-beta j)S_ij-pq S_(i+1,j)-beta y S_(i,j+1). (2)

Define J_i as a partial derivative of J, and A_i,A_ij as partial derivatives with index i,j in{q,y}. Quotient differentiation gives

    A_i=(S_yyi-A J_i)/J,
    A_ij=(S_yyij-A_i J_j-A_j J_i-A J_ij)/J.               (3)

Set B=J^(-2)+A² and C=-J_q/J³-A_y+A A_q. Applying(1) twice, including derivatives of J and A, yields

    Omega=-Delta Psi=-[B Psi_qq-2A Psi_qy+Psi_yy+C Psi_q]. (4)

For i=q ory,

    B_i=-2J_i/J³+2A A_i,
    C_i=-J_qi/J³+3J_q J_i/J⁴-A_yi+A_i A_q+A A_qi,
    Omega_i=-[B_i Psi_qq+B Psi_qqi-2A_i Psi_qy-2A Psi_qyi
                +Psi_yyi+C_i Psi_q+C Psi_qi].            (5)

Every quantity on the right uses derivatives of S of order at most4. Equations(2)-(5) follow by the product and quotient rules, so require no differentiation of a numerically constructed Omega field. Physical Omega_x=Omega_q/J and Omega_Y=Omega_y-A Omega_q. Consequently the actual unforced vorticity residual and its physical term normalizer are

    R=pq Omega_q+V Omega_y+Omega-2a0q/J,
    N=|W1 Omega_x|+|V Omega_Y|+|Omega|+|2a0q/J|.          (6)

The first term in(6) follows because q-dot=pq for W. The normalizer keeps its two physical advection components separate; it is not a fitted or floored denominator. At N=0,R=0 use ratio0, and at N=0,R!=0 use infinity.

## An independent exact manufacture

For any real h take S=q y+(h/3)q³. Then x=q,J=1,

    Psi=(1+beta/2)xy+h(1+beta/6)x³,
    Omega=-h(beta+6)x,
    W1=p x, W2=mu y+h(beta/2+3)x²,
    R=-[h beta(beta+6)/2+2a0]x.                            (7)

This follows by direct Cartesian differentiation of the polynomial Psi, independently of(2)-(5). In particular h=-4a0/[beta(beta+6)] makes the local defining PDEs exact, but the resulting velocity has quadratic growth and fails the prompt's admissible full-plane class. This is solely a manufactured check; no solution endpoint is claimed.

## Independent numerical design

The evaluator reads only serialized coefficients. It does not import or execute the lead's Jet or solver code. S is evaluated pointwise through a separately bracketed monotone root for log R and a Chebyshev recurrence. Tensor product finite-difference weights are derived from exact rational moment equations. An odd stencil with9 or11 nodes in each variable estimates the derivatives in(2)-(5) from high-precision values. Multiple step sizes and stencil orders check differentiation. Unlike the lead's fourth-order automatic jets, this uses value-only differentiation and an independently solved implicit radius.

Numerical tests establish finite-point residual estimates only. Small J can amplify error; nonpositive J invalidates the local chart and is reported separately. Global properness, full-plane inversion and far-field growth need separate verification. No conclusion about those follows from a good finite-point residual. All coefficient inputs and tested archive hashes are recorded in exact JSON, with no hardcoded large tables in the proof source. No Lean/Lake build is used.

## Additional nonlinear manufacture and radius uniqueness

For d=0.13,h=-0.07 take S=(y+d y²/2)sinh(q)+h q³/3. Its physical chart is x=(1+d y)sinh(q), so q=asinh(x/(1+d y)) and J=(1+d y)cosh(q)>0 on y>-1/d. Direct high-precision differentiation of the explicit physical Psi(x,y) tests all quotient-rule terms against the mixed finite-difference evaluator. Eighteen checks at three beta values, three points, and two steps pass with maximum relative discrepancy6.50e-34. This supplements the polynomial test where J was constant.

The stored radial ansatz solves g(logR)=q²exp(-2a logR)+(1+y²)exp(-2logR)-1=0, a=1/2-1/beta>0. It is strictly decreasing, with g(0)>=0 and limit-1; hence its R>=1 root is unique, and the derivative is strictly negative there. The implicit root is smooth everywhere, including q=0, and the bracketed evaluator cannot choose a different branch. The finite-difference stencil differentiates this globally defined S, so its values need not themselves lie in an invertible physical chart; only the target point requires J>0 for the local physical formulas. No global injectivity or properness is inferred.

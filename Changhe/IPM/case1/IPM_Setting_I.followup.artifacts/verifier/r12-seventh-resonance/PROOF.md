# Seventh-order test at the R12 fifth resonance

Date: 2026-10-20. Status: complete exact proof with two independent implementations. This is a conditional obstruction for prescribed axis data, not a global endpoint.

## Exact setting

For 0 < x < 2 prescribe the axis data

    w(x) = -2x(1-x^2/4)/(1+x^2/4),
    g(x) = x^2/(1+x^2/4),     h(x)=3-w'(x).

Here A=2, c_l=3/2, g is the coefficient of y in the density, and the parity is rho even in x and odd in y. The velocity W has coefficients

    W_1=w+a_2 y^2+a_4 y^4+a_6 y^6+...,
    W_2=h y+b_3 y^3+b_5 y^5+b_7 y^7+...,
    rho=g y+G_3 y^3+G_5 y^5+G_7 y^7+....

These are prescribed axis data, not a claimed coupled profile. The third and fifth traces are selected by zero normalized source limits at x=2. The uniquely selected formulas are

    G_3 = 4(x/2)^2/[3(1+(x/2)^2)^3],
    G_5 = x^2(11x^6+88x^4-1872x^2+9984)/(90(x^2+4)^5).

Substitution in their hierarchy equations gives zero residual exactly. Both formulas are bounded at x=2, while H_3 and H_5 diverge there, so they satisfy the selection and are unique. The derivation below reconstructs the hierarchy directly from the equations.

## Hierarchy and finite-part protocol

The equations are W.grad rho=rho, div W=3, and partial_x W_2-partial_y W_1=-partial_x rho. Equating powers of y in the last two equations gives

    a_2=(g'-w'')/2, b_3=-a_2'/3,
    a_4=(b_3'+G_3')/4, b_5=-a_4'/5,
    a_6=(b_5'+G_5')/6, b_7=-a_6'/7.

In transport the terms contributing at degree seven are wG_7', 7hG_7, a_2G_5', a_4G_3', a_6g', 5b_3G_5, 3b_5G_3 and b_7g. Hence

    wG_7'+(7h-1)G_7=F_7,
    F_7=-a_2G_5'-5b_3G_5-a_4G_3'-3b_5G_3-a_6g'-b_7g.

The normalized homogeneous solution is

    H_7=x^17(1+x^2/4)^(-7)(1-x^2/4)^(-3).

Its logarithmic derivative is (1-7h)/w, and H_7/x^17 tends to one at zero. Its source exponent is -3. The finite part is defined by subtracting exactly the divergent lower-end powers and logarithms, without adding a finite constant:

    B_7=-FP integral_0^2 F_7/(wH_7) dx.

All lower traces displayed above are rational with poles only at imaginary x. Thus F_7 is smooth at x=2 and F_7/(wH_7)=O((2-x)^2); the upper endpoint is integrable. Integrating (G_7/H_7)'=F_7/(wH_7) gives, for every solution, its center homogeneous coefficient C_{0,7}=ell_7+B_7, where ell_7=lim_{x->2}G_7/H_7. Its existence follows from that endpoint integrability.

The exact value is

    B_7 = -23/29059430400 != 0.

The corresponding natural unit coefficient is 2^11 B_7=-23/14189175, since the rescaling power is p_7-7+1=11.

Consequently ell_7=0 is incompatible with smooth even G_7 at zero: the homogeneous exponent is the odd integer17. With ell_3=ell_5=ell_7=0 these prescribed axis data admit no profile smooth at the center. More precisely such a density cannot be C^24 near the center, since that regularity would make G_7=partial_y^7 rho/7! an even C^17 function of x. This does not exclude every admissible axis trace.

At A=2 the source endpoint theorem with n=2,4,6 has thresholds0,-1,-2, respectively. Therefore if 0<alpha<1 and both density and velocity are C^(6,alpha) near the source, it forces ell_3=ell_5=ell_7=0 for a profile smooth along the punctured axis and satisfying the stated transport, divergence, parity and source linearization. In this example w'(2)=2, h(2)=1, g(2)=2, so those source linearization data agree. Canonical velocity regularity can supply the velocity hypothesis when the appropriate full-plane density assumptions hold, but that deduction is a separate dependency. This endpoint theorem is a separate dependency, proved in ../source-estimates/PROOF.md and audited in ../cone-endpoints/PROOF.md. Smoothness at the center alone does not impose source selections.

## Exact evaluation

Write D=x^2+4 and

    P(z)=33z^5-5324z^4-115472z^3+3577280z^2-20143104z+30892032.

Direct differentiation in the stated hierarchy gives

    F_7 = 2x^2 P(x^2)/(945D^8),
    -F_7/(wH_7) = (x^2-4)^2 P(x^2)/(990904320x^16).       (1)

These identities can be checked solely with polynomial arithmetic. For example all six terms defining F_7 have a common denominator D^9 and a numerator of degree at most14. Multiplication by D^9 and collection of coefficients cancels one factor D and gives the first identity in (1). The factor 990904320 is 945 times4^10, from the normalization of H_7. It is essential to retain this normalization.

Let d_k be the coefficient of z^k in (z-4)^2P(z), 0<=k<=7. The integrand in (1) is the Laurent polynomial sum_k d_k x^(2k-16)/990904320. None of its exponents is -1. A primitive with no constant term is therefore

    J(x)=1/990904320 sum_(k=0)^7 d_k x^(2k-15)/(2k-15).

Every exponent in J is negative, so the finite part at zero is exactly zero. Thus

    B_7=J(2)
       =1/990904320 sum_(k=0)^7 d_k 2^(2k-15)/(2k-15)
       =-23/29059430400.                                  (2)

Equations (1) and (2) provide an exact rational calculation without a numerical quadrature limit. The expanded Laurent coefficients and both independent arithmetic reconstructions are retained in verification/check.json and verification/series.json.

## The center obstruction and the source selection

The unique source-selected seventh solution is

    G_7(x)=H_7(x)[B_7-J(x)].                              (3)

Its transport equation follows by differentiating (3), since J'=-F_7/(wH_7). At x=2, J(2)=B_7 and J'(x)=O((2-x)^2), so B_7-J(x)=O((2-x)^3). This cancels the cubic pole of H_7. In particular G_7/H_7 tends to zero there. Every other solution differs by ell_7 H_7.

Near zero, H_7=x^17 T(x^2), where T is analytic and T(0)=1. The primitive J is an odd Laurent polynomial, with lowest power x^(-15) and highest x^(-1). Hence -H_7 J is an even analytic function whose lowest possible power is x^2. Formula (3) has the exact decomposition

    G_7=an even analytic function + B_7 x^17 T(x^2), x>0.

Its coefficient at the odd power x^17 is B_7, which is nonzero. The even extension required by the density parity replaces this term by B_7 |x|^17 T(x^2). Its seventeenth derivative has opposite one-sided nonzero limits at zero. Therefore G_7 has no even C^17 extension, proving the smooth-center obstruction under the three source selections. A general source constant would instead give coefficient B_7+ell_7; it cancels the obstruction exactly at ell_7=23/29059430400. No argument here prohibits that constant under baseline source regularity alone.

The smooth fifth trace is not contradicted by this argument. At order five the center exponent is12, and the finite part 11/1474560 multiplies a smooth even homogeneous term. At order seven the exponent17 is odd, so that exception no longer applies. These distinct parity conditions are why the seventh calculation is necessary.

## Independent verification and limitations

code/check.py differentiates the rational w,g,G_3,G_5, reconstructs a_2 through b_7, verifies both lower transport equations, all three homogeneous equations, the primitive, (3), and the source limits. It uses exact SymPy rational algebra. code/check_series.py is a separate implementation using only Python Fraction arithmetic and center power-series convolution. It reconstructs the hierarchy, exploits the denominator and degree bounds described above, extracts the Laurent polynomial and evaluates its finite part. It imports no output or code from the first implementation or another lane. The two exact values and all eight Laurent coefficients agree; the checks took2.56seconds and0.017seconds.

The informal hierarchy and finite-part protocol were written before either new computation. Both implementations serve to audit the displayed finite algebra. There is no proof-assistant verification and no Lean or Lake build. No global coupled realization or proximity to the computed candidate has been established. The source C^(6,alpha) assumption is stronger than the baseline class, and fixing w to this exact R12 function is an additional restriction. Therefore this is a restricted necessary-condition exclusion, not NO_inf for the full strong setting and not a verdict authorizing the team to finish.

## Corollary for the entire prescribed R12 family

Let A>1,L>0 and prescribe, on 0<x<L,

    w=-Ax(1-x^2/L^2)/(1+x^2/L^2),
    g=x^2/(1+x^2/L^2), h=A+1-w'.

Suppose the coupled profile equations and parities hold, the fields are smooth along the punctured axis, both rho and W are C^(6,alpha) near P=(L,0) for some 0<alpha<1, and rho is C^24 near the center. These assumptions are incompatible. This is a statement about this particular two-parameter axis family.

To prove it, C^(6,alpha) near P implies C^(2,beta) and C^(4,beta) on a smaller neighborhood for every beta<1: the next derivatives are bounded, giving Lipschitz derivatives of orders two and four. Choose beta>max(0,1-2/A,1-4/A). The source theorem applied at orders two and four gives ell_3=ell_5=0. The source jet has w'(L)=A, h(L)=1, and g(L)=L^2/2>0, as required.

For completeness the exact third finite part is

    B_3=C_A L^(-4-2/A)(1-S_A/L^2),
    S_A=6A(4A-3)/(8A-1),
    C_A=-(8A-1)Beta(-2-1/A,2/A)/[3A(2A-1)]>0.          (4)

This identity does not assume L^2=S_A. Indeed, setting u=x/L, direct differentiation gives

    F_3=-u^2[(6A+3L^2)u^2+5L^2-30A]/[3(1+u^2)^4].

Multiplication by the homogeneous integrating factor and t=u^2 give the two beta terms with a=-2-1/A, q=2/A. Their combination is

    B_3=-Beta(a,q)/(6A L^(6+2/A))
            [5L^2-30A+(6A+3L^2)(2A+1)/(2A-1)].

The bracket is 2(8A-1)(L^2-S_A)/(2A-1), proving (4). The finite-part substitution is justified by subtracting three center Taylor monomials; a lies strictly between -3 and -2, so no logarithmic denominator vanishes. Gamma(a)<0, Gamma(q)>0 and Gamma(a+q)>0 since a+q lies between -2 and -1. Thus C_A>0.

The third exponent p_3=6+2/A is never an even integer. Since G_3 is even and C^21 at the center under the assumed C^24 density regularity, its homogeneous coefficient must vanish. With ell_3=0, (4) therefore forces L^2=S_A. The third trace is now the one used in ../r12-global-sign/PROOF.md.

If A!=2, that proof gives B_5<0. Its exponent p_5=10+4/A lies in(10,14) and is not an even integer. The even C^19 center trace G_5 and ell_5=0 would instead force B_5=0. This is a contradiction. If A=2, the axis scale is L=2. C^(6,alpha) and the sixth-order source theorem give ell_7=0, and the exact seventh obstruction already proved above supplies the contradiction. These cases exhaust A>1.

The two extra restrictions, this exact axis formula and higher source regularity, are not consequences of the problem's admissible class or of the observed numerical branch. The corollary therefore supplies no global NO_inf endpoint. In particular, the R12 family originally served as compatible axis examples; excluding its smoother realizations does not exclude profiles with other axis functions.


## Canonical localization and the finite center hypothesis

For the application to a profile of the original full-plane class, the source assumption can be stated on rho alone: local C^(6,alpha) density regularity, with 0<alpha<1, implies local C^(6,alpha) regularity of U and hence W. This implication uses the canonical inverse and sublinear global density growth. It does not hold merely from local transport and divergence.

Here are its dependencies and the finite derivative count. Choose a smooth compact cutoff chi equal to one on twice the source ball. The canonical inverse is the order-zero multiplier (xi_1 xi_2,-xi_1^2)/|xi|^2 on chi rho plus the far part U[(1-chi)rho]. The multiplier maps compactly supported C^(6,alpha) functions to local C^(6,alpha) functions by the positive noninteger Holder multiplier bound. This is the same standard bound used in the report's Localization paragraph, with exponent 6+alpha instead of 2+alpha. If |rho(Y)|<=C(1+|Y|)^gamma, gamma<1, each derivative of order k>=1 of the far part is bounded by an integral of (delta+|Y-P|)^(-2-k)|rho(Y)|. In polar coordinates its large-radius majorant is r^(gamma-k-1), integrable because k>=1>gamma. The undifferentiated canonical far part exists by the prescribed velocity law, and its differences are absolutely convergent. Differentiation under this majorant proves that the far part is smooth. This proves the required local velocity regularity without a derivative gain or an assumption of decay of rho.

The assertion that C^24 density regularity at the center suffices also has a finite propagation dependency. In the report's one-derivative transport lemma and its induction, replace the region where all derivatives are known by a region where rho is C^24. On compact subsets of that region rho is H^24. Starting from the class H^2 regularity, apply the same finite sequence of localized estimates at k=2,...,23 on nonstationary tubes leading to that region. At the k-th step the forward endpoint has H^(k+1), and the induction gives H^(k+1) on the tube. No step asks for the twenty-fifth derivative. Thus rho and its localized canonical velocity are H^24 on a neighborhood of each point of the open axis segment. In two dimensions H^24 embeds locally in C^(22,beta) for each beta<1. This is more regularity than the hierarchy through order seven requires: the largest axis derivative of w in its seventh forcing is order seven, and the source bound needs only the seventh transverse trace on the punctured axis. The finite source-transport identity can also be used distributionally under C^(6,alpha) near P, as proved in source-estimates.

Consequently the corollary applies to profiles of the original canonical full-plane class with rho C^24 near zero and C^(6,alpha) near P. Its punctured-axis hypothesis follows from the finite iteration just described. This finite iteration depends on the localized energy and product estimates already audited in source-estimates/verification/c1_audit.md and printed in report 6.3.1(f); it is not a new proof of those estimates. The exact R12 axis hypothesis remains essential. The conclusion still gives no endpoint for the entire class.

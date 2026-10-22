# Analytic flow bounds on the inner disk and the exterior

Date: 2026-10-20. Topic71. Status: OPEN pending computation and review. The result concerns the exact repaired modal trial of modal_repair, with canonical whole-plane inverse, k=1615536043799051/9007199254740992, c_l=1/k and c=3c_l-1. It gives no inverse of the coupled IPM operator and no existence or exclusion endpoint.

## Statement and dependencies

Let V=c_l X+U, s=X.V/r^2, v1=V1/x, v2=V2/y, with continuous limits on the two axes. Use the conic rate

 T=-(1+c_l)+a v1+b v2+(mu(r)-S)s,
 a=129/20, b=307/100, S=a+b, gamma=1129/1000,
 mu(r)=gamma+(S-gamma)/(1+(r/6)^4).

The density has at most261 nonzero stream modes. Let R=exp(t_a) be the exact first spline endpoint. The separately proved and independently computed inner_majorant result supplies nonnegative C_r,C_theta satisfying, on 0<r<=R,

 sum_n |u_n(r)|<=C_r r^3, sum_n |w_n(r)|<=C_theta r^3,
 U-U_lin=sum_n u_n cos(2n theta) e_r+sum_n w_n sin(2n theta) e_theta,
 U_lin=(-cx,cy).

These constants follow from the complete canonical Green integrals in that topic, not from a local density assumption. Its T=0 row covers the whole disk, including the logarithmic and nonpolynomial inner terms. Use the maximum of the exact rational upper endpoints produced by its Arb and independent mpmath.iv calculations.

The separately proved exterior_flow result supplies constants P,Q on r>=R_e=exp(t_b+9), where t_b is the exact final spline knot, such that

 |s-c_l|<=P, |v1-c_l|<=Q, |v2-c_l|<=Q.

Use its T=9 row, again taking the maximum of the two certified rational upper endpoints. Its proof bounds every radius beyond R_e, including the complete canonical homogeneous transient, and both axis quotients. These are already two independent computations; the calculation below rechecks their scalar consequences with two differently factored interval expressions. It does not claim to recompute their Green integrals anew.

## Inner disk proof

By the exact angular identity sin(2n theta)/sin(theta)=2 sum_(j<n)cos((2j+1)theta) and its reflected identity at the other axis,

 |cos(theta)sin(2n theta)/sin(theta)|<=2n,
 |sin(theta)sin(2n theta)/cos(theta)|<=2n.

Polar-to-Cartesian conversion therefore gives, for N=261,

 |s-(c_l-c cos2theta)|<=C_r r^2,
 |v1-(c_l-c)|, |v2-(c_l+c)| <= (C_r+2N C_theta) r^2.

Set D=(C_r+522 C_theta)R^2. This simultaneously bounds all three errors throughout the disk. The axis extensions follow from the finite trigonometric polynomial identities, so division by x or y creates no unproved boundary assumption.

Put L=c_l-|c|-D. Since mu(r)-S lies in [mu(R)-S,0] and s>=L,

 (mu(r)-S)s <= max(0,(mu(R)-S)L).

For L>=0 the left side is nonpositive. For L<0, replacing s by L reverses the inequality after multiplication by the nonpositive factor; its largest possible product with L is (mu(R)-S)L. This proves the formula in both cases. Hence

 v2>=c_l+c-D, v2<=c_l+c+D, v1<=c_l-c+D,
 T<=-(1+c_l)+a(c_l-c+D)+b(c_l+c+D)+max(0,(mu(R)-S)L).

Also R<4.8 will be checked, so this entire inner disk is disjoint from the flow box B=[float(4.8),float(6.82)] x [0,float(2.85)]. Its T bound is consequently an off-box bound. No finite inner-cell run is required for this alternative analytic coverage.

## Exterior proof

The three exterior deviations give

 T<=-(1+c_l)+mu(r)c_l+S Q+(S-mu(r))P
   <=-(1+c_l)+mu(R_e)c_l+S Q+(S-gamma)P.

Here c_l>0 and mu decreases with r; also gamma<=mu(r)<=S. Both replacements are upper bounds. In particular s>=c_l-P and vi>=c_l-Q throughout this exterior. Checking R_e>20 places this tail within the requested far region and outside B. It does not cover all r>=20: the interval20<=r<=R_e still needs the finite middle and outer certificates. This tail overlaps the finite outer certificate whose exact logarithmic endpoint is t_b+17; 9<17 is exact. No comparison of rounded printed endpoint radii is needed.

## Exact y-axis correction to the lead's flow note

The exact modal_repair/PROOF.md definition, including the normalization repair that changes only the mode-zero radial coefficient, is rho=x^2 y sum_(m=0)^259 a_m(r)cos(2m theta). This is a global definition, not an inference from parity. Each individual angular factor obeys

 cos²(theta)sin(theta)cos(2m theta)
 = [sin((2m+1)theta)+sin((1-2m)theta)+sin((2m+3)theta)+sin((3-2m)theta)]/8.

 At theta=pi/2 the four terms sum to zero for every integer m. Thus the alternating sum vanishes separately for every radial coefficient, every inner or outer family, every spline span, and also for the exact-real normalization correction. The audit checks this coefficient identity for all260 inputs without making any assumption about their values. No separate cancellation between numerical approximations is used.

 For this exact modal trial rho=x^2 y A(r,theta), every point (0,y0), y0!=0 has a neighborhood on which the finite radial and angular factors are C^1. Differentiating this identity gives rho(0,y)=rho_x(0,y)=rho_y(0,y)=0. At the origin the proven local regularity gives the same values. For X3 itself equation(ansatz) in PROMPT.md defines rho=x²y exp(H), where H is C¹ near any nonzero point of the y-axis for the stated p3>6 and finite radial splines. It has the same factor and the same conclusion. Consequently b_+=(|grad rho|-rho_y)/2 is exactly zero on the y-axis for each trial. The assertion in lead notes/global_flow.md lines250-252 that this trial's y-axis value is merely of residual size is false. Floating evaluation with cos(pi/2) unequal to zero does not change the exact identity. Parity alone would indeed be insufficient, but the trial has the stronger global factorization.

On the x-axis rho_x=0 follows by differentiation of rho(x,0)=0, so b_+=(-rho_y)^+. Positivity of rho_y is a separate assertion. No claim of a uniform coupled energy gap follows from either observation.

## Computation and scope

Before accepting numerical bounds, verify the two dependency verdict hashes and all files they pin; read the exact rational values rather than printed displays. Compute the inner and outer consequences using Arb512 and mpmath.iv180, record exact rational endpoints, and audit the public decimals by exact comparisons. A fresh higher-precision evaluation must contain the same exact input data and independently check the scalar formulas. Record all times and actual model-review provenance. No endpoint is implied even if all checks pass. The finite middle field bounds, any needed finite outer interval, and the nonlocal inverse remain separate obligations.

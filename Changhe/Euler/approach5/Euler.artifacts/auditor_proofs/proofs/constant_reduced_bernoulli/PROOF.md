# Constant reduced Bernoulli function forces a sublinear profile to vanish

## Statement and notation

Let 0<c<1/2 and omega be any finite real number. Suppose U is C2 on R3, P is C1, div U=0, and

    (1-c)U + ((cI-omega J)y+U).grad U + omega J U + grad P=0.

Assume U(y)=o(|y|) uniformly as |y| tends to infinity. Set A=cI-omega J, B=Ay+U, q=|U|^2/2, Omega=curl U and a=1-2c. If the reduced Bernoulli function

    H=P+q+(Ay).U

is spatially constant, then U=0 and P is constant. Constancy of this particular H is an extra hypothesis. No inference of it from decay, zero total helicity, or zero helicity density is made.

The proof below is independent of pressure normalization, a pressure representation formula, any unproved Liouville theorem, and any dynamical classification.

## 1. A positive-stress lemma

Suppose V is continuous, Q is continuous and nonnegative, and

    partial_i partial_j(V_i V_j)+Delta Q=0

in distributions. If for some sequence R tending to infinity

    R^(-1) integral_(R<|y|<2R)(|V|^2+Q) -> 0,

then V=0 and Q=0.

To prove this, let psi(y)=sqrt(1+|y|^2). Its Hessian has one eigenvalue (1+|y|^2)^(-3/2) and two eigenvalues (1+|y|^2)^(-1/2), all strictly positive. Also Delta psi=(3+2|y|^2)/(1+|y|^2)^(3/2)>0. Take a smooth radial cutoff chi_R equal to one on the radius-R ball and zero beyond radius 2R, with values in [0,1] and first and second derivatives bounded by C/R and C/R^2. Testing the equation against chi_R psi gives

    0=integral chi_R [V^T D2psi V+Q Delta psi]+Err_R.

On the cutoff annulus, |grad psi|<=1 and psi<=3R for R>=1. The product-rule terms therefore satisfy

    |Err_R|<=C R^(-1) integral_(R<|y|<2R)(|V|^2+Q).

For each fixed radius L and R>L, the nonnegative main integral dominates its integral on the radius-L ball. Along the assumed sequence the error tends to zero. Thus the latter integral is zero for every L. Strict positivity and continuity give V=0 and Q=0. No integration by parts at infinity has been used.

## 2. The actual pressure becomes nonnegative

The exact rotating Lamb identity is

    Omega cross B=-a U-grad H.

It follows by expanding Omega cross U=(U.grad)U-grad q, Omega cross Ay=(Ay.grad)U-(DU)^T Ay, and grad((Ay).U)=A^T U+(DU)^T Ay. Here A^T=cI+omega J and a+c=1-c.

If H is constant, taking its scalar product with B gives U.B=0 because a>0. Since

    H=P-q+U.B,

we obtain P=q+H. Subtract this constant H from the pressure. The normalized pressure is now exactly q>=0, as a consequence of the equation, not an assumption about the harmonic ambiguity.

Taking divergence of the profile equation gives

    Delta P=-partial_i partial_j(U_i U_j).

For completeness, the linear drift contributes A_ji partial_j U_i, whose skew part is -omega J_ji partial_j U_i; div(omega J U)=omega J_ij partial_i U_j cancels it after relabeling. The c-part and all remaining linear divergence terms vanish with div U. The identity is valid distributionally, which suffices even though only P in C1 was assumed. Consequently V=U and Q=q satisfy the stress equation of Section 1.

## 3. The required energy growth is a direct consequence

The exact energy equation is

    div(q B+P U)=(5c-2)q.

Put E(R)=integral_(|y|<R)|U|^2 and M_R=sup_(|y|=R)|U|. With P=q and (Jy).y=0, the divergence theorem gives

    c R E'(R)-(5c-2)E(R)=-2 integral_(|y|=R)|U|^2 U.n.

Hence

    (cR-2M_R)E'(R)<=(5c-2)E(R).                 (1)

Uniform sublinearity gives M_R/R ->0, so the coefficient on the left is positive for all sufficiently large R.

For c<2/5, the left side is nonnegative and the right side is strictly negative unless E(R)=0. Thus U=0 already.

For c=2/5, (1) forces E'(R)=0 for all sufficiently large R. Therefore E is bounded and E(2R)/R tends to zero.

For 2/5<c<1/2, choose 0<epsilon<min(c/2,1-2c). For all sufficiently large R, M_R<=epsilon R. Then

    E'(R)<=p E(R)/R,
    p=(5c-2)/(c-2epsilon),        0<p<1.

Gronwall gives E(R)<=C R^p, including the case where E at the initial radius is zero. Consequently

    R^(-1) integral_(R<|y|<2R)(|U|^2+q)
        <=(3/2)E(2R)/R ->0.

The positive-stress lemma now applies and gives U=0. The original momentum equation gives grad P=0. This completes the theorem for every stated c and omega.

## 4. Conditional first-integral corollary

Suppose additionally that all geometric hypotheses of the audited no-decaying-first-integral theorem A244 hold with W=Omega, that U.Omega=0 pointwise, and that H tends to a finite common limit H_infinity at spatial infinity. The Lamb identity dotted with Omega gives

    Omega.grad H=-a U.Omega=0.

Thus H-H_infinity is a smooth decaying Omega first integral. A244 forces it to vanish, and the theorem above forces U=0. This application retains the full global geometry of A244, including the proper exceptional line, its exact basin complement, the recurrence conditions, and the compact boundary leaf. These assumptions are not consequences of having one regular attractor. The pointwise helicity condition and finite Bernoulli limit are also extra hypotheses.

## Dependencies and verification

Sections 1-3 use only local vector calculus, compactly supported distributional tests, the divergence theorem, and Gronwall. Section 4 additionally uses A244 at its exact scope. No numerical or formal computation is required. The result is a conditional nonexistence theorem and does not close the main arbitrary-rotation problem.

# Exact candidate screens and profile transformations

All fields are in three dimensions. Write J(x,y,z)=(-y,x,0), M=cI-omega J, and c>0. The profile residual is

\[
 E(U,P)=(1-c)U+DU(My+U)+\omega JU+\nabla P.
\]

## 1. A rigid Euler state that is also a decaying similarity profile is zero

Assume U,P,p are C^2, div U=0, U tends uniformly to zero, E(U,P)=0, and for some finite beta and constant v,

\[
 DU\,U+\beta(JU-DU\,Jy)-DU\,v+\nabla p=0.       \tag{1}
\]

Set delta=omega-beta and A=cI-delta J. Subtract (1) from the profile equation and take curl. Rotation covariance of curl gives

\[
 \Omega+(Ay+v)\cdot\nabla\Omega+\delta J\Omega=0.
\]

A is invertible. The affine characteristic through y is Y(s)=y_*+e^{cs}e^{-delta Js}(y-y_*), where y_*=-A^{-1}v. It tends to y_* as s tends to minus infinity. Along it,

\[
 \Omega(Y(s))=e^{-s}e^{-\delta Js}\Omega(y).
\]

Continuity of Omega near y_* bounds the left side; the norm on the right is e^{-s}|Omega(y)|. Therefore Omega=0. Harmonicity and decay give U=0. This is LIT05, with H0, H1 and the additional equation H9. It is not a theorem excluding arbitrary profiles without (1).

## 2. Affine residual and its examples

For U=Ay+b, trace A=0, direct multiplication gives

\[
 E(U,0)=Cy+d,\quad
 C=A+A^2+\omega(JA-AJ),\quad
 d=((1-c)I+A+\omega J)b.
\]

A pressure can cancel this residual exactly if and only if C is symmetric, in which case P=-y dot Cy/2-d dot y plus a constant. This proves the affine classification asserted in LIT06 without numerical calculations.

For A=diag(-c,-c,2c), C=diag(c^2-c,c^2-c,4c^2+2c), giving

\[
 P=(c-c^2)|y_h|^2/2-(c+2c^2)y_3^2,
 \quad B=-\omega Jy+3cy_3e_3.
\]

All backward trajectories are bounded. If omega is nonzero and y_h is nonzero, their alpha-limit sets are horizontal circles. This is an exact smooth PDE example, but U has linear growth. It refutes only the implication from exact PDE, positive divergence and backward boundedness to point limits, not the implication with sublinearity added.

For A with horizontal block [[-1/2,-beta],[beta,-1/2]] and A_33=1, C has horizontal block -(1/4+beta^2)I and C_33=2. Thus P=(1/4+beta^2)|y_h|^2/2-y_3^2 gives an exact affine vortical profile. Its horizontal B eigenvalues are c-1/2 plus or minus i(beta-omega), and its vertical eigenvalue is c+1. For c<1/2, nonaxial trajectories are unbounded backward. The example violates sublinearity and decay.

For a constant U=b, P=-((1-c)I+omega J)b dot y is exact. At y=e_1 with b=(-c,omega/2,0), X dot B=-omega^2/4. This disproves unconditional pointwise Bernoulli positivity even among exact uniformly sublinear profiles, but the nonzero constant limit fails H1.

## 3. Singular exact examples

For y nonzero, U=grad(1/|y|)=-y/|y|^3 is divergence-free and curl-free. Its degree is -2 and it is rotation-equivariant. The linear profile terms are (1-3c)U and the nonlinear term is grad(|U|^2/2). Therefore

\[
 P=-(1-3c)/|y|-1/(2|y|^4)
\]

makes E=0 away from zero for all omega. This field decays, but is singular and has a distributional source at the origin.

For cylindrical radius r>0, alpha>0, k nonzero and c=1/(1+alpha), take U=k r^{-alpha}e_theta. Its degree cancels the linear terms, its rotation term is zero and DU U=-k^2r^{-2alpha-1}e_r. The pressure P=-k^2r^{-2alpha}/(2alpha) cancels this. The field is singular on the axis and, since it is independent of z, fails full spatial decay even on its domain. Every nonzero negatively homogeneous field similarly fails continuity at its dilation center.

## 4. Kinematic decay examples do not solve momentum

For alpha>0, U=(1+|y|^2)^{-(alpha+1)/2}Jy is smooth and divergence-free: grad of its radial scalar is perpendicular to Jy. It decays at rate |y|^{-alpha}. Direct angular integration gives

\[
 \int_{|y|<L}|U|^2=\frac{8\pi}{3}\int_0^L
             r^4(1+r^2)^{-alpha-1}\,dr.
\]

The integral diverges precisely for alpha<=3/2. It is logarithmic at equality and grows like L^{3-2alpha} below it. Hence smooth divergence-free decay alone is not an L^2 assumption.

The field U=sin(|y|^4)Jy/(1+|y|^2) is also smooth, divergence-free and O(|y|^{-1}). On y=(r,0,0),

\[
 \partial_1U_2=\frac{1-r^2}{(1+r^2)^2}\sin(r^4)
                +\frac{4r^4}{1+r^2}\cos(r^4).
\]

At r=(2pi n)^{1/4} this tends to infinity. Smooth velocity decay alone therefore does not even bound DU.

For an exact field of the form U=f(|y|)Jy, the azimuthal component of the profile residual apart from pressure is r(f+cR f'), where R=|y|. Its angular average cannot be canceled by the angular derivative of a single-valued pressure. Neither scalar f just used solves f+cR f'=0. These are only kinematic implication checks.

## 5. The printed examples in Reference C

The literature agent's archived arXiv 1201.6009v2 text and rendered page 5 were both inspected. Its equation is

\[
 (1+alpha)^{-1}y\cdot\nabla v+alpha(1+alpha)^{-1}v
       =(v\cdot\nabla)v+\nabla q.                      \tag{2}
\]

Equation (11) prints v=(y_2^alpha,0), q=2alpha y_2^{alpha+1}/(1+alpha)^2. On y_2>0 the left side of (2) is 2alpha y_2^alpha e_1/(1+alpha), and the right side is the same scalar times e_2. For alpha not zero or minus one they are unequal. Equation (12) prints v=y_perp/|y|^{alpha+1}, q=0. Its left side is zero; its convective term is -r^{-2alpha-1}e_r. It needs the pressure -r^{-2alpha}/(2alpha) when alpha is nonzero, or log r when alpha=0. These printed examples fail as written. No statement about an uninspected corrected version, or about the validity of the paper's separate Liouville proofs, follows from this check.

## 6. Constant far-field normalization and intrinsic dilation

If E(U,P)=0, define, for any constant h,

\[
 U^h(y)=U(y+h)+Mh,
\quad
 P^h(y)=P(y+h)-(((1-c)I+\omega J)Mh)\cdot y.
\]

Then My+U^h(y)=M(y+h)+U(y+h). In the residual, the derivative terms equal the original translated ones; the only extra constant is ((1-c)I+omega J)Mh, canceled by grad P^h. Thus E(U^h,P^h)=0 and div U^h=0. If U tends to b, choose h=-M^{-1}b to make U^h tend to zero. Invertibility follows from c>0. This proves LIT07. A nonconstant profile with a constant far-field limit could therefore produce a target-class candidate; constants themselves normalize to zero.

For lambda>0, U_lambda(y)=lambda U(y/lambda), P_lambda(y)=lambda^2 P(y/lambda) also solve the same equation at unchanged c and omega, since every momentum term scales by lambda. Decay and smoothness persist, sup|U_lambda|=lambda sup|U|, and DU_lambda(y)=DU(y/lambda). A uniform theorem requiring only sufficiently small sup|U|, with no competing length scale, would imply the full conjecture by this dilation. Small velocity amplitude alone is not a normalization-invariant perturbative condition.

## Audit scope

These calculations confirm LIT05-LIT07 as precisely stated in the literature agent. No nonzero exact example here satisfies both whole-space smoothness and full spatial decay. The identities, elementary integrals and explicit characteristic formulas are analytic proofs; no small numerical residual is used as evidence of exactness.

# Backward stretching and periodic-orbit multipliers

## Exact hypotheses

Let 0<c<1/2 and finite omega be fixed. Let U,P be C^2 exact rotating profiles on R^3, with div U=0 and uniform U=o(|y|). Write B=(cI-omega J)y+U, Omega=curl U, F=B cross Omega, a=1-2c and b=1+c. Hypothesis tags: H0, H1-prime. Phi_s denotes the complete B-flow.

## 1. Collinearity has zero volume within the vortical set

The vorticity equation and the vector curl identity give

\[
 \nabla\times F=a\Omega.                                 \tag{1}
\]

Indeed curl(B cross Omega)=(Omega dot grad)B-(B dot grad)Omega-div(B)Omega=(b-3c)Omega=aOmega.

For any C^1 vector field F, its derivative is zero at almost every point of its zero set. Here is the elementary density-point argument: if DF(p) were nonzero at a density point of {F=0}, differentiability would confine nearby zeros to an arbitrarily thin cone about the proper kernel of DF(p), whose volume fraction is bounded away from one; this contradicts density one. Apply the Lebesgue density theorem to {F=0}. Equation (1) then implies Omega=0 at almost every point of {F=0}, since a>0. Consequently

\[
 |\{x:F(x)=0,\ \Omega(x)\ne0\}|=0.                         \tag{2}
\]

Thus {F nonzero} is open and has full measure in {Omega nonzero}. It need not contain the entire latter set.

## 2. An exact covector transport identity

Autonomy gives B(Phi_s x)=DPhi_s(x)B(x), and Cauchy gives Omega(Phi_s x)=e^{-bs}DPhi_s(x)Omega(x). For any invertible matrix A, (Av) cross (Aw)=det(A) A^{-T}(v cross w). Since det DPhi_s=e^{3cs},

\[
 F(\Phi_s x)=e^{-as}D\Phi_s(x)^{-T}F(x),
 \qquad D\Phi_s(x)^T F(\Phi_s x)=e^{-as}F(x).               \tag{3}
\]

In particular nonvanishing of F is B-invariant. For each x with F(x) nonzero, its bounded backward orbit lies in a compact ball D_x. Let M_x=sup_{D_x}|F|, which is finite and positive. Setting s=-t in (3),

\[
 \|D\Phi_{-t}(x)\|\ge\frac{|F(x)|}{M_x}e^{at}
                  \quad(t\ge0).                          \tag{4}
\]

This is a lower bound for the largest singular value. It does not identify one fixed initial vector that realizes the bound for every t, and it does not by itself prove positive metric entropy or a positive-measure basin of any single limiting object.

## 3. Vortical nonstationary periodic B orbits are saddles

Let gamma be a nonconstant B-periodic orbit of period T and suppose Omega is nonzero at some point p on it. Transport makes it nonzero everywhere on the orbit. DPhi_T(p) fixes the nonzero vector B(p) and has Omega(p) as an eigenvector with eigenvalue e^{bT}>1. These two vectors are independent, since a vector cannot have the distinct eigenvalues 1 and e^{bT}. The determinant is e^{3cT}; therefore the third multiplier is

\[
 e^{3cT}/e^{bT}=e^{(2c-1)T}<1.
\]

The nontrivial transverse multipliers lie strictly on opposite sides of the unit circle. Thus this is a hyperbolic saddle periodic orbit, with a two-dimensional flow-saturated backward stable set for the reversed flow, equivalently the unstable manifold for B. Its backward basin is null; a fully local proof and the countable treatment of arbitrarily many cycles are supplied in the team records.

## Scope

These computations confirm approach3 items 8 and 10 in the portions stated here. They do not extend the null-basin conclusion from individual equilibria or cycles to arbitrary compact recurrent sets. A union over an uncountable collection of null submanifolds is not automatically null. No derivative decay or global derivative bound is used in (1)-(4); all backward estimates take place in a compact ball.

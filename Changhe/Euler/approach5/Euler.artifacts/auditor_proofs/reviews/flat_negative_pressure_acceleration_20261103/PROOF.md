# A flat negative-pressure swirl with bounded acceleration

## 1. Exact statement and dependency

Fix 0<s0<1/4 and a point z on the cylinder rho=1 in R3. There is a smooth local stationary incompressible Euler pair (v,P) near z with v=P=0 on rho>=1, both infinitely flat at z, but v nonzero at every nearby point with rho<1. Its helicity is zero. On its nonzero set put E=|v|^2, S=P-E/2, H=-S and R=E/H. Then

    P<0, 1<=R<2, liminf_(y->z,E>0) R=1,
    limsup_(y->z,E>0) R=2, inf_(near z,E>0) (-P/E)=0.

On each sufficiently small B_epsilon(z), writing r=|y-z|,

    |(v.grad)v|<=2E<=2epsilon E/r, 0<r<epsilon.

Thus the acceleration constant can be arbitrarily small while every fixed pressure comparison -P>=kappa E, kappa>0, fails. The pressure is normalized by P(z)=0. This refutes replacing the fixed margin in LIT257/A1699 by the pointwise sign -P>0 on the nonzero set, even for local stationary zero-helicity flows. The exact LIT257 proof, including its normalized pressure F=P(z)-P, was reread. No actual tail or decaying profile is asserted.

## 2. Construction and smooth flat extension

For s=1-rho in (0,s0) set

    A(s)=2+s^(-4)sin^2(1/s),
    I(s)=exp(-integral_s^s0 A(t)/(1-t) dt),
    f(s)=sqrt(A(s)I(s)),
    v=f(s)e_theta, P=-I(s).

Extend both by zero for s<=0. The construction is needed only locally where rho>3/4; the cylindrical basis is smooth there. The substitution u=1/t and sin^2 u=(1-cos 2u)/2 gives

    integral_s^s0 t^(-4)sin^2(1/t)dt
      =integral_(1/s0)^(1/s) u^2 sin^2 u du
      =s^(-3)/6+O(s^(-2)).

The last error follows by integration by parts in the cosine integral. Since 1/(1-t)>=1, there is C>0 such that I(s)<=exp(-C/s^3) for small s. Every derivative of A has a polynomial bound in 1/s. Also A>=2, so every derivative of sqrt(A) has such a bound. The identity I'=AI/(1-s) and repeated differentiation show that every derivative of I is bounded by a polynomial in 1/s times I; the same argument applies to sqrt(I). Consequently every derivative of f tends to zero faster than any power of s. Successive difference quotients prove both zero extensions are smooth with all jets zero on the cylinder.

For any z on the cylinder, |s(y)|=|rho(y)-rho(z)|<=|y-z|. The scalar bounds in s therefore imply infinite value order in Euclidean distance to z. Every ball centered at z contains points with s>0, where f>0. Thus neither v nor P vanishes identically near z.

## 3. The full local stationary equation

Write F(rho)=f(1-rho). A pure axisymmetric swirl independent of the axial coordinate satisfies

    div v=0, (v.grad)v=-F(rho)^2 e_rho/rho,
    curl v=(F'(rho)+F(rho)/rho)e_3.

Therefore v.curl v=0. Directly from Section2,

    partial_rho P=I'(s)=A(s)I(s)/(1-s)=F(rho)^2/rho.

Hence (v.grad)v+grad P=0. This holds on both sides and across the cylinder by smoothness. Taking the divergence gives Delta P=-div div(v tensor v)=-tr((Dv)^2). Thus the pressure equation and all the stationary weak products hold classically, not merely formally.

## 4. Pressure ratios and the acceleration bound

Here E=AI and H=(1+A/2)I. Thus R=2A/(A+2) and -P/E=1/A. Since A>=2, one has 1<=R<2. Along radial approaches with s_n=1/(n pi), A=2 and R=1. Along s_n=1/(pi/2+n pi), A=2+s_n^(-4), so R tends to2 and -P/E tends to0. All approaches have R in[1,2), which proves the exact liminf and limsup.

Choose epsilon<s0. On B_epsilon(z), rho>1-s0>3/4, so |(v.grad)v|=E/rho<=2E. For 0<r<epsilon this is at most 2epsilon E/r. At velocity zeros the same undivided inequality holds. Given any desired positive K, choosing 2epsilon<=K proves the inverse-radius bound with that K. All remaining hypotheses of the infinite-flat version of LIT257 hold, including a full ball, pressure normalization, smoothness, incompressibility and the pressure equation. Only a fixed positive kappa fails.

## 5. Why this is not a tail counterexample

For any c>0 and real omega let X=(cI-omega J)y, J y=e_3 cross y, and L=(1-c)I+omega J. The tail equation DV X=-LV for this swirl would require

    c rho F'(rho)=-(1-c)F(rho).

The radial components involving omega cancel. Its nonzero solutions on a radial interval are constant multiples of rho^(-(1-c)/c), incompatible with smooth flat vanishing at rho=1. Thus the twisted homogeneity fails for every such c and omega.

For any 0<eta<1/2, the vector representing the candidate normalized one-form H^(-eta)v is purely angular. If it were closed on a neighborhood, its angular coefficient B(rho) would satisfy (rho B)'=0. But

    rho B=rho R^eta F^(1-2eta)

is positive inside and tends to zero at the cylinder. It cannot be constant on the whole connected radial interval meeting that cylinder. Thus the needed closed normalized form is absent as well. For omega!=0 the contraction X.v=-omega rho F is already nonzero; for omega=0 it vanishes, but homogeneity and closedness still fail.

## 6. Verdict and limits

CO66 Section7 is CONFIRMED at exactly its local stationary scope. The fixed Rstar<2 margin in the acceleration theorem cannot be weakened to pointwise R<2. This is distinct from the negative ratio endpoint2/3 in A1658/A1697: no conclusion about that endpoint follows. The unrestricted rotating-profile conjecture, and the missing actual-tail acceleration or angular-frequency estimate, remain OPEN.

The other sections of the pinned coordinator note were read. Its orbit-adapted force and boundary identities in Sections3-4 were explicitly not submitted and are not certified here. The construction above is checked directly; no numerical computation, formal build, external model call or global extension argument was used.

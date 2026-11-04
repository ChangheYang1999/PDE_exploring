# Component constants in an exact small local swirl

## 1. The field and its domain

Fix0<c<1/2, omega!=0 and epsilon>0. Put p=(1-c)/c>1, d=p-1, a=1-2c, b=2-2c, q=b/a=2p/d>2, eta=a/b, Jx=e3 cross x and X=(cI-omega J)x. On the cylindrical domain rho>0 define

    V=epsilon rho^(-p)e_phi,
    P=-epsilon² rho^(-2p)/(2p).

Both are smooth on this entire domain. They satisfy the full rotating similarity equation there and all the listed local tail identities. Their sole vortical component with nonzero k=X.V has

    W=-d epsilon rho^(-p-1)e3,
    k=-omega epsilon rho^(-d),
    S=P-|V|²/2=-epsilon² rho^(-2p)/b,
    S=D_epsilon |k|^q,
    D_epsilon=-epsilon^(2-q)/(b|omega|^q).

This is a local full-equation example, already present in A1405. The new claim concerns its component constant and normalization, not existence of a whole-space decaying profile.

## 2. Every equation is exact

The cylindrical divergence is zero and curl has the sign stated above, since d_rho(rho V_phi)=-d epsilon rho^(-p). V.W=0 and W.grad S=0. The vector angular derivative is partial_phi V=JV, so

    X.grad V=-cpV-omega JV=-(1-c)V-omega JV,
    X.grad P=-2cpP=-bP.

Thus all linear similarity terms cancel. The remaining terms are

    (V.grad)V=-epsilon² rho^(-2p-1)e_rho,
    grad P=epsilon² rho^(-2p-1)e_rho,

and cancel as well. In particular the pressure Poisson equation holds. Directly, both -Delta P and tr((DV)^2) equal2p epsilon² rho^(-2p-2), confirming the sign without a pressure normalization argument. Since dq=2p, the displayed D identity is exact; differentiating it gives bS grad k=ak grad S. No interface, axis boundary or distributional equation across the excluded axis is asserted.

## 3. What upper norm bounds cannot control

For every fixed compact K in rho>0 and integer m>=0,

    ||V||_(C^m(K))=epsilon C_(K,m),
    ||P||_(C^m(K))=epsilon² C'_(K,m),

with finite constants independent of epsilon. Given any finite collection of positive upper derivative bounds, all sufficiently small epsilon satisfy them simultaneously, while |D_epsilon| tends to infinity because q>2. Hence there is no finite bound for |D| uniform over this class based only on those fixed upper bounds, the fixed domain and fixed c,omega. The same conclusion holds for any selected finite collection of compact subsets and derivative orders.

A lower normalization, global smoothness and decay, or the geometry of one common-flat germ are different hypotheses and have not been tested by this family. In particular the example does not refute a bound that uses such additional information.

## 4. The product and exact degenerate endpoint

Since p(q-2)=q,

    (-D_epsilon)|V|^(q-2)=1/[b(|omega|rho)^q].

This does not tend to zero with epsilon. Also R=|V|²/|S|=b and P=-|V|²/(2p)<0. Consequently shrinking all local smooth norms does not supply the positive-pressure margin used by the component doubling criterion.

The negative-scalar pressure-ratio matrix is

    M_R=((1-eta)R-1)I+eta V tensor V/|S|.

At R=b, b-a=1 gives M_R=a e_phi tensor e_phi. The perpendicular eigenvalues are zero and its only nonzero eigenvalue is a>0. Since grad|S| is radial and grad R=0, the complete ratio flux M_R grad|S|+|S|grad R is zero. Thus Poisson does not itself restore uniform ellipticity at this ratio, even within exact local full similarity solutions. This concerns the degeneracy, not the isolated-flat continuation theorem.

## 5. The local potential has a nonzero period

On an angular coordinate patch,

    V/k=-e_phi/(omega rho)=grad(-phi/omega),
    X.grad(-phi/omega)=1.

A full circle about the axis has integral(V/k).dx=-2pi/omega. A gradient of a single-valued C1 function has zero integral around a closed parametrized curve by the fundamental theorem, so no such global potential exists on the full annulus. This agrees with CO60 but now holds for an exact local full-equation solution. No contradiction with a period-removal theorem for a different weighted form is claimed.

## 6. Scope and verdict

All five submitted sections and all six independent sections were read. The amplitude scaling, normalized product, degenerate matrix and period are confirmed. The same velocity solves the local full equation for omega=0, but then k=0 and neither D_epsilon nor the V/k quotient is defined; those assertions retain omega!=0.

Every member is singular on the omitted axis, fails decay as |z| tends to infinity at fixed rho, has only one connected vortical region and has no velocity or scalar zero. The limit epsilon->0 is the identically zero field, not one field with infinitely many small components accumulating at a common-flat point. The missing component-uniform estimate in the campaign therefore remains open. This finding is submitted for continued comparison through the existing configured model agents, with provider runtime unattested. No computation or formal build was used.

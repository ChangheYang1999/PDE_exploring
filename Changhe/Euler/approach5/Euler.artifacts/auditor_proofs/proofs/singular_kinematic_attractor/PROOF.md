# A singular attracting set for the independent bracket equations

## Statement and scope

Put c0=2(2-sqrt(2))/(5-sqrt(2)). For every c0<c<1/2 and every finite real omega there are smooth vector fields U,W on R3 such that U is compactly supported,

    div U=div W=0, B=(cI-omega J)y+U, [B,W]=-(1+c)W,
    W(y)=O(|y|^(-1/c)).

There is a smooth compact genus-two handlebody H, strictly trapping for the backward B-flow Psi, with W nowhere zero on a neighborhood of H. Its maximal invariant set K is a nontrivial transitive singular-hyperbolic attractor. It contains a zero p of B and nonstationary orbits. There is a unique physical probability nu on K with support K; for Lebesgue-almost every z in H, alpha_B(z)=K. In particular a positive-volume set of points with W nonzero has a backward limit set containing both p and a nonstationary orbit.

The construction is a parameter variant of A066, with the smooth global extension A121. The measure conclusion uses the precise published singular-hyperbolic attractor theorem stated below. The entire target interval 2/5<c<1/2 is covered. The fields are NOT Euler profiles: W is not curl U, and the Euler pressure and U-circulation laws have not been imposed.

## 1. Parameters and all construction inequalities

Use the unambiguous notation

    kappa=1+c, d=3c, a=kappa-d=1-2c,
    b=(kappa+a)/2=1-c/2, L=b+a=2-5c/2, q=b/L.

Then 1/2<q<1. The inequality q>1/sqrt(2) is equivalent to c>c0. Choose

    Kpar=1+sqrt(2)/(2q),
    T=log(Kpar*q)/a, rho=exp(-kappa*T),
    delta=(1-rho)/4,
    epsilon=min(delta,1/Kpar-1/2)/2,
    m=(rho*(1+2*delta)+1+delta)/2.

Here Kpar denotes a scalar parameter, not the invariant set K. Directly,

    1/q<Kpar<2, Kpar*q=q+sqrt(2)/2>sqrt(2), T>0,
    0<epsilon<delta, Kpar*(1/2+epsilon)<1,
    rho*(1+2*delta)<m<1+delta,
    b*Kpar*rho=L*exp(-d*T).

The last equality follows from Kpar*q=exp(a*T). The strict m inequalities follow from 1+delta-rho*(1+2*delta)>0. These are precisely the footprint, signed-flux and collar inequalities used in the complete A066 construction. Thus changing Kpar is legitimate provided T,rho,delta,epsilon,m are all recomputed. Merely altering the flight time while holding the footprints fixed would violate the flux identity.

For comparison the original parameter Kpar,0=(2+1/q)/2 only gives Kpar,0*q=q+1/2. It is not uniformly above sqrt(2) in the target range. No conclusion here relies on a finite parameter grid.

## 2. The exact local and return dynamics

In the core use

    X=-B=(Lx,-kappa y,-bz), W=partial_y.

The core box and the two exit-to-top maps are those in A066:

    |x|<=1, -epsilon<=z<=1, |y|<=z+delta,
    P_+(y,z)=(Kpar*(z-1/2),rho*y-m+rho*(z+delta),1),
    P_-(y,z)=(-Kpar*(z-1/2),rho*y+m-rho*(z+delta),1).

Section 1 gives strictly interior disjoint return footprints. The increasing tube cross-sections and the rounded incoming faces in A066 make the actual lateral boundary strictly incoming. They do not change the vector field or these return formulas on the invariant core.

For a point (x,y,1), x nonzero, the core exit time is tau(x)=-log|x|/L. Consequently the return time is T+tau(x), and the return map is

    f(x)=sign(x)*Kpar*(|x|^q-1/2),
    h_+(x,y)=rho*|x|^(kappa/L)*y-m+rho*(|x|^q+delta),
    h_-(x,y)=rho*|x|^(kappa/L)*y+m-rho*(|x|^q+delta).

In particular |partial_y h|<=rho<1. After one return the quotient lies in I=[-Kpar/2,Kpar/2]. A full invariant orbit in H either is the equilibrium, belongs to its incoming or outgoing separatrices, or is described by these returns and their limiting histories. In particular the auxiliary bottom face creates no extra invariant component: a negative-z core point followed backward reaches that face, since z(t)=z(0)exp(-bt), whereas all returning points enter through z=1.

For completeness the two returned strips even lie on opposite sides of a horizontal line. Indeed c0>3/10, hence kappa/a>13/4, so rho<2^(-13/8)<1/3; the last strict inequality follows from 2^13>3^8. Therefore

    m-2*rho*(1+delta)=(5-15*rho+2*rho^2)/8>0.

Thus h_+<0 and h_->0 on the whole section, with a uniform gap. Relabeling the vertical orientation matches the usual geometric-Lorenz convention.

## 3. Expansion and local eventual onto property

Normalize x=(Kpar/2)*xi. On [-1,1] the quotient is

    g(xi)=sign(xi)*(2*(Kpar/2)^q*|xi|^q-1).

It is smooth and increasing on each side of zero, with g(0+)=-1, g(0-)=1, and g(1)=s in (0,1), g(-1)=-s. Its derivative tends to infinity at zero and satisfies

    g'(xi)>=lambda:=2*q*(Kpar/2)^q>=Kpar*q>sqrt(2).

The second inequality uses Kpar/2<1 and q<1. The reciprocal derivative has bounded variation on each branch. These are the actual expanding Lorenz-map conditions, after normalization to the invariant interval. It is not necessary, and generally not true, that each restriction to a half of I maps onto all of I.

Here is the elementary eventual-onto argument, also given in Williams, Proposition 1, printed p. 78. Start with a nonempty open interval and retain one component on a single side of zero. Repeatedly map it and, if the image crosses zero, retain the longer component. Each step expands length by at least lambda except for a possible factor 1/2 at a cut. If cuts never occurred in two consecutive steps, every two steps would expand length by at least lambda^2/2>1, an impossibility in a bounded interval. At two consecutive cuts, the image of the interval abutting zero has an endpoint at -1 or 1; its longer component is therefore a full half interval. The image of a full half interval contains the other half. More explicitly, s=g(1)>=lambda-1 and g(s)>=lambda*s-1, so

    g(s)+s>=(lambda+1)*(lambda-1)-1=lambda^2-2>0.

The images of the two resulting pieces cover the interval. Endpoint statements use one-sided limits; for open intervals the conclusion is coverage of the interior, which is sufficient for all transitivity arguments. No kneading-sequence restriction from the later classification sections is used.

## 4. From the quotient to the attracting flow

The geometric model checked here is the one in Guckenheimer-Williams, printed pp. 61-63: a linear saddle with strong stable, unstable and weak stable magnitudes satisfying

    0<b<L<kappa,

followed by two disjoint contracting return strips and an increasing quotient with slope greater than sqrt(2). The final inequality is equivalent to c>2/7 and follows from c>c0. The actual paper's equations (7)-(8) on p. 62 and its inverse-limit description on p. 63 apply after the section rescaling and harmless changes of vertical strip coordinates. The attracting flow is the suspension with its singular separatrices attached; no numerical claim about the classical Lorenz differential equations is involved.

One can see the transitivity implication directly. A finite admissible past return history determines a strip whose vertical width is at most C*rho^n after n returns. Its interior quotient coordinates form an interval, on which all specified branches are smooth. Such strips, with longer histories and smaller quotient intervals, form a neighborhood basis on the regular part of the invariant return set. The eventual-onto property lets an interval in one such strip reach the initial interval of any prescribed finite history. Following that history then reaches the target strip. Taking its history sufficiently long controls the vertical coordinate by contraction. Hence the return dynamics connects every pair of relative open sets in its regular invariant part. This is the usual inverse-limit transitivity proof; it uses contraction of actual strips, not only transitivity of the quotient in isolation.

The flow saturation of the regular return set is dense in the full invariant set. Finite histories that end on the singular line are approximated by histories avoiding it. The equilibrium is also in their closure: if x tends to zero at entry, then at time tau(x)/2 its coordinates have sizes |x|^(1/2), at most (1+delta)|x|^(kappa/(2L)), and |x|^(q/2), respectively. All tend to zero. The outgoing singular legs and their forward images are limits by continuity of the flow. This accounts for the singular points omitted by the return map.

Thus the compact attracting set has a dense recurrent positive orbit. Formally, apply the Baire argument to a countable relative-open basis and the open dense sets of points whose flow orbit meets each basis element after arbitrarily large times. The return-strip connection above gives density; the flow is continuous on the compact invariant set, including at the equilibrium. Its positive limit set is all of K. This is the transitive-attracting hypothesis required by the measure theorem below.

## 5. Singular hyperbolicity and physical basin

The complete proof of A134 in the team records is kinematic: it uses the exact W transport, constant divergence and the eigenvalues at the carrier zeros, not W=curl U. On K the vector W never vanishes. The only zero of B in H is p, and its eigenvalues are kappa,b,-L. The largest other real part is b<kappa. The proof therefore gives a dominated splitting for Psi with strong stable line R W, contraction exponent -kappa, and two-dimensional central area expansion exponent kappa-d=a>0. The zero is hyperbolic. All singular-hyperbolic hypotheses hold.

The external measure theorem is Araujo-Pacifico-Pujals-Viana, Singular-hyperbolic attractors are chaotic, arXiv:math/0511352v3. Its Definition 1.1 requires a transitive attracting set. Theorem B at C2 regularity supplies a unique ergodic physical probability whose basin has full volume in the topological basin; Theorem C gives support equal to K. These exact statements and their local-to-compact-manifold application were checked in A135. The actual PDF and source record are in the team records. This proof checks the theorem's hypotheses and does not claim to reprove its full measure-theoretic argument.

Apply those statements to our smooth flow near H, extended to a compact boundaryless manifold without changing a neighborhood of H. For a generic point z of nu in H, attraction gives alpha_B(z) subset K. Conversely, every neighborhood of a point in supp nu=K is visited at arbitrarily large times: choose a nonnegative continuous function supported in that neighborhood with positive nu integral and use the convergent time averages. Thus K subset alpha_B(z), proving equality. H has positive volume and W is nonzero throughout it.

## 6. Global extension, rotation and exclusions

The smooth two-handle filling of A121 changes no field near H. Its signed-flux matching, flat extensions, cap continuation, relative Euclidean volume correction and exterior rotation collar are all independent of the special original value of Kpar. Section 1 supplies every inequality used in that construction. Hence it applies for this variant for every prescribed finite omega. It yields smooth compactly supported U and smooth W with the asserted bracket, divergence and decay properties. A smooth volume-preserving coordinate change transports the attractor and preserves all the basin conclusions.

Because curl U is compactly supported whereas W is nonzero on exterior rays transported from H, W is not curl U. Kinematic circulation means the circulation of a primitive of i_W vol, for example (B cross W).dy/a; it does not mean circulation of the actual U. The latter requires the missing Euler coupling.

This settles the independent-field realization of case (beta). It does not settle case (gamma), which only requires a limit set to MEET {W=0}; that limit set need not be wholly irrotational. Nor does it prove that every increasing Lorenz map with slope merely greater than one has the same full-support basin conclusion. Those stronger statements are not used.

## Verification and dependencies

A066: complete handlebody, collar, signed-flux and Euclidean extension proof in the team records.
A121: smooth global filling in the team records.
A134-A135: dominated splitting and the precise APPV measure theorem application in the team records.
Primary geometric sources: Guckenheimer-Williams, Structural stability of Lorenz attractors, Publications mathematiques de l'IHES 50 (1979), 59-72, DOI 10.1007/BF02684769; Williams, The structure of Lorenz attractors, same volume, 73-99, DOI 10.1007/BF02684770. Actual PDFs, text extractions and retrieval hashes are in the team records.

The inequalities, return formulas and eventual-onto argument were checked symbolically by hand. No numerical grid or floating-point computation is evidence for the theorem. B24's parameter script was inspected but was not run by this agent. Continuing model collaboration is recorded in the team records.

# A direct meridian proof for the analytic regular plug

## Exact statement and inputs

Let M, F, P, eta and Y be the smooth torus, diffeomorphism, monotone collapse, closed one-form and nonsingular vector field constructed in the team records. In its eigenvector coordinates, K=(3+sqrt(5))/2, r>1, rho=K^(-r), eta=du, Y=partial_v, and P F=A P for the cat matrix A=[[2,1],[1,1]]. The central collapsed ribbon is 0<=v<=w(u). Its source is p=(0,w(0)/2); its two fixed boundary saddles are q_0=(0,0), q_1=(0,w(0)). The smooth disc D contains p and the derivative-defect region, F^(-1)D is contained in int D, and the nested inverse discs shrink to p.

For every 0<c<1/2 choose r=(1+c)/(1-2c), a=1-2c and T=log(K)/a. The exact suspension of S=M\int D constructed in the team records can be chosen so that its boundary foliation by span(B,W) has a smooth compact leaf gamma with the following properties:

1. Filling its boundary torus along gamma gives a manifold diffeomorphic to S3. Thus this realization of the plug is a knot exterior and gamma is its meridian.
2. The linear holonomy of gamma is K or K^(-1), in particular is not one.
3. There is a smooth meridian isotopic to gamma and everywhere transverse to span(B,W).

The global completion theorem in the team records consequently applies. For every finite omega it gives the independent-field model stated in the team records. This proof replaces that result's Yang-Yu classification input with Lacher's cell-like mapping theorem and the three-dimensional Poincare theorem. It does not give W=curl U or an Euler profile.

## The actual closed boundary leaf

Let x_+=(0,w(0)-epsilon) be the upper intersection of partial D with the vertical source-to-saddle prong. Then F(x_+)=(0,w(0)-rho epsilon). The annulus F(D)\int D contains the embedded vertical arc J_+ from F(x_+) to x_+, and a disjoint analogous lower arc J_-.

In the suspension construction choose the annulus sweeping field V tangent to both arcs. To do this choose endpoint collar fields tangent to the arcs, prescribe the other collar germs by F, and identify the two disjoint crossing arcs with radial arcs in product annulus coordinates. A positive radial interpolation preserves tangency. The positive scalar change which normalizes every crossing time to T also preserves tangency. The collar matching remains exactly the one in the suspension construction.

The swept upper arc gives the curve

    gamma(t)=(flow_V^t(F(x_+)),t),  0<=t<=T.

It closes smoothly at the suspension seam (z,T)~(F(z),0). Its tangent is in span(partial_t,Y)=span(B,W), because V is parallel to Y on J_+. It is therefore an actual leaf of the boundary foliation, rather than a chosen curve with only the same suspension degree.

## Holonomy and transverse perturbation

On this suspension B=-partial_t, W=exp((1+c)t)Y and m=exp(-3ct)dt wedge omega_S, where i_Y omega_S=eta. Hence

    theta=i_B i_W m=exp(at)eta,       dtheta=a dt wedge theta.

The restriction of theta to the boundary never vanishes: its kernel in the ambient tangent space is span(B,W), and B is transverse to the boundary. Along a leaf, Cartan's formula shows that the transverse form is multiplied by exp(a times elapsed suspension time). Since gamma has degree one, its return derivative is K or its inverse, according to the holonomy convention. It is nonunit.

The local graph argument in the team records then perturbs gamma within an arbitrarily small boundary annulus to a smooth transverse curve isotopic to gamma. It remains to establish that this slope is a meridian.

## Transfer of the marked fundamental group

The open ambient suspension is the mapping torus of F on M\{p}. The trapping plug is a deformation retract of it: every point outside the plug enters it once in positive suspension time, and the transverse first-entry time is continuous. Use paths concatenated from left to right. If rho_y joins y to F(y), its fundamental group is the HNN extension with stable generator s represented by the vertical time path followed by rho_y^(-1), and

    s^(-1) g s = phi_F(g),       phi_F(g)=rho_y F(g) rho_y^(-1).

Choose y=(0,w(0)+h) just above q_1. The closed vertical interval J from x_+ to y is F-invariant. In a small neighborhood of q_1 the derivative along Y is exactly rho, and F contracts toward q_1 on both sides. For every zeta in J, the curve

    t |-> ((1-t/T)F(zeta)+(t/T)zeta,t)

closes at the seam. It gives a free homotopy from gamma to the curve with zeta=y. The latter is conjugate to s when rho_y is the vertical interval from y to F(y). Therefore filling along gamma kills s, and the filled fundamental group is

    pi_1(M\{p},y) / <<g^(-1) phi_F(g)>>.               (1)

To transfer phi_F, take a finite unstable arc J_0=[-L,L]x{0} of the linear torus, long enough that its full preimage R=P^(-1)J_0 contains D in its interior. R is the closed central ribbon over this finite interval, an embedded closed disc. A nonzero lattice translation cannot identify two of its points, since its stable component would then vanish. The finite lattice-point argument permits h>0 so small that y and rho_y avoid R: among lattice points with bounded unstable component there are only finitely many with stable component in a fixed bounded interval, and none has zero stable component except the origin.

Since A(J_0) contains J_0, F(R) contains R. Thus F preserves M\R forward and A preserves M_0\J_0 forward. The restricted map

    P: M\R -> M_0\J_0

is proper and onto, with point or compact-arc fibers. Both open surfaces are locally compact finite-dimensional ANRs, hence ENRs. Points and compact arcs are cell-like. Lacher's Theorem 1.2 and Corollary 1.3 therefore make this map a proper homotopy equivalence.

The inclusion M\R -> M\{p} is a homotopy equivalence, as is M_0\J_0 -> M_0\{0}. For the first, use a slightly larger disc containing R and retract both complements to the same exterior along annular coordinates. For the second, use a small closed regular neighborhood of the embedded arc J_0: its complement and the complement of the point retract to a common exterior, and the annular region outside the arc has the same radial retraction. The arc is a finite embedded smooth arc even if it winds many times around the torus. This is a regular-neighborhood argument; the set J_0\{0} itself is not an annular collar.

These inclusion maps commute with the dynamics, and P F=A P. They transfer (1) to the linear punctured torus with base point x=P(y) on the positive stable ray and reference path sigma=P rho_y along that ray from x to A x. The transferred automorphism is

    phi_A(g)=sigma A(g) sigma^(-1).                   (2)

## The two words, checked without floating point

The sign of the stable eigenvector can be chosen so that the base point is x=e_s/5, with e_s=(1,-(1+sqrt(5))/2). Changing its distance along the same punctured stable ray conjugates the based description and does not alter the filled group. Put

    xi=(3-sqrt(5))/10,       eta0=(1-sqrt(5))/10.

Then A x=(xi,eta0), with 0<xi<1 and -1<eta0<0. The reference path sigma remains in that open unit square and contributes no crossing. Let a,b denote the horizontal and vertical fundamental loops through x. The punctured torus cut along the two coordinate circles has one open square; recording signed crossings of its sides gives these free generators.

The lifted A-image of a is the segment (xi,eta0)+t(2,1), 0<=t<=1. Its crossings occur, in order, at

    y=0: t=(sqrt(5)-1)/10,
    x=1: t=(7+sqrt(5))/20,
    x=2: t=(17+sqrt(5))/20.

All lie strictly between zero and one, and the written order follows directly from 2<sqrt(5)<3. The word is b a a. The lifted A-image of b is (xi,eta0)+t(1,1). Its y=0 crossing precedes its sole x=1 crossing at t=(7+sqrt(5))/10. Thus

    phi_A(a)=b a^2,       phi_A(b)=b a.

Consequently the filled group has presentation <a,b | a=b a^2, b=b a>. The second relation gives a=1 and the first then gives b=1. The group is trivial. This argument proves the needed word calculation entirely by exact inequalities; no group enumeration or numerical ordering is required.

## Filling and scope

Filling a smooth torus boundary along an embedded primitive slope gives a closed orientable smooth three-manifold. By the three-dimensional Poincare theorem, a simply connected such manifold is S3; uniqueness of smoothing in dimension three gives the smooth conclusion used here. The attached solid torus has a core knot, whose exterior is precisely N, and gamma bounds its meridian disc. The transverse perturbation has the same slope. This verifies the final hypothesis of the explicit completion theorem.

The coordinator's script and its logged neighboring-slope tests are consistency checks, not premises of this proof. Although its symbolic coordinates are in Q(sqrt(5)), its crossing routine converts event times and order comparisons to floating point and uses a 10^(-12) lattice-point tolerance. The description of that routine as an exact arithmetic certificate is therefore inaccurate. Its reported core words agree with the exact hand calculation above. The finite-group counts and the optional Property P and fractional-Dehn-twist remarks are not used or independently established here.

## Primary source and verification

R. C. Lacher, Cell-like mappings I, Pacific Journal of Mathematics 30(3) (1969), 717-731: the ENR characterization on p.718, Theorem 1.2 on p.719 and Corollary 1.3 on p.720 were read in the actual publisher PDF, retained in the team records. They apply to the two open surfaces above. The three-dimensional Poincare theorem and smoothing uniqueness are stated external theorems, not newly reproved results.

This audit independently checks the coordinator's model-agent proof in the team records. Its Sections 1-2 also agree with the earlier analytic-triple and suspension audits. No new numerical computation was run.

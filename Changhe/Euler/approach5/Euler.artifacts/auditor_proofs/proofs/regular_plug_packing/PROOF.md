# Packing test for a proposed regular train-track plug

Let 0<c<1/2, a=1-2c, b=1+c, kappa=(3+sqrt(5))/2 and rho=kappa^(-b/a). Consider the substitution a_edge -> a_edge a_edge b_edge, b_edge -> a_edge b_edge. A regular point of the first target edge has three preimages. If each full input and target tie has the same W-time interval [-1,1] and each tie map is v -> rho v+G, then injectivity and strict containment require three disjoint closed intervals of total length 6rho to lie in the interior of an interval of length 2. Consequently

    3rho<1.

Equivalently c>c*, where

    c*=(log 3-log kappa)/(2 log 3+log kappa).

This number lies between zero and 2/5. Thus the literal equal-width model fails for 0<c<=c*, but this packing test excludes no parameter in the primary range 2/5<c<1/2.

The obstruction disappears at the level of lengths if the two tie half-widths are w_a=1, w_b=kappa-2. Indeed the incoming sums are the components of [[2,1],[1,1]]w=kappa w, and rho kappa<1 because b>a. Both target ties have strict length slack. This verifies only capacity, not existence of smooth compatible strips.

In charts where W=partial_v and the transverse flux form is du, an oriented overlap must have the form (u,v)->(u+d,v+h(u)). Two affine branch expressions (kappa u+b_i,rho v+G_i(u)) must satisfy the exact overlap equalities

    b_i+d_target=kappa d_source+b_j,
    G_i(u)+h_target(kappa u+b_i)=rho h_source(u)+G_j(u+d_source).

The graph substitution and the length inequalities do not solve these equations at the switch. They also do not supply a smooth trapping suspension, identify its meridian relative to the actual plane field, or prove the needed transverse meridian exists. These are the remaining construction tasks, not a general impossibility theorem.

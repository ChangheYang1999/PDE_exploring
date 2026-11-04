# Exclusion of non-Lorenz zeros from nonsingleton vortical limits

Status: CONFIRMED in A159 after independent reconstruction of the entrance-time proof. This strengthens the independently audited B19. The model coordinator has been asked to challenge the extraction argument; no affirmative external check is being claimed here.

## Statement

Let U in C2, P in C1 solve the full rotating profile equation, with 0<c<1/2 and finite omega. Let a forward orbit of X=-B be precompact and let K be its omega-limit set. Suppose K is not a single point and Omega=curl U is nowhere zero on K. Then every zero p of B in K has real spectrum

    {1+c,lambda_2,lambda_3},
    lambda_3<0<=lambda_2, lambda_2+lambda_3=2c-1.

There is no hypothesis that any regular orbit converges to p. No assertion lambda_2<1+c is made. The conclusion therefore does not supply A134's domination assumption.

## Local entrance lemma

Let X be C1 near a hyperbolic equilibrium p, let K be compact and fully invariant, and assume W^s_X(p) intersects K only at p. Then p cannot lie in a nonsingleton omega-limit set of a precompact orbit whose omega-limit is K.

Choose a sufficiently small closed ball D centered at p such that every forward orbit staying in D for all positive time belongs to the local stable manifold. Such a ball is part of the local hyperbolic stable-manifold theorem. Shrink it so K has a point outside D. If p belongs to K, the given orbit has arbitrarily late visits close to p and arbitrarily late visits outside D. Choose times t_n tending to infinity with x(t_n)->p and, before t_n, an outside visit later than n. Let s_n be the last entry through the boundary of D before t_n. Then s_n->infinity, x(s_n) belongs to the boundary, and x([s_n,t_n]) stays in D.

The durations t_n-s_n tend to infinity. Indeed, a Lipschitz bound |X(z)|<=L|z-p| on D gives

    |x(t_n)-p|>=radius(D) exp(-L(t_n-s_n)).

Take a subsequence with x(s_n)->z. Since s_n->infinity, z belongs to K; it also belongs to the boundary of D and differs from p. Continuous dependence and the diverging durations imply that X_t z stays in D for every t>=0. Hence z belongs to W^s_X(p), contrary to its assumed intersection with K. This proves the lemma.

The same proof shows that a regular orbit contained in K cannot even accumulate on p. If it stays eventually in D, it already belongs to W^s_X(p), a contradiction; otherwise use the same entry points.

## Application to the profile

At a vortical zero p, DB(p) has eigenvalue b=1+c along Omega(p), with the other two summing to 2c-1. If those two have negative real parts, p is hyperbolic and the backward stable manifold is its vortex line, by the uniqueness argument of in the team records. A130 implies that line meets K only at p. The entrance lemma excludes p from the nonsingleton limit set K. Therefore one of the remaining eigenvalues is nonnegative; the negative sum excludes a complex pair and gives the stated real spectrum.

This argument uses the full vorticity bracket through the exact vortex line and the compact-vortical-set nonintersection. It is not an argument from positive divergence alone. The hypotheses allow p to be approached repeatedly without any assumed asymptotic phase or connecting orbit. The only external local input is the hyperbolic stable-manifold theorem.

Audit written: 2026-11-02T20:42:34Z

# Global signed background bound for finite exact candidates

## Statement and hypotheses

Let chi be the real exact finite rational potential in the candidate's
canonical JSON. Its branches have p_j=(3+gamma-j delta)/2, gamma=1/c,
delta=1-gamma>0, and its harmonic polynomials are smooth at the origin.
Let rho=-partial_y Delta chi and

    A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
    theta=sup_X (sqrt(rho_x²+rho_y²)-rho_y)/2.

For a positive rational tau, the certificate target is A+tau I>=0 on the
whole plane. A complete successful certificate proves theta<=tau. A
partial cover or an inconclusive cell proves no global statement. For
candidate C1-N1-007-d2w-j7-e2bal the requested target is tau=2/25.
Combining this with the independently confirmed full-plane kappa gives
c+1-theta-kappa>=c+1-2/25-kappa. The arithmetic of the final strict
comparison with2 is recorded only when the cover is complete.

## Exact polynomial construction

Set t=r²/(1+r²), z=cos(2 theta_angle), w=(1-t)^(delta/2).
The exact radial derivative recurrence gives each fourth derivative as
r^(-4)(1+r²)^p_j times a rational polynomial in t. The numerator has an
exact factor t². Dividing by this factor leaves the radial multiplier
(1+r²)^(p_j-2)=w^(j+1). Every sine harmonic is sin(2 theta_angle) times
a Chebyshev U polynomial in z; every cosine harmonic is a Chebyshev T
polynomial in z. The recurrences T_0=1,T_1=z and U_0=1,U_1=2z, with
P_(m+1)=2z P_m-P_(m-1), construct them exactly.

Thus rho_y=sum_j w^(j+1) R_j(t,z) and
rho_x=sin(2 theta_angle) sum_j w^(j+1) S_j(t,z).
All coefficients of R_j,S_j are exact rationals. The matrix diagonals
are a=tau+rho_y and b=tau, and its off-diagonal is sin(2 theta_angle)q,
where q=-sum_j w^(j+1)S_j/2. The eigenvalues are unchanged by the S1
reflections. The compact rectangle0<=t<=1,-1<=z<=1 covers the entire
plane and its limiting origin and infinity. Exact cancellation at t=0
checks origin consistency; at t=1 every positive w power vanishes.

The code compares the constructed fields at the already independently
reproduced Cartesian point with its outward field record. This is a
construction check; it does not replace the interval cover.

## Range bounds and positivity

The tensor Bernstein enclosure and correlated midpoint Taylor bound are
the same elementary methods proved in ../global_matrices/PROOF.md.
Here the number J of branch powers is read from the actual candidate,
rather than fixed at six. On a radial interval[l,h], w is enclosed by
[(1-h)^(delta/2),(1-l)^(delta/2)]. The finite polynomial in w of degree J
is transformed to Bernstein form along with t and z. The convex-hull
property gives valid bounds everywhere, including h=1.

When h<1, replace w^j by its degree-six Taylor polynomial about
mu=(l+h)/2. For q_j=j delta/2 and H=(h-l)/2, its remainder is bounded by

    |(q_j)_7| H^7/7! max((1-l)^(q_j-7),(1-h)^(q_j-7)).

Multiply the Taylor polynomial with each radial Bernstein polynomial
using the exact Bernstein-product identity; bound the remainder by the
above error times the largest absolute tensor Bernstein coefficient.
Sum the enclosures over all j. Either valid enclosure may certify a
cell; combining them never uses a heuristic error estimate.

If diagonal lower bounds are a0,b0 and |q|<=q0, the off-diagonal is at
most C=q0 sqrt(1-min_cell|z|²) in absolute value. Hence a valid least
eigenvalue lower bound is

    (a0+b0-sqrt((a0-b0)²+4C²))/2.

The bound min(a0,b0)-C is also valid. A nonnegative outward lower bound
certifies positivity throughout that cell.

## Complete cover and scope

Start with a checked finite binary partition or the full rectangle.
Each unsuccessful bound replaces one cell by its two radial or angular
halves. At every saved checkpoint the accepted and pending leaves are
checked to form a complete prefix-free binary partition. The split rule
may compare relative radial width(h-l)/(1-l) with angular width/2;
this affects only search cost. A certificate is complete exactly when
there are no pending cells and every accepted cell has a nonnegative
bound. This finite induction supplies full coverage, including cell
boundaries. A grid maximum or a sum of cell areas is never substituted.

Dependencies: the exact canonical candidate and its established S1
constraints; the exact radial derivative recurrence; Chebyshev and
Bernstein identities; Taylor's theorem; outward Arb arithmetic; and the
separately reviewed kappa bound. This is a numerical analytic certificate,
not a Lean formalization, and it requires an independent peer check before
being marked CONFIRMED. It supplies only this signed background condition,
not the other background conditions, residual smallness, or existence.

# An interior gradient bound for the same-quadrant profile cover

Keep all definitions and the complete pair classification of ../PROOF.md.
For a same-quadrant pair with radii1,u, u>0, assume both endpoint angles
lie at least delta>0 from either coordinate axis. Along their line segment,
each coordinate is at least u sin(delta), and the coordinate sum is at
least u. Consequently

    r>=u/sqrt(2), d=2|z1 z2|/r>=sqrt(2)u sin(delta).

Indeed r>=(|z1|+|z2|)/sqrt(2), while d>=sqrt(2)min(|z1|,|z2|).
The known gradient bound |grad d|<=2 and the profile formula give

    |grad g| <= alpha/2 [(u/sqrt(2))^(alpha-1)
                     +2(sqrt(2)u sin(delta))^(alpha-1)].

Integrating along the segment therefore gives this gradient bound times
D^(1-alpha) as an upper bound on the Holder quotient S. For a parameter
box take its smallest u and angular distance from the axes, and its
largest possible D. The estimate may be intersected with every previous
upper bound. If the angular distance is zero, omit this extra estimate.
It changes no endpoint argument, pair classification, or previously
accepted certificate. It only accelerates the same-quadrant cover.

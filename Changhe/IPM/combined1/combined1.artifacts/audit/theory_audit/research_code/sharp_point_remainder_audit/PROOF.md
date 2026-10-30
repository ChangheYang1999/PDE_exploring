# The remaining three sharp-ball point comparisons

## Statement

Let rho be one of the exact references d2, Mpen2 or b6 whose Cartesian point values were independently confirmed in T4-015. Let F=(cX+U[rho]).D rho-rho and V=cX+U[rho]. If rho+h is an exact fixed-c solution with ||h||_(H^(2+s))<=r, set

    s=1/8192, r=43/50000,
    C0=(4 pi(1+s))^(-1/2), C1=(8 pi s(1+s))^(-1/2).

At every point X, a necessary condition is

    |F(X)| <= r[C1|V(X)|+C0(1+|D rho(X)|)]+C0 C1 r^2.       (1)

For Mpen2 at (0,2) and b6 at (0,1) the right side is strictly smaller than |F|. Thus neither exact reference has a fixed-c correction in this ball, including the smaller class N_s(h)<=r. For d2 at (0,1) this particular comparison is inconclusive.

## Proof and dependencies

The difference equation is F+V.Dh-h+U[h].D rho+U[h].Dh=0. Fourier Cauchy-Schwarz gives |h|,|U[h]|<=C0||h||H^(2+s) and |Dh|<=C1||h||H^(2+s); the vector velocity multiplier has modulus at most one, and the derivative evaluation constant follows by rotational symmetry of its Gram matrix. These embeddings and their normalization were proved in T4-007. The triangle inequality gives (1). This proof does not require any inverse or signed-background hypothesis.

The standalone certificate recomputes (1) at512-bit precision using the already independently confirmed Cartesian intervals. It compares all six bound/gap intervals with the frozen N4-047 output. A positive gap proves exclusion, while a negative gap alone proves nothing about existence. The source point fields are inherited from T4-015; this arithmetic audit does not pretend to recompute the fields.

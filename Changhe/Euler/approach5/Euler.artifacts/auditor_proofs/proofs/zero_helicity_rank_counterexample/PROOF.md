# Constant profiles refute an unqualified Bernoulli rank implication

Let 0<c<1/2, omega!=0, and u be a constant vector with Ju!=0. Here J(y1,y2,y3)=(-y2,y1,0), a=1-2c and A=cI-omega J. Set

    U=u, P=-[(1-c)u+omega Ju].y, B=Ay+u,
    H=P+|U|2/2+(Ay).U, G=B.grad H.

These are smooth exact rotating Euler profiles: div U=0, DU=0 and the constant momentum terms cancel grad P. The velocity is uniformly sublinear. It does not tend to zero. Its vorticity and helicity vanish everywhere.

A is invertible, and with y_star=-A^-1u its complete carrier flow is

    Phi_t(y)=y_star+exp(ct)exp(-omega Jt)(y-y_star).

All backward trajectories converge to y_star and are bounded. The vorticity flow is the identity and is complete, volume preserving and recurrent at every point.

Skew symmetry gives A^T u=cu+omega Ju. Hence

    H=|u|2/2-a u.y,
    grad H=-a u,
    G=-a u.(Ay+u),
    grad G=-a(cu+omega Ju).

It follows that

    grad G cross grad H=a2 omega(Ju cross u)!=0.

For example u=e1 gives H=1/2-a y1, G=-a(c y1+omega y2+1), and dG wedge dH=-a2 omega dy1 wedge dy2. Therefore G dH is not closed on any nonempty open set, so no local C2 function K can satisfy dK=G dH there.

This confirms LIT69 exactly: zero helicity, uniform sublinearity and the listed flow hypotheses do not imply the global rank identity dG wedge dH=0. The vorticity region is empty, so the example does not test the identity on a nonempty vortical region or at its boundary. It refutes neither a decay-only statement nor LIT56's spatially constant conclusion. In LIT57 the local rank proof on the vortical region must still retain its stated density premise for global extension unless a different argument is supplied. No numerical calculation or pressure normalization is used.

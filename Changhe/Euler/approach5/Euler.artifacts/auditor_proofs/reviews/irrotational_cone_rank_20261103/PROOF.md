# An irrotational conical profile whose scalar rank vanishes only on a trace

Status: CONFIRMED at A607. Independent reconstruction of LIT157. This checks a local example and its stated limitation; no vortical matching or global pressure extension is supplied.

## 1. Exact claim

For every 2/5<c<1/2 and finite real omega, put p=(1-c)/c, d=p-1, a=1-2c=cd, beta=d/(2p), A=cI-omega J and Jx=(-x2,x1,0). Thus 0<d<1/2. There exists delta>0 and real analytic, axisymmetric fields V,P2 on

    C_delta={x: r=|x|>0, |z|<delta}, z=x3/r,

such that div V=0, curl V=0 and

    (1-c)V+DV(Ax+V)+omega JV+grad P2=0.

They have the exact velocity and pressure twisted homogeneities of degrees -p and -2p. With k=(Ax).V and S=P2-|V|^2/2, the weight |S|^beta is positive and locally A2 on this cone. Rank grad k cross grad S is0 on z=0 and nonzero whenever0<|z|<delta. V is nonzero. All local tail identities, including actual local Poisson and scalar compatibility, hold; rank on the vortical set is vacuous because that set is empty.

This proves only that the local irrotational equations and the TRACE of rank on an interface do not force rank on its side. It does not disprove global tail density or provide Cauchy data realized by a neighboring vortical solution. The cone omits both the origin and polar directions.

## 2. Convergent harmonic potential

Define

    K(z)=sum_(n>=0) a_n z^(2n), a_0=1,
    a_(n+1)/a_n=(2n+d)(2n+1-d)/((2n+2)(2n+1)).

Every factor is positive, and the ratios tend to1, so this series converges for |z|<1 and can be differentiated termwise on compact subintervals. The coefficients satisfy

    (2n+2)(2n+1)a_(n+1)
      =[2n(2n+1)-d(d-1)]a_n,

which is exactly the coefficient recurrence of

    ((1-z^2)K')'+d(d-1)K=0,
    K(0)=1, K'(0)=0, K''(0)=d(1-d).

Set h=r^-d K(z), V=-grad h/a and P2=-|V|^2/2. The spherical Laplacian is

    Delta h=r^(-d-2)[((1-z^2)K')'+d(d-1)K]=0.

Thus V is divergence free and curl free, and is real analytic on the cone. Its radial component is d r^(-d-1)K/a>0 because the positive even series makes K>0. In particular V never vanishes there.

## 3. Momentum, homogeneity and pressure

Ordinary homogeneity gives DV x=-pV. Rotational equivariance gives DV Jx=JV. Thus

    (1-c)V+DV(Ax)+omega JV=[1-c-cp]V=0.

The remaining nonlinear terms cancel since symmetric DV gives DV V=grad(|V|^2/2)=-grad P2. This verifies each term of the FULL local profile equation for every omega. Equivariance also turns the ordinary degrees into the required twisted homogeneities.

For the actual scalar k, (Jx).grad h=0 and x.grad h=-dh, whence

    k=(Ax).V=(cd/a)h=h.

Harmonicity of V gives

    -Delta P2=|DV|_F^2=tr(DV^2)
              =partial_i partial_j(V_i V_j).

The second equality uses symmetric DV; the last uses div V=0. This is the actual local Poisson equation. No tensor convolution over missing parts of space has been defined, so it is not a global canonical-pressure statement.

## 4. Weight and rank coefficient

Let n=x/r, t_z=e3-zn, w=1-z^2 and M=d^2 K^2+w(K')^2. Then M>0 and

    S=-a^-2 r^(-2p)M,
    |S|^beta=a^(-2beta)r^-d M^beta.

On each sufficiently small closed ball contained in the cone, this weight and its reciprocal are bounded. Their average product is therefore bounded, proving local A2 directly. It is essential here that A2 is asserted locally within the conical domain, not on all punctured space.

The gradients are

    grad k=r^(-d-1)(-dK n+K't_z),
    grad S=a^-2 r^(-2p-1)(2pM n-M't_z).

Hence

    grad k cross grad S
       =a^-2 r^(-d-2p-2)[dKM'-2pK'M](n cross t_z).

The differential equation for K yields M'=2d KK'+2z(K')^2. Near0,

    K'=d(1-d)z+O(z^3), M=d^2+O(z^2),
    M'=2d^2(1-d)z+O(z^3).

Therefore

    dKM'-2pK'M=-2d^4(1-d)z+O(z^3).

The coefficient is strictly nonzero for the parameter range. Taking delta sufficiently small proves the rank is nonzero for0<|z|<delta and zero atz=0; the geometric factor has norm sqrt(1-z^2)>0. The nonzero derivative of this rank on the irrotational side is part of the example, not a claimed smooth extension through a vortical side.

The scalar values on the interface can satisfy a proportional relation k=C|S|^beta, and their first z-derivatives both vanish there. This alone does not construct any neighboring solution or prescribe all needed Cauchy data. Conversely it would be too broad to claim the example violates every possible first-order matching condition. The precise verified statement is absence of a constructed vortical match and failure of rank continuation from its zero trace alone.

## 5. General irrotational equations and scope

For an actual tail on an open set where W=curl V=0, the linear Lamb identity reads0=aV+grad k. Thus V=-grad k/a and Delta k=0. Harmonic regularity makes V smooth inside that open set. Actual local Poisson implies

    Pi=P2+|V|^2/2 is harmonic,
    S=Pi-|V|^2, Delta S=-2|DV|_F^2.

The example above has Pi=0 and satisfies these equations exactly. Superharmonic S and positive weight consequently do not propagate rank from the displayed trace. They give no omitted boundary condition by themselves.

The example is singular as r->0 and is not defined on the whole sphere of directions. A globally smooth curl-free and divergence-free decaying extension would have bounded entire harmonic components and therefore be0, contradicting this V. No smooth mixed vortical extension or global nonlocal pressure matching has been supplied. There is no counterexample to the main campaign conjecture or to a global conditional theorem. This is a fully convergent analytic example checked by exact differentiation and series arithmetic; no computation or external existence theorem is required.

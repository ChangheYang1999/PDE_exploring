# Pressure-deficit geometry on the limiting Bernoulli sheet

Status: CONFIRMED by independent audit A534, 2026-11-03T07:22:07.096261+00:00, at the exact hypotheses below. The full existing configured-model source/comparison was read; no new model client was used.

## 1. Exact setting

Fix 2/5<c<1/2 and any finite omega. Write

    a=1-2c, p=(1-c)/c, A=cI-omega J,
    L=(1-c)I+omega J, Q_t=exp(omega tJ),
    J(x1,x2,x3)=(-x2,x1,0).

Let U in C2(R3;R3), P in C1(R3) solve the full incompressible rotating profile equation

    LU+DU(Ax+U)+grad P=0, div U=0, U.curl U=0.

Assume U tends uniformly to zero and DU=O(sqrt(|x|)) at infinity. The confirmed A498,A476,A477 chain supplies the natural bounds

    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

The canonical pressure normalization and common limit P_infinity are those of A031,A508,A516. Put

    B=Ax+U, W=curl U, H=P+|U|²/2+(Ax).U,
    g=U.B, Q=P-P_infinity-|U|²/2=H-P_infinity-g.

For t>=0 define on D=R3 minus{0}

    u_t(x)=exp((1-c)t)Q_t U(exp(tA)x),
    p_t(x)=exp(2(1-c)t)[P(exp(tA)x)-P_infinity].

The convergence needed for the argument is

    u_t -> V and p_t -> P2 in C1loc(D).                (1)

It now follows from A530 for the pressure and A533 for the velocity under the stated profile hypotheses. The proof below also applies independently if (1) is imposed directly. Write Wstar=curl V, k=(Ax).V, E=grad k and S=P2-|V|²/2. Then S_t=p_t-|u_t|²/2 converges to S in C1loc. The limits inherit the exact twisted homogeneities

    V(exp(tA)x)=exp(-(1-c)t)Q_t^T V(x),
    k(exp(tA)x)=exp(-at)k(x),
    S(exp(tA)x)=exp(-2(1-c)t)S(x).                     (2)

A509 gives E=-aV+Ax cross Wstar. The homogeneities follow either from A210 and the pressure limit, or by shifting the parameter in (1). No derivative of a first correction is assumed.

Let z be an escaping regular vortical point on the A509/A518 Bernoulli level associated with a vortical carrier equilibrium of rate rho<-a. Explicitly, along y_t=Phi_t(z), assume the already confirmed identities

    H=H(p)=P_infinity, g=0,
    dg=-(rho/a)dH, grad H!=0,
    B cross W=f grad H, f(y_t)=exp(mu t)f0,
    mu=-a-rho>0, f0=f(z)!=0.                         (3)

The globally helicity-free regular level and A517 provide such escaping points whenever this lower branch occurs. A518 proves mu>=1 in the target range. The pointwise conclusions below apply to every point satisfying (3), not only the unstable manifold of the original equilibrium.

## 2. The exact covector formula

On the escaping open set define

    v_t(z)=exp(-tA)Phi_t(z), M_t=Dv_t(z).

A518 proves that v_t tends in C1 locally to v, that det M_t=1, and that M_t tends to an invertible matrix M. It also gives v_t-v=O(exp(-t)) on compact subsets of this open set. The exact covector transport on (3) is

    D Phi_t(z)^T grad H(y_t)=exp(rho t)grad H(z).

Since D Phi_t=exp(tA)M_t, it follows that

    grad H(y_t)=exp((rho-c)t)Q_t^T M_t^(-T)grad H(z).
                                                               (4)

Equation Q=H-P_infinity-g and (3) give

    Q(y_t)=0, grad Q(y_t)=-(mu/a)grad H(y_t).           (5)

The spatial rescaling of a scalar gradient is

    grad S_t(v_t)=exp((2-c)t)Q_t grad Q(y_t).

Combining with (4)-(5), and using 2+rho-2c=1-mu, gives the exact formula

    grad S_t(v_t)=-(mu/a)exp((1-mu)t)
                           M_t^(-T)grad H(z).         (6)

No estimate was differentiated to obtain (6).

Passing to (1), Q(y_t)=0 gives S(v)=0. If mu>1, (6) gives

    grad S(v)=0.                                     (7)

If mu=1, instead

    grad S(v)=-(1/a)M^(-T)grad H(z)!=0.                (8)

This is a nonzero covector because M is invertible and grad H(z)!=0. These conclusions require only C1 convergence, not any specified rate of derivative convergence.

## 3. Relation to the limiting velocity and surface

The Lamb identity aU+grad H=B cross W together with (3) gives

    a U(y_t)=(exp(mu t)f0-1)grad H(y_t).

Multiply by exp((1-c)t)Q_t and use (4). Since 1-c+rho-c=a+rho=-mu,

    a u_t(v_t)=[f0-exp(-mu t)]M_t^(-T)grad H(z).

Therefore

    a V(v)=f0 M^(-T)grad H(z)!=0.                     (9)

In particular, at mu=1 equation (8) is equivalently

    grad S(v)=-V(v)/f0.                              (10)

A518 already gives k(v)=0, E(v)=0 and Ax cross Wstar=aV!=0 there. The same conclusions follow from the exact formulas and the leading gradient limit. The local image T under v of the regular level in (3) is a C1 surface, since v is a local C1 diffeomorphism. Its tangent directions are Av and Wstar(v): M B=Av, M W=Wstar, and B,W are independent when f0!=0 and grad H!=0. Thus V is a nonzero normal to T. On this surface

    k=0, dk=0, S=0,

and (7)-(10) distinguish the two rates. These are necessary conditions on a local limiting surface. They neither assert a compact global surface nor give a profile exclusion.

## 4. Why the endpoint forces k to vanish in a neighborhood

Fix z satisfying (3) with mu=1 and set x0=v(z). By (9), Wstar(x0)!=0. Choose a small ball O about x0 on which Wstar never vanishes. Uniform convergence of curl u_t makes W(exp(tA)x) nonzero on O for all sufficiently large t. The confirmed rank identity A413 therefore gives

    dH wedge dg=0, hence dH wedge dQ=0,

at every exp(tA)x with x in O for large t.

The rescaled leading gradient converges uniformly:

    exp((1-c)t)Q_t grad H(exp(tA)x) -> E(x).           (11)

For example, with k_t=(Ax).u_t, the exact scalar rescaling of H gives its left side as

    grad k_t+exp(-t)grad(p_t+|u_t|²/2),

which converges by (1). The other rescaled gradient is grad S_t. Multiplying the rank identity by its two positive scalar factors and the same rotation, then passing to (1),(11), proves

    dk wedge dS=0 on O.                              (12)

By (8), dS(x0)!=0. Shrink O to a product coordinate box in which S is the first coordinate. Equation (12) means that k is independent of the two remaining coordinates. Thus k=F(S) for a C1 scalar F on an interval containing0. Here F(0)=0 because k(x0)=0.

Differentiate the homogeneities (2) along Ax. They give

    (Ax).grad k=-ak, (Ax).grad S=-2(1-c)S.

Substitute k=F(S). Since the range of S contains an interval about0,

    s F'(s)=beta F(s), beta=a/[2(1-c)] in(0,1).        (13)

On either side of0 its solutions are F(s)=C_+ s^beta or C_-(-s)^beta, by differentiating F(s)/|s|^beta. A nonzero coefficient would make the derivative unbounded at0. Since F is C1, both coefficients are zero. Hence k vanishes on a neighborhood of x0, and E=dk vanishes there as well.

Homogeneity extends this zero region to the union of its images under exp(tA), an open twisted cone. That cone need not be the whole punctured space, and it does not allow application of a global nodal maximum theorem without that additional premise. No analytic continuation principle is asserted.

## 5. The critical-saturation variant

There is a related conditional statement without a spectral rate. Suppose z is an escaping point whose full B-orbit lies in Crit H intersect Crit g, with H=P_infinity and g=0 there, and B cross W(z)!=0. Such points are the regular critical saturation considered in A510-A511 when they escape. Then Q=0 and dQ=0 along that orbit. Formula (1) directly gives

    S(v)=0, dS(v)=0, k(v)=0, dk(v)=0.

The exact cross-product transport is

    exp((1-c)t)Q_t(B cross W)(y_t)
                      =M_t^(-T)(B cross W)(z).

The leading limit on the left is Av cross Wstar(v). Its right side is nonzero. Since E(v)=0, this equals aV(v), so V(v)!=0. These conclusions concern such an escaping critical orbit or its local B/W surface. They do not assert that a compact critical set itself contains an escaping point, or that every critical point has these hypotheses.

## 6. Regularity dependencies and comparison

A530 and A531 give the pressure part of (1) without velocity derivative convergence. A533 gives the velocity part by the fully audited C37 Holder iteration and the full image of the bounded-profile scattering map. The stronger local W2q conclusion in LIT136 remains a separate result. The present geometric argument does not use the Chae-Wolf theorem or a differentiated first-remainder assertion.

The actual configured-model coordinator check in the team records, items8-9, states these same conditional distinctions; it leaves its C1 input unverified. The proof here reconstructs the covector scaling, the exact nonzero coefficient and the neighborhood conclusion. LIT138 independently obtains the gradient distinction from a stronger forced-correction expansion; that stronger expansion is not required here. No numerical computation or new model client was used. The complete postread agrees with C37 Proposition17 and Theorem18 and the actual coordinator comparison.

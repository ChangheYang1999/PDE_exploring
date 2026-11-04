# Transverse strain identities and exact affine sign tests

Status: CONFIRMED, audit A199. This is a local identity and obstruction-to-sign argument, not a nonexistence theorem.

## Statement and hypotheses

Let 0<c<1/2, omega be any finite real number, a=1-2c, b=1+c, J(x,y,z)=(-y,x,0), and A=cI-omega J. Suppose U is C2 and P is C1 on an open subset of R3, div U=0, and

    (1-c)U + (B.grad)U + omega JU + grad P = 0,
    B=Ay+U, Omega=curl U.

Write S=(DU+DU^T)/2, Ht=P+|U|^2/2+(Ay).U, F=Ht-ac|y|^2/2, Z=B cross Omega, q=|Z|, n=Z/q where q>0, and m=Omega/|Omega| where Omega!=0. Along any backward B trajectory on its interval of existence,

    (log q)' = 1-c+n^T S n,
    (log |Omega|)' = 1-m^T S m.

If a compact invariant set has q>0 everywhere, every invariant probability mu on it satisfies

    integral n^T S n dmu = -(1-c),
    integral m^T S m dmu = 1.

The coupling also gives

    n.grad F = q-a omega (Jy).n,
    B.grad F = -a(|B|^2+omega (Jy).B).

For each fixed omega!=0 there are exact affine profiles exhibiting either sign of (log q)' and both signs of n.grad F. These profiles are not decaying, and have no compact attractor. For omega=0 they have Omega=0 and the q,n sign tests are undefined.

## Proof of the identities

The curl equation and divergence give [B,Omega]=-b Omega, div B=3c and div Omega=0. For beta=Z.dy=i_Omega i_B vol, the cross-product curl identity gives

    d beta = a i_Omega vol.

Both beta(B) and beta(Omega) vanish. Cartan's formula therefore yields

    L_B beta = -a beta,   L_Omega beta=0.

In particular, in coordinates (B.grad)Z+DB^T Z=-aZ. Contract with n, divide by q, reverse time, and use sym DB=cI+S. This proves the first logarithmic derivative. Similarly the bracket relation gives (B.grad)Omega=DB Omega-b Omega, proving the second. The invariant averages follow by integrating the generator of the bounded C1 observables log q and log |Omega| on the compact set. Compactness and q>0 bound both logarithms; no limiting boundary integral is involved.

The Lamb identity is beta=a U.flat+dHt. Since U=B-cy+omega Jy, this becomes

    beta = a B.flat+a omega (Jy).flat+dF.

Evaluation on n and B gives the asserted two scalar equations. They apply at every omega under their displayed domain conditions. At omega=0, BF=-a|B|^2 and n.grad F=q where q>0.

## Exact affine family

For arbitrary p in R set, in coordinates (x,y,z),

    B_p=(1+px, -(a+p)y, bz),
    U_p=(1+(p-c)x-omega y, omega x-(1-c+p)y, z).

Its divergence is zero, Omega_p=2 omega e3, and [B_p,Omega_p]=-b Omega_p. An explicit polynomial is

    Ht_p= a(c-p)x^2/2 - omega(a+2p)xy
          + a(1-c+p)y^2/2 - a z^2/2 - ax - 2 omega y.

Direct component differentiation gives grad Ht_p=B_p cross Omega_p-aU_p. Thus

    P_p=Ht_p-|U_p|^2/2-(Ay).U_p

solves the full momentum equation, since the Lamb and momentum forms are algebraically equivalent for this A. This checks the pressure without assuming that a bracket identity alone implies the Euler equation.

For omega!=0,

    Z_p=(-2 omega(a+p)y, -2 omega(1+px), 0).

On the backward orbit from the origin, 1+px(t)=exp(-pt), so q(t)=2|omega|exp(-pt) and (log q)'=-p. For p=0 the backward flow is

    Psi_t(x,y,z)=(x-t, exp(at)y, exp(-bt)z).

Along (x,0,0), its variational rates are 0,a,-b, n=-sgn(omega)e2, and

    n.grad F_p=|omega|(ax+2).

This changes sign with x. The exponents are those of the derivative along this noncompact orbit; they are not the assertion of an invariant probability or of a compact hyperbolic attractor.

## Related periodic-orbit statement and limitations

For a nonstationary periodic B orbit gamma of period T, integration of BF gives

    E=integral_0^T |gamma'|^2 dt
      =-omega integral_0^T (gamma_1 gamma'_2-gamma_2 gamma'_1) dt>0.

Subtract the mean from the planar projection r. Cauchy-Schwarz and the periodic Wirtinger inequality give the absolute value of the last integral at most T E/(2 pi). Hence T>=2 pi/|omega|. At omega=0 no nonstationary periodic orbit exists. This agrees with the previously audited period bound; no upper bound or parameter exclusion follows.

All arguments are local except where compact invariance or periodicity is explicitly stated. Uniform sublinearity, decay, pressure normalization at infinity, and flow completeness are not used and are not consequences of this affine family. A pointwise sign failure does not rule out another global monotone quantity.

## Dependencies and verification evidence

The proof uses the displayed Euler equation, Cartan's formula, invariant integration, and the periodic Wirtinger inequality. It independently checks the formulas in Theory Agent C in the team records Section 3.7 and its transverse_euler proof. No numerical or symbolic computation was needed for this audit. The source proof explicitly assumes omega!=0; the condensed Section 3.7 must retain that condition for the affine sign assertions.

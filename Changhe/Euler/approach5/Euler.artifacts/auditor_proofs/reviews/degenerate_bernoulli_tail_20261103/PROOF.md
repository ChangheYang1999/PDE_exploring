# Nonzero natural tails with identically zero leading Bernoulli gradient

Status: CONFIRMED in A514 by a complete exact analytic reconstruction and full postread. These are singular homogeneous fields, not smooth whole-space profiles.

## 1. Exact field and conclusions

Fix 1/3<c<1/2 and any finite omega. Put q=(1-c)/c in (1,2), b=omega/c, d=2-q=(3c-1)/c, a=1-2c and A=cI-omega J, with J(y1,y2,y3)=(-y2,y1,0). In spherical coordinates (r,theta,phi), let

    V=r^(-q)[ b sin(theta)^2 cos(theta) e_r
              -(b d/4) sin(theta)^3 e_theta
              +sin(theta) cos(theta) e_phi ].             (1)

Then V is smooth on R3 minus zero, is nonzero, divergence free, axisymmetric as a vector field and satisfies

    V(exp(sA)y)=exp(-(1-c)s)exp(-omega sJ)V(y),
    k(y)=(Ay).V(y)=0,
    W_*=curl V, V.W_*=0, E=-aV+Ay cross W_*=0.            (2)

The vorticity is nonzero, smooth off zero and homogeneous of degree -q-1=-1/c. Both V and W_* are locally integrable across zero, and div V=0 and curl V=W_* hold distributionally on all R3. The field V is unbounded near zero and is therefore not a global smooth profile, irrespective of whether any additional punctured-domain equation happens to hold. No nonlinear profile equation is asserted.

For 2/5<c<1/2, V is also locally square integrable and has the exact ball energy law

    integral_(|y|<R)|V(y)|^2 dy
       =[integral_S2|V(w)|^2 dw]/(3-2q) * R^(3-2q),
    3-2q=5-2/c.                                         (3)

This is only a kinematic match to the Euler energy exponent.

## 2. Smoothness at the polar axis and at nonzero points

Write y=(x1,x2,z), rho^2=x1^2+x2^2 and r=|y|. The three angular vectors in (1) have Cartesian expressions

    sin(theta)^2 cos(theta) e_r
       =rho^2 z (x1,x2,z)/r^4,
    sin(theta)^3 e_theta
       =(z rho^2 x1,z rho^2 x2,-rho^4)/r^4,
    sin(theta) cos(theta) e_phi
       =z(-x2,x1,0)/r^2.

All are smooth off zero, including the polar axis. Their homogeneities and covariance under rotations about that axis are explicit. Since exp(sA) is dilation by exp(cs) followed by rotation by -omega s, and cq=1-c, the first identity of (2) follows.

The azimuthal component in (1) is independent of b. At theta=pi/4 it equals r^(-q)/2, so V is nonzero and its norm diverges as r->0. The poloidal terms are orthogonal to this component and cannot remove the divergence.

## 3. Divergence and the scalar k

For an axisymmetric spherical field,

    div V=r^(-q-1)[(2-q)b sin(theta)^2 cos(theta)
                  +(1/sin(theta)) partial_theta
                     (-(b d/4)sin(theta)^4)].

The second term is -bd sin(theta)^2 cos(theta), canceling the first because d=2-q. The formula holds away from the polar axis and extends there by smoothness.

Since Jy=r sin(theta)e_phi,

    (Ay).V=r^(1-q)[cb sin(theta)^2 cos(theta)
                         -omega sin(theta)^2 cos(theta)]=0.

No differential Euler equation was used to obtain this identity.

## 4. Exact curl identity, helicity and nonvanishing vorticity

Differentiating the twisted homogeneity gives

    (Ay).grad V=-(1-c)V-omega JV.

For any smooth V and linear X=Ay, the vector identity is

    grad(X.V)=A^T V+(DV)X+X cross curl V.

Since A^T=cI+omega J, the preceding two displays give grad k=-aV+Ay cross W_*. The function k is zero, so E=0 and aV=Ay cross W_*. Taking the scalar product with W_* yields V.W_*=0, since a>0.

The radial curl component comes only from the azimuthal component in (1):

    (W_*)_r=r^(-q-1)(1/sin(theta))partial_theta
                       (sin(theta)^2 cos(theta))
             =r^(-q-1)(3cos(theta)^2-1).

In particular it tends to 2r^(-q-1) at the north pole. By smoothness there W_* is nonzero. The whole curl has the ordinary homogeneous degree -q-1, and differentiating rotational covariance gives the A210 twisted vorticity homogeneity.

## 5. Distributional extension and energy

The angular functions and all their derivatives are bounded on the sphere. Thus |V|<=C r^-q and |W_*|<=C r^(-q-1). The restrictions q<2 and q+1<3 ensure local integrability of both fields. When integrating by parts outside a ball of radius epsilon, the boundary term for divergence or curl of V has absolute value at most C epsilon^(2-q) times a bound for the compactly supported test function. This tends to zero. Hence there is no additional distribution supported at zero, and the global distributional identities are exactly div V=0 and curl V=W_*.

For q<3/2, equivalent to c>2/5, spherical integration gives (3). The angular integral is finite and positive because V is smooth and nonzero on the sphere. The radial integral is R^(3-2q)/(3-2q). At c<=2/5 no finite ball energy assertion is made.

## 6. What the example does and does not establish

The class of divergence-free, helicity-free natural homogeneous tails with E identically zero is nonempty for every omega. Thus the tail-level conditions alone do not force the nonvanishing criterion Z_E empty in A509. For this example Z_E is the whole sphere, so A512's totally disconnected condition also fails. This does not show that such a tail belongs to an exact global profile. It neither contradicts the confirmed whole-space Liouville results nor constructs a rotating Euler counterexample.

All claims above follow from exact analytic expressions. The full Theory Agent C example and its surrounding scope have been read, and the reconstruction avoids reliance on its finite-difference numerical check. The existing configured-model source supplies the model comparison. No computation is needed.

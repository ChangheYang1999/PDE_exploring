# Exact nonlinear failure of the degenerate Bernoulli tail

Status: A784 CONFIRMED. Independent reconstruction of LIT130; continuing focused configured-model comparison is pending. The leading family itself is confirmed in A514.

## 1. Exact statement

Let 1/3<c<1/2, omega be any finite real number, p=(1-c)/c in(1,2), b=omega/c and d=2-p. With J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J and L=(1-c)I+omega J, define on R3 minus zero

    V=r^-p [b sin^2(theta)cos(theta) e_r
             -(bd/4)sin^3(theta) e_theta
             +sin(theta)cos(theta) e_phi].                (1)

A514 proves V is smooth off zero, nonzero, divergence free, and satisfies LV+DV Ay=0, (Ay).V=0, V.curl V=0 and -aV+Ay cross curl V=0, where a=1-2c. No single-valued C1 pressure makes V solve the full profile equation on any complete exterior region {|y|>R0}. Moreover, there is a smooth divergence-free whole-space field U equal to V on {|y|>=2} and zero on {|y|<=1}. It has the same failure on every exterior region, despite natural decay and the same leading tail.

This theorem concerns V itself and the exact cutoff field. It does not exclude (1) as a leading term with smaller corrections in some other exact profile.

## 2. The nonzero-rotation obstruction is circulation

The vanishing linear momentum term reduces the required equation to

    F+grad P=0, F=(DV)V.                                  (2)

The field is axisymmetric as a vector field. Let s=r sin(theta) be cylindrical radius and let ell=s V_phi=r^(1-p)sin^2(theta)cos(theta) be its angular momentum. The cylindrical transport formula gives

    s F_phi=V.grad ell.

Here the azimuthal part of V differentiates no scalar coefficient. Differentiate the radial factor and use

    partial_theta(sin^2(theta)cos(theta))
         =sin(theta)(3cos^2(theta)-1).

Substituting the two meridional components from(1) then gives

    s F_phi=(b/4)r^(-2p)sin^4(theta)
                          [d-(p+2)cos^2(theta)].           (3)

Indeed the cos-squared coefficient is (1-p)-3d/4=-(p+2)/4. On the equatorial circle of radius R this is

    F_phi=(bd/4)R^(-2p-1),
    integral_circle F.dl=(pi bd/2)R^(-2p).                (4)

For omega!=0, b!=0 and d>0, so this integral is nonzero for every R>0. The line integral of a single-valued C1 scalar gradient on a closed circle is zero. Equation(2) is therefore impossible on any full exterior region. No axisymmetry of P is assumed or needed.

## 3. The zero-rotation obstruction is local curl

If omega=0, the field is pure swirl. Use cylindrical coordinates(s,phi,z), where z now denotes the Cartesian third coordinate. Then

    V_phi=sz(s^2+z^2)^(-(p+2)/2), V_s=V_z=0,
    F_s=-s z^2(s^2+z^2)^(-p-2), F_phi=F_z=0.

Differentiate F_s in z to obtain

    (curl F)_phi=2sz(s^2+z^2)^(-p-3)
                         [(p+1)z^2-s^2].                 (5)

At s=z=1 it equals p 2^(-p-2)>0. Homogeneity gives a nonzero value at each point s=z=t>0, hence at points in every exterior region. If(2) held with P in C1, its smooth right-hand side would imply distributionally curl F=0. Formula(5) contradicts that implication. The obstruction thus requires no separate C2 assumption on P.

## 4. A smooth whole-space extension preserving the exterior

The cross-product curl identity, div V=0 and ordinary homogeneity y.grad V=-pV give

    curl(y cross V)=y div V-V div y+(V.grad)y-(y.grad)V
                  =(p-2)V.

Define T=(y cross V)/(p-2) on the punctured space. Choose a smooth radial cutoff chi equal to zero for r<=1 and one for r>=2. The product chi T extends smoothly by zero across the origin; set U=curl(chi T). This is smooth and divergence free on the whole space and equals V for r>=2. It tends uniformly to zero with DU=O(r^(-p-1)). On that exterior the entire momentum equation is identical to the equation for V, so Sections2-3 preclude a full-profile pressure there.

For 2/5<c<1/2, p<3/2. If C_v is the positive angular integral of the squared vector coefficient in(1), then for R>=2

    integral_(|y|<=R) |U|^2
       =C_0+C_v (R^(3-2p)-2^(3-2p))/(3-2p).

Thus the leading energy power is precisely 3-2p=5-2/c. This is a kinematic power-law match. No exact Euler energy identity, helicity condition for the cutoff interior, canonical-pressure residual estimate, or smallness of the residual is asserted.

## 5. Dependencies and verification

A514 supplies only the leading family and its exact kinematic identities; the new steps are the explicit circulation and curl calculations, and the vector-potential cutoff. The complete LIT130 source was read and pinned, then every calculation was reconstructed here. No numerical residual or symbolic computation is used as proof. A focused comparison by the existing configured-model team is pending. A nonlinear obstruction for the exact homogeneous field must not be promoted into an obstruction for that field as a leading asymptotic term.

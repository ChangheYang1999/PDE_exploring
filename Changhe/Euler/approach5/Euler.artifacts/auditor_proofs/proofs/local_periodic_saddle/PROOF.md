# An exact local rotating Euler saddle with a regular periodic orbit

## Statement and domain

Let 0<c<1/2, set k=1-2c>0, and choose a>0, kappa!=0 and omega!=0. On the open domain r=sqrt(x^2+y^2)>0 define, in the orthonormal cylindrical frame,

    U_r=-r/2+k a^2/(2r),
    U_theta=kappa(r-a^2/r),
    U_z=z,

and

    P=(1/8+kappa^2/2)r^2
       -(k^2/2+2kappa^2)a^2 log(r/a)
       -(k^2/8+kappa^2/2)a^4/r^2-z^2.

These are single-valued real analytic fields on that domain and solve the full rotating profile equation. They have div U=0 and Omega=2kappa e_z. The carrier B=(cI-omega J)y+U has the periodic orbit gamma={r=a,z=0}, where B cross Omega is nonzero. Its least period is T=2pi/|omega| and its transverse forward exponents are -k and 1+c.

This is a local model only. It is singular on the axis and grows at infinity. The periodic orbit is a saddle for both time directions, not an attractor. It is not a counterexample to the global conjecture.

## Exact component verification

Write v=U_r and w=U_theta. Direct differentiation gives

    (r v)'/r=-1,    partial_z U_z=1,
    (r w)'/r=2kappa,

and all other curl components vanish. Therefore div U=0 and Omega=2kappa e_z. The carrier components are

    B_r=-k(r^2-a^2)/(2r),
    B_theta=(kappa-omega)r-kappa a^2/r,
    B_z=(1+c)z.

Even though the scalar coefficients are axisymmetric, the cylindrical frame must be differentiated. The three momentum components consequently reduce to

    (1-c)v+B_r v'-w^2/r+P_r=0,
    (1-c)w+B_r w'+v w/r=0,
    (1-c)z+(1+c)z+P_z=0.

The omega terms cancel because B_theta=w-omega r, while omega JU has components (-omega w,omega v,0). Thus no rotation term has been omitted.

For the radial component, explicit expansion gives

    (1-c)v+B_r v'-w^2/r
       =-(1/4+kappa^2)r
        +(k^2/2+2kappa^2)a^2/r
        -(k^2/4+kappa^2)a^4/r^3,

which is -P_r. For the azimuthal component, use

    B_r w'=kappa[-kr/2+k a^4/(2r^3)],
    v w/r=kappa[-r/2+(1+k)a^2/(2r)-k a^4/(2r^3)].

Adding (1-c)w gives zero because (1+k)/2=1-c. Finally P_z=-2z proves the third component. These calculations verify the entire PDE, not merely its curl or invariant moments.

## Periodic geometry and variational exponents

At r=a,z=0 one has U_r=-ca, U_theta=0, B_r=B_z=0 and B_theta=-omega a. Thus

    B=-omega a e_theta,
    B cross Omega=-2kappa omega a e_r!=0.

The orbit travels once around the circle in time T=2pi/|omega|. Its circulation is zero because U_theta=0 there. Its oriented projected area is -sgn(omega) pi a^2, so

    integral_0^T |B|^2 dt
       =omega^2 a^2 T
       =-2omega A_xy(gamma).

The carrier equations are

    r'=-k(r^2-a^2)/(2r),
    theta'=kappa-omega-kappa a^2/r^2,
    z'=(1+c)z.

Linearization at the cycle gives delta r'=-k delta r, delta z'=(1+c)delta z and delta theta'=(2kappa/a)delta r. The triangular monodromy therefore has multipliers

    exp(-kT),    exp((1+c)T),    1.

The radial and axial exponents have opposite signs. This verifies the saddle qualification and rules out treating the local circle itself as the regular backward attractor required in CO9.

## Scope

The example confirms coordinator Example 13.3 and the local portion of its regular-attractor consultation. It shows that exact Euler coupling is compatible locally with the periodic circulation, orientation, and exponent restrictions in the regular region. It does not realize a compact attracting set, global smoothness, velocity decay, or the canonical global pressure/energy asymptotics. Its pressure is explicitly given and is not inferred from a Poisson equation alone. No computation is needed beyond the expansions above.

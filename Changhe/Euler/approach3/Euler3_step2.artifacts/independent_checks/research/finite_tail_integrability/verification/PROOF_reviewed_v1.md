# Integrability of the finite rotating representation

## Exact statement and notation

Fix c in (2/5,1/2), omega in R, positive R0 and R1, and a nonnegative integer damping order k. Put alpha=(1-c)/c and kappa=omega/c. Use exactly the finite scalar potentials T and S of ../represented_tail_decay/PROOF.md, with real coefficients independent of position, finite polynomial degrees, and E-channel angular degrees at least two. No Euler equation, tail constraint, normalization, or non-axisymmetry assumption is imposed. Let U=curl(Ty)+curl curl(Sy), and let Omega=curl U.

For r=|y|>0 define psi0(r)=kappa log(r/R0). For each real solid harmonic write H_lm^psi(y)=H_lm(Q_psi y), where Q is rotation about the third axis. Define the leading potentials by

    T0(y)=sum_lm H_lm^psi0(y) (r/R0)^(-alpha-l) A_lm(1),
    S0(y)=sum_lm H_lm^psi0(y) (r/R0)^(1-alpha-l) C_lm(1),
    U0=curl(T0 y)+curl curl(S0 y),  Omega0=curl U0.

Here A_lm(1) and C_lm(1) are the endpoint values of the radial polynomials in xi, not one selected coefficient. The differential operators act on every radial factor, including psi0. The singular leading fields are only defined away from zero and are never used as the full interior fields.

There exist finite constants C_U,C_Omega and R_b>0 such that for all r>=R_b and n in S^2,

    |U(rn)-U0(rn)| <= C_U r^(-alpha-1),
    |Omega(rn)-Omega0(rn)| <= C_Omega r^(-alpha-2).

With F(n)=U0(n) and H(n)=Omega0(n), these leading fields satisfy

    U0(rn)=r^(-alpha) Q_{-kappa log r} F(Q_{kappa log r} n),
    Omega0(rn)=r^(-alpha-1) Q_{-kappa log r} H(Q_{kappa log r} n).

Consequently, with physical sphere measure and A=integral_S2 |F|^2, the limit

    lim_(R -> infinity) [integral_(|y|<R) |U|^2 dy - A R^(3-2alpha)/(3-2alpha)]

exists and is finite. The full-space helicity integral integral_R3 U dot Omega is absolutely convergent. This includes A=0. It does not assert that either quantity vanishes.

## Proof of the remainder bounds

All interior factors in the full potentials are smooth functions of r^2 with positive denominators; integer k makes the damping factor smooth at zero. Solid harmonics are polynomials. Thus U and Omega are smooth on every bounded set, including the origin.

To bound the exterior remainder with derivatives, fix an annulus 1<=|z|<=2 and write y=Rz, with R>=max(1,R0,R1). On this fixed annulus the following expansions hold uniformly together with any fixed finite number of z derivatives:

    sqrt(r^2+R0^2)/r = 1+O(R^-2),
    xi = 1 - 4R0/(sqrt(r^2+R0^2)+R0) = 1+O(R^-1),
    psi-psi0 = (kappa/2) log(1+R0^2/r^2) = O(R^-2),
    (r^2/(r^2+R1^2))^k = 1+O(R^-2).

For clarity, each O statement here means a bound in the C^j norm on the fixed annulus, for any chosen finite j. It follows by setting epsilon=1/R: the displayed functions of z and epsilon have denominators bounded away from zero for 0<=epsilon<=epsilon0, and are smooth there. Taylor's formula in epsilon, including z derivatives, gives the indicated order. The xi expression has a nonzero first-order term; the other three begin at second order. Constants may depend on the fixed coefficients, parameters, j and radii.

A finite polynomial satisfies A_lm(xi)=A_lm(1)+O(R^-1) and the analogous statement for C. A solid harmonic of degree l contributes R^l. A constant rotation by kappa log(R/R0), although it changes with R, has bounded sine and cosine coefficients; all remaining z-dependent twist derivatives are bounded on the fixed annulus. It therefore does not change these uniform estimates.

Combining factors shows that the main-channel potential remainders satisfy

    ||T-T0||_(C^j in z, main channels) <= C_j R^(-alpha-1),
    ||S-S0||_(C^j in z, main channels) <= C_j R^(-alpha).

The B-channel toroidal potential is O(R^(-2alpha-1)), and the D-channel poloidal potential is O(R^(-2alpha)). Since alpha>0, both are smaller than the respective main-channel remainder orders. An E-channel poloidal potential of degree l is O(R^(-l-1)). Since l>=2 and alpha<3/2, it too is smaller than O(R^(-alpha)). These statements hold in every fixed C^j norm in z by the same smooth-annulus argument. Thus the two displayed bounds hold for the full potential remainders.

Each derivative with respect to y contributes R^-1. The exact potential identities are

    curl(Ty)=grad T cross y,
    curl curl(Sy)=2 grad S+(D^2 S)y-y Delta S.

The first operator preserves the radial order of a potential; the second loses one power of R. Applying these formulas with j=3 proves U-U0=O(R^(-alpha-1)) and its first derivative O(R^(-alpha-2)) on the annulus. Taking the curl gives the asserted Omega bound. Every sufficiently large y belongs to such an annulus, and the constants are independent of R, so the pointwise exterior bounds follow.

## Proof of the rotating scaling law

For lambda>0, homogeneity of H_lm and psi0(lambda r)=psi0(r)+kappa log lambda give

    T0(lambda y)=lambda^(-alpha) T0(Q_{kappa log lambda} y),
    S0(lambda y)=lambda^(1-alpha) S0(Q_{kappa log lambda} y).

The toroidal and poloidal operators above commute with a constant rotation when the vector output is rotated back. Their scaling orders are zero and minus one, respectively. Applying them to the last two identities yields

    U0(lambda y)=lambda^(-alpha) Q_{-kappa log lambda} U0(Q_{kappa log lambda} y).

Taking one more curl yields the same identity with Omega0 and exponent -alpha-1. Set lambda=r and y=n to obtain the stated formulas. F and H are smooth on the unit sphere and hence square integrable.

## Energy and helicity consequences

The pointwise remainder bounds imply the sphere L2 bounds in ../energy_helicity/PROOF.md with delta=1, after multiplying the constants by sqrt(4pi). Here p=3-2alpha satisfies 0<p<1, so delta>p. That theorem therefore proves existence of the finite energy part with the actual coefficient A, and absolute convergence of helicity. Smoothness on bounded balls supplies their interior integrability. Its explicit remainder formulas apply if numerical upper bounds for C_U,C_Omega and R_b are separately established; no such numerical constants are supplied by this proof.

## Dependencies and scope

Dependencies are the specified finite potential representation, elementary Taylor bounds on a fixed compact annulus, the potential-to-velocity identities of ../field_reconstruction/PROOF.md, rotation covariance of curl, and the energy/helicity theorem in ../energy_helicity/PROOF.md. This is a mathematical property of the exact represented field, with its given real coefficients. It is not a quadrature-error bound, a proof of exact gauge A=1, or evidence that an Euler profile exists. No formalization has been performed.

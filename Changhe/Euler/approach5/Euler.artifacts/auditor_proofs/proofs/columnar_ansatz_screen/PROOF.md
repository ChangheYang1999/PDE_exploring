# Independent columnar-ansatz screen

## Exact statement

Fix s,R,L>0. In cylindrical coordinates consider

    v_r=(r/s)a(r/R), v_z=(z/s)b(r/R), v_theta=(z/s)g(r/R),

with continuous radial coefficients, and the differentiability needed for any stated derivative. The following four conclusions hold.

1. If the formula holds on all of R3 and v tends uniformly to zero at infinity, all coefficients vanish. A coefficient nonzero on a positive-radius interval gives infinite whole-space kinetic energy.
2. If g(xi)=k xi^2+O(xi^6) at zero with k nonzero, v fails Cartesian C2 regularity at each (0,0,z0) with z0 nonzero.
3. If g(r_*/R) is nonzero for some 0<r_*<R, the trace on the upper cap z=L cannot be continuously extended to a C1 curl-free field on every full disk of radius r_* just above that cap.
4. If g vanishes outside xi=1 and g(xi)^2=K(1-xi)^alpha(1+o(1)) inside, with K>0, 0<alpha<2 and fixed sign of g, then v is not differentiable across r=R at z nonzero.

These are tests of this ansatz, not a theorem about general Euler profiles.

## Proof

For fixed r>0 and theta, the radial component is independent of z and the other components are proportional to z. Uniform decay as |z| tends to infinity forces all three coefficients to vanish at that r; continuity handles the axis. If a coefficient is nonzero on an interval, continuity bounds it below on a smaller interval away from the axis. Cylindrical integration then contains either a positive multiple of integral_R dz or integral_R z^2 dz, both infinite.

On the line y=0,z=z0, the second Cartesian component is solely azimuthal:

    v_2(x,0,z0)=(z0/s) sign(x)g(|x|/R)
               =(z0 k/(s R^2))x|x|+O(|x|^6).

A C2 function has one second-order Taylor coefficient at zero. The right and left expressions have opposite nonzero coefficients, so no such Taylor expansion exists.

For the cap claim, Stokes gives zero circulation around each circle r=r_*, z=L+epsilon in the curl-free region. Continuity on a compact cap neighborhood makes the limit of these circulations the cap circulation. The latter is 2 pi r_* L g(r_*/R)/s, which is nonzero. This is impossible. The argument requires the full disk in the curl-free region, not merely an annulus. A vortical transition region does not satisfy its hypothesis.

For the interface claim, |g(xi)|/(1-xi)=sqrt(K)(1-xi)^(alpha/2-1)(1+o(1)) tends to infinity. Since g(1)=0, its one-sided difference quotient is unbounded. Projection onto the smooth azimuthal direction near any positive-radius point transfers this failure to the velocity.

If R=kappa s^nu, substituting r=s^nu rho and z=s^nu zeta gives the stationary similarity components rho a(rho/kappa), zeta b(rho/kappa), zeta g(rho/kappa). This field is equivariant under axial rotations, so adding a logarithmic axial rotation does not change it.

## Actual-manuscript application

The source is Adda-Bedia and Rica, *Self-focusing of helicity drives finite-time singularities in inviscid flows*, arXiv:2605.17569v2, 28 May 2026. Actual PDF evidence: in the team records, SHA256 `fdb8fd3dd19c7b5825005bf413c953568b9a98c6dae15e3f199bf533bbeef06d`. Independently inspected the title/version, equations (3.1)-(3.5), (4.23)-(4.29), (5.4)-(5.16), and Section 6.1 including the finite-cylinder matching description. Inspection date: 2026-11-02T19:46:51Z.

The source's positive swirl branch has g=sqrt(S_phi) and S_phi=12(1+4nu)a4 xi^4+O(xi^8), with positive leading coefficient. Thus test 2 applies, independently of the radial interface. The reported interface exponent lies between one and two; test 4 applies if that asserted asymptotic is taken. The source itself describes U_phi as only continuous there. Section 6.1 restricts the inner formula to a finite cylinder and proposes a curl-free outer matching. A direct continuous match across its caps with nonzero swirl is excluded by test 3. Treating the formula globally instead fails test 1.

The numerical ODE series and their convergence are not certified by this audit. None is needed for these conditional screens. The manuscript therefore does not supply the campaign's C2 decaying whole-space profile. A different outer solution with vorticity is not excluded by this argument.

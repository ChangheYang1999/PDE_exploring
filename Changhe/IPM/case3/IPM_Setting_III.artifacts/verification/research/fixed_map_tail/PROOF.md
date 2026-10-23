# A fixed radial map restricts the exponent of a smooth finite-basis release

Date: 2026-10-20. Status: independently derived exact representation identities. These exclude individual saved finite interpolants with a mismatched tail exponent, not the primary class. Independent numerical reconstruction tests are pending.

## 1. Representation and statement

Let L>0, kappa>1, eta=1/kappa, and gamma0=1-eta. Consider the following finite smooth representation, using polynomials B_k and finitely many angular modes:

    r=L sqrt((1+t)/2)/(1-t)^kappa, -1<=t<1,
    sigma=(1+t)/2, w=(1-t)/2,
    rho(r,theta)=r sin(theta) w sum_(k=0)^(M-1) sigma^k B_k(t) cos(2k theta).

The angular prefactor sigma^k cancels the Cartesian denominator in cos(2k theta), so rho is smooth at the origin. The map is fixed by kappa. A separate parameter ell>1 enters the transport field W=ell X+U[rho], with the canonical full-plane inverse, without changing the representation.

Define the endpoint data

    B0(theta)=sum_k B_k(1) cos(2k theta),
    B1(theta)=sum_k [B_k'(1)+(k/2)B_k(1)] cos(2k theta),
    gK=B0(pi/2).

Then the actual density exponent is gamma0, regardless of a separately recorded metadata field called gamma or 1/ell. Its first two coefficients are

    rho=r^gamma0 Theta0+r^(2gamma0-1) Theta1+O_symbol(r^(3gamma0-2)),
    Theta0=(L^eta/2) sin(theta) B0(theta),
    Theta1=-(L^(2eta)/2) sin(theta) [B1(theta)+(eta/4)B0(theta)].       (1)

In particular its actual axis amplitude at exponent gamma0 is

    K0=(L^eta/2)gK.                                                (2)

There is no factor 2^(-eta/2) in (2) for the displayed radial map. With gK nonzero, an exact unforced profile of this finite form must satisfy

    ell gamma0=1.                                                 (3)

More quantitatively, on the positive y-axis,

    |R|/N_f -> |ell gamma0-1|/(ell gamma0+1),
    |R|/N_v -> |ell gamma0-1|/(1+gamma0).                          (4)

Here R=W.grad rho-rho and the two denominators are exactly those in PROMPT. The same limits hold for a residual with a fixed forcing mu y(1+r^2/Lf^2)^(-2), because that source is O(r^-3). These are nonzero residual floors when (3) fails.

## 2. Expansion of the actual map

Put z=1-t and h=(L/r)^eta. The radial map gives

    z=h(1-z/2)^(eta/2).

Near h=0 this equation has a unique analytic solution z(h), since its derivative with respect to z at (z,h)=(0,0) is one. Expanding,

    z=h-(eta/4)h^2+O(h^3).

Also sigma=1-z/2. Polynomial expansion at t=1 yields

    sum sigma^k B_k(1-z)cos(2k theta)=B0-z B1+O(z^2).

Multiplying by r sin(theta)z/2 proves (1). Analyticity in h and finite smooth angular sums give the stated differentiated symbol remainder. Formula (2) follows by putting theta=pi/2. This proof uses the actual square-root sigma map, not a map with sqrt(1+t) instead.

At the other endpoint write u=1+t. The map obeys r^2=L^2 u/[2(2-u)^(2kappa)], an analytic function of u with nonzero derivative at zero. Thus u is analytic in r^2 near zero. Every factor r sin(theta) sigma^k cos(2k theta) is y times a smooth radial factor times Re(x+iy)^(2k). This proves the claimed Cartesian smoothness. No fractional central term is introduced by this representation.

## 3. Canonical inverse and residual

The density in Section1 is smooth, has the required parity, and has symbol bounds of order gamma0 in (0,1). The canonical inverse therefore has U=O(r^gamma0), with corresponding first-derivative bounds. This follows directly by splitting its Cartesian cancellation kernel into near, intermediate and far regions, as proved in ../inverse/PROOF.md and ../far_field_second_term/PROOF.md. It does not require the density to solve transport and introduces no free harmonic strain.

Consequently U.grad rho=O(r^(2gamma0-1)). Equation (1) gives

    R=(ell gamma0-1)r^gamma0 Theta0+O(r^(2gamma0-1)).         (5)

If gK!=0, (2) makes the leading coefficient on the y-axis nonzero. Equation R=0 then forces (3). Along that axis rho_x=0, so ell y rho_y=ell gamma0 K0 y^gamma0+o(y^gamma0), and U2 rho_y=O(y^(2gamma0-1)). Direct substitution into the definitions of N_f and N_v proves (4). No denominator threshold or near-axis exclusion is used: the positive y-axis is a valid test line; only the x-axis has symmetry-forced zero denominators.

If ell differs from 1/gamma0, the quantity y^(-1/ell)rho(0,y) equals K0 y^(gamma0-1/ell)(1+o(1)); it diverges in magnitude or tends to zero. Thus assigning a finite nonzero K at exponent 1/ell to such a saved function is incorrect.

## 4. Application and scope

The numerics lane's Q and QL release driver constructs its radial map at the initial ell, then changes ell in the transport rows while keeping the map fixed. The saved release checkpoint retains that map exponent in its field p, but writes gamma=1/ell using the final ell. Reconstruction must use the actual map exponent p, which is kappa here. It must not reinterpret that field as the density exponent.

For a release starting at ell=3, kappa=3/2 and gamma0=1/3 remain fixed. For a release starting at ell=3/2, kappa=3 and gamma0=2/3 remain fixed. Nonzero prescribed gK therefore restricts any exact solution of the finite representation to the initial ell. Such releases cannot test smooth existence with an unrestricted far-field exponent. This does not establish that changing the map would make the solver converge, nor that a profile exists at another ell. It identifies one imposed restriction and an explicit residual floor in the saved functions.

The independent verifier's free_cl_smooth_solver instead rebuilds its density exponent as 1/ell at every trial and changes the canonical-inverse matrices with that parameter. That different implementation still has nonzero residuals and does not provide a candidate.

Dependencies: the elementary analytic implicit-function expansion and the canonical inverse bounds cited above. Verification records will include raw checkpoint hashes, actual map metadata, independent scalar reconstruction, and Cartesian finite-difference/inverse evaluations. No numerical absence conclusion follows from a stalled optimizer, a finite cutoff or this representation calculation.

# Exact exponent and normalization of separately defined finite fields

Verifier result164. Written 2026-10-21 before implementing the comparison. This defines new finite fields from the coefficients of existing approximations. It does not reinterpret the literal saved binary formula as a different field, and it does not construct an exact profile.

## Statement and definitions

Use the smooth finite basis of ../smooth_representation/PROOF.md on R^2. Fix ell=5/2 and L=1. For a rational alpha in (0,1/2), w=(1+r^2)^(-alpha), sigma=r^2/(1+r^2), t=1-2w, and finite real polynomials B_k, put

    rho = y w sum_(k=0)^(M-1) sigma^k B_k(t) cos(2k theta).

The apparent angular factors are their smooth Cartesian expressions, Re((x+iy)^(2k))/(1+r^2)^k. Define the canonical full-plane stream by -Delta psi=rho_x with U=(-psi_y,psi_x)=o(r), odd stream parity and no added harmonic strain. Set a=B_0(-1), c=psi_xy(0), p=1-2alpha and K=sum_k(-1)^k B_k(1). Since L=1, K is the y-axis leading coefficient.

Field A is the literal original formula, with exact binary coefficients and the exact alpha computed by its scalar reconstructor. Field B keeps those coefficients but sets alpha=3/10 exactly, so p=2/5=1/ell. It is a separately defined field, recorded in an exact JSON input. Field C starts from B and makes the two polynomial corrections

    B_0(t) <- B_0(t)+u(t+1),
    B_1(t) <- B_1(t)+v(t+1),
    v=4alpha(1-ell-c),  u=(a-K+2v)/2,                    (1)

where a,c,K are the exact values for B. Absent B_1 is initially zero. Then C has exactly the original a, exactly c=1-ell, exactly K=a, and exactly p=1/ell. If a is nonzero, its center branch is nondegenerate and its reporting length L_axis=(K/a)^(1/(1-p)) equals1. Its canonical gauge is unchanged in kind: the new density determines a new canonical inverse, not a fitted harmonic correction. These exact statements do not imply the transport equation beyond its first derivative at zero.

For B and C the transport residual R=(ell X+U).grad rho-rho is uniformly O(r^(-1/5)) at infinity. Thus R tends to zero absolutely at infinity. Field A can instead have a leading residual (ell p-1) r^p Theta_0 when its literal exponent does not satisfy ell p=1. The growth of that leading residual is a property of A, not an obstruction to B, C, or an exact nearby profile. Finite residual samples for B/C are numerical evidence only; no existence or convergence conclusion follows.

## Canonical strain and exact projection proof

The independently proved canonical moment identity gives

    c=-a/4 + (1/(4alpha)) integral_0^1
       [B_1(1-2z)-(1-z^(1/alpha))B_2(1-2z)] dz.         (2)

It is obtained from c=-a/4+integral_0^infinity rho_3(r)r^(-2)dr by the substitution z=w. Endpoints converge because the basis is smooth at zero and sublinear at infinity. Formula(2) involves only rational integrals of powers when alpha and coefficients are rational, so c is exact rational.

The correction to B_0 is zero at t=-1, so a is preserved and its contribution -a/4 to c does not change. The correction to B_1 is v(2-2z) in(2), whose integral equals v; hence Delta c=v/(4alpha). At t=1 the corrections are 2u and2v. The y-axis cosine factor for k=1 is -1, so Delta K=2u-2v. Formula(1) therefore gives c_new=1-ell and K_new=a exactly. In the Chebyshev array, add u to its (k,j)=(0,0),(0,1) entries and v to its (1,0),(1,1) entries. No other entry changes.

The correction is rational and smooth. It preserves the SettingIII parities and sublinear growth. Differentiating transport at zero yields R_y(0)=a(ell+c-1), so field C satisfies this necessary first-order condition exactly. The degree-three and higher transport coefficients need not vanish. The finite-angular obstruction in ../finite_angular/PROOF.md excludes a nonzero exact profile at a fixed finite M, independently of rounding defects; that obstruction does not exclude approximation by a sequence with growing M.

## Far-field residual proof

For the finite polynomials, expand w=r^(-2alpha)(1+O(r^-2)) and sigma=1+O(r^-2), with derivatives. Uniformly in theta,

    rho = r^p Theta_0 + r^(2p-1)Theta_1 + O_S(r^(3p-2)),
    Theta_0=sin(theta)sum_k B_k(1)cos(2k theta),
    Theta_1=-2sin(theta)sum_k B'_k(1)cos(2k theta).       (3)

Here O_S includes any fixed finite derivative order, with one inverse radial power per Cartesian derivative. The geometric correction r^(p-2) is smaller than r^(3p-2) for p>0. For p=2/5, the canonical angular inverse of the leading density is nonresonant at every positive even stream frequency because p+1=7/5 is not an even integer. The canonical inverse of the remainder of degree2p-1=-1/5 is also nonresonant at its leading degree (2p=4/5 is not even). The finite-mode Green integrals therefore give

    U = r^p V_0 + O_S(r^(2p-1)).                       (4)

Any decaying global harmonic velocity starts at r^-3 and is absorbed by this bound. This follows directly by integrating each source mode with the full-plane Green formula, as in ../smooth_full_inverse_primitives/PROOF.md; no far-box boundary condition is imposed.

Insert(3),(4) into R. Euler differentiation of a homogeneous term gives

    R=(ell p-1)r^p Theta_0 + r^(2p-1) E_1
                                      +O_S(r^(3p-2)),
    E_1=[ell(2p-1)-1]Theta_1
          +p (V_0)_r Theta_0+(V_0)_theta Theta_0'.      (5)

For B/C, ell p=1 and2p-1=-1/5, proving the asserted absolute decay. E_1 is a finite smooth angular function, so the O-bound is uniform in theta even at trace zeros. This does not claim a useful explicit constant for any finite radius. For A the same two leading terms hold with its actual exponent, and a nonzero leading defect must be retained. The change in exponent may be tiny on fixed compact sets while changing which term dominates at arbitrarily large r; there is no uniform absolute perturbation claim on the whole plane.

## Verification plan, dependencies and scope

Freeze separate exact JSON inputs A, B, C. Verify coefficient differences, exact p, a, c and K; compare the source-tail primitive expression for c with the independent density-moment expression(2). Exercise(1) first on manufactured rational coefficient arrays. Evaluate selected original residual peaks, near-axis points and far radii with the independent multiprecision source primitives and Cartesian differentiation at two precisions. Record the field identity and input hash with every result. Check the two-term far asymptotic formula, without using it as the actual field evaluator. Report absolute residuals and both denominators, including their zeros, without filtering. The observed precision agreement is not an interval certificate.

Dependencies are the smooth basis, canonical inverse, exact center jets, finite source primitives and finite-angular exclusion, all independently developed in this lane. No numerical-lane code is used. This work supplies exact finite definitions and tests the numerical relevance of exponent/normalization rounding. Stationarity, convergence, existence, nonexistence and the primary decisive endpoint remain OPEN.

# Candidate001 has no stationary correction in its affine L2 class

Written at2026-10-29T14:33:08.589529+00:00, before the checker was implemented.

## Exact statement

Let rho be C1-N1-001-refit860-jabs, defined by the860 exact rational
potential generators in source/raw.json, SHA256
8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7.
Put c0=4076476460239181/2251799813685248, gamma=1/c0,
delta=1-gamma. The norm L2 means Lebesgue measure on R2. Let
U[h]=(-R1R2 h,R1^2 h), where Rj has symbol i xi_j/|xi|; this
Fourier multiplier defines U for every real h in L2. The reference's
canonical smooth velocity is u=(-chi_xyy,chi_xxy), and
rho=-partial_y Delta chi, with chi the exact stored potential.

The claim is that for every real c there is no real h in L2(R2)
satisfying

 F_c+div((cX+u)h)-(2c+1)h+U[h].grad rho+div(h U[h])=0       (1)

in distributions, where F_c=(cX+u).grad rho-rho. No symmetry, trace,
smallness or correction-gradient assumption is imposed on h. The
products are locally integrable: h U[h] is in L1, and the other
coefficients are smooth. In particular the candidate admits no
stationary correction in any registered norm that continuously embeds
in L2, at any radius and any exponent. This does not exclude a non-L2
repair, a weighted affine class, or an unrelated distant profile.

The analytic implication is conditional on the exact nonzero angular
coefficients checked below. Its numerical status and peer review must
be recorded separately before calling this candidate application proved.

## Exact leading coefficients and smooth asymptotics

Every generator is a rational multiple of

 H_m(X)(1+r^2)^(p_j-m) T(r^2/(1+r^2)),
 p_j=(3+gamma-j delta)/2,
 H_m=r^(2m)cos(2m theta),

where T=t^k or t^w P_n(2t-1). All stored indices are nonnegative
integers, j<=3, and P_n(1)=1. Therefore T(1)=1. With z=r^-2,
the radial factor remaining after r^(2p_j) is extracted is analytic
for |z|<1 and has constant term1. Consequently the leading potential
profile of branchj is exactly

 C_j(theta)=sum_m (sum_{rows with j,m} a_row) cos(2m theta). (2)

The finite analytic series has uniform angular remainders, as do its
fixed finite derivatives, on each exterior r>=r0>1. All fields are
smooth at zero because the denominator is positive, powers of1+r^2
are smooth, and each H_m is a polynomial. Thus u=O(r^gamma),
grad rho=O(r^(gamma-1)), uniformly in angle. Since0<gamma<1,
these are precisely the sublinear hypotheses of the annular theorem.
The potential realization of the canonical velocity is the same as
in the accepted generator contract. It also obeys div u=0 and
Delta u=(rho_xy,-rho_xx), by direct differentiation; smooth sublinear
canonical solutions are unique within the stated velocity parity,
since their difference is an entire sublinear harmonic vector and
therefore constant, and each velocity component is odd in one axis.
No polynomial or harmonic background velocity is added.

For a coefficient A r^d cos(n theta), write rho=-partial_y Delta chi.
Its sine coefficients at n+1 and n-1 are respectively

 -A(d^2-n^2)(d-2-n)/2,
 +A(d^2-n^2)(d-2+n)/2.                            (3)

The stream psi=chi_xy has sine coefficients at n+2 and n-2

 +A(d-n)(d-n-2)/4,
 -A(d+n)(d+n-2)/4.                               (4)

Negative sine frequencies reverse sign, and zero frequency vanishes.
Let G_j be the resulting density profile at exponent gamma-j delta,
and S_j its stream profile at exponent gamma-j delta+1.
The identities Delta psi=-partial_x rho and (3)-(4) are exact
independent checks on the algebra.

The leading density is r^gamma G_0. Its linear residual vanishes at
c0 because c0 gamma=1. At exponent q=2gamma-1 the complete residual
coefficient is

 E=(c0 q-1)G_1 + [u_0.grad(r^gamma G_0)]_angular.    (5)

To compute the last term, a stream mode A sin(m theta) with radial
exponent gamma+1 and a density mode B sin(n theta) with exponent
gamma contribute sine frequencies n+m and n-m with coefficients

 AB[-gamma m+(gamma+1)n]/2,
 AB[-gamma m-(gamma+1)n]/2.                         (6)

This follows from u_r=-psi_theta/r and u_theta=psi_r, retaining both
velocity components and every input mode. No mode is discarded because
only a low output frequency is of interest.

The checker independently sums all860 raw coefficients in (2), uses
(3)-(6), and checks exact coefficient equality with the full E_(1,0)
polynomial in N4-028. In particular its mode21 coefficient is nonzero.
It also checks G_0 is nonzero, 0<gamma<1, and
q=427123167131315/4076476460239181>0. All other residual exponents are
strictly less than q: their labels are gamma-h delta-2k, with h>=0,
k>=0; (0,0) vanishes, the retained leading sector is(1,0), and every
remaining exponent has h>=2 or k>=1. Therefore

 F_c0=r^q E(theta)+o(r^q),                          (7)

uniformly in angle, with E nonzero. This uses convergent finite-generator
series, not an assumed convergent stationary formal series.

## Annular contradiction at the fixed exponent

For completeness, choose a nonnegative nonzero smooth radial eta
supported in1<r<2, and set phi_R(X)=R^-1 eta(|X|/R)E(arg X).
Write A_R={R<|X|<2R}. Testing (1) against phi_R and using
||U[h]||2<=||h||2 gives

 |<F_c0,phi_R>| <= C ||h||L2(A_R)
   +C R^(gamma-1)(||h||L2(A_R)+||U[h]||L2(A_R))
   +C R^-2 ||h||L2(A_R)||U[h]||L2(A_R).             (8)

Every term tends to zero, since the annular L2 tails tend to zero
and gamma<1. On the other hand (7) gives

 <F_c0,phi_R>=R^(q+1)(A+o(1)),
 A=(int_1^2 t^(q+1)eta(t)dt)(int_0^(2pi)E(theta)^2 dtheta)>0.

As q>0, this diverges, contradicting(8). This is the already AUDITED
T4-049 argument, with its full divergence-form L2 domain.

## Changed exponents and normalization

For c different from c0,

 F_c=F_c0+(c-c0)X.grad rho
    =(c-c0)gamma r^gamma G_0+o(r^gamma).             (9)

Here q=2gamma-1<gamma, and differentiated analytic asymptotics give
X.grad rho=gamma r^gamma G_0+o(r^gamma). Since gamma>0 and G_0 is
nonzero, the coefficient in(9) is nonzero. The same annular proof
with q replaced by gamma excludes every changed exponent. No
unproved modulation theorem is invoked.

At high regularity the normalized correction condition would be
c[h]=partial_y U2[h](0)=0. Its formula includes the contact term
-h_y(0)/4. Neither this trace nor its absence at general L2 is needed
in the stronger contradiction. The entire affine L2 class is excluded,
so its normalized subset is excluded. A scaling mode that changes the
nonzero leading r^gamma density is not an L2 correction and falls
outside the statement. No assertion about uniqueness across charts is
made.

## Dependencies, verification and limits

The independent rational checker is a finite leading-coefficient
reconstruction, not a full-plane integration or an existence solver.
It must bind the raw snapshot, manifest, N4 coefficient output, this
proof, and the already accepted annular proof and review. A printed
positive sector norm alone does not replace the exact nonzero check.
Exact rational coefficient tables belong in JSON. The result file
records its actual time, checks and hashes. Independent Opus review
of the new application remains required for AUDITED status.

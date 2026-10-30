# Candidate001: independent coefficient check and exclusion of its affine L2 class

## Statement

Let chi be the potential specified by the 860 exact rational generators
of C1-N1-001-refit860-jabs. Its immutable generator SHA256 is
8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7.
Set

    c0 = 4076476460239181 / 2251799813685248,
    gamma = 1/c0, delta = 1-gamma,
    rho = -partial_y Delta chi, u = (-chi_xyy, chi_xxy).

All spaces below are real Lebesgue spaces on the entire plane. For
h in L2(R2), define U[h]=(-R1 R2 h,R1^2 h), where Rj has Fourier
symbol i xi_j/|xi|. Fix any real c and any constant v in R2, and put
F_(c,v)=(cX+u+v).grad rho-rho. There is no h in L2(R2) satisfying

    F_(c,v) + div((cX+u+v)h) - (2c+1)h
            + U[h].grad rho + div(h U[h]) = 0                 (1)

in distributions. There is no symmetry, trace, gradient, moment,
normalization or smallness hypothesis on h.

The conclusion concerns the specified reference and constant background
velocities, within the single affine class rho+L2. It does not exclude
non-L2 corrections, other far-field data, linear velocity backgrounds,
different profiles, or existence of a self-similar IPM profile.

The finite input of this argument is the exact coefficient identity
described below. The theorem is accepted only after its own checker
reconstructs that identity from the raw generators, compares it with
N4-028 and the independently reviewed T4 table, and verifies its sources.
The numerical point experiments in the Opus T2 review are not premises.

## Generator semantics and exterior expansion

Every raw row has rational coefficient a and the form

    a r^(2m) cos(2m theta) (1+r^2)^(p_j-m) T(t),
    p_j=(3+gamma-j delta)/2, t=r^2/(1+r^2).

Here j is 0,1,2,3, m is an integer between 0 and 9, and T(t) is either
t^k or t^w P_n(2t-1), with nonnegative integer indices and the ordinary
Legendre polynomial P_n. Its normalization is included in a.
The exact Bonnet recurrence gives P_n(1)=1, hence T(1)=1.

Put z=r^-2. Extracting r^(2p_j) leaves
(1+z)^(p_j-m)T(1/(1+z)), analytic near z=0 with value one there.
There are finitely many generators. Their expansions and every fixed
finite derivative therefore have remainders uniform in theta on the
exterior. Smoothness at the origin follows from
r^(2m)cos(2m theta)=Re(x+iy)^(2m) and smooth functions of r^2.

The branch-j density and velocity have leading degree gamma-j delta.
A radial descendant lowers that degree by an even nonnegative integer.
A velocity-density interaction between branches i and j has degree
gamma-(i+j+1)delta, before such radial descendants. Thus all residual
degrees have the form gamma-H delta-2K, H,K nonnegative integers.
The degree-gamma linear term vanishes because c0 gamma=1.

Let q=gamma-delta=2gamma-1. The own exact checker establishes

    q = 427123167131315 / 4076476460239181,  0<q<gamma<1,
    rho = r^gamma G0(theta) + r^q G1(theta) + o(r^q),
    F_(c0,0) = r^q E(theta) + o(r^q),                         (2)
    X.grad rho = gamma r^gamma G0(theta) + o(r^gamma).

Only the linear branch-1 density and u0.grad rho0 contribute at q.
Every other nonzero label has H>=2 or K>=1 and is strictly below q,
since delta>0. This ordering needs no claim that an unbounded set of
labels is pairwise distinct. The finite expansions also give
u=O(r^gamma) and grad rho=O(r^(gamma-1)), uniformly in angle.

## Exact reconstruction of the angular input

The own conversion expands each Legendre polynomial by its rational
three-term recurrence and combines canonical monomials. It is an exact
identity of potentials, as proved in ../refit_audit/PROOF.md.
For each homogeneous term r^s A(theta), independently differentiate
using

    partial_x = cos(theta) partial_r
                - sin(theta) r^-1 partial_theta,
    partial_y = sin(theta) partial_r
                + cos(theta) r^-1 partial_theta.

The implementation in ../sector_audit/code/sectors_flint.py applies
the resulting finite sine and cosine shifts, forms rho and both
Cartesian velocity components, and includes every ordered product.
The exact exponent-q coefficient is

    E = (c0 q-1) G1 + [u0.grad(r^gamma G0)]_angular.           (3)

The checker freshly constructs the leading potential, density and stream
of all four branches and (3). Each rational coefficient must equal the
frozen T4 table. E must also equal the first complete nonzero sector
already independently saved in N4-028, at label (H,K)=(1,0).

The required exact supports are

    supp G0 = {1,3,...,19},  supp E = {21,23,...,39}.

Both are sine polynomials with all ten listed coefficients nonzero.
Angular orthogonality therefore gives

    integral E G0 = 0,
    integral E^2 = pi sum_n E_n^2 > 0,
    integral G0^2 = pi sum_n G0_n^2 > 0.                     (4)

The large rational coefficients and squared sums stay in exact JSON.
No numerical sampling, radial quadrature or floating cancellation is
used to establish (2), (3) or (4). The accepted derivative identities
and finite analytic expansion justify their use for the exact profile.

## Distributional annular contradiction

The vector symbol of U is
(xi1 xi2/|xi|^2,-xi1^2/|xi|^2). It is perpendicular to xi and has
squared modulus xi1^2/|xi|^2<=1. Thus div U[h]=0 and
||U[h]||2<=||h||2. In particular h U[h] belongs to L1 and every term
of (1) is a well-defined distribution. No derivative or trace of h
is introduced.

Choose eta in C_c^infinity((1,2)), nonnegative and not identically
zero. For a fixed smooth angular polynomial A define

    phi_R(X)=R^-1 eta(|X|/R) A(arg X),
    A_R={X:R<|X|<2R}.

These are smooth compactly supported tests. Rescaling gives bounded
L2 norms of phi_R and X.grad phi_R, while
||grad phi_R||2=O(R^-1) and ||grad phi_R||infinity=O(R^-2).
The implicit constants are precisely the corresponding finite norms
of eta(r)A(theta) on 1<r<2.

By the uniform exterior estimates there is a finite M, depending only
on the exact reference, such that |u|<=M r^gamma and
|grad rho|<=M r^(gamma-1) for r>=2. Testing (1), integrating the
divergences by parts, and using Cauchy-Schwarz gives

    |<F_(c,v),phi_R>| <= C ||h||L2(A_R)
      + C R^(gamma-1)(||h||L2(A_R)+||U[h]||L2(A_R))
      + C |v| R^-1 ||h||L2(A_R)
      + C R^-2 ||h||L2(A_R)||U[h]||L2(A_R).                  (5)

Here C is a finite constant determined by this fixed c, M and the
four test norms just described; it is independent of R. The first
term bounds cX transport and (2c+1)h. The second bounds u transport
and U[h].grad rho. The last two terms bound the constant transport
and nonlinear divergence. Since h and U[h] belong to L2, their
annular tails tend to zero. Since gamma<1, the right side tends to
zero. This conclusion holds at any finite ||h||2.

If c=c0, use A=E. The constant background adds
v.grad rho=O(r^(gamma-1))=o(r^q), since gamma-1<q. From (2) and (4),

    <F_(c0,v),phi_R> = R^(q+1)(C_E+o(1)),
    C_E = (integral_1^2 t^(q+1)eta(t)dt)(integral_0^(2pi)E^2)>0.

This diverges because q>0, contradicting (5).

If c!=c0, use A=G0. The exact identity
F_(c,v)=F_(c0,0)+(c-c0)X.grad rho+v.grad rho and (2) give

    <F_(c,v),phi_R>
      = R^(gamma+1)((c-c0)gamma C_G+o(1)),
    C_G = (integral_1^2 t^(gamma+1)eta(t)dt)
          (integral_0^(2pi)G0^2)>0.

Its absolute value diverges, again contradicting (5).
The angular factor must change together with the radial exponent:
using E for the changed-c leading term would give zero by (4).
This explicit choice incorporates T2's correction and T4's erratum.

## Reviews, verification and scope

Read the complete T4 original application, its erratum and accepted
review proof, T1 R1-046, and T2 the review of T4-458. T1 independently uses
homogeneous Cartesian differentiation; T2 uses exact Wirtinger
differentiation. Both agree with the exact angular table. The own
checker executes only the own conversion and sector algorithms and
fresh finite arithmetic. Peer scripts are frozen as text.

Record the raw and canonical hashes, all own imported modules, the
original N4-028 result, peer proof and review hashes, every coefficient
comparison, exact nonzero norms, source preservation and actual runtime.
The Opus collaboration is through the existing theory lanes configured
for us.anthropic.claude-opus-5-5. Their provider response identity is not
observable from these local files; no substitute or remote client is
used by this lane.

Exclusion of the entire affine L2 class includes any normalized subset
or correction space embedded in L2. It does not extend by implication
to a decaying-weight space admitting non-L2 functions. This proof
constructs no inverse, contraction or existence theorem.

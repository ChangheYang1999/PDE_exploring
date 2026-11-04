# A radial convex-test obstruction from the spherical mean of the source

Status: independent derivation submitted for existing-agent comparison. No designated CONFIRMED verdict yet. No novelty or optimal-growth claim is made.

## 1. Exact statement and notation

Let U belong to C^1(R^3;R^3), with div U=0, and write

    E(R)=integral_(|y|<R) |U(y)|^2 dy,
    q(y)=tr((DU(y))^2),
    Q(r)=integral_(S^2) q(r theta) d sigma(theta),   r>=0.

Assume E(R)=o(R). If Q(r)>=0 for all r>=0, or Q(r)<=0 for all r>=0, then U=0.

This is a statement about a divergence-free vector field. It does not assume an Euler equation or even the existence of a pressure. A useful intermediate statement is: if E(R)=o(R) and Q is identically zero, then U=0. The proof uses only the distributional double-divergence identity, radial integration and a compactly supported cutoff of a convex test with a controlled annular error.

## 2. The double-divergence identity and the signed mean

For a smooth divergence-free field,

    q=partial_i partial_j(U_i U_j).

For C1 fields this follows in distributions by local convolution, which preserves divergence and gives local uniform convergence of the fields and their first derivatives. Thus for every compact smooth scalar test psi,

    integral q psi=integral (U tensor U):D^2 psi.             (1)

Choose a radial chi in C_c^infinity(R^3), with 0<=chi<=1, chi=1 on B_1 and chi=0 outside B_2, and set chi_R(y)=chi(y/R). Write K2=sup ||D^2 chi||_op. Then

    |integral q chi_R|<=K2 R^-2 E(2R).                      (2)

Because chi_R is radial, the left integral is integral_0^infinity Q(r) chi(r/R) r^2 dr, where the radial profile of chi is denoted by the same letter. If Q>=0, for every fixed L and R>=L,

    0<=integral_0^L Q(r) r^2 dr<=K2 R^-2 E(2R)->0.

Continuity of Q gives Q=0. The case Q<=0 follows by reversing the sign. This step would already follow from E=o(R^2). The stronger E=o(R) assumption is used next.

## 3. A convex radial test with vanishing boundary error

Set f(y)=sqrt(1+|y|^2), and take psi_R=f chi_R in (1). This test is smooth and compactly supported, and Q=0 gives

    integral q psi_R=0.

The Hessian of f is

    D^2 f=(1+|y|^2)^(-1/2) I
          -(1+|y|^2)^(-3/2) y tensor y.

Its tangential eigenvalue is (1+|y|^2)^(-1/2), and its radial eigenvalue is (1+|y|^2)^(-3/2). Both are strictly positive. Expanding the product Hessian yields

    0=integral chi_R U.D^2 f U+integral U.H_R U,
    H_R=f D^2 chi_R+grad f tensor grad chi_R
                         +grad chi_R tensor grad f.      (3)

H_R is supported in R<=|y|<=2R. For R>=1, f<=sqrt(5) R there, |grad f|<=1, |grad chi_R|<=K1/R and ||D^2 chi_R||_op<=K2/R^2, where K1=sup|grad chi|. Hence

    ||H_R||_op<=(sqrt(5)K2+2K1)/R,
    |integral U.H_R U|<=C_chi E(2R)/R->0.                 (4)

The first integral in (3) is nonnegative. Fix L and take R>=max(1,L). Since chi_R=1 on B_L,

    (1+L^2)^(-3/2) E(L)
      <=integral chi_R U.D^2 f U
      <=C_chi E(2R)/R->0.

Thus E(L)=0 for every L. Continuity gives U=0. No boundary value of U or DU was imposed; the only boundary estimate is (4). This proves both the intermediate and signed-mean statements.

## 4. Consequences for Euler profiles and the axial angular mean

For a C1/C1 full Euler profile with bounded U, Hb meaning U(R.) tends to zero in distributions, 0<c<1/2 and any finite omega, the confirmed energy theorem A052-A053 gives E=o(R): the velocity is already zero for c<2/5, its energy is finite at c=2/5, and its exponent 5-2/c lies in (0,1) for 2/5<c<1/2. Therefore a nonzero profile in this class must have Q positive at some radius and negative at another radius.

In particular, define the axial angular mean

    q_0(rho,z)=(2pi)^-1 integral_0^(2pi)
                    q(rho cos(theta),rho sin(theta),z) d theta.

If q_0 has one sign everywhere, then Q has that sign, because for r>0

    Q(r)=2pi integral_(-1)^1 q_0(r sqrt(1-u^2), r u) du.

Consequently a nonzero profile in this class also requires the angular mean q_0 to take both signs. Uniformly decaying profiles satisfy Hb, so this applies to the campaign interval for every finite omega. No derivative decay, pressure symmetry or flow hypothesis is added.

This conclusion extends the particular sign criterion of LIT362 only in the range where the stronger E=o(R) estimate is available. It does not claim the same averaged-sign result under E=o(R^2), nor at c=1/2. The A052-A053 energy theorem is the named dependency of the Euler consequence, not of the divergence-free theorem in Sections1-3.

## 5. Scope, comparison target and negative control

The C07:02:05 comparison, item14, correctly leaves nonzero angular pressure modes unrestricted after the projection step. Sections2-3 supply an additional radial convex-test argument under E=o(R). The new argument does not infer those modes vanish individually. It directly forces the positive velocity integral to vanish when the spherical mean of q is zero.

The growth hypothesis cannot simply be discarded: a nonzero constant field is divergence-free and has q=Q=0, but E(R)=(4pi/3)|U|^2 R^3. This is not a counterexample to the stated theorem. No sharpness at linear growth is asserted. The theorem supplies a new necessary sign variation under its assumptions; it does not derive a forbidden mean sign from decay and therefore does not settle the unrestricted rotating conjecture.

All calculations above are symbolic algebra performed by hand. No computation, external theorem beyond the stated elementary identities, or formal proof build was used. Existing model-agent comparison is requested before any designated confirmation.

## 6. Complete C comparison and three explicit consequences

The full C comparison dated 2026-11-04T07:15:46Z, all eight analytical items and its diagnostic description, was read. The original five-section proof agrees with it. The phrase in Section1 has been clarified to say a compactly supported cutoff of a convex test: the cutoff product itself is not asserted convex. The eighteen-item diagnostic script, Gaussian sample and quadrature were not read or rerun here and are not certified.

The following quantitative version of C item4 follows directly from (1)-(4). Choose chi with a nonincreasing radial profile, so chi_R increases pointwise to1. For every nonzero divergence-free C1 U with E=o(R),

    integral_0^infinity Q(r) chi(r/R) r^2 dr ->0,
    integral_0^infinity Q(r) sqrt(1+r^2) chi(r/R) r^2 dr
       -> integral_R3 U.D^2 f U in (0,+infinity].          (5)

The first limit is (2). For the second, the right side of (3) without the zero-source hypothesis is the nonnegative Hessian integral plus the error in (4). Monotone convergence applies to its nonnegative main term, and the error tends to zero. Strict positivity follows because continuous nonzero U is nonzero on an open set and D^2 f is positive definite everywhere. The limit may be infinite. No uncut conditionally convergent integral of Q is asserted.

A precise linear-growth countertest, consistent with C item5 and LIT366, is U=(0,0,g(x1,x2)), where g=(1-rho^2)^2 for rho<1 and g=0 for rho>=1. This is C1, divergence-free, and (DU)^2=0, so Q=0. For R>1,

    E(R)=2 integral_(rho<1) sqrt(R^2-rho^2)g^2 dx1 dx2
        =2R integral_(rho<1)g^2 dx1 dx2+O(R^-1)
        =(2pi/5)R+O(R^-1).

The integral of g^2 is 2pi integral_0^1 rho(1-rho^2)^4 d rho=pi/5. The remainder estimate is uniform on the unit disk. Thus E=o(R) cannot be replaced by E=O(R) for this kinematic theorem. This does not prove that the same threshold is sharp within the full Euler class. The field fails decay along the vertical direction. In the target c interval it also fails full momentum: horizontal momentum makes P depend only on z, while vertical momentum at rho=0 gives P'=-(1-c) and at rho>1 gives P'=0.

Finally, combine Section4 with A3042 and the C1 global pressure theorem A3047. A nonzero bounded C1/C1 full profile with Hb and 0<c<1/2 must have a spherical mean Q and an axial mean q_0 taking both signs. Its actual pressure cannot be axisymmetric: otherwise A3047 gives an axial constant U, while E=o(R) excludes a nonzero constant. Fourier uniqueness for the continuous periodic function P(rho,theta,z) then gives some nonzero integer m for which P_m is not identically zero. A3042 gives q_m not identically zero for the same m. This strengthens the regularity in C item6 to C1 using the separately confirmed A3047. Neither the sign changes nor the nonzero mode are contradictions.


## 7. Existing-agent comparisons

The full C07:15:46 comparison and A117 comparison were read. Both independently confirm the distributional double-divergence identity, radial cutoff, positive Hessian and vanishing annular error in Sections1-4. A117 correctly notes that Q<=0 needs the convex test alone; the preliminary cutoff reduction remains a valid common proof for either sign. The source-sign criterion here and the pointwise-source criterion A3044 have different growth ranges. The present criterion contains the pointwise-sign conclusion on0<c<1/2; A3044 separately reaches0<c<2/3 with a pointwise sign and cannot be subsumed by an assertion at the excluded endpoint1/2.

C's scalar-mode observation is valid; Section6 uses the independently confirmed C1 theorem A3047 to state its C1 version, while C's original comparison cited C2 theorem A3029. The sharp linear-growth shear is a kinematic control only. Neither the diagnostic scripts and logs, Gaussian samples, numerical quadrature, nor the first or revised A117 diagnostic run is read or certified. A117's optional R1-R3 are separate analytical proposals and are not automatically included in the verdict on Sections1-7. Existing configured model collaboration is through the files, with actual provider execution independently unattested.

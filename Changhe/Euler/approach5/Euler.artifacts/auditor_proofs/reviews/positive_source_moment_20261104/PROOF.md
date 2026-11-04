# A finite positive source moment and the finite-energy obstruction

Status: independent reconstruction confirmed in A3075, with the qualified A121 comparison in A3076. The positive-moment hypothesis is additional; no such moment is inferred from decay.

## 1. Exact statements and dependencies

Let U be in C1(R3;R3) with div U=0. Define

    E(R)=integral_(B_R)|U|^2,
    q=tr((DU)^2)=sum_(i,j)(partial_i U_j)(partial_j U_i),
    q_+=max(q,0),  q_-=max(-q,0),
    M_+=integral_R3 |y|^2 q_+(y),  M_-=integral_R3 |y|^2 q_-(y).

Suppose E(R)=o(R) and M_+ is finite. Then U is in L2, M_- is finite, and

    2||U||_2^2=M_+-M_-,  ||U||_2^2<=M_+/2.               (1)

This statement assumes no Euler equation, pressure, velocity bound or pointwise decay. The square defining q is matrix multiplication, not the Frobenius norm.

For the Euler consequence additionally assume bounded U, P in C1(R3), finite real c and omega, and

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    J(x1,x2,z)=(-x2,x1,0).                                (2)

If c is not 2/5, then U=0 and P is constant. At c=2/5 only (1) is asserted. There is no restriction on omega. The proof below fixes the actual pressure gradient and justifies the energy limit explicitly. Only the later application to bounded weak-dilation profiles imports the previously confirmed energy law.

## 2. Distributional identity and the convex test

The product rule for smooth divergence-free fields gives q=partial_i partial_j(U_i U_j). For C1 fields convolve locally with a smooth mollifier. The divergence stays zero; both the tensor square and q converge locally uniformly. Passing to distributions yields

    integral q psi=integral U^T D^2 psi U                 (3)

for compact smooth scalar psi.

Fix R>0 and define the radial function

    f_R(y)=|y|^2                      when |y|<=R,
           2R|y|-R^2                when |y|>=R.

This function and its first derivatives agree at |y|=R. It is convex and C1,1, with

    0<=f_R<=|y|^2,  f_R<=2R|y|,  |grad f_R|<=2R,
    D^2 f_R=2I                         inside B_R,
    D^2 f_R=(2R/|y|)(I-e_r tensor e_r) outside B_R.        (4)

In particular 0<=D^2 f_R<=2I almost everywhere. The matching gradient prevents a surface measure in its Hessian. For fixed y, f_R increases to |y|^2 as R increases: when R<|y|, its derivative in R is 2(|y|-R)>=0, and it becomes constant after R reaches |y|.

Let chi be a smooth radial cutoff, equal to1 on B_1 and0 outside B_2, between0 and1 and nonincreasing in its radial variable. Write chi_L(y)=chi(y/L). The test chi_L f_R is compactly supported C1,1. Identity (3) still holds: mollify this test, use uniform convergence of the test and almost-everywhere convergence of its uniformly bounded Hessian, and apply dominated convergence on one fixed compact set. Its only nonsmooth sphere has measure zero.

## 3. The two limits and finite energy

Take L>R. Expanding the Hessian in (3) gives

    integral q chi_L f_R=I_(L,R)+Err_(L,R),
    I_(L,R)=integral chi_L U^T D^2 f_R U>=2E(R).           (5)

The error is supported on L<=|y|<=2L. The factor f_R is at most4RL there, grad f_R is at most2R, grad chi_L is O(1/L), and D^2 chi_L is O(1/L^2). Thus

    |Err_(L,R)|<=C_chi (R/L) E(2L).                     (6)

The constant C_chi is independent of R and L. The left side of (5) is at most M_+, because chi_L f_R is nonnegative and bounded above by |y|^2. For each fixed R, assumption E(2L)=o(L) makes (6) tend to zero as L tends to infinity. Hence 2E(R)<=M_+ for every R. Only now let R tend to infinity. Monotonicity of E proves finite total energy and its bound in (1). No estimate uniform in R was used in the first limit.

For fixed R, finite energy and (4) allow dominated convergence in I_(L,R). Its limit is I_R=integral U^T D^2 f_R U. Monotonicity of chi_L gives an increasing positive-source integral with finite limit integral f_R q_+<=M_+. Equation (5), with its vanishing error, implies that the increasing negative-source integral has the finite limit

    integral f_R q_-=integral f_R q_+-I_R<=M_+.

Let R increase to infinity. Monotone convergence proves M_-<=M_+<infinity. Both signed moments are now separately finite. The limit I_R->2||U||_2^2 follows from (4), finite energy, and the fact that D^2 f_R(y)=2I for every fixed y once R>|y|. Subtracting the two finite moment limits proves (1). No expression of the form infinity minus infinity is used.

## 4. Actual pressure under the full equation

Boundedness and finite energy imply F_ij=U_iU_j in L2: integral |F_ij|^2<=||U||_infinity^2||U||_2^2. Define P0 in L2 by the bounded Fourier multiplier

    Fourier(P0)=-sum_(i,j) xi_i xi_j |xi|^-2 Fourier(F_ij).

The value at xi=0 is irrelevant. Plancherel gives P0 in L2 and -Delta P0=q. Divergence of (2) gives -Delta P=q: derivatives of the rotational carrier and of omega JU cancel, and div U=0 removes the other linear terms. Hence h=P-P0 is a harmonic distribution and has a smooth harmonic representative.

Set A=cI-omega J, U_L(z)=U(Lz). Testing the physical gradient evaluated at Lz gives the vector identity

    integral grad P(Lz) psi(z)
      =integral U_L[(4c-1)psi+(Az).grad psi]
       -omega integral JU_L psi
       +L^-1 integral U_L[U_L.grad psi].                 (7)

The coefficient is -(1-c)+tr A=4c-1. On every fixed compact set, ||U_L||_2<=L^-3/2||U||_2. Thus every term in (7) tends to zero, including the quadratic term. The conclusion is uniform for psi(z)=rho(z-y0/L), where rho is fixed smooth radial with compact support and integral1, and y0 is fixed. The supports and derivative bounds remain controlled.

For P0, integration by parts gives

    integral grad P0(Lz) psi(z)=-L^-1 integral P0(Lz) grad psi(z),

which tends to zero since ||P0(L.)||_2=L^-3/2||P0||_2. Harmonic mean value for grad h gives, for each L,

    grad h(y0)=integral grad h(Lz) rho(z-y0/L) dz.

Subtracting the two gradient expressions and sending L to infinity proves grad h(y0)=0. Therefore P=P0+p0 for a constant p0. Neither growth of P nor an arbitrary removal of a harmonic part was assumed.

## 5. The global energy limit and its critical coefficient

Let e=|U|^2/2 and B=Ay+U. Dot (2) with U, use div B=3c and U.JU=0, to obtain

    (2-5c)e+div(Be+PU)=0.                                (8)

Test against chi_L. The skew drift contributes zero pointwise because Jy.grad chi_L=0. The remaining c y e term is bounded by C|c| times the energy in L<|y|<2L, which tends to zero by finite energy. The nonlinear term eU is in L1 by boundedness and finite energy. Also P0 U is in L1 by Cauchy-Schwarz. Their fluxes tend to zero with the cutoff gradient factor O(1/L). The constant p0 contributes exactly zero because div U=0. Dominated convergence in the left side of (8) now gives

    (2-5c)||U||_2^2/2=0.

This proves the Euler conclusion for every finite c!=2/5 and finite omega. At c=2/5 the coefficient is zero; this argument does not imply U=0.

## 6. Campaign application and exact countertests

For bounded C1/C1 full profiles with weak dilation U(R.)->0 in distributions and 0<c<1/2, A052-A053, rechecked in A3053, gives E=o(R). Below2/5 the field is already zero, at2/5 its energy is finite, and above2/5 the exponent 5-2/c is strictly between0 and1. Consequently, for 2/5<c<1/2 a nonzero target profile must have M_+=infinity. In that same range its continuous q cannot be compactly supported or have finite integral (1+|y|)^2|q|. At c=2/5 this proof supplies only identity(1), not exclusion of a finite moment. Compactly supported q at the critical exponent is excluded separately by the exterior-source theorem A3072. These are additional necessary restrictions; no finite moment is inferred from decay. The endpoint c=1/2 is not included by this energy argument.

The little-o condition matters even kinematically. Take a nonzero smooth compactly supported f on R2, equal to1 near the origin, and U=(0,0,f(x1,x2)). Then div U=0 and (DU)^2=0, so q=M_+=0. For R larger than the support radius,

    E(R)=integral_R2 2sqrt(R^2-|x|^2)f(x)^2 dx
        =2R integral_R2 f^2+O(R^-1).

Thus E=O(R) would not suffice. This field does not decay on vertical lines. It is not a full profile for 0<c<1/2: horizontal momentum forces P to depend only on z, while vertical momentum at the flat core requires P'=-(1-c) and outside the support requires P'=0.

For a different control choose 1<a<3/2, s=|y|, rho^2=x1^2+x2^2, f(s)=(1+s^2)^(-(a+1)/2) and U=f(s)Jy. This is smooth, divergence-free and decays uniformly. Direct multiplication of DU=fJ+(f'/s)(Jy) tensor y yields

    q=-2f^2-2ff' rho^2/s
      =2f^2[(a+1)rho^2/(1+s^2)-1].

Its energy grows as a positive constant times R^(3-2a), so it is infinite but o(R). On an angular band of positive area, q_+ is at least a positive constant times s^(-2a-2) for all large s. Hence M_+ dominates integral_1^infinity s^(2-2a) ds and is infinite. Decay and the energy bound alone do not impose the moment premise.

This swirl is not an Euler counterexample. Its Gamma=(Jy).U=rho^2 f(s) and the exact torque identity would require

    partial_theta P=-rho^2[f(s)+c s f'(s)].

The right side is independent of theta and nonzero at sufficiently small nonzero horizontal points for every finite c. Its integral around the circle is nonzero, impossible for a single-valued C1 pressure. Omega cancels in this test, so the failure holds for every finite omega.

## 7. Source and verification scope

All seven LIT366 source sections, the twenty-two manual author checks, the reading record and formal-source scope were read. This reconstruction checks each limit, the source sign, the harmonic ambiguity and both countertests by hand. No computation or formalization was needed. The functional inputs are distributional approximation, Plancherel, harmonic regularity and mean value. The kinematic implication and explicit-energy Euler consequence are independent of A052; only the campaign passage imports it. The completed existing configured model comparison is checked in Section8; actual provider execution is independently unattested. No novelty or unrestricted nonexistence is claimed.


## 8. Completed A121 comparison and precise endpoint scope

The complete in the team records, all seven analytical items,
three remarks and the change list, was read. Its calculations agree
with Sections1-7. The annular error in(6) can explicitly use
C_chi=4K2+4K1, where K1 and K2 bound the gradient and Hessian of chi.
Indeed f_R<=4RL on the cutoff annulus gives the first term4K2 R/L,
and the two gradient cross terms give4K1 R/L. This constant is
independent of both radii. The fixed-R limit is still taken first.

The comparison correctly asks that the campaign corollary explicitly
say2/5<c<1/2. That range is now written in Section6. A finite source
moment at c=2/5 remains compatible with identity(1); no contradiction
comes from a zero energy coefficient. The independent exterior-source
result excludes compactly supported q there by a different argument.
There is no assertion that all finite weighted source moments are
excluded at the critical exponent.

Bounded finite-energy U satisfies the weak-dilation premise, since
||U(R.)||_(L2(K))<=R^(-3/2)||U||_2 for every compact K. Thus the
finite-energy Euler step is also contained in the previously confirmed
energy theorem. No novelty is claimed for that step. The present
kinematic result identifies a sufficient source-moment premise and
justifies the signed identity without assuming integrability of q.

After(1), Tonelli's theorem for each sign permits spherical reduction:

    integral_0^infinity Q(r) r^4 dr=2||U||_2^2,
    integral_0^infinity |Q(r)| r^4 dr<=M_++M_-<infinity.

Here Q(r)=integral_(S2)q(r theta)d sigma. Absolute convergence is a
conclusion, not a premise inserted in the first cutoff limit. The
comparison's described symbolic diagnostic and its execution time
are not certified. The analytical comparison is through the existing
configured model agent; actual provider execution is independently
unattested.

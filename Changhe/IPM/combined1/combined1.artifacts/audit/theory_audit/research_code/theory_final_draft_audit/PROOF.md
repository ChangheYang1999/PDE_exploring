# Audit of the H12 theory report, draft 3

## Source, purpose and notation

The reviewed source is the immutable local copy
`source/THEORY_FINAL_0503.md`, copied from working file THEORY_FINAL.md. (not published) Its
header is draft 3, 2026-10-29T04:58Z, and its SHA256 is
73aa2b484bff6e15c1cd762f918cf4192d1ec6b9ae1cc56ca5c3cb39ec85e7f2.
The report assembles previously audited theorems. This audit checks the
assembly and the scope of the comparisons. It does not withdraw the
conditional theorems proved in their full source files.

Write H for real S1 L2(R2), whose functions are even in x and odd in y.
Put J=(1-Delta)^(1/2), omega=(1+4|X|^2)^(2/5), and use the full ordered
Cartesian Hessian. Define the two completed forcing spaces by

    N_s(f)^2 = ||omega D2 J^s f||2^2
             + 2^14 ||D J^s f||2^2 + 2^18 ||J^s f||2^2
             + 2^18 (20/21) ||J^s f||Hdot^-1^2,
    X_t(f)^2 = ||omega D2 J^t f||2^2
             + 2^15 ||D J^t f||2^2 + 2^20 ||J^t f||2^2.

Here s=2^-18 and t=1/5184, so 0<s<t. The spaces are completions of compact
smooth S1 functions, as in A2 S1_CLOSURE.md, lines 66-80, and the new
sharpw theorem. All statements below concern these exact spaces.

## 1. Invertibility at zero is not the positive-real resolvent hypothesis

The report's section 2.4 correctly defines (L0): every lambda>=0 is in
the low resolvent set of every A_k on the ball, with a uniform inverse
bound at zero. The subsequent finite-rank sentence is insufficient if
read as a certificate from its displayed assumptions alone. Dissipativity
of D_0 and a nonzero singular-value margin for M_k(0) do not verify (L0).

A counterexample already exists at k=0. Take any normalized e in H and
let P h=<h,e>e. Set D=-I, Psi a=2ae, Phi h=<h,e>, and

    A=D+Psi Phi=-I+2P.

D is bounded and maximally dissipative with gap beta_D=1. At zero,
R=D^-1=-I and M(0)=1+Phi R Psi=-1, whose smallest singular value is 1.
A^-1=A has norm 1. The displayed Woodbury bound is valid and gives the
larger bound 1+2=3. Nevertheless Ae=e, so lambda=1 is not in rho(A).
Thus even a perfect zero-parameter certificate does not prove (L0).

The sufficient repair is the full statement already proved in
../stationary_resolvent_audit/PROOF.md, sections 3-4, together with the
raw-low-norm repair in ../finite_rank_repair_audit/PROOF.md. Require the
consistent maximal low and high generators. Require D_k to have
||(D_k-lambda)^-1||<=1/(beta_D+lambda) for every k in the ball and
lambda>=0. For each lambda certify M_0(lambda), then control the
perturbation M_k(lambda)-M_0(lambda) uniformly on the ball. A finite
interval cover and a separate large-lambda Neumann bound can give this
certificate. Finally the margin at zero supplies K_L through Woodbury.
A high-column bound must also be justified; its raw-L2 version does not
need the spurious extra positivity loss of the original coarse proof.
No such whole-axis matrix certificate is currently supplied for a
campaign candidate.

Verdict: REFUTED as a standalone sufficient implication in the shortened
sentence. The full TP-1/TP-1b source and its repaired proof remain valid.

## 2. The two selected forcing spaces are incomparable

The claims in sections 0.2, 2.8 and 4 that the selected sharpw forcing
space is larger than the A2 forcing space are false as set inclusions.
Deleting Hdot^-1 relaxes low-frequency membership. Increasing s to t
strengthens high-frequency membership. We prove both non-inclusions.

Fix the unitary Fourier transform. Choose a nonzero real smooth bump eta
supported in {|xi|<1/10}, even in each coordinate. Put R_n=4^n,
q=(s+t)/2, and a_n=R_n^(-(2+q)), for n>=1. Define

    fhat(xi)=i sum_n a_n [eta(xi-R_n e2)-eta(xi+R_n e2)].       (1)

Its disjoint supports make f real and S1. On each support |xi| is
comparable to R_n. Consequently its H^(2+t) norm squared is bounded
below by a positive constant times

    sum_n a_n^2 R_n^(4+2t) = sum_n R_n^(2(t-q)) = infinity.  (2)

Thus f is not in X_t. On the other hand, N_s(f) is finite. The low and
first derivative components are bounded by the analogous convergent
sums. There is no low-frequency contribution to Hdot^-1. To verify the
weighted Hessian, use omega(X)<=C(1+|X|^2)^(1/2) and Plancherel:

    ||omega D2 J^s f||2^2
       <= C sum_ij (||m_ij fhat||2^2+||Dxi(m_ij fhat)||2^2),
    m_ij=xi_i xi_j (1+|xi|^2)^(s/2).                       (3)

The fixed bumps and their first derivatives have fixed L2 norms, while
m_ij and Dxi m_ij are O(R_n^(2+s)) on their supports. The right side is
at most C sum_n a_n^2 R_n^(4+2s), which converges since q>s. Partial sums
converge in N_s by the same bounds. Each partial sum is Schwartz and S1;
symmetric physical cutoffs approximate it in N_s. For the negative
component this follows, for a Schwartz zero-mean S1 function g, from

    |ghat(xi)|<=|xi| |||X|g||1 near xi=0,

and from its L2 bound away from zero. The other weighted fractional
components follow from continuity of J^s on Schwartz functions.
This also verifies membership in the specified completion, not just
formal finiteness of the norm. Therefore N_s is not a subset of X_t.

For the opposite direction choose a real smooth radial eta_0 supported
in 1<|xi|<2, not identically zero, and let

    psi(xi)=i xi_2 eta_0(xi), r_n=4^-n, b_n=r_n,
    ghat(xi)=sum_n b_n r_n^-1 psi(xi/r_n).                 (4)

The annular supports are disjoint. The parity and Fourier conjugation
conditions again give a real S1 function. Each summand has L2 norm
b_n||psi||2, so g is in L2. But its Hdot^-1 norm squared is

    sum_n b_n^2 r_n^-2 integral |psi(zeta)|^2/|zeta|^2 dzeta
      = infinity.                                       (5)

J^s is bounded below by 1, so N_s(g)=infinity. Conversely X_t(g) is
finite. All supports lie in a bounded frequency ball. Each Hessian
Fourier summand has norm O(b_n r_n^2), and its first xi derivative has
norm O(b_n r_n). The smooth J^t multiplier preserves these bounds.
Equation (3) with t in place of s bounds the weighted Hessian by a
convergent sum of b_n^2(r_n^4+r_n^2). The lower components are finite as
well. Partial sums converge in X_t by these estimates and are Schwartz;
physical cutoffs put g in the X_t completion. Hence X_t is not a subset
of N_s.

At a common exponent u the correct one-way statement is immediate:
N_u membership implies X_u membership. The finite positive component
weights are equivalent and X_u lacks the negative component. This is
a strict inclusion by (4). For the selected unequal exponents, the
correct comparison is: the sharpw theorem imposes fewer far-field
cancellations but slightly more fractional regularity. The ratio 330.8
is a quotient of the stated numerical tolerances in different norms;
it is not a uniform enlargement of the same residual ball. The finite
partial sums of (1), after normalization, already show why no universal
high-frequency comparison constant exists, even on smooth functions.

Verdict: REFUTED for the selected-space inclusion and for an unqualified
same-norm enlargement. CONFIRMED for the fewer-sector statement and the
fixed-exponent inclusion. No candidate certificate is affected: the
campaign's finite smooth candidate residuals have separately checked
membership and norm bounds.

## 3. Norm domination does not need a large constant

Let Y be any normed correction space continuously embedded in L2, with
||h||2<=C||h||Y and 0<C<infinity. If every exact correction obeys
||h||2>d, then a closed Y ball of radius r contains no such correction
whenever Cr<=d. This is direct substitution and does not require 1/C
to be large. Its usefulness depends on r and C, not on an extra
qualitative size hypothesis.

For the localized weight w=e^psi with inf psi=0, w>=1, hence C=1 for
Y=L2(w^2). Thus every exact correction to007 has ||h||Y>0.004769166867.
Section 2.7 of the report states this correctly; section 6's sentence
that NC-T-DIST does not apply to the localized route is false. The
repair is to retain the necessary radius and state that no independent
upper ceiling on that radius has been established. There is therefore
no exclusion of all future localized frameworks.

A decaying-weight space E_a, a>0, does not globally control L2 by a
positive constant. The unweighted distance cannot be transferred to
its ball by the preceding argument. It needs its own weighted probe
or a further embedding. This is the relevant distinction for DYADIC-Y.

Verdict: REFUTED for the localized exception in section 6; CONFIRMED for
the corrected radius statement already in section 2.7.

## 4. Two compressed statements that are valid with their source scope

The section 3.2(C2) formula is valid when G and B come from the three
parity blocks complementary to S1. The self-adjoint Hilbert-Schmidt
operator K reduces coordinate parity. Its total squared Hilbert-Schmidt
norm contains the full S1 block and every complementary compression as
disjoint nonnegative sums. Subtracting their traces bounds ||K|S1||op.
The report should say "complementary parity blocks" explicitly. A
compression inside S1 cannot be subtracted this way: K=P on a
one-dimensional subspace would give a spurious zero bound. The signed
S1 repair is instead

    sup spectrum(K|S1)<=sqrt(kappa2-T_other-T_S1+q^2),

where q>=0 and qG-B is positive semidefinite. This is a quadratic-form
upper bound, not generally an absolute operator norm bound. The cited
008 value uses this repaired signed formula, so its certificate stands.
Dependencies: ../parity_hs_budget/PROOF.md,
../parity_hs_angular/PROOF.md and ../signed_compression_budget/PROOF.md.

The section 6 graded H^(2+s) bound is also valid, not merely an L2
bound. With component radii r2,r1,r0 let n^2=r2^2+2r1^2+r0^2. The
Fourier identity (1+|xi|^2)^2=1+2|xi|^2+sum_ij xi_i^2 xi_j^2 and
omega>=1 give ||h||H^(2+s)<=n. Positivity of the common top margin
then yields n<50/(651 sqrt(28248))<25/54684. See
../graded_budget_audit/PROOF.md. The report's rounded 4.5717e-4 is
an upper ceiling. These statements are CONFIRMED within that scope.

## 5. Fixed radii and family ceilings must have distinct labels

Section 2.1 lists a fixed ball r alongside the larger optimized family
ceiling under the name "L2 correction budget". Both are valid upper
bounds, but they refer to different scopes. The fixed balls imply

    sharp:  ||h||2<=147/102400000 = 0.000001435546875,
    sharpw: ||h||2<=1351/1024000000 = 0.0000013193359375.

The values 3.0927e-6 and 2.8496e-6 in the table are the looser ceilings
for every positive-rate ball in each parameter family. Label them
"universal family ceiling" and optionally add the fixed-ball row.
The family ceilings are appropriate for the uniform exclusions; using
them is conservative. This is a scope clarification, not a refutation
of those exclusions. Likewise the A2 fixed ball r=2^-16 implies
||h||2<=2^-25, whereas 6.8626e-8 is its optimized family ceiling.

## Status and limitations

The new Fourier constructions and assembly corrections await a second
Opus review. They are complete informal arguments and require no
numerical integration. The finite-rank counterexample is exact algebra.
No new inverse, no existence theorem, and no global nonexistence result
is claimed. The unsigned/signed compression and graded statements here
are checks against already independently audited source proofs.

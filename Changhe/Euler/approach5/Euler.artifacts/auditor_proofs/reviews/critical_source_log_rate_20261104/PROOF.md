# Explicit logarithmic positive-source bound

Status: independently reconstructed and compared with the existing Theory Agent A agent;
verdicts are recorded separately in the auditor's ledger (AUDIT_LEDGER.md). This is a kinematic theorem with a conditional Euler
consequence. It does not prove the unrestricted rotating conjecture.

## 1. Exact claim and dependencies

Let U belong to C1(R3;R3), div U=0, q=tr((DU)^2) and q_+=max(q,0).
For 0<beta<1, L>0 assume

    E(R)=integral_(B_R)|U|^2,  E(R)/(L R^beta) -> 1.

Put m=2-beta, k_beta=beta(2-beta)(1-beta), and

    H_+(R)=integral_(B_R)|y|^m q_+(y)dy.

Then liminf H_+(R)/log R>=k_beta L. If in addition
E(R)=L R^beta+O(R^(beta-1)), then for some finite C and all
sufficiently large R,

    H_+(R)>=k_beta L log R-C.

Both conclusions hold about each fixed center a, with the same L,k_beta
but potentially different threshold and C. No boundedness or decay of
U or DU is required here. All source integrals over compact sets are
finite because both q and the weight are continuous on compact sets. The
condition m>1 will be used for convexity, not for this local finiteness.

The only Euler input later is the confirmed energy theorem A3053.
The separate LIT373 construction is not needed for this proof and is
not a source of the constant. No optimality of k_beta is asserted.

## 2. Compact test and both errors

Mollify U on compact sets. Divergence is preserved and the smooth identity
partial_i partial_j(U_i U_j)=partial_i U_j partial_j U_i passes to
distributions under local C1 convergence. Thus

    integral q psi=integral U^T D^2 psi U

for every compactly supported smooth psi. Only this compact identity is
used; there is no integration by parts at infinity.

Choose radial smooth cutoffs chi,eta between0 and1, with chi=1 on B1
and zero outside B2, and eta=0 on B1 and1 outside B2. Set
phi(y)=eta(y)|y|^m. This is smooth, nonnegative, zero near0 and at most
|y|^m. Its Hessian inside B2 may have either sign. For r>2 it equals

    D^2 phi=m r^(-beta)(I-beta e_r tensor e_r).

The tangential eigenvalues are m r^(-beta), and the radial eigenvalue is
m(1-beta)r^(-beta)>0. Consequently the quadratic form is at least
m(1-beta)r^(-beta)|U|^2 there.

For R>2 test against psi_R=phi chi(y/R). Write K1=sup|grad chi|,
K2=sup|D^2 chi|_op. The extra Hessian terms are supported in R<=r<=2R,
and their operator norm is at most

    C_chi,m R^(-beta),
    C_chi,m=2^m K2+2m 2^(m-1)K1.

Indeed phi<= (2R)^m and |grad phi|<=m(2R)^(m-1) on that annulus.
The two mixed gradient terms account for the factor2. The contribution
of the inner Hessian is bounded below by

    -C_U,  C_U=sup_(B2)|D^2 phi|_op E(2).

The main Hessian contribution outside B2 is nonnegative, including the
part in R<r<2R, so it may be discarded outside B_R. Since the test is
nonnegative and at most r^m, its signed source pairing is at most
H_+(2R). The compact identity therefore yields

    H_+(2R)>=m(1-beta) F_beta(R)-C_U
                         -C_chi,m R^(-beta)E(2R),       (1)
    F_beta(R)=integral_(2<|y|<R)|y|^(-beta)|U|^2.

The proof assigns no positive Hessian to the full compact test. The
inner and outer errors are different and both have been retained.

## 3. The logarithmic coefficient

The actual E is continuously differentiable for positive R. Finite
interval integration by parts, without differentiating an asymptotic
formula, gives

    F_beta(R)=R^(-beta)E(R)-2^(-beta)E(2)
                +beta integral_2^R t^(-beta-1)E(t)dt.   (2)

Write E(t)=L t^beta(1+epsilon(t)), epsilon(t)->0. The logarithmic
average integral_2^R epsilon(t)dt/t is o(log R): split it at a fixed
large radius beyond which |epsilon|<=delta and then let delta tend
to zero. Thus F_beta(R)=beta L log R+o(log R). Also
R^(-beta)E(2R) is bounded. Equation(1), divided by log(2R), proves
liminf H_+(2R)/log(2R)>=m(1-beta)beta L. Since R is any sufficiently
large real number, this proves the claim at all large radii, not just
a subsequence.

Under the stronger remainder write E(t)=L t^beta+d(t), where
|d(t)|<=C t^(beta-1) for large t. The tail integral of
|d(t)|t^(-beta-1) is bounded by C integral_R^infinity t^(-2)dt,
so it is O(1/R). Its full integral from2 has a finite limit. The
endpoint d(R)R^(-beta) is O(1/R) as well. Hence exactly

    F_beta(R)=beta L log R+C0+O(1/R).

Inserting this into(1), using the bounded outer error and replacing
2R by an arbitrary large radius, proves the additive bound. A mere
ratio limit was not used to claim a bounded additive remainder.

## 4. Fixed centers

For fixed a and R>|a| the inclusions of balls give

    E(R-|a|)<=E_a(R)<=E(R+|a|).

They preserve the ratio limit with the same L. Under the stronger
remainder, expansion of the fixed shifts gives
L(R+-|a|)^beta=L R^beta+O_a(R^(beta-1)), and both bounding energies
have that same order of error. The squeeze therefore preserves the
stronger remainder at each center. Apply Sections2-3 to the translated
field U(a+.) and the translated source q(a+.). This uses translation
invariance of the double-divergence identity, not of the Euler profile
equation. All constants except L and k_beta may depend on a.

## 5. Conditional Euler consequence and remaining scope

Suppose U is C1 and bounded, P is C1, U(R.) tends to zero in
distributions, and

    (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0,
    div U=0,  J(y1,y2,y3)=(-y2,y1,0),  2/5<c<1/2.

For a nonzero U, A3053 supplies the stronger energy law with L>0 and
beta=5-2/c. Thus m=2/c-3 and

    k_beta=(5-2/c)(2/c-3)(2/c-4)>0.

It follows that the integral of (1+|y-a|)^(2/c-3) q_+ is infinite
for every fixed a. Conversely finiteness at even one a forces U=0,
and then grad P=0 so P is constant. The pointwise inequality
q_+<=|DU|_F^2 gives the same sufficient condition with the squared
Frobenius gradient. The coefficient is independent of every finite
omega; the theorem imposes no symmetry on U or P.

Uniform decay implies boundedness and the stated weak-dilation premise,
but it does not supply the extra weighted integrability in this proof.
Neither endpoint, optimal coefficient, novelty, automatic integrability
nor unrestricted nonexistence is established. The LIT373 quadratic
cumulative-moment lower bound is a separate statement; the present
logarithmic bound does not imply it by differentiation.

## 6. Evidence and independent comparison boundary

All five sections of source588f0c78, all33manual checks, the formal-source
note and reading record were read and captured in verification. The
argument above was reconstructed without mathematical computation or
formal builds. Its examples are not dependencies. The complete existing Theory Agent A comparison A131 has now been read and retained.
Its six section checks agree with Sections1-5; its analytical refinements
are checked below. Existing configured model file collaboration was used;
actual provider execution remains independently unattested. The source
author's own reading record is not substituted for independent comparison.

## 7. Removing the inner cutoff at this regularity

The function f(y)=|y|^m is C1, convex, and belongs to W^(2,1) on every
compact set. Its pointwise Hessian off0 is the formula in Section2 and
is O(|y|^(-beta)). It is locally integrable because beta<1<3. That is
also the distributional Hessian: integration by parts outside B_epsilon
has boundary terms bounded by C epsilon^(m+1), which vanish. There is
no extra measure at the origin.

Consequently f chi_R can be used as a test. Mollify this compact W^(2,1)
function; the functions converge uniformly and their Hessians in local
L1. On a common compact support q and U are bounded, so both sides of
the compact distribution identity converge. Keeping the same outer
error as Section2 gives

    H_+(2R)>=m(1-beta) integral_(B_R) r^(-beta)|U|^2
                  -C_chi,m R^(-beta)E(2R).

There is no inner error. The weighted energy is finite at0 because
E(t)=O(t^3). Its exact integration-by-parts identity is

    integral_(B_R) r^(-beta)|U|^2
       =R^(-beta)E(R)+beta integral_0^R t^(-beta-1)E(t)dt.

It has the same logarithmic coefficient as Section3. This verifies X1,
including its regularity and origin boundary terms.

## 8. Positive part after spherical averaging and signed pairing

Let Q_a(r)=integral_(S2)q(a+r theta)dtheta, using unnormalized surface
measure. Since every cutoff above is radial and nonnegative, Fubini
bounds its signed source pairing by

    H^Q_a(2R)=integral_0^(2R) r^(4-beta)[Q_a(r)]_+dr.

Thus the complete liminf and additive lower bounds hold for H^Q_a,
with the same k_beta L. This is potentially smaller than the pointwise
q_+ moment; no strict separation within the full-profile class is claimed.
For a full profile the additional sufficient condition can therefore be
weakened to finite integral_1^infinity r^(2/c-1)[Q_a(r)]_+dr.

For the actual pressure mean
Pbar_a(r)=(4pi)^(-1)integral_(S2)P(a+r theta)dtheta, the Poisson equation
gives (r^2 Pbar_a')'=-r^2 Q_a/(4pi). The last integral is exactly

    4pi integral_1^infinity r^(2/c-3)
                         [-(r^2 Pbar_a')']_+dr.

This uses the actual pressure and no arbitrary normalization. Constants
in P do not matter. The regularity follows from the distributional
Poisson equation with continuous q and the spherical flux identity.

There is also a two-sided statement for the compact signed pairing
S(R)=integral q(y)|y|^m chi(y/R)dy, under the stronger energy remainder.
The identity and the same annular error give

    S(R)=m integral chi_R r^(-beta)(|U|^2-beta|U.e_r|^2)+O(1).

The quadratic expression lies between(1-beta)|U|^2 and |U|^2. The
weighted energies over B_R and B_(2R) are both beta L log R+O(1).
Hence k_beta L log R-C<=S(R)<=m beta L log R+C.
For the confirmed exact-energy radial swirl U=f0(r)Jy, U.e_r=0 and
the upper coefficient m beta L is attained. Its exterior spherical
source is Q(r)=beta(2-beta)L r^(beta-5), so
H^Q(R)=beta(2-beta)L log R+O(1). These computations verify X2-X3.
They assert no optimal lower coefficient across all divergence-free fields.

## 9. Quantitative comparison and limits of the logarithmic conclusion

The numerical comparison in A131 is unnecessary for the coefficient
comparison. For the radial cutoff of LIT373 let Cchi=4(K1+K2), where
K1>=1 by the mean value theorem on a radial line between radii1and2.
Its constants obey

    K=max(2,(2^(beta+2) Cchi)^(1/(1-beta))),
    c_beta=1/[2(2K)^beta].

Therefore with t=beta/(1-beta)>0,

    k_beta/(beta c_beta)
       >=2(2-beta)(1-beta) 2^(5beta/(1-beta))
        =2(t+2)/(t+1)^2 times 2^(5t)>4.

For the strict last inequality, the logarithmic derivative of the last
expression is 1/(t+2)-2/(t+1)+5log2>0, since log2>1/2; its value at0
is4. This is an analytic verification for the whole range, not evidence
from a finite grid.

A logarithmic lower bound alone does not imply LIT373's all-radius
power lower bound. To see the logical distinction for increasing
functions, put a jump k(2j+1) in H at R_j=exp(j^2), j=0,1,2,... . Then
H(R)>=k log R for R>=1. Define M(R)=integral_[1,R] t^beta dH(t), so
H(R)=integral_[1,R] t^(-beta)dM(t). Immediately before R_(n+1),
M(R)/R^beta<=C_beta(n+1)exp(-beta(2n+1)), which tends to0.
The estimate follows by bounding the earlier exponentials by a geometric
series. This is a monotone-function countertest, not a field construction.
Thus no derivative of a lower bound may be used to identify these two
claims.

All three sections of A131's comparison, including X1-X3, have been
checked independently. Its local-finiteness wording precision is adopted.
Diagnostic scripts, their output counts and model-provider execution are
not certified. Neither endpoint, automatic source integrability, an
optimal coefficient, nor the unrestricted rotating conjecture is settled.

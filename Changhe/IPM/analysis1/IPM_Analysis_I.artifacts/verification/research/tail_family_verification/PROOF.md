# Tail uniqueness, conditional kernel families, and limits of parameter inference

Date: 2026-10-20. Status: conditional mathematical claims independently checked and accepted in an actual Opus 5.5 follow-up on 2026-10-20 at17:43:35 UTC. The separate evidence/verdict.json pins the proof, source snapshot and review records. This note audits the lead's tail_family.md snapshot in evidence/. It supplies corrected conditional statements. No exact IPM solution, full inverse, or family has been constructed in this run.

## Spaces, notation, and the tail uniqueness theorem

Fix R>1 and gamma_E in R. Let H_E be L^2({r>R},r^(-2(gamma_E+1))dX), using the full angular circle. Let chi(r) be a smooth cutoff equal to1 for r>R and vanishing near0. Let Tau be a real Banach space continuously embedded in L^2(S^1). Angular profiles may obey even-x, odd-y parity. A valid infinite-dimensional example is the closed subspace of C^m(S^1) with this parity that vanishes on a fixed open neighborhood of the four coordinate-axis angles. If prescribed profiles do not vanish in that neighborhood, take their finite-dimensional span together with such a subspace and choose a Banach direct sum after removing any intersection.

For nonzero Phi in L^2(S^1), r^q Phi belongs to H_E if and only if q<gamma_E. In fact its squared norm is ||Phi||_2^2 times integral_R^infinity r^(2(q-gamma_E)-1)dr. At q=gamma_E this is logarithmically divergent. Thus a nonzero r^k Phi, with k>=gamma_E, cannot be absorbed into an H_E remainder.

Suppose

chi r^(k_1) Phi_1 + g_1 = chi r^(k_2) Phi_2 + g_2,

g_i in H_E, nonzero Phi_i in L^2(S^1), and k_i>=gamma_E. Then k_1=k_2 and Phi_1=Phi_2. If k_1>k_2, the angular norm of the difference for large r is at least r^(k_1)||Phi_1||_2/2, by the reverse triangle inequality. The radial integral diverges, a contradiction. Equal exponents reduce directly to the preceding membership test.

For the logarithmic version, fix k>=gamma_E and nonzero Psi in L^2. If

chi r^k [(d_1-d_2)log(r)Psi+Phi_1-Phi_2] belongs to H_E,

then d_1=d_2 and Phi_1=Phi_2. A nonzero log coefficient makes the angular norm at least r^k[|d_1-d_2| ||Psi||_2 log r-C] for large r. This diverges in H_E even at equality k=gamma_E. With that coefficient zero, apply the power test. This proves the lead's Lemma T, including its stated strict-exponent range and a harmless endpoint extension.

## Exact leading forcing identity and its mapping premise

Write rho=chi r^k Phi+g and c_l=(1+c[rho])/3, where c[rho]=psi_xy(0) is the unscaled strain. Direct differentiation, with Phi independent of r, gives the exact identity

F(rho)=(c_l k-1)chi r^k Phi+R(rho),
R(rho)=c_l r chi'(r)r^k Phi+(c_l X dot grad-1)g+U[rho] dot grad rho.

Thus the displayed identity in the lead's hypothesis S1 is algebraically correct. For it to be an identity in the asserted forcing splitting, all three terms of R must belong to Y_-. This is a mapping hypothesis. Compact support alone is not enough for an arbitrary Y_- with singular edge weights; a pointwise O(r^(2k-1)) assertion alone is not an edge or derivative norm estimate. In particular neither weighted L^2 control of g alone nor an angular L^2 profile alone proves this premise. If Y_- direct-sum span(chi r^k Phi) is the actual target splitting and Phi is nonzero, then F(rho)=0 forces c_l k=1. Directness is required here; it can be proved by a suitable tail nonmembership condition for Y_- or included in the specified splitting.

For the tail increment T(Psi)=chi r^k Psi at an exact base solution with c_l k=1, differentiating F gives

L T(Psi)=c_l r chi' r^k Psi+U[rho] dot grad T(Psi)+U[T(Psi)] dot grad rho
 +(c[T(Psi)]/3) X dot grad rho.

If rho=chi r^k Phi_*+g, subtracting (k c[T(Psi)]/3)chi r^k Phi_* leaves the first three terms and the rank-one cutoff/remainder terms (c[T(Psi)]/3)[r chi' r^k Phi_*+X dot grad g]. Under their Y_- membership this proves the scalar in S2 is s_Psi=k c[T(Psi)]/3. It does not establish that membership or its boundedness. These formulas are purely product-rule identities and explicitly separate their algebra from the unproved IPM mapping assumptions.

## A precise conditional kernel theorem

Let X and Y be Banach spaces. Assume that restriction to the exterior is a continuous map X -> H_E; X need not inject into H_E, since compactly supported functions may restrict to zero. Fix k_* in (gamma_E,1), nonzero Phi_* in Tau, and nonzero Theta_1 in Tau. Put

T(Phi)=chi r^(k_*)Phi,    Z_*=chi r^(k_*)log(r)Phi_*.

Regard E_+=X direct-sum T(Tau) direct-sum span(Z_*) as a Banach algebraic extension, with the corresponding sum norm. The sum is direct by tail uniqueness. Suppose a linear map L is defined on E_+ with values in Y. Assume:

1. T(Phi) maps by L to Y continuously and linearly as Phi varies in Tau.
2. A(g,d,t):=L[g+d Z_*+t T(Theta_1)] is a bounded bijection X x R^2 -> Y.

The target Y can be an already specified forcing remainder plus its one-dimensional leading tail component. Its norm and the directness of that target splitting are part of these assumptions. A bare algebraic bijection does not replace assumption2. By the Banach inverse theorem A^-1 is bounded.

Define

(g_Phi,d_Phi,t_Phi)=-A^-1 L T(Phi),
kappa(Phi)=T(Phi)+g_Phi+d_Phi Z_*+t_Phi T(Theta_1).

Then kappa is continuous and linear, L kappa(Phi)=0, and these correcting coordinates are unique. If kappa(Phi)=0, the logarithmic tail uniqueness theorem gives d_Phi=0 and Phi+t_Phi Theta_1=0. Conversely kappa(t Theta_1)=0, since the unique correcting coordinates are (0,0,-t). Consequently kappa induces a continuous injective linear map from Tau/span(Theta_1) into ker L.

It is also onto ker L in E_+. Indeed write any kernel element as g+T(Phi)+d Z_*. The triple (g,d,0) solves the same correction equation for Phi, so uniqueness makes that element kappa(Phi). Thus the kernel is algebraically isomorphic to Tau/span(Theta_1), and is infinite-dimensional when Tau is. No claim about an IPM kernel follows until these mapping and inverse hypotheses are established in actual spaces.

The notation E_+ describes a normed tail extension. Its embedding in a pointwise P_2-type growth class needs extra assumptions. Sufficient ones are Tau continuously embedded in C^1(S^1), and X continuously embedded in the growth norm G_gamma defined below for every relevant gamma>k_*. Weighted L^2 membership alone does not imply these pointwise bounds or the local P_2 admissibility conditions.

## Scaling identification, with its domain premise

For this note only, c denotes the unscaled strain psi_xy(0); the prompt's rank-one scaling functional is c/3. Assume this c is a bounded linear functional on E_+ whenever it is differentiated below. For canonical IPM, write c[rho]=psi_xy(0), c_l[rho]=(1+c[rho])/3 and F(rho)=(c_l[rho]X+U[rho]) dot grad rho-rho. The exact scaling is S_a rho(X)=a rho(X/a), a>0. Under the differentiability and canonical-law hypotheses proved in ../scaling_index/PROOF.md,

F(S_a rho)=S_a F(rho),   c[S_a rho]=c[rho],
K=rho-X dot grad rho,   L K=0 at an exact solution,   c[K]=0.

Suppose, in addition to the kernel theorem, that the scaling curve is differentiable in the realization needed to apply L and c, and that

K-(1-k_*)T(Phi_*) belongs to X.

Then uniqueness of the kernel correction implies

K=kappa((1-k_*)Phi_*),   d_((1-k_*)Phi_*)=0.

Indeed K itself has the permitted correction coordinates (K-(1-k_*)T(Phi_*),0,0). As k_*<1, linearity gives d_(Phi_*)=0. The scaling direction changes tail amplitude and leaves its exponent and c_l fixed. This is conditional on membership and differentiability. Bare center factorization and P_2 regularity do not guarantee them, as the explicit oscillatory-factor counterexample in scaling_index shows. The present F- ansatz has no fixed J constraint, so the nonzero scaling trace J(K)=-2J(rho) is consistent with the statement.

## Conditional nonlinear family and topology

Suppose an independently justified nonlinear argument constructs exact solutions

rho_Theta=chi r^(k(Theta))[Theta+t(Theta)Theta_1]+g_Theta,

for Theta in an open ball U in Tau. Assume g_Theta in X, gamma_E<k(Theta)<1, and the displayed tail profile is nonzero. At the base parameter assume k(Theta_0)=k_* and Phi_*=Theta_0+t(Theta_0)Theta_1, identifying this family with the preceding kernel theorem. Statements asserting an infinite-dimensional family or non-isolation assume Tau is infinite-dimensional. Suppose the PDE target splitting proves c_l[rho_Theta]k(Theta)=1. These are existence and mapping hypotheses, not conclusions from small sampled residuals.

Choose a closed complement Z of span(Theta_1) in Tau; it exists because a continuous functional nonzero on Theta_1 gives a bounded rank-one projection. On the affine slice (Theta_0+Z) intersect U, the map Theta -> rho_Theta is injective. Equality of two solutions gives equal exponents and equal full angular profiles by tail uniqueness. Their parameter difference lies in both Z and span(Theta_1), hence is zero. Uniqueness for a fixed Theta is a separate property of the asserted nonlinear construction and its specified ball.

For pointwise non-isolation, define

||f||_(G_gamma)=sup_X (1+r)^(-gamma)[|f(X)|+(1+r)|grad f(X)|].

Assume Tau embeds continuously into C^1(S^1), X embeds continuously into G_gamma, and Theta -> (g_Theta,k(Theta),t(Theta)) is continuous in X x R^2. Fix gamma>k(Theta_0), with gamma<1 if a sublinear class is desired. Shrink U so that k(Theta)<=gamma-delta for some delta>0. On r>R,

|r^(k_1)-r^(k_2)|<=|k_1-k_2|r^(max(k_1,k_2))log r.

The same differentiation in r gives a bound by a constant times |k_1-k_2|r^(max k-1)(1+log r), and the angular derivative is controlled by the C^1 profile norm. Since sup_(r>R) r^(-delta)(1+log r)<infinity, these estimates imply continuity of the tail map in G_gamma. Compact cutoff terms are smooth and satisfy the same continuity. The remainder converges by its X embedding. Thus rho_Theta -> rho_Theta0 in G_gamma. Any sequence of distinct parameters on the affine slice tending to Theta_0 yields distinct exact solutions tending to the base solution.

The relevant exponent is the exact base exponent k(Theta_0), not an approximate trial exponent. Continuity into the tuple space X x R^2 alone, with Tau embedded only into L^2, does not give this C^1 weighted topology. Nor does this argument prove non-isolation in every topology one might call P_2-type.

## Center normalization and a correct amplitude slice

Assume X consists of functions in L^2_loc, and its remainders belong to H_E on the exterior. Then every S_a g has an H_E exterior restriction: change variables on r>max(R,aR), and use local L^2 integrability on the remaining bounded annulus. The difference chi(r/a)-chi(r) is compactly supported away from0, so its tail term also lies in H_E. These facts justify applying tail uniqueness to a scaled solution.

Assume J(rho_Theta)>0 and the stated scaling law J(S_a rho)=a^-2 J(rho). Then N(rho)=S_(sqrt(J(rho)))rho has J=1. If N(rho_Theta)=N(rho_Theta'), the unnormalized solutions are related by a positive scaling. Tail uniqueness therefore gives equal exponents and

Theta'+t(Theta')Theta_1 = a^(1-k) [Theta+t(Theta)Theta_1]

for some a>0. Thus their classes in Tau/span(Theta_1) are positive multiples. This implication is valid without assuming that the constructed family is invariant under scaling.

An injective normalized subfamily can be obtained by one more affine condition, without asserting a quotient parametrization. Let pi:Tau -> Tau/span(Theta_1), and suppose pi(Theta_0)!=0. Choose a continuous functional lambda on this quotient with lambda(pi(Theta_0))=1. Restrict the previous gauge slice further by lambda(pi(Theta))=1. If two normalized solutions on this slice coincide, applying lambda to the preceding identity gives a^(1-k)=1, hence a=1 because k<1. The full profiles and the gauge slice then give Theta=Theta'. The parameter slice has codimension two in Tau and is still infinite-dimensional. To deduce convergence of these normalized solutions one additionally needs continuity of J on the family and continuity of scaling in the chosen topology.

In contrast, identifying all positive profile multiples as the same normalized solution requires the reverse implication: solutions assigned to collinear tail parameters must be exact rescalings. Covariance produces a rescaled solution, but fixed-parameter uniqueness in a possibly different local ball does not by itself put that solution into the ball. A scaling-invariant construction, uniqueness on overlapping neighborhoods containing both solutions, or an equivalent compatibility premise would supply the missing implication. The original quotient-parametrization sentence has not established it.

## What the exponent derivative does and does not decide

Suppose the constructed family is differentiable at Theta_0 in the realization needed to linearize F and c; a C^1 curve of inputs and mere continuity of outputs do not suffice. Absorb derivatives of fixed far corrections into the X component. Then for the input tangent Phi,

D rho[Phi]=kappa(Phi),
D c_l[Phi]=-k_*^(-2) D k[Phi]=c[kappa(Phi)]/3,
ell(Phi):=D k[Phi]=-pi_k A^-1 L T(Phi).

Here pi_k(g,d,t)=d is the scalar coordinate multiplying Z_*. The first identity follows by differentiating the exact equation and applying uniqueness in the kernel correction theorem. The second follows both from c_l=1/k and from the affine formula for c_l. The last follows directly from the definition of the correcting triple. Thus ell is a continuous linear functional, ell(Theta_1)=0, and ell(Phi_*)=0 under the scaling hypotheses.

If ell is nonzero at a base solution, there is a direction with nonzero first derivative, so k and c_l vary in every sufficiently small neighborhood along that differentiable curve. If ell=0 at that single solution, only first-order stationarity follows. The scalar counterexample k(t)=k_*+t^2 on a small interval satisfies k'(0)=0 but k is not constant in any neighborhood. Its reciprocal c_l(t) is also nonconstant. This refutes the statement that local constancy is equivalent to ell=0 at one solution. It does not refute a family of IPM solutions, and it does not claim such a quadratic curve exists for IPM.

A valid strengthened statement is: if k is C^1 on a connected open ball and Dk is zero at every point, then k is constant there. On each line segment, the one-variable fundamental theorem of calculus gives k(v)-k(u)=integral_0^1 Dk(u+t(v-u))[v-u]dt=0. Connected open sets are locally polygonally connected, so the same conclusion extends through overlapping balls. First-order numerical solves at one point cannot replace this neighborhood hypothesis.

## Explicit checks of two topology pitfalls

The set of C^m profiles that vanish on some neighborhood of the axes, where the neighborhood may depend on the profile, is not closed in C^m. Take a smooth parity profile flat at every axis but nonzero arbitrarily close to one, such as a signed periodic construction from exp(-1/theta^2) near an axis. Multiplying it by smooth cutoffs that vanish when the angular distance to an axis is below1/n gives profiles in the proposed set converging to the original profile in C^m. Flatness controls every cutoff-derivative term. The limit belongs to C^m but not to that set. Hence the proposed example with varying neighborhoods is not a Banach space in the C^m norm. A fixed neighborhood repairs it.

Weighted L^2 does not imply a pointwise power growth bound. Choose disjoint disks centered at radius R_n=2^n, amplitudes A_n=R_n^(gamma+1), and radii d_n=2^(-n^2) times a sufficiently small fixed factor. Let h_n=A_n phi((X-X_n)/d_n), with nonzero smooth phi supported in the unit disk. For large n the weighted squared integral is at most C A_n^2 d_n^2 R_n^(-2(gamma_E+1)), a summable sequence. Yet sup (1+r)^(-gamma)|h_n| grows at least like R_n on the disk centers. The locally finite sum is smooth and in H_E but has unbounded G_gamma norm. Reflected copies with appropriate signs impose the IPM parity without changing these estimates. This disproves the use of weighted L^2 alone to infer the growth assertion for E_+; stronger norms may of course supply it.

## Verdict and scope

The tail and log uniqueness proof and the kernel quotient construction are confirmed under the explicit bounded inverse and mapping hypotheses above. Nonlinear injectivity on a gauge slice is confirmed conditional on the existence assumptions. Pointwise non-isolation needs the additional topology and exact-exponent conditions; scaling-normalized injectivity is proved on a codimension-two slice. The at-point derivative/local-constancy equivalence is refuted, and the unqualified quotient parametrization and pointwise-growth inference are not established by the supplied assumptions. All actual PDE mapping, inverse, closure, differentiability, and global admissibility obligations remain open.

# Four coverage-proof checkpoints and their exact scopes

Status: four local verification checks CONFIRMED after reading the report passages, both complete prior source proofs, and Theory Agent A Note A78. This is not a fresh proof of every theorem in Section 2C and certifies no unread external source.

## 1. Reading boundary and dependencies

The report is the pinned 8155336d snapshot, whose passages are retained in the team records. The stable-curve source is auditor_proofs/proofs/pesin_zero_capture/PROOF.md (A201), and the selection source is auditor_proofs/proofs/original_curve_measure/PROOF.md (A307), both relative to this agent root. Both were read completely. The existing configured model Theory Agent A comparison is retained as in the team records; actual provider runtime is independently unattested.

The following checks use the already stated Oseledets/Pesin inputs and elementary ODE, recurrence and measure facts. Their external-source provenance has not been re-audited here. No computation or formal build is used.

## 2. The cutoff contributes no relevant positive-exponent measure

Let Q be the closed trapping ball in the report. Let B be the smooth complete carrier with B(y).y>=b0|y|^2 outside Q, b0>0, and let rho be a smooth nonnegative radial cutoff, nonincreasing with radius, equal to one near Q and zero outside a larger ball. Consider the cutoff backward field -rho B on the one-point compactification.

For rho(y)>0 outside Q, the radius decreases at rate at least b0 rho(y) times the radius. As the radius decreases, rho does not decrease. Thus the trajectory enters Q in finite time. The strict radial inequality and continuity near its boundary put the trajectory in the interior in finite additional time and prevent a later return to the outside region. Such a point is not recurrent. Poincare recurrence for an invariant probability therefore gives zero measure to the positive-cutoff transition region, including the collar at the boundary of Q.

At every point where rho=0, nonnegativity and differentiability imply D rho=0. Hence D(-rho B)=0 there. The point is fixed, the derivative of the time-one map is the identity, and all Lyapunov exponents are zero. The added point has the same property because the field vanishes in a neighborhood of it. Consequently an ergodic invariant probability with a positive exponent lies in Q, and invariance puts its support in the maximal invariant subset K. All plaques used near K can be chosen inside the open region where rho=1 and the cutoff map is the original time-one map. This verifies report checkpoint 3 without a recurrence assumption on the transition dynamics.

## 3. Stable-curve capture is genuinely pointwise

Let Bp be a complete C2 carrier with backward flow Theta, F=Theta_1, and let Wt be C1 with the real-time law

    Wt(Theta_t x)=exp(kp t)DTheta_t(x)Wt(x), kp>0.

Fix a two-sided regular q with simple exponents chi>0, 0, -lambda<0, Wt(F^n q)=0 for every integer n, and compact control of the small stable plaques and their forward iterates. The adapted two-sided Lyapunov coordinates satisfy

    ||L_n||<=C, ||L_n^-1||<=C_epsilon exp(epsilon n),
    m(L_(n+1)^-1 DF(F^n q)L_n)>=exp(-lambda-epsilon).

For a on a small stable plaque, |F^n a-F^n q|<=C exp((-lambda+epsilon)n). Since DF is Lipschitz on the compact region, the corresponding adapted derivative at F^n a differs by at most C exp((-lambda+2epsilon)n). Take 2epsilon<lambda. The 1-Lipschitz property of the conorm then gives a lower bound exp(-lambda-2epsilon) for all large n. Multiplication and the endpoint coordinate comparison imply

    |DF^n(a)v|>=c exp((-lambda-3epsilon)n)|v|.

On the other hand, C1 regularity of Wt and its zero at F^n q give |Wt(F^n a)|<=C exp((-lambda+epsilon)n). Combine with transport and choose 4epsilon<kp to obtain

    |Wt(a)|<=C exp((-kp+4epsilon)n) ->0.

So Wt vanishes on the local stable plaque, on its entire global stable curve by invertibility, and on every finite flow translate by the real-time law. Nothing in this argument requires averaging over an ergodic component once q is fixed. The zero exponent need not be identified with the flow direction for this particular conclusion. The positive-volume corollary in the old source is not used in this report checkpoint. This verifies checkpoint 10 at the exact pointwise scope of Lemma 19.

## 4. The existential witness selects whole parents

Use the nested finite interval partitions, good atoms and sets E_n of the report. A good atom has a large image and at least one hyperbolic witness. It need not have every point as a witness. At depth ell and window M, retain a whole parent P precisely when some y in P intersect E_n has a good descendant at depth ell+i with 0<=i<=M and ell+i<=n. Keep the full original conditional mass of E_n on P.

Every y in E_n has at least beta n good depths, so window zero has mass at least beta-1/n: only the endpoint depth n can be omitted from the average over 0<=ell<n. Enlarging the window retains every previously chosen parent with the same weight, hence the measures increase. If a depth-ell parent with ell>=1 is chosen at window M, its ancestor at ell-1 is chosen at window M+1, using the same y and the same good descendant. This holds for every sampled point of the chosen parent, not just the existential witness. It gives the measure inequality

    g_* mu_n^(M+1)>=mu_n^M minus the time-zero error,

where the error has mass at most 1/n. Passing first to the common n-subsequence and then to increasing M gives invariance by equality of total masses. This is exactly the A307 source rule and verifies checkpoint 13. The narrower variant requiring y itself to be a hyperbolic witness also works, but is not needed to justify the stated rule.

## 5. Componentwise exceptions remain null without a common gap

Let the components E of the relevant vortical open set each have the theorem's required spectral gap, with constants and selected parameters allowed to depend on E. An open subset of R3 has at most countably many components: choose a rational point in a small ball inside each component, with distinct points for disjoint components. A null exceptional set N_E in each E therefore has null union. When a time map must pull back an exception, a smooth flow diffeomorphism is locally Lipschitz on a countable compact exhaustion and preserves null sets. A further countable union over integer times is still null.

No estimate uniform in E and no strict gap for sup_E of the component exponents is needed for this measure-theoretic step. The claim presupposes that each component theorem has been established with its own hypotheses; it does not prove those hypotheses from decay. This verifies checkpoint 27.

## 6. Editorial points and limits

The report still presents the four checkpoints above as instructions to check. Their outcomes may now be recorded with this audit. Two other suggestions in Note A78 are correct: the shift identity in Lemma 29 is applied at every point with bounded forward orbit, including points outside Q, by choosing a compact neighborhood of that particular orbit; no uniform time over a neighborhood of the initial point is needed. The dependency list should include dominated convergence, second countability and the use of an unstable plaque in Lemma 27. These are documentation clarifications, not missing mathematical steps in the displayed arguments.

The report's coverage theorem and global helicity-sign theorem retain all their existing regularity, dynamical and sign hypotheses. These four checks do not prove the unrestricted arbitrary-helicity conjecture, upgrade the finite-regularity cases, or audit the whole external literature.

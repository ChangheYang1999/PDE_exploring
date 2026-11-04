# Expanded selection windows without phase domination

## 1. Exact assumptions and conclusions

Let D be a compact embedded C1 interval in a compact smooth Riemannian manifold M, with normalized arclength lambda. Let g be a C1 diffeomorphism of M. For each ell>=0 let P^ell be a finite partition of D into intervals, modulo lambda-null boundaries, with P^(ell+1) refining P^ell. Assume the interleaved family hypotheses of the preceding noncollapse lemma: P^(ell-1) refines to Q^ell and then P^ell; every Q^ell family has at most A0 members of P^ell; each geometric family has total g^ell-image length at least v0>0 and arclength Jacobian distortion at most D1.

For each n let E_n be measurable with m_n=lambda(E_n)>0, eta_n=lambda|E_n/m_n and L_n=log(1/m_n)=o(n). A specified collection of whole P^ell atoms is called BG, possibly depending on n. Each BG atom belongs to a geometric Q^ell family. Let W_n be a measurable witness set; it need not equal E_n. Define S_(n,ell)^M to consist of all P in P^ell for which there are y in P intersect W_n and 0<=i<=M such that the P^(ell+i) atom containing y is BG. All selections and witnesses are taken modulo the fixed null boundaries. Future times may be capped at n; this only decreases a selection.

For each selected P use the same C1 parametrization gamma_(ell,P) of g^ell(P), independently of M. Also use the same conditional probability rho_(n,ell,P) that represents the image of eta_n|P/eta_n(P). Ignore atoms with eta_n(P)=0. Put

    p_n^M = (1/n) sum_(0<=ell<n) sum_(P in S_(n,ell)^M)
                            eta_n(P) delta_(gamma_(ell,P),rho_(n,ell,P)).

For every fixed M assume these parametrizations belong to a compact C1 class C_M, with C_M contained in C_(M+1), and satisfy the distortion and descendant-diameter assumptions of the entropy absolute-continuity lemma. Length means parametrized arclength; for the original embedded images it equals their ordinary image length.

Then, along a common subsequence, p_n^M converges for every fixed M. The associated joint curve-and-point limits theta^M increase with M, have mass at most one, and have no constant curves. They are absolutely continuous along their curves. Their increasing limit theta has the same properties, on the countable union of the C_M. Its ambient projection mu is g-invariant. If the total mass selected at M=0 has a positive lower limit beta, then beta<=mu(M)<=1.

These conclusions do not require an estimate comparing mu^M with finitely many translates of mu^0. Such an estimate does not follow from the displayed selection rule alone.

## 2. The finite selection counterexample

Take g=Id, D=[0,1], lambda equal to Lebesgue measure and E_2=W_2=D. Let P^0={D} and P^1 consist of the left and right halves. Only the left atom at time 1 is BG. No atom at time 0 is BG. For n=2 the ambient measures are

    mu_2^0 = (1/2) lambda|[0,1/2],
    mu_2^1 = (1/2) (lambda + lambda|[0,1/2]).

The second formula includes all of D at time 0 because that parent contains a future BG witness. Both forward and backward phase images are identical because g=Id. Thus

    mu_2^1 <= mu_2^0 + (g^(-1))_*mu_2^0

is false: its left side assigns mass 1/4 to the right half and its right side assigns zero. This refutes a claimed finite-measure inequality obtained directly from the selection sums. It does not refute a theorem that assumes positive expansion and additional geometric estimates, or independently establishes an asymptotic domination by another argument.

## 3. Noncollapse for every fixed M

Set

    K_M = max(1, max_(1<=i<=M) sup_(z in M) ||Dg^i(z)||),

with K_0=1. This is finite by compactness. Suppose P at time ell has a witness at ell+i with i>=1. Let F be the geometric family containing the BG descendant at that future time. Interleaving puts all of F in one P^(ell+i-1) atom. That atom contains y, hence is contained in P by nesting. Therefore

    v0 <= length(g^(ell+i)(F))
       <= K_M length(g^ell(F))
       <= K_M length(g^ell(P)).                              (1)

Consequently a selected image of length less than v0/K_M can only have an i=0 witness. Since BG status is constant on each atom, it is selected at M=0. The weights and parametrizations agree. If q_n^M denotes the curve marginal, then for 0<h<v0/K_M,

    q_n^M{length<h} <= q_n^0{length<h}
      <= D1 A0 h/v0 + sqrt(L_n/(2n)) + 1/n.                  (2)

The second inequality is the interleaved-family entropy lemma. If a convention changes at the last M indices, an additional M/n bound suffices instead; it has no effect on the conclusion.

Compactness and a diagonal extraction give q^M. Length is C1-continuous, so its strict sublevel sets are open. Portmanteau and (2) give

    q^M{length<h} <= D1 A0 h/v0,  0<h<v0/K_M.

Let h decrease to zero. This proves q^M{length=0}=0 for each fixed M. No positive lower bound for every individual BG chart is asserted.

## 4. Increasing limits and absolute continuity

All p_n^M can be regarded as measures on the same C1 curve space times parameter probabilities, even though their compact supports grow with M. Because the selections are nested and the terms for a given atom are unchanged,

    p_n^M <= p_n^(M+1).

Choose a diagonal subsequence with limits p^M. For every nonnegative bounded continuous test the same inequality passes to the limit; hence p^M<=p^(M+1). The joint image map is

    (gamma,rho) -> delta_gamma tensor gamma_*rho.

It is continuous for weak measures tested against continuous functions on compact curve classes. Therefore theta^M<=theta^(M+1), and their curve marginals q^M also increase. Let theta=lim_M theta^M and q=lim_M q^M. Their masses are at most one.

The entropy absolute-continuity lemma applies separately for each M. It gives

    theta^M << q^M(dgamma) lambda_gamma(dx),                 (3)

because Section 3 removed the constant-curve locus. Here lambda_gamma is normalized parametrized arclength. Since q^M<=q, every q(dgamma)lambda_gamma(dx)-null set is also null for theta^M. Monotone convergence proves

    theta << q(dgamma)lambda_gamma(dx).                     (4)

Also q{length=0}=lim_M q^M{length=0}=0. This reasoning uses neither monotonicity of normalized conditional probabilities nor the false phase estimate.

## 5. Invariance from the witness rule

Let mu_n^M be the ambient image of p_n^M. If k>=1 and the P^k atom of x is selected at window M, its witness y also belongs to the P^(k-1) atom of x. The same future BG time is at distance at most M+1 from k-1. Thus that earlier atom is selected at window M+1. For every continuous h>=0,

    integral h d(g_*mu_n^(M+1))
      >= integral h d mu_n^M - ||h||_infinity/n.             (5)

Only the k=0 contribution is lost. First let n tend along the common subsequence, and then let M tend to infinity. The resulting finite measure satisfies g_*mu>=mu. These measures have the same total mass, so equality holds. If liminf mass(p_n^0)>=beta>0, monotonicity gives mass(mu)>=beta. Normalizing mu is then legitimate.

For any measurable alternative Z, mu(Z)>0 implies mu^M(Z)>0 for some finite M. In particular, if mu is decomposed into invariant alternatives, localization can use one such finite-M component of the joint curve representation. There is no need to assert that mu^0 sees every ergodic component.

## 6. Retaining geometric provenance

Every curve in the support of p^M is a C1 limit of selected original image curves. Contributions from ell<=L have total mass at most (L+1)/n, for each fixed L, so almost every limiting curve can be approximated with ell tending to infinity. If the finite-time construction supplies

    diameter(g^(-j)(g^ell(P))) <= C a^j,
                0<=j<=ell, 0<a<1,                        (6)

the limit satisfies the same bound for every fixed integer j. Thus every pair of points on the limiting curve approaches exponentially under g^(-j). When Pesin regularity is available, this is the geometric input placing a nonconstant limiting arc inside the full unstable manifold of any regular point on it. The precise regularity and Pesin theorem remain separate premises of that application.

If the original selected parents also carry a uniform density property for a fixed set F in D, that property is retained in the approximating parents. More explicitly, suppose every selected parent at a sufficiently large level intersects a set E on which

    lambda(F intersect P^ell(x))/lambda(P^ell(x)) -> 1

uniformly in x in E. Then the same ratio tends to one for any such approximating sequence of parents. Saturating E_n inside final partition atoms does not alter this conclusion, since those final atoms and all their ancestors still meet E. This is the density information needed for the later basin-capture argument; it is distinct from absolute continuity of the limiting measure.

## 7. Dependencies and scope

The proof uses the finite relative-entropy lemmas proved immediately before this result, ordinary C1 compactness, nesting, a geometric-family length lower bound, bounded distortion, and the explicitly stated witness rule. It reconstructs the measure-limit and invariance stage for one-dimensional curves. It does not construct the required finite-time partitions or prove a positive selected density.

The actual Ben Ovadia-Burguet manuscript, printed pages 43-48, defines the expanded selection by an existential witness in the parent atom and proves invariance by (5). Its page-24 tree supplies the required interleaving. The finite-time geometric propositions, the positive-density selection and genuine vector-derivative bounds remain external assumptions in this campaign. The source's literal modulus-only seminorm and endpoint compactness issues have separate audits. No full-source certification, C2 existence theorem, or Euler nonexistence theorem is implied here.

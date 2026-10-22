# Directional regularity at a smooth flat interface

Status: CONFIRMED by a complete independent proof, exact controls, and written reviews338/339 from actual Claude Opus5.5 with the endpoint objection resolved. The application is a conditional beta-two regularity exclusion, not a full B2 nonexistence theorem.

## Statement and conventions

Use positively oriented orthonormal physical coordinates (s,t), and a smooth graph C={(s,g(s)):s in I}, where I is a nonempty open interval. All fields below are smooth on an open neighborhood of this graph. A scalar function f is directionally flat on C when

    partial_t^k f(s,g(s))=0 for every s in I and k>=0.       (1)

Assume also that f is not identically zero on any full neighborhood of any point of C. The first assertion is:

(A) The set of s for which t -> f(s,t) has the zero germ at t=g(s) is meager in I. Its complement is a dense residual set. At every point of this complement the line restriction is flat but nonzero as a germ. Thus it belongs to no quasianalytic derivative-weight class on any line neighborhood of that point. Here the last assertion allows an arbitrary class for each line, provided the class has flat-germ uniqueness.

For a smooth vector field U=(U_s,U_t), put

    Omega=−curl U=−partial_s U_t+partial_t U_s.             (2)

Assume Omega satisfies (1) and is not zero on a full neighborhood of any point of C. Fix one positive derivative weight m, with m_0=1, logarithmic convexity, D_m=sup_{k>=1}(m_{k+1}/m_k)^(1/k)<infinity and sum_{k>=1}m_{k-1}/m_k=infinity. A one-variable C{m} function has bounds A B^k m_k on every compact interval, as in185. The second assertion is:

(B) The set of s for which both components of t -> U(s,t) belong to C{m} on some neighborhood of g(s) is meager. The neighborhoods and bounds may depend arbitrarily on s. There is no assumption of uniform bounds in s. The conclusion excludes vector membership; it does not say that both scalar velocity components fail separately.

The conclusion of (B) also holds simultaneously for any countable collection of such fixed weights, by taking the union of the exceptional meager sets. It is not asserted simultaneously for an arbitrary uncountable collection. No analyticity or quasianalyticity of the graph g is assumed. No divergence hypothesis or one-sided open zero region is required for these two general assertions.

For the beta-two B2 setting, take C to be a smooth local graph piece of Cstar, the endpoint and the two continued strong unstable orbits from179. At the endpoint this is the smooth local strong unstable manifold, with its two branches joined through the endpoint; at a regular orbit point a smooth flow map supplies the graph piece. Smoothness here is not inferred from the finite-C4 simultaneous chart. Set L=Theta(p), a constant. The precise common input is179: smooth full-plane B2 fields with W=2X+U−U(0), div W=4, Omega=−curl U, W.grad Theta=0, (W.grad+1)Omega=Theta_x and U=o(|X|); a compact smooth central zero arc gamma with normally repelling interior; a nonaccumulating endpoint p with DW(p)=4n tensor n and Theta−Theta(p),Omega flat there. The local unchanged-time C4 chart has gamma on v=0,u<=0, the smooth strong unstable curve on u=0, and u'=g(u)+uv B(u,v), v'=v D(u,v), D>2, |B|<=M, g=0 for u<=0. Require g>0 for small u>0 (outgoing), or g<0 there (incoming) with every other zero outside gamma isolated. Under exactly these hypotheses179(A)–(C) give all ambient derivatives of Theta−L and Omega zero on C and no full neighborhood of any point on which either is zero. No condition Z=gamma is used. Accumulating endpoints, absence of a definite sign of g, and incoming endpoints without the isolation premise are not covered. Hence (A) applies separately to Theta−L and Omega. For each fixed physical line direction for which the patch is a graph, on a dense residual set of its parallel-line parameters s in I, both scalar restrictions are flat and nonzero as germs and belong to no quasianalytic class. For each fixed weight in185, (B) also excludes the velocity restriction on a dense residual set; intersecting the three residual sets gives the simultaneous statement. A countable collection of fixed weights is allowed for U. Each fixed direction gives its own residual set; no simultaneous assertion over an uncountable collection of directions is made. Given a physical unit line direction e_t=(a,b), choose e_s=(b,−a); the ordered frame (e_s,e_t) has determinant1, so Omega=−curl U retains its sign. Shrink the patch so the chosen line direction is transverse at every point. The line direction must be transverse to C so it is a graph. A single selected transverse line can be exceptional, and tangent restrictions are not covered. These are necessary regularity properties of any putative profile, not contradictions to unrestricted smoothness.

## Elementary category fact

A set is nowhere dense if its closure contains no nonempty open interval. A meager set is a countable union of nowhere dense sets. We use residual to mean a complement of a meager set, rather than merely a nonmeager set. If E_n are closed with empty interior in a nondegenerate compact interval K, then K minus their union is dense in K.

For completeness, start in any open subinterval of K and choose a nondegenerate closed interval J_1 in that subinterval avoiding E_1. Given J_n, choose J_{n+1} inside its interior, avoiding E_{n+1}, with length at most2^(−n−1). This is possible because E_{n+1} has empty interior and is closed. Nested compactness gives a point in every J_n. It lies in the original subinterval and avoids every E_n, proving density. This also proves the assertions about countable intersections of residual sets used below. A countable compact-interval exhaustion transfers these conclusions to I.

## Proof of the scalar assertion

First work on a nondegenerate compact interval K contained in I. Compactness of the graph above K gives an integer N_0 such that the strip |t−g(s)|<=1/N_0, s in K, lies in the domain. For N>=N_0 put

    E_N={s in K: f(s,g(s)+u)=0 for every |u|<=1/N}.         (3)

Each E_N is closed: if s_j -> s in K and s_j in E_N, continuity applied at each fixed u in [−1/N,1/N] gives the defining equality at s. The union of E_N is exactly the set of zero germs along these lines. If E_N contained an interval J of positive length, then f would vanish on

    { (s,t): s in interior J, |t−g(s)|<1/N }.

This is open, by continuity of g, and contains a neighborhood of every graph point over interior J. It contradicts the hypothesis. Therefore each E_N is nowhere dense. The category fact proves (A) on K and then on I. For any s outside the union, (1) gives a flat but nonzero line germ. Quasianalytic flat-germ uniqueness excludes membership in every class with that property. Subtracting a constant, when using f=Theta−L, preserves the derivative-weight class.

Notice that the category conclusion uses no derivative bounds and no uniform class: it follows just from continuity, absence of a full zero neighborhood and the definition of a zero germ. Flatness is used only for the quasianalytic consequence.

## Proof of the velocity assertion

Fix K and N_0 as above, now for the domain of U and Omega. For each sufficiently large integer N define

    H_N={s in K: |partial_t^k U_j(s,g(s)+u)|
          <=N^(k+1)m_k for all k>=0, j=s,t, |u|<=1/N}.   (4)

H_N is closed. Indeed, for each fixed k,j,u the evaluated derivative depends continuously on s, so the bound is a closed condition; intersect these closed conditions over all k,j,u. The union of H_N is exactly the set in (B), restricted to K: local C{m} membership yields bounds on a compact line neighborhood, and a large enough N absorbs its radius, A and B. Conversely (4) gives the required bounds on the interior line interval.

It remains to prove H_N has no interior. Suppose an open subinterval J lies in H_N. Set u=t−g(s), and define on J x (−1/N,1/N)

    A(s,u)=U_s(s,g(s)+u), B(s,u)=U_t(s,g(s)+u),
    O(s,u)=Omega(s,g(s)+u).

The chain rule applied only once in s and any number of times in u gives

    O=−partial_s B+partial_u A+g'(s)partial_u B.           (5)

In particular, no transverse derivative estimate for U is inferred from (4). The extra graph coefficient depends only on s, so it creates no u derivatives. The physical line direction is unchanged: partial_u equals partial_t. Only smoothness of g is used.

For any smooth compactly supported test function phi in J, define F_phi(u)=integral_J O(s,u)phi(s)ds. Integration by parts in s has no boundary term and gives

    F_phi(u)=integral_J B(s,u)phi'(s)ds
          +partial_u integral_J (A(s,u)+g'(s)B(s,u))phi(s)ds.  (6)

Choose a compact subinterval of (−1/N,1/N). Bounds (4), the compact support of phi and boundedness of g' there show that every u derivative of each integral on the right is bounded by a constant times N^k m_k. The second integral has one further u derivative. Derivative closure from185 absorbs it: with D=max(1,D_m), m_{k+1}<=max(1,m_1)D^k m_k. Explicitly, a valid derivative bound for (6) is

    |F_phi^(k)(u)| <= N[||phi'||_1
        +N max(1,m_1)(1+sup_supp(phi)|g'|)||phi||_1]
                       (N D)^k m_k.                    (7)

The derivative and integral interchanges are justified by smoothness on the compact support times the chosen compact u interval. Thus F_phi belongs to C{m} on (−1/N,1/N), although no mixed derivative bounds for U were assumed.

For every k, condition (1) on Omega gives partial_u^k O(s,0)=0. Hence every derivative F_phi^(k)(0) is zero. The one-dimensional uniqueness theorem185 yields F_phi=0 on this whole interval. Since this is true for every test function phi, O(.,u) is zero as a distribution on J for every fixed u. Its continuity makes it pointwise zero. Thus Omega vanishes on the open curved strip J x (−1/N,1/N) in physical coordinates, a full neighborhood of graph points. This contradicts the hypothesis.

So H_N has empty interior and is closed. Its countable union is meager, which proves (B). Repeating for countably many weights and taking a countable union proves the asserted simultaneous extension. This argument never asserts that differentiation in s preserves a linewise class; equation (6) moves that derivative onto a test function instead.

## Why the generic qualification and the hypotheses matter

Let h(t)=exp(−1/t²) for t<0 and0 for t>=0. Put f(s,t)=s²h(t), g(s)=0. It is smooth, all its derivatives vanish along t=0, and no graph point has a full zero neighborhood. Nevertheless the line s=0 has the identically zero germ, while every s!=0 has a flat nonzero germ. Thus (A) cannot be strengthened to every transverse line from these assumptions. This is a manufactured scalar example, not a B2 solution.

If the no-full-zero-neighborhood hypothesis is removed, f=0 defeats both scalar conclusions, while U=(t,s), Omega=0 supplies an analytic vector field that defeats (B). If the scalar flatness hypothesis is removed, f=t at g=0 is nonzero as a line germ and analytic; the category zero-germ conclusion still holds, but its nonquasianalytic consequence fails. If quasianalyticity is removed, the smooth divergence-free field U=(h(t),0), Omega=h'(t), gives a flat vorticity with no zero neighborhood along the interface and velocity in a higher Gevrey class along every transverse line. This last example is not a B2 profile and does not supply one.

The term g' partial_u B in (5) cannot be dropped for a curved graph. For example U=(0,s t), g=s² gives physical Omega=−t, pulled-back Omega=−u−s². The term −partial_s B alone is −u−3s², and the correction restores the correct expression. This polynomial checks the coordinate identity only; its vorticity is not flat and it is not a B2 profile.

## Dependencies, source and scope

Packet185 supplies the full one-variable uniqueness and derivative closure theorem with the actual-derivative weight convention. Packet179, with the incoming qualification established in177, supplies the stated B2 flatness and absence-of-neighborhood hypotheses. This proof verifies the additional category and weak-derivative argument and makes no new existence assertion. No theorem-prover formalization or build is claimed. Controls will test the coordinate and integration identities and explicit failures of overstrong statements, not certify a residual set by finite sampling.

A background source for the elementary closed-nowhere-dense-set theorem is M. Christ, Math202B, Spring2014, Topic4, first Baire theorem and its nested-ball proof, https://math.berkeley.edu/~mchrist/Math202B/Lectures/topic4.pdf. The complete interval proof above is independent and sufficient here. The source uses residual differently in a later paragraph; only its first dense-intersection theorem is used, and our convention is explicit. No novelty relative to general category or partial-regularity literature is claimed.

## Verification evidence

Published UTC 2026-10-21T17:09:49.364764+00:00. The original complete proof was written2026-10-21T17:03:03.047452Z, before any controls; its initial hash is in verification/draft_record.json. Final controls375 and negative controls8 passed from2026-10-21T17:08:12.735090+00:00 to2026-10-21T17:08:22.731166+00:00 in9.996096635s. They verify16 independent polynomial graph/curl cases, directional derivatives through order4, weak integration identities and their derivatives, proper-frame rotations, absorption of line-dependent constants, and derivative-closure bookkeeping including order0. The polynomial test functions in the finite integration controls vanish at the two interval endpoints; they are used only to check the boundary-free identity and are not asserted to be smooth compactly supported test functions on the open interval. The proof uses the latter. Negative examples detect omission of the graph correction, wrong curl sign, an unjustified missing boundary term, replacing residual by every line, removal of flatness or the no-zero-neighborhood hypothesis, removal of quasianalyticity, and strengthening vector failure to failure of both components. None of these finite checks establishes a category theorem or a B2 profile.

Actual model us.anthropic.claude-opus-5-5 returned claude-opus-5-5 through the existing Python Bedrock client. Review338 provided a written general-theorem audit in71.083620235s. It confirmed the closed-set argument, nonuniform linewise constants, graph correction, weak-curl identity and bound(7), while recommending the fixed-direction wording adopted above. It initially suggested removing the endpoint because an arbitrary pair of orbits need not join smoothly. We challenged that suggestion with the precise179 statement and the original smooth strong unstable curve. Review339 returned a written follow-up in41.029487494s and withdrew the objection: the local graph includes the equilibrium. It also confirmed that L=Theta(p) is constant and that179(A)–(C) imply exactly the scalar and velocity hypotheses. Both reviews limit their scope: they do not newly certify the proofs of185 or the geometric dependencies of179. Those independently checked earlier packets remain the explicit premises.

We independently checked the proposed orientation qualification: for any fixed unit e_t=(a,b), the choice e_s=(b,−a) is positively oriented, so no orientation reversal or change of Omega is necessary. The rotation controls verify this identity. The endpoint may be included in a local graph patch, but no global embeddedness assertion for a general Cstar is needed here. The incoming isolation premise and all common endpoint hypotheses are stated explicitly. No theorem-prover build or numerical existence claim is made.

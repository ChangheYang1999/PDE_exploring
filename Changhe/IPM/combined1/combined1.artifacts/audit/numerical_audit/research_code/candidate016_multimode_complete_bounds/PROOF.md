# Complete candidate016 bounds from sixteen verified trials and a full angular tail

## Exact statement and conventions

Use the canonical residual F of C1-N1-016-legqs25-quot013, raw SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42, at c=4076476460239181/2251799813685248. Put rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), F=(cX+u).grad rho-rho on R2. All fields are real and every norm uses Lebesgue measure. The full source has1360 branches and exactly160 odd sine frequencies1 through319. The accepted complete-field record N4-392 establishes its regularity, complete nonlinear products and G0=||F||2, G1=||grad F||2, P2=||(1+4r^2)^(2/5)D2F||2 and ||rF||2, with the Euclidean Hessian norm and containing endpoint certificates.

Define H(F)=sup{|int F phi|:phi smooth compactly supported,||grad phi||2<=1} and
 E2(F)^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2.

Let q_n=pi int_0^infinity r^3 f_n(r)^2dr for F=sum f_n(r)sin(n theta). Let a complete odd prefix1 throughN be source-certified with q_n in[l_n,u_n], and let complete R2=||rF||2^2 be at most R_U. If N<319 set m=N+2 and

 V_N=R_U/m^2+sum_(odd n<=N)(1/n^2-1/m^2)u_n.

For N=319 use V_N=sum u_n/n^2. Let the16 exact finite dual and solenoidal tests at n=1,3,...,31 be those in candidate016_multimode_dual_cross. Let L_n and J_n be their accepted positive strict rational floors for |int Fpsi_n|/||grad psi_n||2 and <A_F,Z_n>^2/||Z_n||2^2. Within modes1 and3, an already accepted deeper trial can be selected separately for each of these two objectives by maximum; no same-frequency floors are added. Put L2=sum L_n^2 and U2=V_N-sum J_n. Then

 L2<H(F)^2<U2.

The bound record gives exact positive rational endpoints, verifies L2<U2, and assembles E2 by monotone substitution of the accepted complete component bounds. The same E2 definition for007 has accepted upper606.820219, so any derived016strictlower e_L yields the strict gap E2(016)-E2(007)>e_L-606.820219. Its accepted H lower ball similarly gives H(007)-H(016)>H007_lower-h_U whenever that rational difference is positive. No ordering of correction distances follows.

## Complete proof

Set A_F=-e_theta r sum f_n cos(n theta)/n. It is square integrable because sum q_n=R2 is finite, and has squared norm M2=sum q_n/n^2. Angular differentiation gives div A_F=F on annuli; local regularity and its zero radial flux give the distributional identity across the origin. Hence H(F)<=||A_F||2. When N<319, every omitted odd frequency is at least m and nonnegativity gives M2<=R2/m^2+sum_(n<=N)(1/n^2-1/m^2)q_n. All coefficients are positive, so M2<=V_N. For the complete prefix the exact angular identity gives the stated V_N directly. Every uncomputed mode is retained through R_U. Agreement with a truncated sum is not used.

Each selected test is smooth at the origin, its gradient and r Delta are in L2, and radial cutoffs converge in gradient norm. These facts follow from its finite exact labels beta>3/2, k>=-1 and 3+2k-n even nonnegative, as proved in candidate016_multimode_dual_cross/PROOF.md and checked label by label. The signed pairing equals its ordinary absolutely convergent integral by its source-bound endpoint checks. Distinct frequencies give orthogonal gradients. Applying F to the finite combination with coefficients p_n/d_n, where p_n=int Fpsi_n and d_n=||grad psi_n||2^2, gives H(F)^2>=sum p_n^2/d_n>sum L_n^2.

Put Z_n=A_(Delta psi_n)-grad psi_n. The whole-plane divergence identities imply div Z_n=0. Their polar components have distinct frequencies, hence the Z_n are mutually orthogonal in L2. Write b_n=<A_F,Z_n>, a_n=||Z_n||2^2>0. The field A_F+sum t_n Z_n has divergence F and squared norm M2+sum(2t_nb_n+t_n^2a_n). Taking t_n=-b_n/a_n yields H(F)^2<=M2-sum b_n^2/a_n<V_N-sum J_n. Selection by maximum simply chooses one admissible test for each n; the choices for the lower and upper arguments may differ. The elementary gradient dual and divergence-free theorems have both complete Opus reviews accepted in N4-404/408, with the general angular prefix review reciprocated by N4-414. Their source, domain, normalization and local-integrability scopes are preserved. No outstanding review is silently declared complete.

Insert L2 and each component lower bound in the positive E2 square to obtain EL2; insert U2 and each upper bound to obtain EU2. Exact squaring verifies every stored rational lower and upper endpoint. Exact subtraction then proves the stated same-norm gaps when positive. This uses complete bounds on the same actual residuals; it proves no basis optimality, exact H value, inverse, fixed point, existence or changed candidate exclusion.

## Verification and dependencies

This proof precedes its checker. Register the accepted immutable norm, old upper, general reviews,007 norm and exact source hashes in source/dependencies.json. At execution bind the completed16-mode result, every mode and group record, the complete-source prefix result and every declared input. Recompute the sums and positive coefficient formula using exact Fraction arithmetic. Require all sixteen distinct trial frequencies and all prefix frequencies, exact candidate/source identity, no same-frequency addition, and all accepted check verdicts. Verify group counts and retained endpoint serialization without repeating expensive source integrals. Both the production certificates and the completed independent reviews are dependencies, not consequences of file hashing. The checker accepts only a new unused version path. A failed or incomplete source result cannot be promoted.

Collaborating theory lanes are configured as us.anthropic.claude-opus-5-5, with actual provider responses unobservable. No remote model call, substitute model, JavaScript/TypeScript, server, RLScience cluster, Lean build, GPU or optimizer is used.

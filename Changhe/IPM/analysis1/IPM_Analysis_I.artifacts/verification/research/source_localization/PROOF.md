# Concentration of a homogeneous adjoint mode at a smooth fixed point

Date:2026-10-20. Status: CONFIRMED conditional theorem, independently derived and reviewed by actual Claude Opus5.5. This is a conditional theorem about specified Sobolev graph realizations. It is not a nonexistence theorem for the IPM profile, and does not identify the domain or target of the lead's proposed inverse.

## Precise statement

Work on R^2 with the unitary Fourier transform and the ordinary Sobolev norm

||f||_{H^t}^2 = integral (1+|xi|^2)^t |fhat(xi)|^2 dxi.

For a Schwartz function whose Fourier transform has compact support disjoint from zero, also write

||f||_{dot H^t}^2 = integral |xi|^{2t}|fhat(xi)|^2 dxi.

Let s>0, let N be an integer greater than s, and fix P in R^2. Let V be a real C^1 vector field with bounded first derivative, V(P)=0 and DV(P)=B. Assume V is C^{N+1} on a neighborhood of P. Thus V has at most linear growth. Let a_j, j=1,...,J, be bounded measurable real-valued functions, C^N on a neighborhood of P. No high coefficient regularity is required outside that neighborhood. Let T_j be bounded L2 Fourier multipliers with bounded symbols homogeneous of degree zero; the same symbols define bounded operators on every H^t and dot H^t used below. No angular smoothness of their symbols is needed for the estimates.

Define, on test functions,

A h=V.grad h-h+sum_j a_j T_j h,
A_P h=(B(X-P)).grad h-h+sum_j a_j(P)T_j h.

Let D be a Hilbert space continuously embedded in H^s, with C_c^infty dense in D and continuously included in D as test functions. Suppose A extends to a bounded map D to H^s agreeing with its distributional action, and let K:D to H^s be finite rank and bounded. This includes the completion of a C_c^infty graph domain whenever that completion is embedded in H^s and the stated map exists. It does not assert that every possible extension of A has this core.

Suppose there are Schwartz functions phi_j, each with smooth compact Fourier support disjoint from zero, for which

||phi_j||_{dot H^{-s}}=1,
||A_0' phi_j||_{dot H^{-s}} tends to0,

where A_0 is A_P translated to a fixed point at0 and prime is the formal L2 adjoint. Then A+K:D to H^s is not Fredholm.

In particular, this premise holds for

A_0=A x partial_x+y partial_y-1-gM,
Mhat(xi,eta)=xi^2/(xi^2+eta^2), A>1, g>=0,

whenever

(g+b)/A < s < b, where b=(A+3)/2. Thus this statement requires a nonempty open band (g+b)/A<b.

The conclusion is an obstruction to Fredholmness in these ordinary Sobolev graph realizations. Normalization terms whose images do not belong to H^s, spatially weighted targets, a different source domain, or a finite-regularity coefficient field require additional arguments. In particular no conclusion here excludes P_2 or P_infty solutions.

## The scaling and polynomial identities

For epsilon>0 define

(S_epsilon phi)(X)=epsilon^{-s-1} phi((X-P)/epsilon).

Its Fourier transform is epsilon^{1-s} exp(-i P.xi) phihat(epsilon xi). Hence

||S_epsilon phi||_{H^{-s}}^2
 = integral (epsilon^2+|zeta|^2)^{-s}|phihat(zeta)|^2 dzeta.

For Fourier support bounded away from zero, dominated convergence gives convergence to ||phi||_{dot H^{-s}}^2 as epsilon tends to0. More generally the displayed norm is at most ||phi||_{dot H^{-s}}, whenever the latter is finite. A degree-zero Fourier multiplier commutes with this scaling and translation. Multiplication by a polynomial in the scaled variable, and differentiation in that variable, preserve smooth compact Fourier support away from zero. Therefore every polynomial times phi or its derivatives has a finite dot H^{-s} norm and its S_epsilon-scaled H^{-s} norm is bounded uniformly in epsilon.

There is also the cruder bound

||S_epsilon f||_{H^{-s}} <= ||S_epsilon f||_2 = epsilon^{-s}||f||_2.

This bound is used only for Taylor remainders of sufficiently high order. Using it for the first-order coefficient error would fail when s>1.

## A Taylor estimate for the variable coefficients

Fix one Schwartz phi with smooth Fourier support compact and away from zero. On a closed ball about P on which the required derivatives are bounded, Taylor expansion about P gives

V(P+epsilon z)=epsilon Bz+sum_{q=2}^N epsilon^q V_q(z)+R_epsilon(z),

where V_q is a homogeneous polynomial vector field of degree q. The bounds below hold first for |epsilon z| at most a fixed positive delta:

|R_epsilon(z)| <= C epsilon^{N+1}|z|^{N+1},
|grad_z R_epsilon(z)| <= C epsilon^{N+1}|z|^N.

The second inequality follows by applying the order N-1 Taylor formula to DV(P+epsilon z), and multiplying its remainder by epsilon. Since DV's Taylor terms through degree N-1 are exactly the derivatives of the displayed polynomial for V, it gives precisely the remainder stated. For |epsilon z|>=delta the same bounds hold after increasing their constants. Indeed V has at most linear growth, DV is bounded, and the subtracted Taylor polynomials have degrees N and N-1. Every resulting power of |epsilon z| of degree at most N is bounded by a delta-dependent constant times |epsilon z|^{N+1}; the derivative case is bounded by a constant times |epsilon z|^N. The displayed Taylor bounds therefore hold globally. Their constants may depend on delta, V and N, but not on z or epsilon.

The formal adjoint of V.grad is -div(V times). Applying the scaled formal adjoint difference gives

(A'_{drift}-A'_{P,drift})S_epsilon phi
 = S_epsilon[-sum_{q=2}^N epsilon^{q-1}div_z(V_q phi)
              -epsilon^{-1}div_z(R_epsilon phi)].

Every polynomial term has H^{-s} norm O(epsilon^{q-1}) by the preceding Fourier-support observation. For the remainder, the Schwartz decay of phi and its first derivatives and the global Taylor bounds give

||epsilon^{-1}div_z(R_epsilon phi)||_2 <= C_phi epsilon^N.

The crude scaling inequality therefore bounds its H^{-s} norm by C_phi epsilon^{N-s}, which tends to zero because N>s.

For a_j expand through degree N-1:

a_j(P+epsilon z)=a_j(P)+sum_{q=1}^{N-1}epsilon^q a_{j,q}(z)+r_{j,epsilon}(z),
|r_{j,epsilon}(z)|<=C epsilon^N |z|^N.

For |epsilon z|>=delta the same remainder bound follows from global boundedness of a_j and the finite Taylor polynomial, increasing the constant as above. The adjoint zero-order term is T_j^*(a_j times). Its difference from the frozen term is the multiplier applied to the corresponding polynomial terms and remainder. The multiplier is bounded on H^{-s} and commutes with scaling. It is applied after the coefficient-error norm is bounded, so its nonlocal support does not change the Taylor estimate. The polynomial terms are O(epsilon) and the remainder is O(epsilon^{N-s}) by the same estimates. Summing the finitely many terms proves

||A' S_epsilon phi - S_epsilon A_0' phi||_{H^{-s}} = O(epsilon^{min(1,N-s)}),

which tends to0. The constant depends on finitely many weighted L2 norms of phi and its derivatives, and homogeneous norms of its polynomial multiples.

All operators in this identity act on actual Schwartz functions and distributions. No negative-order homogeneous space is used on a function with unexamined low-frequency behavior: homogeneous norms are used only for the finite polynomial terms, whose Fourier support stays away from zero. The high-order remainders use ordinary L2 instead.

## Construction of a weakly null dual sequence

Apply the preceding estimate separately to each phi_j in the theorem premise. If its Fourier support has minimum radius r_j>0, choose epsilon_j>0 so small that epsilon_j<r_j/j and the following three conditions hold:

1. | ||S_epsilon_j phi_j||_{H^{-s}} -1 | <1/j;
2. ||A' S_epsilon_j phi_j-S_epsilon_j A_0' phi_j||_{H^{-s}} <1/j;
3. epsilon_j<1/j, so epsilon_j tends to0.

This is a diagonal choice of real numbers, not a numerical assumption. Condition1 uses the exact scaling limit, and condition2 the fixed-phi Taylor estimate. Normalize f_j=S_epsilon_j phi_j/||S_epsilon_j phi_j||_{H^{-s}}. Then ||f_j||_{H^{-s}}=1 and

||A'f_j||_{H^{-s}} tends to0,

because ||S_epsilon_j A_0'phi_j||_{H^{-s}}<=||A_0'phi_j||_{dot H^{-s}}. The frozen adjoint preserves the compact Fourier support away from zero: its drift is a first-order Fourier differential operator, and the bounded multiplier terms do not enlarge support. The assumed homogeneous norm is therefore legitimate even without smoothness of the multiplier symbol.

The Fourier support of f_j is contained in {|xi|>j}. For each fixed h in H^s, dual Cauchy-Schwarz gives

|<f_j,h>| <= ||f_j||_{H^{-s}} ||1_{|xi|>j} hhat||_{H^s},

which tends to zero. Thus f_j converges weakly to zero in H^{-s}, the dual of H^s.

## Graph-dual obstruction

For h in C_c^infty the formal adjoint identity gives <f_j,Ah>=<A'f_j,h>. The right side has absolute value at most C||A'f_j||_{H^{-s}}||h||_D, by the continuous embedding D to H^s. Density of C_c^infty in D extends this identity and estimate to all D. Consequently the Banach adjoint A^*:H^{-s} to D^* satisfies ||A^*f_j||_{D^*} tending to0.

The adjoint of a finite-rank bounded map is compact. Since f_j is bounded and weakly null, ||K^* f_j||_{D^*} tends to0 as well. One can see this directly by writing K h=sum_{l=1}^d lambda_l(h)v_l, with lambda_l in D^* and v_l in H^s: each <f_j,v_l> tends to0.

If A+K were Fredholm, its adjoint would have closed range and finite-dimensional kernel. The closed-range theorem on Hilbert spaces gives

dist_{H^{-s}}(f,ker(A+K)^*) <= C||(A+K)^*f||_{D^*}.

The orthogonal projections of the weakly null f_j onto that finite-dimensional kernel tend to zero in norm. The displayed estimate would then imply ||f_j||_{H^{-s}} tending to0, contradicting its unit norm. This proves the theorem.

## The IPM frozen premise

The already checked theorem in ../frozen_cokernel/PROOF.md supplies an exact homogeneous adjoint kernel after conjugating A_0 by Lambda^s, whose Fourier multiplier is the full frequency modulus |(xi,eta)|^s. All Sobolev frequency moduli below are two-dimensional. Write D_F=A xi partial_xi+eta partial_eta, and use eta=plus-or-minus exp(t), xi=exp(A t)v with the Jacobian unitary transformation from that theorem. The conjugated adjoint is partial_t+C with

C=s-b+[s(A-1)-g]m,
m=v^2 exp(2(A-1)t)/(1+v^2 exp(2(A-1)t)).

Take a nonzero smooth a(v) compactly supported in1<|v|<2. The function

G(v,t)=a(v) exp((b-s)t)
       [1+v^2 exp(2(A-1)t)]^{[g-s(A-1)]/[2(A-1)]}

is square integrable, since b-s>0 and b+g-As<0. Multiply by smooth cutoffs chi_j(t) that equal1 on[-j,j], vanish outside[-j-1,j+1], and have derivatives bounded uniformly. The adjoint of the cutoff function is just chi_j'G, whose L2 norm tends to zero by the integrable tails. The cutoff norm tends to a nonzero finite limit. Transforming back gives normalized smooth compactly supported Fourier functions g_j away from the axes and from frequency zero, with

||(Lambda^s A_0 Lambda^{-s})^*g_j||_2 tending to0.

Set phi_j=Lambda^s g_j in physical notation, that is phihat_j=|xi|^s ghat_j. Then ||phi_j||_{dot H^{-s}}=1, and

||A_0'phi_j||_{dot H^{-s}}
 = ||(Lambda^s A_0 Lambda^{-s})^*g_j||_2 tends to0.

The compact Fourier support away from zero makes phi_j Schwartz. Thus the theorem premise is satisfied. This proof uses the open homogeneous adjoint band only. The wider ordinary-H^s frozen cokernel theorem alone does not imply the same localization conclusion.

## Dependencies and scope

Dependencies are the explicit frozen adjoint calculation, Taylor's theorem with bounded derivatives, Plancherel, the elementary Sobolev duality and closed-range theorem, and compactness of finite-rank maps. The high regularity of V and a_j is an explicit hypothesis. It has not been certified for an unknown exact P_2 profile. No coefficient-enclosure calculation, residual bound, nonlinear estimate, spatially weighted realization, source/saddle trace domain, or global canonical normalization functional is proved here.


Review record: actual Claude Opus5.5 accepted the elementary Taylor estimate and its rate at2026-10-20T15:53:24Z in ../../notes/reviews/taylor_only_response.md. Larger requests returned refusal without a final text; they provide no review evidence. The graph-dual and frozen-premise constructions were subsequently accepted in graph_dual_localization_response.md and frozen_premise_localization_response.md. The symmetric and general-mu extensions were accepted at2026-10-20T15:59:14Z in source_localization_extensions_response.md. Its stronger per-multiplier parity condition was challenged using a(x,y)=xy exp(-x^2-y^2) and symbol xi*eta/(xi^2+eta^2): each factor anticommutes with either reflection while their product commutes. Actual Opus5.5 checked the counterexample and withdrew that unnecessary condition at2026-10-20T16:01:26Z in source_parity_correction_response.md.


## Symmetric real realization

Suppose P=(p,0), p>0, A and its formal adjoint preserve real-valued functions and commute with the two coordinate reflection operators on the test-function core, with these identities extended to the indicated domain and target by continuity, and its frozen operator at P is exactly B=diag(A,mu) with sum_j a_j(P)T_j=-gM aligned with the x-axis. Here mu=1 in the first displayed band, or A>mu>0 in the generalized band below. In particular V(P)=0 and the reflection symmetry gives V(-P)=0. Let H^s_sym denote real functions even in x and odd in y. Replace the core hypothesis by density of C_c^infty intersect H^s_sym in a Hilbert domain D_sym continuously embedded in H^s_sym, and assume A+K maps D_sym to H^s_sym with K bounded and finite rank. The same non-Fredholm conclusion holds for the diagonal frozen operator in the stated band.

To prove this, choose a(v) even, take opposite signs on the two eta half-planes, and multiply the Fourier function by i. The inverse Fourier transform phi_j is real, even in its first variable and odd in its second, by the Hermitian symmetry under simultaneous reversal and the separate reflection identities. Concentrate this function at P as before. Write R_x for reflection in x and put

h_{j,epsilon}=S_epsilon phi_j+R_x S_epsilon phi_j.

This is even in x and odd in y. For fixed j the H^{-s} squared norms of each summand tend to1. Their cross inner product tends to0. Indeed, up to a sign of the phase, it is

integral exp(2i P.zeta/epsilon)(epsilon^2+|zeta|^2)^{-s}|phihat_j(zeta)|^2 dzeta.

The amplitude converges in L1 to |zeta|^{-2s}|phihat_j(zeta)|^2, since its support is compact and avoids zero. The Fourier integral of that limiting L1 function tends to0 as |2P/epsilon| tends to infinity. This last fact follows first for smooth compactly supported amplitudes by integration by parts along P, then for L1 amplitudes by approximation. Hence ||h_{j,epsilon}||_{H^{-s}} tends to sqrt(2).

Add the cross-inner-product bound <1/j to the diagonal choice, and normalize h_{j,epsilon_j}. Each summand still has Fourier support outside radius j, so the normalized sum is weakly null. Reflection commutes with A' because it is a unitary involution commuting with A on test functions. Thus both formal adjoint residuals tend to zero and so does their sum. The graph-core and finite-rank argument then applies entirely within the symmetric real spaces. This supplies the parity conclusion without replacing a pair of sources by a fictitious source at the origin.

## A general positive diagonal fixed point

For the frozen operator

A_0=A x partial_x+mu y partial_y-1-gM,
A>mu>0, g>=0,

with an integer N>s as before, the same argument works in the nonempty open band

(g+b)/A < s < b/mu, b=1+(A+mu)/2,

which requires mu(g+b)<Ab.

In the Fourier variables eta=plus-or-minus exp(mu t), xi=exp(A t)v, the Jacobian is mu exp((A+mu)t), so use its positive square root in the unitary transformation. The conjugated adjoint potential is

C=s mu-b+[s(A-mu)-g]m,
m=v^2 exp(2(A-mu)t)/(1+v^2 exp(2(A-mu)t)).

Its exact homogeneous adjoint solution is

G=exp((b-s mu)t)
 [1+v^2 exp(2(A-mu)t)]^{[g-s(A-mu)]/[2(A-mu)]}.

Logarithmic differentiation gives G'/G=-C. The two exponential tail rates are b-s mu at minus infinity and b+g-sA at plus infinity. The stated strict inequalities are exactly their integrability conditions. The same smooth cutoffs and all localization estimates therefore apply. This general form can assess an approximate background whose slow eigenvalue is close to, but not exactly,1. It still requires that the fixed point and every operator-domain hypothesis have been proved.


The reality and reflection hypotheses above are imposed on the full operator. Its individual Fourier multipliers need not be even under each reflection: for example the real symbol xi eta/(xi^2+eta^2) changes sign under each coordinate reflection, and multiplication by a real coefficient odd in each coordinate compensates both signs. This is the form of the U1[h]rho_x term in IPM. Requiring each separate multiplier to preserve parity would be an unnecessary additional restriction.

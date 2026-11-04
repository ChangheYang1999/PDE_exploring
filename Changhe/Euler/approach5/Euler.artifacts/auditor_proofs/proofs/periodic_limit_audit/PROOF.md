# A conditional Liouville theorem for point or periodic backward limit sets

## Exact statement and scope

Let 0<c<1/2, omega be any finite real number, and U,P belong to C^2(R^3). Assume div U=0, uniform U(y)=o(|y|), and

\[
 (1-c)U+B\cdot\nabla U+\omega JU+\nabla P=0,
 \qquad B=(cI-\omega J)y+U.
\]

Suppose, additionally, that for Lebesgue almost every initial point the alpha-limit set of the complete B-flow is a single equilibrium or the image of a single nonconstant periodic orbit. Then U is constant. If U tends to zero, then U=0.

Hypothesis tags: H0, H1-prime, H6. No pressure normalization, derivative decay, integrability, symmetry or restriction on omega is assumed. The H6 condition has not been derived from decay. This is an independently checked version of LIT03 in the literature agent.

## 1. Flow and form transport

Linear growth of B gives its complete C^1 flow Phi_t. Since B(y) dot y=c|y|^2+U(y) dot y, every backward trajectory is bounded. Its nonempty compact alpha-limit set attracts that trajectory in backward time as a set: otherwise a sequence staying a fixed positive distance away has a limit point in the alpha-limit set, a contradiction.

Set a=1-2c>0 and beta=d(U dot dy), with skew coefficient matrix W. Direct differentiation of the momentum equation as a one-form gives

\[
 \Phi_t^*\beta=e^{-at}\beta.
\]

Equivalently, with F_t=DPhi_t,

\[
 W(\Phi_t x)=T_t(x)W(x),\qquad
 T_t(x)Z=e^{-at}F_t(x)^{-T}ZF_t(x)^{-1}.       \tag{1}
\]

All matrix norms below are fixed finite-dimensional norms. This transport identity is verified separately in the team records. Its validity does not require any bound on derivatives at infinity.

## 2. A direct local trapping lemma

We record the precise finite-dimensional dynamical fact needed for null basins. Let G be a C^1 local diffeomorphism fixing zero and let A=DG(0) have an eigenvalue outside the unit circle. There is a small ball D such that points whose nonnegative G iterates stay in D form a null set.

To prove it, split the real space into invariant generalized eigenspaces E_cs and E_u for eigenvalue moduli at most one and greater than one. The latter space is nonzero. For some M,beta>0 and any sufficiently small epsilon>0,

\[
 \|A_{cs}^n\|\le M e^{\epsilon n},\qquad
 \|A_u^{-n}\|\le M e^{-\beta n}\quad(n\ge0).
\]

On a convex small ball, G(x)=Ax+f(x), with Lip(f)<=delta as small as desired. Take two trapped orbits x_n,z_n, put d_n=x_n-z_n and choose epsilon<eta<beta. Their boundedness makes

\[
 D_* =\sup_{n\ge0}e^{-\eta n}|d_n|<\infty.
\]

Variation of constants gives the forward sum for d_cs,n. The unstable component has the backward sum

\[
 d_{u,n}=-\sum_{k=n}^{\infty}A_u^{n-1-k}
                      (f(x_k)-f(z_k))_u.
\]

The discarded terminal term tends to zero because both orbits are bounded and A_u^{-N} decays. Estimating the two geometric sums yields

\[
 D_*\le M|d_{cs,0}|+
 M\delta\left((e^\eta-e^\epsilon)^{-1}
                 +(e^\beta-e^\eta)^{-1}\right)D_*.
\]

Use the sum norm on the splitting and absorb the last term by shrinking delta. Thus D_*<=2M|d_cs,0|. Projection to E_cs is injective on the trapped set and its inverse is Lipschitz. The trapped set is a Lipschitz graph over a subset of E_cs, of dimension at most d-1, hence null. A coordinatewise Lipschitz extension, or the elementary cube-cover estimate, supplies this last nullity statement. This proves the needed trapping result without assuming hyperbolicity in the center directions or citing a global stable-manifold theorem.

## 3. Equilibrium limits

At an equilibrium p set A=DB(p). If all eigenvalues have nonnegative real part, the matrices e^{-tA} grow at most polynomially for t>=0. Therefore

\[
 \|T_t(p)\|\le e^{-at}\|e^{-tA}\|^2\longrightarrow0.
\]

Choose tau>0 with norm below 1/2. Continuity gives a neighborhood O on which ||T_tau||<=3/4. A trajectory converging backward to p eventually stays in O. Applying (1) to j consecutive forward steps of length tau, starting j steps into its backward tail, gives

\[
 |W(\Phi_{s_0}y)|\le(3/4)^j|W(\Phi_{s_0-j\tau}y)|\longrightarrow0.
\]

The last W is uniformly bounded on the compact tail. Transport gives W(y)=0.

If A has an eigenvalue with negative real part, G=Phi_{-1} has an eigenvalue outside the unit circle. Section 2 provides a neighborhood O_p with null forward-G trapping set. These neighborhoods cover the bad equilibria, and second countability gives a countable subcover. A trajectory converging to any covered equilibrium eventually remains in one neighborhood. It lies in an integer positive-time image of that neighborhood's trapping set. The countable union of these C^1 diffeomorphic images is null. Countability of the equilibria themselves is not assumed.

## 4. Periodic limits with no contracting multiplier

Let K be a nonconstant periodic B orbit of least period T. Write C_p=DPhi_T(p) for p in K. If all eigenvalues of C_p have modulus at least one, then C_p^{-n} grows at most polynomially. The polynomial bound is uniform over p in K: monodromies are conjugate through DPhi_s(p_0), 0<=s<=T, and these conjugating matrices and inverses are uniformly bounded. Consequently

\[
 \sup_{p\in K}\|T_{nT}(p)\|
 \le e^{-anT}\sup_{p\in K}\|C_p^{-n}\|^2\longrightarrow0.
\]

Choose an integer n and tau=nT making this supremum below 1/2. Compactness and continuity give a neighborhood O_K with ||T_tau||<=3/4. Every backward trajectory with alpha-limit K eventually stays in O_K. The same iterative estimate as in Section 3 gives W(y)=0. No convergence of a phase, no commensurability between different orbit periods and no global choice of tau is needed.

## 5. Periodic limits with a contracting multiplier

Suppose C_p has an eigenvalue of modulus below one. The vector B(p) is a nonzero eigenvector with eigenvalue one. On a transverse two-dimensional section through p, the derivative of the Poincare return map R is the induced monodromy on the quotient by the flow direction. Its spectrum therefore contains the contracting multiplier. R^{-1} has an eigenvalue outside the unit circle. Section 2 applied in this section gives a neighborhood D whose points trapped by all forward R^{-1} iterates form a Lipschitz graph M of dimension at most one.

Here are the flow and locality details. K is an embedded compact C^2 circle with nonvanishing tangent. A sufficiently small tubular neighborhood has a C^1 circle-valued phase function theta equal to flow time modulo T on K. On a smaller tube, dtheta(B)>1/2, say, after normalizing dtheta(B)=1 on K. The section theta=0 is transverse. Shrink the tube further so every section crossing of a trajectory remaining in it lies in D and successive crossings are related by the same local return map R or its inverse. This follows from continuous dependence of the flow over the finite interval [0,2T] and local existence of R near p. The positive lower bound for phase speed bounds successive return times above, and its finite upper bound bounds them below.

Thus every trajectory remaining in the tube for all negative time meets the section infinitely often backward, with its crossings in M. Its current point is on a flow segment of uniformly bounded length through M. The set of all such points is contained in the image of M times a bounded interval under a C^1 map. On compact coordinate pieces this map is Lipschitz; the image has dimension at most two and is null in R^3. Denote a null containing set by N_K and the chosen tube by O_K. We have

\[
 \{x:\Phi_{-t}x\in O_K\text{ for all }t\ge0\}\subset N_K.
                                                        \tag{2}
\]

No isolated-cycle hypothesis was used.

## 6. Countability for an arbitrary family of cycles

The null sets N_K cannot simply be united over all bad cycles. Use the countable collection of finite unions of rational open balls. For each bad K there is a member V with K contained in V and V contained in O_K. Let V_collection be the subcollection of all finite unions admitting at least one such witness. For each V choose one witness K_V with V contained in O_{K_V}.

If an initial point has a bad cycle K as alpha-limit set, choose V containing K and contained in O_K. Eventually its full backward tail stays in V, hence in O_{K_V}, regardless of which witness was selected. For some integer N>=0, Phi_{-N}(y) is trapped in O_{K_V}; (2) gives

\[
 y\in\bigcup_{V\in V_{\rm collection}}\bigcup_{N\ge0}
                 \Phi_N(N_{K_V}).
\]

This union is countable and null. This step does not require a countable family of periodic orbits.

## 7. Completion

By H6 almost every initial point has one of the limits just treated. Bad limiting objects have null backward basins. At every remaining such point W=0. Therefore W=0 almost everywhere and, by continuity, everywhere. Since U is curl-free and divergence-free, its components are entire harmonic functions. The harmonic interior gradient estimate on balls of radius R bounds |DU(x)| by a constant times sup_{B_R(x)}|U|/R; uniform sublinearity makes this tend to zero. Hence U is constant, and decay makes the constant zero.

## Audit result

The extension from sampled periodic points to a single continuous periodic alpha-limit set is valid. The claim remains conditional. In particular this proof does not classify general recurrent sets, equilibrium continua, heteroclinic networks or chaotic alpha-limit sets. It cannot by itself prove the main rotating conjecture.

# Discounted Bernoulli identities and the size of Weber actions

This independently checks CORE_WEBER, including the pressure normalization, past completeness and the constants needed for a pressure-action contradiction. The exact identities are confirmed. A new pressure estimate excluding a sign-changing basin is not supplied.

## 1. Exact statement without a far-field derivative condition

Fix \(0<c<1/2\) and \(\omega\in\mathbb R\). Let \(U\in C^1(\mathbb R^3;\mathbb R^3)\), \(P\in C^1(\mathbb R^3)\) solve

\[
\operatorname{div}U=0,\qquad
(1-c)U+(B\cdot\nabla)U+\omega JU+\nabla P=0,
\quad B=Ay+U,\quad A=cI-\omega J,
\]

where \(Jy=(-y_2,y_1,0)\). Suppose \(U(y)=o(|y|)\) uniformly. Put

\[
a=1-2c>0,\quad q=|U|^2/2,\quad
H=P+q+(Ay)\cdot U,\quad g=U\cdot B,
\quad\Phi_t=\operatorname{Fl}^B_t,\quad\Psi_t=\Phi_{-t}.
\]

Then both flows are complete. For every \(y\),

\[
H(y)=a\int_0^\infty e^{-as}(P-q)(\Psi_s y)\,ds.                 \tag{1}
\]

This integral converges absolutely. For every compactly supported probability \(\nu\) invariant under the entire carrier flow,

\[
\int H\,d\nu=\int(P-q)\,d\nu,\qquad \int g\,d\nu=0.         \tag{2}
\]

No pressure normalization or Dini condition is needed for (1)-(2). The constants bounding a single orbit need not be uniform over all \(y\). The formula is covariant under \(P\mapsto P+C\), \(H\mapsto H+C\).

### Proof

Uniform sublinearity gives at most linear growth of the locally Lipschitz vector field \(B\), so no finite-time escape occurs. For all sufficiently large \(|y|\),

\[
B(y)\cdot y=c|y|^2+U(y)\cdot y\ge(c/2)|y|^2.
\]

Thus each sufficiently large closed ball is forward invariant under \(\Psi\). Each backward carrier orbit is contained in one such ball, including its initial point. Consequently every continuous function is bounded on the closure of that orbit.

The pointwise Lamb identity follows already at \(C^1\):

\[
\nabla H=-aU-(\operatorname{curl}U)\times B.
\]

Indeed, subtracting the momentum equation from the derivative of the definition of \(H\) leaves \(A^TU-\omega JU=cU\) and \((DU^T-DU)B=-(\operatorname{curl}U)\times B\). Dotting with \(B\), and using \(H-g=P-q\), gives

\[
B H+aH=a(P-q).                                               \tag{3}
\]

Integrate (3) on \([-T,0]\) along \(\Phi_s y\):

\[
H(y)-e^{-aT}H(\Psi_Ty)
=a\int_0^T e^{-as}(P-q)(\Psi_s y)\,ds.
\]

The boundary term tends to zero because the past orbit is bounded and \(a>0\). The same boundedness gives absolute convergence. This proves (1). On the compact invariant support of \(\nu\), the integrand has a uniform integrable bound, so invariance and Fubini give (2).

Equation (1) also proves uniqueness of the continuous solution of (3) among functions bounded on each past orbit. The difference satisfies \(F(\Psi_t y)=e^{at}F(y)\), which is bounded as \(t\to\infty\) only when \(F(y)=0\). The positive probability weight in (1) places \(H(y)\) between the infimum and supremum of \(P-q\) on that past orbit. It supplies no sign unless that pressure excess has a sign or another quantitative bound.

## 2. Additional hypotheses for the two-sided and forward actions

For the remainder assume \(U\in C^2\), \(U(y)\to0\) uniformly, \(2/5<c<1/2\), and the additional condition

\[
\int_1^\infty\sup_{|y|\ge r}|DU(y)|\,\frac{dr}{r}<\infty.       \tag{D}
\]

Take exactly the canonical pressure \(P=P_{\rm can}\), whose limit at infinity is zero. Write \(k=(1-c)/c\in(1,3/2)\), so \(a=c(k-1)\), and \(d=\|U\|_\infty/c\). The already confirmed scattering and pressure results give the following precise inputs:

* A continuous map \(S\), \(|S(y)-y|\le d\), and a compact null invariant set \(K=S^{-1}(0)\). Off \(K\), \(S\) is a \(C^1\) volume-preserving diffeomorphism onto \(\mathbb R^3\setminus\{0\}\), with \(S\Phi_t=e^{tA}S\).
* A continuous twisted homogeneous tail \(V\), of norm degree \(-k\), with \(U=V+o(|y|^{-k})\), and \(|\Phi_t y-e^{tA}S(y)|\le d\) for \(t\ge0\).
* \(|H(y)|\le C(1+|y|)^{1-k}\), \(|P(y)|+q(y)\le C(1+|y|)^{-2k}\log(2+|y|)\).
* With \(\tau(z)=(Az)\cdot V(z)\) and \(\kappa=\tau\circ S\),
  \(e^{at}H(\Phi_t y)\to\kappa(y)\) at every \(y\notin K\).

The letter \(\kappa\) denotes a scalar coefficient here, not the vorticity contraction exponent \(1+c\) used in other results.

For \(y\notin K\), define

\[
K_{\rm act}(y)=\int_0^\infty e^{as}q(\Phi_s y)\,ds,\qquad
\Pi(y)=\int_0^\infty e^{as}P(\Phi_s y)\,ds.
\]

Both integrals converge absolutely, \(K_{\rm act}\ge0\), and

\[
K_{\rm act}(y)+|\Pi(y)|\le C|S(y)|^{1-k}.                      \tag{4}
\]

Moreover,

\[
\phi=K_{\rm act}-\Pi=\frac{H-\kappa}{a},                     \tag{5}
\]

\[
\kappa(y)=a\int_{-\infty}^{\infty}
 e^{as}(P-q)(\Phi_s y)\,ds.                                  \tag{6}
\]

The last integral is absolutely convergent on both half-lines.

### Proof of the bounds and limits

Set \(s_0=|S(y)|>0\), \(R_0=2(d+1)\), and
\(t_e=\max(0,c^{-1}\log(R_0/s_0))\). Up to \(t_e\), the boundedness of \(q\) and \(P\) yields a bound \(C s_0^{1-k}\) if \(s_0<R_0\); the interval is empty otherwise. For \(s\ge t_e\),

\[
|\Phi_s y|\ge e^{cs}s_0-d\ge e^{cs}s_0/2\ge1.
\]

Substitution \(r=e^{cs}s_0\) bounds the remaining absolute integral by

\[
C s_0^{-a/c}\int_{\max(R_0,s_0)}^\infty
 r^{a/c-2k-1}\log(2+r)\,dr
\le C s_0^{1-k}.
\]

Here \(a/c-2k-1=-k-2<-1\), and extending the lower limit down to \(R_0\) gives the uniform constant. This proves (4). For each fixed starting point the late-time integrand is also \(O_y((1+s)e^{-s})\), because \(a-2(1-c)=-1\).

Integrating (3) from zero to \(t\) and using the stated limit gives
\(\kappa-H=a(\Pi-K_{\rm act})\), proving (5). Integrating from \(-T\) to \(t\), then sending both endpoints to infinity, proves (6). Past convergence uses boundedness on the past orbit; future convergence uses (4).

The pressure normalization is indispensable for (4)-(6). If a nonzero constant \(C\) is added to \(P\), the forward weighted integral of that constant diverges. For an arbitrary pressure representative these formulas use \(P-p_\infty\) and \(H-p_\infty\). Formula (1) itself remains valid with the arbitrary representative.

## 3. Vortex arcs and exactly what a contradiction would require

Let \(W=\operatorname{curl}U\), \(h=U\cdot W\), and \(\eta=(V\cdot\operatorname{curl}V)\circ S\). The confirmed scattering identities give, off \(K\),

\[
WH=-ah,\quad W\kappa=-a\eta,\quad
B\kappa=-a\kappa,\quad
U=DS^T(V\circ S)-\nabla\phi.                                 \tag{7}
\]

Thus \(B\phi=\kappa-g\) and \(W\phi=\eta-h\). These are literal differences of the identities for \(H\) and \(\kappa\).

Consider a vortex arc \(\gamma:(\sigma_-,\sigma_+)\to\mathbb R^3\setminus K\), \(\gamma'=W(\gamma)\), with finite parameter interval and endpoints in \(K\). Assume this arc has the properties supplied by the separately confirmed almost-everywhere arc theorem. It extends continuously to its endpoints, so its image is compact and \(h\) is bounded there. Therefore

\[
\int_{\sigma_-}^{\sigma_+}h(\gamma(\sigma))\,d\sigma
=\frac{H(\gamma(\sigma_-))-H(\gamma(\sigma_+))}{a}
\]

is absolutely convergent. On compact subarcs, the analogous formula for \(\eta\) is the endpoint difference of \(\kappa/a\). If \(\eta>0\) on the arc and the normalized angular coefficient of \(\tau\) has finite nonzero limits at both ends, then \(|\kappa|\to\infty\) there. Strict decrease forces the signs to be \(+\infty\) at entry and \(-\infty\) at exit: the opposite sign at either endpoint would contradict monotonicity against any interior finite value. Hence \(\int\eta=+\infty\) and \(\phi\) goes from \(-\infty\) to \(+\infty\). Nonzero angular limits are additional hypotheses, not consequences of the arc theorem.

The exact action relation is

\[
a\Pi=aK_{\rm act}-H+\kappa\ge\kappa-H
\ge\kappa-\|H\|_\infty.                                     \tag{8}
\]

It is compatible with (4) and with \(\phi=-\kappa/a+O(1)\). For example, along a sequence with \(\kappa\to+\infty\), an independent bound
\(\limsup a\Pi/\kappa<1\) would contradict (8). A bound merely saying \(\Pi\le\kappa/a-\epsilon\) with some unspecified fixed \(\epsilon>0\) need not contradict it: the gap has to beat the relevant bound for \(H/a\). A sufficient additive version is \(a\Pi\le\kappa-\|H\|_\infty-\epsilon\).

The elementary scalar choices \(\kappa_n=n\), \(H_n=1\), \(K_{{\rm act},n}=0\), and \(\Pi_n=(n-1)/a\) satisfy (5), (8), nonnegativity and the corresponding order bounds while having a fixed deficit below \(\kappa_n/a\). This tests an inference between inequalities only; it is not an Euler construction.

Likewise a statement that the Weber route is impossible in every strengthened form is not proved. What is established is that the present identities are algebraically redundant, their proved orders are compatible, and no pressure estimate with the needed strict constant is available here. The suggestion about shadowing a core orbit is expressly heuristic until a uniform error relative to the exponentially weighted exit term is controlled.

## Dependencies and verification

The local Lamb identity, completeness, integration and all constants were reconstructed in this proof without numerical computation. The additional scattering inputs are A209-A210, A274, A295-A296, A302 and A354-A355, not assumptions derived anew here. Their exact source passages and the complete CORE_WEBER text were reread and copied into in the team records; hashes record the inspected versions. No whole-campaign or unrestricted C2 nonexistence is inferred. Existing configured-model Theory Agent A  exposition is the submission being checked; no extra model or provider attestation is claimed.

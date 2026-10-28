# Conditional injectivity certificates

## Statement and scope

The operator, spaces, and qualitative Fredholm properties are those in `../../question.md`. The results below are abstract sufficient conditions and explicit estimates for a regular cylinder chart. The supplied data do not establish their quantitative hypotheses for the full Taylor-subtracted, weighted operator. In particular, no numerical inverse bound or actual proof of injectivity is asserted.

Use the sign determined by `-Delta psi = partial_x h`, `U = (-partial_y psi, partial_x psi)`. Its principal coupling symbol is `g_1 nu_1 nu_2 - g_2 nu_1^2`, where `g = grad rho`.

## 1. Finite adjoint certificate

Let \(F:H\to H\) be bounded and Fredholm of index zero on a Hilbert space. Suppose
\[
m\|u\|\leq\|Fu\|+\|Ku\|,\qquad K:H\to H_0,
\]
and \(K=K_S+E\Phi^*\), where \(\|K_S\|\leq\delta\) and \(E:\mathbb R^n\to H_0\) is an isometry. Write \(\Phi a=\sum_i a_i\phi_i\). Given \(W:\mathbb R^n\to H\), \(Wa=\sum_i a_i\psi_i\), suppose
\[
\|W\|\leq\Psi,\qquad\|F^*W-\Phi\|\leq\epsilon.
\]
If \(d=m-\delta-\epsilon>0\), then
\[
\|F^{-1}\|\leq (1+\Psi)/d.
\]

Indeed,
\[
\begin{aligned}
(m-\delta)\|u\|
&\leq \|Fu\|+\|\Phi^*u\|\\
&\leq \|Fu\|+\|W^*Fu\|+\|(\Phi^*-W^*F)u\|\\
&\leq(1+\Psi)\|Fu\|+\epsilon\|u\|.
\end{aligned}
\]
This gives injectivity and a lower bound. Index zero then gives surjectivity. Individual residual bounds imply
\(\epsilon\leq(\sum_i\|F^*\psi_i-\phi_i\|^2)^{1/2}\); the operator norm can be substantially smaller.

For the question, one possible realization is \(F=L_{\rm red}T^{-1}\) on \(H=Y\). Then
\[
\|L_{\rm red}^{-1}\|_{Y\to Z}
\leq \|T^{-1}\|_{Y\to Z}(1+\Psi)/d.
\]
The initial weak-coercivity certificate for this \(F\) must be established. Its constant is not automatically the remainder-space margin \(m_a\).

For example, without a jet or bordering term, if \(L=T+C\), \(\|C\|_{H\to H}\leq b\), and
\(m_0\|h\|\leq\|Lh\|+\|K_0h\|\), putting \(u=Th\) gives
\[
\frac{m_0}{m_0+b}\|u\|
\leq\|LT^{-1}u\|+
\frac{b}{m_0+b}\|K_0T^{-1}u\|.
\]
Proof: \(\|u\|\leq\|Lh\|+b\|h\|\), followed by substitution of the weak estimate. The jet row and graph-bounded functionals require their own quantitative bounds.

## 2. Explicit Fourier commutator estimate

Work on a torus of lengths \(\ell\) and \(2\pi\), with frequency lattice
\(\Gamma_\ell=\{(2\pi j/\ell,n):j,n\in\mathbb Z\}\). Fourier coefficients use normalized area measure. Let \(Q_\Lambda\) retain frequencies \(|p|\geq\Lambda\).

Let \(M\) be a scalar or matrix Fourier multiplier, with
\[
\sup_{\Gamma_\ell}\|M(p)\|\leq M_0,\qquad
\|\nabla M(p)\|\leq M_1/|p|\quad (|p|\geq\Lambda/2).
\]
The derivative bound is required on the continuous interpolation used in the next argument. Define \(S_1(a)=\sum_q |q||\widehat a(q)|\). Then
\[
\|[a,M]Q_\Lambda\|
\leq\frac{\max(2M_1,4M_0)}{\Lambda}S_1(a).
\]

To prove this, the Fourier matrix entry from \(p\) to \(p+q\) is
\(\widehat a(q)(M(p)-M(p+q))\). For \(|q|\leq\Lambda/2\), the segment stays at radius at least \(|p|/2\), so the multiplier difference is bounded by \(2M_1|q|/\Lambda\). For \(|q|>\Lambda/2\), use \(2M_0\leq4M_0|q|/\Lambda\). The convolution inequality on \(\ell^2(\Gamma_\ell)\) proves the claim.

A sharper variant, useful when low Mellin modes have large multipliers, is
\[
\|[a,M]Q_\Lambda\|
\leq \frac{2M_1}{\Lambda}S_1(a)
2M_0\sum_{|q|>\Lambda/2}|\widehat a(q)|.
\]
The final sum is at most \((2/\Lambda)^p S_p(a)\), where \(S_p(a)=\sum_q|q|^p|\widehat a(q)|\).

For an explicit derivative-only bound put
\[
D_{ij}=\|\partial_t^i\partial_\theta^j a\|_\infty,
\]
\[
\mathcal D_3(a)^2=
D_{10}^2+D_{01}^2+
2(D_{20}^2+2D_{11}^2+D_{02}^2)+
D_{30}^2+3D_{21}^2+3D_{12}^2+D_{03}^2.
\]
Then
\[
S_1(a)\leq C_\ell\mathcal D_3(a),\qquad
C_\ell^2=\sum_{q\in\Gamma_\ell}(1+|q|^2)^{-2}
\leq1+\frac\pi2+\frac{3\ell}{4}.
\]
The first inequality is Cauchy--Schwarz with weights \((1+|q|^2)^{-1}\), followed by Parseval and normalized \(L^2\leq L^\infty\). For the lattice bound, set \(h=2\pi/\ell\). Summation of the decreasing function in the first coordinate is bounded by its central value plus its real integral:
\[
\sum_j(1+h^2j^2+n^2)^{-2}
\leq(1+n^2)^{-2}+\frac{\pi}{2h}(1+n^2)^{-3/2}.
\]
Summing in \(n\) and applying the same integral bound gives
\(\sum_n(1+n^2)^{-2}\leq1+\pi/2\) and
\(\sum_n(1+n^2)^{-3/2}\leq3\), as required.

This is a regular-chart result. Localization, periodization, singular angular weight conjugation, radial weight transitions, and Taylor subtraction are additional errors, not covered by this statement.

## 3. An explicit principal Gårding estimate

Let \(g=(g_1,g_2)\), let \(R_\theta\) be the rotation from the radial/angular frame to the Cartesian frame, and set
\[
B=R_\theta^{T}
\begin{pmatrix}-g_2&g_1/2\\g_1/2&0\end{pmatrix}R_\theta.
\]
Its largest eigenvalue is \(b_+=(|g|-g_2)/2\). Let \(S_j\) be the self-adjoint multiplier \(p_j/|p|\), set to zero at \(p=0\), and
\(C_{\rm pr}=\sum_{ij}B_{ij}S_iS_j\).
For \(\eta>0\), set
\[
b_\eta=(\sqrt{|g|^2+\eta^2}-g_2)/2.
\]
For a vector \(v=Q_\Lambda v\),
\[
\operatorname{Re}\langle C_{\rm pr}v,v\rangle
\leq\int b_+|v|^2+
\left[
\frac{\eta}{2}
+\frac4\Lambda\left(\sum_{ij}S_1(B_{ij})+2S_1(b_\eta)\right)
\right]\|v\|^2.
\]

Indeed, \(\sum_{ij}S_iB_{ij}S_j\) has quadratic form at most
\(\sum_j\langle b_\eta S_jv,S_jv\rangle\). Commuting each \(S_i\) through \(B_{ij}\) costs at most \(4S_1(B_{ij})/\Lambda\). Commuting each \(S_j\) through \(b_\eta\), and using \(\sum_jS_j^2v=v\), costs at most \(8S_1(b_\eta)/\Lambda\). Finally \(0\leq b_\eta-b_+\leq\eta/2\). The commutator lemma applies with \(M_0=M_1=1\).

Regularization is necessary for the displayed derivative bound: \(b_+\) need not have three derivatives where \(g=0\). All derivatives of \(b_\eta\), including their dependence on \(\eta\), must be included.

## 4. Exact homogeneous multipliers and a radial error bound

Away from resonances, for \(h=r^\lambda e^{in\theta}\), set
\[
A_+(\lambda,n)=\frac{\lambda-n}{\lambda+n+2},
\qquad A_-(\lambda,n)=\frac{\lambda+n}{\lambda-n+2}.
\]
The physical sign convention above gives
\[
U_xh=\frac{r^\lambda}{4i}
\big(A_+e^{i(n+2)\theta}-A_-e^{i(n-2)\theta}\big),
\]
\[
U_yh=-\frac{r^\lambda}{4}
\big(A_+e^{i(n+2)\theta}+2e^{in\theta}+A_-e^{i(n-2)\theta}\big).
\]
To verify these identities, first compute
\[
\partial_xh=\tfrac12r^{\lambda-1}
\big((\lambda-n)e^{i(n+1)\theta}+(\lambda+n)e^{i(n-1)\theta}\big)
\]
and solve the two scalar Laplacian equations. A particular solution is
\[
\psi=-\tfrac12r^{\lambda+1}
\left(\frac{e^{i(n+1)\theta}}{\lambda+n+2}
+\frac{e^{i(n-1)\theta}}{\lambda-n+2}\right).
\]
Differentiation gives the displayed formulas. The choice of harmonic additions and the treatment of poles must agree with the actual renormalized operator; the formulas alone do not specify that choice.

For \(\lambda=\sigma+i\xi\), \(p=(\xi,n)\), and \(|p|>|\sigma+2|\), comparison with
\(A_\pm^0=(i\xi\mp n)/(i\xi\pm n)\) gives
\[
|A_\pm-A_\pm^0|
\leq\frac{2\max(|\sigma+1|,1)}{|p|-|\sigma+2|}.
\]
For the plus sign, the exact numerator of the difference is
\(2((\sigma+1)n-i\xi)\), while the denominator has modulus at least
\(|p|(|p|-|\sigma+2|)\). The minus sign is identical in modulus. The two angular shifts are isometries. Hence
\[
\|(U_\sigma-U_{\rm pr})Q_\Lambda\|_{L^2\to L^2(\text{cylinder};\mathbb R^2)}
\leq\frac{\sqrt2\max(|\sigma+1|,1)}
{\Lambda-|\sigma+2|}.
\]
Multiplication by \(g\) adds the factor \(\|g\|_\infty\).

For the specified weight, the exact isometry to unweighted cylinder measure is
\[
(Jh)(t,\theta)=
e^{-13t/4+(29/8)t_+}|\cos\theta|^{-17/4}h(e^t,\theta).
\]
The radial Mellin lines are therefore \(\sigma=13/4\) inside and \(\sigma=-3/8\) outside. Angular conjugation and the kink at \(t=0\) remain separate. Neither is covered by the radial estimate.

## 5. Finite-dimensional concentration criterion

Let \(A:H\to H\) be bounded and Fredholm of index zero, and \(P\) an orthogonal finite-rank projection, \(Q=I-P\). Suppose \(D=QAQ:QH\to QH\) is bijective and
\[
\|D^{-1}\|\leq d^{-1},\quad
\|PAQ\|\leq b,\quad\|QAP\|\leq c,\quad
\|(PAP)p\|\geq a\|p\|\quad(p\in PH).
\]
If \(s=a-bc/d>0\), then \(A\) is invertible. In fact, for \(Au=f\), \(u=p+q\),
\[
d\|q\|\leq\|Qf\|+c\|p\|,
\qquad
s\|p\|\leq\|Pf\|+(b/d)\|Qf\|.
\]
Consequently, writing \(p_0=\sqrt{1+(b/d)^2}/s\),
\[
\|A^{-1}\|
\leq\sqrt{p_0^2+\big((1+cp_0)/d\big)^2}.
\]
The inequalities follow by solving the \(Q\) equation and applying the lower bound for \(PAP\). They first prove trivial kernel; index zero supplies existence, after which the same inequalities bound the inverse.

For a kernel vector, \(\|q\|\leq(c/d)\|p\|\). A lower bound on the finite subspace alone is insufficient; the complement and cross terms are essential. Apply this only in a bounded realization such as \(A=L T^{-1}\), or with appropriate graph norms. The coercivity constant for its complement is not automatically the original \(m_a\).

## 6. Rank and cost

On a periodic cylinder window of length \(\ell\), the parity class has angular basis \(\sin(n\theta)\), \(n>0\) odd. A disk cutoff has real dimension
\[
N(\Lambda,\ell)=
\sum_{\substack{1\leq n\leq\Lambda\\n\ {\rm odd}}}
\left(2\left\lfloor\frac{\ell}{2\pi}
\sqrt{\Lambda^2-n^2}\right\rfloor+1\right)
=\frac{\ell\Lambda^2}{8}+O(\ell\Lambda+\Lambda).
\]
This counts a model periodic trial space; rigorous localization requires padding and a separate error bound. A Mellin bandlimit on the whole real line has infinite rank.

If the full regularized error has the certified form
\(\delta_{\rm other}+B_{\rm eff}/\Lambda\), and a chosen high-frequency budget is \(m/4\), then the leading dimension estimate is
\(N\approx2\ell(B_{\rm eff}/m)^2\). This is conditional, not a measured rank of the operator.

Ordinary Fourier projection of the raw remainder is not bounded in the specified weighted space: it can destroy the order-four cancellation at the axis. An admissible projection can instead be built as \(J^{-1}PJ\), provided its trial vectors lie in the transport domain, or from axis-vanishing basis functions with their actual weighted Gram matrix. All transformed operator estimates must then be proved.

## Dependencies and open inputs

Only elementary Hilbert-space inequalities, Fourier convolution, Parseval, differentiation of homogeneous functions, and the Fredholm facts explicitly assumed in the question enter the proofs above.

Still needed for the actual problem: quantitative Taylor-subtracted kernel bounds; angular strip and output-tail estimates; control of localization and radial weight transitions; full jet and bordering norms; an actual finite-rank compact-defect approximation; approximate adjoint witnesses with certified residuals; and norm conversion to the specified \(Z\). The given margin is \(0.9659\); the sampled value near \(3.09\) is not a certified global margin.

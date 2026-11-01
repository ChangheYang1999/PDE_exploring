# A rational majorant initialized from a certified finite prefix

Status: PROVED. Independent analytic review of171 and172 was completed by the theory part at2026-10-31T13:01Z. The exact supersolution certificates are confirmed in V325,V326,V330,V332.

A convergent majorant need not reconstruct coefficients that have already been enclosed. Keeping those coefficients as fixed inputs removes repeated overestimation of the same finite part. The remaining harmonic corrections must still be bounded at every later resonance.

## Statement

Assume the hypotheses of 145: coprime integers \(h\ge2\), \(Q>2h\), exponent \(\delta=2h/Q\), finite even bandwidth \(B\), a compatible nonzero leading sine polynomial, and a uniform lower bound \(s>0\) on every tuning response. Fix an integer \(M\ge1\) and put \(N=MQ\). Suppose positive rational bounds have been certified for the actual tuned prefix:

\[
 d_j\ge j\|f_j\|_1\quad(1\le j\le N),\qquad
 e_a\ge aQ|H_{aQ}|\quad(1\le a<M).
\]

Let \(L\) bound every particular Poisson inverse. A valid common nonlinear constant for all subsequent equations is

\[
 \kappa_N=B[2-\delta+\max(\delta,1-\delta)]
             \frac{1-\delta}{\delta}\frac{N+1}{N}.
\]

The original larger constant in 145 also suffices. The polynomial system below has a nonnegative strictly triangular affine part at zero. If its transformed map has a nonnegative supersolution at \(w=w_0>0\), the tuned density, stream, common potential and every appropriately weighted derivative converge on each closed exterior

\[
 r\ge R>w_0^{-1/(2h)}.
\]

The usual amplitude scaling multiplies this sufficient radius by \(|\epsilon|^{Q/(2h)}\). The statement concerns an exterior solution; it asserts neither a sharp radius nor a global stationary extension.

## 1. Scalar continuation after the known prefix

Set \(x_j=d_j\) for \(j\le N\) and \(\eta_{aQ}=e_a\) for \(a<M\). Set all nonresonant harmonic bounds to zero. For each true resonance \(n\ge N\), use the scalar lookahead and harmonic equations of 171. After each base order compute the next density bound by its scalar convolution. All these equations are imposed with equality.

This ordering is triangular. The lookahead equation at \(n+r\) uses density indices at most \(n\), harmonic indices at most \(n-1\), and smaller lookahead indices. The initial bounds refer to the already tuned prefix, so induction gives domination of the actual continuation. No scalar recurrence is required of the supplied \(d_j\) or \(e_a\). The first unknown harmonic is \(H_N\), which first affects density order \(N+1\).

Every newly estimated density or lookahead equation has total order at least \(N+1\). The bound on \(m/(m-1)\) used in 168 is therefore \((N+1)/N\), proving the displayed value of \(\kappa_N\). In bounding \(N|H_N|\) by its obstruction at \(N+Q\), the factor \(N/(N+Q)\le1\) is again discarded safely.

## 2. Residue projections

Write

\[
 P(z)=\sum_{j=1}^{N}d_jz^j,\qquad
 H(z)=\sum_{a=1}^{M-1}e_az^{aQ},\qquad
 H_*(w)=\sum_{a=1}^{M-1}e_aw^a.
\]

Let \(P_{\ge b}\) retain the terms of \(P\) with index at least \(b\). For a polynomial \(F\), define the finite projection

\[
 \mathcal K_r F(w)=\sum_{k\ge0}[z^{N+r+kQ}]F(z)w^k,
 \qquad 1\le r\le Q.
\]

The unknown residue series are

\[
 X_r=\sum_{k\ge0}x_{N+r+kQ}w^k,\quad
 E=\sum_{k\ge0}\eta_{N+kQ}w^k,\quad
 V_r=\sum_{k\ge0}u_{N+kQ,r}w^k\quad(r<Q).
\]

In particular, the density tail is \(\sum_r z^{N+r}X_r(z^Q)\), while the harmonic tail is \(z^N E(z^Q)\).

For \(1\le r\le Q\) put

\[
 D_r=\sum_{i+j=r}X_iX_j,\qquad
 C_r=\sum_{i+j=Q+r}X_iX_j,
\]

where both indices lie in \(\{1,\ldots,Q\}\). Define the known/unknown density product

\[
 S_{r,b}(w,X)=
 \sum_{\substack{b\le i\le N,\ 1\le t\le Q\\
                   i+t-r\in Q\mathbb Z_{\ge0}}}
 d_iX_tw^{(i+t-r)/Q},
\]

and the known density residue polynomial

\[
 T_{r,b}(w)=
 \sum_{\substack{a\ge0\\b\le aQ+r\le N}}d_{aQ+r}w^a.
\]

Then set

\[
 \begin{aligned}
 A_r&=\mathcal K_r(P_{\ge r}^2)+2S_{r,r}
                  +w^M D_r+w^{M+1}C_r,\\
 B_r&=\mathcal K_r(P^2)+2S_{r,1}
                  +w^M D_r+w^{M+1}C_r,\\
 Z_{r,b}&=\mathcal K_r(HP_{\ge b})+H_*X_r+ET_{r,b}+w^MEX_r.
 \end{aligned}
\]

Every expression is a polynomial in \(w\) and the unknown components, with nonnegative coefficients. Projection of the original scalar sums gives

\[
 \begin{aligned}
 V_r&=\kappa_N\left[LA_r+Z_{r,Q+1}
                    +2L\sum_{j=1}^{r-1}d_jV_{r-j}\right],\quad r<Q,\\
 E&=\frac{\kappa_N}{s}\left[LA_Q+Z_{Q,Q+1}
                    +2L\sum_{j=1}^{Q-1}d_jV_{Q-j}\right],\\
 X_r&=\kappa_N[LB_r+Z_{r,1}],\quad 1\le r\le Q.
 \end{aligned}                                                    \tag{1}
\]

Here \(Z_{r,Q+1}\) implements exactly the lookahead restriction that a harmonic factor has density partner at least \(Q+1\). The ordinary density equation has no such restriction and uses \(Z_{r,1}\).

To check the powers, a product of two density tails has degree \(2N+i+j\). Dividing by the projected base degree \(N+r\) gives \(w^M\) when \(i+j=r\), and \(w^{M+1}\) when \(i+j=Q+r\). A known density coefficient times a density tail has exponent difference \(i+t-r\), yielding \(S\). A known harmonic times a density tail gives \(H_*X_r\). An unknown harmonic times a known density coefficient gives \(ET_{r,b}\). The product of the two tails gives \(w^MEX_r\). These four cases exhaust the harmonic product.

## 3. The constant-level map

Order the components as \(Y=(V_1,\ldots,V_{Q-1},E,X_1,\ldots,X_Q)\). Since \(M\ge1\), every tail/tail term vanishes at zero. Also \(H_*(0)=0\). In a lookahead equation, \(S_{r,r}\) has positive \(w\) degree: its known index is at least \(r\), while its unknown residue is positive. The polynomial \(T_{r,Q+1}\) also vanishes at zero. Thus the \(V\) rows depend only on earlier \(V\) rows, and the \(E\) row depends only on \(V\).

In the density row, the constant term of \(S_{r,1}\) uses only residues \(t<r\). The remaining unknown constant term is \(Ed_r\). Consequently the constant-level map is \(c+JY\) with nonnegative strictly lower triangular \(J\). Its inverse \(T=(I-J)^{-1}\) is nonnegative. Put \(Y_0=Tc\) and

\[
 G(w,Y)=Y_0+T\bigl(\Phi(w,Y)-\Phi(0,Y)\bigr).
\]

Every nonconstant term has positive \(w\) degree. If \(b\ge Y_0\) and \(G(w_0,b)\le b\), monotone iteration from zero gives the unique formal solution, coefficient by coefficient, and bounds each component's coefficient sum at \(w_0\). Hence the scalar sequence has geometric base \(w_0^{-1/Q}\). Domination proves the same bound for the tuned coefficients. The angular support and potential argument in 145 then prove all stated convergence conclusions.

When \(M=1\), the known harmonic polynomial is zero and (1) reduces exactly to 171. This special case and direct total-order scalar sums provide independent checks of the residue formulas. The finite-prefix norm bounds remain necessary certificate inputs; no observed finite decay replaces the infinite response hypothesis.

## Completed verification

Nine generic cases cover three exponent pairs and prefix lengths M=1,2,3. Three exact M=1 comparisons reproduce171's constant, Jacobian, initial fixed point and polynomial map. Direct total-order scalar calculations confirm378 coefficient identities. Five choices N=9,18,27,45,90 for the independently certified largest two-mode4/9 profile confirm270 further identities. Every exact box passes and its adjacent dyadic box fails.

Using the old response lower bound s=1, the five choices give w-exponents171,131,131,131,130. The N90 certificate therefore gives the proposed sufficient radius2^(65/2), pending independent review of this theorem. The generic batch took2.072913067881018 seconds; the actual-prefix batch took4.41490946803242 seconds. All norm inputs are upward-rounded rational bounds from167's3072-bit enclosure, including the wider printing intervals of the exported values. No later response estimate is inferred from the finite prefix.

## Independent review closure

The theory part independently rederived the scalar domination, every residue projection and the constant-level triangularity at2026-10-31T13:01Z. All exact boxes already passed. The earlier pending status above records the audit chronology; the theorem and these sufficient radii are now PROVED. The167 root interval is propagated through every Cartesian operation and every computed harmonic without a midpoint reset. Thus its prefix bounds contain the exact uniquely tuned coefficients at the exact algebraic root. The65-digit export bounds are treated as enclosing intervals before upward rational rounding.

# Independent audit of the four-component closure proposal

## Scope and dependencies

This checks the equations and generator argument of T1's graded closure proposal, frozen in `source/T1_model_v01.md`, Section 4. The source and Analysis II excerpts are hashed in `verification/source_hashes.txt`. The resulting conditional theorem below makes the low-level feedback condition explicit. The numerical optimization in T1's script is not taken as a proof of a global optimum.

Use real S1 functions, even in x and odd in y, with canonical velocity \(U=(-R_1R_2,R_1^2)\), \(R_j=\partial_j(-\Delta)^{-1/2}\). Let \(H=\dot H^{-1}\) be the completion of the smooth compact S1 core. Define

\[
\omega=(1+4|X|^2)^{2/5},\qquad J=(1-\Delta)^{1/2},
\]
\[
(P,a,b,H)(h)=\big(\|\omega D^2J^sh\|_2,\|DJ^sh\|_2,
\|J^sh\|_2,\|J^sh\|_{\dot H^{-1}}\big).
\tag{1}
\]

Here H in a tuple denotes the fourth scalar component. The ambient Hilbert space X is the completion for the square sum of these four components; it is equivalent to the baseline Ns space with weights 1, 2^14, 2^18 and 2^18(20/21). All derivatives are full ordered tensors.

The reference is smooth, has the canonical sublinear velocity and satisfies the structural, normalization and coefficient hypotheses of Analysis II P7.5 and P8.4. In particular, the base separate energy inequalities are

\[
\mathcal D_H\ge(19/5)H^2,\quad
\mathcal D_0\ge(11/4)b^2-H^2,\quad
\mathcal D_1\ge(9/10)a^2-6ab,
\]
\[
\mathcal D_2\ge(1/2)P^2-(347/5)aP-10bP-40a^2,
\tag{2}
\]

and the ordered component-sum coefficient bounds are

\[
(C,U_1,U_2,U_3,R_1,R_2,R_3,R_4)\le(2,6,24,160,22,32,80,2048).
\]

These hypotheses must be checked for the actual reference. Write \(Lh=(cX+U[\bar\rho])\cdot Dh-h+U[h]\cdot D\bar\rho\) and \(A_k=L+U[k]\cdot D\). Suppose \(c+c[\bar\rho]=1\), \(a_0=\bar\rho_y(0)\ne0\), and take the fixed-exponent chart.

## Conditional theorem

Choose \(0<s\le1/1024\) and positive radii \(r=(r_2,r_1,r_0,r_H)\). Set

\[
n=(r_2^2+2r_1^2+r_0^2)^{1/2},\quad \nu=n/\sqrt s,
\quad A_s=127/50+(653/5)s,\quad B_s=(9/5)(1+44s),
\]
\[
m_H=19/5-2s,\quad m_0=11/4-3882s-(3/10)\nu,
\]
\[
m_1=9/10-4290s-(13/10)\nu,\quad
m_2=1/2-4708s-(A_s+B_s)\nu,
\]
\[
q_0=476s+\nu,\quad \kappa=q_0/m_H,\quad
\alpha=347/5+5440s+B_s\nu,\quad \beta=10+34816s.
\tag{3}
\]

Assume every m is positive and

\[
q_0<m_H\sqrt{m_0}.
\tag{4}
\]

For a nonnegative forcing bound \(\phi=(\phi_2,\phi_1,\phi_0,\phi_H)\), define

\[
\Gamma_0=\frac{\phi_0/m_0+\phi_H/(m_H\sqrt{m_0})}
 {1-\kappa/\sqrt{m_0}},\qquad
\Gamma_H=\phi_H/m_H+\kappa\Gamma_0,
\]
\[
\Gamma_1=\frac{\phi_1+(6+1360s)\Gamma_0}{m_1},
\]
\[
\Gamma_2=\frac{\phi_2+\alpha\Gamma_1+\beta\Gamma_0}{m_2}
 +\sqrt{40/m_2}\,\Gamma_1.
\tag{5}
\]

For every k in the component box, A_k is bijective from its maximal distributional X-domain to X. Its inverse obeys \(e(A_k^{-1}f)\le\Gamma\) whenever \(e(f)\le\phi\). Here the vector order is componentwise.

Let F be the actual reference residual. If \(e(F)\le\phi\), \(\Gamma\le r\), and

\[
d=\frac{n}{2\sqrt{\pi s(1+s)}}<19/10,
\tag{6}
\]

then exactly one h in the component box with c[h]=0 solves \(F(\bar\rho+h;c)=0\). The exponent is fixed. Positive corrected origin slope follows if \(d<a_0\), and the leading tail is preserved under the baseline tail hypothesis.

The feedback condition (4) is essential to this sufficient proof. Positivity of the four diagonal margins alone does not establish the asserted inverse. T1's numerical gamma_map already tests (4), through its positive denominator.

## 1. Background component estimates

The P8.4 table bounds each output norm of \([J^s,L]J^{-s}\), not only the sum of its energy contributions. Its unscaled rows give, after taking the inner product with the corresponding component,

\[
s(4708P+5440a+34816b)P,
\quad s(4290a+1360b)a,
\quad 3882s b^2,
\quad s(2H+476b)H.
\tag{7}
\]

For example, the top diagonal is \(6C+28U_1+166U_2+17R_2=4708\). The top-to-gradient coefficient is \(17U_3+34R_3=5440\). The H row uses exact divergence identities and does not require bounded multiplication by the growing reference density. No symmetric-matrix aggregation into the scalar constant 4800 is needed at this stage.

## 2. Rough transport: dependence on the component box

By the Fourier identity for the Bessel norm and \(\omega\ge1\),

\[
\|k\|_{H^{2+s}}^2
=\|J^sk\|_2^2+2\|DJ^sk\|_2^2+\|D^2J^sk\|_2^2
\le b_k^2+2a_k^2+P_k^2\le n^2.
\tag{8}
\]

For W=U[k], the vector multiplier has norm at most one. Thus \(\|W\|_{H^{2+s}}\le n\), \(\|DW\|_\infty\le c_sn\), where \(c_s=[2\sqrt{\pi s(1+s)}]^{-1}\). Also \(\|DW\|_{H^{1+s}}\le n\). The centrally odd weighted Riesz estimate gives

\[
\|\omega J^sD^2W\|_2\le(9/5)P_k\le(9/5)n.
\tag{9}
\]

These are all occurrences of the rough input k in P8.1/P8.4. The factors 128 and 512 from the scalar energy do not enter (8) or (9).

For the output h, write g=J^sh. The first three terms in the differentiated rough transport cost at most \(A_s\nu P^2\). In the last term, the product estimate of P8.1 has factors

\[
\|Dh\|_{H^{1+s}}\le(P^2+a^2)^{1/2}\le P+a,
\qquad \|\omega J^sD^2W\|_2\le(9/5)n.
\]

It therefore costs at most \(B_s\nu(P+a)P\). This yields the top rough contributions in (3). The gradient and L2 costs are at most \((13/10)\nu a^2\) and \((3/10)\nu b^2\), respectively, by the same unweighted transport commutator and product bounds.

For the fourth row, use incompressibility before estimating:

\[
J^s(W\cdot Dh)=\operatorname{div}J^s(Wh),
\]
\[
\|J^s(Wh)\|_2
\le s^{-1/2}\|W\|_{H^{1+s}}\|h\|_{H^s}
\le\nu b.
\tag{10}
\]

Pairing with \(( -\Delta)^{-1}g\) costs at most \(\nu bH\). This checks the H row not yet verified in T2's reply to T1. It uses the stated product estimate, not a hypothetical estimate of fractional multiplication by a merely bounded W.

Combining (2), (7) and (8)-(10) yields exactly

\[
m_H H\le\phi_H+q_0b,
\quad m_0b^2\le\phi_0b+H^2,
\]
\[
m_1a\le\phi_1+(6+1360s)b,
\quad m_2P^2\le(\phi_2+\alpha a+\beta b)P+40a^2.
\tag{11}
\]

If a divided component vanishes the resulting bound is automatic. Initially these are smooth-core inequalities.

## 3. Positive auxiliary energy and generator realization

This fills in the qualitative inverse step. Since q0>0, take

\[
t=2m_0m_H/q_0^2.
\]

The low quadratic form

\[
Q_\mathrm{low}=m_0b^2+(tm_H-1)H^2-tq_0bH
\]

has determinant \(m_0(m_0m_H^2/q_0^2-1)>0\) and positive first diagonal by (4). Hence for some \(\ell>0\), \(Q_\mathrm{low}\ge\ell(b^2+H^2)\).

Put \(c_1=6+1360s\). Take

\[
M=(41+\alpha^2/m_2)/m_1,
\qquad L=(1+\beta^2/m_2+(Mc_1)^2/2)/\ell.
\]

For the auxiliary squared norm

\[
E_*^2=P^2+Ma^2+L(b^2+tH^2),
\]

use \(\alpha aP\le(m_2/4)P^2+(\alpha^2/m_2)a^2\), the analogous bound for beta bP, and \(Mc_1ab\le a^2/2+(Mc_1)^2b^2/2\). The homogeneous versions of (11) then imply

\[
-\operatorname{Re}\langle A_kh,h\rangle_{E_*}
\ge(m_2/2)P^2+a^2/2+b^2+H^2\ge\delta E_*^2,
\]

where \(\delta=\min\{m_2/2,1/(2M),1/L,1/(Lt)\}>0\).

E_* is equivalent to the original Ns norm. P8.1's construction therefore applies: smooth approximation of k, uniform energy bounds, convergence of the linear solutions in L2, weak compactness in X and strong continuity give the limiting semigroup. Strictness of (3)-(4) supplies the same positive auxiliary decay for a slightly enlarged box, so smooth approximants need not lie exactly inside the original box. The complete Lipschitz transport field and bounded L2 coupling identify the maximal distributional domain; the same semigroup is restricted to X. Integrating its exponentially decaying orbit proves both inverse identities.

For smooth approximants and smooth forcing, (11) applies to the inverse image. Solve its second inequality using \(b\le\phi_0/m_0+H/\sqrt{m_0}\), combine with the first and (4), and then use the third. The positive root of the fourth is bounded by \((\phi_2+\alpha a+\beta b)/m_2+\sqrt{40/m_2}\,a\). This proves (5). Approximate the forcing in X and k in a slightly enlarged box. The uniform inverse bound, L2 resolvent convergence, weak lower semicontinuity of each component and continuity of Gamma pass (5) to the maximal-domain inverse. This avoids assuming that individual formal energy expressions are separately defined for every rough X element.

## 4. Nonlinear and normalization steps

Define \(T(k)=-A_k^{-1}F\) on the component box with c[k]=0. Equation (5) and Gamma<=r make it invariant. The origin identity is

\[
(A_kh)_y(0)=c[k]h_y(0)+a_0c[h],
\]

because the background is exactly normalized. Since F_y(0)=0, the inverse image has c[h]=0. The continuous trace is available by (8) and s>0.

The difference identity is \(A_k(T(k)-T(l))=-U[k-l]\cdot DT(l)\). The existing low inverse bound and stream-function divergence estimate give Lipschitz constant \(d/(19/5-d)<1\) in H by (6). The common low-domain justification is unchanged: the high semigroup is the L2 realization, and the H extension agrees on their common dense core. The component box is a bounded, closed convex subset of X. A sequence in it converging in H has, by weak compactness, its unique distributional limit in that box; the continuous strain functional preserves c=0. The box is complete in H. The contraction theorem proves the stated nonlinear conclusion.

## 5. Independent rational certificate

The independent script `code/check_box.py` uses Arb256 and the exact data

\[
s=1/50000,\qquad r=(1/5000,1/3000000,1/50000000,1/30000000),
\]
\[
\phi=(25/1572864,25/201326592,25/805306368,205/6442450944).
\]

All four diagonal margins, the feedback denominator and the four self-map slacks are positive. The output Gamma is approximately

\[
(1.78599131\,10^{-4},\ 2.99436379\,10^{-7},\
1.69591428\,10^{-8},\ 8.61590044\,10^{-9}),
\]

and the low contraction ratio is below 0.003331. These decimals are orientation only; the directed enclosures are in `verification/rational_box.json`. The script also exhibits positive auxiliary weights, using t=1 and low matrix floor 5/2 for this particular box.

This is a valid sufficient forcing box with each component at least 25 times the corresponding old single-component bound. The s values differ, and no candidate's forcing vector has been placed in this box. T1's optimized scalar directions with three zero components are sensitivities of the comparison system; most cannot be nonzero actual functions, since a zero L2 or H norm forces the function to vanish. They must not be reported as realized residual profiles or certified global optima.

# A global helicity constraint on vortical carrier equilibria

Status: CONFIRMED A428 after the focused configured-model challenge. This is an elementary consequence of A413, whose full proof has been reread. It selects local jets that could occur in the global helicity-free problem; it is not a local Euler identity without those global premises.

## Exact statement

Let \(0<c<1/2\), \(\omega\in\mathbb R\), \(Jy=(-y_2,y_1,0)\), \(A=cI-\omega J\), and \(a=1-2c\). Suppose \(U\in C^2(\mathbb R^3;\mathbb R^3)\), \(P\in C^1(\mathbb R^3)\) solve

\[
\operatorname{div}U=0,\qquad
(1-c)U+(B\cdot\nabla)U+\omega JU+\nabla P=0,
\qquad B=Ay+U.
\]

Assume uniform sublinearity \(U(y)=o(|y|)\) and global zero helicity \(U\cdot W=0\), where \(W=\operatorname{curl}U\). Suppose \(p\) is a vortical carrier zero, and write

\[
B(p)=0,\quad u=U(p),\quad w=W(p)\ne0,\quad
M=DU(p),\quad N=DB(p)=A+M.
\]

Then \(u\ne0\), \(u\cdot w=0\), and there is a real number \(\rho\) such that

\[
N^Tu=\rho u,\qquad Nw=(1+c)w.                                \tag{1}
\]

All three eigenvalues of \(N\), counted with algebraic multiplicity, are real and equal to

\[
1+c,\quad \rho,\quad -a-\rho.                                \tag{2}
\]

No density of \(\{W\ne0\}\), SRB measure, basin coverage, Dini bound or pressure normalization is required. No universal bound on \(\rho\) follows from (1)-(2).

## Proof of the global-to-local implication

Put \(H=P+|U|^2/2+(Ay)\cdot U\) and \(g=U\cdot B\). The equation makes \(P,H\in C^2\), and the Lamb identity gives

\[
\nabla H=-aU-W\times B,\qquad BH=-ag.                         \tag{3}
\]

The vorticity equation at \(p\) is \(Mw=w+\omega Jw\), equivalently \(Nw=(1+c)w\). Differentiating the identically zero helicity in the direction \(w\) gives

\[
0=(Mw)\cdot w+u\cdot DW(p)w=|w|^2+u\cdot DW(p)w.
\]

Hence \(u\ne0\); global helicity also gives \(u\cdot w=0\).

A413 proves \(d(BH)\wedge dH=0\) on \(\{W\ne0\}\) at exactly these \(C^2\), uniform-sublinearity and global-helicity hypotheses. Its input is complete recurrent volume-preserving vortex flow with no periodic vortex orbits, followed by \(C^2\) Sard for the two first integrals \((H,BH)\). The rank step needs no dense-vorticity assumption; that assumption enters only its separate global-primitive step. Thus \(dg\wedge dH=0\) near \(p\).

At \(p\), (3) gives \(\nabla H(p)=-au\ne0\). Direct differentiation, retaining that \(B(p)=0\), gives

\[
\nabla g(p)=M^TB(p)+N^Tu=N^Tu.
\]

Rank at most one now implies \(N^Tu=\rho u\) for some real \(\rho\), proving (1). In a submersion chart for \(H\), the rank identity also yields a local \(C^2\) scalar function \(f\) with \(g=f(H)\), \(f(H(p))=0\) and \(\rho=-a f'(H(p))\). This local function need not extend globally.

The rank identity holds pointwise: H and G=BH are C2, so their differential wedge is continuous.

For (2), the plane \(u^\perp\) is \(N\)-invariant because \(u\cdot Nv=(N^Tu)\cdot v\). It contains the nonzero eigenvector \(w\) with eigenvalue \(1+c\). The induced map on the one-dimensional quotient by this plane has eigenvalue \(\rho\). The remaining eigenvalue of the real two-dimensional restriction is real and is determined by \(\operatorname{tr}N=3c\): it equals \(3c-\rho-(1+c)=-a-\rho\). This argument covers repeated eigenvalues and does not assume diagonalizability.

## The submitted rotating sample fails the global test

The local finite-jet package uses \(c=9/20\), \(\omega=1\), \(u=e_1\), \(w=e_3\), and

\[
M=\begin{pmatrix}-1/3&-2/5&0\\3/5&-2/3&0\\0&0&1\end{pmatrix},
\qquad
N=\begin{pmatrix}7/60&3/5&0\\-2/5&-13/60&0\\0&0&29/20\end{pmatrix}.
\]

Thus \(N^Te_1=(7/60,3/5,0)\) is not parallel to \(e_1\). This first jet cannot occur in a globally helicity-free uniformly sublinear \(C^2\) profile. No degree-seven calculation is needed for that global exclusion. The exact finite-jet theorem remains a different statement about local formal extensions, where the global recurrence premise is absent.

On the often-used two-parameter slice

\[
M(s,b)=\begin{pmatrix}s&b&0\\b+1&-1-s&0\\0&0&1\end{pmatrix},
\quad u=e_1,\quad w=e_3,
\]

condition (1) reduces to

\[
b=-\omega.                                                  \tag{4}
\]

At this specific normalization, the slice is exhaustive for the first-jet vorticity constraints: M e3=e3 gives M13=M23=0 and M33=1; curl(M y)=e3 then gives M31=M32=0 and M21=M12+1; the trace fixes M22=-1-M11. This is not a coordinate normalization claimed for every orientation relative to the fixed rotation axis.

Consequently a search intended to produce jets compatible with this global necessary condition should include this locus explicitly. This is a selection criterion for the global problem, not an assertion that arbitrary jets on the locus extend.

## The same necessary conditions allow large exponents

For any \(L>0\), set \(s=-c-L\), \(b=-\omega\). Then all the pointwise first-jet relations above hold, and

\[
N=\begin{pmatrix}-L&0&0\\1-2\omega&L-a&0\\0&0&1+c\end{pmatrix}.
\]

Its backward eigenvalues are \(L,a-L,-(1+c)\). Choosing \(L>2a\) makes the largest one exceed \(2a\). The carrier point can be placed at \(p=-A^{-1}e_1\), since \(c>0\) makes \(A\) invertible. These are matrices satisfying the displayed necessary first-jet constraints only. In particular, the further condition grad(U.W)(p)=M^T w+DW(p)^T u=0 involves second derivatives and has not been imposed. The top backward exponent under (2) is max(-rho,a+rho), at least a/2; the displayed family shows that the algebraic constraints do not provide an upper bound. No helicity-free neighborhood, infinite formal solution, globally decaying profile, or actual counterexample to the \(\Gamma_Z\) bound is constructed.

## Two immediate pointwise consequences

The origin cannot be a vortical carrier zero under the theorem's hypotheses: B(0)=U(0), so a carrier zero there would have u=0. This contradicts the proved nonvanishing of u.

At a carrier zero p!=0 in the closure of O, even if W(p)=0, continuity extends d(BH) wedge dH=0 to p. Since u=-Ap and A is invertible, u!=0. The same gradient calculation gives N^T u=rho u. The conclusion that all eigenvalues are real uses w!=0 and is not asserted in this irrotational case.

## Evidence and received review

The complete A413 rank proof and the rotating sample proof are pinned in the team records. Every displayed matrix and derivative was computed by hand; no numerical computation is needed. The coordinator review, written02:38Z and pinned alongside the sources, independently recomputes the gradients, matrices, slice, eigenvalues and scope. All five precision points have been checked and incorporated. The received review checks the A413 statement and regularity passage; this agent separately reread its complete proof. Existing agent configuration is the primary model, not a separate provider-execution attestation. No new model client or subagent was used.

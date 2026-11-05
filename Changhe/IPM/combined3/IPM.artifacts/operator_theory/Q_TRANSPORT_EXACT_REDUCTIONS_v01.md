# Exact reductions for the Q-norm transport form

Status: exact identities and scope checks. No norm bound for their additional
terms is claimed. These formulas prevent transferring an old-N commutator
certificate into Q without its missing weight terms.

Put q=21/10, f=J^q g, G=Wf, W²=1+4r², and
\[
C=[J^q,u_*\cdot\nabla]J^{-q},\quad C_s=(C+C^*)/2,\quad C_a=(C-C^*)/2.
\]
All identities first hold as real quadratic forms on Schwartz tests. The
actual smooth background has polynomial growth below one and all the
displayed forms are defined there. Separate quantitative estimates are
required for any subsequent extension.

## Hermitian and skew kernels

For a=J(xi), b=J(eta), tau=a/b, zeta=xi-eta, divergence freeness gives
xi·uhat(zeta)=eta·uhat(zeta). The exact kernels are
\[
C_s(\xi,\eta)=\frac i2\eta\cdot\widehat u(\zeta)
(\tau^q-\tau^{-q}),\qquad
C_a(\xi,\eta)=\frac i2\eta\cdot\widehat u(\zeta)
(\tau^q+\tau^{-q}-2).
\tag{1}
\]
The conventions are those of `../EXACT_COMPACT_DECOMPOSITION.md`; Fourier
kernel integration has factor (2pi)^-2. The old remainder satisfies
\[
\langle C_sG,G\rangle=q\langle S mRG,mRG\rangle+C_{tr,old}(G),
\quad m=|D|J^{-1}.
\tag{2}
\]

## An exact double-commutator transfer

The algebraic identities
\[
\operatorname{Sym}(WC_sW^{-1})
=C_s+\tfrac12W^{-1}[W,[W,C_s]]W^{-1},
\]
\[
\operatorname{Sym}(WC_aW^{-1})
=\tfrac12W^{-1}[W^2,C_a]W^{-1}
\]
give
\[
\begin{aligned}
C_{tr,Q}(G)={}&C_{tr,old}(G)
+q\langle S mRG,mRG\rangle-q\langle SRG,RG\rangle\\
&+\tfrac12\langle[W,[W,C_s]]f,f\rangle
+\tfrac12\langle[W^2,C_a]f,f\rangle.
\end{aligned}
\tag{3}
\]
**The principal difference in the first line is not merely a negative p
sandwich.** Its exact expansion is
\[
q\langle S mRG,mRG\rangle-q\langle SRG,RG\rangle
=T_{IS}(G)-q\langle S pRG,pRG\rangle,
\tag{4}
\]
where p=J^-1 and TIS is the double commutator from the exact decomposition.
This term must be retained when using the reduction.

The polynomial weight in the skew contribution is especially explicit:
\[
\widehat{[W^2,C_a]}(\xi,\eta)
=-4(\Delta_\xi-\Delta_\eta)C_a(\xi,\eta).
\tag{5}
\]
Thus it requires only derivatives of the smooth J symbols and of the actual
stream transform. The double-W term has no corresponding polynomial
identity; treating it as a bounded order-minus-two operator without a
constant does not finish a quantitative proof.

## Exact polynomial-coordinate representation

Let L0=1, L1=2x, L2=2y, and h_a=L_a f. Then
\[
\boxed{\Re\langle WCf,Wf\rangle
=\sum_{a=0}^2\langle C_sh_a,h_a\rangle
+4\sum_{j=1}^2\Re\langle[x_j,C]f,x_jf\rangle.}
\tag{6}
\]
No fractional W occurs in its coordinate commutators. Their Fourier kernels
are i(D_xi_j+D_eta_j)C; the derivative sum keeps zeta fixed, so it does not
differentiate uhat. In explicit form, writing t=tau^q,
\[
[x_j,C](\xi,\eta)=
-\widehat u_j(\zeta)(t-1)
-q(\eta\cdot\widehat u(\zeta))t
\left(\frac{\xi_j}{a^2}-\frac{\eta_j}{b^2}\right).
\tag{7}
\]
This is a complete kernel formula, not a numerical bound.

There is an exact way to retain the existing pointwise matrix certificate
without reconciling R h_a with RG. For the actual pointwise matrix M* and
its certified lower bound beta,
\[
\sum_a\int(Rh_a)^T\mathcal M_*(Rh_a)
\ge\beta\sum_a\|Rh_a\|_2^2
=\beta\sum_a\|h_a\|_2^2=\beta\|G\|_2^2.
\tag{8}
\]
The changed parities of h1,h2 cause no problem in (8), because the matrix
inequality is pointwise for all two-vectors and R is an L2 isometry. They
**do** matter for remainder estimates whose proofs used S1. In particular
one cannot simply assign ||J^-q h_a||<=||g||. The coordinate commutators
and local kernel coordinate factors have to be priced explicitly.

For reference, the existing weighted old-Ctr obligation does have one
precise coordinate consequence. If its proved bound is
\(|C_{tr,old}(h)|\le C_H\|W^{-1}ph\|_2^2\), then
\[
\sum_a|C_{tr,old}(h_a)|\le4C_H\|pf\|_2^2.
\tag{9}
\]
Indeed W^-1 L is an isometry, while the vector commutator [p,L] has norm
at most ||pf||, because its nonzero Fourier entries are 2i xi_j p³ f and
2|xi|p²<=1. Minkowski gives the factor four. No value of C_H is supplied
by this identity.

## Scope

Equations (3)--(9) are two exact routes, not an asserted comparison between
the old and new norms. Their unresolved constants are separate obligations.
The actual theorem remains open until one route supplies a complete usable
bound and is assembled with all other linear and nonlinear terms.

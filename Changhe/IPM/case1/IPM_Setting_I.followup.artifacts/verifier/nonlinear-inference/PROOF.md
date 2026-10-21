# What finite numerical probes can exclude

Status: proved statement about information from numerical probes. It is not a theorem about the IPM equation.
Date: 2026-10-20. Source of the question: the numerical researcher's report (not published), sections 0, 4j and 4k, read at about 13:10 UTC.

## Statement

Let $n\geq2$, let $F:B_R(0)\subset\mathbb R^n\to\mathbb R^m$ be smooth, and let $D$ be a finite collection of lines through $0$. For every $0<r<R$, there are a smooth map $\widetilde F$ and a point $z_*$ with $0<|z_*|<r$ such that:

1. $\widetilde F=F$ on every line in $D$ intersected with $B_R(0)$;
2. $\widetilde F=F$ in a neighbourhood of $0$, so their derivatives of every order agree at $0$;
3. $\widetilde F(z_*)=0$.

Consequently, a residual value, a Jacobian at the base point, and complete residual scans along finitely many fixed directions cannot, without further uniform information, exclude roots throughout a ball.

## Proof

A finite union of lines has empty interior in $\mathbb R^n$ when $n\geq2$. Choose $z_*$ in $B_r(0)$ outside that union. The union is closed. There is therefore a positive $\eta$ such that the closed ball $\overline B_\eta(z_*)$ lies in $B_r(0)$ and is disjoint from the union. In particular it does not contain $0$.

Choose a smooth function $\chi$ supported in $B_\eta(z_*)$ with $\chi(z_*)=1$. Set $\widetilde F(z)=F(z)-\chi(z)F(z_*)$. On the union of lines and in a neighbourhood of $0$, the function $\chi$ vanishes identically. These facts give the first two assertions. At $z_*$ the definition gives $\widetilde F(z_*)=F(z_*)-F(z_*)=0$, which proves the third assertion.

No derivative bounds for $\widetilde F$ away from $0$ are asserted. Such bounds are precisely additional information that could support a ball-wide exclusion.

## Restricted singular values

Let $J:\mathbb R^n\to\mathbb R^m$ with $m\geq n$, and let $Q$ be an $n$ by $k$ matrix with orthonormal columns. List the singular values of $J$ in increasing order as $\sigma_1\leq\cdots\leq\sigma_n$ and those of $JQ$ as $\theta_1\leq\cdots\leq\theta_k$. Then $\sigma_i\leq\theta_i$ for $1\leq i\leq k$.

Indeed, the variational characterization of the $i$-th eigenvalue of $J^TJ$ minimizes the maximum Rayleigh quotient over all $i$-dimensional subspaces. Restricting those subspaces to the range of $Q$ can only increase the minimum. The resulting restricted operator is $Q^TJ^TJQ$. Taking square roots proves the assertion. It gives no positive lower bound on any of the $\sigma_i$.

If the computed action matrix is $Y=JQ+E$ with a proved operator-norm error $\|E\|\leq\varepsilon$, then the usable bound is $\sigma_i(J)\leq\sigma_i(Y)+\varepsilon$. A maximum error of $\varepsilon_c$ in each of $k$ columns only gives $\varepsilon\leq\sqrt{k}\varepsilon_c$ without further structure.

## Application and scope

A large Newton step $-J^{-1}F(0)$ only says that the linear approximation would place its root far away. It gives no nonlinear root exclusion. A small value of $\|Jv\|$ in a trial subspace also does not establish a kernel or an exact nonlinear family. Likewise, small changes of a nonzero residual after fixing $c_l$ show weak sensitivity at that residual level; calling $c_l$ a free parameter of solutions requires actual solutions and a continuation argument.

The numerics lane withdrew its earlier ball-exclusion and lower-bound claims in section 4k(c) before this note was completed. That correction is supported by the proof above. The numerical question of whether there is any nearby IPM root remains open.

Dependencies: elementary topology, a smooth compactly supported bump function, and finite-dimensional variational characterization of eigenvalues. No IPM hypothesis is used. No formalization or build was run.

## Comparing singular vectors after changing norms

Let $D$ be the invertible positive diagonal matrix defining the parameter conversion $v=Dz$, and let $W$ be the positive diagonal matrix defining the residual norm. A singular pair for $M=WJD$ with $\|z\|_2=1$ obeys $\|WJDz\|_2=\sigma$. If the physical direction is subsequently normalized to $v=Dz/\|Dz\|_2$, then
\[
 \|D^{-1}v\|_2=\|Dz\|_2^{-1},\qquad
 \frac{\|WJv\|_2}{\|D^{-1}v\|_2}=\sigma.
\]
This follows by direct substitution. The physical quantity $\|Jv\|_2$ generally differs from $\sigma$, even for an exact Jacobian and exact singular vector. Finite differences must use the same numerator and denominator to validate this singular value. This correction does not remove a measured vector discrepancy between a finite difference and $Jv$.

The audit in `verification/matrix_n120m48_S.json` independently recomputes the diagonal weights, both full singular spectra of the saved 5762 by 5762 matrix, and the QR/Ritz calculation on saved actions. It confirms the reported matrix spectra. It does not establish that the saved matrix equals the derivative of the numerical residual map, nor that this map approximates the continuum linearization to a controlled accuracy.

Finally, a large projection of a residual $F$ onto $J(S)$ for a selected small-action domain subspace $S$ does not mean that this part of $F$ can only be reached through $S$. The images of $S$ and $S^\perp$ need not be orthogonal. For example $J(x,y)=\varepsilon x+y$ has $J(S)=\mathbb R=J(S^\perp)$ for the first coordinate axis $S$, although the action along $S$ is arbitrarily small. Every nonzero residual has projection fraction one onto $J(S)$, and a well-scaled correction using only $S^\perp$ cancels it. Orthogonality of the image spaces, or another exclusion of the complementary action, is additional information.

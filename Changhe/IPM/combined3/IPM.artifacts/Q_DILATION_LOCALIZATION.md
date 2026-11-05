# Quantitative localization of the favorable Q-norm dilation term

Status: analytic lemma. This supplies localized damping only; all other far-field terms still require their own estimates.

Let \(p=J^{-1}\), \(W=\sqrt{1+4r^2}\), and \(T=Wp^2W^{-1}\). Its symmetric kernel is
\[
T_s(x,y)=K(x-y)\frac{W(x)/W(y)+W(y)/W(x)}2,
\]
where K is the positive convolution kernel of p², with integral one. The heat representation gives
\[
\int |z|K(z)dz=\pi/2,\quad\int |z|^2K(z)dz=4,\quad
\int |z|^3K(z)dz=9\pi/2.
\tag{1}
\]
The global ratio bound \(W(x)/W(y)\le1+2|x-y|\) and its reciprocal imply \(\|T\|_{2\to2}\le1+\pi\), by Schur's test. As independently proved in the Q-norm branch,
\[
\operatorname{Re}\langle TG,G\rangle\ge0.
\tag{2}
\]
For completeness set f=TG. Then
\(G=WJ^2W^{-1}f\), and integration by parts gives
\[
\operatorname{Re}\langle TG,G\rangle
=\|\nabla f\|_2^2+\int(1-|\nabla\log W|^2)|f|^2\ge0,
\]
since \(|\nabla\log W|\le1\). This is first justified on smooth data and extended using boundedness and density.

## The far block differs from p² only by O(R−2)

If H is supported in \(|x|\ge R\), then
\[
\boxed{\left|\operatorname{Re}\langle TH,H\rangle-\|pH\|_2^2\right|
\le\frac{2}{R^2}\|H\|_2^2.}
\tag{3}
\]
Indeed the kernel difference is exactly
\[
K(x-y)\frac{(W(x)-W(y))^2}{2W(x)W(y)}.
\]
For both variables in the support, W(x),W(y)≥2R and |W(x)−W(y)|≤2|x−y|. Thus it is bounded in absolute value by \(K(x-y)|x-y|^2/(2R^2)\). Schur's test and (1) prove (3). Its pointwise positive kernel is not asserted to be a positive operator.

## An IMS estimate with an explicit radial partition

Let \(\chi_N=\cos\theta(r)\), \(\chi_F=\sin\theta(r)\), where theta=0 for r≤R, theta=pi/2 for r≥2R, and between these radii
\[
\theta(r)=\frac\pi2[3t^2-2t^3],\qquad t=(r-R)/R.
\]
These are bounded C1 radial functions, sufficient for all L2 quadratic forms below; their Lipschitz phase constant is \(L_\theta\le3\pi/(4R)\). They satisfy \(\chi_N^2+\chi_F^2=1\).
The exact quadratic localization error has kernel
\(T_s(x,y)[1-\chi_N(x)\chi_N(y)-\chi_F(x)\chi_F(y)]\).
Since the bracket equals \(1-\cos(\theta(x)-\theta(y))\), its absolute value is at most \(L_\theta^2|x-y|^2/2\). Therefore
\[
\left|\operatorname{Re}\langle TG,G\rangle
-\sum_{i=N,F}\operatorname{Re}\langle T(\chi_iG),\chi_iG\rangle\right|
\le\frac{9\pi^2(4+9\pi)}{32R^2}\|G\|_2^2.
\tag{4}
\]
Here the weight-ratio bound and (1) give the kernel moment \(4+9\pi\). Combining (2) for the near block, (3) for the far block, and (4) gives
\[
\boxed{\operatorname{Re}\langle TG,G\rangle
\ge\|p(\chi_FG)\|_2^2
-\frac{2+9\pi^2(4+9\pi)/32}{R^2}\|G\|_2^2.}
\tag{5}
\]
The numerator is below 92. Thus choosing R=100 retains a complete far low-frequency damping norm at a high-norm cost below 0.0092 before multiplication by qc. The remaining estimates must use exactly p(chi_F G), or account for every commutator needed to replace it by a different localized norm. Formula (5) by itself does not supply a global lower bound by a fixed multiple of ||pG||².

## Simultaneous global and additional far damping on S1

The sharper symmetry-restricted lemma in `finite_rank/QNORM_BACKGROUND_IDENTITY.md` gives
\(\operatorname{Re}\langle TH,H\rangle\ge\frac12\|pH\|_2^2\) on S1. Radial multiplication preserves S1. Apply this to the near block, and (3) to the far block, in (4). This yields
\[
\operatorname{Re}\langle TG,G\rangle\ge
\frac12\sum_{i=N,F}\|p(\chi_iG)\|_2^2
+\frac12\|p(\chi_FG)\|_2^2
-\frac{2+9\pi^2(4+9\pi)/32}{R^2}\|G\|_2^2.
\]
For the unweighted kernel K, exactly the same IMS argument gives
\[
\left|\|pG\|_2^2-\sum_{i=N,F}\|p(\chi_iG)\|_2^2\right|
\le\frac{9\pi^2}{8R^2}\|G\|_2^2.
\]
Consequently
\[
\boxed{\operatorname{Re}\langle TG,G\rangle\ge
\tfrac12\|pG\|_2^2+\tfrac12\|p(\chi_FG)\|_2^2
-\frac{98}{R^2}\|G\|_2^2\quad(G\in S1).}
\tag{6}
\]
Indeed \(2+9\pi^2(4+9\pi)/32+9\pi^2/16<98\), for example by substituting the rational upper bound pi<22/7. This preserves the full global half-damping allowance and supplies an additional far half. It is stronger than merely averaging (5) with the global half lemma. No bound on a source or transport commutator follows without its separate proof.

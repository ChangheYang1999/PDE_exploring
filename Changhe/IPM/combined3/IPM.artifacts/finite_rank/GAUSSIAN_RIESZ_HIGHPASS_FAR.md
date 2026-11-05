# Explicit Gaussian Riesz high-frequency bound

Status: proved operator estimates. The numerical companion certifies actual far coefficient bounds only; joining every term of the stationary IPM energy remains a separate obligation.

Use unitary Fourier transform in dimension two, (R_j) with symbol (-i\xi_j/|\xi|), (P_\mu=\exp(\Delta/(2\mu^2))), and (H_\mu=I-P_\mu). Write (t=1/(2\mu^2)). The sign of the Riesz convention does not affect any estimate below.

## A first spatial moment without a low-frequency cutoff

Let (p_s(x)=(4\pi s)^{-1}\exp(-|x|^2/(4s))). The vector kernel of (RH_\mu), interpreted first away from the origin, is
\[
 k_H=\pi^{-1/2}\left[\int_0^t s^{-1/2}\nabla p_s\,ds
 +\int_t^\infty\big(s^{-1/2}-(s-t)^{-1/2}\big)\nabla p_s\,ds\right].
\]
This follows by subtracting the two heat representations of (R) and (RP_\mu). Since
\[
 \int |x|\,|\nabla p_s(x)|\,dx=2,
\quad \int |x|\,|\partial_jp_s(x)|\,dx=4/\pi,
\]
and the total absolute integral of the two scalar weights is (4\sqrt t), Tonelli gives the explicit bounds
\[
 \boxed{\int |x|\,|k_H(x)|\,dx\le\frac{4\sqrt2}{\sqrt\pi\,\mu}},
\quad
 \int |x|\,|k_{H,j}(x)|\,dx\le\frac{8\sqrt2}{\pi\sqrt\pi\,\mu}.
\]
The near-origin kernel is a principal-value kernel, but its product with a Lipschitz coefficient difference is absolutely integrable. No second kernel moment is asserted.

For comparison, the Gaussian has the exact moment
\[
 \int |x|p_t(x)\,dx=\sqrt{\pi t}=\frac{\sqrt{\pi/2}}\mu.
\]

## Matrix double commutator

Let \(K(x)\) be a real symmetric bounded \(2\times2\) matrix and assume
\(\|K(x)-K(y)\|_F\le L|x-y|\). Define the bounded self-adjoint operator
\[
 C_K=-\frac12\sum_{j,k=1}^2[R_j,[R_k,K_{jk}]].
\]
Equivalently (C_K=\operatorname{Sym}A_K), where
\(A_K=\sum_{j,k}[R_j,K_{jk}]R_k\). In particular the IPM (C_{vs3}) is exactly (C_K) for
\[
 K=\begin{pmatrix}-\rho_y&\rho_x/2\\\rho_x/2&0\end{pmatrix}.
\]

The elementary exact identity
\[
 [R_j,K_{jk}]R_kH_\mu
 =[R_jH_\mu,K_{jk}]R_k-R_j[H_\mu,K_{jk}]R_k
\]
puts the high multiplier inside the Riesz kernel. Using (R:L^2\to L^2(\mathbb R^2;\mathbb R^2)) isometrically, matrix kernel differences satisfy
\[
 \left\|\sum_{j,k}[R_jH_\mu,K_{jk}]R_k\right\|
 \le L\int |z||k_H(z)|\,dz.
\]
The second term has norm at most (L\int |z|p_t(z)dz). For (A_K^*H_\mu), commute (H_\mu) through the Riesz transforms. The first resulting kernel is the transposed matrix difference applied to (k_H(z)), followed by the norm-one Riesz contraction. The second term is the contraction \(\sum_{j,k}R_jR_k[H_\mu,K_{jk}]\). The map from a matrix field (F) to \(\sum_{j,k}R_jR_kF_{jk}\) has norm at most one from Frobenius-valued L2 to scalar L2, since its Fourier symbol has Frobenius norm one. Thus the same Gaussian moment bounds this term. Therefore
\[
 \boxed{\|C_KH_\mu\|\le\frac{C_*L}{\mu}},\qquad
 C_*=\frac{4\sqrt2}{\sqrt\pi}+\sqrt{\frac\pi2}.
\]
This proves, by (C_K-P_\mu C_KP_\mu=H_\mu C_K+P_\mu C_KH_\mu),
\[
 \boxed{|\langle C_KG,G\rangle-\langle C_KP_\mu G,P_\mu G\rangle|
 \le\frac{2C_*L}{\mu}\|G\|_2^2.}
\]
The proof controls the two matrix sums through vector Riesz isometries and consequently does not insert an unnecessary sum of four component norms.

## Actual far coefficients

Take any radial cutoff \(0\le\chi_F\le1\), zero on \(r\le R\), with \(\|\nabla\chi_F\|_\infty\le c_\chi/R\), and set \(K_F=\chi_FK\). If \(B_R\) bounds \(|\nabla\rho|\) for all \(r\ge R\), and \(D_R\) bounds the Frobenius Hessian norm there, then
\[
 \operatorname{Lip}_{F}(K_F)\le D_R+c_\chi B_R/R.
\]
Indeed (|K|_F\le|\nabla\rho|), and the same contraction holds after each directional derivative. These bounds require only a Lipschitz cutoff. Smooth cutoffs with (c_\chi=2) exist; the standard cosine transition has (c_\chi=\pi/2) and is already globally C1.

The companion `Gaussian_Riesz_far_bounds.py` uses the exact-source far expansion to certify (B_R,D_R) uniformly on the whole exterior, and substitutes (\mu=1/10,c_\chi=2). Its output is an actual high-frequency/cross error for the (C_{vs3}) term. A favorable low-frequency damping allowance and the other IPM energy terms still have to be joined separately.

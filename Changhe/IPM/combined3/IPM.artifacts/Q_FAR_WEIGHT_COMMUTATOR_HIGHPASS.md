# A quantitative far-field high-pass bound for the Q weight-source form

Status: analytic operator lemma. Its hypotheses must be supplied by actual coefficient bounds. This does not estimate the near source, the transport remainder, or the complete IPM energy.

Work on real centrally odd functions in two dimensions. Put W=sqrt(1+4r²), c=W^-1, P=exp(Delta/(2mu²)), H=I-P, and U=(-R1R2,R1²). Let the real vector coefficient b be centrally even, bounded, zero for r<=R, and globally Lipschitz. Assume

|b|<=B, Lip_F(b)<=Lb, Lip_F(Wb)<=Ld.

The last coefficient need not itself be bounded; its Lipschitz seminorm suffices. Define the bounded real self-adjoint operator

E=Sym(b·WUc-b·U).

The central-odd weighted velocity bounds imply ||E||<=(sqrt(3)+1)B. The following bound controls every Gaussian low/high cross term explicitly.

## Additional power weights

For 1<=alpha<2,
\[
\|W^\alpha Uf\|_2\le C_\alpha\|W^\alpha f\|_2,\qquad
C_\alpha=2^{(\alpha-1)/2}\frac2{2-\alpha}.
\tag{1}
\]
Here f is real centrally odd and the output norm is vector valued. To prove this, use the Beurling transform B0, whose angular-Mellin multiplier on physical angular mode m is, up to an irrelevant convention,
\[
\frac{m-1-\alpha+i\tau}{1-m-\alpha+i\tau}.
\]
Oddness restricts m to odd integers. The norm on homogeneous r^(2alpha)-weighted L2 is therefore at most (2+alpha)/(2-alpha): m-1 is even, and its negative value of smallest nonzero magnitude is -2. The scalar mode m=1 has multiplier of modulus one. The real identity U2+iU1=-(I+B0)/2 gives homogeneous velocity norm at most 2/(2-alpha). These formulas are justified first on finite angular sums and compactly supported smooth radial Mellin data; density, or the radial first-order differential equation for B0, identifies the extension with the usual transform. The physical far tail is integrable because alpha<2.

Finally, for alpha>=1,
\[
1+s^\alpha\le(1+s)^\alpha\le2^{\alpha-1}(1+s^\alpha).
\]
Combining the unweighted and homogeneous estimates proves (1). This additional weighted bound is used only on centrally odd inputs.

## Heat-kernel moments

Let Z have density p_t, t=1/(2mu²), and define
\[
m_s=\mathbb E|Z|^s=2^{s/2}\mu^{-s}\Gamma(1+s/2).
\]
The vector kernel k of UH has moments
\[
\int |z|^2|k(z)|\,dz\le M_2=5\mu^{-2},\qquad
\int |z|^3|k(z)|\,dz\le M_3=3\sqrt{2\pi}\mu^{-3}.
\tag{2}
\]
Indeed UH is a signed row of second derivatives of \(\int_0^t p_s\,ds\). Its vector kernel is bounded by
\[
\int_0^t \left(\frac{r^2}{4s^2}+\frac1{2s}\right)p_s(z)\,ds.
\]
Tonelli and the explicit radial Gaussian moments give (2). Possible local identity distributions are annihilated by the coefficient differences below. In particular these moment estimates do not assert that the kernel itself is integrable at the origin.

## Exact high-pass decomposition

Let E_UH denote E with U replaced by UH in both symmetric halves. Commuting H through c, b and Wb gives the exact identity
\[
\boxed{EH=E_{UH}
+\tfrac12 bWU[c,H]
+\tfrac12(cU^*W-U^*)[b,H]
+\tfrac12cU^*[W,H]b.}
\tag{3}
\]
All vector contractions have their natural scalar/vector types. This can first be checked on smooth truncated coefficients and then passed to the bounded forms below. No high-pass/weight commutator is dropped.

The symmetric kernel of E_UH is
\[
\frac{k(x-y)}2\cdot
\frac{(W(x)-W(y))(W(x)b(x)-W(y)b(y))}{W(x)W(y)}.
\]
When |x-y|<=R/2 and this kernel is nonzero, one point lies in the support of b and both points have radius at least R/2. Thus its absolute value is at most Ld |k(z)||z|²/R². For |z|>R/2, it is at most 2B|k(z)||z|, which is bounded by 8B|k(z)||z|³/R². Schur's test yields
\[
\|E_{UH}\|\le (Ld M_2+8BM_3)/R².
\tag{4}
\]

For the first error in (3), the Gaussian kernel and W(x)<=W(y)+2|z| imply
\[
W(x)^\alpha|c(x)-c(y)|
\le2|z|(1+2|z|)^{\alpha-1}.
\]
This is a radial convolution majorant for both Schur integrals. Since 0<=alpha-1<1, it follows that
\[
\|W^\alpha[c,H]\|\le I_\alpha,\qquad
I_\alpha=2m_1+2^\alpha m_\alpha.
\]
The output multiplier b is supported in r>=R. Apply (1) to obtain
\[
\|bWU[c,H]\|\le B(2R)^{1-\alpha}C_\alpha I_\alpha.
\tag{5}
\]

The middle error in (3) is bounded by
\[
\|(cU^*W-U^*)[b,H]\|\le(\sqrt3+1)Lb\,m_1.
\tag{6}
\]
Indeed ||cU*W||<=sqrt3 on odd vectors, and the Gaussian commutator kernel of b is bounded by Lb|z|p_t(z).

For the last error, use ||cU*W||<=sqrt3 and estimate c[W,H]b. Its kernel is (W(x)-W(y))b(y)p_t(z)/W(x), with |y|>=R whenever b(y) is nonzero. If |z|<=R/2, then W(x)>=R. The absolute kernel is at most 2B|z|p_t(z)/R. If |z|>R/2, use W(x)>=1 and |z|<=4|z|³/R². Therefore
\[
\|cU^*[W,H]b\|\le\sqrt3 B(2m_1/R+8m_3/R²).
\tag{7}
\]
Every input to a symmetry-restricted weighted U estimate in (5)--(7) remains centrally odd.

## Final explicit bound

Combining (3)--(7), set
\[
A_E=\frac{Ld M_2+8BM_3}{R²}
+\frac12\left[
B(2R)^{1-\alpha}C_\alpha I_\alpha
+(\sqrt3+1)Lb\,m_1
+\sqrt3 B(2m_1/R+8m_3/R²)\right].
\]
Then
\[
\boxed{\|EH\|\le A_E,\qquad
|\langle EG,G\rangle-\langle EPG,PG\rangle|
\le2A_E\|G\|².}
\tag{8}
\]
The second assertion uses E-PEP=HE+PEH, self-adjointness of E and the norm-one property of P. For mu<=1, ||PG||<=||J^-1G|| exactly, since log(1+s)<=s/mu². Thus (8) can join a separately priced low-frequency source block to Bessel damping.

The lemma alone is not such a complete join: the other source component, the chosen spatial cutoff and its actual B,Lb,Ld, the near-field price, and every other background term must all be included. The proof deliberately retains the coordinate and Gaussian commutator errors that would be lost by commuting a spatial weight with P.

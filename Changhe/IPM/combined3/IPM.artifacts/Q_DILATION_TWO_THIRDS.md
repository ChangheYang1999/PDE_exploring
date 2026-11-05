# Exact two-thirds Bessel damping for the Q norm

Status: proved analytic lemma, independently checked by both other operator workstreams. This improves the previous one-half bound; it does not bound the other IPM remainders.

Let W=sqrt(1+4r²), J=(1-Delta)^(1/2), p=J^-1, T=WJ^-2W^-1, and ell=grad log W. On the real S1 subspace,
\[
\boxed{\operatorname{Re}\langle TG,G\rangle
\ge\frac23\|pG\|_2².}
\tag{1}
\]

We use the bounded-form construction already justified in finite_rank/QNORM_BACKGROUND_IDENTITY.md. The inverse differential operator is
\[
M_0=WJ²W^{-1}
=-\Delta+2\ell\cdot\nabla+1+\operatorname{div}\ell-|\ell|².
\]
For a test f write F=||f||2, Drad=||partial_r f||2, Dang=||r^-1 partial_theta f||2, and E=||ell f||2. Its real symmetric form is
\[
H_0[f]=D_{\rm rad}²+D_{\rm ang}²+F²-E².
\]
Its skew form is
\[
B_0(f,h)=\langle\nabla f,\ell h\rangle
-\langle\ell f,\nabla h\rangle.
\]
Because ell is radial, only radial derivatives enter B0.

Set t=r². The following exact nonnegative rational identity is the key:
\[
1+\frac1t-3|\ell|²
=1+\frac1t-\frac{48t}{(1+4t)²}
=\frac{1+t(4t-3)²}{t(1+4t)²}\ge0.
\tag{2}
\]
On almost every circle, central oddness gives the angular Poincare inequality ||f||²_circle<=||partial_theta f||²_circle. Multiply (2) by |f|² and integrate to obtain
\[
3E²\le F²+D_{\rm ang}².
\]
Consequently
\[
H_0[f]\ge D_{\rm rad}²+2E².
\tag{3}
\]
For two tests the skew form satisfies
\[
|B_0(f,h)|\le D_{\rm rad}(f)E(h)+E(f)D_{\rm rad}(h)
\le\frac1{\sqrt2}\sqrt{H_0[f]H_0[h]}.
\tag{4}
\]
The last inequality is Cauchy-Schwarz after applying the norm-one swap matrix to (Drad,sqrt(2)E).

Now V=J^-1 M0 J^-1=H+B is a bounded invertible form operator on the S1 Hilbert space. Its symmetric part obeys I/2<=H<=I by the preceding half-damping proof. Formula (4) shows that the skew-adjoint operator A=H^-1/2 B H^-1/2 has norm at most1/sqrt(2). Hence
\[
\operatorname{Re}V^{-1}
=H^{-1/2}(I-A²)^{-1}H^{-1/2}
\ge\frac23 H^{-1}\ge\frac23 I.
\]
Since T=J^-1 V^-1 J^-1, (1) follows. The bounded inverse agrees with the explicit weighted Bessel inverse on smooth tests by the previously proved uniqueness of the coercive form problem, and both extend by density.

The argument actually uses only central oddness, so radial multiplication preserves every symmetry condition needed for applying it to localized blocks.

At the fixed c=4076476460239181/2251799813685248 and q=21/10, the favorable frozen term therefore supplies
\[
qc\,\operatorname{Re}\langle TG,G\rangle
\ge\frac{2qc}3\|pG\|²,
\qquad \frac{2qc}3=2.5344468942799973198987\ldots.
\]

Combining the localized far-block proof in Q_DILATION_LOCALIZATION.md with (1), the same partition gives
\[
\operatorname{Re}\langle TG,G\rangle\ge
\frac23\|pG\|²+\frac13\|p(\chi_FG)\|²
-\frac{100}{R²}\|G\|².
\tag{5}
\]
Indeed the IMS numerator is at most
2+9pi²(4+9pi)/32+(2/3)9pi²/8<100, verified by pi<22/7. No separate source or transport term is included in this allowance.

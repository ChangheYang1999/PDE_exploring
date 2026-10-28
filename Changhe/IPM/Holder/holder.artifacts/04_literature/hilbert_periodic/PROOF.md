# Exact periodic Hilbert seminorm from Babenko's increment theorem

## Statement

For real continuous 2pi-periodic functions and 0<alpha<1, use the angular
geodesic seminorm

$$[f]_{\alpha,\mathbb T}=\sup_{x\in\mathbb R,\ 0<h\le\pi}
\frac{|f(x+h)-f(x)|}{h^\alpha}.$$

Let

$$Hf(x)=\frac1{2\pi}\operatorname{pv}\int_{-\pi}^{\pi}
 f(y)\cot\frac{x-y}{2}\,dy.$$

The principal value exists on this space by angular cancellation and
integrability of t^(alpha-1) at zero. Its exact operator seminorm is

$$N_\alpha=\frac{2^{1-\alpha}}\pi
 B\left(\frac{1-\alpha}{2},\alpha\right)
 =\frac{\Gamma(\alpha/2)\Gamma((1-\alpha)/2)}{\pi^{3/2}}.$$

The same constant applies to complex-valued functions with the absolute
value seminorm. This is not a statement about the chordal metric or a full
norm including a supremum term. The whole-line version has its separate
proof in `../hilbert_exact/PROOF.md`.

## Source dependency

V. F. Babenko, *Sharp Estimates for Norms of Functions from Conjugate Classes
in Metrics C and L*, arXiv:1402.0829v1, Theorem 1(2), page 2, gives the exact
maximal increment for every concave Dini modulus omega. Remark 3, page 3,
asserts attainment. All three pages were checked in the saved primary
source `../sources/conjugate_sharp_2014.pdf` and its text extraction. The
paper is an announcement with references for its proof; this note uses its
stated theorem and does not claim to reproduce that theorem's proof.

For omega(t)=t^alpha, Babenko gives

$$\sup_{[f]_{\alpha,\mathbb T}\le1}
\sup_x|Hf(x+h)-Hf(x)|
=\frac2\pi\int_0^{h/2}F_h(u)(\rho_h(u)-u)^\alpha\,du,$$

where F_h(u)=sin(h/2)/(cos u-cos(h/2)), and rho is defined by matching the
integrals of F on (0,u) and minus F on (rho,pi). Its specified branch has
h/2<rho<pi. The class H^omega in the source equals the seminorm unit ball:
angular distances greater than pi impose no additional restriction on a
periodic function.

## Calculation of the norm

Put b=tan(h/4), with 0<b<=1, and s=tan(u/2)/b, with 0<s<1. Integrating F
explicitly in the mass-matching equation yields

$$\tan(\rho_h(u)/2)\tan(u/2)=b^2,\qquad
\rho_h(u)=2\arctan(b/s),\qquad
F_h(u)\,du=\frac{2\,ds}{1-s^2}.$$

Since h=4arctan(b), the sharp normalized increment is

$$I_\alpha(b)=\frac4\pi\int_0^1
 \frac{Q_b(s)^\alpha}{1-s^2}\,ds,\qquad
Q_b(s)=\frac{\arctan(b/s)-\arctan(bs)}{2\arctan b}.$$

Here is an explicit proof of the needed majorant. Set c=(1-s^2)/s>0. The
arctangent subtraction formula applies with its branch in (0,pi/2), so

$$\arctan(b/s)-\arctan(bs)
=\arctan\frac{cb}{1+b^2}
\le\frac{cb}{1+b^2}\le c\arctan b.$$

The final inequality follows either by integration or differentiation of
arctan(b)-b/(1+b^2), which is nonnegative for b>=0. Consequently

$$0\le Q_b(s)\le\frac{1-s^2}{2s},\qquad
\lim_{b\downarrow0}Q_b(s)=\frac{1-s^2}{2s}.$$

The majorant in I is 2^(-alpha)s^(-alpha)(1-s^2)^(alpha-1). It is integrable
at zero because alpha<1 and at one because alpha>0. Dominated convergence
therefore shows that the upper bound is approached as b tends to zero.
Babenko's sharp increment equality lets us interchange the two suprema
over f and h, giving

$$\|H\|=\frac{2^{2-\alpha}}\pi
 \int_0^1 s^{-\alpha}(1-s^2)^{\alpha-1}\,ds
=\frac{2^{1-\alpha}}\pi B((1-\alpha)/2,\alpha).$$

The duplication identity for Gamma gives the second displayed formula.
For a complex input and a fixed output increment, multiply by a unit
complex number so that its real part equals its magnitude. Apply the real
estimate to that real projection of the input. This proves the same upper
bound, and real inputs give the reverse inequality.

Finally Gamma's simple pole at zero gives alpha N_alpha -> 2/pi and
(1-alpha)N_alpha -> 2/pi at the two endpoints. These one-dimensional
constants are comparisons, not planar second-order Riesz constants.

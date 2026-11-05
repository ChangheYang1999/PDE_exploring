# Constructive finite-rank checkpoint

Status: active research. The stationary existence theorem has not been proved. The exact Gram and rank-one source-commutator enclosure below are established by the accompanying Arb/Acb computations; the larger matrices are floating-point screens. A sufficiently small operator tail for the full compact remainder remains open.

## Smooth basis and the exact low-order Gram

Use the normalized physicists' Hermite functions
\[
h_n(t)=\pi^{-1/4}(2^n n!)^{-1/2}H_n(t)e^{-t^2/2},\qquad
\varphi_{mn}^{\alpha}(x,y)=\alpha h_m(\alpha x)h_n(\alpha y).
\]
Even m and odd n give the required S1 symmetry. The total-degree7 family has10 orthonormal functions. `hermite_gram.py` evaluates
\[
B_{ij}=\int J^q\varphi_i J^q\varphi_j+4\sum_k\partial_{\xi_k}(\langle\xi\rangle^q\widehat\varphi_i)
\overline{\partial_{\xi_k}(\langle\xi\rangle^q\widehat\varphi_j)}\,d\xi,
\quad q=21/10,
\]
where the Fourier transform is unitary in dimension2. The first term is likewise represented in Fourier variables. This is exactly \(\langle WJ^q\varphi_i,WJ^q\varphi_j\rangle\), since \(W^2=1+4|X|^2\).

All polynomial operations are rational. Monomial radial moments are evaluated by
\[
\int_{\mathbb R^2}\xi_1^{2k}\xi_2^{2l}e^{-\beta|\xi|^2}(1+|\xi|^2)^s\,d\xi
=\Gamma(k+1/2)\Gamma(l+1/2)U(k+l+1,k+l+s+2,\beta).
\]
Arb encloses the Gamma/Tricomi functions. `hermite_gram_d7_a1.json` has the10-by10 B matrix and a certified row-sum bound below3924. The q=0 specialization independently recovers the explicit W² Hermite matrix, including B01,01=9 at alpha1 and off-diagonal B01,03=2sqrt6.

`interval_matrix.py` computes an interval Cholesky factor B=LLᵀ and bounds \(\|L^TAL\|\). This equals \(\|B^{1/2}AB^{1/2}\|\) for real symmetric A. Its numerical eigenvector rotation is treated as an exact binary-rational matrix Q, with \(\|Q^TQ-I\|<1\) checked by Arb; the rotated row-sum bound is divided by \(1-\|Q^TQ-I\|\). No floating eigenvalue is accepted as a certificate.

## Actual source symmetrization matrix

Let b=(rho_x,rho_y), Kmat=[[-rho_y,rho_x/2],[rho_x/2,0]], and
\[
\mathcal K_s[G]=\langle b\cdot U[G],G\rangle-\int(RG)^TKmat(RG).
\]
This is Cvs3, the self-adjoint Hilbert-Schmidt source symmetrization remainder. Its full-plane Hilbert-Schmidt identity is inherited from combined2, with its extension hypotheses retained until the actual profile decay/Hessian enclosures are checked.

The matrix element in a real orthonormal basis is
\[
A_{ij}=\int b_xD^x_{ij}+b_yD^y_{ij},
\]
\[
D^x_{ij}=\tfrac12(\varphi_iU_1\varphi_j+\varphi_jU_1\varphi_i-R_1\varphi_iR_2\varphi_j-R_2\varphi_iR_1\varphi_j),
\]
\[
D^y_{ij}=\tfrac12(\varphi_iU_2\varphi_j+\varphi_jU_2\varphi_i)+R_1\varphi_iR_1\varphi_j.
\]
`hermite_polar.py` gives exact angular polynomials and rigorous Kummer1F1 radial formulas for every phi, Rphi and Uphi. They follow by Fourier-Hermite eigenfunctions and
\[
\int_0^\infty t^{p+1}e^{-\beta t^2}J_l(rt)dt=
\frac{r^l\Gamma((p+l+2)/2)}{2^{l+1}\beta^{(p+l+2)/2}\Gamma(l+1)}
{}_1F_1((p+l+2)/2;l+1;-r^2/(4\beta)).
\]
Negative angular modes are handled using \(J_{-l}=(-1)^lJ_l\).

For phi=phi01 at alpha1, the rigorous computation `source_rank1_certificate.py` produced
\[
A_{11}\in[-0.068674008\mathbin{\pm}3.58\times10^{-10}],\quad
B_{11}\in[76.24248469591404981915657569881117\mathbin{\pm}3\times10^{-32}],
\]
and \(C_N<5.235877\). The stored internal A midpoint is -0.0686740077826094 with radius below1.40e-10. The displayed outer enclosure is deliberately wider.

The exact angular products Dx,Dy have frequencies at most4, so potential harmonics n>8 cannot contribute. Removing them is exact orthogonality, not a numerical truncation. The profile coefficient source hashes are checked by `fields013.py`.

### Certified radial quadrature

On each real panel [c-h,c+h], bound the analytic integrand in the Bernstein ellipse rho2 by evaluating its complex rectangle
\[
\Re z\in[c-5h/4,c+5h/4],\qquad |\Im z|\le3h/4.
\]
All fractional profile powers are evaluated only when \(\Re(1+z^2)>0\) and \(\Re(t+z^2)>0\) for the actual scales t>=1/8. Panels are split when interval evaluation cannot prove finiteness. This ensures the principal branches used by the finite algebraic profile are analytic on the ellipse.

If M bounds |f| on that ellipse, its degree2n-1 Chebyshev truncation has uniform error at most \(4M2^{-2n}\). Gaussian quadrature with n nodes is exact on that polynomial and has positive weights summing to2h. Comparing both the integral and quadrature to the polynomial gives total error at most \(16hM2^{-2n}\). `arb.legendre_p_root(n,k,weight=True)` encloses the exact nodes and weights. All point values and summation use Acb. The run used188 adaptive panels between1e-4 and1000 and saved per-panel enclosures/checkpoints.

### Origin and far tails

At the origin, actual exact power expansions of the pruned profile bound bx and by uniformly on r<=1e-4. Entire basis modes are enclosed on the same radius interval. Direct bounds on Dx,Dy give the omitted origin integral below5.15e-16.

For phi01=c*y*exp(-r²/2), c=sqrt(2/pi), its Riesz vector satisfies
\[
|R\varphi_{01}(X)|\le5|X|^{-3},\qquad |X|\ge16.
\]
Indeed H=(-Delta)^-1/2 exp(-r²/2) has the positive Laplace representation
\[
H(r)=\pi^{-1/2}\int_0^{1/2}\frac{e^{-vr²}}{\sqrt v\sqrt{1-2v}}\,dv,
\qquad R\varphi_{01}=-c\,\partial_y\nabla H.
\]
On v<=1/4 use (1-2v)^-1/2<=sqrt2 and extend the Gamma integrals to infinity. This bounds the derivative vector by \((8/\sqrt\pi)r^{-3}\). The part v>=1/4 is bounded by \((1+r²)e^{-r²/4}\). For r>=16 the sum is below5r^-3. Fourier inversion also gives \(|U\varphi_{01}|\le2/\pi\).

The exact far expansion of the pruned profile gives a uniform G bound for |bx|+|by| on r>=R. Since ||Kmat||<=G, the source tail is at most
\[
G\left[4c(R+R^{-1})e^{-R²/2}+\frac{25\pi}{2R^4}\right].
\]
At R1000, the stored exact-data G bound is below1.642814; this tail is below6.452e-11.

### A genuine finite-rank operator and its tail formula

The operator \(\mathcal K_NG=A_{11}\langle G,\varphi_{01}\rangle\varphi_{01}\) is an actual smooth rank-one compression. Once an actual certified upper kappa of \(\|\mathcal K_s\|_{HS}\) is supplied,
\[
\|\mathcal K_s-\mathcal K_N\|_{op}\le
\|\mathcal K_s-\mathcal K_N\|_{HS}
\le\sqrt{\kappa²-|A_{11}|²}.
\]
The Hilbert-Schmidt orthogonality is exact. Thus the certificate is constructive; it is not yet quantitatively sufficient for full existence. A11<0 also means its finite part can be discarded in an upper-energy estimate, although its absolute low-order price is the C_N recorded above.

For higher ranks and the S1 sector, exploit that Ks commutes with both reflections. The four parity sectors are orthogonal. Subtract any certified captured squared entries from the other three sectors from the full HS² upper before bounding the S1 tail. This avoids a separate4D parity-kernel integral. Current larger all-parity matrices are only FLOAT screens.

## Whole compact remainder screens

`full_remainder_screen.py` computes the original conjugated energy E in a Cartesian Hermite Galerkin space, the full principal matrix form, the negative qA pR sandwich, and two equivalent compact matrices Krest and Kc. All finite-box FFT, radial spline interpolation and roundoff errors remain uncertified.

At rank136, degree31, alpha1, grid512, radius24, the FLOAT largest eigenvalue of Krest is .56444 and that of Kc is1.02306. The full-matrix dual compression D for beta0=.3,.4,.5 gives FLOAT largest eigenvalues of D^1/2 Kc D^1/2 respectively .71557,.79745,.91386. These margins support pursuing full-matrix finite-core absorption, but prove no operator inequality.

The existing rank10 and rank36 low-order C_N screens are small (about257 and798 at alpha1), compared with the inherited price room above1e11. The hard remaining issue is the full compact operator-norm tail, together with certification of the larger profile-dependent matrices.

## Residual-test helper

`fractional_riesz_gaussian.py` provides FLOAT radial modes of Phi=R J^-0.1 psi for normalized Gaussian derivative tests, including an explicit physical-width interface. The heat substitution t=z²⁰ removes the endpoint singularity. Its narrow-width three-by-three L2 Gram is independently certified in `fractional_riesz_gaussian_gram_narrow.json` by
\[
\langle\Phi_a,\Phi_b\rangle=a²b²U(2,2.9,(a²+b²)/2),
\]
where a,b are physical widths. This Gram does not certify the full-M weighted integral; that further certificate remains separate.

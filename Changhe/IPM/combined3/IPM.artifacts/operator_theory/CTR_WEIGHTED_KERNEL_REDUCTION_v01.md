# An explicit weighted transport-kernel reduction

Status: exact algebra, proved universal kernel majorants, and an executed 574-interval scalar certificate. Profile-dependent Fourier moments remain to be bounded. No numerical Ctr operator norm is claimed.

Let \(u_*=\nabla^\perp\psi_*\), q=21/10, and let Ctr be the **old N-norm** transport remainder in `../EXACT_COMPACT_DECOMPOSITION.md`. Put \(A=JC_{tr}J\). The stream function is the actual finite-potential stream of Candidate 013. It has all-order symbol growth 2-gamma, gamma=1-1/c>0.

## Exact preconditioned Fourier kernel

Write \(a=\langle\xi\rangle\), \(b=\langle\eta\rangle\), \(\tau=a/b\), \(\zeta=\xi-\eta\), and
\[
H(\tau)=\tau^q-\tau^{-q}-q(\tau-\tau^{-1}).
\]
The Hermitian transport commutator kernel before preconditioning is
\((i/2)(\eta\cdot\widehat u_*(\zeta))H(\tau)\).
The qS principal form has already been subtracted in H. Since div u=0 and \(\widehat u=i\zeta^\perp\widehat\psi\), the preconditioned kernel is exactly
\[
C(\xi,\eta)=-F(\xi,\eta)\widehat\psi_*(\zeta),\qquad
F=\tfrac12ab(\xi_1\eta_2-\xi_2\eta_1)H(a/b).
\tag{1}
\]
The overall sign has no effect on the norm bounds below. Fourier convolutions carry factor (2pi)^-2.

## Certified scalar bounds

For every tau>=1 the companion code proves
\[
|H(\tau)|\le3(\tau-1)^3\tau^{q-3},\quad
|H'(\tau)|\le9(\tau-1)^2\tau^{q-3},\quad
|H''(\tau)|\le18(\tau-1)\tau^{q-3}.
\tag{2}
\]
The proof covers [1,1.01] by exact Taylor coefficients through degree four and a rational bound on the remaining power-series coefficients, [1.01,4] by 574 containing Arb Taylor/Cauchy intervals, and [4,infinity) by direct algebraic power bounds. In particular the scalar certificate is a continuum bound and not a grid maximum. The output is `Ctr_kernel_constants_result.json`.

Here are the analytic details for its two noncompact endpoints. At tau=1+x the first nonzero coefficients are a3=2387/1000 and the exact a4 obtained from binomial(q,4)-binomial(-q,4)+q. For j>=5, the absolute coefficient is at most 2j², since 2<q<3. Differentiation up to order two and summing the positive geometric-polynomial tails at x=.01 proves the near bounds. For tau>=4, H is nonnegative and H<=tauq. Also H' is nonnegative and H'<=q tau^(q-1). Finally
\[
|H''|\le q(q-1)\tau^{q-2}+q(q+1)\tau^{-q-2}+2q\tau^{-3}.
\]
Dividing by the targets in (2), and using 1-1/tau>=3/4, proves the far bounds by the exact rational comparisons in the code.

## Uniform Cartesian derivative bounds

Let z=|zeta| and define \(Z_j(z)=z^j+z^{q+2}\), j=2,3,4. Then for all xi,eta, including limits at zero,
\[
\boxed{|F|\le2Z_4(z),\quad
|\partial_{\xi_i}F|\le20Z_3(z),\quad
|\partial_{\eta_j}F|\le20Z_3(z),\quad
|\partial_{\xi_i}\partial_{\eta_j}F|\le60Z_2(z).}
\tag{3}
\]
These are componentwise estimates, without sums over i,j.

For verification put c=xi cross eta and denote logarithmic tau derivatives by dots, so dot H=tau H' and ddot H=tau H'+tau²H''. Direct differentiation gives
\[
\partial_{\xi_i}F=\tfrac12ab[c_{\xi_i}H+c\xi_i a^{-2}(H+\dot H)],
\]
\[
\partial_{\eta_j}F=\tfrac12ab[c_{\eta_j}H+c\eta_j b^{-2}(H-\dot H)],
\]
\[
\partial_{\xi_i}\partial_{\eta_j}F=\tfrac12ab[
c_{\xi_i\eta_j}H+c_{\xi_i}\eta_jb^{-2}(H-\dot H)
+c_{\eta_j}\xi_ia^{-2}(H+\dot H)
+c\xi_i\eta_j(a^2b^2)^{-1}(H-\ddot H)].
\tag{4}
\]
By symmetry assume a>=b. Then |c|<=bz, |c_xi|<=b, |c_eta|<=a, |c_xi_eta|<=1, delta=a-b<=z, and tau<=1+z. Equations (2),(4) give the sharper intermediary bounds
\[
|F|\le\tfrac32z^4\tau^{q-2},\quad
|D_{\xi,\eta}F|\le\tfrac{15}{2}z^3\tau^{q-1},
\]
\[
|D_\xi D_\eta F|\le\tfrac32z^3\tau^{q-2}+27z^2\tau^{q-1}.
\]
Split at z=1 and use the certified rational bound 2^(1/10)<27/25. The respective coefficients are at most 1.62, 16.2, and 59.94, proving (3) with its simple integer bounds.

## A concrete weighted Schur certificate obligation

All derivatives below are of the actual stream transform on zeta!=0. Define positive integrable majorants
\[
k_{00}=2Z_4|\widehat\psi|,
\]
\[
k_{i0}=20Z_3|\widehat\psi|+2Z_4|\partial_i\widehat\psi|,
\quad k_{0j}=20Z_3|\widehat\psi|+2Z_4|\partial_j\widehat\psi|,
\]
\[
k_{ij}=60Z_2|\widehat\psi|+
20Z_3(|\partial_i\widehat\psi|+|\partial_j\widehat\psi|)
+2Z_4|\partial_i\partial_j\widehat\psi|.
\tag{5}
\]
Set a 3-by-3 nonnegative symmetric upper matrix D by
\[
D_{00}=(2\pi)^{-2}\int k_{00},\quad
D_{i0}=D_{0i}=2(2\pi)^{-2}\int k_{i0},\quad
D_{ij}=4(2\pi)^{-2}\int k_{ij},\quad i,j=1,2.
\tag{6}
\]
Then
\[
\boxed{\|WJC_{tr}JW\|_{2\to2}\le\|D\|_{\mathrm{op}}
\le\max_a\sum_bD_{ab}.}
\tag{7}
\]
To prove it use Lf=(f,2x1f,2x2f), so L*L=W² and LW^-1 is an isometry. Thus
\(WAW=(W^{-1}L^*)(LAL^*)(LW^{-1})\).
The nine kernels of LAL* are C, the first Cartesian derivatives of C with factors two, and the mixed derivatives with factors four. Equations (3)--(5) and Young's convolution inequality bound their norms by the entries of D. The matrix operator norm bounds their block operator norm, proving (7).

The moment integrals in (5) are finite for the actual profile. The stream symbol growth gives, away from zero,
\(|D^\alpha\widehat\psi(\zeta)|=O(|\zeta|^{\gamma-4-|\alpha|})\) at small frequency, and rapid decay at large frequency after sufficiently many physical integrations by parts. Every integrand in (5) is therefore locally integrable: the worst exponent is gamma-2 in dimension two. The full product C is O(|zeta|gamma) near the diagonal; its first and second weak derivatives have no point-supported contact term, since the shrinking boundary integrals are O(rgamma). This also justifies applying the Schur argument to the actual growing stream, rather than an uncharged periodic truncation.

## Consequence once actual moment uppers are supplied

For \(h=W^{-1}J^{-1}G\), (7) yields
\[
|C_{tr}(G)|\le C_H\|h\|_2^2,\qquad C_H=\|D\|_{\mathrm{op}}.
\]
The independently proved lower-norm bound in `BESSEL_WEIGHT_LOWER_NORM_v01.md` then gives an explicit interpolation price in terms of ||g||2 and its qth homogeneous derivative. This is a quantitative implementation route with fixed universal constants. **No actual upper for the moment matrix D has yet been computed here**, so it is not a completed Ctr certificate.

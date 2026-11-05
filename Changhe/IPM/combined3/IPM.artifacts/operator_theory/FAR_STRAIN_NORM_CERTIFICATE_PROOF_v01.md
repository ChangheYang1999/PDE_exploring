# Proof of the far-strain radial norm certificate

This document specifies the analytic and numerical enclosure performed by `certify_far_strain_norms_v01.py`. The running panel producer is restartable. A complete result requires every planned panel and both endpoint records; a partial directory is not a certificate.

The actual coefficient is
\[
S_f=(1-\chi(r/2))\operatorname{Sym}Du_*,
\quad\chi(r)=\tfrac12\operatorname{erfc}(\log(r/\sqrt8)/\ell),
\quad\ell=\log8/(2\sqrt\pi).
\]
This is an auxiliary strain split. The scalar near/far split of the inherited weight commutators remains unchanged. The exact background density, velocity, and c are unchanged.

## Quantities being enclosed

Set
\[
D_2=\|\Delta S_f\|_{2,F},\quad
D_3=\|\nabla\Delta S_f\|_{2,F},\quad
D_4=\|\Delta^2S_f\|_{2,F}.
\]
The trace of S_f is zero, so its Frobenius norm squared is twice the sum of the squared norms of its 11 and 12 entries. Their exact finite angular expansions have radial coefficients f_n(r). For a mode of frequency n the radial Laplacian is
\(L_nf=f''+r^{-1}f'-n^2r^{-2}f\). Its angular integral factor is 2pi for a constant cosine and pi for every other nonzero sine or cosine mode. The zero sine mode is omitted.

Consequently the radial densities for the three squared norms, including the radial Jacobian and trace-free factor two, are the sums of
\[
2c_nr\,(L_nf_n)^2,\quad
2c_nr\,[(L_nf_n)'^2+n^2r^{-2}(L_nf_n)^2],\quad
2c_nr\,(L_n^2f_n)^2,
\tag{1}
\]
over both independent entries and every actual mode. No angular quadrature or harmonic truncation is used. The conventions in (1) were independently checked by the coercivity/residual agent against the actual evaluator and ordered derivative convention.

## Middle region: actual Taylor coefficients and Cauchy tails

The planned radial region is [1/16,1024]. On each dyadic annulus [2^k,2^(k+1)], k=-4,...,9, split into 128 equal radial subintervals. There are exactly 1,792 panels with rational endpoints. Their interiors are disjoint and their closed union is the full region.

For a panel with center r and half-width h, the actual source evaluator computes radial Taylor coefficients of the strain entries through degree 84, in 512-bit Arb arithmetic, after all exact polynomial grouping and cancellations. Multiplication by the exact erflog far-cut series gives the actual S_f coefficients. Source and code hashes are bound in every record.

The source Cauchy majorant is computed on the complex disk |z-r|<=r/8, using the containing potential disk r/4. Every t+z² stays in the right half plane, so the positive radial powers have their specified analytic branches. The source-majorant implementation is the same frozen exact-source code used by the other campaign certifiers.

Here is the additional cut majorant. On that disk, |z| lies in [7r/8,9r/8] and |arg z|<=arcsin(1/8). Put w=-log(z/(2sqrt8))/ell, x=Re w, and Y=arcsin(1/8)/ell. Its real part belongs to the explicit interval [x_lo,x_hi] computed in the code. Integration along the vertical segment gives
\[
\tfrac12|\operatorname{erfc}(x+iy)|
\le\tfrac12\operatorname{erfc}(x)+\frac{|y|}{\sqrt\pi}e^{-x^2+y^2}.
\]
Thus a containing disk bound for |1-chi(z/2)| is
\[
\tfrac12\operatorname{erfc}(x_{lo})+
\frac{Y}{\sqrt\pi}e^{Y^2-\operatorname{dist}([x_{lo},x_{hi}],0)^2}.
\tag{2}
\]
Arb encloses all terms and the interval distance is rounded in the safe direction.

Let B_n be the resulting source-times-cut bound for one radial coefficient on the disk R=r/8. On the disk R/2, its jth derivative is bounded by j! B_n/(R/2)^j. The actual derivative Taylor polynomial is known through degree 84-j. Therefore on the real panel its omitted tail is bounded by
\[
\frac{j!B_n}{(R/2)^j}
\frac{(h/(R/2))^{85-j}}{1-h/(R/2)},\qquad j=0,1,2,3,4.
\tag{3}
\]
All ratios are strictly below one. The producer evaluates each actual derivative polynomial on [-h,h] and adds (3) as a centered interval. It then uses the explicit identities
\[
\begin{aligned}
L_nf&=f''+f'/r-n^2f/r^2,\\
(L_nf)'&=f'''+f''/r-(1+n^2)f'/r^2+2n^2f/r^3,\\
L_n^2f&=f''''+2f'''/r-(1+2n^2)f''/r^2
+(1+2n^2)f'/r^3+(n^4-4n^2)f/r^4.
\end{aligned}
\tag{4}
\]
These give containing intervals throughout the panel. The upper of (1) times panel width is therefore a rigorous integral upper. Every stored energy upper is an exact dyadic rational obtained from Arb's exact endpoint; no floating-point display is accepted as an endpoint.

## Endpoint source bounds

The endpoint implementation uses the exact finite origin and far expansions of the actual potential, at degree 18. It reuses the frozen `asymptotics013.py` implementation, including its exact rational coefficient grouping and Cauchy geometric remainder. In its notation N=19, which exceeds twice every differential order used (the largest potential order is eight). Its required geometric ratio is below 1/4 at each endpoint used.

For the origin, expand the source strain on |z|<=9r0/8, r0=1/16. Every nonzero radial power is nonnegative; therefore its absolute coefficient bound at 9r0/8 bounds the full complex disk. For the far endpoint R0=1024, all strain powers are <=-gamma, gamma=1-1/c. The expansion bound at 7R0/8 gives a complex-disk bound M_f(r/R0)^(-gamma) on |z-r|<=r/8 for every r>=R0. The remainder coefficients are fixed at the endpoint and their geometric factors improve further outward.

Each harmonic has frequency at most 162: the base potential has maximum frequency 158 and takes four Cartesian derivatives to form strain; the correction has maximum frequency 159 and takes three. Four times (162+1)=652 bounds the total number of sine/cosine coefficients in the two independent entries. This deliberately coarse count is used only in exponentially small endpoint errors.

## Gaussian endpoint factors and integral bounds

The erfc inequality erfc(x)<=exp(-x²)/(sqrt(pi)*x), x>0, combined with the same vertical-segment argument as (2), gives
\[
|1-\chi(z/2)|\le K_0e^{-[\log(C_0/r)/\ell]^2},
\quad C_0=16\sqrt8/9,\quad0<r\le r_0,
\]
\[
|\chi(z/2)|\le K_fe^{-[\log(C_fr)/\ell]^2},
\quad C_f=7/(16\sqrt8),\quad r\ge R_0,
\tag{5}
\]
on the complex radial disks, with the explicit positive endpoint constants in the code. For each radial harmonic, Cauchy's derivative estimate with radius r/16 and (4) give the squared multipliers
\[
a_n^2,\quad b_n^2+n^2a_n^2,\quad c_n^2,
\]
where
\[
a_n=528+n^2,\quad b_n=25104+18n^2,
\quad c_n=1622544+1056n^2+|n^4-4n^2|.
\]
Their values at n=162 bound all frequencies occurring. Inserting the uniform source bound and (5) into (1) reduces every endpoint correction to the closed Gaussian integral
\[
\int_0^{r_0}r^{p-1}e^{-2[\log(C/r)/\ell]^2}\,dr
=C^p e^{p^2\ell^2/8}\frac{\ell\sqrt\pi}{2\sqrt2}
\operatorname{erfc}\left(\frac{\sqrt2}{\ell}[\log(C/r_0)+p\ell^2/4]\right),
\]
or
\[
\int_{R_0}^{\infty}r^{p-1}e^{-2[\log(Cr)/\ell]^2}\,dr
=C^{-p}e^{p^2\ell^2/8}\frac{\ell\sqrt\pi}{2\sqrt2}
\operatorname{erfc}\left(\frac{\sqrt2}{\ell}[\log(CR_0)-p\ell^2/4]\right).
\tag{6}
\]
These formulas follow by completing the square after logarithmic substitution. Arb evaluates them directly.

At infinity write S_f=S-chi(r/2)S. The actual physical Laplacian energies of S are bounded by the exact far-expansion integral bounds for the required Cartesian velocity derivatives through order five. Minkowski bounds the correction norm using (5)--(6); its sum with the source tail norm is squared to give the exterior energy upper. Thus the exterior interval is charged in its entirety.

## Assembly and scope

The assembler requires every panel index, exact parameter identity, and matching frozen code bindings; it then sums the exact dyadic panel and endpoint upper energies. Taking upward Arb square roots yields D2,D3,D4 upper bounds. The separate proved Fourier moment inequality gives
\[
M_2(S_f)\le\sqrt{(D_2D_4+D_3^2)/(2\pi)}.
\]
The target test M2<11/20 is checked by interval comparison only after the complete sum exists. The exact TIS reduction then yields the corresponding p-damping charge (q/2)M2. A successful target check would certify this component; it would not bound any other commutator or establish an invariant ball.

Each worker writes one immutable panel JSON at a time and skips an existing panel only after checking its full metadata. A host restart loses at most the in-flight panel; its shard command can be rerun. No passing target is claimed while the certificate is incomplete.

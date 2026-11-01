# A canonical whole-plane extension of every convergent exterior potential

Status: CONFIRMED, with the proof reviewed and adopted in the theory part's theory Section 12. The extension solves the stationary equation only outside a disk. It is not a global stationary solution.

## Statement

Let `0<gamma<1`, and let `chi_ext` be a smooth potential on `r>R_0`, even in `x` and in `y`, with

\[
 |D^j\chi_{\rm ext}(X)|\le C_j r^{\gamma+3-j},\qquad r\ge R_1>R_0,
\tag{1}
\]

for every derivative order `j`. Suppose its density `rho_ext=-partial_y Delta chi_ext` and velocity `u_ext=(-partial_y psi_ext,partial_x psi_ext)`, where `psi_ext=partial_x partial_y chi_ext`, solve the stationary self-similar IPM equation on `r>R_0`.

For any `R_2>R_1>R_0`, there is a smooth whole-plane pair `(rho,u)` with S1 symmetry that agrees with `(rho_ext,u_ext)` on `r>=R_2`, has `rho=O(r^gamma)`, and satisfies the canonical Poisson/Biot-Savart relation on the whole plane. Its stationary residual is smooth and compactly supported in `r<=R_2`.

Here the canonical stream is defined precisely as the unique smooth S1 stream, odd in both Cartesian variables, that solves

\[
 -\Delta\psi=\partial_x\rho,\qquad \psi=o(r^2).
\tag{2}
\]

It is also obtained from the symmetric-cutoff whole-plane Green integral. No arbitrary exterior harmonic multipoles are needed for this constructed extension.

The convergent potentials in topics 13 and 14 satisfy all the hypotheses. Thus the canonical-velocity issue does not obstruct extending those exterior solutions as smooth canonical density/velocity pairs. The additional requirement of stationarity inside the disk remains open.

## Construction

Take a smooth radial cutoff `eta` that is zero on `r<=R_1` and one on `r>=R_2`. Define

\[
 \chi(X)=\begin{cases}\eta(r)\chi_{\rm ext}(X),&r>R_1,\\0,&r\le R_1,\end{cases}
 \qquad
 \rho=-\partial_y\Delta\chi,\quad
 \psi=\partial_x\partial_y\chi,\quad
 u=(-\psi_y,\psi_x).
\tag{3}
\]

The cutoff can be chosen flat at the joining radii, so these fields are smooth. They retain their stated symmetries. Commutation of derivatives gives `-Delta psi=partial_x rho`. Bound (1) gives

\[
 |\rho(X)|\le C(1+r)^\gamma,\quad
 |\partial_x\rho(X)|\le C(1+r)^{\gamma-1},\quad
 |\psi(X)|\le C(1+r)^{\gamma+1}=o(r^2).
\tag{4}
\]

They agree with the exterior fields beyond `R_2`. Consequently their stationary residual is zero there and is smooth everywhere, so its support is contained in the closed disk of radius `R_2`.

It remains to identify the stream in (3) with the canonical whole-plane inverse. The following argument also establishes existence and uniqueness of that inverse in the required growth class.

## Symmetric Green integral

Write `h=partial_x rho`. It is odd in `x`, odd in `y`, and satisfies the second bound in (4). Let `S_x(y_1,y_2)=(-y_1,y_2)` and `S_y(y_1,y_2)=(y_1,-y_2)`. Define

\[
 K(X,Y)=\frac14\bigl[\log|X-Y|-\log|X-S_xY|
                       -\log|X-S_yY|+\log|X+Y|\bigr].
\tag{5}
\]

By the two odd symmetries, integration against `h` on any disk centered at zero is unchanged if `log|X-Y|` is replaced by `K(X,Y)`. Constant and linear terms in the expansion at large `|Y|` cancel in (5), so, uniformly for `X` in a fixed compact set,

\[
 |K(X,Y)|\le C_X |Y|^{-2}\quad (|Y|>2|X|+1).
\tag{6}
\]

Therefore

\[
 \psi_{\rm can}(X)=-\frac1{2\pi}\int_{\mathbb R^2}K(X,Y)h(Y)\,dY
 =-\frac1{2\pi}\lim_{T\to\infty}\int_{|Y|<T}\log|X-Y|h(Y)\,dY
\tag{7}
\]

converges. Its tail is absolutely convergent, because its radial majorant is `C_X r^{gamma-2}`, which is integrable at infinity for `gamma<1`. The logarithmic singularities at the four reflected points are locally integrable.

The fundamental-solution identity `-Delta[-log|X-Y|/(2 pi)]=delta_Y` and reflection parity show that `-Delta psi_can=h`. Equivalently, applying `-Delta_X` to (5) yields a quarter of four reflected delta masses, whose integrals against `h` add to `h(X)`. This equality is valid in distributions. Splitting the integral into a compactly supported smooth source and its distant tail proves smoothness: the local logarithmic potential is smooth for a smooth source, and derivatives of the distant kernel converge locally uniformly. The same parity in `X` shows that `psi_can` is odd in each coordinate.

Its growth is subquadratic. For `|X|=r>=1`, split the integral into `|Y|<=2r` and its complement. In the first region, put `Y=rZ`; the four `log r` terms in (5) cancel. The integral is bounded by `C r^{gamma+1}` times a uniformly bounded integral of `|Z|^{gamma-1}` times four logarithmic kernels on `|Z|<=2`. Uniform boundedness follows by splitting into `|Z|<1/2` and `1/2<=|Z|<=2`: on the first set the reflected singularities are absent and the weight is integrable; on the second set the weight is bounded and logarithmic singularities have a uniform integrable bound. In the outer region, (6) can be taken as `C r^2/|Y|^2`, giving

\[
 C r^2\int_{2r}^{\infty}s^{\gamma-2}\,ds
 \le C' r^{\gamma+1}.
\]

Thus `psi_can=O(r^{gamma+1})=o(r^2)`.

## Uniqueness and canonical agreement

The difference `H=psi-psi_can` is a smooth harmonic function on the whole plane, odd in both variables, and `H=o(r^2)`. The harmonic coefficient estimates on a circle of radius `T` give, for each homogeneous harmonic coefficient of degree `k>=2`, a bound proportional to `T^{-k} sup_{|X|=T}|H(X)|`, which tends to zero. Hence `H` is affine. An affine function odd in each of `x` and `y` must vanish. Therefore `psi=psi_can` and the velocities agree.

Differentiating (7) also gives the canonical velocity integral with the same symmetric cutoff. It has no added harmonic field. The symmetry and growth normalization are part of this canonical definition; without them a Poisson inverse is not unique.

## Multipoles for other interior extensions

For a different smooth density extension with the same exterior density, the difference from (3) is a compactly supported S1 density `v`. Its change in exterior stream has the multipole coefficients derived in topic 08:

\[
 \Delta\beta_j=-\frac1{2\pi}\int
       \operatorname{Im}\bigl((y_1+i y_2)^{2j-1}\bigr)\,v(Y)\,dY.
\tag{8}
\]

Consequently the mismatch coefficients are moments of the **difference from a chosen extension whose stream agrees with the series**. Calling them moments of the interior density alone omits this reference term. The particular cutoff-potential extension (3) has zero mismatch by construction and the uniqueness proof above. It is not claimed to make the stationary residual vanish inside the disk.

## Dependencies and scope

The dependencies are the potential identities and growth estimates of topics 01, 13 and 14, the compact multipole calculation in topic 08, the planar logarithmic fundamental solution, and the elementary harmonic expansion on disks. The argument uses no numerical approximations and no formal proof assistant.

The result is kinematic plus exterior stationarity. It establishes neither a smooth global stationary self-similar IPM solution nor a way to eliminate the compact interior residual while keeping the required far field.

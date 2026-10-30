# Canonical strain, origin compatibility and scaling

## Statement and hypotheses

The density has S1 parity: it is real, even in x and odd in y. On Schwartz densities define

\[
G(X)=-\frac1{2\pi}\log |X|,\qquad
\psi[h]=G*\partial_xh,\qquad
U[h]=(-\partial_y\psi,\partial_x\psi).
\]

Thus \(-\Delta\psi=\partial_xh\), and the Fourier multiplier of U is
\((\xi_1\xi_2/|\xi|^2,-\xi_1^2/|\xi|^2)\). The strain is
\(c[h]=\partial_yU_2[h](0)\). Write \(b[h]=\partial_yh(0)\).

The following conclusions hold.

1. For Schwartz h,
   \[
   c[h]=-\frac14b[h]+\frac1\pi\operatorname{PV}_{\rm circ}
          \int_{\mathbb R^2}\frac{\sin(3\theta)}{r^3}h(X)\,dX.
   \tag{1}
   \]
   The same formula defines the strain for locally \(C^{1,\alpha}\) densities, \(\alpha>0\), with \(|h(X)|=O(r^\beta)\), \(\beta<1\), whenever the canonical extension of the velocity has this distributional derivative. It is not a construction of that extension for arbitrary growing densities.
2. Let a reference \(\bar\rho\) and its canonical velocity be \(C^1\) near zero with S1 parities. Put \(a=b[\bar\rho]\), \(d=c[\bar\rho]\), \(V=c_lX+U[\bar\rho]\), and
   \[
   Lh=V\cdot\nabla h-h+U[h]\cdot\nabla\bar\rho.
   \]
   If h,k and their velocities are \(C^1\) near zero, then the function
   \(f=(L+U[k]\cdot\nabla)h\) has a derivative at zero and
   \[
   \partial_y f(0)=(c_l+d-1+c[k])b[h]+a\,c[h].\tag{2}
   \]
   In particular, if \(c_l+d=1\), \(a\ne0\), and \(c[k]=0\), then \(f_y(0)=0\) if and only if \(c[h]=0\).
3. At fixed exponent, a decaying correction class fixes a nonzero leading tail \(r^\gamma\Theta\), \(0<\gamma<1\), against the dilation \(S_t\rho(X)=t\rho(X/t)\). Prescribing the center slope alone does not fix this dilation.

## Proof of the contact term

Distributional differentiation of G gives

\[
\partial_x^2G=\operatorname{PV}_{\rm circ}
 \frac{\cos(2\theta)}{2\pi r^2}-\frac12\delta_0.
\]

One can check the delta coefficient by summing the analogous x and y identities, obtaining \(\Delta G=-\delta_0\), and using rotational symmetry to make the two local coefficients equal. Away from zero the displayed kernel follows by ordinary differentiation.

The kernel is even, so its convolution with \(\partial_yh\) evaluated at zero yields

\[
c[h]=-\frac12b[h]+\lim_{\epsilon\downarrow0}
 \int_{r>\epsilon}\frac{\cos(2\theta)}{2\pi r^2}\partial_yh(X)\,dX.
\]

Integrate by parts on \(\epsilon<r<R\). The outer boundary vanishes as \(R\to\infty\). On the inner boundary the outward normal of the annulus is \(-e_r\). Since \(h(\epsilon,\theta)=b[h]\epsilon\sin\theta+o(\epsilon)\), its contribution tends to

\[
-\frac{b[h]}{2\pi}\int_0^{2\pi}\cos(2\theta)\sin^2\theta\,d\theta
=\frac14b[h].
\]

Finally,
\(\partial_y[\cos(2\theta)/(2\pi r^2)]
=-\sin(3\theta)/(\pi r^3)\), which proves (1).

For local \(C^{1,\alpha}\) regularity subtract \(b[h]y\eta(r)\), where \(\eta\) is smooth, radial, compactly supported and one near zero. Its angular pairing with \(\sin(3\theta)\) is zero for every r. The subtracted integrand has absolute radial majorant \(Cr^{\alpha-1}\), which is integrable at zero. The exterior majorant is \(Cr^{\beta-2}\), integrable at infinity precisely for this sufficient condition \(\beta<1\). The local coefficient remains \(-b[h]/4\).

As a direct check, \(h=y e^{-r^2}\) has \(b[h]=1\) and no third angular harmonic, so (1) gives \(c[h]=-1/4\). In Fourier variables the ratio of the relevant angular integrals is
\(\int\cos^2\theta\sin^2\theta/\int\sin^2\theta=1/4\), and the multiplier has negative sign. A formula omitting the contact term gives zero and is false.

## Proof of the origin identity

Parity gives \(h(X)=b[h]y+o(r)\), \(\nabla h(X)=(0,b[h])+o(1)\), and \(U[h](0)=0\). Velocity parity and incompressibility give

\[
DU[h](0)=\begin{pmatrix}-c[h]&0\\0&c[h]\end{pmatrix}.
\]

Therefore
\[
V(X)=((c_l-d)x,(c_l+d)y)+o(r),\qquad
U[k](X)=(-c[k]x,c[k]y)+o(r).
\]

Substitution into f gives its linear term (2), with an \(o(r)\) remainder. No second derivative of h is used: vanishing of the transport field at zero supplies the factor r. For a reference residual,
\(\partial_yF(\bar\rho;c_l)(0)=a(c_l+d-1)\).

The different, variable-exponent chart \(c_l[\rho]=1-c[\rho]\) has derivative
\[
L_{\rm norm}h=Lh-c[h]X\cdot\nabla\bar\rho.
\]
Its first y-jet vanishes for every h when the reference is normalized. Thus this operator cannot be onto an unrestricted forcing class retaining a y-derivative trace. A bound for \(L_{\rm norm}\) is not a bound for L, or conversely, without handling this finite-rank term and range condition.

## Proof of the scaling assertions

Dilation covariance of the canonical inverse gives
\[
U[S_t\rho](X)=tU[\rho](X/t),\quad
c[S_t\rho]=c[\rho],\quad b[S_t\rho]=b[\rho].
\]
The last identity proves that a fixed center slope leaves the dilation unchanged. The residual obeys
\(F(S_t\rho;c_l)(X)=tF(\rho;c_l)(X/t)\). Its derivative at \(t=1\), for smooth profiles for which that derivative is defined, is

\[
L_\rho(\rho-X\cdot\nabla\rho)
=F(\rho;c_l)-X\cdot\nabla F(\rho;c_l).
\]

This is zero at an exact profile; it is generally nonzero at a numerical reference. Meanwhile the leading angular coefficient becomes \(t^{1-\gamma}\Theta\). A correction o(\(r^\gamma\)) cannot absorb this change for \(t\ne1\) and \(\Theta\ne0\). In the baseline space \(N_s\), continuity and vanishing at infinity follow from its Sobolev embedding and L2 membership; therefore this correction class fixes the leading coefficient.

## Dependencies and scope

The proof independently checks the identities in the copied baseline notes. It neither constructs a full-plane inverse nor verifies any numerical profile coefficients. A trace constraint is used only in a topology where the trace is continuous. The low norm alone cannot supply the strain trace. No formal verification was run.

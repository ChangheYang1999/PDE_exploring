# Angular contrast and the limitation of multiplier positivity

Status: CONFIRMED by an independent argument, 2026-10-20. Exact checks are
recorded in `verification/`. This result audits SGN2-A/B of the lead's frozen
proof, recorded with its hash in `../../evidence/sgn2_audit/`.

## Statement and conventions

Let \(X=(x,y)\), \(r=|X|\), and let \(q\) be smooth and even in both
coordinates, with \(q(0)=1\). Assume for some \(p<1\) that
\(D^j q=O(r^{p-1-j})\) at infinity, for \(j=0,1\).
Set \(\rho=a yq\), where \(a\ne0\). Let
\(U=(-\psi_y,\psi_x)\) be the canonical full-plane velocity satisfying
\(-\Delta\psi=\rho_x\), with the sublinear gauge. Write
\(c=\psi_{xy}(0)\), and suppose \(c=-D\), \(D>0\).
These hypotheses hold for an exact primary profile with
\(a=\rho_y(0)\), \(D=\ell-1\), \(p=1/\ell\), by the independently
proved symbol bounds and smooth odd division. The argument below does not
require the no-extra-equilibrium hypothesis.

Define
\[
 {
 \cal A}(q)=\int_0^\infty
   \left(\max_{0\le\theta\le\pi/2}q(r,\theta)
        -\min_{0\le\theta\le\pi/2}q(r,\theta)\right)\frac{dr}{r}.
\]
Then \({\cal A}<\infty\). If \({\cal A}>0\),
\[
 \left|\frac D a-\frac14\right|
   <\frac{3\sqrt3}{4\pi}{\cal A}.                    \tag{1}
\]
If \({\cal A}=0\), then \(a=4D\). In particular,
\({\cal A}\le\pi/(3\sqrt3)\) implies \(a>2D\).
For \(z=3\sqrt3{\cal A}/\pi\) in the strict interval \(0<z<1\),
\[
 \frac4{1+z}<\frac aD<\frac4{1-z}.                  \tag{2}
\]
The exceptional case \(z=0\) has equality \(a/D=4\), not the strict
inequalities in (2). The constant in (1) is sharp among smooth positive
functions satisfying these decay and origin conditions and having a
positive value of \(D/a\). Sharpness does not assert existence of exact
transport profiles.

Separately, let \(T\) be the Fourier multiplier
\(\widehat{Tg}(\xi)=\xi_x^2|\xi|^{-2}\widehat g(\xi)\), equal to
\(-U_2[g]\) with these conventions. Although \(\int gTg\ge0\), there
exist smooth \(g\) of the density parity, positive in \(y>0\), and a
smooth strictly positive even-even weight \(w\) such that
\[
 \int_{\mathbb R^2}wgTg<0.                          \tag{3}
\]
Thus the unweighted multiplier sign alone cannot justify a weighted
pointwise or quadratic positivity step.

## Proof of the angular identity

Evenness and smoothness imply, uniformly in angle,
\(q=1+O(r^2)\), \(q_r=O(r)\), and \(q_\theta=O(r^2)\) near zero.
At infinity the assumed bounds give \(q=O(r^{p-1})\),
\(q_r=O(r^{p-2})\), and \(q_\theta=O(r^{p-1})\). These bounds prove
convergence of \({\cal A}\).

The canonical strain formula, independently derived in
`../strain_sign/PROOF.md`, gives
\[
 \frac ca=\frac4\pi\int_{x,y>0}\frac{xy^2}{r^4}q_x\,dX.
\]
Its integrand is absolutely integrable at zero and infinity under the
bounds just stated. In polar coordinates,
\(q_x=\cos\theta q_r-\sin\theta q_\theta/r\). Consequently
\[
 \frac D a=-\frac4\pi\int_0^{\pi/2}\cos^2\theta\sin^2\theta
     \int_0^\infty q_r\,dr\,d\theta
   +\frac4\pi\int_0^\infty\int_0^{\pi/2}
     \cos\theta\sin^3\theta q_\theta\,d\theta\frac{dr}{r}.
\]
The radial integral is \(-1\). The angular factor in its coefficient
integrates to \(\pi/16\). Since
\[
 k(\theta):=-(\cos\theta\sin^3\theta)'
      =\sin^2\theta(4\sin^2\theta-3),
\]
and the boundary values of \(\cos\theta\sin^3\theta\) vanish,
\[
 \frac D a=\frac14+\frac4\pi\int_0^\infty\int_0^{\pi/2}
                   k(\theta)q(r,\theta)\,d\theta\frac{dr}{r}. \tag{4}
\]
Here \(\int k=0\). Near zero the integrand in (4) can and must be
written \(k(q-1)\), giving absolute convergence of the iterated expression.
No assertion of absolute convergence of \(|kq|/r\) at zero is needed.

The sign change of \(k\) occurs at \(\pi/3\), and
\[
 \int_{\pi/3}^{\pi/2}k\,d\theta
   =-\int_0^{\pi/3}k\,d\theta=\frac{3\sqrt3}{16}=:m.
\]
For any continuous nonconstant \(h\) on the closed quadrant,
\(|\int kh|<m(\max h-\min h)\). Indeed, equality in the non-strict
bound would require \(h\) to equal one extreme on the open positive
interval and the other on the open negative interval. Continuity at
\(\pi/3\) then forces the extremes to coincide. If \({\cal A}>0\),
nonconstant angular sections occur on a set of positive radial measure.
Integrating this strict inequality and using the triangle inequality in
(4) proves (1). When \({\cal A}=0\), continuity implies every section
is constant, and (4) gives \(D/a=1/4\).

If \({\cal A}>0\) and \(z\le1\), (1) gives
\(0<D/a<1/2\), proving the slope claim. The zero case follows separately.
For \(0<z<1\), solving \((1-z)/4<D/a<(1+z)/4\) gives (2).
The same inequality also gives the necessary conditions
\[
 a<0\Longrightarrow {\cal A}>\frac\pi{3\sqrt3}
                   \left(1+\frac{4D}{|a|}\right),
\quad
 0<a\le2D\Longrightarrow {\cal A}>\frac\pi{3\sqrt3}
                   \left(\frac{4D}{a}-1\right).
\]

To check sharpness, choose a nonzero nonnegative smooth radial bump
\(b\) supported in a compact annulus. Let \(h_j(\theta)\) be smooth
functions of \(\sin^2\theta\), between zero and one, equal to zero and
one on subintervals on opposite sides of \(\pi/3\), and converging
pointwise off this angle to \(1_{(\pi/3,\pi/2]}\). Extend them by the
required reflections. The function
\[
 q_j=(1+r^2)^{(p-1)/2}+\alpha b(r)h_j(\theta),\qquad\alpha>0,
\]
is smooth, positive and has the prescribed origin and decay.
Its contrast is \(\alpha\int b\,dr/r\). Its deviation in (4), divided
by this contrast, tends to \(4m/\pi\) by bounded convergence.
For sufficiently large \(j\) its strain has \(D/a>0\), and the
relation can be enforced with any chosen \(D>0\) by choosing \(a\).
This proves the stated sharpness. Under the spatial dilation of the
profile, \(q_\lambda(X)=q(X/\lambda)\), substitution in the radial
integral proves invariance of \({\cal A}\).

## Independent Gaussian proof of (3)

Take \(g=y e^{-r^2}\) and set \(s=r^2\). The smooth canonical stream is
\[
 \psi=-xyH(s),\qquad
 H(s)=\frac{1-(1+s)e^{-s}}{2s^2},\qquad H(0)=\frac14.
\]
Differentiation gives \(-\Delta\psi=g_x\); its decaying velocity fixes
the canonical gauge. Since \(2sH'=e^{-s}-4H\),
\[
 Tg=y\left[H(s)+\frac{x^2}{s}(e^{-s}-4H(s))\right].
\]
At \((2,1)\) this equals
\[
 -\frac{11}{250}+\frac{133}{125}e^{-5}<0.
\]
For example, \(e^5>1+5+25/2+125/6>266/11\) proves the strict sign
without floating point. Therefore \(gTg<0\) on a small open disk about
\((2,1)\). Its value has even parity in both coordinates, so choose a
nonnegative even-even smooth sum \(w_0\) of four reflected bumps
supported in these negative disks, not identically zero.
Then \(I_0=\int w_0gTg<0\). All functions have sufficient decay for
\(I_1=\int e^{-r^2}gTg\) to be finite. Choose \(\epsilon>0\) small
so that \(|\epsilon I_1|<-I_0/2\) and set
\(w=w_0+\epsilon e^{-r^2}>0\). This proves (3).

## Scope and verification

This gives a conditional exclusion when a GLOBAL UPPER bound for
\({\cal A}\) is known. A sampled angular oscillation and a finite radial
window give lower estimates, not that upper bound. They cannot alone
exclude a profile or a nearby profile in an unspecified topology. The
Gaussian shows failure of a general weighted positivity implication; it
does not refute an additional identity special to actual profile weights.
Dependencies are the canonical strain formula and, for application to the
primary class, `../local_ipm_continuation/PROOF.md`. Neither transport
existence nor a full-class nonexistence theorem follows here.

Independent implementation checks completed 2026-10-20T19:45:09.497250+00:00. See `verification/independent_checks.json`; all checks passed. These checks support the algebra and manufactured examples; the proof above supplies the quantified statements.

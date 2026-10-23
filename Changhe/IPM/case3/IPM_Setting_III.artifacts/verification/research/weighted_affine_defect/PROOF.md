# Weighted energy of the affine defect

Status: analytic argument independently checked, 2026-10-20. Symbol and
manufactured checks are recorded in `verification/` when completed.
This audits the lead's VAN25 claim and supplies its general exponent form.

## Statement

Let \((\rho,U,\psi,\ell)\) be a nondegenerate exact primary profile on
\(\mathbb R^2\), with the canonical inverse and \(\ell>1\). Write
\[
 a=\rho_y(0)\ne0,\quad c=\psi_{xy}(0)=1-\ell,\quad
 h=\rho-ay,\quad \varphi=\psi-cxy,\quad
 v=\nabla^\perp\varphi=U-(-cx,cy).
\]
For \(2<m<4\), set
\[
 \|f\|_m^2=\int_{\mathbb R^2}|f(X)|^2r^{-2m}\,dX,
 \quad \sigma=\sup_X|\operatorname{sym}DU(X)|_{\rm op},
\]
and
\[
 N_m=\max\left\{\frac{m^2+4}{m^2-4},
                     \frac{m^2+16}{16-m^2}\right\}.
\]
Then \(0<\|h\|_m<\infty\), \(\|v\|_m\le N_m\|h\|_m\), and
\[
 (m-1)\ell-1\le m\sigma+N_m|a|.                    \tag{1}
\]
In particular \(N_3=25/7\), so
\[
 2\ell-1\le3\sigma+\frac{25}{7}|a|,
 \qquad
 G_\rho+G_U\ge\frac7{25}(2\ell-1),                 \tag{2}
\]
where \(G_\rho=\sup|\nabla\rho|\) and
\(G_U=\sup|DU|_{\rm F}\) uses the Frobenius matrix norm.
Under the additional, unproved-for-the-full-class strain cap
\(\sigma\le\ell-1\),
\[
 |a|\ge\frac7{25}(2-\ell).                         \tag{3}
\]
For \(1<\ell<2\), this excludes slopes smaller in absolute value than
the right side only within that strain-cap subclass.

More generally, suppose a smooth non-profile has the same parity,
sublinear bounds, canonical inverse and exact center relation, and put
\(F=(\ell X+U)\cdot\nabla\rho-\rho\). Then
\[
 (m-1)\ell-1\le m\sigma+N_m|a|+\frac{\|F\|_m}{\|h\|_m}.        \tag{4}
\]
No proximity theorem is implied by a small or large residual ratio here.

## Integrability and the exact energy identity

The established exact-profile symbol estimates give all derivatives
needed below. Parity and the origin coefficients give \(h=O(r^3)\),
\(\varphi=O(r^4)\), and \(v=O(r^3)\) near zero. At infinity they
have bounds \(h,v=O(r)\), \(\varphi=O(r^2)\), with corresponding
symbol derivatives. These prove finiteness of all displayed weighted
norms for \(2<m<4\). If \(h\) vanished identically, then
\(\rho=ay\) would contradict sublinear growth and \(a\ne0\).

Let \(W=\ell X+U\). Since \(\ell+c=1\), substitution of
\(\rho=ay+h\), \(U=(-cx,cy)+v\) gives
\[
 W\cdot\nabla h-h=-a v_2+F.                        \tag{5}
\]
Multiply by \(h r^{-2m}\) and integrate on circular annuli.
The boundary flux is \(O(r^{8-2m})\) at zero and \(O(r^{4-2m})\)
at infinity, so both vanish. Since \(\operatorname{div}U=0\),
\[
 \operatorname{div}(Wr^{-2m})
 =2(1-m)\ell r^{-2m}-2m(X\cdot U)r^{-2m-2}.
\]
Thus (5) gives the exact identity
\[
 ((m-1)\ell-1)\|h\|_m^2
   +m\int\frac{X\cdot U}{r^2}h^2r^{-2m}
 =-a\int v_2h r^{-2m}+\int Fh r^{-2m}.             \tag{6}
\]
All terms are absolutely integrable. For a non-profile satisfying the
same stated bounds, \(F=O(r^3)\) at zero by the center relation and
\(F=O(r^p)\) at infinity for a sublinear symbol exponent, so its
weighted norm is finite as well.

## A weighted full-plane elliptic estimate

Set \(s=\log r\),
\[
 H(s,\theta)=r^{1-m}h(r,\theta),\qquad
 G(s,\theta)=r^{-m}\varphi(r,\theta).
\]
These functions and the derivatives used below belong to \(L^2(ds\,d\theta)\)
by the origin and infinity estimates. In particular,
\[
 \|h\|_m=\|H\|_2,\qquad
 \|v\|_m^2=\|(\partial_s+m)G\|_2^2+\|\partial_\theta G\|_2^2.
\]
Because \(-\Delta\varphi=h_x\), a direct polar computation gives
\[
 -[(\partial_s+m)^2+\partial_\theta^2]G
  =(\partial_s+m)(\cos\theta H)+\partial_\theta(-\sin\theta H). \tag{7}
\]
The vector \(A=(\cos\theta H,-\sin\theta H)\) has \(\|A\|_2=\|H\|_2\).
Its components are \(\pi\)-periodic, as is \(G\), so only even angular
Fourier integers \(n\) occur. Fourier transformation in \(s\) gives
for each pair \((\xi,n)\) a map from \(\widehat A\) to the two
components \(((i\xi+m)\widehat G,in\widehat G)\). Its Euclidean
operator norm is at most
\[
 M_{m,n}(\xi)=
 \frac{\xi^2+m^2+n^2}
 {\sqrt{(\xi^2+(n-m)^2)(\xi^2+(n+m)^2)}}.           \tag{8}
\]
There is no zero denominator for even \(n\) and \(2<m<4\).
Indeed the square of (8) is
\[
 1+\frac{4m^2n^2}
 {\xi^4+2(m^2+n^2)\xi^2+(m^2-n^2)^2},
\]
which is nonincreasing in \(\xi^2\), strictly so for \(n\ne0\).
Its maximum is therefore at \(\xi=0\). For \(|n|<m\),
\((m^2+n^2)/(m^2-n^2)\) increases with \(|n|\); for \(|n|>m\),
\((m^2+n^2)/(n^2-m^2)\) decreases with \(|n|\).
Among even integers the maximum is attained at \(|n|=2\) or \(4\),
while \(n=0\) has value one. Plancherel applied to (7) now proves
\(\|v\|_m\le N_m\|h\|_m\).
This argument respects the fixed subtractions of the affine density and
harmonic strain. It does not select a different gauge for the original
full-plane inverse.

## The inequalities and an optional optimization

Since \(U(0)=0\),
\[
 X\cdot U(X)=\int_0^1X\cdot DU(tX)X\,dt
             \ge-\sigma r^2.
\]
Apply this bound and Cauchy--Schwarz to (6), use the elliptic estimate,
and divide by \(\|h\|_m^2>0\). This proves (4), and (1) follows when
\(F=0\). In two dimensions the trace-free symmetric matrix
\(S=\operatorname{sym}DU\) has \(|S|_{\rm op}=|S|_{\rm F}/\sqrt2\).
Thus \(\sigma\le G_U/\sqrt2\), and \(|a|\le G_\rho\).
At \(m=3\), \(3/\sqrt2<25/7\), proving (2). Substituting the extra
strain cap into (2)'s first inequality gives (3).

The general bound can be slightly stronger than the fixed choice \(m=3\).
For all \(2<m<4\), \(N_m\ge3>m/\sqrt2\), so
\[
 G_\rho+G_U\ge\sup_{2<m<4}\frac{(m-1)\ell-1}{N_m}.             \tag{9}
\]
The two branches of \(N_m\) meet at \(m=\sqrt8\). The quotient is
strictly increasing for \(2<m\le\sqrt8\). On \([\sqrt8,4)\) its
derivative has the sign of
\[
 \ell(256-m^4)-64\ell m^2+64(\ell+1)m.
\]
Consequently the optimizer is \(m=\sqrt8\) if
\(\ell\ge\ell_*:=64\sqrt8/(320-64\sqrt8)\).
For \(1<\ell<\ell_*\) it is the unique root in \((\sqrt8,4)\) of
\[
 m^4+64m^2-64(1+1/\ell)m-256=0.                    \tag{10}
\]
Uniqueness follows because the derivative of the polynomial in (10) is
\(4m^3+128m-64(1+1/\ell)>0\) on this interval. The endpoint signs
follow from the definition of \(\ell_*\) and evaluation at \(m=4\).
No claim that (9) is the sharp PDE bound is made: the elliptic estimate
uses a larger vector input space than the inputs arising from \(H\).

## Dependencies and scope

The center relation, canonical elliptic equation and global symbol bounds
are established earlier in this lane, including
`../local_ipm_continuation/PROOF.md`. This proof uses no numerical profile,
finite box, monotonicity condition or assumed strain cap until (3).
It gives a necessary gradient size and a conditional exclusion, not a
full-class NO. The weighted norms of \(h,v,F\) scale by the common
factor \(\lambda^{2-m}\) under positive spatial dilation; inequalities
(1)--(4) and the residual ratio therefore respect the unresolved scaling
freedom.

Independent implementation checks completed 2026-10-20T19:45:09.497250+00:00. See `verification/checks.json`; all checks passed. These checks support the algebra and manufactured examples; the proof above supplies the quantified statements.

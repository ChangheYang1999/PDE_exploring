The SPEC needs corrections before being used as an analytic specification. **V1–V3 are equivalent under the stated \(C^2\) and growth assumptions; Lemma 1 is repairable; Lemma 3 can be strengthened; D6 is valid after supplying a missing growth estimate. Lemma 5 does not establish its claimed two-dimensional regularity conclusion.** There are also explicit errors in the amplitude scaling and the far-field tail formula.

**1. Canonical velocity and the strain formula.**

Assume \(\rho\in C^2(\mathbb R^2)\) satisfies (A1),(A3). The parity cancellation in V2 is correct:
\[
\int_{|Y|<R}K(-Y)\rho(Y)\,dY=0.
\]
For \(K_1\), the integrand is odd in \(Y_1\); for \(K_2\), it is odd in \(Y_2\). Thus the exterior integral can be written using
\[
K(X-Y)-K(-Y),
\qquad
|K(X-Y)-K(-Y)|\lesssim |X||Y|^{-3}
\quad (|Y|>2|X|).
\]
Its absolute tail is bounded by
\[
C|X|\int_{2|X|}^{\infty}s^{\gamma-2}\,ds,
\]
which converges for \(\gamma<1\). The local principal value exists by subtracting \(\rho(X)\).

In fact, for \(0\leq\gamma<1\),
\[
|U(X)|\lesssim (1+|X|)^\gamma.
\]
No logarithm is needed here. To see this, put \(R=|X|\geq2\). In \(B(X,R/2)\), subtract \(\rho(X)\) and use
\[
|\nabla\rho|\lesssim R^{\gamma-1},
\]
giving a contribution \(O(R^\gamma)\). On the remainder of \(\{|Y|<2R\}\), the kernel is \(O(R^{-2})\), while the density has \(L^1\) mass \(O(R^{\gamma+2})\). The exterior estimate above gives the same bound. The local term in \(U_2\) is also \(O(R^\gamma)\).

For \(\gamma<0\), the weaker bound \(U=O(1)\) suffices and follows by using exponent zero. One should **not** claim \(O(r^\gamma\log r)\) for arbitrarily negative \(\gamma\): \(\rho=x^2y e^{-r^2}\) satisfies (A3) for every \(\gamma\), but
\[
U_1(R,0)=\frac1{4R^3}+O(R^{-4}),
\]
because \(\int y\rho\,dY=\pi/4\). In every case relevant here, \(U=o(r)\).

Local elliptic regularity gives \(U\in C^{1,\alpha}_{\rm loc}\) for every \(0<\alpha<1\). Its odd/odd streamfunction can be chosen with \(\psi=o(r^2)\). Each angular coefficient solves
\[
-\psi_n''-\frac1r\psi_n'+\frac{(2n)^2}{r^2}\psi_n=f_n.
\]
Variation of constants gives exactly V1, including its factor \(1/(4n)\). Regularity at zero excludes \(r^{-2n}\); subquadratic growth excludes \(r^{2n}\). This proves equivalence with V2. Convergence of the individual tail integrals alone would not prove convergence of the differentiated modal series; the elliptic construction supplies that missing justification.

The V3 uniqueness argument is correct, with one distributional step made explicit. A difference \(D\) satisfies \(\Delta D_i=0\), hence is smooth. Then \(D_1-iD_2\) is entire, and the Cauchy estimate gives
\[
|(D_1-iD_2)'(z)|
 \leq R^{-1}\sup_{|w-z|=R}|D(w)|\longrightarrow0.
\]
Thus \(D\) is constant, and the component parities kill both constants.

The strain formula, however, needs an origin correction under only (A1),(A3). The modal differentiation identity gives
\[
f_1=\frac12\left(\rho_0'-\frac{\rho_0}{r}
                         +\rho_1'+\frac{3\rho_1}{r}\right).
\]
Consequently,
\[
\begin{aligned}
c
&=\frac12\int_0^\infty\frac{f_1(r)}r\,dr\\
&=\frac14\left[\frac{\rho_0+\rho_1}{r}\right]_0^\infty
  +\int_0^\infty\frac{\rho_1(r)}{r^2}\,dr\\
&=\boxed{\int_0^\infty\frac{\rho_1(r)}{r^2}\,dr
          -\frac14\rho_y(0)}.
\end{aligned}
\]
The upper boundary vanishes because \(\gamma<1\). The lower boundary does **not** vanish for that reason.

A concrete counterexample is
\[
\rho(x,y)=y e^{-r^2}.
\]
It satisfies (A1),(A3), has \(\rho_1=0\), but
\[
f_1=-r^2e^{-r^2},\qquad c=-\frac14.
\]
Its displayed two-dimensional strain integral is not absolutely integrable at zero; concentric angular integration gives zero, which still misses the correction.

Under (A2), \(\rho_y(0)=0\) and \(\rho=O(r^3)\). Then the SPEC’s formula is correct:
\[
\boxed{
c=\int_0^\infty \rho_1(r)r^{-2}\,dr
 =\frac1\pi\int_{\mathbb R^2}
       \rho(X)\sin(3\theta)r^{-3}\,dX .
}
\]
Both sign and constant are right, and the integral is absolutely convergent.

**2. Lemma 1: correct conclusion, defective proof as written.**

Here is a complete repair for the actual class \(A_m\), \(m\geq2\).

Local \(C^1\) regularity and \(|W(X)|\lesssim1+|X|\) give complete characteristics in both time directions. Along them,
\[
\rho(X(s))=e^s\rho(X(0)).
\]

First eliminate the exceptional regimes:

- If \(\gamma\leq0\), \(\rho\) is bounded globally, so the transport formula forces \(\rho=0\), contradicting (A2).
- If \(c_l<0\), \(W\) points inward outside a sufficiently large ball. Every forward orbit is bounded, again forcing \(\rho=0\).
- If \(c_l=0\), qualitative sublinearity gives, for every \(\varepsilon>0\),
  \[
  |U(X)|\leq\varepsilon|X|+C_\varepsilon,
  \qquad |X(s)|\leq C_\varepsilon e^{\varepsilon s}.
  \]
  At a nonzero-density point, (A3) would imply
  \(e^s\lesssim e^{\gamma\varepsilon s}\), impossible when
  \(\gamma\varepsilon<1\).
- If \(c_l>0\), the same argument gives
  \[
  |X(s)|\leq C_\varepsilon e^{(c_l+\varepsilon)s}.
  \]
  Hence \(1\leq\gamma(c_l+\varepsilon)\) for every \(\varepsilon>0\).

Therefore
\[
\boxed{0<\gamma<1,\qquad c_l\geq1/\gamma>1.}
\]
In particular, all \(0<c_l\leq1\) are excluded.

The assertion that qualitative \(U=o(r)\) directly implies
\(|X(s)|\lesssim e^{c_ls}\) is false. A smooth divergence-free example with the required velocity parities is
\[
\psi=-\frac{xy}{\log(e+x^2+y^2)}.
\]
On the positive x-axis,
\[
x'=c_lx+\frac{x}{\log(e+x^2)}.
\]
For \(c_l>0\), \(e^{-c_ls}x(s)\) is unbounded. For \(c_l=0\),
\[
\log x(s)=(1+o(1))\sqrt{s},
\]
which is superpolynomial. This example refutes the qualitative ODE inference; it is not a stationary \(A\)-profile.

For an actual profile, the quantitative velocity bound repairs the stronger statement. With \(q=1+|X(s)|\),
\[
q'\leq c_lq+Cq^\gamma.
\]
Applying this to \(q^{1-\gamma}\) gives \(q(s)\lesssim e^{c_ls}\). On every escaping orbit, eventually
\[
r'\geq \frac{c_l}{2}r.
\]
Thus
\[
\int^\infty\frac{|U(X(s))|}{r(s)}\,ds<\infty.
\]
It follows that \(\log r(s)-c_ls\) has a finite limit. Moreover,
\[
\frac d{ds}\big(e^{-c_ls}X(s)\big)=e^{-c_ls}U(X(s))
\]
is integrable, so
\[
e^{-c_ls}X(s)\longrightarrow V\neq0.
\]
Writing \(k=1/c_l\), this proves
\[
\frac{\rho(X(s))}{|X(s)|^k}
 \longrightarrow \rho(X(0))|V|^{-k}.
\]

The limit is nonzero only when the initial density is nonzero. **Escaping zero-density characteristics remain zero**—the x-axis already makes this qualification necessary. Bounded forward characteristics carry zero density.

A useful additional conclusion is the uniform spatial bound
\[
\boxed{|\rho(X)|\lesssim(1+|X|)^k.}
\]
Choose a large circle \(r=R_0\) outside which the radial component is positive. Every exterior point, followed backward, reaches that circle. Along its forward orbit from the circle,
\[
\left|\log\frac{r(t)}{R_0}-c_lt\right|
 \leq C\int_0^t r(s)^{\gamma-1}\,ds
 \leq C',
\]
uniformly in the starting point and time. Hence \(e^t\lesssim r(t)^k\), and the bounded density on the circle proves the claim.

**3. Lemma 3 is correct and stronger than stated.**

Set
\[
w(x)=W_1(x,0),\qquad h(x)=\partial_yW_2(x,0),
\qquad g(x)=\rho_y(x,0).
\]
On the x-axis, \(\rho=\rho_x=W_2=0\). Differentiating transport in \(y\) therefore gives exactly
\[
\boxed{wg'=(1-h)g.}
\]
Incompressibility gives exactly
\[
\boxed{w'+h=2c_l.}
\]

Near zero, \(g=x^2a(x,0)\sim x^2>0\) and
\(w=(1-2c_l)x+o(x)<0\). At infinity, \(w(x)\sim c_lx>0\). Thus the first positive zero \(x_*\) exists, and the scalar ODE propagates \(g>0\) on \((0,x_*)\).

Put \(A=2c_l-1>1\). The equation becomes
\[
\frac{g'}g=\frac{w'-A}{w}.
\]

A degenerate first zero is impossible. Indeed, differentiability and the first-zero property give \(\mu=w'(x_*)\geq0\). If \(\mu=0\), then near \(x_*\), for any sufficiently small fixed \(\varepsilon>0\),
\[
|w(x)|\leq\varepsilon(x_*-x),\qquad w'(x)-A\leq-A/2.
\]
Since \(w<0\),
\[
\frac{g'}g\geq\frac{A}{2\varepsilon(x_*-x)}.
\]
Integration forces \(g\to\infty\), contradicting continuity.

Hence \(\mu>0\). With \(t=x_*-x\),
\[
g(x)=t^{\alpha+o(1)},\qquad
\alpha=\frac{\mu-A}{\mu}
       =\frac{1-h(x_*)}{\mu}<1.
\]
This follows by integrating \(g'/g\), whose leading term is
\(\alpha/(x-x_*)\).

If \(g(x_*)=0\), \(C^2\) regularity of \(\rho\) makes \(g\in C^1\), so \(g(x)=O(t)\). But the power estimate gives
\(g(x)\geq C_\delta t^{\alpha+\delta}\) for any small \(\delta>0\); choosing \(\alpha+\delta<1\) contradicts \(g=O(t)\). Thus \(g(x_*)>0\). Evaluating the ODE at the endpoint now gives
\[
\boxed{
h(x_*)=1,\qquad w'(x_*)=2c_l-1,\qquad g(x_*)>0.
}
\]

Thus **nondegeneracy need not be assumed** under the actual hypotheses.

The stated weaker \(C^1\)-density conclusion is also right, provided \(W\in C^1\): continuity of \(g\) excludes \(h(x_*)>1\). If \(h(x_*)<1\), then \(0<\alpha<1\), contradicting bounded \(g'\).

The regularity qualifications are:

- \(U\in C^1\) near the relevant axis segment is sufficient for this argument with \(\rho\in C^2\).
- The literal asymptotic \(g\sim Ct^\alpha\), rather than \(t^{\alpha+o(1)}\), needs additional control such as a Hölder or suitable Dini modulus of \(DW\).
- Actual \(C^2\) density supplies \(U\in C^{1,\alpha}_{\rm loc}\), so that improvement is available.
- \(C^1\) density alone does not automatically supply a \(C^1\) velocity.

For Lemma 4, the sign conclusion is valid. Indeed, \(g(P)>0\) already implies \(\rho>0\) in \(Q\) sufficiently near \(P\), and transport preserves the sign on every orbit emanating from \(P\).

A precise fixed-\(W\) rigidity statement can also be proved without assuming a full smooth linearization. Write \(W_2=y\,b(X)\), with \(b(P)=1\). Backward orbits approach this source exponentially, and \(W\in C^{1,\alpha}\) makes
\[
I(X)=\int_{-\infty}^0[b(\Phi_tX)-1]\,dt
\]
convergent. Define
\[
\eta_P(X)=y e^{-I(X)}.
\]
The flow identity gives \(\eta_P(\Phi_sX)=e^s\eta_P(X)\). Since
\(\rho(X)/y\to C=\rho_y(P)\) at \(P\), transport gives exactly
\[
\rho=C\eta_P.
\]
This is rigidity for a **fixed vector field**. It does not prove uniqueness of the coupled profile, where \(W\) changes with \(\rho\). The resonance calculation alone is not a proof of smooth linearization.

**4. Lemma 5: the exponents are right; the regularity inference is incomplete.**

Let
\[
A=2c_l-1>1,\qquad b=4c_l-1=2A+1.
\]
With enough regularity to form the transverse jets, coefficient comparison gives
\[
wG_j'+(jh-1)G_j=F_j.
\]
The forcing includes lower jets **and their x derivatives**, as well as velocity derivatives. For example, writing
\(W_1=w+A_2y^2+\cdots\), \(W_2=hy+B_3^Wy^3+\cdots\),
\[
F_3=-A_2G_1'-B_3^WG_1.
\]
A straightforward classical justification uses
\(\rho\in C^{j+1}\), \(W\in C^j\); one cannot form all these equations in a fixed finite \(A_m\).

For smooth coefficients, the homogeneous solution is a smooth nonzero even multiplier times
\[
|x|^{p_j},\qquad
\boxed{p_j=\frac{jb-1}{A}=2j+\frac{j-1}{2c_l-1}.}
\]
Thus
\[
p_1=2,\qquad p_3=6+\frac2{2c_l-1}\in(6,8).
\]
It is never an even integer, and equals \(7\) when \(c_l=3/2\).

If one has actually proved a uniform two-dimensional expansion containing
\[
B_3y^3|x|^{p_3}
\]
with a sufficiently regular remainder that cannot cancel it, the conclusions are:

| Parameter range | Regularity of this term |
|---|---|
| \(c_l\geq3/2\), so \(6<p_3\leq7\) | \(C^6\), not \(C^7\) |
| \(1<c_l<3/2\), so \(7<p_3<8\) | \(C^7\), not \(C^8\) |

These are statements about regularity on a neighborhood: fix a small \(y\neq0\) and examine the x dependence. They do not follow merely from a high-order jet at the single point \((0,0)\).

The SPEC has not justified the passage from an axis coefficient to that uniform two-dimensional expansion. Here is a concrete counterexample to that inference. For any \(p\in(6,8)\), set near zero
\[
\rho=x^2y+B x^2y^3(x^2+y^2)^{(p-2)/2},\qquad B\neq0.
\]
It has the required parity and factorization, with
\[
a=1+B y^2r^{p-2},\qquad a(0)=1,
\]
and
\[
\frac{\rho_{yyy}(x,0)}6=B|x|^p.
\]
Nevertheless, the perturbation is smooth away from zero and homogeneous of total degree \(p+3>9\), so it is \(C^9\). For \(p>7\), it is \(C^{10}\). A smooth radial cutoff gives a global example satisfying (A1)–(A3).

**This example is not a stationary IPM solution.** It disproves the regularity inference from the displayed axis information, not a possible theorem using additional consequences of the full PDE. Such a theorem would need a saddle-passage argument controlling the expansion up to the unstable axis.

The immediate trace consequence is only
\[
\rho\in C^m\ \Longrightarrow\ G_3\in C^{m-3}.
\]
Thus a genuinely noncancellable \(|x|^{p_3}\) term in \(G_3\) directly rules out:

- \(C^{10}\) when \(6<p_3\leq7\);
- \(C^{11}\) when \(7<p_3<8\).

It does not directly rule out \(C^8\).

The “infinitely many conditions” statement is defensible as a **necessary formal/ODE compatibility statement**, with qualifications. For smooth coefficients and lower jets, every non-even \(p_j\) requires its homogeneous coefficient \(B_j\) to vanish if \(G_j\) is smooth. There are infinitely many such \(j\): writing \(j=2\ell+1\),
\[
p_j=4\ell+2+\frac{2\ell}{A},
\]
which is even exactly when \(\ell/A\) is an integer.

But:

- Even-integer exponents can introduce additional forcing conditions to exclude logarithms. For example,
  \(xG'-pG=x^p\) produces \(x^p\log|x|\).
- Necessity does not establish independence or sufficiency.
- The \(B_j\) belong to one coupled nonlinear problem and could obey structural identities forcing their vanishing.
- No such structural theorem, nor a nonvanishing or transversality theorem, is supplied.

Accordingly, “smooth profiles are isolated in \(c_l\)” and “a generic candidate is only \(A_6\)” remain heuristics.

**5. D6: sign and range are correct after the missing estimate is supplied.**

On an annulus, homogeneity gives
\[
\begin{aligned}
\operatorname{div}(\rho\phi W)
&=\phi W\cdot\nabla\rho+\rho W\cdot\nabla\phi
  +\rho\phi\operatorname{div}W\\
&=[1+(2-d)c_l]\rho\phi+\rho U\cdot\nabla\phi.
\end{aligned}
\]

At zero, \(\rho=O(r^3)\), \(U=O(r)\). Both volume integrands have radial absolute majorant \(Cr^{4-d}\,dr\); the inner boundary term is \(O(\varepsilon^{5-d})\). Thus \(d<5\) is sufficient.

At infinity, use the uniform bound proved above, \(\rho=O(r^k)\), \(k=1/c_l\). The dilation term requires \(d>k+2\). The velocity volume term is bounded by
\[
C\int^\infty r^{k+\gamma-d}\,dr,
\]
and its boundary term is \(O(R^{k+\gamma+1-d})\). Both are controlled by \(d>k+2\), since \(\gamma<1\).

Letting the annulus exhaust the plane proves exactly
\[
\boxed{
[1+(2-d)c_l]\int\rho\phi\,dX
+\int\rho U\cdot\nabla\phi\,dX=0,
\qquad k+2<d<5.
}
\]
Consequently the \(d=3,m=1\) specialization is also correct:
\[
\pi(1-c_l)c+
\int\rho U\cdot\nabla(\sin(3\theta)r^{-3})\,dX=0.
\]
Using (A3) alone would initially require \(d>\gamma+2\); the sharper density estimate is what validates the stated range.

**6. Further errors and assumptions.**

- **Amplitude scaling is reversed.** For
  \[
  (c_lX+U)\cdot\nabla\rho=c_\rho\rho,
  \]
  replacing \(\rho\) by \(\lambda\rho\) replaces \(U\) by \(\lambda U\) and requires
  \[
  (c_l,c_\rho)\mapsto(\lambda c_l,\lambda c_\rho),
  \]
  not division by \(\lambda\). The spatial scaling and its normalization effect are correct.

- **N3(a) has an extra factor of \(R\).** With its definition of \(F_n\),
  \[
  f_n(s)=R^{-k}s^{k-1}F_n,
  \]
  hence
  \[
  \boxed{
  \int_R^\infty s^{1-2n}f_n(s)\,ds
  =\frac{F_nR^{1-2n}}{2n-k-1}.
  }
  \]
  The stated \(R^{2-2n}\) would be correct if \(F_n\) meant \(f_n(R)\), which it does not. For \(R=4,k=1/2,n=1,F_n=1\), the true integral is \(1/2\); the SPEC gives \(2\).

- **Lemma 2 is conditional as written.** Positive constant divergence excludes periodic orbits and separatrix cycles enclosing a region: boundary flux is zero while the divergence integral is \(2c_l\) times its positive area. Backward orbits are bounded. With finitely many equilibria, the planar limit-set argument gives convergence to an equilibrium. Finiteness has not been proved from \(A\). The index sum \(+1\) is valid when the equilibria are isolated; without isolation, the individual-index sum is not defined as stated. The origin and the two first x-axis sources already contribute \(-1+1+1=1\), but further equilibria of net index zero remain possible.

- **The full angular far-field expansion is additional information.** Characteristic asymptotics and \(\rho=O(r^k)\) do not by themselves establish convergence at fixed polar angle to a smooth \(\Theta\), its correction series, or boundedness of \(U/r^k\). The available estimates do give the sufficient bound \(U=O(r^k\log r)\). D8’s bounded-ratio test is stronger than merely checking \(U=o(r)\).

- **A global \(x^2y\) ansatz can restrict the class.** A2 imposes \(\rho(0,y)=0\) only near zero. If the positive y-axis has no stagnation point, transport extends that vanishing along the whole axis. If stagnation points intervene, that argument no longer connects all axis intervals. Global factorization, including N3(b), therefore needs justification or must be declared an additional restriction. A second-order angular zero of \(\Theta\) also needs suitable angular regularity of the limiting process.

- **Section 7’s growth-to-velocity implication is false in general.** The exact stationary solution \(\rho=y,\ c_l=1,\ U=0\) has linear density and zero velocity/source modes. More generally \(\rho=y^q,\ c_l=1/q,\ U=0\) works for positive odd integers \(q\). These do not satisfy A2, but they invalidate the proposed inference from density growth alone. Nor must the first modal tail diverge: an outer \(\sin(5\theta)\) density mode produces only \(\sin(4\theta)\) and \(\sin(6\theta)\) source modes.

- **The physical gauge justification is conditional.** A bounded physical outer strain contributes a vanishing rescaled strain proportional to \(T-t\). Neither that boundedness nor the matching limit is established by the profile hypotheses.

- **Minor formulation issues:** \(A_1\) is undefined in the SPEC; the classes start at \(m=2\). Pointwise normalized residuals need a convention where their denominators vanish. N6’s normalization formula is algebraically correct.

I saved the complete proof notes and reproducible symbolic checks in the [audit index](INDEX.md). All symbolic checks passed, and the SPEC was left unchanged.

Opus 5.5 collaboration could not be performed: the existing Bedrock configuration returned no EC2 credentials, so no Opus invocation or model confirmation was possible.
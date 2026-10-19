The dynamical and positivity arguments survive. The main problems are the \(C^4\) justification of the finite part, the claim that smoothness forces a linear transversal function, and the proposed sharp regularity conclusion for finite-regularity coupled profiles. The numerical diagnostic also has a serious instability near \(p_3=7\).

I read both files completely and copied and ran the script. Counterexamples below involving prescribed transport fields or axis jets are explicitly distinguished from actual whole-plane IPM profiles.

Write
\[
A=2c_l-1>1,\qquad \lambda_1=-A,\qquad \lambda_2=2A+1,
\qquad q=2+\frac1A,\qquad p=p_3=6+\frac2A.
\]
Also write \(g=\rho_y(x,0)\), \(a_2=W_{1,yy}(x,0)/2\), and \(b_3=W_{2,yyy}(x,0)/6\).

**1. Sections 2.2 and 2.3: CORRECT, with the stated finiteness condition retained.**

For the rescaling argument, derivative convergence of \(\rho_\varepsilon\) is unnecessary. Put
\[
\rho_\varepsilon(X)=\varepsilon^{-3}\rho(\varepsilon X),
\qquad V_\varepsilon(X)=\varepsilon^{-1}W(\varepsilon X).
\]
The continuous factor in (A2) gives \(\rho_\varepsilon\to x^2y\) locally uniformly. Since \(W\in C^1\), \(V_\varepsilon\to DW(0)X\) locally uniformly, and \(\operatorname{div}V_\varepsilon=2c_l\). The weak equation is
\[
-\int \rho_\varepsilon V_\varepsilon\cdot\nabla\varphi
=(1+2c_l)\int\rho_\varepsilon\varphi.
\]
Passing to the limit gives
\[
DW(0)X\cdot\nabla(x^2y)=x^2y,
\]
hence \(2(c_l-c)+(c_l+c)=1\).

Thus the local calculation uses continuous (A2), a \(C^1\) field with the prescribed parity and divergence, and the transport equation. The previously proved forced regime supplies \(c_l>1\), making the origin a hyperbolic saddle. Axis invariance and uniqueness of the local invariant manifolds identify its stable and unstable manifolds.

For 2.3:

- \(U=o(r)\) and \(c_l>0\) give an outward-pointing sufficiently large circle, hence bounded backward orbits.
- Constant positive divergence excludes periodic orbits and separatrix circuits enclosing a region.
- With finitely many equilibria in the trapping region, the planar limit-set theorem then gives convergence to one equilibrium. **Finiteness must remain a hypothesis.**
- The index sum follows from homotopy on a large circle to \(c_lX\). Because all zeros lie in a compact set, isolatedness of every zero actually implies finiteness.

No nondegeneracy assumption on every equilibrium is needed.

**2. Section 2.5: CORRECT WITH REPAIR. The entire conclusion holds already in \(A_2\).**

The first two basin arguments are sound.

If \(\Phi_tX\to0\) as \(t\to-\infty\), its sufficiently negative-time tail lies in the local unstable manifold. Flow invariance therefore puts the entire orbit on the global unstable manifold, which is contained in the invariant y-axis. An interior point of \(Q\) cannot have this alpha-limit.

Under Hmin, symmetry gives precisely the global equilibria \(0,P,-P\). Consequently every \(X\in Q\) belongs to the backward basin of \(P\).

The fixed-\(W\) rigidity applies there. In particular, the limiting ratio is justified by
\[
\frac{\rho(x,y)}y=\int_0^1\rho_y(x,ty)\,dt\longrightarrow \rho_y(P).
\]
Together with exponential backward convergence and Hölder continuity of \(b-1\), this proves
\[
\rho=\rho_y(P)\eta_P>0.
\]
It is a statement about the already fixed field, not uniqueness of the coupled profile.

For the y-axis, put \(v(y)=W_2(0,y)\). Hmin implies \(v>0\) on \((0,\infty)\): it is positive near zero and has no positive zero. The equation
\[
v(y)\frac{d}{dy}\rho(0,y)=\rho(0,y)
\]
and its vanishing on a small interval imply \(\rho(0,y)=0\) everywhere on the positive axis.

The curvature conclusion needs a better finite-regularity argument than the brief reference to rescaling. It does **not** need \(C^3\). Let
\[
k(y)=\frac12\rho_{xx}(0,y).
\]
Along an axis orbit \(y_t\), the transverse flow derivative is
\[
J(t)=\exp\!\left(\int_0^t W_{1,x}(0,y_s)\,ds\right).
\]
Evenness and axis vanishing give
\[
\rho(x,y)=x^2k(y)+o(x^2)
\]
locally uniformly in \(y\). Apply \(\rho(\Phi_tX)=e^t\rho(X)\), divide by the square of the initial transverse coordinate, and let it tend to zero:
\[
k(y_t)J(t)^2=e^t k(y_0).
\]
Thus the sign of \(k\) is preserved with only \(C^2\) density. Near zero,
\[
k(y)=y\,a(0,y)\sim y>0.
\]
Hence \(k>0\) on the entire positive axis. Since \(v\neq0\), the same formula also establishes the differentiability needed for the displayed scalar ODE.

**3. Section 3.2 and the diagnostic: the bounded branch is CORRECT; the finite-part claim is CONDITIONAL; the algorithm needs repair.**

The endpoint at \(P\) is handled correctly. With \(\beta=2/A>0\),
\[
H(x)\sim C(x^*-x)^{-\beta}.
\]
The integrand \(-F_3/(wH)\) is integrable at \(P\). Variation of constants and boundedness give
\[
G_3(x)=H(x)\int_x^{x^*}\frac{-F_3(t)}{w(t)H(t)}\,dt,
\qquad
G_3(P)=\frac{F_3(P)}2.
\]
Two solutions differ by a multiple of the unbounded function \(H\), proving uniqueness.

The origin requires stronger hypotheses.

For **smooth symmetric axis data**, \(a_2,g'\) are odd and \(b_3,g\) are even. Therefore
\[
F_3=-a_2g'-b_3g
\]
is even and vanishes to order at least two. Writing \(w=x\omega(x)\) and \(H=x^pe^{E(x)}\) for \(x>0\),
\[
\frac{-F_3}{wH}=x^{1-p}K(x),
\qquad
K(x)=\frac{-F_3(x)}{x^2\omega(x)e^{E(x)}},
\]
where \(K\) is smooth even.

Since \(6<p<8\), precisely three Taylor terms require subtraction:
\[
K(x)=k_0+k_2x^2+k_4x^4+O(x^6).
\]
The coefficient is
\[
B_3=\lim_{\varepsilon\downarrow0}
\left[
\int_\varepsilon^{x^*}x^{1-p}K(x)\,dx
+\sum_{n=0}^2
\frac{k_{2n}\varepsilon^{2+2n-p}}{2+2n-p}
\right].
\]
Multiplication by \(H\) shows that this is exactly the coefficient of \(x^p\), relative to the smooth even particular solution, when \(H/x^p\to1\).

A logarithm would require \(1-p+2n=-1\), equivalently an **even integer** \(p\). At \(p=7\), the powers are
\[
x^{-6},\ x^{-4},\ x^{-2},\ 1,\ldots,
\]
so there is no logarithm.

However, **\(C^4\) does not supply this Taylor expansion**. For example, \(b_3\) is then only a \(C^1\) trace. Neither a smooth even series nor the needed integrable remainder follows.

The local scalar example
\[
-AxG'+ApG=|x|^p
\]
has
\[
G=-\frac1A|x|^p\log|x|+B|x|^p.
\]
Its forcing can be realized as \(-b_3g\) with \(g=x^2\) and \(b_3=-|x|^{p-2}\), which is \(C^4\). This is an axis-ODE example, **not a coupled IPM profile**. It establishes that parity and the advertised regularity alone do not justify the argument. A coupled bootstrap excluding such forcing remains to be proved.

A clean repair is to assume smooth axis data. For the finite part at this order, a weaker explicit endpoint expansion such as the displayed \(K=k_0+k_2x^2+k_4x^4+O(x^6)\), with adequate regularity of \(E\), suffices.

The manufactured calculation itself is correct. Set
\[
P(z)=2\alpha_0(1+z)^2+\beta_0(1+z)^3
=\sum_{m=0}^3P_mz^m.
\]
Then
\[
\frac{-F_3}{wH}
=-\frac1A x^{1-p}(1-x^2)^{\beta-1}P(x^2),
\]
and substitution \(z=x^2\) gives
\[
B_3=-\frac1{2A}\sum_{m=0}^3
P_m\,\mathrm B\!\left(m+1-\frac p2,\beta\right),
\]
using the meromorphic continuation of Beta. At \(c_l=3/2\), the value is exactly \(2/3\). The manufactured \(g\) also satisfies its stated axis ODE.

The requested default-`python3` run completed successfully:

| \(c_l\) | Exact \(B_3\) | Finite-part result | Relative error |
|---|---:|---:|---:|
| 1.3 | 0.8163631204695 | 0.8163630971260 | \(2.86\cdot10^{-8}\) |
| 1.5 | 0.6666666666667 | 0.6666666641315 | \(3.80\cdot10^{-9}\) |
| 2.2 | 0.6010774834808 | 0.6010774819336 | \(2.57\cdot10^{-9}\) |

The smooth-target test returned \(-3.479\cdot10^{-9}\). ODE-fit errors were approximately \(10^{-6},10^{-6},3\cdot10^{-7}\).

**There is nevertheless a serious numerical defect near \(p=7\).** Tiny spurious odd FFT coefficients are retained. The coefficient with index \(5\) is divided by \(7-p\). In additional local tests:

| \(c_l\) | Exact value | Original algorithm | Odd FFT coefficients set to zero |
|---|---:|---:|---:|
| 1.49999999 | 0.666666670486 | 0.095114750205 | 0.666666670543 |
| 1.50000001 | 0.666666662847 | 0.688804643493 | 0.666666662880 |

Thus the diagnostic can be grossly wrong arbitrarily close to the supposedly harmless integer case.

The FFT convention and Gauss–Jacobi weight and scaling are correct. The repair is to enforce the **known exact even parity**, while reporting measured parity errors separately. Further error control remains necessary:

- A fitted polynomial evaluated on a complex circle is not a validated analytic continuation of arbitrary finite-regularity data.
- Small FFT tails do not bound interpolation or endpoint-subtraction errors.
- The scaled ODE-fit matrices have condition numbers around \(10^9\); tiny fit residuals do not certify \(B_3\).

Finally, the manufactured data are a scalar-ODE test, not compatible IPM jets. Constant divergence requires
\[
a_2'+3b_3=0,
\]
whereas the supplied constants give \(0.7+3(-0.4)=-0.5\).

**4. Section 3.3: the representation is CORRECT WITH REPAIR; “\(F\) is linear” is WRONG; the global and finite-regularity consequences are CONDITIONAL.**

On \(\xi>0\), characteristics of the linear field give
\[
\rho(\xi,\eta)=\xi^{-1/A}\widehat F(\eta\xi^q).
\]
Evenness identifies the functions on the two sides and permits \(|\xi|\); oddness makes \(\widehat F\) odd. Values on \(\xi=0\) require the axis-vanishing or regularity condition as well.

Every local solution has its own transversal function. The additional assertion \(\widehat F=CF\) uses the source-basin rigidity. It is not true for arbitrary unrelated local solutions.

Assume now that both the symmetric linearizing chart and \(F\) are \(C^\infty\). Then the correct criterion is
\[
\rho\in C^\infty
\quad\Longleftrightarrow\quad
F_j=0
\quad\text{for every odd }j\text{ with }p_j\notin2\mathbb N.
\]

For sufficiency, fix a desired derivative order and take a sufficiently long Taylor expansion of \(F\). Allowed terms become ordinary polynomial powers of \(\xi\). The remainder, after multiplication by \(|\xi|^{-1/A}\), extends with that many derivatives because its transverse exponent can be made arbitrarily large. Necessity follows by restricting to a fixed small \(\eta\neq0\) and taking the first forbidden Taylor term.

But this does **not** imply that \(F\) is linear. For instance,
\[
F(s)=s+s e^{-1/s^2},\qquad F(0)=0
\]
produces
\[
\rho=\xi^2\eta
\left[1+\exp\!\left(-\frac1{\eta^2|\xi|^{2q}}\right)\right],
\]
with the exponential contribution defined as zero on either axis. It is smooth and flat there, satisfies the linear transport equation exactly, and has a nonconstant quotient \(\rho/(\xi^2\eta)\).

Allowed resonances give another counterexample. At \(A=2\),
\[
F(s)=s+s^5
\quad\Longrightarrow\quad
\rho=\xi^2\eta+\xi^{12}\eta^5,
\]
which is smooth.

These are counterexamples to the **formal transport inference**, not asserted IPM profiles. The corrected nonresonant \(C^\infty\) statement is “linear modulo a flat function.” To conclude literal linearity requires analyticity of \(F\), as well as absence of allowed higher resonances.

The supplied files do not prove existence of a smooth symmetric linearization for every already smooth coupled profile. Nonresonance gives a sufficient condition; resonant values of \(c_l\) have not been excluded. The separately cited proof needs verification before that claim is used unconditionally.

For propagation along the y-axis, smooth coordinates and \(F_3\neq0\) give a nonzero transverse term
\[
F_3\eta^3|\xi|^p
\]
at every sufficiently small positive axis point. Smooth finite-time transport preserves this singularity along the connected nonstationary axis orbit. To reach **every** \(y>0\), one needs no intervening axis equilibrium—Hmin is sufficient—and adequate flow regularity along each intervening segment. The unconditional “every radius” claim is therefore too strong.

For finite regularity, the proposed formula already fails literally at \(p=7\):
\[
|x|^7\in C^{6,1},\qquad |x|^7\notin C^7.
\]

A useful conditional theorem can be proved. Suppose the chart and its inverse are \(C^m\), \(F\in C^m\), \(m=\lceil p\rceil\), and \(F_3\neq0\). Write
\[
F(s)=F_1s+F_3s^3+R(s),\qquad R(s)=O(s^5).
\]
Then
\[
\rho=F_1\xi^2\eta+F_3\eta^3|\xi|^p+\widetilde R,
\qquad
\widetilde R=|\xi|^{-1/A}R(\eta|\xi|^q)\in C^m.
\]
Indeed, differentiation gives powers at least \(p_5-u\), where \(u\) is the number of \(\xi\)-derivatives and
\[
p_5=10+\frac4A>10.
\]
Taylor bounds for derivatives of \(R\) through order five, and boundedness of higher derivatives, establish continuous extension through total order \(m\le8\).

Consequently:

- If \(p\notin\mathbb Z\), the exact regularity is \(C^{\lfloor p\rfloor,p-\lfloor p\rfloor}\), but not \(C^{\lceil p\rceil}\).
- If \(p=7\), it is \(C^{6,1}\), but not \(C^7\).

To state this theorem using the **physical \(B_3\)**, its identification with the transversal \(F_3\) must also be justified. A low-regularity coordinate change does not automatically preserve that identification.

There is no lower-regularity conclusion from the axis coefficient and local transport alone. With the perfectly smooth linear field, take
\[
F(s)=s+Bs^3+\operatorname{sgn}(s)|s|^{9/2},\qquad B\neq0.
\]
The resulting density has the required local parity and continuous \(x^2y\) factorization, and
\[
G_3=B|x|^p.
\]
Nevertheless it is only \(C^{4,1/2}\), not \(C^5\), across \(y=0\) at \(x\neq0\). Again, this is a local transport counterexample, not a source-matched coupled profile.

For the actual coupled problem there is another important limitation: if \(W\) is smooth near the origin, then
\[
\rho_x=-\operatorname{curl}W
\]
is smooth. Since \(\rho(0,y)=0\),
\[
\rho(x,y)=-\int_0^x\operatorname{curl}W(t,y)\,dt
\]
is smooth too. Thus a genuinely rough coupled profile cannot simultaneously have the smooth field assumed in the illustrative linearized calculation.

**The sharp regularity theorem for actual \(C^4\) IPM profiles remains unproved here.** It needs a finite-regularity or anisotropic saddle-passage argument.

**5. Section 3.4, structural cancellation, and section 5: heuristic status is appropriate, but several repairs are needed.**

The counting discussion honestly acknowledges that existence, independence, and nonvanishing have not been proved. It should remain a heuristic. The fixed-point equation is still infinite dimensional; no Fredholm index or local solution manifold justifies counting only two scalar unknowns.

Also, \(C^1\) regularity alone does not force \(\mu_2=1\): a source with \(\mu_2=1/3\) admits the smooth odd eigenfunction \(y^3\). Here the decisive additional fact is \(g(P)>0\).

I found no identity forcing \(B_3=0\) for every \(C^4\) profile. There is, however, a useful exact identity at \(c_l=3/2\).

The coupled axis relations are
\[
a_2'+3b_3=0,\qquad h'-2a_2=-g',
\qquad
a_2=\frac{g'-w''}{2}.
\]
At \(A=2\), the \(g\) equation and normalization give
\[
H=-\frac{2g^4}{w}.
\]
Therefore
\[
\frac{-F_3}{wH}
=\frac16\left(\frac{a_2}{g^3}\right)'.
\]
For smooth parity-consistent axis data, \(a_2/g^3=x^{-5}\) times a smooth even function, whose expansion has no constant term. Hence
\[
\boxed{\displaystyle
B_3=\frac{a_2(P)}{6g(P)^3}
=\frac{w''(P)\,[g(P)-2]}{24g(P)^3}
\qquad(c_l=3/2).}
\]
This is not an automatic zero.

For a concrete check, take \(x^*=1\) and
\[
w=-\frac{2x(1-x^2)}{1+x^2},\qquad
g=\frac{x^2}{1+x^2},\qquad h=3-w',
\]
\[
a_2=\frac{x(5x^2-11)}{(1+x^2)^3},
\qquad b_3=-\frac13a_2'.
\]
These satisfy the \(G_1\) equation and both displayed divergence/curl axis constraints. They give
\[
F_3=\frac{x^2(55-15x^2)}{3(1+x^2)^4},
\qquad
\frac{-F_3}{wH}=\frac{55}{6x^6}-\frac5{2x^4}.
\]
Thus
\[
B_3=-1,
\]
and the bounded solution is
\[
G_3(x)=
\frac{\frac{11}{6}x^2-\frac56x^4-x^7}
{(1-x^2)(1+x^2)^3},
\qquad G_3(P)=\frac5{12}.
\]
All these identities were checked symbolically.

This is **compatible axis data, not a whole-plane IPM solution**. It rules out cancellation from the listed axis identities alone, while leaving open an additional genuinely global constraint.

It also exposes a hidden assumption in the proposed invariant \(\xi_P\xi\). At \(A=2\), the source eigenvalues are \((2,1)\), and \(a_2(P)y^2\) in \(W_1\) is resonant. A smooth coordinate \(\xi_P\) with nonzero x-derivative satisfying \(W\xi_P=2\xi_P\) cannot exist when \(a_2(P)\neq0\): the quadratic homological operator annihilates \(y^2\), so it cannot remove that term. Such a source coordinate must not be assumed without checking resonance.

Section 5 needs these logical repairs:

- Nonvanishing of a forbidden coefficient for every sufficiently regular candidate is **one possible** NO strategy, not something every NO proof must establish.
- \(B_3\) is not classically defined by this hierarchy for arbitrary \(A_2\) profiles.
- Small numerical \(B_3,B_5\) do not prove smooth existence; numerical evidence is not logically necessary for an analytic existence proof either.
- Its \(P_\infty\) definition—smooth factor near zero, merely classical elsewhere—is weaker than SPEC’s globally smooth \(A_\infty\), unless another propagation theorem is supplied.
- The expansion and regularity claimed for \(a\) remain conditional on the missing two-dimensional expansion.

**6. Sections 4.2, 4.4, and other corrections.**

**4.2: CORRECT on \(\{\rho\neq0\}\).**
\[
\operatorname{div}(WF(\rho))
=2c_lF(\rho)+\rho F'(\rho)
\]
is the chain rule. Taking \(F(s)=|s|^{-2c_l}\) gives the asserted invariant density.

It does not give a finite invariant measure across the axes. Under 2.5,
\[
\rho(x,y)\sim k(y)x^2,
\qquad |\rho|^{-2c_l}\sim |x|^{-4c_l},
\]
which is not locally integrable there.

**4.4: CORRECT WITH REPAIR.**

Literal strict positivity throughout the upper half-plane conflicts with \(\rho(0,y)=0\) near zero; use positivity in \(Q\).

The inequality \(c>2\) comes from \(c=3c_l-1\) and \(c_l>1\), **not from positivity alone**. The precise sector statement is
\[
\int_{\theta<\pi/3}\rho|\sin3\theta|r^{-3}
-\int_{\theta>\pi/3}\rho|\sin3\theta|r^{-3}
=\frac{\pi c}{4}>\frac\pi2,
\]
with both integrals over their respective portions of \(Q\). This does not compare the sector masses with the sine factor omitted.

Positivity alone cannot even force \(c>0\): add a large nonnegative symmetric bump, supported away from zero in the negative-sine sector, to the coefficient in \(x^2y e^{-r^2}\). This preserves normalization, smoothness, positivity in \(Q\), and rapid decay, but makes \(c<0\). It is not a stationary profile; it identifies the invalid positivity-only inference.

Two previously audited passages also need repair:

- In 1.1,
  \[
  \sup_{B_{2s}}|\nabla\rho|\lesssim s^{\gamma-1}
  \]
  is false because the ball contains the origin. Use \(|X-Y|<s/2\) for the gradient estimate, and bound the remaining inner region directly using \(|K|\lesssim s^{-2}\). The asserted velocity estimate survives.
- The uniform density estimate establishes the optimal **density** exponent \(k=1/c_l\), not the gradient part of (A3) with \(\gamma=k\). The phrase “\(\gamma\) close to \(k\)” in 4.1 is unnecessary: the original \(\gamma<1\) gives
  \[
  k+\gamma+1-d<k+2-d<0.
  \]
  SPEC’s standalone \(U=O(r^\gamma)\) assertion also needs \(\gamma\ge0\); its negative-\(\gamma\) exception is already recognized in analysis 1.1.

The report and verification evidence are saved in [PROOF.md](PROOF.md) and [INDEX.md](INDEX.md). All machine restrictions were observed.

The configured Opus target was `us.anthropic.claude-opus-5-5`, but the permitted Python Bedrock invocation failed because AWS credentials were unavailable. No Opus response or actual-model confirmation was obtained, and no other model was substituted.
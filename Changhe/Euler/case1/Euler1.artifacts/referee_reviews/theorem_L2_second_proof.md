**Answer to uncount1.** The countability hypothesis can be removed. I obtain a full obstruction for the class in the question, without analyticity, a stratification of the stagnation set, or an assumption that backward orbits converge.

The additional argument has two parts. A backward limit set meeting \(E\) must be a single point: otherwise it contains a regular equilibrium arc on which a transverse quadratic estimate forces convergence. Once convergence is established, finitely many local trapping neighborhoods of \(E\), followed by countably many flow maps, suffice for the measure argument. One must not take an uncountable union of individual null basins.

Here is a self-contained proof. The new local convergence argument and the local null-set argument are given explicitly. This is an informal mathematical proof, not a formal verification or an independently completed Opus audit; the review limitation is recorded at the end.

**Theorem.** Let \(0<c<1/2\). Suppose \(U,P\in C^2(\mathbb R^3)\) satisfy
\[
 (1-c)U+(cy+U)\cdot\nabla U+\nabla P=0,
 \qquad \operatorname{div}U=0,
 \qquad U(y)=o(|y|).
\]
Put
\[
 V=cy+U,\quad A=DV=cI+DU,\quad
 S=\tfrac12(DU+DU^\top),\quad \Omega=\operatorname{curl}U,
\]
\[
 N=\{V=0\},\qquad
 E=\{p\in N:\lambda_{\max}(S(p))\ge1\}.
\]
Let \(\Phi_s\) be the flow of \(V\), and let \(\alpha(a)\) be the backward limit set of \(a\). Then
\[
 W:=\{a:\alpha(a)\cap E\ne\varnothing\}
 \quad\text{has three-dimensional Lebesgue measure zero}.
\]
Consequently \(\Omega\equiv0\) and \(U\) is constant. If \(U\to0\) at infinity, then \(U\equiv0\); if also \(P\to0\), then \(P\equiv0\).

In particular, the stated decay assumptions imply the desired conclusion. The proof does not use the two-fold rotation symmetry or the separate decay bound on \(DU\). It uses the profile equations essentially; it is not a theorem about arbitrary smooth vector fields merely having compact equilibrium sets.

**The identities and compactness needed below.** Write
\[
 \kappa=1-2c>0,\qquad C_\Omega v=\Omega\times v,
 \qquad
 H=\frac{|V|^2}{2}+P+\frac{c(c-1)}2|y|^2.
\]
Substitution of \(U=V-cy\) into the profile equation, followed by
\[
 (V\cdot\nabla)V=\nabla(|V|^2/2)+\Omega\times V,
\]
gives
\[
 \nabla H=-(\kappa I+C_\Omega)V,
 \qquad V\cdot\nabla H=-\kappa |V|^2.                 \tag{1}
\]
Since \(V\perp\Omega\times V\),
\[
 |\nabla H|^2=\kappa^2|V|^2+|\Omega\times V|^2.
\]
Thus, everywhere,
\[
 \kappa |V|\le|\nabla H|
 \le\sqrt{\kappa^2+|\Omega|^2}\,|V|.                 \tag{2}
\]
In particular, the matrix
\[
 B(p):=\kappa I+C_{\Omega(p)}
\]
is invertible, and \(\operatorname{Crit}H=N\). At an equilibrium \(p\), differentiating (1) gives
\[
 D^2H(p)=-B(p)A(p).
\]
Consequently,
\[
 \operatorname{rank}D^2H(p)=\operatorname{rank}A(p),
 \qquad \ker D^2H(p)=\ker A(p).                    \tag{3}
\]
The vanishing of \(V(p)\) is what eliminates the derivative of \(B\) in this calculation.

Sublinearity gives a global bound \(|V(y)|\le C(1+|y|)\), so the \(C^2\) vector field has a complete flow in both time directions. Choose \(R>0\) so that \(|U(y)|\le c|y|/2\) when \(|y|\ge R\). For the backward trajectory
\[
 x(t)=\Phi_{-t}(a),\qquad t\ge0,
\]
one has, outside that ball,
\[
 \frac{d}{dt}|x(t)|^2=-2x(t)\cdot V(x(t))
 \le-c|x(t)|^2.
\]
Every backward trajectory therefore enters the closed ball of radius \(R\) and remains there. Also \(N\) is contained in this ball and is compact.

Along this trajectory,
\[
 \frac{d}{dt}H(x(t))=\kappa|V(x(t))|^2.             \tag{4}
\]
The bounded tail of the trajectory implies that \(H(x(t))\) increases to a finite limit \(h\). Its limit set \(K=\alpha(a)\) is nonempty, compact and connected: it is the intersection of the nested compact closures of the connected trajectory tails. It is invariant, and \(H=h\) on \(K\). Invariance and (4) then imply
\[
 K\subset N.                                      \tag{5}
\]
This also proves constancy of \(H\) on the particular limit set without invoking Sard's theorem or making any assertion about paths in \(N\).

Taking the curl of the profile equation gives
\[
 \Omega+(V\cdot\nabla)\Omega=(DU)\Omega=S\Omega.     \tag{6}
\]
For the last equality, the skew part of \(DU\) is \(C_\Omega/2\), which annihilates \(\Omega\). The trace identity is
\[
 \operatorname{tr}A=3c.                            \tag{7}
\]

**Every point of \(E\) has rank at least two and a contracting direction.** At an equilibrium with \(\Omega(p)\ne0\), equation (6) gives
\[
 A(p)\Omega(p)=(1+c)\Omega(p).
\]
One eigenvalue of \(A(p)\) is positive, and the other two have sum \(2c-1<0\). At least one of those two has negative real part. Thus \(\operatorname{rank}A(p)\ge2\).

At an equilibrium with \(\Omega(p)=0\), \(A(p)=cI+S(p)\) is symmetric. If \(p\in E\), its largest eigenvalue is at least \(c+1>0\). Since \(\operatorname{tr}S=0\),
\[
 \lambda_{\min}(S(p))
 \le-\tfrac12\lambda_{\max}(S(p))\le-\tfrac12,
\]
so its smallest eigenvalue is at most \(c-\tfrac12<0\). Again the rank is at least two. We have proved
\[
 p\in E
 \ \Longrightarrow\
 \begin{cases}
 \operatorname{rank}A(p)\ge2,\\
 A(p)\text{ has an eigenvalue with negative real part}.
 \end{cases}                                      \tag{8}
\]

**Local convergence lemma.** Under the hypotheses above, if \(\alpha(a)\) contains an equilibrium \(p\) with \(\operatorname{rank}A(p)\ge2\), then \(\alpha(a)\) is a singleton.

Here it is important to prove the assertion for an arbitrary connected limit set, without assuming local connectedness or a prescribed manifold structure.

If \(\operatorname{rank}A(p)=3\), the inverse function theorem makes \(p\) an isolated zero of \(V\). A connected subset of \(N\) containing that isolated point can only be \(\{p\}\).

Suppose the rank is two and, for contradiction, \(K=\alpha(a)\) is not a singleton. Choose two components of \(V\) whose differentials are independent at \(p\). Their common zero set is a \(C^2\) embedded curve near \(p\), by the implicit function theorem. Thus there is a coordinate neighborhood
\[
 \Psi:(-\delta,\delta)\times D\longrightarrow\mathcal O,
 \qquad \Psi(0,0)=p,
\]
where \(D\) is a disk in \(\mathbb R^2\), such that
\[
 N\cap\mathcal O
 \subset \{\Psi(\xi,0):|\xi|<\delta\}.              \tag{9}
\]
Shrink \(\mathcal O\) so that the chosen rank-two minor stays nonzero and so that some fixed point \(r\in K\setminus\{p\}\) lies outside \(\mathcal O\).

I claim that \(K\) contains a nontrivial one-sided interval of the coordinate axis starting at \(p\). Otherwise there are arbitrarily small numbers \(\xi_-<0<\xi_+\) with
\[
 \Psi(\xi_-,0)\notin K,\qquad
 \Psi(\xi_+,0)\notin K.
\]
Choose a smaller transverse disk \(D_\rho\), with
\[
 \overline{\mathcal D}\subset\mathcal O,\qquad
 \mathcal D=\Psi((\xi_-,\xi_+)\times D_\rho).
\]
The lateral boundary of \(\mathcal D\) has no points of \(K\), by (5) and (9). Each end cap can meet \(K\) only at its axis point, and those two points were chosen outside \(K\). Therefore
\[
 K\cap\partial\mathcal D=\varnothing.
\]
But \(K\cap\mathcal D\) is then a nonempty, proper subset that is both open and closed in \(K\): it contains \(p\) and excludes \(r\). This contradicts connectedness. The claim follows.

Choose \(q\) strictly inside the resulting equilibrium interval, away from its endpoints. In a smaller neighborhood of \(q\), the equilibrium set is exactly a \(C^2\) curve \(\Gamma\), an open subarc of that interval. Every point of this curve has rank exactly two: the selected minor gives rank at least two, and differentiation of \(V|_\Gamma=0\) supplies a nonzero tangent vector in its kernel. Formula (3) now gives
\[
 \ker D^2H(q')=T_{q'}\Gamma,\qquad
 \operatorname{rank}D^2H(q')=2
 \quad(q'\in\Gamma).                              \tag{10}
\]
Also \(H=h\) on \(\Gamma\), since this arc lies in \(K\).

The resulting local gradient inequality can be proved by Taylor expansion; no analytic Łojasiewicz theorem is needed. In coordinates \((\xi,z)\) straightening \(\Gamma\), put \(F=H\circ\Psi\). Then
\[
 F(\xi,0)=h,\qquad dF(\xi,0)=0.
\]
By (10), the \(2\times2\) transverse Hessian
\[
 Q(\xi)=D^2_{zz}F(\xi,0)
\]
is invertible. Indeed, since \(dH=0\) on the curve, the coordinate Hessian there is \(D\Psi^\top D^2H D\Psi\), whose kernel is exactly the \(\xi\)-axis. Its restriction to the transverse coordinate plane is therefore nonsingular. On a smaller coordinate box its transverse Hessian has smallest singular value bounded below. Taylor expansion, uniformly on that box, gives constants \(C_1,m>0\) such that
\[
 |F(\xi,z)-h|\le C_1|z|^2,\qquad
 |D_zF(\xi,z)|\ge m|z|.
\]
For the second estimate, use
\[
 D_zF(\xi,z)=Q(\xi)z+o(|z|)
\]
with the error uniform in \(\xi\). Equivalence of coordinate and Euclidean gradient norms therefore gives
\[
 |H(y)-h|^{1/2}\le C_0|\nabla H(y)|                \tag{11}
\]
near \(q\). Positive definiteness is not being assumed: an invertible indefinite transverse Hessian gives the same estimates.

It remains to show that an orbit accumulating at \(q\) is trapped there; a gradient inequality without this step would be insufficient. Set
\[
 e(t)=h-H(x(t))\ge0.
\]
Then \(e(t)\to0\), and (4) gives
\[
 e'(t)=-\kappa|x'(t)|^2.
\]
On a fixed small neighborhood of \(q\), (2) gives \(|\nabla H|\le M|x'|\). Combining this with (11), whenever \(e(t)>0\) and the trajectory remains in that neighborhood, gives
\[
 -\frac{d}{dt}\sqrt{e(t)}
 =\frac{\kappa|x'(t)|^2}{2\sqrt{e(t)}}
 \ge\frac{\kappa}{2C_0M}|x'(t)|.
\]
Thus every such trajectory segment satisfies
\[
 \int_{t_0}^{t_1}|x'(t)|\,dt
 \le\frac{2C_0M}{\kappa}
       \bigl(\sqrt{e(t_0)}-\sqrt{e(t_1)}\bigr)
 \le\frac{2C_0M}{\kappa}\sqrt{e(t_0)}.              \tag{12}
\]
If \(e\) reaches zero, monotonicity and its limiting value imply \(H(x(t))=h\) thereafter, so (4) makes the trajectory stationary. This case causes no difficulty.

Choose \(r_0>0\) so that (11) and the bound defining \(M\) hold on the closed ball \(\overline B_{r_0}(q)\). Since \(q\in\alpha(a)\) and \(e(t)\to0\), choose a sufficiently late time \(t_0\) with
\[
 |x(t_0)-q|<r_0/4,\qquad
 \frac{2C_0M}{\kappa}\sqrt{e(t_0)}<r_0/4.
\]
A first exit from \(B_{r_0/2}(q)\) would require length greater than \(r_0/4\), contradicting (12). The trajectory stays in that ball, and (12) gives finite length for its entire remaining tail. It therefore converges. Its subsequential limit \(q\) is its limit, so \(K=\{q\}\), contradicting the assumption that \(K\) was not a singleton.

This proves the local convergence lemma. In view of (8), it yields precisely the convergence needed here:
\[
 a\in W\quad\Longrightarrow\quad
 \Phi_{-t}(a)\longrightarrow q
 \text{ for some }q\in E.                         \tag{13}
\]
Nothing in this argument assumes in advance that every backward orbit converges.

**A local null-set lemma, including its trapping property.** Let \(X\) be a \(C^1\) vector field near an equilibrium \(p\). If \(DX(p)\) has an eigenvalue with positive real part, there is a small neighborhood \(B_p\) for which
\[
 T_p:=\{b:\text{the forward }X\text{-orbit of }b
                   \text{ remains in }B_p
                   \text{ for all }t\ge0\}
\]
has three-dimensional outer measure zero.

Here is an elementary graph proof, to make explicit the property usually supplied by a center-stable manifold theorem. Translate \(p\) to zero and write
\[
 X(z)=Lz+R(z),\qquad L=DX(p).
\]
Split the real generalized eigenspaces as
\[
 \mathbb R^3=E^{cs}\oplus E^u,
\]
where \(E^u\) corresponds to eigenvalues with positive real part and \(E^{cs}\) to the others. Thus \(\dim E^{cs}\le2\). In coordinates adapted to this splitting, choose \(\beta>0\), \(\epsilon=\beta/4\), \(\eta=\beta/2\), and \(M_0\ge1\) such that
\[
 \|e^{-tL_u}\|\le M_0e^{-\beta t},\qquad
 \|e^{tL_{cs}}\|\le M_0e^{\epsilon t}
 \quad(t\ge0).                                    \tag{14}
\]
These bounds follow directly from the finite-dimensional Jordan form; choose \(\beta\) smaller than the minimum positive real part on \(E^u\). Shrinking a convex neighborhood of zero makes \(R\) Lipschitz with an arbitrarily small constant \(\ell\), because \(DR(0)=0\).

Take two forward trajectories \(z,\widetilde z\) staying in that neighborhood, and set
\[
 w=z-\widetilde z,\qquad
 r(t)=R(z(t))-R(\widetilde z(t)).
\]
Use the product norm for the spectral splitting, so that \(|r(t)|\le\ell|w(t)|\). Variation of constants gives
\[
 w_{cs}(t)=e^{tL_{cs}}w_{cs}(0)
       +\int_0^t e^{(t-s)L_{cs}}r_{cs}(s)\,ds.      \tag{15}
\]
Boundedness of \(w\) and the first estimate in (14) also give the terminal representation
\[
 w_u(t)=-\int_t^\infty e^{(t-s)L_u}r_u(s)\,ds.      \tag{16}
\]
To justify (16), first write the formula with terminal time \(T\); the term \(e^{(t-T)L_u}w_u(T)\) tends to zero.

Let
\[
 D_*=\sup_{t\ge0}e^{-\eta t}|w(t)|<\infty.
\]
Multiplying (15) and (16) by \(e^{-\eta t}\), using (14), and summing the two component bounds gives
\[
 D_*\le M_0|w_{cs}(0)|
 +M_0\ell\left(
       \frac1{\eta-\epsilon}+\frac1{\beta-\eta}
          \right)D_*.
\]
Choose the neighborhood so that the coefficient of \(D_*\) on the right is at most \(1/2\). Then
\[
 |w_u(0)|\le D_*\le2M_0|w_{cs}(0)|.               \tag{17}
\]
Thus projection of \(T_p\) to \(E^{cs}\) is injective, and its inverse is a Lipschitz graph over a subset of \(E^{cs}\). Such a graph has three-dimensional outer measure zero when \(\dim E^{cs}\le2\). For example, covering its bounded parameter set by cubes of side \(\delta\) covers the graph by \(O(\delta^{-\dim E^{cs}})\) boxes of volume \(O(\delta^3)\), whose total volume tends to zero.

This proves the lemma without requiring the construction or uniqueness of an invariant center manifold.

**Applying the local null-set lemma to all of \(E\).** Apply it to \(X=-V\) at each \(p\in E\). The required positive eigenvalue of \(DX(p)=-A(p)\) follows from (8). For each such point, choose an open neighborhood \(U_p\) whose closure lies inside the corresponding trapping neighborhood \(B_p\).

The set \(E\) is compact, since \(N\) is compact and \(\lambda_{\max}(S)\) is continuous. Choose a finite cover
\[
 E\subset U_{p_1}\cup\cdots\cup U_{p_m},
\]
and let \(T_i\) be the set of points whose entire backward \(V\)-orbit remains in \(B_{p_i}\). Each \(T_i\) is null by the lemma.

For \(a\in W\), (13) supplies a limit \(q\in E\). Choose \(i\) with \(q\in U_{p_i}\). For some integer \(n\ge0\),
\[
 \Phi_{-(n+t)}(a)\in B_{p_i}\quad\text{for every }t\ge0.
\]
Consequently \(\Phi_{-n}(a)\in T_i\), and
\[
 W\subset\bigcup_{i=1}^{m}\ \bigcup_{n=0}^{\infty}
                     \Phi_n(T_i).                \tag{18}
\]
Each \(\Phi_n\) is a \(C^1\) diffeomorphism, hence locally Lipschitz and null-set preserving. The right side of (18) is a countable union of null sets. Therefore
\[
 |W|=0.                                          \tag{19}
\]
If \(E=\varnothing\), the same conclusion is immediate. The finite neighborhoods in (18) cover all their nearby limiting equilibria at once; they are not indexed separately by every equilibrium in an uncountable set.

**Eliminating vorticity.** For completeness, the vorticity-free basin implication also follows directly from (6). Along \(x(t)=\Phi_{-t}(a)\),
\[
 \frac{d}{dt}\Omega(x(t))=(I-S(x(t)))\Omega(x(t)).
\]
If \(\Omega(a)\ne0\), uniqueness for this linear equation implies \(\Omega(x(t))\ne0\) at every finite time. Hence
\[
 \frac{d}{dt}\log|\Omega(x(t))|
 \ge 1-\lambda_{\max}(S(x(t))).                   \tag{20}
\]
Suppose \(\alpha(a)\cap E=\varnothing\). Compactness and continuity give a neighborhood of \(\alpha(a)\) on which
\[
 \lambda_{\max}(S)\le1-\delta
\]
for some \(\delta>0\). The bounded trajectory eventually stays in that neighborhood: otherwise an escaping sequence of times would produce a limit point outside it. Equation (20) would then force exponential growth of \(|\Omega(x(t))|\), contradicting boundedness of \(\Omega\) on the compact ball containing the trajectory tail. Thus
\[
 Z:=\{\Omega\ne0\}\subset W.                       \tag{21}
\]
By (19), \(Z\) is null. Since \(Z\) is open, it is empty.

Now \(\operatorname{curl}U=0\) and \(\operatorname{div}U=0\) imply
\[
 \Delta U=\nabla\operatorname{div}U
             -\operatorname{curl}\operatorname{curl}U=0.
\]
For each harmonic component \(u\), the interior gradient estimate at a fixed \(x_0\) gives
\[
 |\nabla u(x_0)|
 \le \frac{C}{R}\sup_{B_R(x_0)}|u|.
\]
Sublinearity makes the right side tend to zero as \(R\to\infty\). Thus \(U\) is constant. The stated limits at infinity then imply \(U=P=0\), as asserted.

**What happens to the proposed exceptional geometries.** There is a useful description of the potential nonconvergent limit sets before the final vorticity argument. The local convergence lemma says that any nonsingleton \(\alpha(a)\) must lie entirely in
\[
 \{p\in N:\operatorname{rank}A(p)\le1\}.
\]
The trace \(3c>0\) makes that rank exactly one. At such a point, \(\Omega(p)\ne0\) would give the eigenvalue \(1+c\), whereas a rank-one matrix of trace \(3c\) has eigenvalues \(0,0,3c\). Since \(c<1/2\), this is impossible. Thus \(\Omega(p)=0\), \(A(p)\) is symmetric, and
\[
 \operatorname{spec}S(p)=\{-c,-c,2c\},
 \qquad\lambda_{\max}(S(p))=2c<1.                 \tag{22}
\]
In particular, a nonsingleton limit set cannot meet both \(E\) and a degenerate portion of \(N\). It cannot meet \(E\) at all. This resolves the mixed-limit-set possibility specifically raised in the question.

The suggested additional hypotheses can therefore be treated as follows.

- **(a) Real analyticity.** It is unnecessary. The only gradient inequality used is the elementary exponent-\(1/2\) inequality (11), on an equilibrium arc with a nonsingular transverse Hessian. All ingredients hold under \(C^2\) regularity.
- **(b) A finite union of embedded curves, surfaces and points.** It is covered, without needing that representation. At a regular equilibrium curve, the tangent lies in \(\ker A\). If \(\Omega\ne0\), the eigenvalues are \(0,1+c,2c-1\). If \(\Omega=0\) and \(\lambda=\lambda_{\max}(S)\ge1\), they are \(0,c+\lambda,2c-\lambda\). At a regular equilibrium surface, \(\operatorname{rank}A\le1\), so (22) applies and the surface misses \(E\). Singular meetings and accumulation points are handled by the rank argument: near any point of \(E\), the zero set is contained in one smooth curve or the point is isolated.
- **(c) Containment in a normally hyperbolic submanifold.** It is also unnecessary. The usual manifold argument would require an invariant manifold and a stable normal direction for \(V\); for a manifold of equilibria in three dimensions, that places its local backward basin in dimension at most two. Mere containment of \(N\) in an arbitrary \(C^1\) submanifold is not itself a normal-hyperbolicity hypothesis. The proof above needs neither a global invariant containing manifold nor uniform spectral estimates along strata.
- **(d) Convergence of every backward orbit.** This would suffice by (18)–(21), even with uncountably many possible limits. The local convergence lemma supplies the weaker statement actually needed: convergence of every orbit whose backward limit set meets \(E\).

The proposed import of vorticity along center-unstable sheets consequently cannot produce an exact profile in this class. On a regular bad stagnation curve, the curve parameter plus its unstable normal direction give a two-dimensional center-unstable sheet. The curve parameter is already included in that dimension. Allowing uncountably many equilibrium points on the curve does not supply a further dimension. More generally, (18) covers all bad equilibria, including irregular configurations, by countably many null sets. The open set \(Z\) cannot fit inside that union.

The two-fold rotation symmetry is compatible with this proof but has no role in it. For example, on a stagnation segment of the \(z\)-axis, symmetry makes \(\Omega\) axial, while differentiation along the segment gives \(A e_z=0\). Together with \(A\Omega=(1+c)\Omega\), this forces \(\Omega=0\) there. No separate axis argument is needed for the theorem.

**Why volume expansion and Sard alone do not prove the result.** The determinant identity
\[
 \det D\Phi_s=e^{3cs}
\]
and invariance of \(Z\) show that its measure is zero or infinite. Infinite measure is not a contradiction. The decisive additional fact is the null covering (18), not volume expansion.

For a \(C^\infty\) function \(H\), Sard's theorem does show that its critical values form a null set. It also shows that \(H\) is constant on each connected component of \(\operatorname{Crit}H\), since a connected subset of \(\mathbb R\) containing two points contains an interval. Neither fact implies that basins of critical values are null.

The exact trivial profile \(U=P=0\) already illustrates the failure:
\[
 V=cy,\qquad N=\{0\},\qquad
 H=-\frac{\kappa c}{2}|y|^2.
\]
There is only one critical value, yet every point of \(\mathbb R^3\) converges backward to the corresponding equilibrium. Its basin has full measure. That equilibrium is outside \(E\), as it must be.

The proof given here does not require Sard. This matters for the stronger \(C^2\) statement: one should not silently invoke a smooth critical-value theorem at lower regularity. Constancy on an actual limit set follows from (4), and constancy on an equilibrium arc follows directly from \(\nabla H=0\).

**Consistency with the threshold and the cited papers.** At \(c=1/2\), \(\kappa=0\). Equation (1) makes \(H\) a first integral, so the argument placing all backward limit sets in \(N\) fails. The matrix \(B=C_\Omega\) is singular, (2) loses its positive lower bound, (3) need not preserve rank, and the dissipation estimate (12) is unavailable. Also the curve eigenvalue \(2c-1\) is zero. Thus this proof gives no obstruction at the threshold.

The question identifies Ganeshram–Duruisseaux–Anandkumar, arXiv:2609.10867, as claiming numerical axisymmetric profiles with swirl at \(c=1/2\). Taken as stated, that claim is compatible with the theorem here: it concerns exactly the parameter at which the essential estimates fail. I have not independently verified that paper or its numerical claims, and do not treat numerical evidence as an existence theorem.

For \(c>1/2\), the contracting-direction assertion (8) is false in general. On a regular stagnation curve with nonzero vorticity, the two normal eigenvalues
\[
 1+c,\qquad 2c-1
\]
are both positive for \(V\). The center direction and both unstable normal directions then have total dimension three, so the corresponding local backward basin need not be null. Although \(H\) remains strictly monotone away from equilibria when \(c\ne1/2\), monotonicity alone does not restore the missing stable direction. No exclusion for \(c>1/2\) follows from this proof.

The supplied audited notes report that Constantin–Ignatova–Vicol, arXiv:2602.17570v3, Theorem 3.9 assumes finite \(N_V\), local outgoing, and its specified profile and growth/regularity assumptions. I have not independently checked that theorem's text. The proof above does not infer local outgoing from smoothness: it handles contracting directions through the null-set argument, and removes countability through the local convergence lemma. Relative to the result reported in the notes, this is a proposed strengthening with an additional proof, not a claim that Theorem 3.9 already states the full conclusion. No novelty claim is being made.

**Sources and verification status.** I read sections 2 and 3 of the supplied `THEORY_NOTES.md`, including the corrected limitations of its curve argument, and rederived the identities used above. The literature identifications below come from the question and those notes:

- Constantin, Ignatova and Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3, Theorem 3.9.
- Ganeshram, Duruisseaux and Anandkumar, arXiv:2609.10867.

Direct retrieval of both arXiv pages failed with a DNS error, `Name or service not known`. Earlier progress messages claiming successful paper retrieval were incorrect and are withdrawn. No independently fetched paper text supports this answer; the comparisons above are explicitly limited to the supplied descriptions. This limitation does not enter the self-contained mathematical proof.

The argument is self-contained apart from standard inverse/implicit function theorems, elementary ODE theory, finite-dimensional spectral estimates, and the harmonic interior gradient estimate. In particular, its two delicate steps—convergence through a rank-two equilibrium and the countable null covering—are proved above rather than left as manifold-theorem heuristics.

I attempted the requested Claude Opus 5.5 collaboration through the configured Python/Bedrock credential chain. It failed with `CredentialRetrievalError`: the configured `cline-profile` could not obtain its EC2 instance-metadata credentials. No Opus model was reached, no actual Opus model identity could be confirmed, and no other model was substituted. Independent Opus review therefore remains unavailable; it should not be inferred from this answer. No server, JavaScript tooling, GPU computation, or RLScience-cluster operation was used.

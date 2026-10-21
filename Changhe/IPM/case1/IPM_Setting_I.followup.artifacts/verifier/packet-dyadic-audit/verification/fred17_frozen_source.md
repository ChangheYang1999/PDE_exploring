# The frozen Fourier packets

## Statement, notation, and scope

All results in this file concern the frozen operator, not an exact IPM profile. Put

\[
D=A s\partial_s+y\partial_y,\quad L_g=D-1+gU_2,\quad
A>1,\quad g>0,\quad q=2(A-1),\quad b=g/q,
\quad Q=A+1,\quad h=1+g.
\]

Our inverse Fourier transform has factor \(c_F=(2\pi)^{-2}\). Let \(\Phi\in C_c^\infty(\mathbb R\setminus\{0\})\), with

\[
\Phi(-t)=-\overline{\Phi(t)},\qquad \int\Phi(t)\,dt=0.                 \tag{1}
\]

Thus the real part of \(\Phi\) is odd and its imaginary part is even. Define, off \(\eta=0\),

\[
f(\xi,\eta)=\Phi(\xi/|\eta|^A)\operatorname{sgn}(\eta)
 |\eta|^{2b-A-2}(\xi^2+\eta^2)^{-b}.                                \tag{2}
\]

**Corrected theorem.** The limit of \(1_{|\eta|>\epsilon}f\) in tempered distributions exists. Its inverse transform \(v\) is a real, continuous, odd-in-\(y\) function and solves \(L_gv=0\). Here \(U_2\) is the unique odd-in-\(y\), sublinearly growing second velocity component satisfying the canonical div-curl equations. There is no origin-supported defect in the equation. The function is smooth off the origin and

\[
|v(s,y)|\le C(1+|(s,y)|)^{1/A}.                                     \tag{3}
\]

The exponent \(1/A\) is optimal for each nonzero packet when a single isotropic power bound is sought. Nevertheless, every nonzero packet fails the profile condition \((1+|X|)|\nabla v(X)|\le C(1+|X|)^\gamma\) for every \(\gamma<1\).

For every integer \(m\ge0\) and \(0<\alpha<1\),

\[
(m+\alpha)A\le h\quad\Longrightarrow\quad v\in C^{m,\alpha}_{\rm loc}.
                                                                    \tag{4}
\]

No nonzero packet is \(C^n\) at the origin when \(nA>h\). In particular, if the exact inequalities \(3<h/A<4\) hold, the packet is \(C^{3,h/A-3}\), is \(C^{2,\alpha}\) for every \(\alpha<1\), and is not \(C^4\). The numerical parameters in the question suggest these inequalities; they do not certify them for an exact profile.

There is an asymptotic expansion consisting of a smooth part and terms of anisotropic degrees

\[
h_k=h+kq,\qquad k=0,1,\ldots.                                      \tag{5}
\]

The terms can have logarithmic scaling anomalies. Pure quasi-homogeneity holds at order \(k\) if no nonnegative integers \(a_1,a_2\) with odd \(a_2\) satisfy \(h_k=Aa_1+a_2\), or if the corresponding residue moments below vanish. No non-resonance assumption is needed for existence, off-origin smoothness, or (4).

The assertions that all these packets have bounded third trace for every \(g>0\), or that their full third trace consists only of a fractional term, are false. The precise trace theorem is in `../02_axis/PROOF.md`.

## 1. Fourier equation and the extension at zero

The Fourier identities give

\[
\widehat{L_gv}=-\left(A\xi\partial_\xi+\eta\partial_\eta+A+2+
             g\frac{\xi^2}{\xi^2+\eta^2}\right)\widehat v.           \tag{6}
\]

The characteristics are \((\xi,\eta)=(\xi_0e^{A\tau},\eta_0e^\tau)\). The invariant is \(t=\xi/|\eta|^A\). Applying the characteristic vector field to the logarithm of the positive factor in (2) gives

\[
2b-A-2-2b\left(1+(A-1)\frac{\xi^2}{\xi^2+\eta^2}\right)
=-A-2-g\frac{\xi^2}{\xi^2+\eta^2}.
\]

This proves (6) away from zero frequency.

For the extension, use \(r=|\eta|\), \(\xi=tr^A\), and \(a(r,t)=(1+t^2r^q)^{-b}\). For a Schwartz test function \(\varphi\), the proposed pairing is

\[
\int_0^\infty r^{-2}\int\Phi(t)a(r,t)
 [\varphi(tr^A,r)-\varphi(tr^A,-r)]\,dt\,dr.                         \tag{7}
\]

At small \(r\), the bracket is \(2r\varphi_\eta(0,0)+O(r^{A+1}+r^3)\), uniformly for \(t\) in the fixed compact support. Moreover, \(a=1+O(r^q)\). The leading term integrates to zero by (1). The remaining integrand is bounded by a Schwartz seminorm times

\[
r^{A-1}+r+r^{q-1},
\]

which is integrable since \(A>1\) and \(q>0\). At infinity the density after the change of variables is \(O(r^{-h-1})\). Thus (7) is a continuous functional on Schwartz space and defines the asserted limit.

For the truncated distribution, the only error in (6) comes from differentiating \(1_{r>\epsilon}\). Its pairing is, up to the irrelevant overall sign,

\[
\epsilon^{-1}\int\Phi(t)a(\epsilon,t)
 [\varphi(t\epsilon^A,\epsilon)-\varphi(t\epsilon^A,-\epsilon)]\,dt.
\]

It is \(2\varphi_\eta(0)\int\Phi+O(\epsilon^A+\epsilon^2+\epsilon^q)\), hence tends to zero. Multiplication of the truncations by \(-\xi^2/(\xi^2+\eta^2)\) also converges: it adds a factor \(-t^2r^q/(1+t^2r^q)\), so odd pairing alone makes the low-frequency integral convergent. Passing to the limit proves the equation with this multiplier prescription. This checks the possible zero-frequency anomaly, rather than merely the characteristic ODE.

Without the moment condition, the boundary term is a nonzero multiple of \(\partial_\eta\delta_0\), or of \(y\) in physical space, and the unsubtracted truncations in (7) do not converge. A finite-part prescription must then be analyzed separately, including its equation defect and growth. The characteristic ODE alone does not justify an exact globally normalized solution.

## 2. A continuous integral and the canonical velocity

Taking the inverse transform of (7) gives the grouped integral

\[
v(s,y)=2ic_F\int_0^\infty \frac{\sin(yr)}{r^2}
       \int\Phi(t)e^{istr^A}(1+t^2r^q)^{-b}\,dt\,dr.                \tag{8}
\]

For bounded \((s,y)\), the inner integral at small \(r\) is \(O(|s|r^A+r^q)\); at large \(r\) it is \(O(r^{-g})\). These bounds make (8) converge locally uniformly and prove continuity. The symmetries in (1) prove reality and oddness.

The velocity component appearing in the equation is

\[
U_2[v]=-2ic_F\int_0^\infty\sin(yr)r^{q-2}
 \int t^2\Phi(t)e^{istr^A}(1+t^2r^q)^{-b-1}\,dt\,dr.               \tag{9}
\]

It converges locally uniformly for every \(A>1\). A compatible first component, anchored by \(U_1(0,0)=0\), is

\[
2c_F\int_0^\infty r^{A-3}\int t\Phi(t)(1+t^2r^q)^{-b-1}
       [e^{istr^A}\cos(yr)-1]\,dt\,dr.                             \tag{10}
\]

At small \(r\), the bracket is \(O(|s|r^A+y^2r^2)\). Both resulting powers are integrable for \(A>1\). At infinity the weight is \(O(r^{-g-A-1})\), which is integrable. Differentiation in distributions, or first differentiating truncated integrals and then passing to the limit, verifies

\[
\partial_sU_1+\partial_yU_2=0,\qquad
\partial_sU_2-\partial_yU_1=-\partial_sv.
\]

For example, the two terms of the divergence have integrands \(\pm2ic_F t^2\Phi e^{istr^A}\cos(yr)r^{2A-3}(1+t^2r^q)^{-b-1}\), and cancel exactly.

Elementary splitting at \(r=1/|y|\) bounds (9) by a constant if \(A>3/2\), by \(C\log(2+|y|)\) if \(A=3/2\), and by \(C(1+|y|)^{3-2A}\) if \(1<A<3/2\). Splitting (10) at \(|s|^{-1/A}\) and \(|y|^{-1}\) gives a bound \(C(1+|X|)^{2-A}\) for \(1<A<2\), a logarithmic bound for \(A=2\), and a constant bound for \(A>2\). All these bounds are sublinear.

Two sublinear solutions of the div-curl equations differ by a constant vector. Indeed their components are entire harmonic functions, and the interior gradient estimate on a ball of radius \(R\), followed by \(R\to\infty\), makes their gradients zero. Oddness in \(y\) eliminates the constant in the second component. This proves that (9) is the canonical second component, without relying on an undefined multiplication of arbitrary distributions at \(\zeta=0\).

Only oddness in \(y\) was required in the packet class. Under this symmetry alone there remains a constant horizontal-velocity ambiguity. The original report's full parity convention removes it, but that convention also requires evenness of the density in the horizontal variable. For the even-in-\(s\) subspace \(\Phi=i\phi\), with \(\phi\) real and even, (10) is odd in \(s\) and has the full centered parity. For general packets one must specify the horizontal constant. When \(A>2\), including the source regime in the question, the unsubtracted version of (10) is absolutely integrable in frequency and gives a distinguished velocity tending to zero at infinity. This is the convention used for axis formulas in the next file. For \(1<A\le2\), the bare unsubtracted integral need not converge. The Fourier formula alone does not justify the report's symmetric-truncation convention for every such packet.

## 3. Growth and the stronger gradient condition

In (8), split \(r<1\) and \(r>1\). The latter is uniformly bounded. For \(r<1\), write \(a=1+(a-1)\). The term with 1 has inner integral bounded by \(C\min(|s|r^A,1)\), because \(\int\Phi=0\). Consequently

\[
\int_0^1r^{-2}\min(|s|r^A,1)\,dr\le C(1+|s|)^{1/A}.
\]

The other term is bounded by \(C\int_0^1r^{q-2}\min(|y|r,1)\,dr\). This is bounded, logarithmic, or \(O(|y|^{1-q})\), according as \(q>1\), \(q=1\), or \(q<1\). Since \(1-q=3-2A<1/A\) for \(A>1\), (3) follows.

There is also the locally uniform scaling limit

\[
R^{-1}v(R^As,Ry)\longrightarrow
V_0(s,y)=2ic_F\int_0^\infty\sin(yr)r^{-2}
                      \int\Phi(t)e^{istr^A}\,dt\,dr.               \tag{11}
\]

To prove it, replace \(r\) in (8) by \(r/R\). For \(r\le1\), the same cancellation gives a uniform integrable bound \(C(r^{A-1}+r^{q-1})\) on compact physical sets. For \(r\ge1\), use \(Cr^{-2}\). Dominated convergence gives (11). Its Fourier transform, restricted off zero, is \(\Phi(t)\operatorname{sgn}(\eta)|\eta|^{-A-2}\), so \(V_0\ne0\) if \(\Phi\ne0\). By continuity it is nonzero at some point with \(s\ne0\). Along that ray, (11) rules out every power smaller than \(1/A\) in (3).

Suppose the weighted gradient bound held for some \(\gamma<1\). On a compact set with \(|s|\) bounded away from zero,

\[
\partial_y[R^{-1}v(R^As,Ry)]=\partial_yv(R^As,Ry)
=O(R^{A(\gamma-1)})\longrightarrow0.
\]

By (11), \(\partial_yV_0=0\) there in distributions. Oddness and continuity then give \(V_0=0\) for every \(s\ne0\), and hence everywhere. This contradicts \(\Phi\ne0\). Thus these global frozen solutions are not admissible profile perturbations with the full gradient bound. A compact physical cutoff removes this far-field difficulty.

## 4. The anisotropic symbol argument, proved by dyadic kernels

On \(r\ge1\), the support satisfies \(0<c\le|\xi|/|\eta|^A\le C\), and

\[
f=\sum_{k<K}c_k\Phi(t)|t|^{-2b-2k}\operatorname{sgn}(\eta)
                     r^{-Q-h_k}+R_K,\qquad
c_k=(-1)^k(b)_k/k!.                                                 \tag{12}
\]

Taylor's formula for \((1+z)^{-b}\), with \(z=t^{-2}r^{-q}\), proves that after any fixed number of \(\xi,\eta\) derivatives the remainder has anisotropic order \(-Q-h_K\). A \(\xi\) derivative costs weight \(A\), and an \(\eta\) derivative costs weight 1. The compact support in \(t\), with its derivatives vanishing at its boundary, justifies these assertions also across the edge of the cone. This is a polyhomogeneous anisotropic symbol with index steps \(q\). If a convention reserves “classical” for integer index steps, that word should be replaced by “polyhomogeneous.”

Choose a smooth partition into \(r\asymp2^n\), \(n\ge0\). The inverse of its \(n\)-th piece has the form

\[
v_n(s,y)=2^{-hn}H_n(2^{An}s,2^ny),                                 \tag{13}
\]

where \(H_n\) is a uniformly bounded family in Schwartz space. To see this directly, rescale the frequency variables to a fixed annulus. All derivatives of the rescaled symbols are bounded uniformly by (12). Integrating by parts in each frequency coordinate then bounds every polynomially weighted derivative of \(H_n\). Thus

\[
|\partial_s^a\partial_y^cv_n|
\le C_{a,c,N}2^{(Aa+c-h)n}
(1+2^{An}|s|+2^n|y|)^{-N}.                                        \tag{14}
\]

On any compact set avoiding the origin, the last factor defeats every derivative factor after taking \(N\) large. The series converges there in every \(C^N\) norm. The low-frequency part is the inverse of a compactly supported distribution and is entire: apply that finite-order distribution to the uniformly convergent exponential power series on its compact support. This proves smoothness off the origin. In particular no unproved assertion about inverse transforms of anisotropic cones is needed.

For \(m\) ordinary derivatives, (14) gives a supremum bound \(C2^{(Am-h)n}\). An increment of size \(d\le1\) has bound

\[
C2^{(Am-h)n}\min(1,2^{An}d).
\]

Split the sum at \(2^{An}d=1\). If \(h-Am=A\alpha\), \(0<\alpha<1\), both geometric sums are bounded by \(Cd^\alpha\). If \(h-Am>A\alpha\), use any slightly stronger exponent below \(\min(1,(h-Am)/A)\). This proves (4), including its noninteger endpoint. When \(h/A\) is an integer, the analogous critical estimate is a Zygmund estimate and does not automatically give that many continuous derivatives or the preceding Lipschitz endpoint.

For completeness, the assertion of failure of \(C^n\) is also independent of formal expansions. Take a smooth frequency test multiplier \(\theta\), supported on a fixed annulus inside the cone, for which \((i\xi)^n\theta a_0\) is not identically zero; here \(a_0\) is the leading symbol in (12). Its inverse is nonzero at some point \(Z\). The anisotropic band projection of \(\partial_s^nv\), evaluated at \((\epsilon^AZ_1,\epsilon Z_2)\), equals

\[
\epsilon^{h-nA}\left(\mathcal F^{-1}[(i\xi)^n\theta a_0](Z)
                                     +O(\epsilon^q)\right).
\]

If \(v\) were \(C^n\) near zero, these projections would be bounded: their rescaled convolution kernels have bounded \(L^1\) norms on a neighborhood of zero. Outside that neighborhood, integrate derivatives onto the Schwartz kernel and use the polynomial growth of \(v\); the contribution tends to zero faster than any prescribed power of \(\epsilon\). The displayed quantity diverges if \(nA>h\), a contradiction.

## 5. What the quasi-homogeneous expansion actually says

For the \(k\)-th homogeneous frequency term in (12), extend through zero by subtracting finitely many Taylor monomials of a test function in its polar integral. The radial power belonging to the derivative with multi-index \((a_1,a_2)\) of that test function at zero is

\[
r^{Aa_1+a_2-h_k-1}.
\]

There are finitely many pairs with \(Aa_1+a_2\le h_k\). Subtraction makes the remaining integral convergent; adding finite-part values for these powers gives a tempered extension. A logarithmic divergence occurs exactly at \(Aa_1+a_2=h_k\). Summing the positive and negative \(\eta\) branches annihilates even \(a_2\). For odd \(a_2\), the residue, apart from the nonzero factorial and Fourier convention factors, is

\[
c_k\int \Phi(t)|t|^{-2b-2k}t^{a_1}\,dt.                            \tag{15}
\]

Rescaling the radial integral proves that its inverse \(u_k\) obeys

\[
u_k(\mu^As,\mu y)=\mu^{h_k}
                [u_k(s,y)+\log\mu\,P_k(s,y)],                     \tag{16}
\]

where \(P_k\) is the polynomial formed from these residues and has weighted degree \(h_k\). This also proves that a truly homogeneous extension exists if and only if all residues at that degree vanish. A change of finite-part normalization adds a polynomial and does not remove a nonzero residue.

The inverse of the high-frequency cutoff of each homogeneous term differs from \(u_k\) by an entire function. Applying the dyadic estimates to the remainder in (12) shows that it is \(C^N\) whenever \(AN<h_K\). Thus for every prescribed integer \(N\), choosing such a \(K\) gives, near zero,

\[
v=\sum_{k<K}u_k+R_N,\qquad R_N\in C^N.                             \tag{17}
\]

The smooth jets in \(R_N\) are part of the answer and can dominate a trace. Smoothness of \(u_k\) off zero follows by the same dyadic integration-by-parts argument, with its low-frequency finite part entire. Formula (16) describes its restriction to any smooth anisotropic sphere and extends it by scaling. It is therefore a complete local expansion, including resonance.

The lead's condition \(h\ne Aa_1+a_2\) is sufficient for the leading term, but stronger than necessary because even \(a_2\) have zero residue and some odd moments vanish. It does not check resonances at later \(h_k\). For a concrete possible nonzero leading residue, take \(A=2,g=2\), so \(h=3\), and choose \(\Phi=i\phi\) with \(\phi\) real even, compactly supported away from zero, \(\int\phi=0\), and \(\int\phi(t)|t|^{-2}dt\ne0\). Two disjoint even bump pairs with equal masses and different radii achieve this. The pair \((a_1,a_2)=(0,3)\) has a nonzero residue. A pure quasi-homogeneous expansion without logarithms is false in this example.

## 6. Infinite dimensionality and frequency cutoffs

The real vector space of \(\Phi=i\phi\), with \(\phi\) real even, compactly supported away from zero and of integral zero, is infinite dimensional. For example take successive disjoint pairs of even bumps inside a fixed compact subset of \(\mathbb R\setminus\{0\}\) and normalize each difference to have zero integral. The Fourier transform off zero recovers \(\Phi\), so the map \(\Phi\mapsto v\) is injective. If \(h/A>3\), (3), (4), and the symmetry statements put all these functions in the class specified in question (1), for every fixed \(\alpha<1\). Thus that frozen infinite-dimensional-kernel claim is confirmed. The profile gradient bound is not part of that particular class.

If instead one multiplies (2) by a smooth frequency cutoff equal to zero near zero and one outside a compact set, no moment condition is necessary. Its equation error has Fourier transform

\[
-(A\xi\partial_\xi+\eta\partial_\eta)\chi\,f.
\]

This is smooth and compactly supported away from zero, hence its inverse is entire and Schwartz. This construction is an approximate frozen solution with analytic error, not an exact kernel element in general.

## 7. Why the proposed classification of all tempered solutions is false

The proposed identification of the previously displayed \(v_d\) family is algebraically correct, with the appropriate one-sided Fourier constants. Indeed, substituting
\(\Phi(t)=c_+t_+^{\lambda-1}+c_-t_-^{\lambda-1}\)
in (2) gives the factors
\((c_+\xi_+^{\lambda-1}+c_-\xi_-^{\lambda-1})
\operatorname{sgn}(\eta)|\eta|^{2b-2-A\lambda}|\zeta|^{-2b}\).
Their total ordinary frequency degree is
\(-3-(A-1)\lambda=-(d+2)\) when \(\lambda=(d-1)/(A-1)\). These data are not compactly supported in \(t\), so the off-origin smoothness and growth theorem for the packets does not apply to them. Their distributional extensions still require the qualifications in the supplied report.

On each half-plane \(\eta>0\) and \(\eta<0\), (6) is conjugate in \((t,r)\) coordinates to differentiation in \(\log r\). Its general distributional solution there is a distribution in \(t\) times the stated integrating factor. The two half-planes have independent data unless oddness is imposed. Thus even locally, “arbitrary function” must be replaced by “distribution” when classifying distributions. Tempered growth and extension across the remaining set must still be imposed. The boundary calculation in Section 1 illustrates a condition that the characteristic ODE alone misses.

Away from \(\xi=0\), a tempered distribution supported on \(\eta=0\) has the form

\[
\sum_{j=0}^N f_j(\xi)\delta^{(j)}(\eta).
\]

Multiplication by the Riesz symbol produces lower derivatives of the delta. Substitution in (6) gives the triangular equations

\[
A\xi f_j'+(A+1-j+g)f_j
+g\sum_{k\ge1}(-1)^k\frac{(j+2k)!}{j!}\xi^{-2k}f_{j+2k}=0.          \tag{18}
\]

Only the top coefficient satisfies the uncoupled homogeneity equation, whose physical exponent is \(\mu_j=(1+g-j)/A\). Lower coefficients are generally forced.

An explicit calculation suffices to refute the pure-mode assertion. Let \(a(s)=|s|^\mu\), \(B(s)=|s|^{\mu+2}/((\mu+1)(\mu+2))\), avoiding the exceptional exponents, and take \(\mu=(g-2)/A\). Then \(B''=a\) and

\[
U_2[y^3a]=-y^3a+6yB,\qquad L_g[y^3a]=6g\,yB\ne0.                 \tag{19}
\]

The needed companion is

\[
v=y^3a-\frac{3g}{A-1}yB.
\]

Indeed \(L_g[yB]=2(A-1)yB\), so this cancels (19). Noninteger homogeneous extensions, for example \(A=3,g=13/2\), make this a distributional example with no polynomial-degree ambiguity. These modes are tempered but generally have excessive growth and singularities away from the origin. Origin-supported Fourier distributions introduce additional polynomial and normalization issues. Thus (18), followed by extension and velocity-domain conditions, is the appropriate starting point for a classification. The lead's identification of all line-supported distributions with the pure monomials is refuted; no full classification is claimed here.

## Dependencies and verification status

Everything above is proved directly from the displayed Fourier law. The external reports supply the problem and notation, not a hidden symbol-calculus theorem. `sources/README.md` records their locations. No numerical calculation is used to establish an inequality for an exact profile. There is no Lean formalization. The common verification record documents the model-review availability limitation.

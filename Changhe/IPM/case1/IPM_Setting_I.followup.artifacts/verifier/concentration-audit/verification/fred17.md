The packet construction yields a genuine infinite-dimensional **frozen** kernel. Several claims about its traces and expansion require correction. The proposed dilation argument is false, and neither a full linearized kernel nor a nonlinear family follows.

Complete proofs, counterexamples, and verification records are in the [reading-order index](lead-run-records/verifier/fred17/README.md).

**(1) Frozen kernel theorem: CONFIRMED after corrections; REFUTED as stated.**

Write
\[
q=2(A-1),\qquad b=g_*/q,\qquad h=1+g_*,\qquad Q=A+1.
\]
The reality condition is
\[
\Phi(-t)=-\overline{\Phi(t)}.
\]
Assume also \(\int\Phi=0\).

The Fourier formula is correct. Its extension must be specified: use the distributional limit of its truncations to \(|\eta|>\epsilon\). With \(r=|\eta|\), \(\xi=tr^A\), its pairing with a Schwartz function \(\varphi\) becomes
\[
\int_0^\infty r^{-2}\int\Phi(t)(1+t^2r^q)^{-b}
 [\varphi(tr^A,r)-\varphi(tr^A,-r)]\,dt\,dr.
\]
The bracket equals \(2r\varphi_\eta(0)+O(r^{A+1}+r^3)\). The moment condition cancels the first term; the remaining radial powers are integrable. The boundary term in the Fourier equation tends to zero by the same cancellation. Thus there is **no residual distribution at zero frequency**.

The inverse is the locally uniformly convergent grouped integral
\[
v(s,y)=\frac{2i}{(2\pi)^2}
\int_0^\infty\frac{\sin(yr)}{r^2}
 \int\Phi(t)e^{istr^A}(1+t^2r^q)^{-b}\,dt\,dr.
\]
It is real, continuous, odd in \(y\), and solves \(L_gv=0\).

The second velocity component has an equally convergent integral obtained by inserting
\[
-\frac{t^2r^q}{1+t^2r^q}.
\]
It is the unique odd-in-\(y\), sublinear second component satisfying the div-curl equations. With only oddness in \(y\), the horizontal velocity retains an additive constant ambiguity. For \(A>2\), its integrable Fourier transform selects the velocity tending to zero at infinity. Full centered parity also fixes that ambiguity.

The correct growth bound is
\[
|v(X)|\le C(1+|X|)^{1/A}.
\]
This exponent is optimal for every nonzero packet. Indeed,
\[
R^{-1}v(R^As,Ry)\longrightarrow V_0(s,y)\ne0,
\]
where \(V_0\) is obtained by replacing \((1+t^2r^q)^{-b}\) by \(1\) in the integral.

There is an important restriction: **every nonzero packet fails the profile’s stronger weighted gradient bound for every \(\gamma<1\)**. Such a bound would force
\[
\partial_y[R^{-1}v(R^As,Ry)]
=\partial_yv(R^As,Ry)\longrightarrow0
\]
on compact sets with \(s\ne0\). The limit \(V_0\) would then be independent of \(y\); oddness would make it zero, a contradiction. Physical cutoff removes this far-field problem.

The anisotropic symbol argument is valid, with an explicit dyadic proof. Frequency pieces with \(|\eta|\asymp2^n\) have inverse transforms
\[
v_n(s,y)=2^{-hn}H_n(2^{An}s,2^ny),
\]
where \(H_n\) are uniformly Schwartz. Consequently
\[
|\partial_s^a\partial_y^cv_n|
\le C_N2^{(Aa+c-h)n}
(1+2^{An}|s|+2^n|y|)^{-N}.
\]
This proves smoothness away from zero. Splitting an increment estimate at \(2^{An}|X-X'|=1\) proves
\[
v\in C^{m,\alpha}_{\rm loc}
\quad\text{if}\quad
(m+\alpha)A\le h,\qquad 0<\alpha<1.
\]
No non-resonance assumption is needed for this assertion, including its noninteger endpoint. At integer critical regularity, the automatic endpoint is Zygmund, not necessarily classical differentiability.

The expansion needs two corrections:

* It includes smooth Taylor terms.
* Its terms of weighted degrees \(h_k=h+2k(A-1)\) can have logarithms.

More precisely,
\[
v=\sum_{k<K}u_k+R_N,\qquad R_N\in C^N,
\]
for sufficiently large \(K\), with
\[
u_k(\mu^As,\mu y)
=\mu^{h_k}\bigl(u_k(s,y)+\log\mu\,P_k(s,y)\bigr).
\]
A possible residue occurs when
\[
h_k=Aa_1+a_2,\qquad a_2\ \text{odd},
\]
and is proportional to
\[
\int\Phi(t)|t|^{-2b-2k}t^{a_1}\,dt.
\]
Vanishing of these residues, rather than non-resonance alone, is the precise condition for pure quasi-homogeneity. Checking only the leading degree does not check later resonances.

Every nonzero packet fails \(C^n\) when \(nA>h\): a suitable anisotropic frequency projection of \(\partial_s^nv\) grows like \(\epsilon^{h-nA}\), contradicting local boundedness if \(v\) were \(C^n\).

Therefore, **CONFIRMED**: if \(h/A>3\), the specified frozen kernel is infinite dimensional for every \(\alpha<1\). Restricting to imaginary even \(\Phi\) of integral zero already gives an infinite-dimensional real subspace. If additionally \(h/A<4\), every nonzero member fails \(C^4\).

The identification of the supplied \(v_d\) family by power-law \(\Phi\) is algebraically correct. Those \(\Phi\) are not compactly supported, so the packet theorem does not apply to them.

The proposed classification of **all tempered solutions is REFUTED as stated**. Characteristic data must be allowed to be distributions, and extension and velocity-domain conditions remain. Moreover, line-supported Fourier distributions form triangular systems, not pure conormal monomials. For example, if
\[
a(s)=|s|^{(g_*-2)/A},\qquad B''=a,
\]
with nonexceptional homogeneous extensions, then
\[
U_2[y^3a]=-y^3a+6yB,\qquad L_g[y^3a]=6g_*yB\ne0.
\]
The companion
\[
y^3a-\frac{3g_*}{A-1}yB
\]
cancels this error. Origin-supported Fourier terms require additional normalization.

See [the frozen proof](lead-run-records/verifier/fred17/01_frozen/PROOF.md).

**(2) Axis traces and velocity: the exponents are CONFIRMED as possible nonsmooth terms; the literal full asymptotics are REFUTED.**

Set
\[
G_j(s)=\frac{\partial_y^jv(s,0)}{j!},
\qquad \mu_j=\frac{1+g_*-j}{A}.
\]
For positive noninteger \(\mu_j\), the correct expansion is
\[
G_j(s)=\sum_{0\le n<\mu_j}a_{jn}s^n
+C_{j,\pm}|s|^{\mu_j}+o(|s|^{\mu_j}).
\]
Coefficients may vanish. At nonnegative integer degrees, logarithms can occur.

The smooth terms are genuinely present. For \(g_*>j-1\),
\[
G_j(0)=
\frac{2i^j}{(2\pi)^2j!q}
B\!\left(\frac{j-1}{q},\frac{g_*-j+1}{q}\right)
\int\Phi(t)|t|^{-(j-1)/(A-1)}\,dt.
\]
An imaginary even difference of two equal-mass bumps at different radii has integral zero but a nonzero weighted integral. Thus \(G_3(0)\ne0\) is possible in the trial parameter range, contradicting the claimed full asymptotic tending to zero.

The general conclusions are:

* \(G_j\) is bounded and continuous if \(g_*>j-1\).
* At equality, logarithmic divergence is possible.
* Below that threshold, power divergence is possible.

For example, \(A=2,g_*=1\), with suitable admissible \(\Phi\), gives \(G_3(s)\sim C|s|^{-1/2}\), \(C\ne0\). Universal boundedness of the third trace is therefore false.

Nevertheless, **every odd normalized endpoint limit vanishes**:
\[
|s|^{(j-1)/A}G_j(s)\longrightarrow0,
\qquad j\ge3.
\]
The worst fractional exponent after multiplication is
\[
\mu_j+\frac{j-1}{A}=\frac{g_*}{A}>0,
\]
and possible logarithms do not prevent convergence.

For the horizontal velocity, the leading possible nonsmooth axis degree is
\[
d_w=1+\frac{g_*}{A}.
\]
There are again preceding smooth terms and possible logarithms at integer degrees. If \(d_w\notin\mathbb N\), the guaranteed trace class is
\[
C^{\lfloor d_w\rfloor,d_w-\lfloor d_w\rfloor}.
\]
An exact consistency identity is
\[
U_1'(s,0)=\frac{A}{g_*}\,sG_1'(s),
\]
which also gives \(U_1'(0)=0\).

At the supplied trial values, the possible fractional degrees are approximately
\[
\mu_3=2.7338,\qquad \mu_5=2.5368,\qquad
\mu_7=2.3397,\qquad d_w=3.9308.
\]
Thus \(G_3,G_5,G_7\) are bounded and their normalized limits vanish for those parameter inequalities. These arithmetic observations are not certified parameters of an exact profile.

See [the axis proof](lead-run-records/verifier/fred17/02_axis/PROOF.md).

**(3a) Full linearization: the proposed dilation proof is REFUTED. A different, precisely scoped non-semi-Fredholm theorem is CONFIRMED.**

At an exact profile, let
\[
Tv=W\cdot\nabla v-v+U[v]\cdot\nabla\rho.
\]
For a translated frozen packet and a cutoff \(\chi=1\) near \(P\),
\[
\begin{aligned}
T(\chi v)={}&
\chi(W-W_0)\cdot\nabla v
+\chi(\nabla\rho-g_*e_y)\cdot U[v]\\
&+(W\cdot\nabla\chi)v+[U,\chi]v\cdot\nabla\rho .
\end{aligned}
\]
For the frozen operator, the physical-cutoff error is smooth. For a merely \(P_2\) background, the displayed full error is generally only safely in \(C^{1,\sigma}_{\rm loc}\), with \(\sigma\) bounded by the background and packet exponents. It is not automatically smooth or small.

The frozen operator is **not** anisotropically invariant. For a shrinking packet, the rescaled velocity multiplier is
\[
-\frac{\xi^2}{\xi^2+\epsilon^{2A-2}\eta^2},
\]
which differs from the original multiplier.

Variable coefficients create another obstruction: an allowed term \(cy^2\partial_s\) becomes
\[
c\epsilon^{2-A}y^2\partial_s.
\]
It is not small when \(A>2\). Ordinary quadratic Taylor control cannot justify the proposed argument.

A valid theorem is available for the following spaces. Let \(K\Subset\Omega\), with \(K\) containing a neighborhood of \(P\), and assume \(W,\rho\in C^{2,\sigma}\) near \(\overline\Omega\), \(W(P)=0\). Then
\[
T:\{v\in C^{2,\sigma}(\mathbb R^2):\operatorname{supp}v\subset K\}
\longrightarrow C^{1,\sigma}(\overline\Omega)
\]
is **not upper semi-Fredholm**.

Indeed, smooth bumps
\[
v_\epsilon(X)=\epsilon^{2+\sigma}\varphi((X-P)/\epsilon)
\]
have \(C^{2,\sigma}\)-norm bounded above and below, tend to zero in \(C^2\), and satisfy
\[
\|Tv_\epsilon\|_{C^{1,\sigma}}=O(\epsilon).
\]
Finite-dimensional kernel and closed range would give
\[
\operatorname{dist}(v_\epsilon,\ker T)\le C\|Tv_\epsilon\|,
\]
forcing a strongly convergent subsequence, a contradiction. Odd bumps and reflected pairs preserve the required symmetries.

This is a theorem for the specified map losing one derivative. Its global extension requires explicit tail estimates for the chosen global norms. It neither proves a nonzero exact kernel nor applies automatically to other graph norms.

**(3b) Correction and nonlinear continuation: UNCLEAR for the full problem.**

Let \(Z\) be a correction class preserving the packet germ, for example corrections smooth near \(P\). The exact linear range condition is
\[
-Tq_\Phi\in T(Z).
\]
Smoothness of the error does not establish this condition. Allowing correction in the unrestricted domain makes it vacuous, since \(z=-q_\Phi\) always removes the packet.

A controlled right inverse \(S\), valued in \(Z\), would give
\[
k_\Phi=q_\Phi-S(Tq_\Phi)\in\ker T.
\]
Independence of the packet germs modulo \(Z\) would then give independent exact kernel elements. Neither this right inverse nor its required estimates is presently supplied.

Even that would not prove nonlinear families. The map \(F(u)=\|u\|^2\) on an infinite-dimensional Hilbert space has derivative kernel equal to the entire space at zero, while its zero is isolated. A sufficient nonlinear route requires an appropriate differentiable formulation and a split surjective derivative, or a theorem solving the remaining cokernel equations, with tame estimates if derivatives are lost.

Before correction, the cutoff packets vanish near the center. A nonlocal correction need not remain smooth there. Preservation of \(P_\infty\) must be imposed or proved through a separate center-regularity argument.

**(3c) Q1: UNCLEAR in both \(P_2\) and \(P_\infty\).**

The frozen construction decides neither isolation nor a family in either class. The statement

> An isolated solution of a \(P\)-regular discretization does not decide Q1

is **CONFIRMED** as a statement about discrete isolation alone.

A finite smooth basis excludes the nonsmooth packets exactly. Smooth functions can nevertheless approximate their cutoffs in \(C^{2,\alpha}\) when \(h/A>3\). What is missing is a continuum stability and convergence theorem, not merely a richer finite basis.

See [the full-operator proof](lead-run-records/verifier/fred17/03_full/PROOF.md).

**(4) Endpoints: conditional obstruction statements are CONFIRMED; neither endpoint follows.**

For an exact profile with the necessary trace and finite-part hypotheses,
\[
C_{0,j}=l_j+B_j.
\]
Therefore, on a hypothetical exact family with \(l_3=0\), smoothness at the center requires \(B_3=0\).

Vanishing of \(l_3\) alone does **not** turn the higher conditions into \(B_5=B_7=0\). Those require the corresponding higher endpoint conditions. Frozen vanishing of all \(l_j\) has not been transferred through nonlinear corrections.

At every nonresonant center order, smoothness requires
\[
C_{0,j}=0.
\]
At resonant orders, a smooth even-power coefficient need not vanish; the appropriate compatibility conditions must instead be checked. Even all necessary conditions are not presently proved sufficient to bootstrap a finitely regular coupled profile to a smooth center.

The report’s **numerical YES_inf** milestone requires its stated candidate and verification tests. A rigorous existence theorem additionally requires an exact admissible profile, all necessary compatibility conditions, and a sufficient smoothness argument.

For **NO_inf**, proving \(B_3\ne0\) everywhere on a family with \(l_3=0\) would be sufficient, but is not necessary. It could instead be proved that \(B_3=0\) forces a higher obstruction to be nonzero. The relevant target is absence of a common compatible zero. Exclusion on a local family becomes a global exclusion only if that family exhausts the claimed scope.

What remains is exact-profile existence, suitable global spaces, a valid variable-coefficient construction, restricted range solvability, nonlinear integrability, preservation of endpoint limits, and center smoothness or an obstruction excluding it. The frozen theorem does not resolve those steps.

See [the endpoint proof](lead-run-records/verifier/fred17/04_endpoints/PROOF.md).

Six exact symbolic algebra checks passed. Opus 5.5 consultation was attempted, but the configured Bedrock credentials were unavailable before invocation; no model answered and no independent Opus review was obtained.
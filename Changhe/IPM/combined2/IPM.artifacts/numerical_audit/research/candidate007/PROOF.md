# Exact Candidate 007 and independent residual evaluation

## Statement, data and scope

The input is the immutable JSON at `../../data/candidate007_exact.json`, whose SHA256 is `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`. Its parameter is

\[
c=4076476460239181/2251799813685248,\qquad
\gamma=1/c,\quad \lambda=1-\gamma,\quad
p_j=(3+\gamma-j\lambda)/2.
\]

For \(s=x^2+y^2\), \(t=s/(1+s)\), and \(H_m=\operatorname{Re}(x+iy)^{2m}\), a generator is
\(aH_m(1+s)^{p_j-m}T(t)\), with exact rational \(a\), where \(T=t^h\) or \(t^wP_n(2t-1)\). The fields and residual are

\[
\rho=-\partial_y\Delta\chi,\quad
u=(-\chi_{xyy},\chi_{xxy}),\quad
F=(cX+u)\cdot\nabla\rho-\rho.
\]

The claims to be checked are the input identity, canonical coefficient conversion, origin normalization, and the eleven asserted zero far-field sectors. Norm calculations will explicitly distinguish exact angular integration, floating radial quadrature, and rigorous whole-plane enclosures. Nothing here supplies the full stationary inverse or an existence theorem.

## Canonical conversion

Rodrigues' polynomial identity gives

\[
P_n(2t-1)=\sum_{a=0}^n(-1)^{n-a}\binom na\binom{n+a}a t^a.
\]

This follows by differentiating \(t^n(t-1)^n\) exactly \(n\) times and dividing by \(n!\). A monomial \(t^h\) in a generator becomes
\(r^{2(m+h)}(1+r^2)^{p_j-m-h}\cos(2m\theta)\). Thus summing the rational polynomial coefficients gives a canonical dictionary \(A_{jmk}\), with \(k=m+h\). The code checks the binomial formula against a separate three-term Legendre recurrence before using it. It never reads a floating coefficient as authority.

Every term is smooth at the origin: \(r^{2k}\cos(2m\theta)=H_m s^{k-m}\) and \(k\ge m\). The potential is even in both coordinates. Three derivatives give the stated S1 parity of \(\rho\), and the velocity is divergence-free by equality of mixed derivatives.

## Origin calculation

Only the homogeneous quartic part of \(\chi\) contributes to \(a_0=\rho_y(0)\) and \(\ell=\partial_yu_2(0)\). For \(m=0,1,2\), define

\[
C_m=\sum_{j,k\le2} A_{jmk}\binom{p_j-k}{2-k}.
\]

The quartic harmonics are \(C_0(x^2+y^2)^2\), \(C_1(x^4-y^4)\), and \(C_2(x^4-6x^2y^2+y^4)\). Direct differentiation therefore gives

\[
\ell=8C_0-24C_2,\qquad a_0=-32C_0+24C_1.
\]

The normalization is exactly \(c+\ell=1\). At the origin the velocity vanishes by parity, \(\rho(0)=0\), and \(\rho_x(0)=0\). Differentiating the residual at zero consequently gives \(F_y(0)=a_0(c+\ell-1)\). These are finite rational checks, with no numerical limit evaluation.

## Independent homogeneous Fourier algebra

Write a homogeneous term as \(r^q e^{in\theta}\). Direct use of the polar Cartesian derivatives yields

\[
\partial_x(r^q e^{in\theta})=
\tfrac{q+n}{2}r^{q-1}e^{i(n-1)\theta}
+\tfrac{q-n}{2}r^{q-1}e^{i(n+1)\theta},
\]

\[
\partial_y(r^q e^{in\theta})=
\tfrac{i(q+n)}2r^{q-1}e^{i(n-1)\theta}
+\tfrac{i(n-q)}2r^{q-1}e^{i(n+1)\theta}.
\]

Cosine coefficients are split between positive and negative modes, except for the constant. The checker stores the factor \(i\) of an odd field separately, so all coefficient operations remain rational. Differentiation shifts the radial degree down by one. Multiplication convolves integer frequencies and adds the radial degrees. This independently reconstructs \(\rho,u,\nabla\rho\) and the nonlinear product for each retained far-field sector.

## Far-field sectors and completeness of the finite check

For \(r>1\), the ordinary binomial series is absolutely convergent and differentiable on each closed exterior bounded away from 1:

\[
r^{2k}(1+r^2)^{p_j-k}
=r^{2p_j}\sum_{n\ge0}\binom{p_j-k}{n}r^{-2n}.
\]

After three derivatives the field degree is \(d_{j,n}=\gamma-j\lambda-2n\). The linear residual contribution is \((cd_{j,n}-1)\rho_{j,n}\). The product of velocity branch \((j_1,n_1)\) with a density gradient branch \((j_2,n_2)\) has degree

\[
d_{j_1,n_1}+d_{j_2,n_2}-1
=\gamma-(j_1+j_2+1)\lambda-2(n_1+n_2).
\]

The residual thus has sectors \(r^{\gamma-J\lambda-2N}E_{J,N}(\theta)\). The asserted eleven cancellations are \((J,0)\) for \(0\le J\le7\), and \((0,1),(1,1),(2,1)\). The leading \((0,0)\) sector vanishes identically because \(c\gamma=1\). The first permitted surviving exponent is \(d_{3,1}=-2.790444924\ldots\), preceding \(d_{8,0}=-3.028501079\ldots\). Exact rational ordering proves these statements. All sectors with \(N\ge2\) have degree at most \(\gamma-4<-3\); all sectors with \(J\ge8,N=0\) have degree at most \(d_{8,0}\). Hence the finite list covers every degree larger than \(d_{3,1}\).

Once the eleven cancellations pass, the convergent expansion and the finite branch count imply \(F=O(r^{d_{3,1}})\), with corresponding derivative decay. This proves qualitative square integrability. It does not bound the tail constant or certify a numerical norm.

## Verification protocol

The implementation is new code in `code/`, using only exact strings from the copied JSON. Evidence binds source and implementation hashes and records real UTC start and finish times. The check includes simple manufactured homogeneous polynomials, the two independent Legendre constructions, and symmetry of every computed Fourier sector. Candidate-specific claims remain OPEN until their successful output is entered in `../../AUDIT_LEDGER.md`. Historical audit code is read for conventions but is not executed by this independent implementation.

## Full radial polynomial representation and exact norm identity

This is a verification formula for the given finite potential. It is not a new inverse estimate. Put \(u=1-t=(1+r^2)^{-1}\). A radial Fourier term \(r^e u^aP(t)e^{in\theta}\) has radial derivative \(r^{e-1}u^aDP\), where

\[
DP=(e-2at)P+2t(1-t)P'.
\]

Thus Cartesian differentiation shifts its angular frequencies to \(n-1,n+1\), with radial polynomials \((DP+nP)/2,(DP-nP)/2\) for \(x\), and \(i(DP+nP)/2,-i(DP-nP)/2\) for \(y\). Start with \(e=0,a=-p_j,P=\sum_k A_{jmk}t^k\), splitting the cosine into its two Fourier modes. After three derivatives \(e=-3\). Each resulting polynomial has an exact factor \(t^2\): origin smoothness and the odd degree-three field imply this, and the checker verifies it coefficient by coefficient before division. Since \(r^{-3}t^2=ru^2\), the fields have the form

\[
\rho_j=r u^{(j+1)\lambda/2}Q_j(t,\theta),\qquad
u_j=r u^{(j+1)\lambda/2}V_j(t,\theta).
\]

Their density gradients have radial prefactor 1. The preceding recurrence at \(e=1\) computes them without approximation. The linear residual is \(ru^{(j+1)\lambda/2}(cD-1)Q_j\). Products of the velocity and density-gradient polynomials give the nonlinear residual, indexed by \(J=j_1+j_2+1\). Consequently

\[
F=r\sum_{J=0}^{15}u^{a_J}\sum_{n>0\text{ odd}}Q_{J,n}(t)\sin(n\theta),
\qquad a_J=(J+1)\lambda/2.
\]

Every polynomial in this identity is rational and finite. Fourier convolution includes both positive and negative modes, and the complete source has no angular truncation. A packed univariate polynomial product may encode \(t^kz^n\) as \(X^{k+Bn}\), after a nonnegative angular shift, provided \(B\) exceeds the sum of the input radial degrees. The product then has no carry between angular blocks; undoing the shift recovers exactly the bivariate coefficients. The checker compares this operation against direct convolution on small fields before using it.

For each \((J,n)\), substitute \(t=1-u\), extract the exact initial factor \(u^{q_{J,n}}\), and call the remaining polynomial \(P_{J,n}(u)\). The eleven cancellation checks imply the strict integrability inequalities below. Complete angular orthogonality and \(r\,dr=-du/(2u^2)\) give

\[
\|F\|_2^2=\frac\pi2\sum_n\sum_{J,K}
\int_0^1 u^{a_J+a_K+q_{J,n}+q_{K,n}-3}(1-u)
P_{J,n}(u)P_{K,n}(u)\,du.
\]

The terms with \(J<K\) have multiplicity two when the sum is taken over unordered pairs. An omitted branch would invalidate an upper bound. For a diagonal term the exponent \(2a_J+2q_{J,n}-3\) must be greater than \(-1\); the checker requires this rational inequality for every nonzero polynomial. It then holds for each cross term by averaging. If the product polynomial including \((1-u)\) is \(\sum_d b_du^d\), its integral is exactly \(\sum_d b_d/(a_J+a_K+q_{J,n}+q_{K,n}-2+d)\). All denominators are strictly positive.

This finite expression is evaluated with outward Arb balls at a stated precision. Rational conversion, polynomial multiplication, division, summation, multiplication by \(\pi\), and the final square root are enclosed. Precision is increased if cancellation leaves an inconclusive result. The output must include every source mode, a positive containing norm ball, exact endpoint orders, and implementation and input hashes. A successful result proves a quantitative whole-plane norm enclosure without radial quadrature or an omitted exterior tail. Comparisons with independent radial quadrature are separate implementation diagnostics.

## Strong weighted regularity membership

Let \(d_* = \gamma-3\lambda-2=-2.790444924\ldots\). If the eleven zero sectors pass, the first surviving sector is nonzero, and the recorded finite expansions are the exact potential, then for every noninteger \(s>0\)

\[
\|\langle X\rangle^\sigma F\|_{C^s(\mathbb R^2)}<\infty
\quad\text{if and only if}\quad \sigma\le-d_*.
\]

Here the inhomogeneous global norm includes the supremum of the function and all derivatives through \(\lfloor s\rfloor\), and the global Hölder seminorm of derivatives of that order. To prove sufficiency, the convergent far-field expansion gives \(D^qF=O(r^{d_*-q})\) for each fixed integer \(q\). Product differentiation of the smooth weight gives \(D^q(\langle X\rangle^\sigma F)=O(r^{\sigma+d_*-q})\). These derivatives are bounded for all \(q\ge0\) when \(\sigma+d_*\le0\); boundedness on the remaining compact set follows from smoothness. If \(g\) has bounded derivatives of orders \(m,m+1\), then for \(0<\eta<1\) the difference of \(D^mg\) at points of distance at most 1 is bounded by its Lipschitz constant times that distance, while at larger distances it is bounded by \(2\|D^mg\|_\infty\). Dividing by distance to the power \(\eta\) proves the global seminorm is finite. Necessity follows by choosing an angle where the nonzero leading trigonometric polynomial is nonzero: along that ray, the weighted function grows like a nonzero multiple of \(r^{\sigma+d_*}\). This is a qualitative membership statement. It does not estimate the strong norm's numerical size.

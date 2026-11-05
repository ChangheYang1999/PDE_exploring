# Explicit tame source commutator in the Q norm

Status: proved estimate in terms of explicitly defined coefficient constants. Candidate013's numerical coefficient bounds remain obligations. This is not a numerical closure or existence claim.

Use unitary Fourier transform in two dimensions. Set \(q=2+\delta=21/10\), \(J=(1-\Delta)^{1/2}\), \(W=(1+4|x|^2)^{1/2}\), \(b=\nabla\rho_*\), and
\[
 M_s(f)=(2\pi)^{-1}\int_{\mathbb R^2}|\xi|^s|\widehat f(\xi)|\,d\xi.
\]
For vector and matrix arrays the absolute value is Euclidean/Frobenius. In particular \(M_s(xb)\) means the Frobenius array with entries \(x_jb_k\). Define
\[
 H_1=\sup_x W(x)|Db(x)|_F,\qquad c_q=\frac{q(q-1)}2,
\]
\[
 A_s=M_s(b)+2M_s(xb)+4M_{s-1}(b),\qquad s=2,2+\delta.
\]
The source commutator satisfies
\[
 \boxed{\|W[J^q,b\cdot]U[g]\|_2
 \le qH_1\|J^{q-1}g\|_2
 +c_q A_2\|J^\delta g\|_2+c_q A_{2+\delta}\|g\|_2.}
\]
Consequently, for a test function with \(Q(g)=\|WJ^qg\|_2\ge M>0\), \(\|g\|_2\le R\), writing \(r=R/M\),
\[
 \boxed{\frac{|\langle W[J^q,b\cdot]U[g],WJ^qg\rangle|}{Q(g)^2}
 \le qH_1r^{1/q}+c_qA_2r^{1-\delta/q}+c_qA_{2+\delta}r.}
\]
The condition \(Q(g)\ge M\) is explicit: this is suitable for an outside-ball barrier, rather than a claim of a uniform frozen-generator bound at every test amplitude.

## Fourier remainder

Let \(m(\eta)=(1+|\eta|^2)^{q/2}\). With \(\zeta\) the coefficient frequency, subtract its first Taylor term:
\[
 r_q(\eta+\zeta,\eta)=m(\eta+\zeta)-m(\eta)-\nabla m(\eta)\cdot\zeta.
\]
The exact physical first term is
\[
 [J^q,b\cdot]U[g]=-q\sum_j(\partial_jb)\cdot\partial_jJ^{q-2}U[g]+\mathcal R_bU[g].
\]
The minus sign comes from multiplying the two physical derivatives. Since
\(\|D^2m(\xi)\|_{op}\le q(q-1)J(\xi)^\delta\), and \(J(\eta+t\zeta)^\delta\le J(\eta)^\delta+|\zeta|^\delta\), integral Taylor remainder gives
\[
 |r_q|\le c_q|\zeta|^2(J(\eta)^\delta+|\zeta|^\delta),
\]
\[
 |\nabla_\xi r_q|\le2c_q|\zeta|(J(\eta)^\delta+|\zeta|^\delta).
\]
Here the derivative is with respect to the output frequency at fixed input frequency, so \(\nabla_\xi r_q=\nabla m(\eta+\zeta)-\nabla m(\eta)\). Weighted Young convolution therefore gives
\[
 \|\mathcal R_bU[g]\|_2\le c_q(M_2(b)\|J^\delta g\|_2+M_{2+\delta}(b)\|g\|_2).
\]
Multiplication by \(x_j\) differentiates the output Fourier variable. Its derivative either acts on \(\widehat b(\zeta)\), giving \(\mathcal R_{xb}\), or on \(r_q\), giving the preceding gradient bound. It does not differentiate the velocity multiplier, which depends only on the fixed input frequency. Thus
\[
 \|x\mathcal R_bU[g]\|_2\le c_q(M_2(xb)\|J^\delta g\|_2+M_{2+\delta}(xb)\|g\|_2)
 +2c_q(M_1(b)\|J^\delta g\|_2+M_{1+\delta}(b)\|g\|_2).
\]
Use \(\|Wh\|_2\le\|h\|_2+2\|xh\|_2\). The principal Taylor term is bounded by \(qH_1\|J^{q-1}g\|_2\), because the joint multiplier \(\nabla J^{q-2}U\) has Euclidean norm at most \(J^{q-1}\). This proves the first box. Standard L2 interpolation between \(\|g\|_2\) and \(\|J^qg\|_2\le Q(g)\) proves the second.

## Wiener moments from integer Sobolev seminorms

For \(0\le\sigma<1\), \(A=\||D|^m f\|_2\), and \(B=\||D|^{m+2}f\|_2\),
\[
 \boxed{M_{m+\sigma}(f)\le C_\sigma
 A^{(1-\sigma)/2}B^{(1+\sigma)/2}},
\]
\[
 C_\sigma=\frac1{2\sqrt{\cos(\pi\sigma/2)}
 (1-\sigma)^{(1-\sigma)/4}(1+\sigma)^{(1+\sigma)/4}}.
\]
In particular \(M_m(f)\le\tfrac12\sqrt{AB}\). To check the normalization and constant, Cauchy–Schwarz with the weight \(1+(|\xi|/a)^4\) yields
\[
 M_{m+\sigma}(f)^2\le
 \frac{a^{2+2\sigma}}{8\cos(\pi\sigma/2)}(A^2+a^{-4}B^2).
\]
Optimize at \(a^4=((1-\sigma)/(1+\sigma))(B/A)^2\). The displayed constant follows; the cases \(A=0\) or \(B=0\) follow by limits.

For Candidate013 this route requires only \(D^1b,D^3b,D^2b,D^4b,D^2(xb),D^4(xb)\) in L2, plus the weighted Hessian supremum \(H_1\). These are derivatives of the exact potential of at most the corresponding finite integer order. Although \(xb\) grows weakly at infinity, its second derivatives are L2. The homogeneous Fourier expressions at orders at least two are defined by those derivatives; polynomial distribution ambiguities at frequency zero disappear under the displayed weighted factors. No step assumes \(xb\in L^2\).

For completeness, the needed limiting argument is available from the exact far decay. Candidate013 satisfies
\[
 |D^j b(x)|\le C_j(1+r)^{-\gamma-j},\qquad
 \gamma=1-1/c>0,
\]
at all finite orders used here; the exact far expansion and its differentiated remainder give this fact with finite constants. Let \(\vartheta\) be a fixed smooth radial cutoff equal to one for \(r\le1\), zero for \(r\ge2\), and put \(b_N=\vartheta(r/N)b\). Product differentiation and radial integration imply
\[
 \|D^m(b_N-b)\|_2=O(N^{1-\gamma-m}),\quad m\ge1,
\]
\[
 \|D^m(x(b_N-b))\|_2=O(N^{2-\gamma-m}),\quad m\ge2.
\]
Also \(\sup W|D(b_N-b)|=O(N^{-\gamma})\). Thus all moment constants needed in the boxed estimate for coefficient differences tend to zero by the integer-seminorm inequality. Apply the already proved identities to the compactly supported smooth \(b_N\). Their commutators are Cauchy in the displayed weighted L2 norm, and their distributional limit is the desired commutator: multiplication by \(b_N\) and by its finite derivatives converges to multiplication by \(b\) on each Schwartz test and on the tempered functions obtained by applying the fixed Fourier multipliers. The principal term converges by the weighted derivative supremum as well. This proves the boxed inequalities for Candidate013 with its actual finite constants, without imposing an L2 assumption on \(b\) or \(xb\). Computing and certifying sufficiently small numerical values of those constants remains separate.

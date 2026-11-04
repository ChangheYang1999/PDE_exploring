# A constant background for every bounded rotating profile

Status: CONFIRMED A406-A407 after independent literature and configured-model
reviews, followed by the checks recorded below. This does not prove
decaying-profile nonexistence in the target interval.

## Statement

Let \(0<c<1\), \(\omega\in\mathbb R\), \(J(y_1,y_2,y_3)=(-y_2,y_1,0)\),
\[
 A=cI-\omega J,\qquad M=(1-c)I+\omega J.
\]
Suppose \(U\in C^1(\mathbb R^3;\mathbb R^3)\) is bounded and
\(P\in C^1(\mathbb R^3)\) satisfies
\[
 MU+(Ay+U)\cdot\nabla U+\nabla P=0,\qquad
 \operatorname{div}U=0.                                      \tag{1}
\]
No decay or distributional dilation limit is assumed.

There is a unique vector \(b\in\mathbb R^3\) such that
\[
 U(R\,\cdot)\longrightarrow b\quad\hbox{in distributions,
 and weak star in }L^\infty,\qquad R\to\infty.                \tag{2}
\]
If \(G[U]\) denotes the canonical double-Riesz pressure gradient,
defined on compact tests as in A031, then
\[
 \nabla P=G[U]-Mb.                                          \tag{3}
\]
Set \(z_0=-A^{-1}b\), which is defined since \(c>0\), and put
\[
 W(y)=U(y+z_0)-b,\qquad
 \widetilde P(y)=P(y+z_0)+(Mb)\cdot y .
\]
Then \((W,\widetilde P)\) solves the same profile equation (1), with
the same \(c,\omega\), and \(W\) satisfies the boundedness and
distributional-dilation hypothesis Hb.

Consequently the already established energy theorem applies to \(W\):
for \(0<c<2/5\), \(U\) is constant; at \(c=2/5\), \(W\in L^2\)
with exterior energy \(O(R^{-5})\); for \(2/5<c<1\),
\[
 \int_{|y|<R}|W|^2=L R^{5-2/c}+O(R^{4-2/c}),
\]
where \(L>0\) unless \(U\) is constant. These are relative-background
statements. They do not license the unmodified energy theorem for an
arbitrary bounded \(U\), and (2) does not assert pointwise convergence
to \(b\) at infinity.

## 1. The harmonic pressure gradient is constant

Write \(F_{ij}=U_iU_j\), \(T_{ij}=R_iR_j\), and define
\[
 \langle G_k[U],\phi\rangle
    =-\sum_{i,j}\int F_{ij}\,T_{ij}\partial_k\phi .
                                                               \tag{4}
\]
The integrability and continuity of \(T_{ij}\partial_k\phi\) follow
from its L2 bound near the support and its \(O(|y|^{-4})\) tail.
The same definition on Schwartz tests is tempered, as in A031.
It defines the gradient of a canonical pressure modulo constants.

The Poisson equation from (1) is
\(-\Delta P=\partial_i\partial_jF_{ij}\). Thus each component of
\(\nabla P-G[U]\) is harmonic in the space of tempered distributions.
Indeed, on Schwartz tests, \(T_{ij}\partial_k\Delta\phi
=-\partial_i\partial_j\partial_k\phi\), which gives
\(\Delta G_k=-\partial_k\partial_i\partial_j F_{ij}\). Moreover (1) gives the tempered
distributional identity
\[
 \partial_kP=-(1-4c)U_k-\omega(JU)_k
              -\partial_j((Ay)_jU_k+U_jU_k).
                                                               \tag{5}
\]
Every term is tempered because \(U\) is bounded. A tempered harmonic
distribution is a polynomial, by Fourier support at the origin.
Therefore \(\nabla P-G[U]\) is a vector polynomial \(H(y)\).

For \(U_R(z)=U(Rz)\), scaling (1) gives
\[
 (\nabla P)(Rz)=-MU_R-(Az\cdot\nabla)U_R
                  -R^{-1}\operatorname{div}(U_R\otimes U_R).
                                                               \tag{6}
\]
Against each fixed compact smooth test the right side is bounded
uniformly for \(R\ge1\). Formula (4) also gives
\[
 \langle G_k[U](R\,\cdot),\phi\rangle
   =-R^{-1}\sum_{i,j}\int U_i(Rz)U_j(Rz)\,
                                  T_{ij}\partial_k\phi(z)\,dz,
                                                               \tag{7}
\]
which is \(O_\phi(R^{-1})\). Hence \(H(R\,\cdot)\) is bounded on each
fixed test uniformly in \(R\).

If a component of \(H\) had positive highest degree \(m\), choose a
compact smooth test with nonzero pairing with its nonzero homogeneous
degree-\(m\) part. Its pairing with \(H(R\,\cdot)\) would be a polynomial
in \(R\) with a nonzero degree-\(m\) coefficient, contradicting that
bound. Thus \(H=g\) is a constant vector.
This step uses no Hb and does not presume growth of \(P\) itself.

## 2. Every bounded dilation limit is the same constant

For any sequence \(R_n\to\infty\), boundedness and weak-star compactness
give a subsequence \(U_{R_n}\) converging weak star in \(L^\infty\) to
some bounded \(v\). Sequential compactness is available because
\(L^1(\mathbb R^3)\) is separable. Using (6), (7), and
\(\nabla P=G[U]+g\), passage to distributions gives
\[
 Mv+(Az\cdot\nabla)v+g=0.                                  \tag{8}
\]
The quadratic term vanishes by its explicit \(R_n^{-1}\) factor;
no weak convergence of the product is assumed.

The matrix \(M\) is invertible because \(1-c>0\). Put \(b=-M^{-1}g\).
Then \(w=v-b\in L^\infty\) solves
\[
 (Az\cdot\nabla)w=-Mw.                                    \tag{9}
\]
For completeness, the bounded distributional solution of (9) is zero.
For real \(t\), its explicit action on a smooth compactly supported
vector test is
\[
 \langle e^{tM}w(e^{tA}\,\cdot),\phi\rangle
 =e^{-3ct}\langle w,e^{tM^T}\phi(e^{-tA}\,\cdot)\rangle.
\]
Differentiate this expression on the transformed test functions. Equation (9) makes that derivative zero. Therefore
\[
 w(e^{tA}z)=e^{-tM}w(z)\quad\hbox{in distributions and almost everywhere}
                                                               \tag{10}
\]
for each fixed \(t\). The invertible linear change \(z\mapsto e^{tA}z\)
preserves the essential-supremum norm. Since \(J\) is skew,
\(e^{-tM}=e^{-(1-c)t}e^{-\omega tJ}\), so (10) implies
\[
 \|w\|_\infty=e^{-(1-c)t}\|w\|_\infty .
\]
Take any \(t>0\). Boundedness and \(1-c>0\) force \(\|w\|_\infty=0\).

Every subsequential weak-star limit is therefore \(b\). Compactness
then gives the full convergence (2): any scalar test whose pairing
failed to converge would give a contradicting subsequence and limit.
Its vector \(b\) is unique, and \(g=-Mb\) proves (3).

## 3. Exact centering and the energy consequences

Because \(Az_0=-b\), the original carrier at \(y+z_0\) is
\[
 A(y+z_0)+U(y+z_0)=Ay+W(y).
 \]
The original equation at this point reads
\[
 MW+(Ay+W)\cdot\nabla W+\nabla P(y+z_0)+Mb=0.
\]
This is precisely the equation for \((W,\widetilde P)\).
Divergence and C1 regularity are unchanged.

To check Hb, test \(U(Rz+z_0)\) against an L1 function \(\phi(z)\)
and change variables \(x=z+z_0/R\). The resulting test
\(\phi(x-z_0/R)\) converges to \(\phi\) in L1.
The common L-infinity bound and (2) imply that the pairing tends to
\(b\int\phi\). Subtracting \(b\) proves \(W(R\,\cdot)\to0\).

All hypotheses of the established A031/A052 energy framework now
hold for \(W\). The stated conclusions follow at their exact parameter
ranges. In the constant case (1) gives
\(P(y)=-(Mb)\cdot y+\text{constant}\).
If the original \(U\) decays, (2) gives \(b=0\), so the construction
adds nothing to the original target theorem.

## Dependencies and verification

Dependencies: the canonical-gradient construction and tempered-harmonic
argument in A031;
the already audited bounded-Hb energy theorem,
including its separately proved critical tail; weak-star compactness; and differentiation of a
distribution under a smooth linear flow, explicitly used above.
There is no numerical or formal verification.

The extension removes an assumed Hb by a unique
constant background and an exact spatial shift. The review checked the uniform dilation bound in (6), uniqueness for
bounded weak solutions of (9), and the signs of \(z_0\) and the pressure
correction.
The constants may depend on this normalization. No pointwise limiting
velocity or new target-range nonexistence is claimed.


The configured-model reviewer reconstructed the argument before reading the
literature review and found no necessary correction. The actual configured
model reported by that agent is the primary model; this is a
configuration record, not independent provider attestation. Its four precision
items have been incorporated: tempered harmonicity on Schwartz tests, the
explicit weak transport identity, constant-case pressure, and normalization
dependence of constants. The auditor rechecked those items and reread the
complete bounded-Hb energy corollaries. Immutable reviews and hashes are in
in the team records. The constants in the relative energy law may depend on the
profile, c, omega, b and z_0. No computation or remote client was used.

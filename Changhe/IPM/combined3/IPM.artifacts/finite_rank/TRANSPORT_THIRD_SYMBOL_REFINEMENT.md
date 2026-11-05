# Improved third Taylor constant for the fractional transport symbol

Status: proved universal symbol estimate, independently checked by the operator-theory agent. Candidate-specific moments and the remaining energy join are separate inputs.

Let \(q=2+\delta\), \(0<\delta<1\), and \(m(\xi)=(1+|\xi|^2)^{q/2}=J(\xi)^q\). For a unit direction \(e\), set \(v=\xi/J(\xi)\), \(t=v\cdot e\). Direct differentiation gives
\[
 D^3m(\xi)[e,e,\cdot]
 =q\delta J(\xi)^{\delta-1}
 \{2te+[1+(\delta-2)t^2]v\}.
\]
Since \(|v|\le1\), the squared vector in braces is at most
\[
 1+(4+2\delta)t^2+(\delta^2-4)t^4
 \le\frac4{2-\delta}.
\]
The final quadratic in \(t^2\) is concave and attains its maximum at \(t^2=1/(2-\delta)\). Thus
\[
 \boxed{\|D^3m(\xi)[e,e,\cdot]\|
 \le\frac{2q\delta}{\sqrt{2-\delta}}J(\xi)^{\delta-1}
 \le\frac{2q\delta}{\sqrt{2-\delta}}.}
\]
The same bound controls the repeated scalar direction \(D^3m[e,e,e]\). These two forms are exactly those required for the third Taylor remainder and for its output-frequency derivative, respectively; a bound for arbitrary unrelated triples is not being substituted.

At \(q=21/10,\delta=1/10\), the constant is \( (21/50)/\sqrt{19/10}\), less than0.305, replacing the coarser valid constant \(q\delta(5-\delta)=1.029\).
If \(\mathcal R_{3,u}\nabla g\) is the transport symbol remainder after subtracting the first two coefficient-frequency Taylor terms, the same weighted Young calculation as in the source note yields
\[
 \|W\mathcal R_{3,u}\nabla g\|_2
 \le\frac{q\delta}{3\sqrt{2-\delta}}
 [M_3(u)+2M_3(xu)+6M_2(u)]\|\nabla g\|_2.
\]
The factor6 in the final moment comes from differentiating the remainder with respect to the output frequency: its bound is one half of the third derivative constant times the squared coefficient frequency, followed by the weight factor2.

All three moments are bounded by the actual density derivative certificate:
\[
 M_2(u)\le\tfrac12\sqrt{D_1D_3},\quad
 M_3(u)\le\tfrac12\sqrt{D_2D_4},
\]
\[
 M_3(xu)\le\tfrac12
 \sqrt{[X_2+(\sqrt2+1)D_1]\,[X_4+(\sqrt2+1)D_3]}.
\]
Here \(D_j=\||D|^jb\|_2\), \(X_j=\||D|^j(xb)\|_2\), \(b=\nabla\rho\). The last estimate follows from the joint velocity multiplier \(m_U\), for which \(|m_U|\le1\) and \(|\xi||\nabla_\xi m_U|_F=1\), and
\[
 |\xi|\,|\nabla\widehat\rho|
 \le|\nabla\widehat b|+\sqrt2|\widehat\rho|.
\]
Therefore \(\||D|^k(xu)\|_2\le X_{k-1}+(\sqrt2+1)D_{k-2}\), \(k=3,5\). These homogeneous seminorms are finite for Candidate013; its exact far decay justifies cutoff passage.

More explicitly, its velocity obeys \(|D^j u|\le C_j(1+r)^{1-\gamma-j}\), where \(\gamma=1-1/c>0\). For a fixed smooth radial cutoff \(\vartheta\), equal to one on the unit disk and zero outside the disk of radius two, set \(u_N=\vartheta(r/N)u\). Product differentiation and integration give
\[
 \|D^j(u_N-u)\|_2=O(N^{2-\gamma-j}),\quad j\ge2,
\]
\[
 \|D^j[x(u_N-u)]\|_2=O(N^{3-\gamma-j}),\quad j\ge3,
\]
and \(\sup W|D^2(u_N-u)|=O(N^{-\gamma})\). Thus the required moments \(M_2(u)\), \(M_3(u)\), and \(M_3(xu)\) converge by the integer-seminorm inequality in the source-commutator note. The compact-coefficient Fourier Taylor remainder estimates therefore pass in operator norm to the actual growing velocity. The polynomial ambiguity of its homogeneous Fourier transform is annihilated by the third-order Taylor remainder; no \(M_0(u)\) or \(M_0(xu)\) assumption is used.

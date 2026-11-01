# Joint density and stream bounds control the logarithmic potential

Status: CONFIRMED after the theory part's independent adversarial review at 2026-10-31T03:56Z and verifier closure V053. This fills the potential-reconstruction step of the joint plain-norm convergence criterion. It does not prove the hypothesized geometric bounds for the stationary recursion.

## Statement

Let delta=a/b in (0,1) be reduced, c=1/(1-delta), and let n_r=2b/gcd(a,2). Thus delta n_r>=2. Let a formal stationary S1 expansion with finite leading Fourier support be constructed by the polynomial-log recurrence of topic10, with any fixed choices of resonant stream constants. Write t=log r and

\[
 \rho_n=r^{1-n\delta}F_n(t,\theta),\quad
 \psi_n=r^{2-n\delta}G_n(t,\theta),\quad
 \chi_n=r^{4-n\delta}C_n(t,\theta).
\]

Assume the density and stream degrees obey the bounds of topic17, in particular deg_t F_n, deg_t G_n<=n/n_r, and their angular frequencies are at most Bn-1 and Bn, respectively. Here B=L+1 for the largest leading sine frequency L. For a polynomial H=sum_k t^k H_k, put

\[
 \lVert H\rVert_* =\sum_k\lVert H_k\rVert_{\ell^1},\qquad
 M_n=\lVert F_n\rVert_*,\quad N_n=\lVert G_n\rVert_*.
\]

The angular norm is the sum of absolute real sine or cosine amplitudes. It is the ordinary complex Fourier Wiener norm for these parity classes.

For every order with X=n delta>=20, one can choose the potential C_n producing both F_n and G_n so that its log degree is at most n/n_r, its largest angular frequency is at most Bn, and

\[
 \boxed{\lVert C_n\rVert_*\le
 \frac{432}{(n\delta)^2}
 \left[M_n+n\left(B+\frac32\delta\right)N_n\right].}
 \tag{1}
\]

Consequently, if M_n,N_n<=C A^n for all n, then the density, stream, potential and every appropriately weighted Cartesian derivative converge absolutely and uniformly for sufficiently large r. For example, any R>e satisfying

\[
 A R^{-\delta}(\log R)^{2/n_r}<1
 \tag{2}
\]

suffices. The resulting sum satisfies the original potential identities and the stationary equation on r>R. The finitely many potential orders below X=20 may contain additional logarithms, including a squared logarithm at potential degree zero; they do not affect this convergence statement.

## 1. Recover the first y derivative without a small divisor

Fix an order and suppress its index. Put q=4-X, P=q-2 and Y=partial_y chi, so Y has radial degree q-1. A formal polynomial-log potential exists by topic10. It satisfies

\[
 Y_x=\psi,\qquad -\Delta Y=\rho.
\]

For the radial Euler operator E=x partial_x+y partial_y, the exact identity

\[
 E(E-1)Y=x^2Y_{xx}+2xyY_{xy}+y^2Y_{yy}
 =(x^2-y^2)\psi_x+2xy\psi_y-y^2\rho
\]

holds. Write Y=r^{q-1}V(t,theta) and D=partial_t. Substituting the Cartesian derivatives of psi and simplifying the angular factors gives

\[
 (q-1+D)(q-2+D)V
 =\cos\theta(P+D)G+\sin\theta\,\partial_\theta G
   -\sin^2\theta F.
 \tag{3}
\]

This identity can also be checked directly from the potential. Both scalar factors on the left are far from zero at large order. If K=max(deg_t F,deg_t G), then K<=n/n_r<=X/2, and D has norm at most K in the plain polynomial norm. For X>=20,

\[
 |q-1|-K\ge X/2-3\ge X/4,\qquad
 |q-2|-K\ge X/2-2\ge X/4.
\]

The finite Neumann inverses of these factors therefore have product norm at most 16/X^2. The angular factors cos(theta), sin(theta) and sin(theta)^2 have Wiener norm one. The angular derivative of G has norm at most Bn N_n, and |P|+K<=3X/2. Thus

\[
 \lVert V\rVert_*
 \le\frac{16}{X^2}
 \left[M_n+n\left(B+\frac32\delta\right)N_n\right].
 \tag{4}
\]

The inverse preserves log degree. The right side of (3) has angular frequency at most Bn+1, so V has the same bound.

## 2. Invert a y derivative in a complex half-plane

We need an inverse of

\[
 \partial_y(r^q C)=r^{q-1}
 [q\sin\theta C+\cos\theta\,\partial_\theta C]
\]

that is analytic in q and uniformly bounded away from the nonnegative exponents. Denote this inverse by T(q). For a sine polynomial v=sum_{m>=0}v_m sin((2m+1)theta), seek C=sum_{m>=0}c_m cos(2m theta). Set x=-q/2. The equations for -v are

\[
 -v_0=2x c_0+(1-x)c_1,\qquad
 -v_m=(m+x)c_m+(m+1-x)c_{m+1}\quad(m>=1).
 \tag{5}
\]

If Re q<=-1, then Re x>=1/2. Every diagonal denominator is nonzero. Also

\[
 |m+1-x|\le|m+x|,\qquad |1-x|\le|x|.
\]

Downward substitution yields

\[
 |c_m|\le\sum_{k\ge m}\frac{|v_k|}{k+\operatorname{Re}x}\quad(m>=1),
\]

and hence sum_{m>=1}|c_m|<=sum_{k>=1}|v_k|. Separately,

\[
 |c_0|\le\frac{|v_0|}{2|x|}+\frac12|c_1|
 \le |v_0|+\frac13\sum_{k\ge1}|v_k|.
\]

In particular the operator bound ||T(q)||<=3 holds uniformly in Re q<=-1 and in every finite angular cutoff. The matrix entries are rational functions of q, analytic throughout this half-plane. The inverse lowers the largest angular frequency by one.

Return to the real q=4-X. On the complex disk centered at q with radius

\[
 s=\frac34(X-5)
\]

we still have Re q<=-1. Expand T(q+z)=sum_{h>=0}T_h z^h. Cauchy's coefficient estimate in the finite-dimensional operator norm gives ||T_h||<=3s^{-h}. For X>=20,

\[
 \frac K s\le\frac{X/2}{3(X-5)/4}\le\frac89.
\]

Define

\[
 C=T(q+D)V=\sum_{h=0}^K T_h D^hV.
\]

Its norm is at most 3 sum_{h=0}^K(K/s)^h ||V||_*<=27||V||_*. Since the formal identity for the y-derivative matrix times T(q+z) is the identity, substituting the nilpotent D proves partial_y(r^q C)=r^{q-1}V exactly. Its log degree is at most K, and its angular frequency at most Bn.

The V in (3) equals the y derivative of any potential supplied by topic10, because the two scalar factors in (3) are invertible on polynomials. Its x derivative is therefore the prescribed psi, and its negative Laplacian is the prescribed rho. The newly constructed C produces the same pair. Combining the factor 27 with (4) gives (1). No inversion near a Laplacian harmonic exponent was used in this bound.

## 3. Convergence of the potential and derivatives

Under the hypotheses M_n,N_n<=C A^n, (1) gives ||C_n||_*<=C' A^n for all sufficiently large n. Enlarge C' to cover the finite remaining orders using the formal potential construction. Their degrees may be larger than n/n_r, but this concerns only a finite set.

At large orders every log degree is at most n/n_r. For n>=2 and t=log r>=1,

\[
 t^{n/n_r}\le t^{2(n-1)/n_r}.
\]

After factoring out r^gamma for density, r^(gamma+1) for stream, and r^(gamma+3) for potential, the large-order terms are therefore bounded by a constant times

\[
 A\,[A r^{-\delta}(\log r)^{2/n_r}]^{n-1}.
\]

Since delta n_r>=2, the bracket is nonincreasing for r>=e. Condition (2) gives a uniformly summable geometric majorant on r>=R.

Each fixed Cartesian derivative introduces only a polynomial factor in n into the corresponding weighted bound: radial differentiation applies the radial exponent plus D, angular differentiation costs at most the angular bandwidth, and the Cartesian trigonometric factors have bounded Wiener norm. The log degree does not increase. A geometric series with any fixed polynomial factor is summable. All weighted derivative series therefore converge uniformly and absolutely. Each of the finitely many exceptional early terms is smooth on r>=R and has finite weighted supremum.

The original potential identities pass to the limit after two or three derivatives. Products in the stationary equation converge absolutely, so the double series can be regrouped by total radial order; its coefficients vanish by the formal recurrence. This proves the conditional exterior theorem.

## Dependencies and limits

This proof uses formal polynomial-log solvability (topic10), the rational degree bounds (topic17), finite Fourier support, elementary Cartesian differentiation, and Cauchy's estimate for a finite matrix analytic in one scalar variable. It does not establish M_n<=C A^n or N_n<=C A^n. Topic28 explains why the density bound alone is insufficient for the stream inverse. The present theorem completes the implication once both bounds are known.

Verification: 32 seeded exact rational polynomial-log potentials were differentiated in Cartesian Laurent form. The Euler identity, reconstruction of the first derivative, recovery of the complete potential, and displayed norm bound all passed. The cases include negative integer resonant potential degrees and noninteger degrees at five rational delta values. Actual check time was 0.10621928283944726 seconds; see verification/cartesian_checks.json. These finite identities are separate from the all-order estimate.

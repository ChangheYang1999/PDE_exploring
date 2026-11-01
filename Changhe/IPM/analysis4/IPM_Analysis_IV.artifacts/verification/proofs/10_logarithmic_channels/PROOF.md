# Formal logarithmic channels at rational resonances

## Statement and scope

Fix c>1, delta=1-1/c, p_n=1-n delta, P_n=p_n+1 and s_n=p_n+3. Let f_1 be a real finite odd sine polynomial. At every order, the stationary equation has a formal expansion with coefficients polynomial in t=log r,

\[
\rho=\sum_{n\ge1}r^{p_n}f_n(t,\theta),\qquad
\psi=\sum_{n\ge1}r^{P_n}g_n(t,\theta),\qquad
\chi=\sum_{n\ge1}r^{s_n}C_n(t,\theta).
\]

The angular coefficients are finite trigonometric polynomials with the same parities as in the pure expansion. The density coefficient f_n is determined uniquely by the earlier coefficients. At an exact stream resonance, one may choose a constant coefficient of the resonant harmonic stream; fixing these constants fixes the subsequent density and stream coefficients. Every resulting pair (rho,psi) can be produced by such a logarithmic potential chi, up to full-field gauges.

This is a theorem about formal coefficients at each finite order. It proves neither convergence of the generalized expansion nor a positive convergence radius at rational delta. A failed compatibility condition obstructs the pure-power ansatz, but does not obstruct this larger formal ansatz.

## Operators with polynomial logarithms

Write T=partial_t and D=partial_theta. On a coefficient attached to radial degree s, the radial Euler operator r partial_r acts as s+T. Thus

\[
\Delta(r^s C)=r^{s-2}[(s+T)^2+D^2]C.
\]

Set H=[(s+T)^2+D^2]C. Direct Cartesian differentiation gives

\[
f=-[\sin\theta(s-2+T)+\cos\theta D]H,
\tag{1}
\]

\[
g=[\cos\theta(s-1+T)-\sin\theta D]
  [\sin\theta(s+T)+\cos\theta D]C.
\tag{2}
\]

These are the original identities rho=-partial_y Delta chi and psi=chi_xy, with no independent choice of velocity. Commuting Cartesian derivatives also gives

\[
-[D^2+(P_n+T)^2]g_n
=[\cos\theta(p_n+T)-\sin\theta D]f_n.
\tag{3}
\]

If a_j(t) is the amplitude of sin((2j+1)theta) in f_n and h_j(t) the amplitude of sin(2j theta) on the right of (3), then

\[
h_j=\tfrac12[(p_n-2j+1+T)a_{j-1}
             +(p_n+2j+1+T)a_j].
\tag{4}
\]

The stream amplitude b_j(t) solves

\[
[4j^2-P_n^2-2P_nT-T^2]b_j=h_j.
\tag{5}
\]

## Solving the stream equation at every order

On polynomials, T is nilpotent. If lambda=4j^2-P_n^2 is nonzero, the inverse is the terminating sum

\[
b_j=\lambda^{-1}\sum_{h\ge0}
 \left(\frac{2P_nT+T^2}{\lambda}\right)^h h_j.
\tag{6}
\]

The sum ends when all derivatives vanish. Its degree is no greater than deg h_j. If lambda=0, the range 0<delta<1 implies P_n=-2j, and (5) becomes

\[
T(4j-T)b_j=h_j.
\]

Choose an arbitrary real number beta_j and put

\[
b_j(t)=\beta_j+\int_0^t
 \frac1{4j}\sum_{h\ge0}\left(\frac{T}{4j}\right)^h h_j(v)\,dv.
\tag{7}
\]

This is a polynomial solution. Its degree is one more than deg h_j when h_j is nonzero. All polynomial solutions differ by a constant: if T(4j-T)b=0, the polynomial (4j-T)b is constant, forcing b constant. The constant beta_j is the free exterior harmonic stream amplitude.

For constant nonzero h_j, formula (7) has the required leading term h_j t/(4j). This confirms both the sign and the normalization of the resonant logarithm. If h_j=0, a pure harmonic stream is possible; a logarithm is not forced at that order.

## Modified stationary recurrence

The polar radial and tangential velocity coefficients of r^{P_i}g_i are -Dg_i and (P_i+T)g_i. Therefore define

\[
S_n=\sum_{i+j=n}
\left[-(Dg_i)(p_j+T)f_j+((P_i+T)g_i)Df_j\right].
\tag{8}
\]

At order one, the stationary equation gives cTf_1=0, so the prescribed leading coefficient is independent of t. At every n>=2 the equation is

\[
[(n-1)(c-1)-cT]f_n=S_n.
\tag{9}
\]

Its unique polynomial solution is

\[
f_n=\frac1{(n-1)(c-1)}
 \sum_{h\ge0}\left(\frac{cT}{(n-1)(c-1)}\right)^h S_n.
\tag{10}
\]

Again the sum terminates. Equations (4), (6), (7), (8) and (10) construct every order. Fixing the beta_j removes the only stream choices at resonance. These formulas reduce exactly to the pure recurrence when all logarithmic derivatives vanish and all inverses are nonresonant.

If f_1 has highest frequency L and B=L+1, the support bound remains deg_theta f_n<=Bn-1 and deg_theta g_n<=Bn. The added harmonic at a resonant order has frequency 2j=n delta-2<Bn, so it also respects the bound. Logarithmic degree is finite: a simple induction gives deg_t f_n<=n-2 for n>=2 and deg_t g_n<=n-1, with degree zero at n=1. Differentiation in t does not raise degree, multiplication adds degrees, and the stream inverse raises degree by at most one.

## A logarithmic potential exists for every constructed pair

For fixed angular cutoff K, let A(s) be the finite matrix sending the cosine amplitudes of r^s C, at frequencies 0,2,...,2K, to the sine amplitudes of -partial_y Delta(r^s C), at frequencies 1,3,...,2K+1. Its entries are the degree-three polynomials given in `../01_recurrence/PROOF.md`. The determinant is not identically zero, so A(s) has a meromorphic rational inverse.

For a target radial degree s_0<4, expand this inverse in a Laurent series

\[
A(s_0+z)^{-1}=\sum_{h=-J}^{\infty}B_h z^h.
\]

For a polynomial vector f(t), interpret z^h as T^h when h>=0 and as h-fold integration from zero when h is negative. More precisely, if Iq(t)=integral_0^t q(v)dv, put

\[
C(t)=\sum_{h=0}^{\deg f}B_hT^h f(t)
     +\sum_{j=1}^J B_{-j}I^j f(t).
\tag{11}
\]

This is a finite polynomial. Since TI is the identity on polynomials, multiplication on the left by the polynomial matrix A(s_0+T) reproduces the Laurent identity A(s_0+z)A(s_0+z)^{-1}=Id. All negative powers cancel, and hence A(s_0+T)C=f. This proves the density identity (1) for a logarithmic potential, including singular degrees.

The pole order is at most two for s_0<4. One can see this without a determinant calculation. First invert the density-to-Laplacian triangular map, whose descending diagonal entries are m+(2-s)/2 for m>=1 and 2-s for m=0. Only the last can vanish in s<4, at s=2, and it gives at most a simple pole. Then divide each cosine amplitude by s^2-4m^2. These factors have simple zeros at nonzero even s, and a double zero for m=0,s=0. At s=2 the possible pole from the first step affects only m=0, while the vanishing Laplacian factor affects m=1. They do not multiply. Thus J<=1 except possibly J=2 at s_0=0.

Let g^C be the stream generated from this C by (2). Both g^C and the prescribed g solve (3), so their difference is a polynomial solution of the homogeneous stream equation. At a nonresonant order the difference vanishes. At resonance P=-2j it is a constant multiple of sin(2j theta). This discrepancy can always be corrected without changing density:

- For j=1, the potential log r is harmonic and has stream -r^(-2)sin(2theta).
- For j>=2, the harmonic potential r^(-2j+2)cos((2j-2)theta) has stream (2j-2)(2j-1)r^(-2j)sin(2jtheta).

Adding the appropriate multiple makes g^C=g. The velocity then agrees with the same original potential. This completes the formal construction.

## Pure-potential compatibility at the exceptional degrees

For completeness, finite angular polynomials admit the following precise classification.

At p=-1 (s=2), a pure potential exists exactly when the sin(theta) amplitude a_0 is zero and f(pi/2)=0. Necessity follows from H=(D^2+4)C: its cos(2theta) amplitude is zero, f=-cos(theta)H', and hence a_0=0 and f(pi/2)=0. For sufficiency, descending substitution in a_m=m d_m+(m+1)d_(m+1) gives a polynomial H whenever f(pi/2)=0; its cos(2theta) amplitude is a_0 and so vanishes. The inverse of D^2+4 then produces C. The free potential modes 1 and cos(2theta) are full-field gauges at this degree.

At p=-3 (s=0), a pure potential exists exactly when a_0=0. Its stream harmonic at frequency two is then fixed by the pure-potential choice; a different harmonic amplitude requires log r.

At p=-2j-1 with j>=2, a pure potential exists exactly when a_(j-1)=0, which is the same compatibility condition as the stream equation. Its density-free harmonic potential can realize any free resonant stream amplitude. Other pure potential degrees with p<1 are nonexceptional.

These conditions refer to finite angular polynomials. The general logarithmic construction (11) removes these finite-order solvability obstructions but makes no convergence assertion.

## Dependencies and remaining question

The proof uses finite trigonometric identities, nilpotence of differentiation on polynomials, and finite-dimensional rational matrix inversion. The only infinite object is a formal sequence of separately constructed finite coefficients. A convergence estimate uniform in both radial order and logarithmic degree is still needed before this generalized series can be claimed to define an exterior solution at a resonant rational parameter.

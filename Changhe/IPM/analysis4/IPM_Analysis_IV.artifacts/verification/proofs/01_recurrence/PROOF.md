# Potential, Poisson inverse and stationary recursion

## Statement and scope

Let c > 1, gamma = 1/c, delta = 1 - gamma, and p_n = 1 - n delta. All functions below are real and 2 pi periodic in theta. Density coefficients are even under x reflection and odd under y reflection, so they have odd sine frequencies. Potential coefficients are even under both reflections, so they have even cosine frequencies. Stream coefficients have even sine frequencies.

For a finite set of nonexceptional orders, the potential formulation

\[
\rho=-\partial_y\Delta\chi,\quad
u=(-\chi_{xyy},\chi_{xxy})
\]

implies exactly the Poisson formula and nonlinear recursion in the prompt. The map from density to a pure homogeneous potential is uniquely invertible on the corresponding finite cosine/sine polynomial spaces if p is not an odd integer and p < 1. The exceptional exponent p = -1 precedes the first stream Poisson resonance p = -3. Thus the equivalence with a pure potential series requires an exception clause. This is a formal coefficient statement, not a convergence theorem.

## One homogeneous potential

Write chi = r^s C(theta), with s = p+3, and D = d/dtheta. Polar differentiation gives

\[
\partial_x=\cos\theta\,\partial_r-r^{-1}\sin\theta D,
\qquad
\partial_y=\sin\theta\,\partial_r+r^{-1}\cos\theta D.
\]

Set H = (D^2+s^2)C and J = s sin(theta) C + cos(theta) C'. Then

\[
f=-[(s-2)\sin\theta H+\cos\theta H'],
\qquad
g=(s-1)\cos\theta J-\sin\theta J'.
\]

Indeed Delta chi = r^(s-2) H, and differentiating once in y gives the density formula. Differentiating chi once in y gives r^(s-1) J, then once in x gives psi = chi_xy = r^(s-2) g. In particular the velocity in the question is exactly (-psi_y, psi_x).

For a single C(theta) = A_l cos(l theta), with l nonnegative and even, these formulas become

\[
f= -\frac{A_l(s^2-l^2)(s-2-l)}2\sin((l+1)\theta)
 +\frac{A_l(s^2-l^2)(s-2+l)}2\sin((l-1)\theta),
\]

\[
g=\frac{A_l(s-l)(s-l-2)}4\sin((l+2)\theta)
 -\frac{A_l(s+l)(s+l-2)}4\sin((l-2)\theta).
\]

Negative sine frequencies carry their usual minus sign; zero sine frequencies vanish. For l = 0 both displayed contributions to each relevant frequency must be combined. In particular the density coefficient is -A_0 s^2(s-2) sin(theta).

If the target density has frequencies at most 2K+1, choose potential frequencies 0,2,...,2K. Its coefficient matrix is bidiagonal when ordered by frequency. The top coefficient of a nonzero l column is

\[
-\tfrac12(s^2-l^2)(s-2-l),
\]

and the l=0 diagonal is -s^2(s-2). These are all nonzero for s < 4 and s not an even integer. Back substitution proves existence and uniqueness in these finite polynomial spaces. Differentiation of the resulting potential gives a stream coefficient satisfying the Poisson equation below; wherever that equation has no even sine kernel, its solution is unique.

## Poisson inverse and its exceptional values

Commuting Cartesian derivatives gives

\[
-\Delta\psi=-\partial_{xy}\Delta\chi=\partial_x\rho.
\]

Therefore, for rho = r^p f and psi = r^(p+1) g,

\[
-(D^2+(p+1)^2)g=p\cos\theta f-\sin\theta f'.
\]

Let a_k denote the coefficient of sin((2k+1)theta), k >= 0, and b_j the coefficient of sin(2j theta), j >= 1. Using the sine product identities, the forcing coefficient at 2j is

\[
h_j=\tfrac12[(p-2j+1)a_{j-1}+(p+2j+1)a_j].
\]

For nonzero d_j = 4j^2-(p+1)^2,

\[
b_j=\frac{h_j}{d_j}
=-\frac{a_{j-1}}{2(2j+p+1)}+
\frac{a_j}{2(2j-p-1)}.
\]

The second expression is useful but cannot be used at a zero denominator without stating a choice of homogeneous solution. With p=p_n<1 and delta>0, the only resonances at n>=1 are

\[
n\delta=2(j+1),\quad p=-2j-1,\quad j\ge1.
\]

At this exponent the forcing reduces to h_j = -2j a_(j-1). A periodic pure-power stream exists if and only if a_(j-1)=0. If this compatibility holds, b_j is arbitrary, because r^(-2j) sin(2j theta) is harmonic. If it fails, no pure-power stream solves the Poisson equation.

For a forcing h_j r^(-2j-2) sin(2j theta), the logarithmic stream

\[
\psi_{\log}=\frac{h_j}{4j}r^{-2j}\log r\sin(2j\theta)
\]

has -Delta psi_log equal to that forcing. This follows from Delta(r^a log(r) sin(k theta)) = 2a r^(a-2) sin(k theta) when a^2=k^2. Logarithmic streams generally produce logarithms in subsequent nonlinear orders, so the pure recursion then needs extension.

## Stationary coefficient equation

The polar velocity of psi_i = r^(p_i+1)g_i is

\[
u_{i,r}=-r^{p_i}g_i',\qquad
u_{i,\theta}=(p_i+1)r^{p_i}g_i.
\]

Consequently

\[
u_i\cdot\nabla(r^{p_j}f_j)
=r^{p_i+p_j-1}[-p_jg_i'f_j+(p_i+1)g_if_j'].
\]

Since p_i+p_j-1 = p_(i+j), all quadratic terms of order n come precisely from i+j=n. Also

\[
cp_n-1=-(n-1)(c-1).
\]

The order-one linear coefficient vanishes, leaving f_1 free. For n>=2, cancellation of the stationary residual is therefore equivalent to

\[
f_n=\frac1{(n-1)(c-1)}\sum_{i+j=n}
[-p_jg_i'f_j+(p_i+1)g_if_j'].
\]

There is no factor 1/2 in this ordered convolution: both (i,j) and (j,i) occur if i differs from j. The i=j term occurs once. This derivation uses the velocity produced by the same potential and fixes the sign independently of a stored recurrence.

If f_1 has no frequency above L, where L is odd, induction gives

\[
\deg f_n\le n(L+1)-1,\quad
\deg g_n\le n(L+1),\quad
\deg C_n\le n(L+1)-2
\]

whenever the nonresonant pure polynomial construction is used. The first bound follows because a stream frequency at order i is at most i(L+1), and a density frequency at order j is at most j(L+1)-1. These are upper bounds, not assertions that each highest coefficient is nonzero.

## The missing potential exception

At p=-1, s=2. The pure potential columns 1 and cos(2 theta) both generate zero density and zero velocity. Thus the pure homogeneous potential map is singular even though the even sine Poisson inverse has no resonance. The missing directions are supplied by logarithmic potentials:

\[
\chi=r^2\log r:
\quad\rho=-4r^{-1}\sin\theta,\quad\psi=\sin(2\theta),
\]

\[
\chi=r^2\log r\cos(2\theta):
\quad\rho=4r^{-1}(\sin\theta+\sin(3\theta)),\quad
\psi=-\tfrac12\sin(4\theta).
\]

The first density is impossible for every smooth pure degree-two potential, not merely a finite polynomial: its coefficient would equal -cos(theta) H'(theta), which vanishes at pi/2.

These identities follow by differentiating the homogeneous formulas with respect to s at s=2, since d_s r^s = r^s log r. The undifferentiated columns vanish in both fields, so the resulting fields have no log terms.

At p=-3, s=0, the constant potential column is also zero. A compatible density has zero sin(theta) coefficient, and pure potentials can represent the remaining finite frequencies. A freely prescribed harmonic stream at frequency 2 may require the additional potential log r, because

\[
\Delta\log r=0,\quad\partial_{xy}\log r=-r^{-2}\sin(2\theta).
\]

For p=-2j-1 with j>=2, the harmonic potential r^(-2j+2) cos((2j-2)theta) generates zero density and a nonzero resonant stream. Such a density-free direction is not a gauge of the full fields. Calling every element of the density kernel an irrelevant gauge would be incorrect.

## Amplitude and convergence scope

Whenever the deterministic recursion is defined with zero free harmonic-stream coefficients, or with choices homogeneous of degree n in f_1 at order n, replacing f_1 by a f_1 replaces (f_n,g_n) by (a^n f_n,a^n g_n), by induction and bilinearity. Thus the weighted generating series becomes a F(a z), where F(z)=sum_(n>=1) f_n z^(n-1). Reducing the amplitude rescales the radius in z; it cannot turn zero radius into positive radius.

The identities above do not justify termwise operations on an infinite series. A separate coefficient bound, together with derivative convergence, is needed. None is inferred from the finite computations associated with this proof.

## Dependencies and evidence

Only the displayed polar differentiation identities, finite Fourier algebra and finite-dimensional back substitution are used. The exact Cartesian-derivative implementation in `../../code` and its recorded outputs in `verification` check finite instances. They supplement the written proof rather than constitute an all-order convergence argument.

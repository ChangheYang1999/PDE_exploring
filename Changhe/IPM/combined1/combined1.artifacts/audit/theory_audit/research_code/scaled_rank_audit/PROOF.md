# Exact rank of the radius-scaled extensions

## 1. Statement

Let c=4076476460239181/2251799813685248, gamma=1/c,
delta=1-gamma, p_j=(3+gamma-j delta)/2, t=r^2/(1+r^2),
v=1/(1+r^2), and H_m=Re(x+iy)^(2m). Let V_old be the exact
1922-dimensional potential space audited in T4-195 and T4-230,
with its selected original basis recorded in data/old_basis.json.
Its functions are sums H_m(1+r^2)^(p_j-m)P_jm(t), where P_jm is a
polynomial and j belongs to{0,...,7}.

For R=25 or R=50, adjoin the252 functions

    G_jmN=H_m(1+r^2)^(p_j-m) [R^2/(R^2+r^2)]^4
                       P_N(2r^2/(R^2+r^2)-1),
    j in{1,2,3}, m in{9,...,15}, N in{0,...,11},

where P_N is the Legendre polynomial normalized by P_N(1)=1.
The augmented potential space has dimension2174. The statement is
about the exact generator functions, regardless of the fitted coefficients.
The new density frequencies lie in{17,19,...,31}, and frequency17
occurs. This confirms N4-248 for R=25; the same proof covers R=50.

## 2. Complete independence proof

For a fixed angular label m, strip off cos(2m theta). A relation in
the potential space has the form sum_j v^(-p_j)Q_j(v)=0, where each
Q_j is rational and analytic at v=0. Distinct p_j have distinct
fractional parts: (j-k)delta/2 is not an integer for j!=k. If some
Q_j is nonzero, it has a finite least Taylor exponent k_j>=0.
The real exponents k_j-p_j are therefore all distinct. Divide the
relation by its unique least power of v and let v tend to zero from
above. The corresponding nonzero Taylor coefficient cannot vanish.
Thus every Q_j is zero. Angular orthogonality separates m first,
so it remains to prove independence for one fixed(j,m).

Set a=R^2-1>0 and L=1+av. The new rational factor in this block is

    R^8 (1-v)^m v^4 P_N(2(1-v)/L-1)/L^4.

At v0=-1/a it has pole order4+N, with coefficient

    C_mN=R^8 v0^4 binom(2N,N)(1-v0)^(m+N)/a^(4+N).                (1)

Indeed the leading coefficient of P_N(x) is 2^-N binom(2N,N).
Its leading term after substitution contributes the stated coefficient;
every lower polynomial degree has a strictly smaller pole order.
All factors in(1) are nonzero. In a relation, the largest N with nonzero
coefficient therefore has a pole that no smaller N or old polynomial
term can cancel. This contradicts a zero rational function. Descending
in N removes all new terms, and the independently audited old basis
has no relation. There are3*7*12=252 new functions, proving the rank.
The negative auxiliary pole is used only in a rational identity after
branch separation; no noninteger physical prefactor is continued there.

## 3. Lowest density frequency

The Laplacian preserves the cos(2m theta) frequency and -partial_y
maps it into sin((2m-1)theta) and sin((2m+1)theta). Therefore every
new density has frequencies in the stated set. For the unit generator
j=1,m=9,N=0, its origin expansion is

    G=H_9[1+(p_1-9-4/R^2)r^2+O(r^4)].

Since Delta H_9=0, Delta(r^2 H_9)=4*19 H_9 and
-partial_y H_9=18 Im(x+iy)^17, the lowest density coefficient is

    4*19*18*(p_1-9-4/R^2) Im(x+iy)^17.                            (2)

It is nonzero for both scales. This proves that the family includes
mode17; it need not say that every fitted coefficient vector has a
nonzero total mode17. No sampled singular value enters this argument.

## 4. Extension of the audited density injectivity lemma

This paragraph is a separate extension submitted for Opus review.
The potential-to-density map chi -> -partial_y Delta chi is injective
on both augmented spaces. Here is the complete argument.

Every new generator is smooth and even in x and y. At infinity its
kth Cartesian derivatives for k<=4 are O(r^(2p_j-8-k)), since the
scale cutoff decays as r^-8, its differentiated asymptotic series
converges for large r, and P_N tends to P_N(1). The old generators
satisfy O(r^(2p_j-k)). Thus every potential has growth O(r^d) and
D^4chi=O(r^(d-4)), where d=3+gamma<4.

If -partial_y Delta chi=0, then Delta chi=f(x). For fixed x,
f''(x)=partial_x^2 Delta chi(x,y) tends to zero as |y| tends to infinity.
Hence f''=0 and evenness gives f=K constant. The function
chi-Kr^2/4 is entire harmonic with growth O(1+r^d). Its angular
Fourier coefficients solve the harmonic radial ODE. Smoothness removes
negative powers and the logarithm; the growth bound removes degrees>=4;
evenness in each coordinate leaves only degrees0and2. Consequently
chi=A+B(x^2-y^2)+Kr^2/4.

For each m, divide the angular equality by r^(2m) where r>0. The
left side is a sum of v^(m-p_j) times rational functions analytic at
v=0. The right side has only integer Laurent powers. Every p_j is
noninteger and all branch differences are noninteger. Applying the
unique least exponent argument to this equality, including the finite
integer Laurent polynomial as one additional class, forces every term
to vanish. Thus chi=0. This proves injectivity and density dimension2174,
conditional only on the already audited old potential dimension.

## 5. Verification and limits

The checker uses the Rodrigues formula to construct each Legendre
polynomial independently, forms its substituted numerator exactly,
and checks all84 coefficients(1) at each scale. It compares the scale25
coefficients with the frozen N4 result, checks all28 branch differences
and all8 nonintegrality conditions, verifies every old/new raw generator
shape in016and017, and checks(2). The old selected basis and its rank
are prior independently audited dependencies; no new rank computation
of that basis is claimed here.

The potential rank is an independent confirmation of N4-248. The
density extension in section4 awaits independent Opus acceptance.
Neither rank implies a coercivity constant, a PDE inverse, good
conditioning, a sampled Jacobian rank, or an optimizer objective floor.

# Exact dimension of the simultaneous radius 25 and 50 spaces

## Statement and definitions

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2, S=1+x^2+y^2, r=sqrt(x^2+y^2),
t=r^2/S, v=1/S and H_m=Re(x+iy)^(2m). Let V_old be the exact
1922-dimensional real potential space whose selected basis is recorded in
../optimizer_quotient_audit/source/N1_013_quot_exact.json. The independence
and description of that basis are the proved dependency
../optimizer_quotient_audit/PROOF.md. Its elements are finite sums
H_m S^(p_j-m) P_jm(t), with polynomial P_jm and j in {0,...,7}.

For both R in {25,50}, and each j in {1,2,3}, m in {9,...,15},
N in {0,...,11}, adjoin the generator

 G_RjmN = H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                              P_N(2r^2/(R^2+r^2)-1),

where P_N is the Legendre polynomial normalized by P_N(1)=1. Let V be
the real span of the old basis and these 504 generators. Then the listed
2426 potentials are linearly independent, and the linear density map

    D: V -> C-infinity(R2), D chi = -partial_y Delta chi

is injective. Hence dim V=dim D(V)=2426. Every potential is smooth and
separately even in x and y. These statements concern the specified exact
function spaces. They make no assertion about a new candidate's actual
shapes until its immutable snapshot is compared with this list. They do
not imply a condition number, optimizer minimum, inverse or existence.

## Branch separation

Angular orthogonality separates cos(2m theta). In one angular component,
a potential relation has the form sum_j v^(-p_j) Q_j(v)=0, where each
Q_j is rational and analytic at zero. Exact rational calculation for
j=0,...,7 gives p_j noninteger and p_j-p_k noninteger whenever j!=k.
If any Q_j is nonzero, it has a finite nonnegative integer order e_j
at zero with nonzero Taylor coefficient. The exponents e_j-p_j are
pairwise distinct. Divide by their unique smallest power of v and let
v tend to zero through positive values. A single nonzero coefficient
survives, a contradiction. Thus the rational functions Q_j vanish
separately. The same argument separates these eight branches from any
integer Laurent polynomial, since none of their exponents is integer.

## Independence at two distinct auxiliary poles

Fix one block (j,m). Put a_R=R^2-1 and L_R=1+a_R v. The new radial
factor, including t^m, is

 A_RmN(v)=R^8 v^4 (1-v)^m
                  P_N(2(1-v)/L_R-1)/L_R^4.

The Legendre leading coefficient 2^(-N) binom(2N,N) follows from
Rodrigues' formula. At v_R=-1/a_R the numerator of the highest pole
term is R^8 v_R^4 binom(2N,N)(1-v_R)^(m+N), which is nonzero.
The pole order is 4+N and the Laurent coefficient is

 C_RmN = R^8 v_R^4 binom(2N,N)(1-v_R)^(m+N)/a_R^(4+N).

Old polynomial terms are analytic there. The other scale R' is also
analytic there because L_R'(v_R)=1-a_R'/a_R is nonzero: the two a's
are 624 and 2499. For either fixed scale, the term with greatest N
having a nonzero coefficient in a relation has a pole uncancellable by
any lower N, old term, or other scale. Descending in N eliminates all
new coefficients at that scale, and then at the other scale. The old
basis independence eliminates the remaining old coefficients. Branch
and angular separation above justify applying this argument block by
block. There are 2*3*7*12=504 new classes, proving dimension 2426.
Only rational identities use negative auxiliary poles; no noninteger
physical prefactor is analytically continued through such a pole.

## Injectivity of the density map

Every element chi in V is smooth and separately even. Direct differentiation
of its finite generator formulas gives

    |D^k chi(X)| = O(r^(3+gamma-k)), 0<=k<=4, r->infinity.

Indeed 2p_j<=3+gamma, ordinary factors and their differentiated powers
have the stated homogeneous bounds, and each scaled rational envelope
and its derivatives are bounded by the corresponding nonpositive powers
of r. The additional fourth power in the scaled envelope only improves
the decay. In particular D^4 chi tends to zero, and chi has growth
O(1+r^d), d=3+gamma<4.

Assume D chi=0. Smoothness implies Delta chi=f(x), independent of y.
For fixed x, f''(x)=partial_xx Delta chi(x,y) tends to zero as |y| tends
to infinity by the fourth derivative bound. It is independent of y,
so f''=0. Evenness in x makes f constant, say K. The function
h=chi-Kr^2/4 is entire harmonic with growth O(1+r^d). At any fixed X,
the interior harmonic derivative estimate on B(X,L) bounds each fourth
derivative by C L^(-4) sup_B |h| = O(L^(d-4)). Taking L to infinity
shows D^4 h=0. Thus h is a polynomial of degree at most three. Separate
evenness and harmonicity imply h=A+B(x^2-y^2). Consequently

    chi=A+Kr^2/4+B(x^2-y^2).

In v coordinates the angular coefficients on the right are integer
Laurent polynomials: A+(K/4)(1-v)/v at m=0, B(1-v)/v at m=1, and
zero otherwise. The branch separation argument above, including its
integer Laurent class, forces all radial branch coefficients and all
these polynomial coefficients to vanish. Hence chi=0. Potential
independence now forces the full coefficient vector to vanish, proving
injectivity and density dimension 2426.

## Verification, dependencies and review scope

The exact checker binds the accepted old rank, both single-scale rank
records and the separately audited density injectivity theorem, including
its Opus review. It constructs the combined abstract generator list,
checks all 2426 shapes and eight branches, independently reconstructs
all 168 Laurent coefficients, and checks analyticity of each scale at
the other pole. Exact witnesses and the shape list are JSON inputs and
outputs. An actual mixed-scale snapshot must be checked separately.

The harmonic interior derivative estimate is a standard analytic lemma;
its precise use and growth argument are supplied above. The finite
checker verifies the numerical hypotheses, not that analytic lemma or
the PDE. The new two-scale theorem remains OPEN until independently
reviewed. No Lean build, numerical conditioning inference, spatial
quadrature or new assumption about the optimizer is involved.

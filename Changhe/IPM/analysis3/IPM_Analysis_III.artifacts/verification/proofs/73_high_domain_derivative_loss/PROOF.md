# The high inverse needs a graph realization

## Exact statements

Let O be a relatively compact open subset of the first quadrant away
from the axes, origin and radial spline knots. Suppose V is smooth on
a neighborhood of its closure and V(X0) is nonzero at some X0 in O.
Let s>=0 and let B be a linear operator satisfying

 ||chi B h||_H^s(R2)<=C||h||_H^s(R2)

for smooth h supported in a fixed sufficiently small ball in O, where
chi is a smooth compactly supported cutoff equal to1 on that ball.
Then V.grad+B is not a bounded operator from these H^s inputs to local
H^s output. This applies to the local transport part of the reduced
IPM operator, including its order-zero nonlocal coupling and bounded
normalization row on this support.

Consequently, a proposed isomorphism L:H->Y_H whose norms on O are
both ordinary H^s and which gives H no transport graph control is
false as a bounded-isomorphism statement. This does not refute a
bounded inverse Y_H->H^s for a suitable unbounded realization of L.

Furthermore, arbitrarily small smooth changes of a transport vector
field do not, in general, preserve its maximal graph domain, even
locally and even after imposing any fixed finite Sobolev order.

## Local oscillatory proof

Choose a unit vector xi with V(X0).xi nonzero. After shrinking O, its
absolute value is bounded below by v0>0. Choose nonzero real
eta in C_c^infinity(O), and let

 h_N=N^(-s)eta(X)exp(iN xi.X).

The Fourier shift formula gives ||h_N||_Hs bounded above and below by
positive constants independent of N. The same formula gives

 N^(-1)||V.grad h_N||_Hs -> ||(V.xi)eta||_L2>0,

up to the fixed Fourier normalization and |xi|^s=1. To prove this
limit, write the leading term as iN^(1-s)(V.xi)eta exp(iNxi.X)
and the remainder as N^(-s)(V.grad eta)exp(iNxi.X). The Fourier
integrals for the two fixed smooth compact amplitudes obey dominated
convergence after division by the appropriate power of N. The
remainder has bounded Hs norm. By hypothesis ||chi B h_N||_Hs is
bounded. Thus ||chi(V.grad+B)h_N||_Hs grows at least linearly.
For real spaces take a sine or cosine subsequence, which has the same
nonzero leading norm. Even-x, odd-y symmetrization over the four
reflected balls preserves the estimates because the balls are
disjoint and the localized original ball is unchanged.

For IPM, local order-zero control of U follows directly from its
bounded Fourier multiplier on Hs. Multiplication by the smooth
background gradient and cutoffs is bounded on Hs. Contributions from
reflected balls have smooth separated kernels on O. The strain kernel
is smooth on the support, so c[h_N] decays faster than every power of
N by integration by parts. Its fixed local coefficient contributes
no leading term. If an exact zero-strain input is desired, subtract
c[h_N] times a fixed parity-compatible smooth input of strain1.
This changes none of the estimates. Such an input exists by taking a
small support on which sin(3theta)/r^3 has one sign and reflecting it.

## Explicit failure of common graph domains

On R2 let T=partial_x-1 and T_epsilon=partial_x+epsilon partial_y-1,
where epsilon is any nonzero real number. For s>=0 choose a compactly
supported g in H^s(R) but not H^(s+1)(R), and a nonzero smooth compact
chi(x). Then h(x,y)=chi(x)g(y) belongs to Hs(R2), and

 T h=(chi'-chi)g belongs to Hs(R2).

But T_epsilon h=T h+epsilon chi g' does not belong to Hs(R2).
Indeed, the Fourier tensor-product formula and integration over a
bounded set of x frequencies where chi-hat is nonzero show that
chi g' in Hs(R2) would imply g' in Hs(R), contradicting the choice of
g. Hence the maximal Hs graph domains differ for every epsilon!=0,
although the vector fields are arbitrarily close in C1 and their
velocity derivatives agree exactly. Localizing the vector-field
perturbation to equal epsilon partial_y on the support gives the
same compactly supported counterexample.

One may choose g explicitly: a smooth cutoff times |y|^alpha, with
alpha noninteger, alpha>s-1/2 and alpha<=s+1/2. Its Fourier transform
has a nonzero leading multiple of |eta|^(-alpha-1), obtained by scaling
the cosine integral with an exponential regularizer; thus it belongs
to Hs but not H^(s+1). Alternatively the standard Fourier definition
of a strict Sobolev inclusion supplies g, followed by localization at
a point of failed H^(s+1) regularity.

## Correct formulations and nonlinear scope

Let H_reg denote the desired variable-regularity space, and Y_H the
forcing space. For each vector field or nonlinear parameter g, define

 D_g={h in H_reg:L_g h belongs to Y_H distributionally},
 ||h||_Dg=||h||_Hreg+||L_g h||_YH.

If the low realization is closed, H_reg embeds continuously in the
low distribution space, and Y_H embeds continuously in the low
forcing distribution space, then D_g is complete: a graph-norm
Cauchy sequence converges in H_reg and its images converge in Y_H;
continuity of the differential and nonlocal terms into distributions
identifies the limiting image. This is the appropriate graph space
for a bounded-isomorphism statement D_g->Y_H.

Alternatively state only the inverse estimate

 ||L_g^(-1)f||_Hreg<=K_H||f||_YH,

with the low maximal realization and its uniqueness specified. That
estimate does not assert that every H_reg input has image in Y_H.
Uniformity in g requires a separate argument. Small ||DW[g]||_infinity
alone does not invoke bounded-operator perturbation theory on a common
maximal graph domain. The two-norm iteration of proof 59 already avoids
this error by comparing smooth/high inverse outputs in the common low
forcing space, where the verified product estimate applies. Its
uniform inverse hypotheses remain hypotheses.

## Dependencies and verdict scope

The first argument uses only Fourier definitions of Sobolev norms and
smooth compact localization. The IPM application uses the explicitly
known order-zero multipliers and strain kernel of topics02 and44.
No actual high inverse is disproved. The invalid bounded same-order
forward map and the generic common-domain inference are disproved.

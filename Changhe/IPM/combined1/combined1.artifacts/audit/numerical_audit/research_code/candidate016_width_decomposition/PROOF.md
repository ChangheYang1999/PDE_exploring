# What the final candidate016 enclosure width measures

## Exact statement and hypotheses

Use the candidate, norms, whole-plane gradient duality and divergence-field
upper bound in candidate016_multimode_complete_bounds/PROOF.md. This is a
finite consequence of the accepted N4-427/428/430/431 records, without new
source integrals. Let P be 47 or 63, N=P+2, and let q_n have accepted upper
u_n. Let R_U bound the full squared norm ||rF||_2^2. For odd n from 1 to 31,
let ell_n and J_n be the selected positive strict dual and solenoidal
floors. Define

    V = R_U/N^2 + sum_(odd n<=P) (1/n^2-1/N^2) u_n,
    L = sum_(odd n<=31) ell_n^2,
    U = V - sum_(odd n<=31) J_n,
    D = sum_(odd n<=31) (u_n/n^2-J_n-ell_n^2),
    T = (R_U-sum_(odd n<=31) u_n)/N^2
        + sum_(33<=odd n<=P) (1/n^2-1/N^2) u_n.

Then U-L=D+T exactly. The checker verifies positivity and exact containing
rational intervals for D/(U-L) at both prefixes. Keeping all accepted low
mode bounds fixed, further Hardy source modes leave D unchanged. Their
maximum possible reduction of this squared enclosure width is therefore
at most T. This is a statement about this bound construction.

The decomposition does not determine how much of D is error of the dual
lower trial, how much is error of the solenoidal upper trial, or how much
is the small numerical enclosure width. Attribution mostly to the dual
lower bound remains OPEN without further information.

## Proof

Expand V and separate the modes through31. Their coefficients split as
u_n/n^2-u_n/N^2. Subtract sum J_n and sum ell_n^2 and collect the remaining
terms. This gives U-L=D+T with no approximation. Exact accepted inputs
and rational arithmetic verify its positivity and the reported shares.
Future additional Hardy modes change only terms outside the fixed low
mode expression D. The new upper construction still includes D and a
nonnegative remainder, so it cannot reduce the width by more than T.
This conclusion assumes the low mode data, trial floors and lower bound
are unchanged; it is not a bound on all possible future methods.

The attribution limitation already occurs in a finite Hilbert space.
Take H=R^3 with its Euclidean inner product, gradient subspace span(e1),
and orthogonal divergence-free subspace span(e2,e3). Let A=(1,1,1).
The exact gradient projection has squared norm1. The dual trial e1 is
exact, giving squared lower1. A solenoidal trial e2 removes only squared
norm1 from ||A||^2=3, giving upper2. The interval width1 comes entirely
from the missed solenoidal direction e3, with zero dual error. Conversely,
in R^2 with the whole space as the gradient subspace, A=(1,1) has squared
norm2, a dual trial e1 gives lower1, and the trivial divergence-free
space gives exact upper2. The same width1 is entirely dual error. Thus a
width split that only distinguishes fixed low modes from angular tails
cannot identify the error within those fixed modes. These examples
refute the general inference, not a factual inequality about candidate016.

## Dependencies and verification

Bind the four accepted own records and this proof before execution. Save
R1-054's review as an inert local source for the literal scope comparison.
Recompute V,L,U,D,T independently with exact Fraction arithmetic and
compare stored U and L. Check the two Hilbert examples by exact dot
products. Do not execute peer code or repeat any source integration.
Record actual times, hashes and every check. The existing complete016
bounds and every candidate verdict remain unchanged.

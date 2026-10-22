# Literal row-density comparisons for the M16/s16 finite sections

## Statement and scope

Let s_{R,p,j} be the binary64 number obtained by parsing entry j of
sections.Fminus.sigma_small5 in the twelve saved JSON files identified by the
capture manifest, where R is L2, L2q, H1 or H1q, p is 2, 4 or 6, and
j ranges from 0 through 4. The p=4 files carry the suffix p4_re2. These are
literal saved numbers, not certified singular values. Interpret each finite
binary64 number exactly as a dyadic rational.

For adjacent p,p' in (2,4,6), define
  d_{R,p,j}=s_{R,p',j}-s_{R,p,j},
  a_{R,p,j}=|d_{R,p,j}|/s_{R,p,j}.
All denominators are positive. The forty exact signed differences, relative
changes and eight maxima are given in evidence/check.json and independently
verified in evidence/audit.json. Each maximum belongs to the closed rational
window recorded there. All forty differences are nonzero.

The recorded input arrays listed in code/check.py have identical dtype,
shape and bytes across the twelve vector archives. Three associated column
metadata pickle files have identical bytes. The saved retained counts are
1866 for L2/C0 and 1834 for the other three C1 functionals at threshold 1e-10;
the respective saved 1e-12 counts are 1887 and 1855. This asserts literal
input and count equality. It does not assert equality of the actual floating
retained bases, exact satisfaction of their join constraints, or a certified
common subspace of the continuous operator domain.

## Proof of the finite arithmetic certificate

A finite binary64 number with sign b, exponent field e and mantissa field m
is (-1)^b (2^52+m)2^(e-1075) when 1<=e<=2046, and
(-1)^b m 2^-1074 when e=0. Thus it is exactly rational. The first checker
uses float.as_integer_ratio and Fraction. The independent checker extracts
the sign, exponent and mantissa from the eight IEEE bytes, uses the displayed
formula and python-flint fmpq, and rereads the copied source JSON files.
Neither checker imports or executes the numerics producer.

For positive s, subtraction followed by division gives exactly d and |d|/s.
Taking a maximum over five rational numbers by integer cross multiplication
is exact. If M>=0 and n=floor(10^12 M), then n/10^12 <= M <= (n+1)/10^12.
The checker records this window; the auditor checks its endpoints by exact
rational order. It also reproduces each numerator, denominator and maximizing
index. This proves the claimed finite comparisons if both checked outputs
and the pinned inputs pass. No floating tolerance is used.

For the smallest entry, an increase relative to the earlier value means
(s_new-s_old)/s_old. It differs from the fraction of the new value
(s_new-s_old)/s_new. A percentage must name its denominator. The report uses
the former convention throughout.

## Input equality and source dependence

The primary checker reads the selected arrays through NumPy and compares
shape, dtype and all payload bytes. The independent auditor reads the NPY
members directly with zipfile, decodes only their literal header using
ast.literal_eval, and compares every payload byte; no pickle is executed.
Equal byte strings are identical encoded inputs. The three column pickle
files are compared as opaque byte strings only. Their hash alone does not
prove any mathematical property of the objects they encode.

The frozen c2_fminus.py constructs radial column pieces from the trial,
stride and Mh, separately from the ppc-dependent collocation nodes. In
c2_gram2.py the Gram quadrature uses the column pieces, the trial parameters
and mode H1m. The constraint and whitening construction additionally uses NJ
and the eigenvalue threshold. These inputs are independent of ppc. The
collocation images enter the spectral calculation through Aw_all. This is a
source-level dependency observation, checked by reading the code. Partial
saved Gram arrays can corroborate it but cannot replace a full Gram or
retained-basis certificate. The output minima and actual assembly remain
floating computations. Equal counts alone would not prove equal subspaces:
span(e1) and span(e2) in R2 are a counterexample.

## Dependencies and excluded conclusions

Only the pinned source JSON, vector members, metadata byte strings and two
producer source snapshots are used. No earlier mathematical result is
required. This result proves no norm convergence, SVD accuracy, full operator
image identity, domain membership, inverse bound, nonlinear closure or IPM
endpoint. Increasing unweighted values is an observation; attributing the
entire change to row count is not proved here. Independent actual Opus5.5
review and a later verifier adjudication are required before FINAL status.

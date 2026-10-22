# Complete cutoff range argument and precise remaining hypotheses

This addendum completes the argument of PROOF.md. Its finite application
remains subject to the final audit. All quantities below use the exact
binary endpoints of the new merged file, with the exact radii
r_in=231/8000, r_out=297/8000, and h=33/4000.

## Complete extrema and independent Bernstein method

Write S_j for the j-th derivative of S. For j=1,2,3,4,
S_j(v)=v^(5-j)(1-v)^(5-j) Q_j(v), where
Q_1=-630,
Q_2=-2520+5040v,
Q_3=-7560+35280v-35280v^2,
Q_4=-15120+136080v-317520v^2+211680v^3.
These identities follow by differentiating S_1=-630v^4(1-v)^4
and multiplying out. The complete interior critical sets for S_j are:

1. {1/2};
2. {(7-sqrt(7))/14,(7+sqrt(7))/14};
3. {(7-sqrt(21))/14,1/2,(7+sqrt(21))/14};
4. {(1+e sqrt((15+d 2sqrt(30))/35))/2: e,d in{-1,1}}.

For the first three sets, factor the next Q polynomial. In particular,
Q_3=-35280(v^2-v+3/14) and
Q_4=211680(v-1/2)(v^2-v+1/7).
For the fourth set, direct differentiation gives
S_5=-15120(35(2v-1)^4-30(2v-1)^2+3)/8.
All displayed radicals are real, distinct, and strictly between0 and1.
The factor degrees show that no interior roots have been omitted.
The numerical condition that an evaluated polynomial ball contains zero
is only a check of these explicit identities. It is not being used as an
existence or completeness proof for roots.

For an exact distance interval[d0,d1], intersect its cutoff-argument
interval[(d0-r_in)/h,(d1-r_in)/h] with[0,1]. The absolute maximum of
S_j on the resulting closed interval is attained at an endpoint or a
listed critical point. Include any critical-point ball overlapping the
interval. S itself decreases from1 to0, so its left endpoint suffices.
Outside the transition interval, the cutoff is constant and its first
four derivatives vanish. Scale the j-th derivative by h^(-j).

The second method uses no critical points. On each rational subdivision
[a,b] of the argument interval, bound v(1-v) by its exact maximum and
Q_j by the maximum absolute Bernstein coefficient after the affine
change v=a+(b-a)u. The identity
u^l=sum_{k=l}^n binom(k,l)/binom(n,l) B_{k,n}(u)
proves the conversion. Nonnegativity and partition of unity of the
Bernstein basis on[0,1] prove its range bound. Multiplication of the two
nonnegative bounds is safe even though their maxima need not coincide.
The two methods independently bound T1,T2F,TL,TL1,TL2 using the radial
identities in topic115 and 1/r<=1/max(d0,r_in) wherever a derivative is
nonzero. In particular T2F is tested using the square root of
|S_2/h^2|^2+(|S_1/h|/max(d0,r_in))^2. The code rejects nonfinite
mpmath endpoint encodings before converting them to rational numbers.

## Scope of the new physical implication

The finite result concerns the new source012e106b... and merged
b5f597c9..., not a historical old-source execution. The geometry transfer
is by exact equality of all five relevant fields of every retained row
and all partition parameters, plus revalidation of the prior pins. It
therefore transfers the already independently proved106496-case cover,
including62547 omitted cells. It transfers no residual or cutoff-model
coefficient estimate. In fact52 G0 endpoints increased from the old file.

The following are the explicit remaining physical hypotheses for the
conditional forcing conclusion:

H0. g is the residual of the specified canonical modal trial, with the
stated parity and local W^{4,infinity} regularity. The local smoothness
of that exact trial was checked in topic115. Identifying the numerical
radial jets with the derivatives of that physical residual is separate.

H1. On each of the26079 inside and1368 straddling rows, the six saved G
fields bound the physical quantities listed in PROOF.md, uniformly on
the restricted physical cell. For inside rows the Hessian G2F is not
needed. The cutoff T fields and their physical geometry receive the
independent checks here; they are not part of this unresolved hypothesis.

H2. On each of the16502 transition rows, the five saved F fields bound
|tau g|, |grad(tau g)|, |Delta(tau g)|, |grad Delta(tau g)| and
|Delta^2(tau g)| on the same restricted physical domain, uniformly in p.
Proving H2 requires valid residual and cutoff function models, their
compositions and products, recentering, truncations, and Bernstein bounds.
A scalar Taylor remainder alone does not certify the missing polynomial
coefficients or their arithmetic ancestry. The331 saved active series
triples on38445 retained rows suffice to check their scalar tail formulas.
They do not establish the physical inequality |q-c0|<=c0*x for the
new execution. Topic120 and121 concern a different contemporary set of
geometry arrays. They are not silently transferred to this pair.

Under H0,H1,H2 the cutoff argument, all pointwise-product inequalities,
the coverage and the two complete aggregations prove the strict ceilings

| lambda | order3 | order4 | order31/10 |
| --- | --- | --- | --- |
| 1 | 0.7759 | 893.16 | 1.5700 |
| 500 | 1.8107 | 1638.56 | 3.5769 |

Here each number bounds N_{lambda,s}(tau g), and strictness follows from
the exact positive gaps in the final aggregate comparison. These
hypotheses are sufficient. They do not claim to be necessary conditions.

The upstream route to H1 and H2 is cert_resid.py SHA
1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053,
_cell_core_deriv, saved as _last_eps. cert_forcing2.py lines212-239
consumes those five radial jets and constructs the complete angular jet.
It reads cert_green.npz SHA
c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1
and trial_v2_h0.008.npz SHA
a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.
The complete independent Green/T/radial checks are topics98,99,101,
currently queued behind the independent middle-region audit. Their
completion would still leave the full forcing angular, Cartesian and
composed-model evaluation obligations. Topic72 states a conditional
floating dot-tree theorem; it does not attest the actual BLAS kernel.

The saved sup_D_eps arrays on B_{9delta/4}(P) and B_{3delta}(P) require
an additional physical assertion for each of their fifteen partial
derivatives. Merging partwise maxima is checked, but the unretained
B_{3delta} cells' derivative polynomials and suprema are not saved in this
merged forcing file. No B3 derivative bound is inferred from the43949
retained rows alone. The forcing norm uses the smaller support disk.

No surrounding exclusion, global inverse estimate, nonlinear closing
inequality or decisive IPM endpoint follows from this conditional result.

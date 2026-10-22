# Independent verification criterion for the exported radial Taylor models

## Exact finite problem and scope

This result checks local ODE propagation in the middle region. It does not
identify every input box with the canonical trial. That remaining data
obligation is explicitly separate. Take one specified middle cell of
length h0 and its certified upper length h>=h0, Q=12, and modes n=1,...,261.
All binary64 data below mean exact dyadic numbers. Let E be a positive real
number in an input interval, and let A_n,B_n and each coefficient F_(n,k),
0<=k<=7, lie in their respective closed input intervals. These inputs are
constant in u. Define

 f_n(u)=E^2 exp(2u) sum_(k=0)^7 F_(n,k)u^k, 0<=u<=h,
 q_+'=(2n-2)q_+-f_n, q_+(0)=B_n/E^2,
 q_-'=-(2n+2)q_-+f_n, q_-(0)=A_n/E^2,
 P_n=(q_++q_-)/2, R_n=(q_+-q_-)/2.                       (1)

The exact canonical Green formula implies these equations for
P_n=2n psi_n/r^2 and R_n=psi'_n/r, with E=exp(t_a); topic81 reconstructs
that identity. Here(1) is a well-defined finite family of entire solutions
for every choice in the specified input boxes, even before canonical
membership is checked. The positive overhang h-h0 is treated only as the
extension of this cell's polynomial forcing. No extension of the actual
spline across a knot is claimed.

The candidate from the frozen cert_flow.py is two degree-Q Taylor models

 sum_(j=0)^Q [p_(n,j)-rp_(n,j),p_(n,j)+rp_(n,j)]u^j
                  +[-ep_n,ep_n]

and the analogous expression for R. Acceptance requires that every exact
Taylor coefficient P_n^(j)(0)/j! and R_n^(j)(0)/j! belongs to the respective
coefficient interval, for all admitted inputs, and that a proved uniform
Taylor remainder is at most ep_n or er_n, respectively. Every coefficient
radius and remainder must be nonnegative and finite. Complete containment
in both independently computed interval enclosures is required; agreement
of samples or overlap does not suffice. If these tests pass, Taylor's
integral formula proves the candidate interval encloses the corresponding
solution of(1) for every u in[0,h], hence in[0,h0].

The first implementation will test explicitly named cells and all261 modes.
No untested cell is accepted. It preserves both successful and failed
comparisons. A failure of containment by an upper-bound method is OPEN,
not a disproof of the producer's enclosure. Disjointness of a rigorous
point value and its asserted value interval could refute it, but no such
disjointness is assumed.

## Two independent coefficient calculations

Write lambda_+=2n-2, lambda_-=-(2n+2). For real lambda define

 T_(j,k)(lambda)=1/j! sum_(v=0)^(j-k-1)
                 ((k+v)!/v!) lambda^(j-k-1-v) 2^v,

when j>=k+1, and zero otherwise. This is the coefficient of u^j in
integral_0^u exp(lambda(u-v))exp(2v)v^k dv. Indeed expand both exponentials;
for a term v^(k+b)(u-v)^a its beta integral is
(k+b)!a! u^(k+b+a+1)/(k+b+a+1)!. Dividing by a!b!, and setting
b=v_index, a=j-k-1-b, gives precisely the displayed rational coefficient.
The exponential series are absolutely uniformly convergent on[0,h],
which justifies termwise integration. For the integer lambdas here all
T weights are exact rational numbers and can be precomputed independently.

Put Z=E^2. Then the exact coefficients are

 P_(n,j)=[B_n lambda_+^j+A_n lambda_-^j]/(2j! Z)
       +(Z/2)sum_(k=0)^7 F_(n,k)[T_(j,k)(lambda_-)-T_(j,k)(lambda_+)],
 R_(n,j)=[B_n lambda_+^j-A_n lambda_-^j]/(2j! Z)
       -(Z/2)sum_(k=0)^7 F_(n,k)[T_(j,k)(lambda_-)+T_(j,k)(lambda_+)]. (2)

The Arb checker evaluates these linear weights, combining each occurrence
of the same F_(n,k) before taking its interval radius. E is enclosed by
its full positive input interval. Interval division and multiplication
then enclose all possible E, without assuming independence between its
occurrences. Any enlargement from interval dependency is harmless if the
result is contained in the producer's interval.

The separate mpmath.iv checker instead forms the forcing Taylor coefficients

 f_j=Z sum_(k=0)^min(j,7) F_(n,k) 2^(j-k)/(j-k)!,

and uses the first-order recursions

 q_(+,0)=B_n/Z, q_(+,j+1)=(lambda_+ q_(+,j)-f_j)/(j+1),
 q_(-,0)=A_n/Z, q_(-,j+1)=(lambda_- q_(-,j)+f_j)/(j+1).

It averages these two sequences to form P and R. Thus the second route
uses neither the first route's weights nor its polynomial summation code.
Both carry input radii and perform directed arithmetic throughout. They
must each pass the full containment test.

## Independent whole-cell Taylor remainders

Let C_k bound |F_(n,k)|, and define, for0<=i<=Q,

 G_i=E_max^2 exp(2h) sum_(k=0)^7 C_k
             sum_(v=0)^min(i,k) binom(i,v) 2^(i-v)
                                      k!/(k-v)! h^(k-v).

Leibniz's rule and nonnegative powers show G_i>=sup|f_n^(i)| on[0,h].
Let a_+=sup|B_n|/E_min^2, a_-=sup|A_n|/E_min^2, and

 Y_+=exp(max(lambda_+,0)h)(a_++h G_0),
 Y_-=exp(max(lambda_-,0)h)(a_-+h G_0).

Variation of constants bounds |q_+|<=Y_+, |q_-|<=Y_-. Repeatedly
differentiating the scalar ODE gives

 q^(Q+1)=lambda^(Q+1)q
                  +sign sum_(i=0)^Q lambda^(Q-i) f_n^(i).

Consequently define

 D_+=|lambda_+|^(Q+1)Y_++sum_(i=0)^Q |lambda_+|^(Q-i)G_i,
 D_-=|lambda_-|^(Q+1)Y_-+sum_(i=0)^Q |lambda_-|^(Q-i)G_i,
 H_n=(D_++D_-)/2 * h^(Q+1)/(Q+1)!.

Taylor's integral remainder proves that H_n bounds the remainder of each
P_n and R_n. The lambda_+=0 case uses 0^0=1 for the term i=Q,
which is the correct coefficient of f_n^(Q); all other positive powers
of zero vanish. The checker must handle this explicitly or by the exact
integer-power convention. Exponentials are evaluated directly, so no
unverified small-step polynomial bound for exp is imported.

Primary Arb forms G_i with the Leibniz sum above. The second engine forms
the derivative polynomial recursively by D(exp(2u)C)=exp(2u)(C'+2C),
then bounds its coefficients on[0,h]. It independently forms Y and D and
checks the resulting H_n against both candidate remainder budgets. The
absolute derivative-polynomial coefficients are bounded before summing;
this may be sharper than the first engine's triangle bound and is valid.
No input radius or high-order forcing derivative is omitted.

If this sufficient uniform bound exceeds a candidate budget, a later
checker can use the defect theorem in topic81 or sharper interval Taylor
remainder bounds. Such a refinement must have its own proof and preserve
the original failed test. It cannot relabel an inconclusive comparison as
a refutation or silently inflate a producer remainder.

## Provenance and canonical data obligations

The candidate is reconstructed with the frozen source SHA pins from
topics69 and75, Q=12, the specified current runtime and all source inputs
as exact dyadics. Only that finite reconstruction is certified; no
bitwise historical runtime identity is asserted. The accepted topic69
finite modal-map audit contains the exact image of every middle-region
input T box in the resulting F box. Topic75 certifies h, E, reciprocal
and auxiliary scalar data, but not the Green-moment or Taylor-polynomial
input membership.

For an actual canonical-trial conclusion at any accepted cell, all of
these further conditions must be established at the same exact t_a:
A_n and B_n are the canonical Green moments; E=exp(t_a); the factor
coefficients T are those of the exact normalized trial in u=t-t_a; and
the finite F derivative map is correctly linked to that factor. The
available selected180 Green checks do not certify the remaining entries.
The independent density-moment archive is a possible source for checking
these conditions, but archive existence is not itself that comparison.

The full flow certificate also requires all cells, angular coefficient
and remainder coverage, product/sum arithmetic, spatial classification,
and each stated field inequality. All are outside the conclusion of the
present local criterion. No global inverse or decisive endpoint follows.
This proof precedes its implementation.

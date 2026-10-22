# Index, precision and evidence conventions before implementation

The pre-code actualOpus5.5 review accepts the identities with seven
requests. The following resolves them, with two corrections to its
reasoning and without editing any frozen dependency.

The archive header has degree7, stream_modes261, spans1558, cells7809.
Each span has density_polynomials[262][8], i_left[261], j_right[261].
The arrays i_left[n-1],j_right[n-1] contain the scaled I_n,J_n in PROOF;
the angular frequency is m=2n, not n. The midpoint coordinate is the
exact (a+b)/2. The density index in the I forcing is n-1, so n=1 uses
H_0. The J forcing at n=261 is H_261, whose eight coefficient balls
must all be exact zero. Archive keys, shape, coordinate and exact-zero
conditions are checked, not inferred from array positions alone.

The actual maximum parent width is below1/50 and hence every argument
has |z|<263/25=10.52. The guard verifies this exact bound from the full
partition. The convolution method uses iv180 decimal digits and N96,
with the exact tail(4), much more precision than the roughly16 bits
lost from cancellation in an exponential with |z|<10.52. A signed
interval sum with its full absolute tail remains rigorous regardless
of cancellation. The review's suggestion that this actual range
necessarily makes the enclosure useless is not justified. Containment
is checked rather than assumed. The n=1 backward J factor grows by
exp(2u); the review's statement that all backward factors decay is
false. Formula(2) and the code retain this growing factor.

For efficiency, compute Phi_7 by(3)-(4), then use the exact identities

 Phi_j(z)=[1+z Phi_(j+1)(z)]/(j+1), j=6,...,0.

They follow by integration by parts applied to the defining convolution
integrals, or by coefficient comparison of the absolutely convergent
series. The same formula holds at z=0. Interval propagation of the
Phi_7 tail encloses every lower moment; no separate tail is discarded.
The code caches only functions of the exact rational pair(lambda,u),
not of a density coefficient or a target interval. Cached evaluations
are tied to the fixed arithmetic precision and N.

The complete assignment asserts first_cell0=0, positive child counts,
consecutive first_cell values, increasing original spans, and
sum(count)=7809. Every target is evaluated at its exact rational t_i,
not at floating tb[i]; tb[i]+/-tb_rad[i] is checked to contain t_i.
The full run captures the old180 selected A/B index pairs as fixtures,
and checks their target containment through each of the two new
methods. The old selected certificate remains limited to180 entries.
Its phrase about untested entries means no assertion about them; no
frozen dependency is rewritten.

Both methods must be CONTAINED for PASS. Either method disjoint from
the target is a candidate REFUTATION only after the proof/input audit;
overlap without containment remains OPEN. If the two methods are
disjoint from each other, the run aborts as an implementation or input
inconsistency. There is no majority vote or intersection used to repair
a failed method. Zero target radius requires exact equality.

The ODE derivation of A/B in PROOF is a consistency check. Their
canonical integral definitions, not merely finite-span ODEs, determine
the homogeneous constants and are imported from modal_green.

Evidence is the complete two-engine streaming calculation with pinned
source and accepted canonical inputs, plus a final artifact audit and
fresh, explicitly selected third-method spot checks. Hashes and saved
minima alone do not verify omitted intervals. The final audit will
recompute the180 old fixture entries and a deterministic sample chosen
from the input hash before the full run. Such spot checks are diagnostic;
they do not replace either complete method. Re-running the full checker
reproduces every comparison and the streamed value hashes. The claim
remains OPEN until this full computation and audit pass.

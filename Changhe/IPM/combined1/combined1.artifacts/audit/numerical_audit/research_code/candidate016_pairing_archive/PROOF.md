# Candidate016: replayable archives of cancelling moment sums

## Statement and dependencies

Use the exact candidate, spaces, rational test functions and complete residual
of ../candidate016_dual_lower/PROOF.md, including its cutoff clarification,
and the angular right inverse and divergence-free fields of
../candidate016_solenoidal_upper/PROOF.md. The candidate raw SHA256 is
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
All integrals are over the whole plane. The two test frequencies are 1 and 3.
The exact input coefficients are read from the hash-bound JSON archive.
No optimization or basis completeness is a premise.

For each frequency n let d_n=||grad psi_n||_2^2>0,
p_n=integral F psi_n, Z_n=A_(Delta psi_n)-grad psi_n,
a_n=||Z_n||_2^2>0, and b_n=<A_F,Z_n>. The cited proofs establish

 H(F)^2 >= p_1^2/d_1+p_3^2/d_3,
 H(F)^2 <= M2-b_1^2/a_1-b_3^2/a_3,

where M2 is the complete angular-divergence energy, including every residual
frequency. This topic does not evaluate M2 and therefore gives no numerical
upper bound for H by itself. Its purpose is to export moment groups with
sufficient absolute precision to replay the already proposed lower bounds
for the two quotients and the two nonnegative improvements.

## Exact formulas and independent reconstruction

Put t=r^2/(1+r^2), w=1-t, b=beta-1 and
P_b(t)=sum_(i:beta_i-1=b) x_i t^(k_i+1), so
psi_n=r sum_b w^b P_b(t) sin(n theta).
Set D_b P=(1-2bt)P+2t(1-t)P'. Then the logarithmic second derivative of
r w^b P is r w^b D_b^2 P. Reconstruct the complete residual mode as
f_n=r sum_ell w^(ell delta/2) A_(ell,n)(t), with exact rational functions A.
Every contributing background interaction is retained and the resulting
coefficient hash must equal the previously accepted complete projection.

For each exponent e=ell delta/2+b-3, form complete grouped rational functions

 L_e(t)=sum_(ell,b with this e) t A_(ell,n)(t) P_b(t),
 C_e(t)=sum_(ell,b with this e) t A_(ell,n)(t) D_b^2 P_b(t)/n^2.

The two signed pairings are exactly

 p_n=(pi/2) sum_e integral_0^1 w^e L_e(t) dt,
 b_n=(pi/2) sum_e integral_0^1 w^e C_e(t) dt.

These are the formulas derived in the two cited standalone proofs. Each
rational function has denominators composed of positive factors 1+s w.
Extract the exact numerator zero order q at w=0 and require e+q>-1.
The exact partial fraction identity and the positive-pole moment recurrences
of ../rational_pole_moments/PROOF.md then give containing Arb intervals.
We rebuild the projections and all grouped functions using own code, and
compare every group exponent, zero order and numerator hash with the
original production records. Exact positive d_n/pi and a_n/pi are imported
from their independently derived rational integrals, with original hashes.

## Exported intervals and the finite replay

Let I_j be a containing interval for an exact group integral. Conversion to
a decimal ball must contain I_j; its midpoint alone is insufficient. If the
printed interval is J_j, interval arithmetic yields

 sum_j exact_integral_j in sum_j J_j.

Multiply by a containing interval for pi/2 to enclose the signed pairing.
Every input and output ball is reparsed from the saved JSON. Bounds on the
sum of absolute radii are recorded, because cancellation makes relative
precision of individual groups an insufficient criterion. The checker
requires the accumulated group radius below 10^-250 and more than 700 bits
of relative accuracy in the final replayed pairing. It also checks strict
containment of that pairing inside the previously saved 200-digit final
pairing ball. These criteria are verified outcomes, not conclusions merely
from printing 650 digits.

Squaring and dividing by positive containing d_n or a_n intervals gives
containing quotient and improvement intervals. The saved exact rational
floors must lie strictly below the lower endpoints. Orthogonality of modes
then reproduces the saved H lower floor. Substitution in the stated exact
energy weights reproduces the saved E2 lower floor and its strict separation
from the independently accepted 007 E2 upper bound. Summing the two exact
improvement floors gives the same bound available to a later complete-M2
assembly. These operations are monotone in the necessary positive arguments.

For comparison, the old 200-digit group displays are summed separately. A
large resulting radius explains why they alone cannot replay the aggregate.
It does not refute the original production, which summed full4096bit values
before formatting. No original file is modified. If any stated replay check
fails, this topic remains OPEN and the reason is recorded.

## Scope

This is a finite replay and archive-precision repair of four complete
candidate pairings. It changes neither the mathematical test functions nor
the original accepted values. It does not establish optimality, completeness
of a trial space, a complete H value, a correction-distance ordering, a
linear inverse, a contraction, or an existence theorem. The existing Opus
analytic reviews are separate premises of the final mathematical assembly.

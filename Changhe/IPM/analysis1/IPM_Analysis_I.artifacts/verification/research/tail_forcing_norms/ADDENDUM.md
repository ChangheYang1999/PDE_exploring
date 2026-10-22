# Mandatory clarifications and finite computation provenance

This accompanies the unchanged proof-first PROOF.md. The actual Opus 5.5
follow-up accepted the proof and requested explicit dependency citations.

The transition chi is zero on s<=1 and one on s>=2, and b is supported
on [1,2], exactly as in topic105, PROOF(3). Topic106, PROOF(6)-(9), proves
that its H1 is exactly the same k Epsilon/(1-k). The canonical inverse
is linear: a sum of its solutions satisfies the summed stream equation,
parities and sublinear growth, so uniqueness identifies it with the
canonical solution. The scaling argument applies at each fixed T. The
spatial sublinear behavior of the V_i follows from their canonical finite
Green expansions; it does not follow merely by comparing powers of T.
The review's reference to a1+1 as a reason for sublinear velocity growth
is unnecessary. Equation(8) is justified by the explicit stream scaling
and the independently established canonical uniqueness.

Uniform expansions are used only as T tends to infinity, so aT eventually
exceeds every fixed exterior radius. No estimate at all T>=R_b/a is
inferred. The topic15 center and growth assertions are kinematic only.

For the Simpson rule, on the unit half-width panel [-1,1] the Peano
kernel of integral minus Simpson is
K(t)=-(1-t)^3(1+3t)/72 for 0<=t<=1 and K(-t)=K(t). It is nonpositive
and integral |K|=1/90. A change of variables gives h^5/90 for a panel
of half-width h. Summing N/2 panels gives length*h^4/180. The audit
checks both polynomial halves, reflection, the exact integral and the
scaling identity with rational arithmetic. Thus the quadrature error
has an independently checked finite bound, not an unverified library
quadrature tolerance.

The Arb calculation uses exact polynomial power antiderivatives for J.
The iv calculation uses 1025 Simpson nodes, the full fourth-derivative
bound, and adds the exact upper endpoint of its error interval in both
directions. Its A and B come from beta moments after s=a+(b-a)u and
the independent recurrence integral u^n/(1+u)=1/n-integral u^(n-1)/(1+u).
Each calculation separately implies every public interval. Overlap is
only a consistency diagnostic. Both full calculations are rerun by the
output auditor, which compares every non-timing output field.

Two implementation failures were caught before certification. The first
iv script attempted to multiply a Fraction directly by an iv value; that
unsupported conversion raised NotImplementedError before producing an
output. It is replaced by an explicit outward interval conversion. The
first audit allowed Python integer true division in the highest Peano
coefficient, creating a float; exact equality failed. Explicit Fraction
conversion repaired the audit. The initial sources are archived as text.
Neither failure is treated as an interval result or an accepted check.

The first Opus attempt returned stop_reason=max_tokens and no final text;
it is not acceptance. The subsequent actual Opus 5.5 end_turn review
supplies the preliminary proof opinion. The final verdict still requires
a whole-current-file closure review and independent adjudication.

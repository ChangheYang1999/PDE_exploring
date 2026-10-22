# Final adjudication: one newly encoded reference still jumps

CONFIRMED for the frozen source reproduced on the captured M24 scalars:
ref_J and ref_Jin are exactly C4 and belong to X. REFUTED for the same
interpretation of ref_wide: its positive inner trace at the outer cutoff
is strictly between1.2121e-13 and1.2122e-13, while the outside value is0.
It does not belong to X. This is a nonzero singular weak-gradient term,
not a large-norm estimate. The ideal exact normalized-coordinate formula
is C4 and is not refuted.

Here X uses the weak gradient and norm squared

    integral_R2 (h^2+r^2|grad h|^2) m(r)^(-2)
                (1+r^2/L^2)^(-3/2) dX,
    m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2),

with the captured profile's L>0 and0<k<1. All references equal x^2y near0
and vanish for sufficiently large r, so the only membership issue is exact
continuity at finite circles. The proof and exact arithmetic settle it.

Rational Horner and independently decoded direct monomial differentiation
agree on30 endpoint derivatives. A third, exact-rational construction with
explicit binary64 nearest-even rounding reproduces all30 returned
coefficients and3 rounded widths, independently of native floating powers.
The two scalar NPY headers and IEEE payloads are checked against prior pins.
Only the isolated source function was executed, not the numerical application.

Two actual Claude Opus5.5 exchanges completed end_turn. The final response,
request71bc4506-eadc-4eb7-82be-e2325fd8ecdd, accepts the scoped result and
withdraws two imprecise phrases: the oriented outside-minus-inside jump is
negative, and a generic value repair gives C0, not C4. PROOF.md, ADDENDUM.md
and REVIEW_RESOLUTIONS.md are mandatory together with this adjudication.
The saved initial AST failure preceded arithmetic and is unused. The harmless
empty-sum initialization in the independent script is overwritten before use.

No historical or future job output, numerical Gram matrix, singular vector,
spectrum, global inverse or PDE endpoint is certified or refuted here.
A continuous reference does not make a nonconforming test vector belong to X.
Exact coefficient reconstruction or another conformity repair would require
its own Gram and angle transfer analysis. The final local hash gates and
actual model identities are recorded in evidence/verdict.json.

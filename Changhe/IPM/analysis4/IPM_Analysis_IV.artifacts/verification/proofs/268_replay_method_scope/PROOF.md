# Scope of independence in the period-seven and period-eight replays

Status: source-level statement CONFIRMED. The convergence admissions remain unchanged.

## Statement

The response constructors and higher-precision replays for topics253 and256 import and call the same Taylor enclosure function from taylor_response_enclosure.py. They are separate higher-precision computations with independently reconstructed coverage and exact-polynomial prefix checks. They are not independent implementations of the Taylor enclosure arithmetic.

## Verification and argument

Parse the four retained Python sources. Each imports enclose from taylor_response_enclosure and contains a call to that name; none replaces it locally. The shared function evaluates the compact response with the same audited jet algebra at the center and on the whole interval, then evaluates the degree-three Taylor enclosure by Horner's rule. Thus the constructor and replay share this arithmetic implementation. The replay independently refines roots, reconstructs dyadic endpoints and integer coverage, compares low-order fields with exact rational Cartesian polynomials, verifies their norm bounds, and checks the rational scalar map. These are valid separate checks, but they do not justify the narrower phrase separate manual Taylor implementation.

The Taylor enclosure is mathematically justified by the derivative remainder theorem: the center coefficients are derivatives divided by factorial, and the whole-interval coefficient encloses the normalized third derivative at every intermediate point. Horner evaluation over the centered interval encloses its polynomial and remainder. The same statement would hold for term-by-term summation. The admitted proofs require a correct enclosure, not two unrelated implementations. Consequently this wording correction does not remove any hypothesis of the convergence theorem or alter a certified number.

Dependencies:253,256 and the reviewed Taylor-jet argument in232/234. The later262 tail replays use a separate term-by-term summation but still share the audited jet algebra. All references to independence should state this scope.

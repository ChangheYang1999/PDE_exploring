# Exact dyadic transport of finite Arb balls

Date: 2026-10-20. Status: elementary enclosure lemma proved; implementation validation recorded alongside the code.

## Statement

Suppose a finite real Arb ball is B=[m-r,m+r], where m is its stored exact dyadic midpoint and r>=0 its stored exact dyadic radius. Export the integer mantissas and exponents

m=M 2^e, r=R 2^f

as four exact JSON strings. On import, evaluate C=arb((M,e)) and D=arb((R,f)) outward, and return C+arb(0,D.upper()). Then the imported ball contains B. This remains true if the import precision differs from the export precision.

## Proof

Exact JSON integer strings represent M,e,R,f without binary64 conversion. Outward conversion guarantees m belongs to C and r belongs to D. Hence r<=D.upper(). Every x in B can be written m+t with |t|<=r, and therefore belongs to C+[-D.upper(),D.upper()]. Arb addition encloses this Minkowski sum. This proves the claim. No relative decimal safety factor, decimal digit estimate or unproved library exp rounding bound enters the argument.

The calls mid().man_exp() and rad().man_exp() are only used on exact, finite Arb values. Their defining contract returns the exact dyadic integer mantissa and exponent. The implementation rejects nonfinite input, negative radius mantissa and a schema mismatch. Its tests compare exact rational dyadic endpoints, including import at both lower and higher precision and zero radii. These tests supplement the preceding proof; a finite test set alone is not the proof of the general lemma.

## Application and limits

Dependent modal coefficients may be exported as these balls while retaining their independent definition by exact join and normalization equations. Transporting an enclosing ball is not proof of those equations. The data definition, derivation and dependency hashes are still required. This helper is a concrete replacement for the radius-free or five-digit-radius export rules refuted in ../modal_exactification/PROOF.md. It writes only into this verifier lane and has not modified the numerics lane.

## Reviewed implementation and local library contract

Actual claude-opus-5-5 accepted the proof and transport implementation at 2026-10-20T15:38:17Z. Its follow-up suggestions were implemented: exact schema keys, canonical integer strings only, rejection of negative zero and non-string integers, and low import precisions 8 and16bits. There are now 432 exact-rational containment checks (72 stored balls at six precisions). The installed library is python-flint0.9.0 with FLINT3.6.0. The actual local constructor, man_exp and upper docstrings are recorded in evidence/library_contract.json. They explicitly give exact tuple semantics, exact finite mantissa decomposition and upward upper endpoints. The earlier numerics report's environment versions are not used as this lane's library provenance.

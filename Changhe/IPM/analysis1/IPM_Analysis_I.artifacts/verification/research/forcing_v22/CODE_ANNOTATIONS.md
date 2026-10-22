# Annotation to the immutable Arb checker

In code/check_cutoff.py, the final auxiliary export writes the method
string `independent upper endpoints, also checked below producer T2F`.
The second clause is REFUTED for the original auxiliary export: on each
of the26079 constant rows, nextafter(0,+infinity) exports2^(-1074),
whereas the producer field is0. The preceding core comparison uses the
exact Arb upper bound0 and passes correctly.

The phrase must be read as: independent outward endpoints; the original
export comparison with producer T2F fails on constant rows; use only
cutoff_hessian_bounds_checked.json if this auxiliary array is needed.
The nearby comment about checking against the Arb upper bound is true.
The source and original output are preserved so their pre-review hashes
remain meaningful. This file, HESSIAN_EXPORT_ADDENDUM and the explicit
REFUTED failure record are mandatory annotations to that immutable code.

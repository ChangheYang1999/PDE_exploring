# Arbitrary-order angular-table reference

This extends the existing exact-polynomial reference to the actual S20 table sets. The standalone statement and informal proof are in ../PROOF.md. The formula includes every integer order between zero and the degree; no parity restriction is used.

Before a production comparison, freeze an `allm-table-nodes-v1` manifest with case `S20_own`, source and input SHA256 bindings, and the exact binary64 coordinates and integer mode triples of every consumed table set. Each set names an NPZ, its SHA256, coordinate and mode keys, degree, consumed derivative order and calling functions. Capture the main and closure paths, including pressure-related closure calls. The present generator accepts degrees up to18. Any consumed set outside this scope remains open and must be added explicitly.

The independent reference uses the previously checked rational Cartesian polynomial coefficients, 70-digit Decimal arithmetic and an 80-digit mpmath normalization. It computes values, three gradient entries and nine Hessian entries at each exact input coordinate. It stores binary64 high and residual low words, with the largest remaining representation difference by degree and derivative order. These differences are measured against the computed 70-digit reference and are not rigorous enclosures of the mathematical value.

At the first, middle and last node of each set, compare all modes and components with the separately derived normalized complex recurrence at70digits. Require relative-to-max(1,absolute-values) disagreement at most1e-55. Qualify odd-order mode handling, Cartesian derivatives, input validation and serialization before the actual reference. Preserve source hashes and exact input bytes throughout.

The producer then compares its double-double table path entrywise using specification G5(c): tolerance1e-13, floor1e-13 times the largest reference magnitude in the same degree and derivative order, and explicit exact-zero blocks. The verifier separately checks the coverage, denominator conventions, saved differences and all failure counts. Reference generation alone releases no case.

Run on CPU35 with one busy process, one thread and no GPU. No JavaScript/TypeScript, server, remote compute, cluster, Lean or Lake. Write only in independent verifier. A conservative uncompressed allowance must fit below the9.9GB storage guard before each compressed file is written. The scientific sources of the running pair holdouts remain unchanged.

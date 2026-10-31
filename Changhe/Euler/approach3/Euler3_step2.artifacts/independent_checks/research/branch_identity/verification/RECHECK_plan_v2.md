# Binding recheck of the two branch-parameter tools

Prepared 2026-10-29 after V414 and the lead's 19:02:50Z and 19:09:20Z notes, before execution. This tests the finite criterion proved in ../PROOF.md. It does not evaluate new fields or establish mathematical branch identity.

Capture both current source files. Re-evaluate the actual P1/F2 parameter example from its saved width and EVAL records, compare to independent scalar arithmetic, then use consistent small fixture records to test source identity, all iteration fields, all parameter fields, column positions, optimizer coordinates, positive finite scales and eigenvalues, finite orthonormal eigenvectors, matrix reconstruction and finite equal costs. For invalid evidence the registered outcome is OPEN. Retain observed acceptance as a counterexample, without asserting that actual records contain that inconsistency.

Evaluate the producer's extracted parameter functions and the lead's captured top-level program with controlled in-memory inputs. Never run their production main routines or write outside this side. Use one CPU process on core 35, thread counts one, no GPU. No JavaScript/TypeScript, servers or cluster access.

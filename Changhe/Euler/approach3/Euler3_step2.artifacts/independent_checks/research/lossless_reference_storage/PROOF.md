# Exact recovery from a bytewise reference

## Statement and hypotheses

Fix an integer n >= 0. Let B and R be elements of {0,1}^(8n), the byte strings of a newly evaluated array and an arbitrary reference of the same length. Fix a permutation pi of the 8n bit positions and a lossless encoder E with decoder D satisfying D(E(X)) = X for every admissible bit string X. Define the stored payload as E(pi(B xor R)). If the decoder receives that payload, the same R, pi and D, it recovers B exactly by applying pi^(-1), then xor R.

An array interpretation additionally requires its original shape, element type and byte order. The claim concerns exact stored bytes, including signed zeros and non-finite bit patterns. It does not identify two different floating-point evaluations.

## Proof

For each bit position i, exclusive-or satisfies (B_i xor R_i) xor R_i = B_i, since R_i xor R_i = 0 and B_i xor 0 = B_i. The lossless decoder first recovers pi(B xor R). The inverse permutation recovers B xor R because pi is a bijection. Applying exclusive-or with the same R therefore recovers B at every bit position. The recovered byte string has length n and equals the original byte string. Interpreting these bytes with the original shape, type and byte order recovers the original array representation. No relation between the numerical values represented by B and R was used.

## Dependencies and implementation conditions

This argument uses only the elementary identities for exclusive-or, the inverse of a finite permutation and the stated lossless-codec hypothesis. A chain of references satisfies the same result by induction from a retained root reference, provided the chain is finite and has no cycle. The implementation must preserve every reference and its metadata. A file hardlink shares the existing bytes; it does not itself establish immutability. Source and decoded-byte checks detect unintended changes in the tested workflow. A digest match alone is not a mathematical proof of byte equality.

The implementation uses the existing reversible byte shuffle and compression. The new reference selection takes place after the new residual is evaluated. It changes storage only. Different coefficient coordinates, Jacobian conventions or residual values may be used as references because the theorem requires equal byte lengths, not numerical agreement. Shape and type are checked in addition to length to avoid metadata mistakes.

## Scope

This is an exact discrete statement. It proves no Euler identity, derivative, residual estimate, tolerance or convergence claim. Numerical checks of the codec and the original-archive reconstruction are documented alongside this proof. No formalization has been attempted.

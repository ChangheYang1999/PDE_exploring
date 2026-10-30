# Candidate 024: checking the publisher's held-out hash explanation

## Claim and exact inputs

The current held-out document is the exact byte string bound in
../candidate024_holdout/verification/result.json, with SHA256
e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab.
The index instead gives
58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5.
The publisher's note at 2026-10-29T11:52Z says that the only edit was

 Objective rows (81? no: 67):  ->  Objective rows (67):

and that it occurred at 09:13:43Z, before the recorded 10:37 launch.
This audit checks the proposed byte explanation. It does not infer
historical timestamps from a hash or from an author's later assertion.

## Argument and finite check

The current document must contain exactly one occurrence of the right
hand string and none of the left hand string. Replacing that one
occurrence by the proposed former wording uniquely reconstructs a
candidate former byte string. Store it with a name marking it as a
reconstruction, compute its hash and compare the complete 64 hexadecimal
characters with the quoted former hash. A match supports precisely this
proposed byte explanation. A mismatch refutes this as the complete edit
explanation. It need not refute that some differently edited file existed.

Independently parse both bullet lists of integer probe pairs from the
current and reconstructed text. Their exact equality, and equality with
the 25 public plus 35 diagnostic pairs accepted in N4-342, proves that
this reconstructed edit preserves the entire intended probe list. A
byte-level single-replacement check proves that every other byte agrees.
In particular the date printed in the first line is identical; it is not
an independently observed creation date.

## Scope

This closes the explanation only if the actual complete hash matches.
Even then, no observation of the reconstructed file at an earlier time
is supplied. The current row-span certificate is unaffected either way.
The bad hash remains absent from the immutable024 manifest, and the
MID16 label and backend corrections in N4-342 remain separate findings.
No numerical residual, norm, inverse or existence claim is involved.

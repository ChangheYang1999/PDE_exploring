# Scope and acceptance of the final theory hash-prefix check

## Statement and inputs

This is T4-514. Its target is the copied report v184, SHA-256 `1ee8d6afe69fd431b347d3d11a54b1b40e0c841d9ca55166296aa72d14c78bca`, lines2543-2544. The local source filename report_v183.md.gz reflects the acquisition plan, not the version in the copied bytes; PREPARATION_NOTE explains the intervening repair. The report now states that T1 checked54 hash tokens printed after T1 filenames and cites T1 note75. The claim here is that this repair accurately narrows T1's stated scope. Its selector, saved output and notes73-75 are the inputs. Universal coverage of every T1 citation in the actual report remains OPEN in this audit. No actual missed citation is asserted.

## Argument

The selector scans mixed letter-and-digit hexadecimal tokens of length8 to64. For each token it takes only the preceding240 characters, finds the last recognized filename in that window, excludes intervening PROOF/result/checker/manifest labels and explicit other-lane paths, and requires that filename in its hash inventory. These conditions restrict the selection. The saved output has54 rows:29 same-name matches,10 other-file matches and15 no-matches. Their interpretation against all historical source files in note73 is producing-lane evidence; this audit does not repeat that source hashing. Note74 corrects the last matched historical draft from63 to62 without changing the counts.

The window rule cannot by itself prove universal citation coverage. Consider THEORY_FINAL followed by one space and a1234567. The recognized filename is within the preceding240 characters. Insert241 additional spaces before the same token. The text still names the file and prints its token, but the preceding240 characters contain only spaces, so the rule omits it. This refutes completeness of that selection rule on arbitrary documents. It is not a counterexample showing an omitted citation in the actual report.

T1 note75 explicitly states this distinction and proposes the54-token wording. The target report uses that wording and cites the note. Read with the stated selection rule, this is an accurate finite-scope report. It does not claim that all possible citation contexts were searched. The adjacent T2 clause is outside this audit and is not independently rechecked here. No mathematical bound or candidate status changes.

## Verdict and limits

CONFIRMED T1 note75's scope clarification, the saved54-row partition, and application of the report repair in the target bytes. REFUTED universal completeness of the240-character rule on arbitrary documents, not a claim about an actual missed citation. OPEN actual exhaustive coverage, historical execution and unexamined new report passages. No further repair is requested against these two lines. No T1 program executes; the only computation is a finite local text check. The final main mathematical synthesis and prior report acceptance remain unchanged.

# Integrity of the eight selected postfreeze audit records

## Statement

The exact selection in source/selection_v01.json consists of audit records N4-436 through N4-443. Each nominated root must match the SHA256 cited by its extracted ledger entry. Every direct input edge in its inputs map must resolve inside this lane and match its recorded SHA256. The finite total is 1937 direct edges across eight roots. This supplements, and does not replace, the H22 selection of49 roots in the N4 evidence index v03.

The three frozen main documents and the H22 index must retain their nominated hashes. FINAL_AUDIT_ADDENDA_through443.md is an immutable copy of the addenda through N4-443; the subsequently appended live addenda is not implicitly frozen by this operation. The complete statement is byte integrity of these explicit files and direct dependencies. It proves no mathematical claim, and it does not upgrade a FLOAT, conditional or OPEN result.

## Hypotheses and proof

A selected root is a JSON object with an inputs map from path strings to64-digit SHA256 strings. The selection specifies its own path, digest, ledger ID and retained proof path. Validate each schema and reject duplicate root IDs. Extract the relevant ledger blocks before this checker is written and verify that each selected digest occurs in its own block. For each root, calculate the digest of its actual bytes, compare it with the selection, and enumerate every input edge. Resolve each path strictly under the lane directory, calculate SHA256 by reading the complete byte stream, and compare it with the recorded digest. A symlink is allowed only if its final target remains inside the lane. Repeated paths can share a digest calculation only while their device, inode, size and nanosecond modification time remain unchanged. Recheck every observed signature at the end.

Under the usual collision-resistance assumption, successful enumeration proves that each explicitly named current local input has the bytes recorded by its root. All1937 direct comparisons must pass; no missing path or unsupported binding may be skipped. Newly inventoried proof hashes are distinguished from previously bound hashes. The immutable addenda snapshot and the three main documents are checked against the predeclared selection, so the frozen-document claims are also finite digest equalities.

N4-443 separately read and checked738 files named in the snapshot and N1 artifact manifests, plus one mutable T4 addenda digest. Those739 external digests are retained as provenance in the N4-443 record and are counted here but not reread. Earlier roots contain their own copied source data; no peer path is executed or traversed by this checker. No unlisted transitive dependency, historical immutability, mathematical proof replay or optimization restart is certified.

## Evidence and scope

source/selection_v01.json and source/ledger436_443.md define the finite scope. verification/PROOF_FIRST_v01.json binds the proof and selected files before code/check.py exists. The checker records all eight root comparisons, all1937 direct edges, exact unique-file counts, retained external provenance, actual start/end times and errors. It writes a separate the N4 post-freeze evidence index v01 and result, using exclusive output creation. The H22 index and all accepted evidence records remain unchanged. No JavaScript, server, cluster, GPU, numerical integration, Lean/Lake or peer program is used.

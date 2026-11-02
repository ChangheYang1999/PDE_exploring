# Exact preservation of overlap-audit inputs

Declared 2026-10-31T19:01:26.910816+00:00, before the existing C audit inputs are snapshotted.

## Statement and scope

An overlap audit names each input path and the SHA256 digest of the bytes read. Team result streams may grow after that audit. The empirical claim is that every input version named by the two completed reserved-C-best-v9e-001 separation audits can still be preserved as a lossless compressed blob whose decompressed SHA256 equals the recorded digest. A missing or changed version that cannot be recovered exactly refutes this claim. No game is run by this check, and a successful snapshot does not strengthen the scope or completeness of the original audits.

## Conditional byte-identity argument

For an ordinary file, hash its complete bytes. For an absent file with a retained gzip archive, decompress that archive and hash the result. For a changed JSONL stream, consider only prefixes ending at a recorded line boundary, together with the empty prefix. Hash each prefix incrementally and accept only a matching digest. If none matches, stop with a failure; do not substitute the current file.

Compress each accepted byte sequence with gzip, decompress the saved blob, and recheck its digest. Record the source path, recorded source digest, recovery method, sizes, and compressed-blob digest. Distinct audits may name different versions of one path, so deduplicate by digest rather than path. Rehash the original audit files after processing to detect audit changes during the check.

Under the usual collision-resistance assumption for SHA256, a verified decompressed digest identifies the bytes named by the original audit. The argument does not prove that an audit read every relevant input, recognized every schema, or established statistical independence. Those limitations remain as stated by the audit.

## Component and integration checks

Exercise a complete current file, an appended JSONL prefix, the empty prefix, a lossless archive, and rejection of a nonmatching digest. Then preserve both completed C separation audits, inspect all declared input versions, and verify every saved compressed and decompressed digest. The terminal D pipeline will use the same preservation step after its separation audits and require this verification before final publication. D remains unexecuted until its previously declared time and selection gates.

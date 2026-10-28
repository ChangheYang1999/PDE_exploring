# Publication file-identity checks

The checker in code/check_publication.py performs local, read-only inspection of the theory author and numerics teams and the original verifier team. It does not run any proof, numerical assembly or peer script. Its only writes are timestamped JSON records under this directory's evidence/ subfolder in the verifier team.

Run it from the original verifier tree using the permitted Python interpreter, one thread and low priority:

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 19 python3 -B certificates/publication/code/check_publication.py --label final

The default sibling locations are the original theory author and numerics team teams. The two optional path arguments only select read locations. The copied publication package is not a self-contained replacement for the original verifier tree: it deliberately omits large proof caches, and some numerical replays additionally need the supplied read-only source files. Do not describe these checks as a portable reproduction of all computations.

The JSON record contains:

- Every listed artifact manifest hash and an inventory comparison with actual artifact files.
- Source/copy comparisons for the main report, all companion reports, verifier handoffs, small proof files, all certificate files, the two root identity scripts, numerics artifacts and theory author audit files.
- Every omitted proof file larger than 2 MiB, checked against its original bytes, listed size and SHA256, and checked to be absent from the copied proof tree.
- The explicitly typed paths and hashes in the supported final audit-record formats, plus the current proof inventory and handoff links. This does not parse every historical hash in prose or establish mathematical validity.
- File metadata checks before and after reads and at the end of the snapshot. The report states its actual start and finish times. Later edits are outside its claim.

The newly written certificate is excluded from its own input inventory. Its later inclusion in a refreshed package cannot be certified by its own checksum. The verifier's chronological ledger and final handoff identify which observed snapshot was checked.

The preflight record preflight_173151.json is intentionally retained with all_checks_pass=false. All 1,576 then-packaged manifest hashes, 24 omission hashes/sizes, 226 recorded dependency relations and 323 guide links passed. Eight source/copy comparisons differed because the verifier files had changed after packaging. V295 records this intermediate failure. A later passing snapshot, if present, supersedes its current-copy status without rewriting this evidence.

No JavaScript/TypeScript, server, cluster, GPU, proof-assistant build or remote calculation is involved.

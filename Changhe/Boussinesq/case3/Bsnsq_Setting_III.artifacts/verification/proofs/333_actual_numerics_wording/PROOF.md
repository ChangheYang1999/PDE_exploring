# Actual numerics wording adoption

Prepared 2026-10-22T09:41:22.917545+00:00, before controls.

## Statement and hypotheses
The actual numerics-lane files named below equal the six complete files approved by P330, and the consolidated CSV retains its P330-frozen bytes. This is a statement about one read snapshot, not future files or numerical truth newly inferred from wording. P330 already checked the data scope and static generator changes; P313/P316 establish the numerical and portability findings.

## Complete argument
Freeze the six actual files plus CSV and the numerics adoption note. For each file, compare bytes, SHA256 and size to its corresponding P330 approved file, or the frozen CSV for the unchanged data. Equality of bytes establishes exact adoption, including all approved scope repairs and generator literals. Parse the SHA256 manifest without executing either generator and check every advertised source file that exists under the recorded source directory. A manifest-line mismatch is an explicit failure, not inferred away from matching table output. Confirm the two source copies agree. No new generator run is needed for byte adoption; its claimed regeneration remains a numerics-lane activity unless separately reproduced. Retain the historic header times and the actual09:38 adoption time distinctly. The exact frozen input list records the read times and hashes.

## Scope
Verdict is CONFIRMED only for the frozen actual files if all comparisons pass. No independent regeneration claim, no PDE solution, and no final T_end claim follows. General B2 remains OPEN. All writes remain in verification. No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake builds or online posts.

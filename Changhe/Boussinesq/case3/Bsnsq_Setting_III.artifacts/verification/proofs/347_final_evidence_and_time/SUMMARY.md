# Final evidence and time accounting

Updated 2026-10-22T11:14:01.849899+00:00. Verdict: CONFIRMED for the finite clock arithmetic and the conditional source reading; OPEN for actual finalization and exact active research time.

The verifier starts 2026-10-20T12:44:15Z and its 48-hour wall horizon is 2026-10-22T12:44:15Z. Lead and numerics start four and two seconds earlier. Each final report must use its own clock. T_end has not been set by this packet.

Independent Python datetime subtraction and source controls passed 83/83 at 2026-10-22T11:12:54.332842+00:00 in 0.002020s. Code SHA256 bf5c62d2599d868b3ca3e5e3d0890538bf5c9b08524c8156f07587a73a3dd6d5; final proof SHA256 dd4c585f6a5e23c7d1c7fd65ea2bbd655d280083f6296c749ef3395d8763780b. The source's outer 47-hour condition only gates the next shift, conditional on this being the executed source; it is not an asynchronous kill of shift 9. Its internal clock is unlogged. The separate timeout starts after the shift log and has no kill-after option, so no exact future exit is certified.

At NUM's provisional 2026-10-22T10:58:00Z, wall elapsed is 46h13m47s. The exact sum of recorded shift-session intervals is 46h10m17s; the seven recorded end/start differences total 210s. The summed integer-minute counters give 46h05m00s, discarding 317s. Neither the counters nor exact session intervals measure active research. The verifier also has seven explicit 30s recorded gaps, while its initial 22m17s before the coordinator switch has no recorded shift-1 end and must remain unclassified. These are timestamp differences at the logs' precision, not an inference about whether background computation or another lane continued.

The finalizer criterion requires actual successful execution, a confirmed pre/post write bracket and current matching report bytes, hash and size. A dry run or audited source does not meet it. Current archive coverage is a separate finite input audit. General B2 remains OPEN: no YES candidate and no NO theorem for the full prompt class has been established.

Read PROOF.md, verification/time_checks.json and verification/model_adjudication.md. Old proof v1/v2 and prior check output remain preserved. No teammate code was executed.

# Numerical-lane final time source: exact bookkeeping and limits

Prepared 2026-10-22T11:25:43.128853+00:00 before the checks in this packet. This is a source and timestamp audit, not a mathematical B2 theorem or execution of the numerics lane's program.

## Statement

Let t0=2026-10-20T12:44:13Z and cap=t0+48h=2026-10-22T12:44:13Z. The frozen numerics log contains eight completed shifts, followed by shift9 starting 2026-10-22T11:19:39Z. For each completed shift, define d_j as its recorded end minus its recorded start, and m_j=floor(d_j/60). For a cutoff q in shift9, define D=sum(d_j)+(q-start9), M=sum(m_j)+floor((q-start9)/60), and wall=q-t0. These are timestamp differences and session occupancy. They do not measure active computation or research.

The recorded m_j are 356,342,353,352,348,353,323,360 and sum to2787. The eight explicit end-to-next-start gaps are30 seconds each. Hence wall=D+240 seconds and D-60M is the sum of the fractional-minute residues, including shift9. The exact floor-minute loss can be computed from the frozen log; it is not an unknown idle gap.

The current frozen NUM_REPORT differs from the P333-approved report only in two provisional time passages. The five approved artifact files should remain byte identical. This is a content snapshot claim, not a statement about all computation performed since P333.

## Source findings and counterexamples

The frozen final_tend.py samples utcnow and then discards seconds and microseconds. Let q be that minute floor. Its printed T_end is q; it need not equal the actual report-write time, which occurs later. A prospective cutoff entry is useful if labelled report cutoff. It is not evidence of the actual end of the lane. An actual end record must use a measured timestamp, clearly state what event it timestamps, and disclose later actions if any. In particular, the source's last-recorded-activity sentence is not made true by planned later WORKLOG, RUN_STATUS, notes and waiting. The source's source-time wall and minute-occupancy arithmetic are accurate for q under the log assumptions; their labels should state that wall is truncated to whole minutes and M is summed floor-minute occupancy.

The horizon branch compares q with12:44:00, thirteen seconds before cap. It labels all q>=12:44:00 as at, including q=12:44:00 (before cap) and q=12:45:00 (after cap). These explicit counterexamples refute that exact boundary classification. An event timestamp e compares to cap by e<cap, e==cap, e>cap. If execution is bracketed by before and after samples, a strict before conclusion requires after<cap, and a strict after conclusion requires before>cap. A bracket straddling cap does not identify the write side. A minute-only timestamp cannot resolve the thirteen-second offset.

The planned statement that shift9 ran no computation is too broad: the lane has already recorded hash/integrity checks and plans a consistency checker. A supported intended statement is that it launched no new numerical solver run. The final source should claim only the completed actions it can substantiate; future actions are not observations.

## Proof and independent method

Subtract each ISO UTC timestamp using the Python standard library, with no system-clock inference. Telescoping the adjacent shift intervals plus their eight gaps gives wall=D+240. Taking each integer floor independently gives the stated m_j and M. Compute boundary examples directly from timestamps, without running or importing any numerics-lane program. Parse the frozen source as text/AST only to confirm its clock truncation, branch and write order. Compare current and approved report bytes with an independently constructed diff, requiring all changed hunks to stay inside the two time passages. Compare the five artifact hashes. Read the preview as data, preserving any new future-looking claims rather than executing it.

## Verdict and scope

The arithmetic and unchanged substantive numerical content can be CONFIRMED when the finite checks pass. The exact horizon classification and identification of the minute-floor timestamp with actual last activity are REFUTED by the counterexamples. General B2, a successful future write and its actual time remain OPEN. Repair suggestions are concrete source/wording proposals, not an authorization to write outside this lane.

Dependencies: frozen log, source, preview, current report, P333 copies and P347 timestamp proof. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake, git commit/push, posting or contact with people. Writes only inside verification.

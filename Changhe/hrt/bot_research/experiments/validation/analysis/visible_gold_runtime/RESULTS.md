# Visible-gold runtime on two retained histories

Completed 2026-10-31T20:52:37.364667+00:00.

H1 **CONFIRMED**: all100 fresh candidate decisions exactly match the recorded actions, and both histories replay through the unchanged engine. H2, a call takes more than3 wall-clock seconds: **CONFIRMED**. H3, a call takes more than3 process-CPU seconds: **CONFIRMED**.

Maximum wall time: 6.770995s, seat0 round50; maximum CPU time: 6.716633s, seat0 round50. These are measurements under the recorded core affinity and low priority, not portable bounds.

| Seat | Round | Visible gold | Own splash S | Max list length | Total type slots | Component wall s | Component CPU s |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 10 | 3132 | 460 | 210 | 410 | 0.000061 | 0.000055 |
| 0 | 20 | 426855 | 1550 | 28457 | 48271 | 0.000601 | 0.000595 |
| 0 | 30 | 2534265 | 1550 | 168951 | 286382 | 0.004735 | 0.004728 |
| 0 | 40 | 6441590 | 1550 | 429439 | 727822 | 0.012727 | 0.012718 |
| 0 | 50 | 12149100 | 1550 | 809940 | 1372720 | 0.027057 | 0.027049 |
| 1 | 10 | 3132 | 460 | 210 | 410 | 0.000059 | 0.000054 |
| 1 | 20 | 426855 | 1550 | 28457 | 48271 | 0.000516 | 0.000510 |
| 1 | 30 | 2534265 | 1550 | 168951 | 286382 | 0.004646 | 0.004640 |
| 1 | 40 | 6441590 | 1550 | 429439 | 727822 | 0.012652 | 0.012645 |
| 1 | 50 | 12149100 | 1550 | 809940 | 1372720 | 0.026861 | 0.026854 |

All10 component calls have maximum list length equal to active opponent entries plus floor(visible gold /15), as predicted by the source argument. The gun cap disables gun search but does not bound these allocated lists. An already immune map does not bypass their construction or the planner's initial list scan.

The original checker stopped before any policy call because it omitted the harness research metadata in the initial headers. AMENDMENT.md documents the exact correction; no game record was edited.

These are two previously recorded standard games against the x202a factory-cap1200 policy, with no new strength sample. Only the candidate action stream is freshly regenerated; the opponent's historical live source is not asserted identical to its current source. The existing result stays best_v9e790:785 in both assignments. Candidate bytes and poolD are unchanged. See PROOF.md and the pinned input/receipt hashes.

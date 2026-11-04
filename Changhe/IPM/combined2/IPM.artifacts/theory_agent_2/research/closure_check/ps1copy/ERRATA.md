# Errata for this directory (the first theory agent)

E1 (2026-11-03, after the theory auditor AT-1448). The header of budget_013i.py, line 2, calls 0.0055545729 the Hermite upper of
AT-1431. That decimal truncates the accepted upper 0.0055545729030073655758 downward, so it is not an upper bound.
Read "the Hermite upper N_(21/10) <= 0.0055545729030073655758 of AT-1431 (input 0.0055546, rounded up)". The script
uses N = 0.0055546, which is outward, so budget_013i.out stands (AT-1448). budget_013i.py is kept unchanged because
theory_v13 cites it. Recorded in theory_v14 as E-v13-2.

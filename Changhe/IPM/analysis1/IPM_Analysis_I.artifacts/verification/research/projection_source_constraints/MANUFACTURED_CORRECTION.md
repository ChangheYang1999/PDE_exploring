# Mandatory correction to the manufactured example

Written 2026-10-21T20:45:21.569298+00:00, before the corrected supplemental checker. The first diagnostic
correctly rejected my mistaken derivative18 in REVIEW_RESOLUTION.md. The
inner derivative is3*2+5=11, the right derivative is-2, so the jump is13.
Replace18 by13 in that manufactured example. The primary actual-column
certificate did not use this manufactured value and is unchanged.

The failed code and log are preserved as code/check_supplement_attempt1.py.txt
and evidence/supplement_attempt1.log. That attempt produced no supplement.json.
This correction changes the diagnostic expected value only, not either exact
trace formula. All four manufactured traces are now(-5,13,5,-2).

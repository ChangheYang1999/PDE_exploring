# One-turret, one-wall extension search

2026-10-31T14:47:58.565928+00:00

The exhaustive enumerator considered78541 distinct proposals and accepted
77408 on the funded fixture. The minimum zero-damage cost is200 for each
of the three stated component rosters. The retained lexicographic witnesses
are gun3 at(1,1) for three tier1 plus three tier3, and gun3 at(10,3) for
three tier1 plus six tier3 or one tier4. None uses an additional wall.
This minimum applies only to the class with at most one new turret and
one wall. A known140-cost gun2-plus-splash answer lies outside that class.

The139 legal single-splash additions have maximum total exposure130,
not180. One extra splash therefore cannot make this fixed two-splash map
splash-immune to tier3. This corrects the proposed one-splash response to
the early tier3 strike; it does not say that guns or larger extensions
cannot stop the finite roster.

The full search took285.662391 seconds. Independent checks
repeat all three winning witnesses with original apply_action, pathfinding
and combat, and independently enumerate all single-splash cells. All pass.
The checker took0.072730 seconds. The minimum-cost assertion
also relies on the full enumerator and its complete finite-class argument;
the witness checks alone establish feasibility. Results concern funded
round6 components, not affordability in every opening or game strength.

Exact JSON: bots/counters/data/cheap_guard_extensions_001.json.
Programs: experiments/validation/search_cheap_guard.py and check_cheap_guard.py.
Receipt: verification/receipt.json. The checker globals accesses were
corrected during source review before its first run; no failed measurement
or earlier result was replaced.

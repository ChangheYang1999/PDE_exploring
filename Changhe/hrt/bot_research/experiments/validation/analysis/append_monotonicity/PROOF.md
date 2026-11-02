# Appending attackers cannot reduce fixed-map damage

## Statement and hypotheses

Use the bundled combat procedure in td_game/combat.py and its nonnegative
catalogue damage values. Fix one round number, a finite tick horizon T, a
legal defender map, its route, and the defender's starting HP. No construction
or other map change occurs during either combat simulation. Let A be the
ordered active attacker roster. Let B be A followed by any finite list of
additional active entries, each with a fresh identity. The old entries keep
their types and identities. Inactive entries may occur in the stored rosters
provided their removal leaves precisely this active-prefix relation.

Then every arrival of an entry of A in the A simulation also occurs, at the
same tick, in the B simulation. Consequently total base damage in the B
simulation is at least total base damage in the A simulation. This remains
true when the additional indices wrap around the modulo-T spawn schedule.

All entries move one route edge per tick after their birth tick. Gun targeting
chooses maximum route progress among entries in range, breaking ties by the
stable entity-list order. All guns choose before any damage or death is
resolved. Splash attacks every adjacent entry independently, with no shared
damage budget. These are properties of the bundled procedure, not assumptions
about an arbitrary tower-defense game.

## Notation

For an old identity i, its birth tick is its dense active index modulo T. Its
position at every subsequent tick before removal is determined solely by that
birth tick and the common route. Let H_A(i,t), respectively H_B(i,t), be its
HP immediately after the attacks at tick t if it remains alive. The stable
list order among identities already present in A is unchanged when restricted
from B: insertion may interleave new identities, and removals may delete
identities, but neither operation reorders the surviving old identities.

## Proof

Induct through the ticks. The induction invariant is: every old identity
alive after the smaller simulation's attacks is alive after the larger
simulation's attacks, at the same position, with at least as much HP.
Every old arrival already recorded in the smaller simulation has also been
recorded at that same tick in the larger simulation.

The invariant is initially vacuous. An old entry spawns at the same tick in
both simulations because appending active entries leaves its dense index
unchanged, including when new indices wrap modulo T. Its initial HP agrees.
Movement changes no HP and depends only on age, so all old identities alive
in the smaller simulation are still present at the same positions before
arrivals. Each such identity reaching the base therefore arrives in both
simulations at that tick. Remove those identities from consideration.

Consider an old identity i still alive in the smaller simulation immediately
before the attacks. It is alive, in the same cell, in the larger simulation.
Its splash damage is identical in the two simulations, since every splash
applies its fixed damage independently to each eligible cell occupant.

For each gun, if it targets i in the larger simulation, it also targets i in
the smaller one. Otherwise the smaller simulation has an eligible identity
j preceding i in that gun's priority order. The induction invariant leaves
j alive in the larger simulation too; eligibility and relative order agree.
The larger simulation would therefore choose j or an identity preceding j,
and could not choose i. This contradiction proves the assertion for that gun.
It follows that the gun damage received by i in the larger simulation is a
subset, gun by gun, of its gun damage in the smaller simulation. Damage is
nonnegative and all target choices precede death resolution. Thus its larger
HP minus its larger total damage is at least its smaller HP minus its smaller
total damage. If it survives the smaller simulation, it survives the larger
one with at least that HP. This proves the invariant's next step.

The arrival assertion now follows by induction through all T ticks. Each
common old arrival inflicts the same nonnegative base damage. Any additional
old or new arrival in the larger simulation adds nonnegative damage. Summing
arrivals proves the total-damage inequality. Combat does not stop when the
defender's HP becomes nonpositive, so this sum remains valid past a lethal
arrival. End-of-round clearing adds no base damage and changes the inequality
in neither direction.

## Positive lethal-count search

Fix any active prefix A and a type q. Let D(n) be fixed-map damage from A
followed by n copies of q, for integer 1 <= n <= N. The theorem gives
D(n+1) >= D(n). For a positive target damage h, the predicate D(n) >= h is
therefore monotone on this finite positive domain.

An exact positive-count search first tests n=1 and then doubles a tested
nonlethal upper candidate, clipping it to N. If the tested N is nonlethal,
no positive count in the domain is lethal. Otherwise a lethal hi and a
strictly smaller tested nonlethal lo enclose the least positive lethal count.
When n=1 is lethal, it is immediately the answer; an artificial lo=0 is used
only to express that boundary and requires no assumption about D(0).
Testing the integer midpoint preserves the bracket. Each test strictly
reduces its integer width until hi-lo=1, when hi is the least positive lethal
count. Clipping and testing N is necessary when doubling would skip it.

## Dependencies and scope

The proof depends on stable priority, fixed routes, unchanged old spawn
indices, simultaneous target selection and nonnegative independent damage.
It requires no monotonicity in construction, spending, roster permutation,
removing an earlier entry, or replacing an old entry with another type.
In particular, a new map can change the route, and inserting a filler before
an old entry can change that entry's spawn phase. Neither operation is covered.
This is a one-round fixed-map theorem, not a statement that buying more units
improves full-game strategy. It does not repair the frozen fortress helper.

Verification will call the original spawn_schedule, combat_tick and
simulate_map functions on paired rosters. It will check the HP invariant at
every tick and compare a separate positive-count helper with exhaustive
original-combat evaluation on finite fixtures. These checks supplement the
argument and do not constitute proof-assistant formalization.

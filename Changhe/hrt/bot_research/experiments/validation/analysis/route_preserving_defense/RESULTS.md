# A route-preserving splash ceiling

Checked 2026-10-31T15:39:26.100114+00:00.

CONFIRMED: with the fixed gun1 at (10,1), adding turrets only off the current route keeps the route at22 steps and caps splash exposure at560. The bound is attained by twenty splashes; every addition is legal on the unchanged engine. The proof covers all such placements, and the checker counts the56 contributing adjacencies in two orders.

On the maximizing splash map, tier4 is stopped, while a tier5 takes at most616 total damage and survives. Original combat confirms all incoming tier5 copies arrive for n=1,2,3,227,228, and the229th copy is cleared at the tick cutoff. No additional guns beyond the fixed corner gun are included in that combat statement.

The current budget defender never builds walls or blocks its current route, so this restriction explains why its splash coverage cannot reach tier5 immunity. It is not a proof that every defensive gun mixture loses. Evidence and exact input hashes: verification/ceiling.json.

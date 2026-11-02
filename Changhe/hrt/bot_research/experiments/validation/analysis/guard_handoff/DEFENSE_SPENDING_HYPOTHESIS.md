# The defense/economy boundary before the H10 handoff

The traced baseline buys a 540-gold gun plan in round6 and a 600-gold gun
plan in round7, then takes140 damage in round8. Its round8 planner fails to
find zero leakage within813 gold even if asked only about the actual four
tier5 copies. Allowing partial gun plans produces the same784-gold plan and
one arrival. This observation does not prove that no affordable defense exists.

Conjecture: a different earlier defense/economy schedule can avoid the hit
and preserve a lead through H10. Change one parameter from P5TNUF3 at a time:
passive_until in4,6,7; fortress_n in null,2,8; fortress_k=1;
big_partial=false; spec_share in0.8,1.0. Compare all ten variants on H10 and
H12, both seats, against the repeated controls of h10-transfer-001.

These are full-policy interventions, not fixed-state plan comparisons.
They may change attacks as a consequence of changing the remaining gold.
All are disclosed development conditions. Any repair needs a later
cross-family regression test. The handoff opponent retains its three-second
gun-planning cutoff; equality of histories will be measured rather than assumed.

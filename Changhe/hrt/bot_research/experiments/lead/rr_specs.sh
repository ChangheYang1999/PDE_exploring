# Finalist specs for the final round robins (sourced by queue_rr.sh). Frozen files only; bots/best.py is not read
# (its bytes equal experiments/lead/frozen/best_v9e.py, sha256 70ef8eab...).
E29='bot_research.bots.economy.frozen.v29.econ29:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400&replan_base=true&own_in_layout="replan"&own_min_s=1200&min_cap=3000&active_cap=4000&fill=true&fill_reserve=true&fill_threat=true'
BEST_V9E='bot_research.experiments.lead.frozen.best_v9e:@make'
BEST_V9F='bot_research.experiments.lead.frozen.best_v9f:@make'
AF2G='bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null'
P5TNUBM='bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5'
V41='bot_research.bots.defense.frozen.v41.fortress:@make'
V29="$E29"
G1="$E29&attack_from=7"
GUARD00='bot_research.bots.counters.early_wall_guard:@make?witness="guard00"'
TDEF='bot_research.harness.baselines:@threat_defender'
# H14 candidate (NOTES_FOR_TEAM 20:19:29Z): best_v9e with the full attack budget from round 6, catch-up kept at 0.5.
AS1C='bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5'
# hrt-w1's final recommendation from 21:45Z (notes/defense.md 21:48Z); used by queue_h17.sh.
V46='bot_research.bots.defense.frozen.v46.fortress:@make'
# hrt-w1's final recommendation from 22:39Z (notes/defense.md 22:39Z); used by queue_h19.sh.
V48='bot_research.bots.defense.frozen.v48.fortress:@make'
# hrt-w2's af5 = V29 + attack_from=5 (experiments/economy/specs/af5.spec; selected by its 18.22 rule, notes/economy.md
# 18.26; recommendation open at 23:20Z); used by queue_h21.sh.
AF5="$E29&attack_from=5"

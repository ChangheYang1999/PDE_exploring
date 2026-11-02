# Separate mid-tier insurance ablation

The source has two independent insurance layers. Setting poke_insurance=false
skips the parent's cheap-poke insurance, but Lead17's mid-tier method still
checks its own mid_until and visible-poke condition. Thus the first ablation
cannot establish that all bait-triggered insurance is absent.

Declare three actual V18FT configurations: unchanged, mid_until=null, and
mid_until=null plus poke_insurance=false. Repeat the ten grower/bait cases and
four early budget-timing cases, and add the frozen economy17 and recommended
economy21 opponents because mid-tier insurance was introduced to protect an
early HP lead against economic opponents. Both assignments give96 conditions.
The unchanged baseline duplicates some existing data and will be treated as a
reproducibility check rather than an independent strength sample.

Hypothesis: removing both layers fixes the one-copy bait, but may regress
against economic opponents' small persistent rosters. The declared comparisons
must report both improvement and regressions. These are whole-policy
interventions; different later construction, income, damage and bounties
prevent a single-path causal decomposition. No reserve-C condition is used.

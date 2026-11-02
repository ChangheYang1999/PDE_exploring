"""Fixed development payoff table (0 loss, 1 draw, 2 win).

Derived from runs/validation/archetype-round-robin-001.jsonl.
Input SHA256: 84642dd407ad845d7c94ba97684f2352f99dcf85d267af29833f28230a6d6308
No runtime reads of experiment files or opponent private state.
"""

NAMES = ('eco3_t1', 'eco5_t1', 'eco5_t3', 'eco6_t5', 'gun_t3', 'heavy_t4', 'mixed5', 'rush_t1', 'rush_t2', 'rush_t3', 'splash3_t4', 'splash_t2')

PAYOFFS = {
    'eco3_t1': (1, 1, 2, 2, 0, 2, 2, 1, 2, 2, 0, 0),
    'eco5_t1': (1, 1, 2, 2, 0, 2, 2, 1, 2, 2, 0, 0),
    'eco5_t3': (0, 0, 1, 1, 2, 2, 1, 0, 2, 2, 2, 1),
    'eco6_t5': (0, 0, 1, 1, 2, 2, 1, 0, 2, 2, 2, 1),
    'gun_t3': (2, 2, 0, 0, 1, 2, 0, 2, 2, 2, 1, 0),
    'heavy_t4': (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    'mixed5': (0, 0, 1, 1, 2, 2, 1, 0, 2, 2, 2, 1),
    'rush_t1': (1, 1, 2, 2, 0, 2, 2, 1, 2, 2, 0, 0),
    'rush_t2': (0, 0, 0, 0, 0, 2, 0, 0, 1, 2, 0, 0),
    'rush_t3': (0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0),
    'splash3_t4': (2, 2, 0, 0, 1, 2, 0, 2, 2, 2, 1, 2),
    'splash_t2': (2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 0, 1),
}

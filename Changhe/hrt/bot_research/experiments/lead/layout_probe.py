"""Quick layout probe: route length and per-copy splash damage for template mazes."""
from bot_research.harness import gamekit as gk
from td_game.config import balanced_config

CFG = balanced_config().to_dict()
RULES = gk.Rules(CFG["minions"], CFG["turrets"], CFG["wall_cost"], 250, 12, 20, 15, 1, 5, 800, 50)


def barrier(y, gap):
    return [(x, y) for x in range(12) if x != gap]


def show(walls, splashes, label):
    b = [{"x": x, "y": y, "type": "wall"} for x, y in walls] + [{"x": x, "y": y, "type": "splash"} for x, y in splashes]
    blocked = gk.cells_of(b)
    path = gk.route(blocked)
    if path is None:
        print(label, "BLOCKED")
        return
    prof = gk.splash_profile(path, b, RULES)
    print(f"{label}: L={len(path)-1} S={sum(prof)} walls={len(walls)} splash={len(splashes)}")


B1, B2, B3, B4, B5 = barrier(1, 11), barrier(3, 0), barrier(5, 11), barrier(7, 0), barrier(9, 11)
show(B1 + B2 + B3 + B4, [], "B1-4")
show(B1 + B2 + B3 + B4 + B5, [], "B1-5")
show(B3 + B4, [], "B3-4")
for sx in range(1, 11):
    show(B3 + B4, [(sx, 1)], f"B3-4 + splash ({sx},1)")
show([c for c in B1 if c != (10, 1)] + B2, [(10, 1)], "B1-(10,1) + B2 + splash(10,1)")
# vertical snake in bottom rows 8..11 after B1-B4
vs = []
for i, x in enumerate(range(1, 11, 2)):
    ys = [9, 10, 11] if i % 2 == 0 else [8, 9, 10]
    vs += [(x, y) for y in ys]
show(B1 + B2 + B3 + B4 + vs, [], "B1-4 + vertical bottom")
vs2 = []
for i, x in enumerate(range(1, 11, 2)):
    ys = [8, 9, 10] if i % 2 == 0 else [9, 10, 11]
    vs2 += [(x, y) for y in ys]
show(B1 + B2 + B3 + B4 + vs2, [], "B1-4 + vertical bottom v2")


def adjacency_table(walls):
    """Per-cell adjacency (route cells at indices 0..L-1 within Chebyshev 1) for a full wall layout."""
    blocked = set(walls)
    path = gk.route(blocked)
    idx = set(path[:-1])
    table = {}
    for c in walls:
        table[c] = sum(1 for n in gk.neighbors8(c) if n in idx)
    return table, len(path) - 1


FULL = B1 + B2 + B3 + B4 + vs
tab, L = adjacency_table(FULL)
print("full layout L", L)
for y in range(12):
    print(" ".join(str(tab[(x, y)]) if (x, y) in tab else "." for x in range(12)))
# reserve slots: per barrier the k cells nearest the gap
for k in (3, 5, 6, 7):
    R = []
    for row, gap in ((1, 11), (3, 0), (5, 11), (7, 0)):
        order = sorted([c for c in tab if c[1] == row], key=lambda c: abs(c[0] - gap))
        R += order[:k]
    walls = [c for c in FULL if c not in R]
    blocked = set(walls)
    path = gk.route(blocked)
    adj = sum(tab[c] for c in R)
    print(f"k={k}: reserved {len(R)} adj sum {adj} (S if all built {adj*10}); L with holes {len(path)-1}")


def evaluate(walls, splashes):
    b = [{"x": x, "y": y, "type": "wall"} for x, y in walls] + [{"x": x, "y": y, "type": "splash"} for x, y in splashes]
    path = gk.route(gk.cells_of(b))
    if path is None:
        return None
    return len(path) - 1, gk.splash_total(path, b, RULES)


def greedy_order(F, W, weight_path=2):
    built = []
    seq = []
    remaining = list(F)
    while remaining:
        best = None
        for c in remaining:
            r = evaluate(W, built + [c])
            if r is None:
                continue
            L, S = r
            score = S + weight_path * L
            if best is None or score > best[0]:
                best = (score, c, L, S)
        built.append(best[1])
        remaining.remove(best[1])
        seq.append((best[1], best[2], best[3]))
    return seq


print("--- option A: F = B1,B2 interiors + 6 snake cells")
snake_F = [(5, 9), (3, 10), (7, 10), (3, 9), (7, 9), (5, 10)]
F_A = [c for c in B1 + B2 if tab.get(c, 0) >= 6] + snake_F
W_A = [c for c in FULL if c not in F_A]
print("start", evaluate(W_A, []), "nF", len(F_A), "nW", len(W_A))
for c, L, S in greedy_order(F_A, W_A):
    print(c, L, S, end="; ")
print()
print("--- option B: F = B1,B2,B3 best 25")
cand = sorted([c for c in B1 + B2 + B3 if tab.get(c, 0) >= 6], key=lambda c: -tab[c])[:25]
W_B = [c for c in FULL if c not in cand]
print("start", evaluate(W_B, []), "nF", len(cand), "nW", len(W_B))
for c, L, S in greedy_order(cand, W_B):
    print(c, L, S, end="; ")
print()

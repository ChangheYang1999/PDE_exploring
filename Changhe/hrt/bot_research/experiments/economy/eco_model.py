"""Closed-form and recurrence economy model (no engine needed).

Rules used (bundled config, read from td_game/config.py and engine.py):
start gold 100; factory cost 20, income 15 per factory per round, paid after
combat of every round from the purchase round on; path income 1 per route
step per round (22 on the empty map, 66 on the full 5-row serpentine);
50 rounds. Gold received after combat of round 50 is never usable.

Usage: python3 eco_model.py   (prints the tables used in notes/economy.md)
"""
from __future__ import annotations


def pure_eco(rounds=12, L=22, start=100, fcost=20, finc=15, cap=None, frac=1.0):
    """Every round spend `frac` of gold on factories (optionally capped).

    Returns rows (round, gold_at_decision, factories_after_buy, cumulative_income).
    """
    gold, fac, cum = start, 0, 0
    rows = []
    for r in range(1, rounds + 1):
        n = int(gold * frac) // fcost
        if cap is not None:
            n = min(n, cap)
        rows.append((r, gold, fac + n, cum))
        gold -= n * fcost
        fac += n
        inc = finc * fac + L
        gold += inc
        cum += inc
    return rows


def factory_return(r, rounds=50, fcost=20, finc=15):
    """Usable gold returned by one factory bought in round r, net of its cost."""
    return finc * (rounds - r) - fcost


def main():
    print("Usable net return of one factory bought in round r: 15*(50-r) - 20")
    for r in (1, 10, 20, 30, 40, 45, 47, 48, 49, 50):
        print(f"  r={r:2d}: {factory_return(r):5d}")
    print()
    print("Pure factory compounding, empty-map route L=22 (gold at decision time)")
    print(" r  gold  factories")
    for row in pure_eco(12):
        print(f"{row[0]:2d} {row[1]:6d} {row[2]:6d}")
    print()
    print("Same with route L=66 from round 1 (needs 55 walls; not affordable with factories in r1)")
    for row in pure_eco(10, L=66):
        print(f"{row[0]:2d} {row[1]:6d} {row[2]:6d}")
    print()
    print("Fraction f of gold to factories each round, gold at decision in rounds 4..9")
    for f in (1.0, 0.75, 0.5, 0.25):
        g = [row[1] for row in pure_eco(9, frac=f)]
        print(f"  f={f:4.2f}: " + " ".join(f"{x:6d}" for x in g[3:]))
    print()
    print("Growth factor per round of pure compounding: gold(r+1)/gold(r)")
    rows = pure_eco(14)
    for a, b in zip(rows, rows[1:]):
        print(f"  {a[0]:2d}->{b[0]:2d}: {b[1] / max(1, a[1]):.3f}")
    print()
    print("Pure compounding capped at 40 factories per round (harness baselines)")
    for row in pure_eco(20, cap=40)[::2]:
        print(f"{row[0]:2d} {row[1]:7d} {row[2]:6d}")


if __name__ == "__main__":
    main()

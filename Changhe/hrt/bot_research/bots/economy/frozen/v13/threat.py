"""Attack-package families and worst-case leak evaluation.

A defender that sees the attacker's gold G and active roster knows every
purchase the attacker can make this round. New entries are appended after the
attacker's active entries, so their spawn ticks are fixed by the roster size.
The families below are a heuristic cover of the attacker's options (pure
tiers, cheap screens in front of heavy copies, greedy mixes, reversed mixes).
They give a lower bound on the attacker's best damage, not a proof of safety.
"""
from __future__ import annotations

from .fastsim import simulate

TIERS = ("tier1", "tier2", "tier3", "tier4", "tier5")


def active_types(roster, round_number):
    out = []
    for e in roster:
        exp = e.get("expires_after_round")
        if e["bought_round"] <= round_number and (exp is None or round_number <= exp):
            out.append(e["type"])
    return out


def greedy_mix(gold, minions, order, cap):
    out = []
    for t in order:
        c = minions[t]["cost"]
        while gold >= c and len(out) < cap:
            out.append(t)
            gold -= c
    return out


def packages(gold, minions, cap=400):
    """Candidate new-purchase lists (in purchase order) for an attacker with gold."""
    pk = [[]]
    seen = set()
    for t in TIERS:
        n = min(cap, gold // minions[t]["cost"])
        if n > 0:
            pk.append([t] * n)
    desc = list(reversed(TIERS))
    pk.append(greedy_mix(gold, minions, desc, cap))
    # cheap screens in front of heavy copies
    c1 = minions["tier1"]["cost"]
    for t in ("tier2", "tier3", "tier4", "tier5"):
        ct = minions[t]["cost"]
        for f in (1, 2, 3, 5, 8):
            rest = gold - f * c1
            if rest >= ct:
                n = min(cap - f, rest // ct)
                body = [t] * n
                rem = rest - n * ct
                tail = greedy_mix(rem, minions, desc, cap - f - n)
                pk.append(["tier1"] * f + body + tail)
        # heavy first then cheap tail
        n = gold // ct
        if n:
            n = min(n, cap)
            rem = gold - n * ct
            pk.append([t] * n + greedy_mix(rem, minions, ["tier1"], cap - n))
            # one fewer heavy, rest cheap swarm
            if n >= 1:
                rem2 = gold - (n - 1) * ct
                pk.append([t] * (n - 1) + greedy_mix(rem2, minions, ["tier2", "tier1"], cap - n + 1))
    out = []
    for p in pk:
        key = tuple(p)
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


def worst_case(model, existing, gold, rules, cap=400, pkgs=None):
    """Max (damage, hits, package) over the families for this defender model."""
    minions = rules["minions"]
    if pkgs is None:
        pkgs = packages(gold, minions, cap)
    best = (-1, 0, None)
    for p in pkgs:
        hits, dmg = simulate(model, existing + p, rules)
        if dmg > best[0]:
            best = (dmg, hits, p)
    return best

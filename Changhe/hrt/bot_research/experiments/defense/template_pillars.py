"""'Independent pillars' templates: early slots = U-turn cells of complete lines; bulk slots in rows 1/3 (or 5/7)."""
import sys
from bot_research.experiments.defense.template_eval import report, lead_template


def snake():
    out = []
    for i, x in enumerate(range(1, 11, 2)):
        out += [(x, y) for y in ((9, 10, 11) if i % 2 == 0 else (8, 9, 10))]
    return out


def pillars_template(bulk_rows=(1, 3), n_bulk_per_row=8, extra_snake=((1, 9), (3, 10))):
    rows = {1: 11, 3: 0, 5: 11, 7: 0}
    cells = [(x, y) for y, gap in rows.items() for x in range(12) if x != gap] + snake()
    pillars = [(10, 1), (1, 3), (10, 5), (1, 7)]
    snake_u = [(1, 10), (3, 9), (5, 10), (7, 9), (9, 10)]
    slots = pillars + snake_u
    for y in bulk_rows:
        gap = rows[y]
        # bulk slots next to the pillar end of the row
        xs = list(range(10 - n_bulk_per_row, 10)) if gap == 11 else list(range(2, 2 + n_bulk_per_row))
        slots += [(x, y) for x in xs if (x, y) not in slots]
    slots += list(extra_snake)
    sset = set(slots)
    walls = [c for c in cells if c not in sset]
    return tuple(walls), tuple(slots)


if __name__ == "__main__":
    report("pillars: bulk rows 1,3 (8 each)", *pillars_template())
    report("pillars: bulk rows 5,7 (8 each)", *pillars_template(bulk_rows=(5, 7)), show_map=False)
    report("pillars: bulk rows 1,3 (7 each) + 4 snake extras", *pillars_template(n_bulk_per_row=7, extra_snake=((1, 9), (3, 10), (5, 9), (7, 10))), show_map=False)
    report("pillars: bulk rows 1,3,5 (5,5,6)", *pillars_template(bulk_rows=(1, 3, 5), n_bulk_per_row=5, extra_snake=((1, 9),)), show_map=False)

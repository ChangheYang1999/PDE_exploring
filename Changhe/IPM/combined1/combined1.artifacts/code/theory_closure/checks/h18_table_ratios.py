# H18 falsification check (c1-coord 13:41Z item 11): recompute every ratio of the THEORY_FINAL section 7 distance table
# from the displayed distance floor and the family ceilings, with exact fractions. A displayed ratio is accepted only if
# it does not exceed the exact ratio (it is a lower bound) and equals the exact ratio rounded down at the displayed
# precision. Ceilings (upper bounds): TB-sharp 3.7930e-6, sharpw 2.8496e-6, graded 25/54684.
# Usage: python3 checks/h18_table_ratios.py [FILE]; FILE defaults to ../../THEORY_FINAL.md from this script.
import os, re, sys
from fractions import Fraction as F
from math import floor

CEIL = [F('3.7930e-6'), F('2.8496e-6'), F(25, 54684)]


def disp_floor(x, shown):
    # round x down at the precision of the displayed string shown (plain decimal or mantissa e exponent)
    m = re.fullmatch(r'(\d+)(?:\.(\d+))?(?:e(\d+))?', shown)
    nd = len(m.group(2) or '') - int(m.group(3) or 0)
    sc = F(10) ** nd
    return F(floor(x * sc), sc)


rows = bad = 0
path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                                           'THEORY_FINAL.md')
for line in open(path):
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(c) != 6 or not re.match(r'\d', c[1]) or c[2] == '-':
        continue
    d = F(c[1].split()[0])
    for k in range(3):
        r = d / CEIL[k]
        shown = F(c[2 + k])
        ok = shown <= r and shown == disp_floor(r, c[2 + k])
        rows += 1
        bad += not ok
        if not ok:
            print('MISMATCH', c[0], k, c[2 + k], float(r))
print(f'ratios checked {rows}, mismatches {bad}')
assert rows > 0 and bad == 0
print('ALL DISPLAYED RATIOS ARE EXACT FLOORS')

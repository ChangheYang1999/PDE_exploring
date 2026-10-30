# Pre-freeze consistency check of THEORY_FINAL against the closure matrix: every reference "C1-N1-0XX ... row N" or
# "C1-N1-0XX ... rows N and M" (also with the short name 0XX) in THEORY_FINAL must point to a matrix row whose FW or
# candidate cell names that snapshot. Text is matched after collapsing whitespace; a reference is the first "row(s)"
# within 160 characters of the name with no '.' or ';' in between. Reading only; no number is computed.
# Usage: python3 checks/row_refs.py [THEORY_FINAL [MATRIX]]; the defaults, from this script, are ../../THEORY_FINAL.md
# and checks/data/closure_matrix_v170.md (frozen copy of c1-shared/closure_matrix.md v170, 18:22Z, read at 18:25Z for the
# final THEORY_FINAL; drafts 57 to 64 used the v157 copy, draft 56 the v155 copy (v135 to v153 stored as .gz), draft 55 the v153 copy, draft 54 the v151 copy, draft 53 the v146 copy; until draft 52 the default was the live
# ../../../c1-shared/closure_matrix.md).
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'THEORY_FINAL.md')
CM = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'data', 'closure_matrix_v170.md')
cand = {}
for line in open(CM):
    m = re.match(r'^\| *(\d+) \|', line)
    if m:
        c = [x.strip() for x in re.split(r'(?<!\\)\|', line)[1:-1]]
        cand[int(c[0])] = c[1] + ' || ' + c[2]
txt = re.sub(r'\s+', ' ', open(TF).read())
bad = n = 0
for m in re.finditer(r'(C1-N1-0\d\d|\b0[0-2]\d\b)[^.;]{0,160}?\brows? (\d+)(?: and (\d+))?', txt):
    name = m.group(1)
    name = name if name.startswith('C1') else 'C1-N1-' + name
    for r in (m.group(2), m.group(3)):
        if r is None:
            continue
        r = int(r)
        n += 1
        if r not in cand or name not in cand[r]:
            bad += 1
            print('CHECK', name, 'row', r, '|', cand.get(r, 'NO ROW')[:80], '| ctx:', m.group(0)[:140])
print('matrix rows read', len(cand))
print('references checked', n, 'mismatches', bad)

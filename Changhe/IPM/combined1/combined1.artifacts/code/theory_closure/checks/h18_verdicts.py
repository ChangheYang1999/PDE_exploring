# H18 check (c1-t1): the candidate verdicts of THEORY_FINAL section 0 item 1 and section 7 against the closure matrix,
# row by row. Usage: python3 checks/h18_verdicts.py [THEORY_FINAL [MATRIX]]; the defaults, from this script, are
# ../../THEORY_FINAL.md and checks/data/closure_matrix_v170.md (frozen copy of c1-shared/closure_matrix.md v170,
# 18:22Z, sha256 8bf325ea...553787ac, read at 18:25Z for the final THEORY_FINAL; drafts 57 to 64 used the v157 copy, sha256
# c94780ad...cc4ed7c4; draft 56 used the v155 copy, draft 55 the v153 copy, draft 54 the v151 copy, draft 53 the v146 copy, draft 52 the v140 copy, and the H18 runs of drafts
# 46 to 49 the v135, v137, v138 and v139 copies in checks/data (v135 to v153 stored as .gz; restore with gunzip -k), with the same result for the claims of those drafts). The hand-coded claims of Part B and Part D are
# those of THEORY_FINAL drafts 48 to 50: those of draft 46 with 017 and row 106 added to the dyadic list.
# Part A: verdict class of every matrix row whose candidate column starts with a candidate ID (RULED OUT / OPEN / other).
# Part B: the claims of section 0 item 1 and section 7 (hand-coded below from the text) against Part A.
# Part C: sentences of THEORY_FINAL (outside tables) that put a candidate next to OPEN while every matrix row of that
#         candidate is RULED OUT, or next to RULED OUT while every row is OPEN; printed for reading, not auto-failed.
# Part D: scope. A row RULED OUT only because the residual is not in the forcing space is framework inapplicability,
#         not an exclusion of exact solutions (matrix status key; c1-t4 H18_PREPARATION step 7). Every row of 001 is of
#         that kind, so THEORY_FINAL must not put 001 in a sweeping "no exact solution" list; 002 to 004 are covered
#         beyond their specified balls only through the section 7 distance rows (T4-068), which must be present.
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'THEORY_FINAL.md')
CM = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'data', 'closure_matrix_v170.md')
rows = {}
for l in open(CM):
    m = re.match(r'^\| *(\d+) \|', l)
    if m:
        c = [x.strip() for x in re.split(r'(?<!\\)\|', l)[1:-1]]
        rows[int(c[0])] = c
REF = {'S131': 'C1-BASE-S131', 'd2': 'C1-A2-d2', 'Mpen2': 'C1-A2-Mpen2', 'b6': 'C1-A2-b6'}
for k in range(1, 29):   # draft 53: 028 (rows 107, 108) added
    REF['%03d' % k] = 'C1-N1-%03d' % k
def vclass(v):
    if v.startswith('RULED OUT') or v.startswith('Mpen2: RULED OUT') or v.startswith('Stated version (s = 2^-17, R = 2^-14): RULED OUT'):
        return 'RULED OUT'
    if v.startswith('OPEN'):
        return 'OPEN'
    return 'OTHER:' + v[:40]
by = {}
for r, c in sorted(rows.items()):
    head = [x.strip().split(' ')[0] for x in c[2].split('(')[0].split(',')]
    for k, name in REF.items():
        if any(x == name or x.startswith(name + '-') for x in head):
            by.setdefault(k, []).append((r, 'DYADIC' if 'DYADIC' in c[1] else ('WLOW' if 'weighted L^2 low' in c[1] else 'BALL'), vclass(c[-1])))
fails = 0; checks = 0
def claim(ok, msg):
    global fails, checks
    checks += 1
    if not ok:
        fails += 1
        print('FAIL', msg)
print('Part A: rows per candidate')
for k in REF:
    print(' ', k, by.get(k, 'NO ROWS'))
# Part B claims (section 0 item 1, section 7 table and bullets of THEORY_FINAL)
ruled = ['S131', 'd2', 'Mpen2', 'b6'] + ['%03d' % k for k in range(1, 27) if k != 11]
for k in ruled:
    rs = by.get(k, [])
    claim(len(rs) > 0, k + ': no matrix row')
    for (r, kind, v) in rs:
        if k == 'S131' and kind == 'WLOW':
            claim(v == 'OPEN', 'row 34 (state 131, weighted low space) should be OPEN, is ' + v)
        else:
            claim(v == 'RULED OUT', '%s row %d (%s) is %s, THEORY_FINAL says RULED OUT' % (k, r, kind, v))
for k in ['011', '027', '028']:
    rs = by.get(k, [])
    claim(len(rs) > 0, k + ': no matrix row')
    for (r, kind, v) in rs:
        claim(v == 'OPEN', '%s row %d is %s, THEORY_FINAL says OPEN / untested' % (k, r, v))
dy = sorted(k for k in REF for (r, kind, v) in by.get(k, []) if kind == 'DYADIC' and v == 'RULED OUT')
# draft 48 adds 017 (matrix v138 row 106, N4-389) to the dyadic list of section 0 item 1
claim(dy == sorted(['S131', 'd2', '007', '008', '009', '010', '015', '016', '017']), 'dyadic RULED OUT set ' + str(dy))
dyrows = sorted(r for k in REF for (r, kind, v) in by.get(k, []) if kind == 'DYADIC')
claim(dyrows == [58, 59, 64, 73, 74, 79, 98, 105, 106], 'dyadic rows ' + str(dyrows))
# section 7 table: each certified-distance row names a candidate whose matrix rows are all RULED OUT
txt = open(TF).read()
sec7 = txt.split('\n## 7. Candidates')[1].split('\n## 8.')[0]
for l in sec7.split('\n'):
    m = re.match(r'^\| (\d\d\d|d2|Mpen2|state 131) \| ([^|]+)\|', l)
    if not m:
        continue
    k = {'state 131': 'S131'}.get(m.group(1), m.group(1))
    cert = not m.group(2).strip().startswith('none certified')
    vs = [v for (r, kind, v) in by.get(k, []) if kind == 'BALL']
    if cert:
        claim(vs and all(v == 'RULED OUT' for v in vs), 'section 7 row %s has a distance but matrix ball rows %s' % (k, vs))
    else:
        claim(vs and all(v == 'OPEN' for v in vs), 'section 7 row %s has no certified value but matrix ball rows %s' % (k, vs))
print('Part B: claims checked', checks, 'failures', fails)
# Part C: sentence scan
flat = re.sub(r'\s+', ' ', '\n'.join(l for l in txt.split('\n') if not l.startswith('|')))
allr = {k for k in REF if by.get(k) and all(v == 'RULED OUT' for (r, kind, v) in by[k] if kind != 'WLOW')}
allo = {k for k in REF if by.get(k) and all(v == 'OPEN' for (r, kind, v) in by[k])}
nC = 0
for s in re.split(r'(?<=[.;])\s', flat):
    for k in ['%03d' % j for j in range(1, 29)]:
        if not re.search(r'(C1-N1-|\b)' + k + r'\b', s):
            continue
        s2 = re.sub(r'except (C1-N1-)?' + k + r'\b', 'except X', s)
        if k in allr and re.search(r'(?<![-\w])%s\b[^.;]{0,40}\b(is|stays|remains) OPEN' % k, s2):
            nC += 1; print('C-OPEN?', k, '|', s[:260])
        if k in allo and re.search(r'(?<![-\w])%s\b[^.;]{0,40}\bis RULED OUT' % k, s2):
            nC += 1; print('C-RULED?', k, '|', s[:260])
print('Part C: sentences flagged for reading', nC)
# Part D
nD0 = checks
# the errata of section 11 quote the old wording, so the sweeping-list tests read the text outside section 11
body = re.sub(r'\s+', ' ', txt.split('\n## 11.')[0] + txt.split('\n## 12.')[1])
inapp = lambda r: 'residual not in the forcing space' in rows[r][-1] or 'residual not in L^2' in rows[r][-1]
claim(all(inapp(r) for (r, kind, v) in by['001']), '001 has a row that is not residual nonmembership')
claim(not re.search(r'C1-N1-001 to C1-N1-02\d', body), 'sweeping list C1-N1-001 to C1-N1-02N still present')
claim(not re.search(r'snapshot through 02\d except', body), 'sweeping list "through 02N except" still present')
for k, d in [('002', '1.56361352'), ('003', '0.22988134'), ('004', '1.40009623')]:
    claim(re.search(r'^\| %s \| %s \(N4-070, T4-068' % (k, re.escape(d)), sec7, re.M) is not None,
          'section 7 row %s with the T4-068 distance %s missing' % (k, d))
# draft 53 (T4-471, matrix v140 row 35): row 35 records framework inapplicability and the affine L^2 exclusion of 001
claim('C1-N1-001 is RULED OUT as framework inapplicability' in flat and
      'by the stronger affine L^2 exclusion at every real c' in flat, 'separate 001 statement missing')
print('Part D: scope claims checked', checks - nD0)
print('RESULT', 'PASS' if fails == 0 else 'FAIL')

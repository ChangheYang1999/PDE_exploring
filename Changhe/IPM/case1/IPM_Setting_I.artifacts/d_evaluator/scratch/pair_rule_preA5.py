"""The lead's 12:02Z reading rule (NOTES_FOR_TEAM item 3) on my evaluator, for a fixed-c_l fit A and a free fit B.
Per configuration (audit logs runs/audit/<tag>_N*_q*_R7.652e6.log present for both): whole-box N_f maximum, N_v maximum
over r <= 1000 and over r > 1000, c_l (identity on my inverse), h(P) - 1; the 857-label J (runs/audit/<tag>_N16875_q384_
R7.652e6_jd2.json). 'Beyond the configuration spread': A's N_v counts as higher only if A - B exceeds the spread of B's
values over the configurations. Usage: python3 pair_rule.py tagA tagB"""
import sys, json, re, glob, os
import numpy as np
A, B = sys.argv[1], sys.argv[2]
inner = ['r<=0.1', '0.1<=r<=2', '2<=r<=10', '10<=r<=100', '100<=r<=1000']


def read(f):
    L = open(f).read().splitlines()
    head = next(json.loads(l) for l in L if l.startswith('{"file"'))
    rows = {}
    for l in L:
        m = re.match(r'\s+(\S+)\s+flux max (\S+) rms (\S+) \| N_v max (\S+) rms (\S+) \| at r (\S+) th (\S+)', l)
        if m: rows[m.group(1)] = [float(x) for x in m.groups()[1:]]
    return dict(cl=head['c_l'], hP=head['hP'] - 1, Nf=rows['all'][0], Nf_at=(rows['all'][4], rows['all'][5]),
                Nv_in=max(rows[k][2] for k in inner), Nv_out=rows['1000<=r<=R'][2], NfP=rows['|X-P|<0.5'][0],
                Nf210=rows['2<=r<=10'][0], Nf10100=rows['10<=r<=100'][0])


cfgs = sorted({os.path.basename(f)[len(A) + 1:] for f in glob.glob('runs/audit/%s_N*_q*_R7.652e6.log' % A)}
              & {os.path.basename(f)[len(B) + 1:] for f in glob.glob('runs/audit/%s_N*_q*_R7.652e6.log' % B)})
def ok(f):
    try: read(f); return True
    except Exception: return False


cfgs = [c for c in cfgs if ok('runs/audit/%s_%s' % (A, c)) and ok('runs/audit/%s_%s' % (B, c))]  # skip logs still being written
V = {t: [read('runs/audit/%s_%s' % (t, c)) for c in cfgs] for t in (A, B)}
print('configurations:', [c.replace('_R7.652e6.log', '') for c in cfgs])
for key in ('Nf', 'NfP', 'Nf210', 'Nf10100', 'Nv_in', 'Nv_out', 'cl', 'hP'):
    a = np.array([v[key] for v in V[A]]); b = np.array([v[key] for v in V[B]])
    fmt = '%.9f' if key == 'cl' else '%.3e'
    print('%-8s %s: %s | %s: %s' % (key, A, ' '.join(fmt % x for x in a), B, ' '.join(fmt % x for x in b)),
          '' if key in ('cl', 'hP') else '| ratio A/B %s | spread B %.2e' % (' '.join('%.3f' % x for x in a / b), b.max() - b.min()))
print('N_f maximum at (r, theta):', A, [v['Nf_at'] for v in V[A]], B, [v['Nf_at'] for v in V[B]])
J = {}
for t in (A, B):
    f = 'runs/audit/%s_N16875_q384_R7.652e6_jd2.json' % t
    if os.path.exists(f):
        d = json.load(open(f)); sp = d['summary']['spread']; eps = d['summary']['eps_P']
        Jm = np.array([r['J'] for r in d['rows']], float); A737 = np.array([r['fam'] == 'A' for r in d['rows']])
        J[t] = 'eps 0.03 / 0.01: 857 %.3e / %.3e, 737 %.3e / %.3e' % (sp[eps.index(0.03)], sp[eps.index(0.01)],
               np.nanmax(Jm[A737, 5]) - np.nanmin(Jm[A737, 5]), np.nanmax(Jm[A737, 6]) - np.nanmin(Jm[A737, 6]))
for t in J: print('J', t, J[t])
nf = all(a['Nf'] < b['Nf'] for a, b in zip(V[A], V[B]))
sp_in = max(v['Nv_in'] for v in V[B]) - min(v['Nv_in'] for v in V[B]); sp_out = max(v['Nv_out'] for v in V[B]) - min(v['Nv_out'] for v in V[B])
nv_in = all(a['Nv_in'] - b['Nv_in'] <= sp_in for a, b in zip(V[A], V[B]))
nv_out = all(a['Nv_out'] - b['Nv_out'] <= sp_out for a, b in zip(V[A], V[B]))
print('rule: N_f(A) < N_f(B) on every configuration:', nf, '| N_v r<=1000 not higher beyond spread:', nv_in,
      '| N_v r>1000 not higher beyond spread:', nv_out)

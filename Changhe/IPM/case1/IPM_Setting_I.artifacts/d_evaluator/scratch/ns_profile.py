"""Verifier scratch (shift 7): the nested pair 56 nst24g (c_l 5.6004662) / 57 nsn8g (5.5683739) on 375 x m <= 200 (lead NOTES
2026-10-19T03:54:45Z), against F3 = c6gF and X3 = c6g on my audits N11250 q384, N16875 q512 (A5 regions), J at N16875 q384.
L2 of X3 from its chain log; L2 of F3 = 1.6641961e-6 as quoted by the lead (its chain log is not in leadcode/gpu/c6gF).
Readings: item 3 (i) Q_200 = L2(56) / L2(F3): flattened (< 2 percent over the last 1000 iterations) and Q_200 >= 3.05 ->
"favours an isolated profile at the attained level"; Q_200 <= 1.36 -> "favours a family through the candidate"; otherwise, or
not flattened (either case) -> "undecided". (iii) interval rule against F3 (NOTES 00:25:51Z item 2): (a) L2, whole-box N_f within 30
percent, |h(P) - 1| <= 1e-6; (b) flattened and near-P N_f >= 2 x F3's on each configuration; (c) otherwise.
Usage: python3 ns_profile.py"""
import json, os
G = ''
D = 'runs/audit/'
cfgs = ['N11250_q384', 'N16875_q512']
L2F3 = 1.6641961e-6


def l2(tag):
    f = G + tag + '/' + tag + '.log'
    if not os.path.exists(f): return None
    ch = {}; done = False; inner = 2500
    for l in open(f):
        if not l.startswith('{'): continue
        o = json.loads(l)
        if o.get('event') == 'check': ch[inner * (o['outer'] - 1) + o['it']] = o['actual']
        if o.get('event') == 'end': done = True
    if not ch: return None
    last = max(ch); prev = [k for k in sorted(ch) if k <= last - 1000]
    return ch[last], last, ((ch[last] / ch[prev[-1]] - 1) if prev else float('nan')), done


def aud(tag, c):
    f = D + '%s_%s_R7.652e6.json' % (tag, c)
    if not os.path.exists(f): return None
    d = json.load(open(f)); r = {x['region']: x for x in d['residual']}
    return dict(wbA=r['all,ya>=0.006']['flux_max'], nv=r['r<=1000,ya>=0.006']['Nv_max'], nP=r['|X-P|<0.5']['flux_max'],
                far=r['1000<=r<=R']['Nv_max'], h=d['vcand']['hP'] - 1, cl=d['vcand']['c_l'], xs=d['vcand']['x_star'])


def jay(tag):
    f = D + '%s_N16875_q384_R7.652e6_jd2.json' % tag
    if not os.path.exists(f): return None
    s = json.load(open(f))['summary']['spread']; return s[5], s[6]


X3 = dict(L2=l2('c6g'), J=jay('c6g'), a={c: aud('c6g', c) for c in cfgs})
F3 = dict(L2=(L2F3,), J=jay('c6gF'), a={c: aud('c6gF', c) for c in cfgs})
LF = l2('c6gF')
print('X3 L2 %.7e at %d its (lead quotes 1.6192702e-6); F3 L2 %.7e (quoted); F3 chain log %s' % (X3['L2'][0], X3['L2'][1], L2F3, ('%.10e at %d its' % (LF[0], LF[1])) if LF else 'none'))
for tag in ['nst24g', 'nsn8g']:
    L = l2(tag)
    if L is None: print('%s: no chain log' % tag); continue
    q = L[0] / L2F3; qx = L[0] / X3['L2'][0]
    print('== %-7s L2 %.6e  /F3 %.3f  /X3 %.3f  at %d its, last 1000 its %+.3f%%, end %s' % (tag, L[0], q, qx, L[1], 100 * L[2], L[3]))
    okA = abs(q - 1) <= 0.3; okB = abs(L[2]) < 0.02; nb = []; hmax = 0.0; have = True
    for c in cfgs:
        a = aud(tag, c); b = F3['a'][c]; x = X3['a'][c]
        if a is None: print('   %s: audit missing' % c); have = False; continue
        hmax = max(hmax, abs(a['h'])); okA = okA and abs(a['wbA'] / b['wbA'] - 1) <= 0.3; nb.append(a['nP'] / b['nP'] >= 2)
        print('   %s wholebox A5 %.4e (F3 %.3f, X3 %.3f)  near P %.4e (F3 %.3f, X3 %.3f)  Nv r<=1000 %.3e (F3 %.3f, X3 %.3f)  far %.3e  h(P)-1 %+.2e  c_l %.10f  x* %.7f' % (
            c, a['wbA'], a['wbA'] / b['wbA'], a['wbA'] / x['wbA'], a['nP'], a['nP'] / b['nP'], a['nP'] / x['nP'],
            a['nv'], a['nv'] / b['nv'], a['nv'] / x['nv'], a['far'], a['h'], a['cl'], a['xs']))
    j = jay(tag)
    if j: print('   J eps 0.03 %.4e (F3 %.3f, X3 %.3f)  eps 0.01 %.4e (F3 %.3f, X3 %.3f)' % (
        j[0], j[0] / F3['J'][0], j[0] / X3['J'][0], j[1], j[1] / F3['J'][1], j[1] / X3['J'][1]))
    if not have: continue
    okA = okA and hmax <= 1e-6
    rd = '(a) not determined at this level' if okA else ('(b) excluded at this level' if (okB and all(nb)) else
                                                         '(c) undecided at the 375 x m <= 200 level after its iterations')
    if not L[3]: rd += ' (PROVISIONAL: run not ended)'
    print('   interval reading vs F3: %s  [|h(P)-1| max %.2e, flattened %s, near P >= 2 x F3 %s]' % (rd, hmax, okB, nb))
    if tag == 'nst24g':
        qr = ('undecided (not flattened)' if not okB else ('favours an isolated profile at the attained level' if q >= 3.05 else
              ('favours a family through the candidate' if q <= 1.36 else 'undecided')))
        print('   item 3 (i): Q_200 = %.3f against Q_150 = 2.036: %s' % (q, qr))
    else:
        print('   item 3 (ii): L2(57)/L2(X3) = %.3f against L2(53)/L2(X2) = 0.771' % qx)

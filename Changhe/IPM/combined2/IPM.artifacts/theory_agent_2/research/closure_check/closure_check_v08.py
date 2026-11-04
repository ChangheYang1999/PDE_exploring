"""closure_check (theory_agent_2, 2026-11-04, version 08): the final closure check of theory_audit's SOURCE013_CHAIN_CONDITIONS_v01,
items 8 and 9, as a conditional program (coordinator 07:08Z item 3(a)). Text: notes/T2_CLOSURE_CHECK_v08.md.
Version 03 followed theory_audit AT2352 to AT2357 and AT2333 to AT2336: H4 reading (ii) (AT2333), same-input transcription
(row N4, AT2354), the combined criterion at the original rate (row J1) kept apart from the companion (row G5, AT2356),
and, after AT2364 to AT2366, row T1: an upper stand-in must not lie below a certified lower of the same quantity.
Version 04 binds theory_agent_1's NEAR_CHECK_v04 (theory_agent_1 note 98; program near_check_v03.py, parameters near_params_v03.json
with the (R4) values of theory_agent_2's Proposition R4 v02, UNAUDITED; copied unchanged into nearcopy_v04/, hashes pinned in
the inputs), takes the matrix rate beta_* at the regional lower of near_params_v03.json (status REGIONAL) with a
level for every region of the cover (row A1), adds beta_* and eps_rest to the same-input row N4, and counts the
statuses UNAUDITED, REGIONAL and STANDIN-ZERO as stand-ins. Everything else is as in version 03.
Version 05 binds theory_agent_1's NEAR_CHECK_v06 (theory_agent_1 notes 99, 100: the run of NEAR_CHECK_v05, program near_check_v03.py,
parameters near_params_v04.json with the (R4) values of Proposition R4 v01, CONFIRMED by AT2477 to AT2479; copied
unchanged into nearcopy_v05/), and renames the companion row G5 (AT2497). Everything else is as in version 04.
Version 06 binds theory_agent_1's NEAR_CHECK_v07 (theory_agent_1 note 102: program near_check_v03.py, parameters near_params_v05.json
with the (R4) values of Proposition R4 v02, CONFIRMED by AT2520 to AT2522, and the whole-plane beta_*, CONFIRMED by
AT2534 to AT2536; copied unchanged into nearcopy_v06/). The host region 7/9 <= r^2 <= 49/15 (AT2512 to AT2515) joins
the region records, so rows A1 and A1g can pass; a CONFIRMED input status of beta_*, g_* or s_* is lowered to a
stand-in when the union has a gap. Block H cites T2_H4REST_v01 and the HI' cuts of AT2564 to AT2569. Everything
else is as in version 05.
Version 07 binds theory_agent_1's NEAR_CHECK_v08 (record of 14:12Z, manifest SHA256SUMS_v08; program near_check_v03.py unchanged, parameters near_params_v06.json, which
change only D4, D5 and D6 of a_n to the certified whole-plane uppers of numerical_audit's executed near consumer, CONFIRMED
by AT2869 to AT2871; copied unchanged into nearcopy_v07/). Block H marks H-NEARU supplied. Everything else is
as in version 06.
Version 08 binds theory_agent_1's NEAR_CHECK_v09 (theory_agent_1 note 116; program near_check_v04.py, CLAIMED, with theory_audit's review pending, parameters near_params_v06.json
as in NEAR_CHECK_v08; copied unchanged into nearcopy_v08/). Its M4 term is A4c min(1024 c + M4^+(a_r), M4^+(a_n))/mu^4,
with M4^+(a_n) = ((D4 D6 + D5^2)/(2 pi))^(1/2) at D_m = D_m(a_n) (NR-25 (iii) for a_n itself; AT2871), and the
independent e_HF of row N2 uses the same minimum. Everything else is as in version 07.
It uses the printed tuple of the bound near check and recomputes its two near quantities independently as a
transcription check.
Interface (after AT2307 to AT2309, which apply to version 01 of this program as well): every value that enters a
decision is an exact rational. e_up and C_N are the printed uppers of NEAR_CHECK_v09; C0 = C_rest + C_N; D_out is a
decimal certified <= the arb ball of D; margins are exact and displayed rounded down; room = D_out - C0 rounded down;
C0/D_out rounded up; the beta_* needed is exact and displayed rounded up. Arb balls are used only inside the CE cell
and the transcription checks.
Rows and input changes (AT2354): no row is claimed monotone under a change of inputs. N2 and N3 compare this
program with NEAR_CHECK_v09 and mean something only at identical inputs, which row N4 checks; they are kept apart from
the sufficient inequalities (E2, G4, J1). When a certified bound becomes available for a stand-in, the rule is the
conservative witness: if the certified bound is at least as good as the stand-in value (an upper at most the value,
a lower at least the value), the input keeps its value, the stand-in value is itself certified and only its status
changes, so every computed row is unchanged. Any other use of a new value (a smaller upper, a larger lower, a value
outside the stand-in) is a new input set: it needs a new same-input NEAR_CHECK for the near inputs and a new run of
this program, whose rows decide.
Every input is a named parameter of inputs_v08.json with a sense (upper, lower, exact, choice) and a status. Arithmetic
is exact (Fraction) or outward arb (python-flint, 200 bits). Each check is reported as
  PASS       it holds, and every input it uses is CONFIRMED (or a choice);
  PASS-COND  it holds at the given values, but some input is a stand-in (STANDIN-FLOAT, STANDIN-TARGET,
             STANDIN-ZERO, UNAUDITED or REGIONAL), so the check proves nothing;
  FAIL       it does not hold at the given values (a failed sufficient test; it excludes nothing);
  OPEN       a premise that no computation here supplies.
The closure statement (block I) follows only if, for one case, every check of H4 reading (ii) is PASS and
every named hypothesis of block H is supplied by an accepted certificate. The CE part (block G) is theory_agent_1's
budget_013h code (ps1copy/), used unchanged.
Usage: python3 -B closure_check_v08.py [inputs.json]   (writes closure_check_v08.json next to this file)"""
import hashlib, json, math, os, sys, time
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'ps1copy', 'ps1'))
import ce_gen as CG                                    # theory_agent_1 budget_013h/ps1/ce_gen.py (imports ../hf/hfq_witness.py)
H = CG.H
from flint import arb, fmpq, ctx
ctx.prec = 200
t_start = time.time()
def A_(x): x = Fr(x); return arb(fmpq(x.numerator, x.denominator))
def fl(x): return float(x.mid())
def fmt(s, e):
    if e >= 0: return str(int(s))
    neg = s < 0; s = abs(s); ip = int(s); fp = s - ip; k = -e
    return ('-' if neg else '') + '%d.%0*d' % (ip, k, int(fp*10**k))
def lodec(x, d=10):  # a d-digit decimal certified <= x (arb), as a string
    v = fl(x.lower()); e = math.floor(math.log10(abs(v))) - d + 1 if v != 0 else -d
    s = Fr(math.floor(Fr(v)/Fr(10)**e) - 1)*Fr(10)**e
    while A_(s + Fr(10)**e) <= x: s += Fr(10)**e
    assert A_(s) <= x
    return fmt(s, e)
def updec(x, d=10):  # a d-digit decimal certified >= x (arb), as a string
    v = fl(x.upper()); e = math.floor(math.log10(abs(v))) - d + 1 if v != 0 else -d
    s = Fr(math.ceil(Fr(v)/Fr(10)**e) + 1)*Fr(10)**e
    while x <= A_(s - Fr(10)**e): s -= Fr(10)**e
    assert x <= A_(s)
    return fmt(s, e)
def frlo(x, k=15): return fmt(Fr(math.floor(x*10**k), 10**k), -k)   # exact rational, lower decimal
def frup(x, k=15): return fmt(Fr(math.ceil(x*10**k), 10**k), -k)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def _e(x, d): return (math.floor(math.log10(abs(float(x)))) - d + 1) if x != 0 else -d
def qdn(x, d=10):  # exact rational x rounded down to d significant digits: (value, string)
    x = Fr(x); e = _e(x, d); s = Fr(math.floor(x/Fr(10)**e))*Fr(10)**e; assert s <= x; return s, fmt(s, e)
def qup(x, d=10):  # exact rational x rounded up to d significant digits: (value, string)
    x = Fr(x); e = _e(x, d); s = Fr(math.ceil(x/Fr(10)**e))*Fr(10)**e; assert s >= x; return s, fmt(s, e)
def bdn(x, d=10):  # a d-digit decimal certified <= the arb ball x: (value, string)
    v = fl(x.lower()); e = _e(v, d); s = Fr(math.floor(Fr(v)/Fr(10)**e) - 1)*Fr(10)**e
    while A_(s + Fr(10)**e) <= x: s += Fr(10)**e
    assert A_(s) <= x
    return s, fmt(s, e)

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'inputs_v08.json')
INP = json.load(open(path))
P = {}
def load(dct):
    for k, d in dct.items():
        if isinstance(d, dict) and 'value' in d: P[k] = dict(v=Fr(d['value']), sense=d['sense'], status=d['status'], cite=d['cite'])
for blk in ('fixed', 'source', 'background', 'far_Fa', 'kb', 'near', 'rest', 'ce'): load(INP[blk])
STANDIN = ('STANDIN-FLOAT', 'STANDIN-TARGET', 'STANDIN-ZERO', 'UNAUDITED', 'REGIONAL')
RES = []
def check(block, name, statement, ok, keys, value='', note=''):
    if ok is None: st = 'OPEN'
    elif not ok: st = 'FAIL'
    else: st = 'PASS-COND' if any(P[k]['status'] in STANDIN for k in keys) else 'PASS'
    stand = [k for k in keys if P[k]['status'] in STANDIN]
    RES.append(dict(block=block, name=name, statement=statement, status=st, value=value, inputs=keys, standins=stand, note=note))
    print('[%s] %s %s: %s%s%s' % (block, st, name, statement, (' | ' + value) if value else '',
                                  (' | stand-ins: ' + ', '.join(stand)) if stand else ''))
    if note: print('      ' + note)
    return st
V = lambda k: P[k]['v']
q, c, sigma = V('q'), V('c'), V('sigma')
cap = c + 1 - q
reading = INP['h4_reading']['value']
print(__doc__)
print('inputs: %s (SHA256 %s)' % (os.path.relpath(path, HERE), sha(path)))
print('cap = c + 1 - q >= %s (exact %s); H4 reading: %s\n' % (frlo(cap), cap, reading))

# ---------- Block N. Binding of theory_agent_1's near part ----------
print('== Block N. Binding of NEAR_CHECK_v09 (theory_agent_1 notes 83, 98 to 100, 102, 116)')
nb = INP['near_binding']; nd = os.path.join(HERE, nb['dir'])
bad = [fn for fn, h in nb['sha256'].items() if sha(os.path.join(nd, fn)) != h]
NR = json.load(open(os.path.join(nd, nb['result'])))
selfok = (NR['params_sha256'] == nb['sha256'][nb['params']] and NR['program_sha256'] == nb['sha256'][nb['program']]
          and NR['program'] == nb['program'] and NR['params'] == nb['params'])
check('N', 'N1', 'the bound near files match the pinned SHA256 and the result file names the pinned program and parameters',
      not bad and selfok, [], 'mismatch: %s' % (', '.join(bad) or 'none'))
NP = json.load(open(os.path.join(nd, nb['params'])))
def npv(x): return sum((Fr(u) for u in x.split(' + ')), Fr(0)) if ' - ' not in x else Fr(x.split(' - ')[0]) - Fr(x.split(' - ')[1])
same = [  # (input here, its value here, the NEAR_CHECK_v09 parameter it must equal)
    ('q', V('q'), 'fixed.q', npv(NP['fixed']['q']['value'])), ('sigma', V('sigma'), 'fixed.sigma', npv(NP['fixed']['sigma']['value'])),
    ('c', V('c'), 'fixed.c', npv(NP['fixed']['c']['value'])), ('C_D', V('C_D'), 'fixed.C_D', npv(NP['fixed']['C_D']['value'])),
    ('t', V('t'), 'fixed.t', npv(NP['fixed']['t']['value'])), ('nu', V('nu'), 'fixed.nu', npv(NP['fixed']['nu']['value'])),
    ('D4_an', V('D4_an'), 'global.D4_an', npv(NP['global']['D4_an']['value'])),
    ('D5_an', V('D5_an'), 'global.D5_an', npv(NP['global']['D5_an']['value'])),
    ('D6_an', V('D6_an'), 'global.D6_an', npv(NP['global']['D6_an']['value'])),
    ('Lambda_plus', V('Lambda_plus'), 'global.Lambda_plus', npv(NP['global']['Lambda_plus']['value'])),
    ('L1_plus', V('L1_plus'), 'global.L1_pos', npv(NP['global']['L1_pos']['value'])),
    ('sup_pos_an_W2', V('sup_pos_an_W2'), 'global.sup_pos_aW2', npv(NP['global']['sup_pos_aW2']['value'])),
    ('sup_abs_an_W2', V('sup_abs_an_W2'), 'max(global.sup_neg_aW2, global.sup_pos_aW2)',
     max(npv(NP['global']['sup_neg_aW2']['value']), npv(NP['global']['sup_pos_aW2']['value']))),
    ('beta_star', V('beta_star'), 'global.beta_star', npv(NP['global']['beta_star']['value'])),
    ('eps_rest', V('eps_rest'), 'global.eps_rest', npv(NP['global']['eps_rest']['value']))] + [
    ('K_LB.%d - K_UB.%d' % (m, m), Fr(INP['near']['K_LB'][str(m)]) - Fr(INP['near']['K_UB'][str(m)]), 'global.K%d' % m,
     npv(NP['global']['K%d' % m]['value'])) for m in (4, 5, 6)]
for cs in INP['cases']:
    npc = next((x for x in NP['cases'] if Fr(x['b0']) == Fr(cs['b0']['value']) and Fr(x['mu']) == Fr(cs['mu']['value'])), None)
    for k in ('kappa_0', 'kappa_2q', 'kappa_j'):
        same.append(('%s[%s,%s]' % (k, cs['b0']['value'], cs['mu']['value']), Fr(cs[k]['value']),
                     'cases[%s].%s' % (npc['label'] if npc else 'none', k), npv(npc[k]['value']) if npc else None))
diff = [a for a, x, b, y in same if x != y]
same_ok = not diff
check('N', 'N4', 'same inputs (AT2354): every near input here equals the parameter of NEAR_CHECK_v09 (%s) that'
      ' N2 and N3 compare against (%d values, exact)' % (nb['params'], len(same)), same_ok, [], 'differ: %s' % (', '.join(diff) or 'none'),
      'N2 and N3 are transcription rows at these identical inputs; with N4 FAIL they are FAIL by definition and say nothing'
      ' about the sufficient inequalities')

# ---------- Block A. Background: whole-plane cover, beta_0*, rates ----------
print('\n== Block A. Background (chain item 3; RC-5, T2.7, Lemma KB, AT-211)')
regs = INP['background']['regions']
def union_gaps(stats, level, kinds=('cover', 'matrix recount')):
    # gaps of the union of the regions with these statuses and kinds whose certified matrix lower is >= level
    iv = sorted((Fr(r['r2_lo']), None if r['r2_hi'] == 'inf' else Fr(r['r2_hi'])) for r in regs
                if r['status'] in stats and r['kind'] in kinds and Fr(r['level']) >= level)
    gaps, reach = [], Fr(0)
    for lo, hi in iv:
        if lo > reach: gaps.append((reach, lo))
        if hi is None: return gaps
        reach = max(reach, hi)
    gaps.append((reach, None)); return gaps
lev0 = Fr(INP['background']['cover_level'])
g1 = union_gaps(('CONFIRMED',), V('beta_star')); g2 = union_gaps(('CONFIRMED', 'CONFIRMED-NO-UNION'), V('beta_star'))
g3 = union_gaps(('CONFIRMED',), lev0, ('cover',)); g4 = union_gaps(('CONFIRMED', 'CONFIRMED-NO-UNION'), lev0, ('cover',))
sg = lambda gs: '; '.join('(%s, %s)' % (a, 'inf' if b is None else b) for a, b in gs) or 'none'
cover_ok = not g1
check('A', 'A1', 'the both-auditor union of regional matrix certificates at level >= beta_* = %s covers r^2 in [0, inf)'
      ' (whole-plane premise of beta_*)' % V('beta_star'),
      True if cover_ok else None, [], 'open r^2 gaps of the union at level beta_*: %s; with the certified roots that have no union: %s'
      % (sg(g1), sg(g2)), ('cutoff %s. The union has no gap, so beta_* >= %s is a whole-plane lower (input status %s).'
      if cover_ok else 'cutoff %s. Until the gap is closed, beta_* >= %s is %s, not a whole-plane lower.')
      % (INP['background']['regions_cutoff'], V('beta_star'), P['beta_star']['status']))
if cover_ok: P['beta_star']['status'] = 'CONFIRMED'
elif P['beta_star']['status'] == 'CONFIRMED': P['beta_star']['status'] = 'REGIONAL'   # a CONFIRMED status needs the union
cover0_ok = not g3
check('A', 'A1g', 'the both-auditor union of the chain item 3 cover certificates (kind cover; a matrix recount certifies only the'
      ' matrix lower) at level %s covers r^2 in [0, inf) (whole-plane premise of'
      ' g_*, s_*)' % lev0, True if cover0_ok else None, [], 'open r^2 gaps of the union at level %s: %s; with the certified roots that'
      ' have no union: %s' % (lev0, sg(g3), sg(g4)), ('the union has no gap, so g_* <= %s and s_* <= %s hold on the whole plane'
      if cover0_ok else 'until the gap is closed, g_* <= %s and s_* <= %s are cover targets (STANDIN-TARGET)') % (V('g_star'), V('s_star')))
for k in ('g_star', 's_star'):
    if cover0_ok: P[k]['status'] = 'CONFIRMED'
    elif P[k]['status'] == 'CONFIRMED': P[k]['status'] = 'STANDIN-TARGET'   # a CONFIRMED status needs the union
b0s = V('beta0') - V('g_star')
check('A', 'A2', 'beta_0* = beta_0 - g_* >= beta0_star = %s (T2.7 full L^2 inverse; g_* < beta_0)' % V('beta0_star'),
      b0s >= V('beta0_star') and V('g_star') < V('beta0'), ['beta0', 'g_star'], 'beta_0 - g_* >= %s' % frlo(b0s))
P['beta0_star']['status'] = 'CONFIRMED' if all(P[k]['status'] == 'CONFIRMED' for k in ('beta0', 'g_star')) else 'STANDIN-TARGET'
check('A', 'A4', 'betaK_* = beta_* - loss_KB > 0 on the reference ball (Lemma KB, chain item 7)', V('beta_star') - V('loss_KB') > 0,
      ['beta_star', 'loss_KB'], 'beta_* - loss_KB >= %s' % (V('beta_star') - V('loss_KB')))
check('A', 'A5', 'beta_* <= c + 1 - q (consistency with the upper of AT-211 for normalized backgrounds)', V('beta_star') <= cap, ['beta_star'])

# ---------- Block B. Far route F-a (exact) ----------
print('\n== Block B. Far route F-a at Rw = Ww = 200 (NR-26; FG1 with Proposition FG, AT-513)')
lhs = max(V('SC_plus'), V('AE_plus')) + V('SW_plus') + V('OMF_plus')
rhs = q*(c - V('s_star'))
fk = ['SC_plus', 'AE_plus', 'SW_plus', 'OMF_plus', 's_star']
check('B', 'B1', 'max(SC^+, A_E^+) + S_W^+ + OMF^+ <= G = q (c - s_*)', lhs <= rhs, fk,
      'lhs %s, G %s, exact margin %s (>= %s)' % (lhs, rhs, rhs - lhs, frlo(rhs - lhs)))
smax = c - lhs/q
check('B', 'B2', 's_* <= s_max = c - lhs/q (any certified whole-plane strain bound up to s_max serves; zero far slack at equality)',
      V('s_star') <= smax, fk, 's_max >= %s' % frlo(smax, 12))
check('B', 'B3', 's_* < c (the free gain of Proposition DR and FG needs s_* < c)', V('s_star') < c, ['s_star'])

# ---------- Blocks C and D. Source and Lemma KB ----------
print('\n== Blocks C and D. Source (ledger rows G1, L) and the reference ball (Lemma KB rectangle)')
f, n = V('f'), V('n')
Rs = f/V('beta0_star')
check('C', 'C1', 'certified ||F_*||_2 <= f and N(F_*) <= n', True, ['f', 'n'], 'f = %s, n = %s' % (frup(f, 22), frup(n, 22)))
check('D', 'D1', 'R_* = f/beta_0* <= Rbar = %s' % V('Rbar'), Rs <= V('Rbar'), ['f', 'beta0_star', 'Rbar'], 'R_* <= %s' % frup(Rs, 18))

# ---------- Block T. Feasibility of the upper stand-ins (AT2364 to AT2366) ----------
print('\n== Block T. Feasibility of the upper stand-ins: no upper target below a certified lower of the same quantity')
LOWERS = [('Lambda_plus', 8*(2*c - 1), 'Lambda_+(a_n) >= lambda_max Hess a_n(0) = 8 (2c - 1), Hess a_n(0) = diag(8 (2c - 1), 8) (AT-575; AT2364)'),
          ('D6_an', Fr(62748), 'D_6(a_n) >= 62748 (AT1467; ledger v11 row G3)')]
infeas = [k for k, lo, _ in LOWERS if V(k) < lo]
for k, lo, why in LOWERS:
    print('  %s: stand-in upper %s, certified lower %s (%s): %s' % (k, INP['near'][k]['value'], lo if lo.denominator == 1 else '%s >= %s' % (lo, frlo(lo, 9)),
          why, 'gap %s (exact), a same-or-better certified upper is impossible (AT2365)' % (lo - V(k)) if V(k) < lo else
          'feasible; value - lower = %s (exact), <= %s' % (V(k) - lo, qup(V(k) - lo, 10)[1] if V(k) > lo else '0')))
check('T', 'T1', 'every upper stand-in with a known certified lower is at least that lower (else no certificate can replace it at'
      ' its value)', not infeas, [], 'infeasible: %s' % (', '.join(infeas) or 'none'),
      'the arithmetic of block E uses max(Lambda_plus, 8 (2c - 1)) = 8 (2c - 1); that is an upper only with a proof that the global'
      ' supremum of the positive Hessian of a_n equals its origin value (AT2366 OPEN). A revised target needs a new NEAR_CHECK and a new run'
      if infeas else '')

# ---------- constants of HF1-NEAR ----------
qa, ca, pi = A_(q), A_(c), arb.pi()
x0 = (qa/2)*arb(2).log(); caw = 2*qa**2*(x0.sinh()/x0)**2
A4c = pi**2*(1 + caw/2) + A_(V('C_D'))/2
floor_L = 8*(2*c - 1)
nu, t = V('nu'), V('t'); nuA, tA = A_(nu), A_(t)
KL = {m: Fr(INP['near']['K_LB'][str(m)]) - Fr(INP['near']['K_UB'][str(m)]) for m in (4, 5, 6)}
Dn = {4: V('D4_an'), 5: V('D5_an'), 6: V('D6_an')}
pos = all(Dn[m]**2 > KL[m] for m in (4, 5, 6))
Dr = {m: A_(Dn[m]**2 - KL[m]).sqrt() for m in (4, 5, 6)}
M4r = ((Dr[4]*Dr[6] + Dr[5]**2)/(2*pi)).sqrt()
M4n = ((A_(Dn[4])*A_(Dn[6]) + A_(Dn[5])**2)/(2*pi)).sqrt()   # M4^+(a_n): NR-25 (iii) for a_n itself (AT2871; NEAR_CHECK_v09)
eps_r = A_(V('eps_rest'))
def U(v):  # NR-32: T_q(a_c; v) <= c sqrt(pi) v^(q+3/2) e^(-v/2)/(2 (v - 2q - 1)), v > 2q + 1
    v = A_(v); assert v > 2*qa + 1
    return ca*pi.sqrt()*v**(qa + A_(Fr(3, 2)))*(-v/2).exp()/(2*(v - 2*qa - 1))
def t6(v): v = A_(v); return v**(qa - 5)*Dr[6]/(4*pi*(5 - qa)).sqrt()
P1 = CG.Weight(1, Fr(1, 2), Fr(9619, 5000))
def ce_cell(b0x):
    Rq = f/V('beta0_star'); R = A_(Rq)
    _, r1, r2 = P1.best_rhos(float(Rq), 0.3); cf = P1.cf_of(r1, r2)
    kfun = lambda M: P1.Kstar_f(float(Rq), M, cf)
    M, B, Ap = P1.search(b0x, Rq, kfun, lambda Pv, M: M*(Pv - float(n)))   # float search; only the arb values below are statements
    Mr = H.rat3(M); clamped = Mr > V('Mbar')
    if clamped: Mr = V('Mbar')
    _, s1, s2 = P1.best_rhos(float(Rq), float(Mr)); Kb = P1.certify_K(Rq, Mr, s1, s2)
    Kok = bool(A_(Kb) - A_(Mr) - P1.E(R, A_(Kb), s1, s2) > 0) or Kb == P1.cWq*Mr
    loss = P1.loss(R, A_(Kb), B, Ap); bp = A_(b0x) - loss
    Z = A_(Mr)*(bp*A_(Mr) - A_(n)); D = Z/R**2
    return dict(R=R, M=Mr, clamped=clamped, B=B, A=Ap, rho=(s1, s2), Kb=Kb, Kok=Kok, loss=loss, bp=bp, Z=Z, D=D)
nk = ['Lambda_plus', 'L1_plus', 'D4_an', 'D5_an', 'D6_an', 'b0', 'mu', 'nu', 't', 'C_D']
pk = ['sup_abs_an_W2', 'sup_pos_an_W2', 'kappa_0', 'kappa_2q', 'kappa_j', 't', 'C_rest']
gk = ['f', 'n', 'beta0_star', 'b0', 'Mbar']
CASES = {}
for cs in INP['cases']:
    load(cs); b0, mu = V('b0'), V('mu'); muA = A_(mu); tag = '[%s,%s]' % (b0, mu)
    print('\n######## case %s: b0 = %s, mu = %s' % (cs['label'], b0, mu))
    check('A', 'A3' + tag, 'b0 <= beta_* (necessary, HF-NEC, AT-211; rate premise RC-5)', b0 <= V('beta_star'), ['b0', 'beta_star'],
          'beta_* - b0 = %s' % (V('beta_star') - b0))
    # ---------- Block E. (R1) ----------
    print('== Block E. (R1) (HF1-NEAR, AT-691; tail B, AT-757; quartic cut e term, AT-1094, AT-1134; core split a_n = -a_c + a_r, a_r = a_n + a_c, NR-25, NR-25 (iii) for a_n (AT2871), NR-30 Remark 5, AT2299;'
          ' K_m, AT-1453, AT-1454; NR-32, AT-1512, AT-1513)')
    Lp = max(V('Lambda_plus'), floor_L)
    e_L = (1 + qa**2)*A_(Lp)/(2*muA**2)
    e_M4 = A4c*(1024*ca + M4r).min(M4n)/muA**4
    tail_c = A_(Fr(4, 3))**qa*U(3*mu/4) + (8/muA)**qa*U(mu/2)
    tail_r = A_(Fr(4, 3))**qa*t6(3*mu/4) + (8/muA)**qa*t6(mu/2)
    e_nu = A_(V('L1_plus'))*nuA**2/(tA*8*(2*pi).sqrt())
    e_HF = e_L + e_M4 + tail_c + tail_r + e_nu
    check('E', 'E0' + tag, 'HF1-NEAR conditions mu >= 1, 0 < 2 nu <= mu, 0 < t < 1; D_m(a_n)^2 > K_m (m = 4, 5, 6); NR-32: mu/2 > 2q + 1',
          mu >= 1 and 0 < 2*nu <= mu and 0 < t < 1 and pos and mu/2 > 2*q + 1, ['mu', 'nu', 't', 'D4_an', 'D5_an', 'D6_an'])
    print('  terms (uppers): Lambda %s | M4 %s [min(1024 c + M4^+(a_r), M4^+(a_n)); M4^+(a_r) <= %s; M4^+(a_n) <= %s; D_m(a_r) <= %s, %s, %s] | tail_B(a_c) %s | tail_B(a_r) %s | low cut %s'
          % (updec(e_L, 9), updec(e_M4, 9), updec(M4r, 9), updec(M4n, 9), updec(Dr[4], 9), updec(Dr[5], 9), updec(Dr[6], 9), updec(tail_c, 9),
             updec(tail_r, 9), updec(e_nu, 9)))
    if V('Lambda_plus') >= floor_L:
        print('  Lambda_+ used: max(input %s, 8 (2c - 1) = %s) = the input, an upper with status %s (row T1 feasible)'
              % (INP['near']['Lambda_plus']['value'], frlo(floor_L, 9), P['Lambda_plus']['status']))
    else:
        print('  Lambda_+ used: max(input %s, 8 (2c - 1) = %s); the second is a certified LOWER bound (AT-575, AT2364), so the'
              ' value used is an upper only if the global supremum equals it (AT2366 OPEN; row T1)' % (INP['near']['Lambda_plus']['value'], frlo(floor_L, 9)))
    nc = next((x for x in NR['cases'] if Fr(x['b0']) == b0 and Fr(x['mu']) == mu), None)
    e_t1 = Fr(nc['e_up']) if nc else None
    agree = same_ok and nc is not None and bool(e_HF <= A_(e_t1)) and abs(Fr(fl(e_HF)) - e_t1) <= Fr(1, 10**10)
    check('N', 'N2' + tag, 'transcription at the inputs of N4: this program\'s independent e_HF ball lies below the printed NEAR_CHECK_v09 e_up,'
          ' within 1e-10', agree, [], 'here <= %s, NEAR_CHECK_v09 %s' % (updec(e_HF, 12), nc['e_up'] if nc else 'no case'))
    e_out = e_t1 if e_t1 is not None else qup(Fr(updec(e_HF, 12)), 12)[0]
    eps_q = V('eps_rest')
    print('  e_up used: the printed NEAR_CHECK_v09 value %s (exact rational)' % (nc['e_up'] if nc else e_out))
    m_i = (cap - b0) - eps_q - e_out
    check('E', 'E1' + tag, 'information only (reading (i), the cap budget; AT2334 REFUTED it as a deduction of the rate):'
          ' e_up + eps_rest <= c + 1 - q - b0', m_i >= 0,
          nk + ['eps_rest'], 'margin %s' % (('>= ' + qdn(m_i, 8)[1]) if m_i >= 0 else ('<= ' + qup(m_i, 8)[1])))
    m_ii = (V('beta_star') - b0) - eps_q - e_out
    need = b0 + eps_q + e_out
    check('E', 'E2' + tag, '(R1), reading (ii), the rate budget of H4 [Theorem H4-R slack, AT-364; AT1687; AT2333]: e_up + eps_rest <= beta_* - b0', m_ii >= 0,
          nk + ['eps_rest', 'beta_star'], 'margin %s' % (('>= ' + qdn(m_ii, 8)[1]) if m_ii >= 0 else ('<= ' + qup(m_ii, 8)[1])),
          'E2 holds iff beta_* >= b0 + eps_rest + e_up = %s (exact; <= %s; AT2335); E1 is E2 at beta_* = c + 1 - q, which is not a'
          ' certified rate' % (need, qup(need, 9)[1]))
    # ---------- Block F. H4-R bound on C^opt(b0) ----------
    print('== Block F. C^opt(b0) <= C_N + P_HF + C_rest (Theorem H4-R, AT-364; Proposition FG, AT-513; HF1-NEAR, AT-691)')
    S1 = A_(max(V('sup_abs_an_W2'), V('sup_pos_an_W2'))); S2 = A_(V('sup_pos_an_W2'))
    k0, k2q, kj = A_(V('kappa_0')), A_(V('kappa_2q')), A_(V('kappa_j'))
    P_HF = arb(2)**A_(sigma)*(S1*k0*k2q + S2*(kj**2 + kj**2)/(1 - tA))
    p_t1 = Fr(nc['C_N_upper']) if nc else None
    agreeP = same_ok and nc is not None and bool(P_HF <= A_(p_t1)) and abs(Fr(fl(P_HF)) - p_t1) <= Fr(1)
    check('N', 'N3' + tag, 'transcription at the inputs of N4: this program\'s independent P_HF ball lies below the printed NEAR_CHECK_v09 C_N_upper,'
          ' within 1', agreeP, [], 'here <= %s, NEAR_CHECK_v09 %s' % (updec(P_HF, 13), nc['C_N_upper'] if nc else 'no case'))
    P_out = p_t1 if p_t1 is not None else qup(Fr(updec(P_HF, 13)), 13)[0]
    C0 = V('C_rest') + P_out
    check('F', 'F1' + tag, 'C0 = C_rest + C_N_upper, C_N_upper >= P_HF = 2^sigma [sup(|a_n| W^2) kappa_0 kappa_2q + (1-t)^-1 sup((a_n)_+ W^2)'
          ' (kappa_1^2 + kappa_2^2)]', True, pk, 'C0 = %s (exact)' % C0)
    # ---------- Block G. Theorem B direct test ----------
    print('== Block G. Theorem B (AT-273), direct test at R_* = f/beta_0* with the certified f and n (CE code of budget_013h)')
    g = ce_cell(b0)
    print('  cell: M %s%s, (B, A) = (%s, %s), rho = %s, %s, Kbar %s (Kbar/M <= %s), L_B <= %s, b\' >= %s, Z >= %s, D = Z/R_*^2 >= %s'
          % (g['M'], ' (clamped)' if g['clamped'] else '', g['B'], g['A'], g['rho'][0], g['rho'][1], g['Kb'], frup(g['Kb']/g['M'], 6),
             updec(g['loss'], 8), lodec(g['bp'], 8), lodec(g['Z'], 6), bdn(g['D'], 10)[1]))
    if nc: print('  NEAR_CHECK_v09 D_lower (stipulated inputs beta_0 = 7/4, ||F_*||_2 <= 7.97e-7, N(F_*) <= 0.006): %s' % nc['D_lower'])
    D_out = bdn(g['D'], 10)[0]
    room = qdn(D_out - C0, 8); ratio = qup(C0/D_out, 8) if D_out > 0 else None
    check('G', 'G1' + tag, 'Kbar certified for Corollary CE-B at (R_*, M): Kbar - M - E(R_*, Kbar) > 0 in arb, or Kbar = c_W M', g['Kok'], gk)
    check('G', 'G2' + tag, "H5': B > 1/2 and b' = b0 - L_B(R_*, Kbar) > 0", g['B'] > Fr(1, 2) and g['bp'] > 0, gk)
    check('G', 'G3' + tag, '0 < M <= Mbar = %s (Lemma KB rectangle; E-v11-1)' % V('Mbar'), 0 < g['M'] <= V('Mbar'), gk)
    check('G', 'G4' + tag, "direct test (chain item 8): C0 R_*^2 <= M [(b0 - L_B) M - n], i.e. C0 <= D_out <= D", D_out > 0 and C0 <= D_out,
          gk + pk + nk, 'D_out = %s, C0/D_out <= %s, room D_out - C0 >= %s' % (fmt(D_out, 0), ratio[1] if ratio else '-', room[1]),
          'G4 does not contain beta_* and does not depend on the H4 reading (AT2356)')
    bii = Fr(math.floor((V('beta_star') - eps_q - e_out)*100), 100)
    comp = None
    if bii > 0:
        g2c = ce_cell(bii); m2 = (V('beta_star') - bii) - eps_q - e_out
        D2 = bdn(g2c['D'], 10)[0] if g2c['D'] > 0 else None
        print('  reading (ii) companion at b0 = %s (largest on the 1/100 grid with (R1) at beta_*): D_out %s, C0/D_out %s, M %s, B %s'
              % (bii, fmt(D2, 0) if D2 else 'not positive', ('<= ' + qup(C0/D2, 8)[1]) if D2 else '-', g2c['M'], g2c['B']))
        check('G', 'G5' + tag, 'companion at another rate (information only; b0 is the largest on the 1/100 grid with E2 at beta_*, and it may be above or below the original b0, AT2497): E2 and the direct test together at b0 = %s, mu %s' % (bii, mu),
              bool(m2 >= 0 and D2 is not None and C0 <= D2), gk + pk + nk + ['beta_star', 'eps_rest'],
              'E2 at the companion: margin %s (%s); direct test at the companion: C0/D_out %s (%s)'
              % (('>= ' + qdn(m2, 8)[1]) if m2 >= 0 else ('<= ' + qup(m2, 8)[1]), 'holds' if m2 >= 0 else 'fails',
                 ('<= ' + qup(C0/D2, 8)[1]) if D2 else '-', 'holds' if D2 is not None and C0 <= D2 else 'fails'))
        comp = dict(b0=str(bii), E2_margin=(qdn(m2, 8)[1] if m2 >= 0 else 'upper ' + qup(m2, 8)[1]), D_out=(str(D2) if D2 else 'not positive'),
                    C0_over_D_out=(qup(C0/D2, 8)[1] if D2 else '-'), M=str(g2c['M']), B=str(g2c['B']))
    st = {r['name'][:2]: r['status'] for r in RES if r['name'].endswith(tag)}
    check('J', 'J1' + tag, 'combined sufficient criterion at the original rate b0 = %s (AT2353): E2 and G4 together' % b0,
          bool(m_ii >= 0 and D_out > 0 and C0 <= D_out), gk + pk + nk + ['beta_star', 'eps_rest'],
          'E2 %s, G4 %s; companion G5 %s' % (st['E2'], st['G4'], st.get('G5', '-')),
          'the failing part at the original rate is %s; at the companion it is %s (AT2356); a failed sufficient test excludes nothing'
          % (' and '.join([x for x, okx in (('E2 (rate budget)', m_ii >= 0), ('G4 (direct test)', D_out > 0 and C0 <= D_out)) if not okx]) or 'none',
             ('none' if (comp is None or st.get('G5') != 'FAIL') else
              ' and '.join([x for x, okx in (('E2', m2 >= 0), ('the direct test', D2 is not None and C0 <= D2)) if not okx]))))
    CASES[cs['label']] = dict(tag=tag, b0=str(b0), mu=str(mu), e_up=str(e_out), margin_i=(qdn(m_i, 8)[1] if m_i >= 0 else 'upper ' + qup(m_i, 8)[1]),
        margin_ii=(qdn(m_ii, 8)[1] if m_ii >= 0 else 'upper ' + qup(m_ii, 8)[1]), beta_star_needed_ii=qup(need, 9)[1], beta_star_needed_ii_exact=str(need),
        C0=str(C0), D_out=str(D_out), Z=lodec(g['Z'], 8), C0_over_D_out=(ratio[1] if ratio else '-'), room=room[1],
        M=str(g['M']), B=str(g['B']), A=str(g['A']), Kbar=str(g['Kb']), loss=updec(g['loss'], 10), bprime=lodec(g['bp'], 10),
        companion_ii=comp)

# ---------- Block H. Named hypotheses ----------
print('\n== Block H. Named hypotheses (premises of T2.7, Lemma KB, Theorem B, H4-R, Proposition FG, HF1-NEAR, route F-a)')
HYP = [
    ('H-B', 'whole-plane background: lambda_max H <= -beta_*, |grad h_*| <= g_*, ||Sym Du||_op <= s_* on R^2 (chain item 3; N0 of H4-R; RC-5)',
     'supplied' if (cover_ok and cover0_ok) else 'OPEN', 'blocks A1, A1g; theory_audit AT2534 to AT2536 (audit_v771; adopted, numerical_audit exchange v755)'
     ' CONFIRM M >= (704955805507/10^12) I, |grad h| <= 1/4 and ||Sym Du||_op <= 137/125 on the whole plane under the admitted'
     ' exact-source and containing-arithmetic hypotheses: the inner lower on r^2 <= 61/67 (AT2386), the host lower'
     ' 890672299617/10^12 on 7/9 <= r^2 <= 49/15 (AT2512 to AT2514) and the outer lower 761272835221/10^12 on r^2 >= 49/15'
     ' (AT2402)'),
    ('H-RC', 'RC-1 to RC-10 of V11-2 (a) for h_* (structural: the exact-potential class, AT-674, AT-675; quantitative: chain items 2, 3)',
     'OPEN', 'its quantitative part runs through H-B (supplied when A1 and A1g pass) and chain item 2; not checked by this program'),
    ('H1', 'actual generator: closed generator, core, weighted semigroup and graph comparison on a reference ball containing K(R_*, M)'
     ' (AT-237 bridge)', 'OPEN', 'conditionally reduced (AT-600; Lemma KB, AT-772, AT-832) to H-B and the source bounds'),
    ('H2', 'full L^2 inverse of L_* + U[k].grad with rate beta_0* on the ball (T2.7, AT-123; E-v11-2); ||z||_2 <= R_* for z = T(k)',
     'OPEN', 'through H-B (g_* <= 1/4; supplied when A1g passes) and H1; this is the uniform small-k inverse (O2)'),
    ('H3', '(R3/R5) of Theorem B and N(F_*) < infinity', 'retained', 'N(F_*) <= n CONFIRMED; R3/R5 imported with their hypotheses'),
    ('H-BALL', 'the reference ball is the full real S1 ball B(Rbar, Mbar), no ell restriction, with the center matrix premise of Lemma KB',
     'OPEN', 'rectangle and loss CONFIRMED (AT-772); the center matrix premise is H-B (supplied when A1 passes); the rest of the'
     ' premise is not checked by this program'),
    ('H4-COMP', 'the join of the near form with H4-R and the far form (NEAR_CHECK_v09 H4): E(g) <= -b0 ||g||^2 + C0 ||h||^2 from P0 + DR,'
     ' FG with the far rule (AT-513, AT-624) and HF1-NEAR for (TII + C_aw)[a_n]; reading (i) charges e_up to c + 1 - q - b0,'
     ' reading (ii) to beta_* - eps_R - b0', ('supplied as an implication (reading ii)' if reading == 'ii' else
     'OPEN' if reading == 'undecided' else 'REFUTED (reading i)'),
     'AT2333 CONFIRMED: the common-domain principal, near, far and rest estimates imply H4 when e_up + eps_rest <= beta_* - b0'
     ' (row E2); AT2334 REFUTED reading (i); theory_agent_1 note 88. The estimates themselves are H-N1, H-NEARU, H4-REST, H-FA'),
    ('H4-REST', 'the other pieces of D_rem^n, T_IS, C_tr and C_vs1 to C_vs3, in NE form with eps_rest and C_rest (T2_H4_v01 NE-lo, NE-vs),'
     ' or charged to the far slack G - A_far under FG', 'OPEN', 'no 013 bound; stand-ins eps_rest = C_rest = 0 (STANDIN-ZERO).'
     ' theory_agent_2 T2_H4REST_v01 (CLAIMED lemmas, FLOAT prices): no estimate found there fits the price allowance, and'
     ' C_vs is the larger obstruction. The unsplit TIS-FG route cannot fit the free gain (AT2456 to AT2458). At the version 2'
     ' (R4) tuple and the whole-plane rate the Lemma HI\' upper fits the rate room only for mu_r >= 207.422143510389 with'
     ' K_half = c_tr\' + q/2 at the plan of record (223.601268661262 with K_q, 266.304848871307 with K; theory_agent_1 note 103) and'
     ' for mu_r >= 70.154855285062 with K_half at the fallback (AT2564 to AT2569); these restrict that sufficient upper only'),
    ('H-N1', 'NEAR_CHECK_v09 H1 to H3 (those of NEAR_CHECK_v03 section 3): N1 for the actual a_n, the whole-plane core split'
     ' a_n = -a_c + a_r (a_r = a_n + a_c; NR-30 Remark 5, AT2299) and theory_audit condition 4 for the erflog cut', 'OPEN',
     'theory_agent_1 NEAR_CHECK_v09 section 3'),
    ('H-N3', 'N3 at mu 72, nu 1/40: certified kernel uppers', 'supplied', 'AT-1491, AT-1492 (mu 72 only)'),
    ('H-NEARU', 'certified uppers of Lambda_+(a_n), ||(a_n)_+||_1, sup((a_n)_- W^2), sup((a_n)_+ W^2) and D4, D5, D6 of a_n on R^2',
     'supplied', 'Lambda_+, ||(a_n)_+||_1 and the two W^2 sups: CONFIRMED, theory_agent_2 Proposition R4 v02 (T2_NEAR_R4_v02; theory_audit AT2520 to AT2522 after numerical_audit\'s complete refined replay; adopted, numerical_audit exchange v750);'
     ' D4, D5, D6: CONFIRMED whole-plane uppers of numerical_audit\'s executed near consumer (request 314; theory_audit AT2869 to AT2871, exchange v872; adopted, numerical_audit exchange v917; adoption CONFIRMED, AT2885, audit_v876),'
     ' under the admitted Schwartz and full-plane Plancherel theorem and the imported containment, tail, regularity and normalization hypotheses'),
    ('H-TAIL', 'NR-25 (i), (iii), NR-30, the radial identity with K_m, NR-32', 'supplied',
     'AT-1344 to AT-1346, AT-1453, AT-1454, AT-1512, AT-1513'),
    ('H-FA', 'analytic premises of route F-a: AE-CS (AT-1698), Corollary CS-W and Proposition DW, HSB (AT-695), the source013 calculus,'
     ' tail-table certificate, Leibniz and Faa di Bruno estimates, singleton repair, CS-W homogeneity', 'retained',
     'the far scalar inequality is CONFIRMED conditional on them'),
    ('H-REG', 'V11-2 (d), stronger Hoelder regularity, with its own premises: route T1.3 (weight sigma_9 > sigma, R9.4 at sigma_9,'
     ' mu_R > 0 not evaluated for 013) or route R6.4 (alpha/(2c - 2) < delta < 1 and 1 < nu < 2; delta > 0.0617041 at alpha = 1/10).'
     ' The Hoelder nu of R6.4 is not the near cut nu = 1/40 of HF1-NEAR', 'OPEN', 'chain item 9; theory_v19 V11-2 (d); not needed for (a), (b)'),
]
for hname, text, st, cite in HYP:
    RES.append(dict(block='H', name=hname, statement=text, status=st, value='', inputs=[], standins=[], note=cite))
    print('[H] %s %s: %s | %s' % (st, hname, text, cite))

# ---------- Block I. Verdict and the statement that would follow ----------
print('\n== Block I. Verdict')
common = [r for r in RES if r['block'] in ('N', 'A', 'B', 'C', 'D', 'T') and '[' not in r['name']]
print('  H4 reading: %s (%s)' % (reading, INP['h4_reading']['cite']))
print('  required per case for reading (ii): A3, E0, N2, N3, E2, F1, G1, G2, G3, G4, J1; E1 and G5 are information only;'
      ' common rows N1, N4, A1, A1g, A2, A4, A5, B1 to B3, C1, D1, T1')
hyp_ok = all(r['status'] in ('supplied', 'retained') or r['status'].startswith('supplied') for r in RES if r['block'] == 'H' and r['name'] != 'H-REG')
cert_case = None
for lab, cd in CASES.items():
    need = ['A3', 'E0', 'F1', 'G1', 'G2', 'G3', 'G4', 'N2', 'N3', 'E2', 'J1']
    rows = [r for r in RES if r['name'] in [x + cd['tag'] for x in need]]
    cd['checks'] = {r['name']: r['status'] for r in RES if r['name'].endswith(cd['tag'])}
    if reading == 'ii' and hyp_ok and len(rows) == len(need) and all(r['status'] == 'PASS' for r in common + rows): cert_case = lab
for r in RES:
    if r['block'] != 'H': print('  %-28s %s' % (r['name'], r['status']))
stand = sorted(set(s for r in RES for s in r['standins']))
print('stand-in inputs used: ' + ', '.join(stand))
print('open hypotheses: ' + ', '.join(r['name'] for r in RES if r['block'] == 'H' and r['status'].startswith('OPEN')))
verdict = 'CLOSURE CERTIFIED (case %s)' % cert_case if cert_case else 'CLOSURE OPEN'
print('VERDICT: %s. %s' % (verdict, 'Every required check PASS and every hypothesis supplied.' if cert_case else
      'The dry run uses stand-ins and open hypotheses and proves nothing.'))
g0 = CASES[INP['cases'][0]['label']]
print('Statement that would follow (V11-2 (a), (b) with E-v11-1, E-v11-2; Theorem B): there is a stationary solution h = h_* + k'
      ' of the 013 profile problem with k real and S1, k in K(R_*, M) inside B(Rbar, M): ||k||_2 <= R_* <= %s <= Rbar = %s and'
      ' ||J^(21/10)(W k)||_2 <= M (M = %s in the plan-of-record cell, M <= 1/2); L_* + U[k].grad has the full L^2 inverse of T2.7'
      ' with rate beta_0* >= %s and the weighted estimate of V11-2 (a); and <X> h is in C^(1,1/10)(R^2) (V11-2 (b)).'
      ' V11-2 (d) stays OPEN.' % (frup(Rs, 18), V('Rbar'), g0['M'], V('beta0_star')))
out = dict(version='closure_check v08', rows_rule=__doc__.split('Rows and input changes')[1].split('Every input')[0].strip(),
           interface='every decision value is an exact rational; e_up and C_N_upper are the printed NEAR_CHECK_v09 uppers; C0 = C_rest + C_N_upper; D_out <= D (arb ball); margin_i, margin_ii and room are exact values rounded down; C0_over_D_out and beta_star_needed_ii are exact values rounded up; G4 passes iff C0 <= D_out', inputs=os.path.relpath(path, HERE), inputs_sha256=sha(path),
           program_sha256=sha(os.path.abspath(__file__)), h4_reading=reading, verdict=verdict, results=RES, cases=CASES,
           common=dict(cap=str(cap), far_margin=str(rhs - lhs), s_max_lower=frlo(smax, 12), R_star_upper=frup(Rs, 18),
                       cover_gaps_union=sg(g1), cover_gaps_with_roots=sg(g2), cover_level=str(lev0),
                       cover_gaps_union_gs=sg(g3), cover_gaps_with_roots_gs=sg(g4)),
           seconds=round(time.time() - t_start, 2))
json.dump(out, open(os.path.join(HERE, 'closure_check_v08.json'), 'w'), indent=1)
print('wrote closure_check_v08.json (%.1f s)' % (time.time() - t_start))

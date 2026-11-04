"""closure_check (theory_agent_2, 2026-11-04, version 01): the final closure check of theory_audit's SOURCE013_CHAIN_CONDITIONS_v01,
items 8 and 9, as a conditional program (coordinator 07:08Z item 3(a)). Text: notes/T2_CLOSURE_CHECK_v01.md.
It binds theory_agent_1's near part NEAR_CHECK_v01 (copied unchanged into nearcopy/, hashes pinned in the inputs) and
recomputes its two near quantities independently as a transcription check.
Every input is a named parameter of inputs_v01.json with a sense (upper, lower, exact, choice) and a status. Arithmetic
is exact (Fraction) or outward arb (python-flint, 200 bits). Each check is reported as
  PASS       it holds, and every input it uses is CONFIRMED (or a choice);
  PASS-COND  it holds at the given values, but some input is a stand-in (STANDIN-FLOAT or STANDIN-TARGET),
             so the check proves nothing;
  FAIL       it does not hold at the given values (a failed sufficient test; it excludes nothing);
  OPEN       a premise that no computation here supplies.
The closure statement (block I) follows only if, for one case, every check of the accepted H4 reading is PASS and
every named hypothesis of block H is supplied by an accepted certificate. The CE part (block G) is theory_agent_1's
budget_013h code (ps1copy/), used unchanged.
Usage: python3 -B closure_check.py [inputs.json]   (writes closure_check_v01.json next to this file)"""
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

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'inputs_v01.json')
INP = json.load(open(path))
P = {}
def load(dct):
    for k, d in dct.items():
        if isinstance(d, dict) and 'value' in d: P[k] = dict(v=Fr(d['value']), sense=d['sense'], status=d['status'], cite=d['cite'])
for blk in ('fixed', 'source', 'background', 'far_Fa', 'kb', 'near', 'rest', 'ce'): load(INP[blk])
STANDIN = ('STANDIN-FLOAT', 'STANDIN-TARGET')
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
print('== Block N. Binding of NEAR_CHECK_v01 (theory_agent_1 notes 83, 84)')
nb = INP['near_binding']; nd = os.path.join(HERE, nb['dir'])
bad = [fn for fn, h in nb['sha256'].items() if sha(os.path.join(nd, fn)) != h]
NR = json.load(open(os.path.join(nd, 'near_check_v01.result.json')))
selfok = NR['params_sha256'] == nb['sha256']['near_params_v01.json'] and NR['program_sha256'] == nb['sha256']['near_check_v01.py']
check('N', 'N1', 'the bound near files match the pinned SHA256 and the result file names the pinned program and parameters',
      not bad and selfok, [], 'mismatch: %s' % (', '.join(bad) or 'none'))

# ---------- Block A. Background: whole-plane cover, beta_0*, rates ----------
print('\n== Block A. Background (chain item 3; RC-5, T2.7, Lemma KB, AT-211)')
regs = INP['background']['regions']
def union_gaps(stats):
    iv = sorted((Fr(r['r2_lo']), None if r['r2_hi'] == 'inf' else Fr(r['r2_hi'])) for r in regs if r['status'] in stats)
    gaps, reach = [], Fr(0)
    for lo, hi in iv:
        if lo > reach: gaps.append((reach, lo))
        if hi is None: return gaps
        reach = max(reach, hi)
    gaps.append((reach, None)); return gaps
g1 = union_gaps(('CONFIRMED',)); g2 = union_gaps(('CONFIRMED', 'CONFIRMED-NO-UNION'))
sg = lambda gs: '; '.join('(%s, %s)' % (a, 'inf' if b is None else b) for a, b in gs) or 'none'
cover_ok = not g1
check('A', 'A1', 'the both-auditor union of regional certificates covers r^2 in [0, inf) (whole-plane premise of beta_*, g_*, s_*)',
      True if cover_ok else None, [], 'open r^2 gaps of the union: %s; with the certified roots that have no union: %s' % (sg(g1), sg(g2)),
      'cutoff %s. Until the gap is closed, beta_* >= %s, g_* <= %s and s_* <= %s are cover targets (STANDIN-TARGET).'
      % (INP['background']['regions_cutoff'], V('beta_star'), V('g_star'), V('s_star')))
if cover_ok:
    for k in ('beta_star', 'g_star', 's_star'): P[k]['status'] = 'CONFIRMED'
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
    print('== Block E. (R1) (HF1-NEAR, AT-691; tail B, AT-757; quartic cut e term, AT-1094, AT-1134; core split NR-25, NR-30;'
          ' K_m, AT-1453, AT-1454; NR-32, AT-1512, AT-1513)')
    Lp = max(V('Lambda_plus'), floor_L)
    e_L = (1 + qa**2)*A_(Lp)/(2*muA**2)
    e_M4 = A4c*(1024*ca + M4r)/muA**4
    tail_c = A_(Fr(4, 3))**qa*U(3*mu/4) + (8/muA)**qa*U(mu/2)
    tail_r = A_(Fr(4, 3))**qa*t6(3*mu/4) + (8/muA)**qa*t6(mu/2)
    e_nu = A_(V('L1_plus'))*nuA**2/(tA*8*(2*pi).sqrt())
    e_HF = e_L + e_M4 + tail_c + tail_r + e_nu
    check('E', 'E0' + tag, 'HF1-NEAR conditions mu >= 1, 0 < 2 nu <= mu, 0 < t < 1; D_m(a_n)^2 > K_m (m = 4, 5, 6); NR-32: mu/2 > 2q + 1',
          mu >= 1 and 0 < 2*nu <= mu and 0 < t < 1 and pos and mu/2 > 2*q + 1, ['mu', 'nu', 't', 'D4_an', 'D5_an', 'D6_an'])
    print('  terms (uppers): Lambda %s | M4 %s [M4^+(a_r) <= %s; D_m(a_r) <= %s, %s, %s] | tail_B(a_c) %s | tail_B(a_r) %s | low cut %s'
          % (updec(e_L, 9), updec(e_M4, 9), updec(M4r, 9), updec(Dr[4], 9), updec(Dr[5], 9), updec(Dr[6], 9), updec(tail_c, 9),
             updec(tail_r, 9), updec(e_nu, 9)))
    print('  Lambda_+ used: max(input %s, 8 (2c - 1) = %s); the second is a certified LOWER bound (AT-575), so the input'
          ' must be a certified upper' % (INP['near']['Lambda_plus']['value'], frlo(floor_L, 9)))
    nc = next((x for x in NR['cases'] if Fr(x['b0']) == b0 and Fr(x['mu']) == mu), None)
    e_t1 = Fr(nc['e_up']) if nc else None
    agree = nc is not None and abs(Fr(fl(e_HF)) - e_t1) <= Fr(1, 10**10)
    check('N', 'N2' + tag, 'transcription: this program\'s e_HF upper agrees with NEAR_CHECK_v01 e_up to 1e-10', agree, [],
          'here <= %s, NEAR_CHECK_v01 %s' % (updec(e_HF, 12), nc['e_up'] if nc else 'no case'))
    e_use = e_HF if e_t1 is None else (e_HF if e_HF > A_(e_t1) else A_(max(e_t1, Fr(fl(e_HF.upper())))))
    print('  e_up used (the larger of the two uppers) <= %s' % updec(e_use, 10))
    m_i = A_(cap - b0) - eps_r - e_use
    check('E', 'E1' + tag, '(R1), reading (i) [V10-4 (a); NEAR_CHECK_v01 (a)]: e_up + eps_rest <= c + 1 - q - b0', m_i > 0,
          nk + ['eps_rest'], 'margin %s' % (('>= ' + lodec(m_i, 6)) if m_i > 0 else ('<= ' + updec(m_i, 6))))
    m_ii = A_(V('beta_star') - b0) - eps_r - e_use
    need = A_(b0) + eps_r + e_use
    check('E', 'E2' + tag, '(R1), reading (ii) [Theorem H4-R slack, AT-364; AT1687]: e_up + eps_rest <= beta_* - b0', m_ii > 0,
          nk + ['eps_rest', 'beta_star'], 'margin %s' % (('>= ' + lodec(m_ii, 6)) if m_ii > 0 else ('<= ' + updec(m_ii, 6))),
          'reading (ii) holds iff beta_* >= b0 + eps_rest + e_up, which is <= %s here; reading (i) is reading (ii) at beta_* = c + 1 - q'
          % updec(need, 8))
    # ---------- Block F. H4-R bound on C^opt(b0) ----------
    print('== Block F. C^opt(b0) <= C_N + P_HF + C_rest (Theorem H4-R, AT-364; Proposition FG, AT-513; HF1-NEAR, AT-691)')
    S1 = A_(max(V('sup_abs_an_W2'), V('sup_pos_an_W2'))); S2 = A_(V('sup_pos_an_W2'))
    k0, k2q, kj = A_(V('kappa_0')), A_(V('kappa_2q')), A_(V('kappa_j'))
    P_HF = arb(2)**A_(sigma)*(S1*k0*k2q + S2*(kj**2 + kj**2)/(1 - tA))
    p_t1 = Fr(nc['C_N_upper']) if nc else None
    agreeP = nc is not None and abs(Fr(fl(P_HF)) - p_t1) <= Fr(1)
    check('N', 'N3' + tag, 'transcription: this program\'s P_HF upper agrees with NEAR_CHECK_v01 C_N_upper to 1', agreeP, [],
          'here <= %s, NEAR_CHECK_v01 %s' % (updec(P_HF, 13), nc['C_N_upper'] if nc else 'no case'))
    P_use = P_HF if p_t1 is None else (P_HF if P_HF > A_(p_t1) else A_(max(p_t1, Fr(fl(P_HF.upper())))))
    C0 = A_(V('C_rest')) + P_use
    check('F', 'F1' + tag, 'C0 = C_rest + P_HF, P_HF = 2^sigma [sup(|a_n| W^2) kappa_0 kappa_2q + (1-t)^-1 sup((a_n)_+ W^2) (kappa_1^2 + kappa_2^2)]',
          True, pk, 'C0 <= %s' % updec(C0, 9))
    # ---------- Block G. Theorem B direct test ----------
    print('== Block G. Theorem B (AT-273), direct test at R_* = f/beta_0* with the certified f and n (CE code of budget_013h)')
    g = ce_cell(b0)
    print('  cell: M %s%s, (B, A) = (%s, %s), rho = %s, %s, Kbar %s (Kbar/M <= %s), L_B <= %s, b\' >= %s, Z >= %s, D = Z/R_*^2 >= %s'
          % (g['M'], ' (clamped)' if g['clamped'] else '', g['B'], g['A'], g['rho'][0], g['rho'][1], g['Kb'], frup(g['Kb']/g['M'], 6),
             updec(g['loss'], 8), lodec(g['bp'], 8), lodec(g['Z'], 6), lodec(g['D'], 6)))
    if nc: print('  NEAR_CHECK_v01 D_lower (stipulated inputs beta_0 = 7/4, ||F_*||_2 <= 7.97e-7, N(F_*) <= 0.006): %s' % nc['D_lower'])
    check('G', 'G1' + tag, 'Kbar certified for Corollary CE-B at (R_*, M): Kbar - M - E(R_*, Kbar) > 0 in arb, or Kbar = c_W M', g['Kok'], gk)
    check('G', 'G2' + tag, "H5': B > 1/2 and b' = b0 - L_B(R_*, Kbar) > 0", g['B'] > Fr(1, 2) and g['bp'] > 0, gk)
    check('G', 'G3' + tag, '0 < M <= Mbar = %s (Lemma KB rectangle; E-v11-1)' % V('Mbar'), 0 < g['M'] <= V('Mbar'), gk)
    check('G', 'G4' + tag, "direct test (chain item 8): C0 R_*^2 <= M [(b0 - L_B) M - n], i.e. C0 <= D", bool(C0*g['R']**2 < g['Z']),
          gk + pk + nk, 'C0/D <= %s, room D - C0 >= %s' % (updec(C0/g['D'], 7), lodec(g['D'] - C0, 6)))
    bii = Fr(math.floor(Fr(fl((A_(V('beta_star')) - eps_r - e_use).lower()))*100), 100)
    comp = None
    if bii > 0:
        g2c = ce_cell(bii); m2 = A_(V('beta_star') - bii) - eps_r - e_use
        print('  reading (ii) companion at b0 = %s (largest on the 1/100 grid with (R1) at beta_*): D %s, C0/D %s, M %s, B %s'
              % (bii, ('>= ' + lodec(g2c['D'], 6)) if g2c['D'] > 0 else 'not positive',
                 ('<= ' + updec(C0/g2c['D'], 6)) if g2c['D'] > 0 else '-', g2c['M'], g2c['B']))
        check('G', 'G5' + tag, 'reading (ii) companion (information only): (R1) at beta_* and the direct test at b0 = %s, mu %s' % (bii, mu),
              bool(m2 > 0 and C0*g2c['R']**2 < g2c['Z']), gk + pk + nk + ['beta_star', 'eps_rest'])
        comp = dict(b0=str(bii), D=(lodec(g2c['D'], 8) if g2c['D'] > 0 else 'not positive'),
                    C0_over_D=(updec(C0/g2c['D'], 8) if g2c['D'] > 0 else '-'), M=str(g2c['M']), B=str(g2c['B']))
    CASES[cs['label']] = dict(tag=tag, b0=str(b0), mu=str(mu), e_up=updec(e_use, 10), margin_i=lodec(m_i, 8) if m_i > 0 else 'upper ' + updec(m_i, 8),
        margin_ii=lodec(m_ii, 8) if m_ii > 0 else 'upper ' + updec(m_ii, 8), beta_star_needed_ii=updec(need, 8),
        C0=updec(C0, 10), D=lodec(g['D'], 8), Z=lodec(g['Z'], 8), C0_over_D=updec(C0/g['D'], 8), room=lodec(g['D'] - C0, 8),
        M=str(g['M']), B=str(g['B']), A=str(g['A']), Kbar=str(g['Kb']), loss=updec(g['loss'], 10), bprime=lodec(g['bp'], 10),
        companion_ii=comp)

# ---------- Block H. Named hypotheses ----------
print('\n== Block H. Named hypotheses (premises of T2.7, Lemma KB, Theorem B, H4-R, Proposition FG, HF1-NEAR, route F-a)')
HYP = [
    ('H-B', 'whole-plane background: lambda_max H <= -beta_*, |grad h_*| <= g_*, ||Sym Du||_op <= s_* on R^2 (chain item 3; N0 of H4-R; RC-5)',
     'supplied' if cover_ok else 'OPEN', 'block A1'),
    ('H-RC', 'RC-1 to RC-10 of V11-2 (a) for h_* (structural: the exact-potential class, AT-674, AT-675; quantitative: chain items 2, 3)',
     'OPEN', 'through H-B'),
    ('H1', 'actual generator: closed generator, core, weighted semigroup and graph comparison on a reference ball containing K(R_*, M)'
     ' (AT-237 bridge)', 'OPEN', 'conditionally reduced (AT-600; Lemma KB, AT-772, AT-832) to H-B and the source bounds'),
    ('H2', 'full L^2 inverse of L_* + U[k].grad with rate beta_0* on the ball (T2.7, AT-123; E-v11-2); ||z||_2 <= R_* for z = T(k)',
     'OPEN', 'through H-B (g_* <= 1/4) and H1'),
    ('H3', '(R3/R5) of Theorem B and N(F_*) < infinity', 'retained', 'N(F_*) <= n CONFIRMED; R3/R5 imported with their hypotheses'),
    ('H-BALL', 'the reference ball is the full real S1 ball B(Rbar, Mbar), no ell restriction, with the center matrix premise of Lemma KB',
     'OPEN', 'rectangle and loss CONFIRMED (AT-772); the center matrix premise is H-B'),
    ('H4-COMP', 'the join of the near form with H4-R and the far form (NEAR_CHECK_v01 H4): E(g) <= -b0 ||g||^2 + C0 ||h||^2 from P0 + DR,'
     ' FG with the far rule (AT-513, AT-624) and HF1-NEAR for (TII + C_aw)[a_n]; reading (i) charges e_up to c + 1 - q - b0,'
     ' reading (ii) to beta_* - eps_R - b0', 'OPEN' if reading == 'undecided' else 'supplied (reading %s)' % reading,
     'Theorem H4-R as stated gives (ii); (i) is (ii) at beta_* = c + 1 - q; theory_audit and theory_agent_1 are asked which implication is accepted'),
    ('H4-REST', 'the other pieces of D_rem^n, T_IS, C_tr and C_vs1 to C_vs3, in NE form with eps_rest and C_rest (T2_H4_v01 NE-lo, NE-vs),'
     ' or charged to the far slack G - A_far under FG', 'OPEN', 'no 013 bound; stand-ins eps_rest = C_rest = 0'),
    ('H-N1', 'NEAR_CHECK_v01 H1 to H3: N1 for the actual a_n, the whole-plane core split and theory_audit condition 4 for the erflog cut',
     'OPEN', 'theory_agent_1 NEAR_CHECK_v01 section 3'),
    ('H-N3', 'N3 at mu 72, nu 1/40: certified kernel uppers', 'supplied', 'AT-1491, AT-1492 (mu 72 only)'),
    ('H-NEARU', 'certified uppers of Lambda_+(a_n), ||(a_n)_+||_1, sup((a_n)_- W^2), sup((a_n)_+ W^2) and D4, D5, D6 of a_n on R^2',
     'OPEN', 'FLOAT stand-ins in blocks E and F; ledger row G3'),
    ('H-TAIL', 'NR-25 (i), (iii), NR-30, the radial identity with K_m, NR-32', 'supplied',
     'AT-1344 to AT-1346, AT-1453, AT-1454, AT-1512, AT-1513'),
    ('H-FA', 'analytic premises of route F-a: AE-CS (AT-1698), Corollary CS-W and Proposition DW, HSB (AT-695), the source013 calculus,'
     ' tail-table certificate, Leibniz and Faa di Bruno estimates, singleton repair, CS-W homogeneity', 'retained',
     'the far scalar inequality is CONFIRMED conditional on them'),
    ('H-REG', 'V11-2 (d), stronger Hoelder regularity: its own premises, delta > alpha/(2c - 2)', 'OPEN', 'chain item 9; not needed for (a), (b)'),
]
for hname, text, st, cite in HYP:
    RES.append(dict(block='H', name=hname, statement=text, status=st, value='', inputs=[], standins=[], note=cite))
    print('[H] %s %s: %s | %s' % (st, hname, text, cite))

# ---------- Block I. Verdict and the statement that would follow ----------
print('\n== Block I. Verdict')
common = [r for r in RES if r['block'] in ('N', 'A', 'B', 'C', 'D') and '[' not in r['name']]
hyp_ok = all(r['status'] in ('supplied', 'retained') or r['status'].startswith('supplied') for r in RES if r['block'] == 'H' and r['name'] != 'H-REG')
cert_case = None
for lab, cd in CASES.items():
    need = ['A3', 'E0', 'F1', 'G1', 'G2', 'G3', 'G4', 'N2', 'N3'] + (['E1'] if reading == 'i' else ['E2'] if reading == 'ii' else [])
    rows = [r for r in RES if r['name'] in [x + cd['tag'] for x in need]]
    cd['checks'] = {r['name']: r['status'] for r in RES if r['name'].endswith(cd['tag'])}
    if reading in ('i', 'ii') and hyp_ok and all(r['status'] == 'PASS' for r in common + rows): cert_case = lab
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
out = dict(version='closure_check v01', inputs=os.path.relpath(path, HERE), inputs_sha256=sha(path),
           program_sha256=sha(os.path.abspath(__file__)), h4_reading=reading, verdict=verdict, results=RES, cases=CASES,
           common=dict(cap=str(cap), far_margin=str(rhs - lhs), s_max_lower=frlo(smax, 12), R_star_upper=frup(Rs, 18),
                       cover_gaps_union=sg(g1), cover_gaps_with_roots=sg(g2)),
           seconds=round(time.time() - t_start, 2))
json.dump(out, open(os.path.join(HERE, 'closure_check_v01.json'), 'w'), indent=1)
print('wrote closure_check_v01.json (%.1f s)' % (time.time() - t_start))

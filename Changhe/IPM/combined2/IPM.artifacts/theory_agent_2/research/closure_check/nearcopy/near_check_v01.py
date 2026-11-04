"""near_check_v01 (theory_agent_1, 2026-11-04 shift 7): the near part of the final closure check of coordinator 07:08Z item
3(a) (theory_agent_1 note 83). A conditional program: every input is a named parameter of near_params_v01.json with a
direction, a status and a source; the arithmetic is outward (python-flint arb, 256 bits), and every comparison is
decided only when the whole ball lies on one side.

For each case (b0, mu) it evaluates
  (a) the budget inequality (R1) of HF1-NEAR (AT-691) with tail B (AT-757), the quartic low cut (NR-27; AT-1094,
      AT-1134) and the core split a_n = a_c + a_r (NR-25, NR-30, NR-32):
        e_up = (1 + q^2) max(Lambda_+, 8 (2c - 1))/(2 mu^2) + A4c (1024 c + M4^+(a_r))/mu^4
               + tail_B(a_c) + tail_B(a_r) + t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi))  <=  c + 1 - q - b0,
      A4c = pi^2 (1 + c_aw/2) + C_D/2, c_aw = 2 q^2 (sinh(x0)/x0)^2, x0 = (q/2) log 2,
      M4^+(a_r) = ((D4 D6 + D5^2)/(2 pi))^(1/2) at D_m = D_m(a_r), D_m(a_r)^2 <= D_m(a_n)^2 - K_m,
      tail_B(a) = (4/3)^q T_q(a; 3 mu/4) + (8/mu)^q T_q(a; mu/2),
      T_q(a_c; v) <= U_q(v) = c pi^(1/2) v^(q + 3/2) e^(-v/2)/(2 (v - 2q - 1))      (NR-32, v > 2q + 1),
      T_q(a_r; v) <= v^(q - 5) D6(a_r)/(4 pi (5 - q))^(1/2)                          (NR-25 (i), m = 6);
  (b) the near price P_HF = 2^sigma [sup(|a_n| W^2) kappa_0 kappa_2q + (1 - t)^-1 sup((a_n)_+ W^2) 2 kappa_j^2],
      with sup(|a_n| W^2) = max(sup((a_n)_- W^2), sup((a_n)_+ W^2)), an upper for the near constant C_N, and its
      comparison with the allowance D (the room D - P_HF is what is left for the far and remainder charges of H4-R);
  (c) the (R1) threshold: the largest D6(a_n) upper, on a grid of 1/10, at which (a) passes with the other inputs.
Every term is nondecreasing in each upper and nonincreasing in each lower (K_m, D), so the conclusions hold for any
certified bounds that are at least as good as the parameter values.

What follows if (a) and (b) pass with every input certified and the hypotheses H1 to H4 of NEAR_CHECK_v01.md hold:
for every h with g = J^q W h in L^2, (TII + C_aw)[a_n](g) <= (c + 1 - q - b0) ||g||^2 + P ||h||^2 with P the printed
upper, so C_N <= P <= D at that (b0, mu). The far charges, H4-R, Theorem B and Lemma KB are theory_agent_2's part.
With FLOAT or UNAUDITED inputs the output is a dry run and proves nothing.

Usage: python3 -B near_check_v01.py [params.json] > near_check_v01.out; writes near_check_v01.result.json."""
import hashlib, json, os, sys
from fractions import Fraction as Fr
from flint import arb, ctx
ctx.prec = 256
here = os.path.dirname(os.path.abspath(__file__))
pfile = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'near_params_v01.json')
P = json.load(open(pfile))
CERT = ('FIXED', 'EXACT', 'CONFIRMED')

def frac(s):
    """exact rational of a decimal or fraction string, or of 'x - y' with such terms"""
    s = s.strip()
    if ' - ' in s:
        a, b = s.split(' - ')
        return frac(a) - frac(b)
    return Fr(s)

def A(x):
    f = frac(x) if isinstance(x, str) else Fr(x)
    return arb(f.numerator)/arb(f.denominator)

def dec(f, n, up):
    """decimal string with n significant digits, rounded up (up True) or down from the rational f"""
    if f == 0: return '0'
    a = abs(f); e = 0
    while a >= Fr(10)**(e + 1): e += 1
    while a < Fr(10)**e: e -= 1
    m = a*Fr(10)**(n - 1 - e)
    k = -((-m.numerator)//m.denominator) if up == (f > 0) else m.numerator//m.denominator
    d = str(k)
    return '%s%s.%se%d' % ('-' if f < 0 else '', d[0], d[1:], e + len(d) - n)

def exact(x):
    me = x.mid().man_exp()
    return Fr(int(me[0]))*Fr(2)**int(me[1])

def upper_dec(x, n=10): return dec(exact(x.upper()), n, True)
def lower_dec(x, n=10): return dec(exact(x.lower()), n, False)

used = {}
def par(group, name, case=None):
    d = (case if case is not None else P[group])[name]
    used[name if case is None else '%s[%s]' % (name, case['label'])] = d
    return A(d['value'])

q, sigma, r0, c, CD, t, nu = (par('fixed', k) for k in ('q', 'sigma', 'r0', 'c', 'C_D', 't', 'nu'))
par('fixed', 'lam_k')
assert r0 == A('1/2') and sigma == 1, 'NR-32 and the price use r0 = 1/2 and sigma = 1'
pi = arb.pi()
cap = c + 1 - q
LPF = 8*(2*c - 1)
x0 = q/2*arb(2).log(); caw = 2*q**2*(x0.sinh()/x0)**2
A4c = pi**2*(1 + caw/2) + CD/2
EPSI = 1/(8*(2*pi).sqrt())
K = {m: par('global', 'K%d' % m) for m in (4, 5, 6)}
G = {k: par('global', k) for k in ('sup_neg_aW2', 'sup_pos_aW2', 'L1_pos', 'Lambda_plus')}
DN0 = {m: par('global', 'D%d_an' % m) for m in (4, 5, 6)}

def U(v):
    assert (v > 2*q + 1) is True
    return c*pi.sqrt()*v**(q + A('3/2'))*(-v/2).exp()/(2*(v - 2*q - 1))

def tc6(v):
    return v**(q - 5)/(4*pi*(5 - q)).sqrt()

def budget(b0, mu, DN):
    """the terms of e_up and the margin c + 1 - q - b0 - e_up (balls); None if some D_m(a_n)^2 <= K_m"""
    dr = {}
    for m in (4, 5, 6):
        x = DN[m]**2 - K[m]
        if not (x > 0) is True: return None
        dr[m] = x.sqrt()
    lam = G['Lambda_plus'].max(LPF)
    terms = {
        'Lambda term (1 + q^2) max(Lambda_+, 8 (2c - 1))/(2 mu^2)': (1 + q**2)*lam/(2*mu**2),
        'M4 term A4c (1024 c + M4^+(a_r))/mu^4': A4c*(1024*c + ((dr[4]*dr[6] + dr[5]**2)/(2*pi)).sqrt())/mu**4,
        'tail_B(a_c) (NR-32)': (A('4/3'))**q*U(3*mu/4) + (8/mu)**q*U(mu/2),
        'tail_B(a_r) (NR-25 (i), m = 6)': ((A('4/3'))**q*tc6(3*mu/4) + (8/mu)**q*tc6(mu/2))*dr[6],
        'e_nu term t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi))': G['L1_pos']*nu**2*EPSI/t}
    e = sum(terms.values(), arb(0))
    return terms, e, cap - b0 - e, dr

res = {'program': 'near_check_v01.py', 'params': os.path.basename(pfile),
       'params_sha256': hashlib.sha256(open(pfile, 'rb').read()).hexdigest(),
       'program_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'cases': []}
print(__doc__)
print('Parameter file %s (SHA256 %s)' % (res['params'], res['params_sha256']))
print('Constants (balls): cap = c + 1 - q = %s; 8 (2c - 1) = %s; c_aw = %s; A4c = %s; 1024 c = %s'
      % tuple(x.str(12, radius=True) for x in (cap, LPF, caw, A4c, 1024*c)))
print('K_m (exact rationals, decimal): ' + ', '.join('K%d %s' % (m, K[m].str(15)) for m in (4, 5, 6)))
for case in P['cases']:
    b0, mu = A(case['b0']), A(case['mu'])
    k0, k2q, kj, Dal = (par(None, k, case) for k in ('kappa_0', 'kappa_2q', 'kappa_j', 'D_allow'))
    side = {'mu >= 1': bool((mu >= 1) is True), '2 nu <= mu': bool((2*nu <= mu) is True),
            'mu/2 > 2q + 1 (NR-32)': bool((mu/2 > 2*q + 1) is True), '0 < b0 < c + 1 - q': bool((b0 > 0) is True and (b0 < cap) is True),
            'b0 > 0.152070 (loss of Lemma KB, AT1688)': bool((b0 > A('0.152070')) is True)}
    out = budget(b0, mu, DN0)
    if out is None:
        print("\nCase %s: some D_m(a_n) upper has D_m(a_n)^2 <= K_m (inconsistent inputs); skipped" % case["label"]); continue
    terms, e, marg, dr = out
    s1 = G['sup_neg_aW2'].max(G['sup_pos_aW2'])
    pa = 2**sigma*s1*k0*k2q; pb = 2**sigma*G['sup_pos_aW2']*2*kj**2/(1 - t); PHF = pa + pb
    room = Dal - PHF
    # (c) threshold for D6(a_n) on the grid 1/10 (each probe is an outward check)
    lo = Fr(int(exact(K[6].sqrt().upper())*10) + 1, 10); hi = Fr(10**6)
    def ok(x):
        o = budget(b0, mu, {**DN0, 6: A(x)})
        return o is not None and (o[2] >= 0) is True
    if ok(lo):
        while hi - lo > Fr(1, 10):
            mid = Fr(int((lo + hi)/2*10), 10)
            if mid <= lo: break
            if ok(mid): lo = mid
            else: hi = mid
        thr = lo
    else:
        thr = None
    bud_pass = bool((marg >= 0) is True); price_pass = bool((room >= 0) is True)
    st = {k: v['status'] for k, v in used.items() if '[' not in k or k.endswith('[%s]' % case['label'])}
    open_inputs = sorted(k for k, s in st.items() if s not in CERT)
    conds = sorted(set(v['conditions'] for k, v in used.items() if 'conditions' in v and k.endswith('[%s]' % case['label'])))
    print('\nCase %s: b0 = %s, mu = %s' % (case['label'], case['b0'], case['mu']))
    print('  side conditions: ' + '; '.join('%s %s' % (k, 'yes' if v else 'NO') for k, v in side.items()))
    print('  D_m(a_r) uppers from the radial identity: ' + ', '.join('D%d %s' % (m, upper_dec(dr[m], 9)) for m in (4, 5, 6)))
    print('  | term of e_up | upper |')
    print('  |---|---:|')
    for k, v in terms.items(): print('  | %s | %s |' % (k, upper_dec(v, 9)))
    print('  | e_up | %s |' % upper_dec(e, 9))
    print('  | c + 1 - q - b0 | %s (ball) |' % (cap - b0).str(12))
    print('  (a) budget margin c + 1 - q - b0 - e_up >= %s: %s' % (lower_dec(marg, 9), 'PASS' if bud_pass else 'NOT DECIDED OR FAILS'))
    print('  (b) P_HF <= %s (kappa_0 kappa_2q part %s, kappa_j part %s); D >= %s; P_HF/D <= %s; room D - P_HF >= %s: %s'
          % (upper_dec(PHF, 9), upper_dec(pa, 7), upper_dec(pb, 7), upper_dec(Dal, 9), upper_dec(PHF/Dal, 7),
             lower_dec(room, 7), 'PASS' if price_pass else 'NOT DECIDED OR FAILS'))
    print('  (c) (R1) threshold: (a) passes for every D6(a_n) upper <= %s at the other inputs' % (('%.1f' % float(thr)) if thr is not None else 'none'))
    print('  inputs that are not certified: %s' % (', '.join('%s (%s)' % (k, st[k]) for k in open_inputs) or 'none'))
    print('  conditions of the certified inputs: %s' % ('; '.join(conds) or 'none'))
    verdict = ('conditional conclusion available (all inputs certified)' if bud_pass and price_pass and not open_inputs
               else 'DRY RUN: proves nothing' if open_inputs else 'check fails or is not decided')
    print('  status: %s' % verdict)
    res['cases'].append({'label': case['label'], 'b0': case['b0'], 'mu': case['mu'], 'side_conditions': side,
                         'e_terms_upper': {k: upper_dec(v, 12) for k, v in terms.items()}, 'e_up': upper_dec(e, 12),
                         'budget_margin_lower': lower_dec(marg, 12), 'budget_pass': bud_pass,
                         'C_N_upper': upper_dec(PHF, 12), 'D_lower': upper_dec(Dal, 12), 'P_over_D_upper': upper_dec(PHF/Dal, 12),
                         'room_D_minus_P_lower': lower_dec(room, 12), 'price_pass': price_pass,
                         'R1_threshold_D6_an': str(thr) if thr is not None else None,
                         'inputs_not_certified': open_inputs, 'conditions': conds, 'status': verdict})
json.dump(res, open(os.path.join(here, 'near_check_v01.result.json'), 'w'), indent=1)
print('\nwrote near_check_v01.result.json')

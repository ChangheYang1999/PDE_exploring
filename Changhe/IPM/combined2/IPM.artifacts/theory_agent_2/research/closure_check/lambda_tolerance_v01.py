"""lambda_tolerance (theory_agent_2, 2026-11-04, version 01): exact arithmetic for the Lambda_+ revision of AT2364 to AT2366.
Not a certificate of any input. It answers: if a certified global upper Lambda_+(a_n) <= Lam (Lam >= 8(2c - 1)) is
supplied, what does E2 of closure_check_v03 (e_up + eps_rest <= beta_* - b0) need at the two fixed cases, and up to
which Lam does a given rate beta_* still suffice?
Facts used (each read from the frozen NEAR_CHECK_v02 copy in nearcopy_v02/):
- NEAR_CHECK_v02 computes the Lambda term as (1 + q^2) max(Lambda_+, 8(2c - 1))/(2 mu^2) and uses Lambda_+ nowhere
  else; its printed e_up is >= the exact sum of the five term uppers (its interface field). With the parameter
  20.862082 < 8(2c - 1) the maximum is the floor F = 8(2c - 1).
- Hence, for a certified Lambda_+ <= Lam with Lam >= F, e_up(Lam) = e_up_printed + (1 + q^2)(Lam - F)/(2 mu^2) is an
  upper of the same near loss, exactly. C_N_upper (the price) does not contain Lambda_+, so G4 is unchanged.
- E2 holds iff beta_* >= b0 + e_up(Lam) + eps_rest; equivalently Lam <= F + (beta_* - b0 - e_up_printed - eps_rest)
  2 mu^2/(1 + q^2).
Rates used: 704955805507/10^12, the regional matrix lower of AT2373 (CONFIRMED on r^2 in [0, 17/47] and
[35/93, 61/67] only; AT2374 OPEN, so here it is a hypothetical whole-plane value), and c + 1 - q, the largest
whole-plane rate possible (AT-211). eps_rest = 0 is the stand-in of inputs_v03.json; the formulas are linear in it.
Every value is an exact rational; displayed decimals are rounded in the safe direction (Lam tolerances down,
needed rates up). Usage (from research/closure_check/): python3 -B lambda_tolerance_v01.py > lambda_tolerance_v01.out"""
import hashlib, json, math, os, re, time
from fractions import Fraction as Fr
t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ND = os.path.join(HERE, 'nearcopy_v02')
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
PIN = {'near_check_v02.py': '0170560ec8ff6952e2c3458c35ec0a1f7ce639ef096200a186e297f6832f298b',
       'near_check_v02.result.json': '2d4cffce6b60b12546da88c5348b4f16b4286db0562b177835f211a9e1aa319f'}
for f, h in PIN.items():
    assert sha(os.path.join(ND, f)) == h, f
src = open(os.path.join(ND, 'near_check_v02.py')).read()
assert src.count("G['Lambda_plus']") == 1 and "lam = G['Lambda_plus'].max(LPF)" in src and '(1 + q**2)*lam/(2*mu**2)' in src
assert len(re.findall(r'\blam\b', src)) == 2, 'Lambda_+ enters only the first term'
R = json.load(open(os.path.join(ND, 'near_check_v02.result.json')))
P = json.load(open(os.path.join(ND, R['params'])))
assert sha(os.path.join(ND, R['params'])) == R['params_sha256']
def dec(s):
    s = s.strip()
    if 'e' in s:
        m, e = s.split('e'); return Fr(m)*Fr(10)**int(e)
    return Fr(s)
q, c = Fr(P['fixed']['q']['value']), Fr(P['fixed']['c']['value'])
assert q == Fr(21, 10) and c == Fr(4076476460239181, 2**51)
lam_par = dec(P['global']['Lambda_plus']['value'])
F = 8*(2*c - 1); cap = c + 1 - q
assert lam_par < F
def qdn(x, d):
    e = math.floor(math.log10(abs(float(x)))) - d + 1; s = Fr(math.floor(x/Fr(10)**e))*Fr(10)**e; assert s <= x; return s
def qup(x, d):
    e = math.floor(math.log10(abs(float(x)))) - d + 1; s = Fr(math.ceil(x/Fr(10)**e))*Fr(10)**e; assert s >= x; return s
def show(x, d=10): return '%.*g' % (d + 2, float(x))
RATES = [('beta_reg = 704955805507/10^12 (AT2373, regional; hypothetical whole-plane)', Fr(704955805507, 10**12)),
         ('cap = c + 1 - q (AT-211; no whole-plane rate exceeds it)', cap)]
eps = Fr(0)
print(__doc__.split('\n')[0])
print('NEAR_CHECK_v02 program and result match the pinned SHA256; parameter file %s matches the result' % R['params'])
print('F = 8(2c - 1) = %s (exact) = %s...; the parameter Lambda_plus = %s lies below F by %s (exact; AT2365)'
      % (F, show(F, 12), P['global']['Lambda_plus']['value'], F - lam_par))
out = dict(version='lambda_tolerance v01', F=str(F), cap=str(cap), eps_rest=str(eps), cases=[])
for cs in R['cases']:
    b0, mu, e_p = Fr(cs['b0']), Fr(cs['mu']), dec(cs['e_up'])
    k = (1 + q**2)/(2*mu**2)
    print('\nCase %s (b0, mu) = (%s, %s): printed e_up = %s; Lambda coefficient (1 + q^2)/(2 mu^2) = %s = %s'
          % (cs['label'], b0, mu, cs['e_up'], k, show(k)))
    need0 = b0 + e_p + eps
    print('  rate needed at Lam = F: b0 + e_up + eps_rest = %s (exact) <= %s' % (need0, show(qup(need0, 12), 12)))
    rec = dict(label=cs['label'], b0=str(b0), mu=str(mu), e_up_printed=cs['e_up'], coeff=str(k), need_at_F=str(need0))
    for name, beta in RATES:
        room = beta - need0
        tol = F + room/k
        print('  %s: room beta - b0 - e_up - eps_rest = %s (exact) >= %s; Lam tolerance F + room/coeff = %s (exact)'
              ' >= %s, i.e. Lam - F <= %s' % (name, room, show(qdn(room, 10)), tol, show(qdn(tol, 10)), show(qdn(tol - F, 10))))
        rec['tol_' + ('reg' if beta != cap else 'cap')] = dict(room=str(room), Lam_tol=str(tol), Lam_tol_down=show(qdn(tol, 10)))
    for Lam in (Fr(21), Fr(22), Fr(23), Fr(25), Fr(30), Fr(35), Fr(40)):
        nd = need0 + k*(Lam - F)
        print('    certified Lambda_+ <= %s: e_up <= %s, rate needed %s (rounded up); %s the regional value, %s the cap'
              % (Lam, show(qup(e_p + k*(Lam - F), 10)), show(qup(nd, 10)),
                 'below' if nd <= RATES[0][1] else 'ABOVE', 'below' if nd <= cap else 'ABOVE'))
    out['cases'].append(rec)
json.dump(out, open(os.path.join(HERE, 'lambda_tolerance_v01.json'), 'w'), indent=1)
print('\nwrote lambda_tolerance_v01.json (%.2f s). Exact arithmetic on frozen inputs; it certifies no near input.'
      % (time.time() - t0))

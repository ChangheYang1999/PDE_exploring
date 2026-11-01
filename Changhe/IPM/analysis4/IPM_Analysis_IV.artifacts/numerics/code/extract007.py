"""Extract c_l and f_1 exactly from Candidate 007 and compare the exact recursion with its stationary branches 2..8."""
import os, sys, math, json, time
sys.path.insert(0, '.')
from ffcore import *
ROOT = os.environ.get('IPM_PROJECT_ROOT', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))   # project root (lane/code/.. /..)
cl, br = load_candidate007(ROOT)
R = RingQ()
gamma = 1 / cl; delta = 1 - gamma
print('c_l =', cl, float(cl)); print('gamma =', float(gamma), 'delta =', float(delta))
def pn(n): return 1 - n * delta
f = {}
for j in sorted(br):
    n = j + 1
    f[n] = f_from_C(br[j], pn(n))
    while len(f[n]) > 1 and f[n][-1] == 0: f[n].pop()
a1 = f[1]
print('f_1: number of sine harmonics', len(a1), 'frequencies 1..', 2 * (len(a1) - 1) + 1)
for k, x in enumerate(a1):
    print(f'  a_1,{k}  sin({2*k+1} theta): {float(x):+.12e}   bits(num,den)=({int(x.p).bit_length()},{int(x.q).bit_length()})')
qn = math.sqrt(math.pi / 4 * sum(float(x) ** 2 for x in a1))
print('quarter-circle L2 norm of f_1 =', qn, '(manifest Theta_0 quarter_norm 16.57100026302882)')
print('full-circle L2 =', 2 * qn, 'A_0 = sum|a| =', sum(abs(float(x)) for x in a1), 'Linf grid =', linf_odd_sine([float(x) for x in a1]))
# sign / positivity properties of f_1 on (0, pi/2)
th = np.linspace(0, math.pi, 20001); v = eval_odd_sine([float(x) for x in a1], th)
print('f_1 on (0,pi): min', v.min(), 'max', v.max(), 'argmax theta/pi', th[np.argmax(v)] / math.pi, 'sign changes', int(np.sum(np.diff(np.sign(v[1:-1])) != 0)))
dv = np.gradient(v, th); print('monotone on (0,pi/2)?', bool(np.all(dv[(th > 1e-3) & (th < math.pi / 2 - 1e-3)] > 0)), 'zeros of derivative in (0,pi/2):', int(np.sum(np.diff(np.sign(dv[(th > 0) & (th < math.pi / 2)])) != 0)))
json.dump({'c_l_exact': str(cl), 'c_l_float': float(cl), 'gamma_float': float(gamma), 'delta_float': float(delta),
           'f1_sine_coefficients_exact': [str(x) for x in a1], 'f1_sine_coefficients_float': [float(x) for x in a1],
           'frequencies': [2 * k + 1 for k in range(len(a1))], 'quarter_L2': qn,
           'C1_cos_coefficients_exact': [str(x) for x in br[0]], 'C1_cos_coefficients_float': [float(x) for x in br[0]],
           'note': 'f_1 = -[(p+1) sin D + cos D^prime], D = C^double-prime + (p+3)^2 C, p = gamma, from branch 0 leading moments of Candidate 007 (sum of generator coefficients per cos(2m theta) mode)'},
          open('../notes/cand007_f1.json', 'w'), indent=1)
# ---- exact recursion vs branches 1..7
t0 = time.time()
ff = FarField(R, cl, a1)
for n in range(2, 9):
    ff.step()
    mine = ff.f[n]; theirs = f[n]
    L = max(len(mine), len(theirs)); mine = mine + [fmpq(0)] * (L - len(mine)); theirs = theirs + [fmpq(0)] * (L - len(theirs))
    diff = [x - y for x, y in zip(mine, theirs)]
    maxdiff = max(abs(float(x)) for x in diff); exact = all(x == 0 for x in diff)
    print(f'order {n}: K_mine={len(ff.f[n])-1} K_007={len(f[n])-1}  exact equal: {exact}  max|diff|={maxdiff:.3e}  max|f_n|={max(abs(float(x)) for x in theirs):.3e}  L2={ff.stats[n]["L2"]:.4e} bits={ff.stats[n]["max_bits"]} t={time.time()-t0:.1f}s')

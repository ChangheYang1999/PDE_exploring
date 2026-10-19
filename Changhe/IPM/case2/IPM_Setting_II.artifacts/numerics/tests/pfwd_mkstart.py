"""Make a warm-start state file for code/pfwd_exitmap.py from a saved state and a new datum: g_new = g_old exp(F_new - F_old) (r/r_max)^(p_old - p_new).
Usage: python3 tests/pfwd_mkstart.py src.npz out.npz "a1,..,aK" p  [idx=k  (for bscan *_states.npz: member index)]"""
import sys, json; import numpy as np
src, out = sys.argv[1], sys.argv[2]; a_new = np.array([float(v) for v in sys.argv[3].split(',')]); p_new = float(sys.argv[4])
idx = int(sys.argv[5].split('=')[1]) if len(sys.argv) > 5 else None
d = np.load(src, allow_pickle=True)
if 'X' in d.files:
    k = idx if idx is not None else 0; g = d['g'][k]; x = d['X'][k]; a_old = x[:-1]; p_old = float(x[-1])
else:
    g = d['g']; a = json.loads(str(d['args'])); p_old = float(a['p']); a_old = np.array(a['par']) if 'par' in a else d['x'][:-1]
lr = d['lr']; th = d['th']; r = np.exp(lr)
def Fof(coef):
    F = np.zeros_like(th)
    for j, c in enumerate(coef):
        n = j + 1; F = F + c * (np.sin(n * th) if n % 2 == 1 else np.cos(n * th))
    return F
g_new = g * np.exp(Fof(a_new) - Fof(a_old))[None, :] * ((r / r[-1]) ** (p_old - p_new))[:, None]
np.savez(out, g=g_new, lr=lr, th=th, x=np.concatenate([a_new, [p_new]]), args=json.dumps(dict(p=p_new, kind='expf', par=[float(v) for v in a_new])))
print('wrote', out, 'from', src, 'member', idx, 'p_old', p_old, '-> p', p_new, 'Nth', len(th))

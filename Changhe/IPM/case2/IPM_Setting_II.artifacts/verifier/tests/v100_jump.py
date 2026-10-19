"""V100 aux: where do the panel-Lagrange interpolants of alpha, beta jump across panel edges? For each interior edge: the max over
th of |left - right| / max|alpha| and its angle; top 8 edges; and alpha, beta, |V|/r at the worst (edge, angle) from both sides.
CPU, one thread. Usage: python3 tests/v100_jump.py OWN.npz"""
import sys, math, json, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from fwdstat import FwdStat
from charsolve import lagrange_eval
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
ppu = int(args['ppu'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=ppu, q=8, nt=nt, dti=0.01, nstep=800, dev='cpu')
rho = torch.tensor(d['rho'], dtype=DT)
al, be, _, _ = F.fields(rho); q = F.S.q
edges = np.concatenate([[0.0], np.exp(np.linspace(F.tmin, F.tmax, int(round((F.tmax - F.tmin)*ppu)) + 1))])
xg = np.polynomial.legendre.leggauss(q)[0]
Lm = torch.tensor(lagrange_eval(xg, 1.0), dtype=DT); Lp = torch.tensor(lagrange_eval(xg, -1.0), dtype=DT)
am = float(al.abs().max()); deg = np.degrees(F.th.numpy()); rows = []
for e in range(2, len(edges) - 1):
    la = Lm @ al[(e - 1)*q:e*q]; ra = Lp @ al[e*q:(e + 1)*q]; lb = Lm @ be[(e - 1)*q:e*q]; rb = Lp @ be[e*q:(e + 1)*q]
    ja = (la - ra).abs(); jb = (lb - rb).abs(); j = int(torch.argmax(ja))
    rows.append((float(ja.max())/am, float(jb.max())/am, round(math.log(edges[e]), 3), round(float(deg[j]), 2),
                 [round(float(la[j]), 4), round(float(ra[j]), 4)], [round(float(lb[j]), 4), round(float(rb[j]), 4)],
                 int((ja > 1e-3*am).sum())))
rows.sort(key=lambda r: -r[0])
print(json.dumps(dict(state=fn.split('/')[-1], max_alpha=am, top=[[float('%.3g' % r[0]), float('%.3g' % r[1])] + list(r[2:]) for r in rows[:8]])))

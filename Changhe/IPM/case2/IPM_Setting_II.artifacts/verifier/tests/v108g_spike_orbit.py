# V108 (7): forward orbit of the spike node of the -1.1 x-odd Ritz vector and its exit-angle sensitivity; min |V|/r along it. CPU.
import sys, math, json, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
d = np.load('runs/v74_a2-1.1_c07.npz', allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=0.01, nstep=800, dev='cpu')
rho = torch.tensor(d['rho'], dtype=DT)
al, be, _, _ = F.fields(rho)
t = F.t_nodes.numpy(); i = int(np.argmin(np.abs(t + 6.456))); j = int(np.argmin(np.abs(np.degrees(F.th.numpy()) - 75.94)))
t0 = float(t[i]); th0 = float(F.th[j]); print('node', t0, math.degrees(th0), 'alpha', float(al[i, j]), 'beta', float(be[i, j]), '|V|/r', math.hypot(float(al[i, j]), float(be[i, j])))
dts = np.array([0, 1e-3, -1e-3, 0, 0, 1e-2, -1e-2, 0, 0]); dths = np.radians(np.array([0, 0, 0, 1e-2, -1e-2, 0, 0, 0.1, -0.1]))
tt = torch.tensor(t0 + dts, dtype=DT); hh = torch.tensor(th0 + dths, dtype=DT)
the, s, nb = F.trace_s(al, be, tt, hh, 0.03, 8000)
for k in range(len(dts)):
    print('dt %+.0e dth_deg %+.2f exit_deg %.4f s %.4f' % (dts[k], math.degrees(dths[k]), math.degrees(float(the[k])) % 360, float(s[k])))
print('not exited', nb, F.last_trace)
# min |V|/r along the orbit of the node: trace in pieces
au = F.Imat @ al; bu = F.Imat @ be
T = torch.tensor([t0], dtype=DT); H = torch.tensor([th0], dtype=DT); mins = 1e9; where = None
for n in range(4000):
    a = F.interp(au, T, H); b = F.interp(bu, T, H); w = torch.sqrt(a*a + b*b)
    if float(w) < mins: mins = float(w); where = (float(T), math.degrees(float(H)) % 360)
    T = T + 0.01*a/w; H = H + 0.01*b/w
    if float(T) >= F.tmax: break
print('min |V|/r along orbit %.4g at (t, deg) %s' % (mins, where))

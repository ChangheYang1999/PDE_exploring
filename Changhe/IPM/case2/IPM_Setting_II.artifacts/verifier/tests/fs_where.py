import sys, numpy as np, torch, math, json
sys.path.insert(0, 'code')
from fwdstat import FwdStat
d = np.load(sys.argv[1]); p = float(d['p'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=-12, tmax=10, ppu=3, q=8, nt=len(d['th']), dti=0.01, nstep=400)
rho = torch.tensor(d['rho'], device='cuda')
Tr, info = F.T(rho)
g = rho/F.R**p
D = ((Tr - rho)/F.R**p).abs()
D2 = D/ g.abs().amax(1, keepdim=True)
for name, M in (('abs', D), ('rel-to-ring-max', D2)):
    i = int(torch.argmax(M)); ir, it = divmod(i, F.nt)
    print(name, 'max %.3e at r %.3e th %.1f deg; g there %.3e, ring max g %.3e' % (float(M.max()), float(F.r[ir]), math.degrees(float(F.th[it])), float(g[ir, it]), float(g[ir].abs().max())))
# angular profile of the error on the worst ring
i = int(torch.argmax(D)); ir, it = divmod(i, F.nt)
print('worst ring: th(deg), g, err')
for j in range(0, F.nt, 4):
    print('%6.1f %.4e %.3e' % (math.degrees(float(F.th[j])), float(g[ir, j]), float(D[ir, j])))

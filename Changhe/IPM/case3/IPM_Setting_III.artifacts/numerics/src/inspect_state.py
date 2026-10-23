import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
st = torch.load(sys.argv[1]); dev='cuda'
mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev); mdl.gauge='inf'
b = st['b'].to(dev); cl = st['cl']
flds = mdl.fields(b); c = mdl.psi_xy0(flds).item()
print(f"cl={cl} gamma={mdl.gamma:.6f} p={mdl.p:.4f} c={c:.8f} a0={b[0,0].item():.6f} b(inf)={(mdl.rad.ext1_R@b).mean().item():.6f}")
r = mdl.rad.rR.cpu().numpy(); t = mdl.rad.tR.cpu().numpy()
bn = b.cpu().numpy()
print(" i      t          r        b(th~0)    b(th~pi/2)   mean_th b    Ur_r(th0)   U2y(th0)  Uth_r(th0)")
for i in range(0, mdl.N+1, max(1, mdl.N//24)):
    print(f"{i:3d} {t[i]:+.6f} {r[i]:12.4e} {bn[i,0]:12.6f} {bn[i,-1]:12.6f} {bn[i].mean():12.6f} {flds['Ur_r'][i,0].item():+.4e} {flds['U2y'][i,0].item():+.4e} {flds['Uth_r'][i,0].item():+.4e}")
# Chebyshev coefficient decay of mean b in t
bhat = mdl.ang.to_coef(b, 'EE').cpu().numpy()
# radial Chebyshev coefficients via least squares on Radau nodes
V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N+1)))
ck = np.linalg.lstsq(V, bhat[:,0], rcond=None)[0]
print("radial Chebyshev coefficients of the angular mean of b (every 4th):", np.array2string(np.abs(ck[::4]), precision=1, max_line_width=200))
print("angular coefficients at centre-ish/mid/far (rows 0, N/2, N):")
for i in [0, mdl.N//2, mdl.N]:
    print(f"  row {i}: ", np.array2string(np.abs(bhat[i,:8]), precision=2, max_line_width=200))
# singular vectors of the unforced coupled Jacobian
mdl2 = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev, couple_gamma=True); mdl2.gauge='inf'
J = mdl2.jacobian(b, cl)
U_, S, Vh = torch.linalg.svd(J)
nb = (mdl.N+1)*mdl.M
scal = -(mdl.rad.gR[:,None]*(mdl.rad.DR@b) + mdl.omegaR[:,None]*b)   # scaling generator in b (d/dlambda b_lambda)
scal_v = torch.cat([scal.reshape(-1), torch.zeros(1, device=dev)]); scal_v = scal_v/scal_v.norm()
print("smallest singular values:", S[-4:].cpu().numpy())
for k in range(1, 4):
    v = Vh[-k]
    bb = v[:nb].reshape(mdl.N+1, mdl.M)
    print(f"  v[-{k}]: cl-component {v[-1].item():+.3e}, |proj on scaling generator| {abs((v@scal_v).item()):.4f}, b-part: centre value {bb[0,0].item():+.3e}, far mean {(mdl.rad.ext1_R@bb).mean().item():+.3e}, max at row {bb.abs().max(1).values.argmax().item()} (t={t[bb.abs().max(1).values.argmax().item()]:+.4f})")

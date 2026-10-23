import sys, numpy as np, torch
sys.path.insert(0, 'numerics/src'); import ipm3
torch.set_default_dtype(torch.float64)
for gauge in ['inf', 'half']:
    mdl = ipm3.IPM3(N=24, M=6, L=1.0, gamma=0.6); mdl.gauge = gauge
    th = mdl.ang.theta
    b = 1.3*(1 + 0.6*mdl.rad.s2R[:, None]*torch.cos(2*th)[None, :]) + 0.2*mdl.rad.s2R[:, None]
    cl = 1/0.6; mu = 0.37; nb = 25*6
    F, E, flds = mdl.system(b, cl, mu=mu, forced=True)
    J = mdl.jacobian(b, cl, flds, forced=True)
    torch.manual_seed(1)
    for trial in range(2):
        du = torch.randn(nb+1); eps = 1e-6
        Fp,_,_ = mdl.system(b + eps*du[:nb].reshape(25,6), cl, mu=mu + eps*du[-1].item(), forced=True)
        Fm,_,_ = mdl.system(b - eps*du[:nb].reshape(25,6), cl, mu=mu - eps*du[-1].item(), forced=True)
        fd = (Fp-Fm)/(2*eps); print(f"gauge {gauge} forced-mode Jacobian vs FD: {(J@du - fd).abs().max().item()/(J@du).abs().max().item():.2e}")
    # also the plain (b, cl) mode with this gauge
    J = mdl.jacobian(b, cl, flds)
    du = torch.randn(nb+1); eps=1e-6
    Fp,_,_ = mdl.system(b + eps*du[:nb].reshape(25,6), cl + eps*du[-1].item()); Fm,_,_ = mdl.system(b - eps*du[:nb].reshape(25,6), cl - eps*du[-1].item())
    print(f"gauge {gauge} (b,cl)-mode Jacobian vs FD: {(J@du - (Fp-Fm)/(2*eps)).abs().max().item()/(J@du).abs().max().item():.2e}")

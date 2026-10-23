import sys, numpy as np, torch
sys.path.insert(0, 'numerics/src')
import ipm3
torch.set_default_dtype(torch.float64)
# radial differentiation on Radau and Lobatto grids
for N in [16, 32, 64, 128, 256]:
    rad = ipm3.Radial(N, 1.0, 2.5, 'cpu')
    for name, t, D in [('radau', rad.tR, rad.DR), ('lobatto', rad.tL, rad.DL)]:
        f = torch.exp(0.9*t)*torch.sin(3*t)
        df = 0.9*f + 3*torch.exp(0.9*t)*torch.cos(3*t)
        err = (D @ f - df).abs().max().item()
        # interpolation Radau->Lobatto
        print(f"N={N:4d} {name:8s} diff err {err:.2e}", end='')
    fL = torch.exp(0.9*rad.tL)*torch.sin(3*rad.tL); fR = torch.exp(0.9*rad.tR)*torch.sin(3*rad.tR)
    print(f"   interp R->L {(rad.P_RL @ fR - fL).abs().max().item():.2e}  L->R {(rad.P_LR @ fL - fR).abs().max().item():.2e}  ext1 {(rad.ext1_R @ fR).item() - np.exp(0.9)*np.sin(3):.2e}")
    # inverse map
    r = rad.rR.numpy()[1:]; t = rad.t_of_r(r); print(f"      t_of_r err {np.abs(t - rad.tR_np[1:]).max():.2e}")
# angular
for M in [8, 16, 32]:
    ang = ipm3.Angular(M, 'cpu')
    th = ang.theta
    for cls, f, df in [('EE', torch.cos(2*th)+0.3*torch.cos(6*th), -2*torch.sin(2*th)-1.8*torch.sin(6*th)),
                       ('OO', torch.sin(2*th)+0.3*torch.sin(4*th), 2*torch.cos(2*th)+1.2*torch.cos(4*th)),
                       ('EO', torch.sin(th)+0.3*torch.sin(5*th), torch.cos(th)+1.5*torch.cos(5*th)),
                       ('OE', torch.cos(th)+0.3*torch.cos(3*th), -torch.sin(th)-0.9*torch.sin(3*th))]:
        err = (ang.dtheta(f, cls) - df).abs().max().item()
        c = ang.to_coef(f, cls); back = ang.to_val(c, cls)
        print(f"M={M:3d} {cls} dtheta err {err:.2e}  roundtrip {(back-f).abs().max().item():.2e}  cond(S) {torch.linalg.cond(ang.S[cls]).item():.2f}")

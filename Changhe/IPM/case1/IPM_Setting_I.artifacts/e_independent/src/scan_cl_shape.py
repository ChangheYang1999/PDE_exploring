"""For a fixed shape b_shape, set the amplitude so that c = 3c_l - 1 for each c_l, and record x*, mu1, h(P), 2c_l-1."""
import sys, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1, charac, diag
dev = 'cuda'; base = ''
def scan(name, make_b, cls):
    print(f"=== shape {name} ===")
    for cl in cls:
        m = ipm1.IPM1(N=48, M=10, L=1.0, gamma=1/cl, device=dev)
        b = make_b(m)
        c = m.psi_xy0(m.fields(b)).item(); b = b*((3*cl-1)/c)
        fe = charac.FieldEval(m, b, cl); P = fe.find_P()
        if P is None:
            print(f"  c_l={cl:5.2f}: no P"); continue
        print(f"  c_l={cl:5.2f}: x*={P['x_star']:.5f} mu1={P['mu1']:.5f} (2c_l-1={2*cl-1:.3f}) h(P)={P['h']:.5f}  h-1={P['h']-1:+.4f}  mu1+h={P['mu1']+P['h']:.4f} (2c_l={2*cl:.3f})  far-field b(inf)max={(m.rad.ext1_R@b).abs().max().item():.3g}")
cls = [1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0]
def shape_s2(m):
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; return 1 + 10*r**2/(m.L**2 + r**2) + 0*cos
def shape_one(m):
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; return torch.ones_like(r*cos)
def shape_fixcl3(m):
    m0, b0, cl0, d0 = diag.load(base + 'runs/fixcl_3.0.npz', device=dev)
    # reinterpret the Radau values on the new grid (same t nodes): b as function of t
    return b0.clone()
def shape_narrow(m):
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]; return 1 + 10*r**2/(m.L**2 + r**2)*(1 + torch.cos(2*th))/2
def shape_wide(m):
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]; return 1 + 10*r**2/(m.L**2 + r**2)*(1 - torch.cos(2*th))/2
scan('1+10 s2', shape_s2, cls); scan('b=1', shape_one, cls); scan('fixcl_3.0 values', shape_fixcl3, cls)
scan('1+10 s2 (1+cos2th)/2 (near x-axis)', shape_narrow, cls); scan('1+10 s2 (1-cos2th)/2 (near y-axis)', shape_wide, cls)

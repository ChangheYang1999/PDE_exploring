"""Project a converged state to another grid / domain (ipm_newton.project_state), keep C, save for jac_dense.
Usage: python3 src/project_seed.py runs/state.npz N M beta L Npsi out.npz"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt
spath = sys.argv[1]; N, M, beta, L, Npsi = int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]); out = sys.argv[7]
m0, x0, d0 = ipn.load_state(spath); C = float(d0['C'])
mf = ipn.Model(N, M, L, device='cuda', beta=beta, Npsi=Npsi)
xf = ipn.project_state(m0, x0, mf); bf, clf = mf.unpack(xf)
ch = cm.Charac(mf); z = ch.pack(bf, clf, C)
F = ch.F(z, **jt.RES_KW)
print(f'projected {spath} -> ({N},{M},{beta}) L={L} Npsi={Npsi}: |F|_2 {F.norm().item():.4e} |F|_inf {F.abs().max().item():.3e} h(P)-1 {F[-2].item():+.3e} ident {F[-1].item():+.3e} c_l {float(clf):.10f} C {C:.8f}')
ipn.save_state(out, mf, xf, extra=dict(tag=os.path.basename(out).replace('.npz', ''), C=C, formulation='psi_hybrid_projected', source=spath, F2_seed=F.norm().item()))
print('saved', out)

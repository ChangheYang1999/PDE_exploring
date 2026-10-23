"""make_const_start.py -- synthetic Q start state with b = a0 constant (rho = a0 y w(r), far-field gauge gK = a0) for q_free.py runs.
usage: python3 src/make_const_start.py N M cl a0 Lf out.pt"""
import sys, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3ql
torch.set_default_dtype(torch.float64)
N, M, cl, a0, Lf, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
q = ipm3ql.IPM3QL(N=N, M=M, L=1.0, gamma=1 / cl, device='cpu', Lf=Lf)
beta = torch.zeros(N + 1, M); beta[:, 0] = a0; u = q.beta_to_u(beta)
torch.save(dict(beta=beta, u=u, cl=cl, mu=None, gamma=1 / cl, N=N, M=M, L=1.0, Lf=Lf, gK=a0, p=q.p, rep='QL-start-const'), out); print('saved', out, 'a0 =', a0, 'gK =', a0)

# Lead exploration (2026-10-17): converged response of A_new to datum perturbations (diagnoses the FD Jacobian of
# fpnewton). Usage: python3 fpdiag.py restart.npz p N nsteps out.npz a_base ; a_pert1 ; a_pert2 ...  (comma lists)
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3]); nsteps = int(sys.argv[4]); out = sys.argv[5]
avecs = [np.array([float(v) for v in s.split(',')]) for s in ' '.join(sys.argv[6:]).split(';')]
lr, th = st['lr'], st['th']
res = []
g = st['g']
for a in avecs:
    t0 = time.time()
    Af = FE.datum_fn(a, N)
    g1, info = FE.evolve(p, Af, g, lr, th, nsteps)
    g2, info2 = FE.evolve(p, Af, g1, lr, th, 200)
    ng = FE.node_and_G(p, Af, g2, lr, th)
    ng1 = FE.node_and_G(p, Af, g1, lr, th)
    res.append(dict(a=a, logA=np.log(np.maximum(ng['A'], 1e-300)), logAn=ng['logAn'], m1=ng['m1'], m1_prev=ng1['m1'],
                    logAn_prev=ng1['logAn'], dgds=info2['dgds']))
    print(json.dumps(dict(a=a.tolist(), m1=ng['m1'], m1_at_nsteps=ng1['m1'], dgds=info2['dgds'],
                          dlogAn_last200=float(np.max(np.abs(ng['logAn'] - ng1['logAn'])[np.abs(np.cos(ng['thA'])) > 0.1])),
                          wall=round(time.time() - t0))), flush=True)
    if len(res) == 1:
        g = g2
np.savez(out, thA=res[0] and FE.node_and_G.__name__, m1=[r['m1'] for r in res],
         logA=np.array([r['logA'] for r in res]), logAn=np.array([r['logAn'] for r in res]), a=np.array([r['a'] for r in res]))

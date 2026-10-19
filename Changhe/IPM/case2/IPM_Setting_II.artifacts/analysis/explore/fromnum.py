# Lead: convert a numerics bnewton iterate (g, lr, th, x = 64 x-even expf modes + p, hist with m1) to the lead npz format.
# Usage: python3 fromnum.py in.npz out.npz
import sys, json, numpy as np
d = np.load(sys.argv[1]); h = json.loads(str(d['hist']))[-1]; a = json.loads(str(d['args']))
x = np.array(a['par'], float); p = float(a['p'])
np.savez(sys.argv[2], g=d['g'], lr=d['lr'], th=d['th'], x=x, p=p, m1=float(h['m1']), thA=d['thA'], logGt=d['logGt'])
print(json.dumps(dict(K=len(x), p=p, m1=h['m1'], Nr=len(d['lr']), Nth=len(d['th']), lr=[float(d['lr'][0]), float(d['lr'][-1])])))

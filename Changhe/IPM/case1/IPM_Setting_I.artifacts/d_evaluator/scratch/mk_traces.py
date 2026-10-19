"""Save the verifier's own x-axis traces (vb3w inverse): x, w, w', w'' (FD and mode-ODE routes), c_l, for x < 60."""
import sys, os, warnings, json
warnings.simplefilter("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))  # the code directory next to this scratch directory
import numpy as np
import vb3w
from vcand import load_modes
path, Mmax, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3]
d, g, ms, F = load_modes(path, Mmax)
c, cl, k, p, dp, ns = vb3w.inverse(g, F, Mmax)
tr = vb3w.w_traces(g, F, ms, p, dp, ns, cl)
x = g.r
sel = x < 60
np.savez(outp, x=x[sel], w=tr['w'][sel], wp=tr['wp'][sel], wpp_fd=tr['wpp_fd'][sel], wpp_ode=tr['wpp_ode'][sel], c_l=cl, c=c,
         source=path, Mmax=Mmax)
print(json.dumps(dict(src=path, Mmax=Mmax, c_l=cl, c=c, n=int(sel.sum()))), flush=True)

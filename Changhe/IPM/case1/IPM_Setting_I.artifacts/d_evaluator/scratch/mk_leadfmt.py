"""Write the verifier's own axis traces (vb3w inverse) in the lead's export key format, so that the lead's
b3_wonly_export.py can be run, read-only, on verifier data."""
import sys, warnings
warnings.simplefilter("ignore")
sys.path.insert(0, 'code')
import numpy as np
import vb3w
from vcand import load_modes
from vb3 import axis_traces
path, Mmax, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3]
d, g, ms, F = load_modes(path, Mmax)
c, cl, k, p, dp, ns = vb3w.inverse(g, F, Mmax)
tr = vb3w.w_traces(g, F, ms, p, dp, ns, cl)
x = g.r
axd = axis_traces(F.T, ms, p, dp, ns, x, cl, lambda a: g.du(a))
sel = x < 60
np.savez(outp, c_l=cl, axis_x=x[sel], axis_w=tr['w'][sel], axis_w_prime=tr['wp'][sel], axis_h=axd['h'][sel],
         axis_G1=axd['G1'][sel], axis_G1_prime=axd['G1p'][sel], axis_A2=axd['W1_2'][sel], axis_B3W=axd['W2_3'][sel],
         axis_A2_finite_difference=axd['W1_2'][sel], axis_B3W_finite_difference=axd['W2_3'][sel], axis_G3=axd['G3'][sel])
print('c_l', cl, 'n', sel.sum())

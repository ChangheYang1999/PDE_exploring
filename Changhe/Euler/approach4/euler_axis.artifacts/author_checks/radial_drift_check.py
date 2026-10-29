# Lead sample check of the radial drift D = c_l + [2 mu P - (1 - mu^2) P_mu]/R (topic 83 identity) on the saved (x, mu) grids
# of the referee's Gaussian and nested fields. A sample can only refute a certified lower bound, never prove it.
import json, sys, numpy as np
from scipy.interpolate import make_interp_spline
base='referee/'
out={}
for name in sys.argv[1:]:
    g=np.load(base+name+'/grid.npz'); s=json.load(open(base+name+'/summary.json'))
    cl=None
    for k in ('c_l','cl','c'):
        if k in s: cl=float(s[k]); break
    if cl is None:
        for v in s.values():
            if isinstance(v,dict) and 'c_l' in v: cl=float(v['c_l']); break
    x=g['x']; mu=g['mu']; P=g['phi']; R=np.exp(x)
    Pmu=np.empty_like(P)
    for i in range(len(x)):
        Pmu[i]=make_interp_spline(mu,P[i],k=5)(mu,1)
    D=cl+(2*mu[None,:]*P-(1-mu[None,:]**2)*Pmu)/R[:,None]
    i,j=np.unravel_index(np.argmin(D),D.shape)
    # analytic small-R limit c_l - 1/2 + (3/2) mu^2 (phi = z/2 near the source) at the smallest radius as a consistency check of the formula
    lim=np.max(np.abs(D[0]-(cl-0.5+1.5*mu**2)))
    out[name]=dict(c_l=cl,min_D=float(D[i,j]),R_at_min=float(R[i]),mu_at_min=float(mu[j]),D_far_max_dev=float(np.max(np.abs(D[-1]-cl))),
                   smallR_limit_dev=float(lim),R_min=float(R[0]),R_max=float(R[-1]),n=[len(x),len(mu)])
json.dump(out,open('author_checks/radial_drift_check_output.json','w'),indent=1)
print(json.dumps(out,indent=1))

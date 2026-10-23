import json,sys
from pathlib import Path
import numpy as np
from numpy.polynomial import chebyshev as cb
from candidate_reader import Candidate
out=[]
for p in sys.argv[1:]:
 c=Candidate(p);n,m=c.meta['N'],c.meta['M'];r=c.meta['L']*(1+c.nodes)/(1-c.nodes)**c.meta['p'];t=c.compact_coordinate(r)
 theta=(np.arange(m)+.5)*np.pi/(2*m)
 exact_t_modes=cb.chebval(c.nodes,c.coefficients).T
 angular=np.cos(2*np.arange(m)[:,None]*theta)
 direct=exact_t_modes@angular
 recovered=cb.chebval(t,c.coefficients).T@angular
 row={'source':p,'max_coordinate_error':float(np.max(np.abs(t-c.nodes))),'argmax_coordinate':int(np.argmax(abs(t-c.nodes))),'max_direct_algebraic_reconstruction':float(np.max(abs(direct-c.values))),'max_recovered_coordinate_reconstruction':float(np.max(abs(recovered-c.values))),'t_errors':(t-c.nodes).tolist()}
 out.append(row);print(json.dumps(row),flush=True)

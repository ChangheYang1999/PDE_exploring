"""Packet122 numerical controls with distinct state variables and integrators."""
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
import json,hashlib
import numpy as np
from global_axis_base import BaseAxis

root=Path('research/122_global_axis_first_order_realization/verification')
t0=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','cases':[]}
radii=np.array([1e-6,1e-4,.01,.1,1,10,100,1e3,1e4,1e5,1e8,1e12,1e24,1e48,1e96])
for beta in [4.,3.]:
    field=BaseAxis(beta)
    for side in [1,-1]:
        a=field.solve(side,radii,'direct',rtol=3e-11,eps=1e-8)
        b=field.solve(side,radii,'integrating_factor',rtol=3e-11,eps=1e-8)
        c=field.solve(side,radii,'direct',rtol=3e-12,eps=1e-7)
        err=max(float(np.max(np.abs(a[k]-b[k]))) for k in ['log_a','log_Q'])
        err2=max(float(np.max(np.abs(c[k]-a[k]))) for k in ['log_a','log_Q'])
        assert err<2e-7,(beta,side,err)
        assert err2<2e-7,(beta,side,err2)
        assert min(a['Q_over_qe'])>0
        row={'beta':beta,'side':side,'max_log_difference_between_formulations':err,'max_log_difference_refinement_and_cutoff':err2,
             'evaluations':[a['nfev'],b['nfev'],c['nfev']],
             'rows':[{'radius':float(r),'log_a':float(a['log_a'][i]),'log_Q':float(a['log_Q'][i]),'Q_over_qe':float(a['Q_over_qe'][i]),'v_over_r':float(a['v_over_r'][i])} for i,r in enumerate(radii)]}
        out['cases'].append(row)
        (root/'axis_ode_tests.json').write_text(json.dumps(out,indent=2)+'\n')
        print('beta',beta,'side',side,'methods',err,'refinement',err2,'ratio_at_1e5',a['Q_over_qe'][9],'ratio_at_1e96',a['Q_over_qe'][-1],flush=True)
out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-t0,
           scope='Floating-point ODE controls; positive limits and all-radii positivity are proved in PROOF.md, not certified by samples.')
out['code_hashes']={name:hashlib.sha256(Path('code_independent',name).read_bytes()).hexdigest() for name in ['global_axis_base.py','test_global_axis_ode.py']}
(root/'axis_ode_tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)

from pathlib import Path
import sys,json,time
import numpy as np
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'));sys.path.insert(0,str(ROOT.parent/'ritz-resolution/code'))
from collocation import NodalDensity
from linearized import direction_coefficients,MultiLinearGPU
from blocked_kernel import BlockedMultiSplit
from multi_kernel import MultiSplit
source=json.loads((ROOT/'verification/actions.json').read_text());row=source['states'][0];d=NodalDensity(ROOT/'data/dnB_n96m40S.npz');V=np.load(ROOT/'data/directions_n96m40S.npz')['V'];co=direction_coefficients(d,V)
f=MultiLinearGPU(d,co,V[-2]);ker=BlockedMultiSplit(f,2048,24,.1,rmax=1e30);out=[]
for i in [11,54]:
 r=row['rows'][i];t=time.monotonic();u=ker.velocity(r['point']);old=np.array(r['delta_U']);err=float(np.max(abs(u-old)));assert err<1e-9
 out.append({'point_index':i,'point':r['point'],'max_abs_change':err,'max_old':float(np.max(abs(old))),'seconds':time.monotonic()-t});print(out[-1],flush=True)
# A direct same-object call checks a moderate point without relying only on the checkpoint.
u=MultiSplit.velocity(ker,row['rows'][11]['point']);err=float(np.max(abs(u-np.array(row['rows'][11]['delta_U']))));assert err<1e-9
out.append({'same_object_unblocked_checkpoint_change':err})
(ROOT/'verification/blocked_check.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',flush=True)

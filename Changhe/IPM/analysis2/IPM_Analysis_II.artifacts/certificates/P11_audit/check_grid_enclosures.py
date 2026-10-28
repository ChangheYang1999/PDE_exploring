"""Audit the saved binary64 midpoint/radius pairs against independent Arb points."""
from pathlib import Path
from datetime import datetime,timezone
import sys,math,json
import numpy as np
from flint import arb,ctx
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'source_audit'))
from field_eval import State
ctx.prec=384
src=Path('numerics/data/grid088_coarse.npz')
z=np.load(src);keys=list(z['keys']);state=State(88,384)
records=[]
for idx in [0,1,1000,4600,9000]:
    ss=float(z['s'][idx]);th=float(z['theta'][idx])
    rr=arb(ss).exp();xx=rr*arb(th).cos();yy=rr*arb(th).sin()
    if th==0:yy=arb(0)
    if abs(th-math.pi/2)<1e-15:xx=arb(0)
    exact=state.evaluate(xx,yy)
    for name in ['rho','rho_y','rho_x']:
        k=keys.index(name);mid=float(z['mid'][idx,k]);rad=float(z['rad'][idx,k])
        saved=arb(mid,rad)
        disjoint=not saved.overlaps(exact[name])
        records.append({'index':idx,'s_hex':ss.hex(),'theta_hex':th.hex(),'field':name,'saved_mid_hex':mid.hex(),'saved_rad_hex':rad.hex(),'saved_mid_display':mid,'saved_radius_display':rad,'independent_ball':exact[name].str(85),'disjoint':disjoint,'midpoint_discrepancy':abs(arb(mid)-exact[name]).str(50)})
        if disjoint:print(idx,name,'saved radius',rad,'discrepancy',abs(arb(mid)-exact[name]).str(12))
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source':str(src),'scope':'This audits the serialized midpoint/radius pair, not correctness of the pre-serialization Arb calculation. Grid locations are reconstructed from the saved s and theta using the original documented mapping.','records':records,'disjoint_count':sum(r['disjoint'] for r in records)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
assert out['disjoint_count']>0

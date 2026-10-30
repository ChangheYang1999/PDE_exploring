"""Necessary-radius point witnesses. Derived numbers remain PENDING-N4.

Inputs are copies of N4 exact canonical conversions. The code performs only
point enclosures and does not claim a continuum or whole-plane certificate.
"""
from pathlib import Path
from datetime import datetime, timezone
import sys, json, time
from flint import arb, ctx
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root.parent/'signed_coupling/code'))
from n4_radial_copy import Radial, ar, q
ctx.prec=768
start=time.monotonic()
s=arb(1)/2**18;r=arb(1)/2**16
C0=1/(2*(arb.pi()*(1+s)).sqrt())
C1=1/(8*arb.pi()*s*(1+s)).sqrt()
B=C0*C1
pts=[(0,1),(1,1),(0,2),(2,2),(1,3),(3,1),(0,5),(5,5),(1,5),(5,1),(0,10),(10,10)]
results=[]
for name in ['d2','Mpen2','b6']:
    model=Radial(root/'data'/f'{name}_canonical.json');c=ar(model.c)
    for x,y in pts:
        f=model.evaluate(x,y)
        V=((c*x+f['u1'])**2+(c*y+f['u2'])**2).sqrt()
        grad=(f['rho_x']**2+f['rho_y']**2).sqrt()
        A=C1*V+C0*(1+grad)
        F=abs(f['residual']);limit=A*r+B*r*r
        gap=F-limit
        required=2*F/(A+(A*A+4*B*F).sqrt())
        item={'candidate':f'C1-A2-{name}','point':[x,y],'F_abs':F.str(60),'V_norm':V.str(60),'gradient_norm':grad.str(60),'bound_at_radius':limit.str(60),'gap':gap.str(60),'radius_necessary_lower_enclosure':required.str(60),'strictly_excludes_r_2m16':bool(gap>0)}
        results.append(item)
        if gap>0:print(name,x,y,'F',F.str(12),'bound',limit.str(12),'required radius',required.str(12),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'s':'1/262144','tested_radius':'1/65536','status':'PENDING-N4','scope':'point witnesses conditional on copied exact candidate conversions; not new sufficient closure claims','results':results,'elapsed_seconds':time.monotonic()-start}
(root/'verification/point_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
print('elapsed',out['elapsed_seconds'],flush=True)

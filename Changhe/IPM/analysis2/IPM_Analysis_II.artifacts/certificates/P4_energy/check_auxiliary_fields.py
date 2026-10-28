"""Independent order-six Cartesian Taylor check of compactified derivatives."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json
from flint import arb,ctx
from compact_matrix import A,BASE
sys.path.insert(0,str(BASE/'source_audit'))
import field_eval as fe
fe.ORDER=6
fe.INDICES=[(i,j) for i in range(7) for j in range(7-i)]
ctx.prec=384
rows=[]
for state in (88,131):
    S=fe.State(state,384)
    data=json.loads(Path(__file__).with_name(f'state{state:03d}_auxiliary_polynomials.json').read_text())
    delta=Q(data['delta'])
    for xs,ys in [('0','0.1'),('0.5','0.5'),('1','2'),('3','1')]:
        qx,qy=Q(xs),Q(ys);qq=qx*qx+qy*qy
        x=A(qx);y=A(qy);q=A(qq);t=A(qq/(1+qq));z=A((qx*qx-qy*qy)/qq);w=(1-t)**(A(delta)/2)
        jets=S.evaluate(x,y,include_potential_jet=True)['potential_derivatives'];record={'state':state,'x':xs,'y':ys,'overlaps':{}}
        for ij in [(1,3),(2,4),(0,6),(3,3),(1,5),(4,2),(5,1)]:
            label='chi'+str(ij[0])+str(ij[1]);v=arb(0)
            for j in range(4):
                poly=sum((A(co)*t**i*z**k for i,k,co in data['polynomials'][f'{label}_{j}']),arb(0))
                v+=w**(j+1)*poly
            if ij[1]%2:v*=2*x*y/q
            good=v.is_finite() and jets[ij].is_finite() and v.overlaps(jets[ij]);record['overlaps'][label]=good
            assert good,(state,xs,ys,label,v,jets[ij])
        rows.append(record);print(state,xs,ys,'all order-six checks overlap',flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'scope':'Independent point checks of exact identities, not a covering certificate.','checks':rows}
Path(__file__).with_name('auxiliary_field_crosschecks.json').write_text(json.dumps(out,indent=2)+'\n')

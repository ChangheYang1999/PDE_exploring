from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from math import isqrt
import json,sys
import numpy as np
root=Path(__file__).resolve().parents[1];v=root/'verification';sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity
angular=json.loads((v/'summary.json').read_text());physical=json.loads((v/'asymptotic.json').read_text());fine=json.loads((v/'asymptotic4096.json').read_text());lookup={(a['tag'],a['radius'],a['theta']):a for a in physical['rows']};meta={a['tag']:a for a in angular['rows']}
assert len(physical['rows'])==36 and len(fine['rows'])==6
rows=[]
for a in fine['rows']:
    row=a.copy();old=lookup[a['tag'],a['radius'],a['theta']];row['2048_to_4096_scaled_change']=abs(a['scaled_R']-old['scaled_R'])
    info=meta[a['tag']];idx=info['targets'].index(a['theta']);D=info['samples']['D'][idx];den=info['samples']['den'][idx];r=a['radius'];row['leading_predicted_report_Nf']=r**(info['k']-1)*abs(D)/den
    d=NodalDensity(info['source']);B=max(abs(Fraction(float(x))) for x in d.b.ravel());B0=(B.numerator+B.denominator-1)//B.denominator;H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1);C=512*H*B0
    assert d.L==8 and 0<1/Fraction(d.cl)<Fraction(1,5)
    ratio=Fraction(int(r),10**30);tail=Fraction(5*C,2)*int(r)*Fraction(1,10**24)/(1-ratio*ratio)**2
    row['exact_tail_C']=C;row['omitted_velocity_bound_beyond_1e30']=float(tail);row['omitted_scaled_R_bound_beyond_1e30']=float(tail)*np.linalg.norm(a['gradient'])*r**(1-2*info['k']);rows.append(row)
out={'date':datetime.now(timezone.utc).isoformat(),'method':'conditional differentiable asymptotics, separately implemented physical-angle homogeneous inverse and full-plane quadrature; floating interior checks plus exact outer tail','angular':angular,'physical_rows':physical['rows'],'refined_rows':rows,'max_gradient_relative_FD_error':max(a['gradient_relative_difference_FD'] for a in physical['rows'])}
(v/'combined.json').write_text(json.dumps(out,indent=2)+'\n')
for a in rows:print(a['tag'],a['theta'],a['scaled_R'],a['target_D'],a['R_report_Nf'],a['leading_predicted_report_Nf'],a['2048_to_4096_scaled_change'],a['omitted_scaled_R_bound_beyond_1e30'])

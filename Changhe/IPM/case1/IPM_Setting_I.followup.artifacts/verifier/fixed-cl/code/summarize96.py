from pathlib import Path
from fractions import Fraction
from math import isqrt
from datetime import datetime, timezone
import json, sys, hashlib
import numpy as np
root=Path(__file__).resolve().parents[1];v=root/'verification96'
sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity
rows=[]
tags=sys.argv[1:] or ['fixclSA_n96m40_d0.001', 'fixclSA_n96m40_d-0.001', 'fixclS_n96m40_d-0.001', 'fixclSA_n96m40_d-0.01']
for tag in tags:
 def read(s):return json.loads((v/(tag+'_'+s+'.json')).read_text())
 source=root/'data96'/(tag+'.npz');d=NodalDensity(source);z=np.load(source);balls=read('balls');strain=read('strain');mid=read('2048');hi=read('4096');ell=read('elliptic4096')
 B=max(abs(Fraction(float(a))) for a in z['b'].ravel());B0=(B.numerator+B.denominator-1)//B.denominator;H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1)
 assert d.L==8 and 0<1/Fraction(d.cl)<Fraction(1,5) and np.array_equal(z['b'][0],np.ones(d.M))
 C=512*H*B0;t=Fraction(1,10**25);tail=Fraction(5*C,2)*10**5*Fraction(1,10**24)/(1-t*t)**2
 r=np.array([.05,.3,1.,3.,10.,100.,1000.,1e5])[:,None];th=np.array([.001,.03,.3,1.,1.4]);x=r*np.cos(th);y=r*np.sin(th);val=d(x,y);per=max(np.max(abs(d(-x,y)-val)),np.max(abs(d(x,-y)+val)))
 row={'tag':tag,'source_md5':hashlib.md5(source.read_bytes()).hexdigest(),'cl':d.cl,'C_aux':d.C,'N':d.N,'M':d.M,'normalization_first_row_one':True,'sampled_parity_error':float(per),'tail_B_exact':str(B),'tail_H':H,'tail_C':C,'tail_gamma':'1/5','tail_radius':'1e30','tail_max_observer':'1e5','velocity_tail_bound':float(tail),'strain_tail_bound':float(Fraction(5*C,2*10**24)),'strain':strain,'center_values':balls['values'],'center_contains_zero':balls['contains_zero'],'transport4096':[{'point':a['point'],'R':a['R'],'R_report_Nf':a['R_Nv'],'R_report_Nv':a['R_Nf'],'refinement_change_report_Nf':abs(a['R_Nv']-b['R_Nv'])} for a,b in zip(hi['rows'],mid['rows'])],'transport_near2048':mid['rows'][2:],'elliptic4096':ell['rows']}
 assert len(ell['rows'])==2
 rows.append(row)
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'actual fields with independently evaluated physical residuals; exact exterior bound but no interval enclosure of interior quadrature','rows':rows}
(v/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r['tag'],r['source_md5'],[a['R_report_Nf'] for a in r['transport4096']],[a['checks'][0]['E_over_rho_x'] for a in r['elliptic4096']],r['strain']['identity_defect_3cl_1_c'],r['tail_C'])

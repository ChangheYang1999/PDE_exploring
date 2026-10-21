from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import sys,json,hashlib
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse/code'))
from collocation import NodalDensity
root=Path(__file__).resolve().parents[1];v=root/'verification'
tags=['fixclS_n120m48_d0.001','fixclS_n120m48_d-0.001','fixclSA_n120m48_d0.01','fixclSA_n120m48_d-0.01'];rows=[]
for tag in tags:
 def read(s):return json.loads((v/(tag+'_'+s+'.json')).read_text())
 balls=read('balls');strain=read('strain');lo=read('1024');mid=read('2048');hi=read('4096');ell=read('elliptic')
 ef=read('elliptic4096') if (v/(tag+'_elliptic4096.json')).exists() else None
 source=Path('numerics/runs')/(tag+'.npz');d=NodalDensity(source);f=np.load(source)
 assert np.array_equal(f['b'][0],np.ones(d.M))
 maxb=max(abs(Fraction(float(x))) for x in f['b'].ravel())
 assert d.N==120 and d.M==48 and Fraction(d.L)==8 and 0<1/Fraction(d.cl)<Fraction(1,5)
 bceil=(maxb.numerator+maxb.denominator-1)//maxb.denominator
 C=512*151*bceil
 # Exact rational bound from AV13, R=10^30, |X|<=10^5, gamma=1/5.
 t=Fraction(1,10**25);tail=Fraction(5*C,2)*10**5*Fraction(1,10**24)/(1-t*t)**2
 strain_tail=Fraction(5*C,2*10**24)
 r=np.array([.05,.3,1.,3.,10.,100.,1000.,1e5]);th=np.array([.001,.03,.3,1.,1.4]);xx=r[:,None]*np.cos(th);yy=r[:,None]*np.sin(th);val=d(xx,yy)
 per=max(np.max(abs(d(-xx,yy)-val)),np.max(abs(d(xx,-yy)+val)),np.max(abs(d(-xx,-yy)+val)))
 contrast=float(d(5.403023058681398,8.414709848078965)/(5.403023058681398**2*8.414709848078965))
 row={'tag':tag,'source_md5':d.md5,'cl':d.cl,'C_aux':d.C,'bmax_exact_fraction':str(maxb),'bmax_ceil':bceil,
 'tail_density_bound_C':C,'tail_gamma':'1/5','tail_R':'10^30','tail_max_observer':'10^5','velocity_tail_bound':float(tail),'central_strain_tail_bound':float(strain_tail),
 'normalization_first_row_exactly_one':True,'sampled_parity_absolute_error':float(per),
 'P1_rho_over_x2y':contrast,'strain':strain,'ball_values':balls['values'],'ball_contains_zero':balls['contains_zero'],
 'transport_high_points':[{'point':a['point'],'R':a['R'],'R_report_Nf':a['R_Nv'],'R_report_Nv':a['R_Nf'],
 'R_report_Nf_1024':lo['rows'][i]['R_Nv'],'R_report_Nf_2048':mid['rows'][i]['R_Nv'],
 'R_report_Nf_change2048to4096':abs(a['R_Nv']-mid['rows'][i]['R_Nv'])} for i,a in enumerate(hi['rows'])],
 'transport_other_points2048':mid['rows'][2:],
 'elliptic2048':[{'point':a['point'],'E_over_rhox_sweep':[b['E_over_rho_x'] for b in a['checks']]} for a in ell['rows']],
 'elliptic4096':[] if ef is None else [{'point':a['point'],'E_over_rhox':a['checks'][0]['E_over_rho_x'],'E_report_normalized':a['checks'][0]['E_normalized'],'divU':a['checks'][0]['divU']} for a in ef['rows']]}
 rows.append(row)
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'independent full-plane quadrature and Cartesian differences; tail bounds exact for ideal interpolants; interior quadrature not certified','all_fine_elliptic_complete':all(len(r['elliptic4096'])==2 for r in rows),'rows':rows}
(v/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r['tag'],r['source_md5'],[x['R_report_Nf'] for x in r['transport_high_points']],r['sampled_parity_absolute_error'],r['tail_density_bound_C'],[x['E_over_rhox'] for x in r['elliptic4096']])

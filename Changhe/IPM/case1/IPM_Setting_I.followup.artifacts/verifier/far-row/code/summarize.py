from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import sys,json,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse/code'))
from collocation import NodalDensity
root=Path(__file__).resolve().parents[1];v=root/'verification'
def read(s):return json.loads((v/(s+'.json')).read_text())
source=Path('numerics/runs/dnR8_n120m48.npz');d=NodalDensity(source);f=np.load(source)
assert np.array_equal(f['b'][0],np.ones(d.M))
assert d.N==120 and d.M==48 and Fraction(d.L)==8 and 0<1/Fraction(d.cl)<Fraction(1,5)
maxb=max(abs(Fraction(float(x))) for x in f['b'].ravel());bceil=(maxb.numerator+maxb.denominator-1)//maxb.denominator;C=512*151*bceil
t=Fraction(1,10**25);tail=Fraction(5*C,2)*10**5*Fraction(1,10**24)/(1-t*t)**2
r=np.array([.05,.3,1,3,10,100,1000,1e5]);th=np.array([.001,.03,.3,1,1.4]);x=r[:,None]*np.cos(th);y=r[:,None]*np.sin(th);val=d(x,y)
per=max(np.max(abs(d(-x,y)-val)),np.max(abs(d(x,-y)+val)),np.max(abs(d(-x,-y)+val)))
lo=read('physical2048');hi=read('physical4096');ell=read('elliptic4096');balls=read('balls')
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'Own full-plane inverse and FD8; exact exterior bound for ideal interpolant; interior quadrature not interval-certified.',
 'md5':d.md5,'c_l':d.cl,'C_aux':d.C,'normalization_exact':True,'parity_sample_max_error':float(per),'U_at_origin':'exactly zero by parity and canonical law',
 'bmax_exact':str(maxb),'tail_C':C,'tail_gamma':'1/5','tail_R':'10^30','tail_max_observer':'10^5','tail_bound_R1e30_rmax1e5':float(tail),'central_strain_tail_bound':float(Fraction(5*C,2*10**24)),
 'strain':read('strain'),'center_values':balls['values'],'center_contains_zero':balls['contains_zero'],
 'physical_high':[{'point':a['point'],'R':a['R'],'R_report_Nf':a['R_Nv'],'R_report_Nv':a['R_Nf'],'change2048to4096':abs(a['R_Nv']-lo['rows'][i]['R_Nv'])} for i,a in enumerate(hi['rows'])],
 'other_physical_points2048':lo['rows'][2:],
 'elliptic4096':[{'point':a['point'],'E_over_rho_x':a['checks'][0]['E_over_rho_x'],'E_normalized':a['checks'][0]['E_normalized'],'divU':a['checks'][0]['divU']} for a in ell['rows']],
 'matrix_audit':'audit.json, supplied finite-difference action arrays, not own orbit differentiation'}
(v/'summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['date','md5','parity_sample_max_error','physical_high','elliptic4096']},indent=2))

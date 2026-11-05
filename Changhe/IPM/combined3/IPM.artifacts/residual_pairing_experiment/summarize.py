"""Consolidate actual, preserved experiment outputs without recomputation."""
import json,math
from pathlib import Path
HERE=Path(__file__).resolve().parent
def read(name):return json.loads((HERE/name).read_text())
ref=read('hankel_full_n131072_bm1_r22.json');Q=ref['Q'];R=4.549261e-7;M=.387
splits=ref['gaussian_splits'];recommended=next(q for q in splits if q['lambda']==1e-7)
comparison={'R':R,'M':M,'Q_numerical':Q,'Q_times_M':Q*M,'global_D':'INFINITE','global_D_times_R':'INFINITE','finite_D_competitive_threshold':Q*M/R,
 'recommended_stable_gaussian':recommended,'recommended_ratio_to_QM':recommended['bound']/(Q*M),'smallest_tested_stable_gaussian':ref['best_gaussian_split'],
 'estimated_numerical_Q_uncertainty_not_bound':1e-7,'estimated_numerical_Dhi_uncertainty_not_bound':.01}
nodes=[]
for N,name in [(16384,'hankel_full_n16384_bm1_r22.json'),(32768,'hankel_full_n32768_bm1_r22.json'),(65536,'hankel_full_n65536_smooth_bm1_r22.json'),(131072,'hankel_full_n131072_bm1_r22.json')]:
    d=read(name);s=next(s for s in d['gaussian_splits']if s['lambda']==1e-7);nodes.append({'nodes':N,'Q':d['Q'],**s})
extent=[]
for C in [3,6,12,24,48,96,192,384,1000,10000,1e6]:
    d=read(f'hankel_cut{C:g}_extent.json');extent.append({'cutoff':C,'Q':d['Q'],'D_compact_cutoff_screen':d['D_with_kmin']})
diagnostics=[]
for name in ['hankel_full_k5.json','hankel_full_k9.json','hankel_full_farstride2.json','hankel_full_kmax500.json','hankel_full_kmax2000.json']:
    d=read(name);s=next(q for q in d['gaussian_splits']if q['lambda']==1e-7);diagnostics.append({'file':name,'Q':d['Q'],**s})
result={'comparison':comparison,'FFTLog_node_convergence':nodes,'source_extent':extent,'FFTLog_diagnostics':diagnostics,'raw_D_field_warning':'D_with_kmin in unlocalized FFTLog data is an infrared-conditioned diagnostic of a divergent target, not a finite norm. Only high-pass D values are used.'}
(HERE/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

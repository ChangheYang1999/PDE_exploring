"""Selected candidate widths only, no whole-region assertion."""
import os,sys,json,time,resource
from pathlib import Path
from fractions import Fraction as F
B=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
import cell_arb as c
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
cases=[('0','1/100'),('1/10','1/5'),('1/5','3/10'),('1/2','3/5'),('1','6/5'),('2','11/5'),('3','16/5'),('5','11/2'),('10','21/2'),('33/2','17')]
st=time.monotonic();data=c.setup(16);rows=[]
for a,b in cases:
 r=c.bound_cell(data,a,b,False);rows.append(r);print(json.dumps({'utc':c.utc(),'a':a,'b':b,'W':r['W']['display'],'Wm':r['W_over_m']['display'],'weighted':{k:v['display'] for k,v in r['weighted'].items()},'nonpoly':r['nonpolynomial_remainder']['display'],'seconds':r['seconds']}),flush=True)
d={'utc':c.utc(),'status':'PROTOTYPE_SELECTED_CELLS_NOT_COVERING','primary_source_sha256':c.sha(B/'research/outer_cells/code/cell_arb.py'),'proof_sha256':c.sha(B/'research/outer_cells/PROOF.md'),'rows':rows,'seconds':time.monotonic()-st};(B/'research/outer_cells/evidence/width_prototypes.json').write_text(json.dumps(d,indent=2)+'\n')

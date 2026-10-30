"""Exact rational postprocessing of the new T4 symmetry-based bound."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,hashlib
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE.parents[0]/'graded_box_audit/code'))
from check import I

def parse(text):
    z=text.strip('[]').split('+/-')
    if len(z)==1:return I(z[0].strip())
    mid,rad=(Q(v.strip()) for v in z);return I(mid-rad,mid+rad)
def absolute(x):
    if x.a>=0:return x
    if x.b<=0:return -x
    return I(0,max(-x.a,x.b))
source=BASE/'verification/cartesian_witnesses.json';prior=BASE/'data/T4_symmetry_witnesses.json'
a=json.loads(source.read_text());b=json.loads(prior.read_text());rows=[]
for row,old in zip(a['rows'],b['rows']):
    assert row['candidate']==old['candidate'] and row['point']==old['point'] and row['canonical_sha256']==old['canonical_sha256']
    f={k:parse(v) for k,v in row['fields'].items()}
    upper=Q(87,10000)*f['velocity_norm']+Q(53,1000000)*(1+f['gradient_norm'])+Q(1,2000000)
    gap=absolute(f['residual'])-upper;assert gap.a>0
    oldgap=parse(old['gap']);assert max(gap.a,oldgap.a)<=min(gap.b,oldgap.b)
    rows.append({'candidate':row['candidate'],'point':row['point'],'gap':gap.record(),'positive':True,'T4_overlap':True})
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,prior,BASE/'data/T4_symmetry_PROOF.md',Path(__file__)]},
        'method':'Exact rational interval postprocessing of independently confirmed Cartesian field values','rows':rows,
        'scope':'Numerical gaps confirmed; theory implication requires independent review of T4 symmetry lemma.'}
(BASE/'verification/symmetry_rational_gaps.json').write_text(json.dumps(result,indent=2)+'\n')
print([(r['candidate'],r['gap']['midpoint_float']) for r in rows],flush=True)

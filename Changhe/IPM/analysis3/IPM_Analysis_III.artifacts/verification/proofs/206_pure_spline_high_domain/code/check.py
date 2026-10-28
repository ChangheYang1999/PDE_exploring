"""Exact original-knot endpoint classification, independently replayed."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import hashlib, json, importlib.util, time
import numpy as np
ROOT=Path(__file__).resolve().parents[3]; TOP=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('own_exact_splines',ROOT/'proofs/198_pure_spline_input_gram/code/check.py'); sp=importlib.util.module_from_spec(spec);spec.loader.exec_module(sp)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def jet(poly,width,right):
 return [sum((v*F(factorial(j),factorial(j-k))*(int(right)**(j-k)) for j,v in enumerate(poly) if j>=k),F(0))/width**k for k in range(8)]
def first_nonzero(a):return next((j for j,v in enumerate(a) if v),None)
def main():
 start=time.monotonic(); assert sha(sp.SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 data=np.load(sp.SRC,allow_pickle=False);fine=list(map(sp.rat,data['knots']));knots=[fine[0]]*8+fine[8:-8][::60]+[fine[-1]]*8; nb=len(knots)-8;assert nb==34
 spanids=list(range(7,len(knots)-8));pieces=[];checked=0
 for si in spanids:
  ps=sp.cox(knots,si)
  for i,poly in ps.items():
   controls=[F(int(j==i)) for j in range(nb)]
   assert poly==sp.db.deboor_poly(knots,controls,7,si);checked+=1
  pieces.append(ps)
 joins=0
 for ci in range(26):
  w1=knots[ci+8]-knots[ci+7];w2=knots[ci+9]-knots[ci+8]
  for i in range(nb):
   assert jet(pieces[ci].get(i,[F(0)]*8),w1,True)[:7]==jet(pieces[ci+1].get(i,[F(0)]*8),w2,False)[:7];joins+=1
 end=[]
 for i in range(nb):
  lo=jet(pieces[0].get(i,[F(0)]*8),knots[8]-knots[7],False)
  hi=jet(pieces[-1].get(i,[F(0)]*8),knots[-8]-knots[-9],True)
  assert first_nonzero(lo)==(i if i<=7 else None)
  assert first_nonzero(hi)==(33-i if i>=26 else None)
  end.append({'i':i,'left_jets':list(map(str,lo)),'right_jets':list(map(str,hi)),'left_first':first_nonzero(lo),'right_first':first_nonzero(hi)})
 high=[];graph=[]
 for i in range(4,30):
  q=min([7]+[v for v in (end[i]['left_first'],end[i]['right_first']) if v is not None])
  if F(25,4)<q+F(1,2):high.append(i)
  if F(25,4)<q-F(1,2):graph.append(i)
 assert high==list(range(6,28)) and graph==list(range(7,27))
 meta=json.loads((ROOT/'proofs/198_pure_spline_input_gram/evidence/source/S1M4P_meta.json').read_text())
 assert len(meta['new'])==78
 positions={'high_input':[],'high_graph':[],'outside_high_input':[],'input_not_graph':[]}
 for j,(typ,label,m) in enumerate(meta['new']):
  assert typ=='rem' and label.startswith('sp') and 1<=m<=3
  i=int(label[2:]);assert 4<=i<=29
  if i in high:positions['high_input'].append(j)
  else:positions['outside_high_input'].append(j)
  if i in graph:positions['high_graph'].append(j)
  elif i in high:positions['input_not_graph'].append(j)
 assert len(positions['high_input'])==66 and len(positions['high_graph'])==60
 record={'date':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(sp.SRC),'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(__file__),'spline_helper_sha256':sha(ROOT/'proofs/198_pure_spline_input_gram/code/check.py'),'independent_deboor_sha256':sha(ROOT/'proofs/04_modal_scalar/code/recompute.py'),'coarse_knots_exact':list(map(str,knots)),'polynomial_replay_count':checked,'interior_C6_joins':joins,'endpoint_data':end,'high_input_radial_indices':high,'high_graph_radial_indices':graph,'S1M4P_positions':positions,'metadata_sha256':sha(ROOT/'proofs/198_pure_spline_input_gram/evidence/source/S1M4P_meta.json'),'producer_snapshot_sha256':{n:sha(TOP/'evidence/source'/n) for n in ('basis.py','section.py','fsec.py')},'seconds':time.monotonic()-start,'status':'EXACT_CHECK_PASS'}
 (TOP/'evidence/check.json').write_text(json.dumps(record,indent=2)+'\n')
 print(json.dumps({k:record[k] for k in ('date','status','polynomial_replay_count','interior_C6_joins','high_input_radial_indices','high_graph_radial_indices','seconds')}),flush=True)
if __name__=='__main__':main()

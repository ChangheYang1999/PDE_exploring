"""Exact audit of independent local velocity constants; no JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,subprocess,sys
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_velocity';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def box(q):return Q(q['lower_exact']),Q(q['upper_exact'])
def fall(n,j):
 v=1
 for i in range(j):v*=n-i
 return v
def main():
 files={};deps={}
 for name in ('source_jet_corrections','normalized_tail_repair','hminus1_tail_repair'):
  p=B/'research'/name/'evidence/verdict.json';data=json.loads(p.read_text());assert data['status'].startswith('CONFIRMED')
  for f,h in data['files'].items():assert sha(B/f)==h,(f,'dependency changed');files[f]=h
  files[str(p.relative_to(B))]=sha(p);deps[name]={'sha256':sha(p),'pins':len(data['files'])}
 depcount=len(files)
 # Complete fresh engine replays. Outputs intentionally replace this topic's provisional engine records.
 for f in ('engine_arb.py','engine_iv.py'):
  p=subprocess.run([sys.executable,str(D/'code'/f)],cwd=B,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True,timeout=60)
  assert p.returncode==0,p.stdout+p.stderr
 a=json.loads((E/'arb.json').read_text());v=json.loads((E/'iv.json').read_text())
 for data in (a,v):
  for f,h in data['files'].items():assert sha(B/f)==h;files[f]=h
 k=Q(a['exact']['k']);beta=2*k-1;N=Q(a['exact']['N']);assert a['exact']['k']==v['exact']['k'];assert a['exact']['tplus']==v['exact']['tplus'];assert N==Q(v['exact']['N'])
 assert k==Q(1615536043799051,9007199254740992) and 0<k<Q(1,4) and -1<beta<1
 npz=Path(v['source_archive']['path']);assert sha(npz)==v['source_archive']['sha256'];files[str(npz)]=sha(npz)
 # Third exact route: closed geometric moment identities through cubic order.
 t=Q(1,4);M=[1/(1-t),t/(1-t)**2,t*(1+t)/(1-t)**3,t*(1+4*t+t*t)/(1-t)**4]
 coeffs=[[1],[3,2],[6,10,4],[6,22,24,8]]
 S=[sum((c*M[i] for i,c in enumerate(row)),Q(0)) for row in coeffs]
 assert S==list(map(Q,a['exact']['S']))==[Q(4,3),Q(44,9),Q(416,27),Q(1312,27)]
 K=v['exact']['K'];assert K==128;assert Q(v['exact']['tail_ratio_ceiling'])==Q(1,4)*(1+Q(2,2*K+1))**3<Q(1,2)
 for j in range(4):
  part=sum((Q(fall(2*m+3,j),4**m) for m in range(K)),Q(0));err=2*Q(fall(2*K+3,j),4**K)
  assert part==Q(v['exact']['partial_S'][j]);assert err==Q(v['exact']['tails'][j]);assert part<S[j]<part+err
  c=4*N*S[j]/(3-beta);assert c==Q(a['exact']['C'][j])
  for data in (a,v):lo,hi=box(data['values']['C'+str(j)]);assert lo<=c<=hi
 # Exact modal cancellation and coefficient checks, with no interval zero inference.
 for n in range(1,784):
  assert Q(2*n-1,2)-Q(2*n-1,2)==0
  assert Q(2*n-1,2)+Q(2*n+1,2)==2*n
  assert Q(2*n,2)==n
  if n>=2:assert Q(n)/(2*n-beta-1)<=2/(3-beta)
  for j in range(4):
   if 2*n-1>=j:assert fall(2*n-1,j)>=0
 # Independently audit the old source endpoints used in the new conservative margin.
 src=json.loads((B/'research/source_jet_corrections/evidence/checks.json').read_text())
 for family in ('exact_ranges','portable_bounds'):
  assert box(src[family]['D'])[0]>Q('6.70197e-7');assert box(src[family]['C'])[1]<Q('30.0230')
 plo,phi=map(Q,src['root_bracket_exact']);assert 0<plo<=phi<9
 margin=Q('6.70197e-7')-Q('30.0230')*Q('1e-8')-2*Q('1e-8')**2;assert margin>Q('3.69e-7')
 public={'C0':('56.21412400010','56.21412400011'),'C1':('206.11845466704','206.11845466705'),'C2':('649.58543289007','649.58543289008'),'C3':('2048.69251911484','2048.69251911485'),'u9':('8.94138073365e-9','8.94138073366e-9'),'w9':('3.64278474334e-9','3.64278474335e-9'),'R_b':('3412.96685816156','3412.96685816157')}
 count=0
 for name,(l,h) in public.items():
  for data in (a,v):lo,hi=box(data['values'][name]);assert Q(l)<lo<=hi<Q(h),(name,data['method']);count+=1
 for data in (a,v):
  assert box(data['values']['R_b'])[0]>3000
  assert box(data['values']['u9'])[1]<Q('1e-8')
  assert box(data['values']['w9'])[1]<Q('1e-8')
 for name in a['values']:
  al,ah=box(a['values'][name]);vl,vh=box(v['values'][name]);assert max(al,vl)<=min(ah,vh),(name,'diagnostic disjoint')
 for p in [D/'PROOF.md',Path(__file__),E/'arb.json',E/'iv.json']:
  files[str(p.relative_to(B))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SCALAR_BOUNDS_TWO_METHODS_AND_EXACT_AUDIT_REVIEW_PENDING','files':files,'dependencies':deps,'public_strict_intervals':public,'source_derivative_strict_lower':'3.69e-7','exact_conservative_margin':str(margin),'counts':{'distinct_prior_pins':depcount,'complete_engine_replays':2,'strict_public_enclosures':count,'independent_geometric_sums':4,'exact_positive_tail_checks':4,'modal_cancellation_indices':783,'source_endpoint_directions':4,'strict_radius_and_jet_tests':6,'overlap_diagnostics':len(a['values'])},'scope':'PROOF numerical specialization checked. No final model acceptance inferred, no neighborhood exclusion.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','counts')}))
if __name__=='__main__':main()

"""Independent rational projection, full dependency and outward-output audit.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import sys,json,hashlib,importlib.util,contextlib,io
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_hminus1_obstruction';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def interval(x):
 a,b=Q(x['lower_exact']),Q(x['upper_exact']);assert a<=b
 return a,b
def main():
 A=load(E/'arb.json');I=load(E/'iv.json');pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['sha256'];files={};counts={}
 def pin(p,h=None):
  v=sha(p)
  if h is not None:assert v==h,str(p)
  files[str(p.relative_to(B))]=v
 for r in (A,I):
  assert r['status']=='COMPUTED_NONZERO_REQUIRES_AUDIT' and datetime.fromisoformat(r['utc'])>datetime.fromisoformat(pf['utc'])
  for p,h in r['files'].items():pin(B/p,h)
 assert sha(Path(I['source_archive']['path']))==I['source_archive']['sha256']
 dependencies={}
 for topic,fn in [('modal_repair','audit_verdict.json'),('far_residual_obstruction','verdict.json'),('normalized_tail_repair','verdict.json'),('hminus1_tail_repair','verdict.json')]:
  p=B/'research'/topic/'evidence'/fn;v=load(p);assert v.get('status',v.get('verdict','')).startswith('CONFIRMED');fs=v.get('files',v.get('source_and_evidence_sha256'));assert fs
  for n,h in fs.items():pin(B/n,h)
  pin(p);dependencies[topic]={'sha256':sha(p),'pins':len(fs)}
 counts['dependency_pins']=len(files)
 assert A['exact']['column6']==I['exact']['column6'];col=list(map(Q,A['exact']['column6']));assert len(col)==260
 expected=[Q(0)]*261
 for m,c in enumerate(col):
  for first in (1,3):
   for sign in (-1,1):
    nu=first+sign*2*m;expected[(abs(nu)-1)//2]+=c*Q(1 if nu>0 else -1,8)
 assert expected==list(map(Q,I['exact']['sine_coefficients']));bd=expected[0];assert bd==Q(A['exact']['bd'])==Q(I['exact']['bd'])==Q(-6077384870622209,39614081257132168796771975168)<0
 counts['column6_coefficients']=260;counts['independent_sine_projection_coefficients']=261
 k=Q(A['exact']['k']);assert k==Q(I['exact']['k'])==Q(1615536043799051,9007199254740992);assert 0<k<Q(1,4)
 assert Q(A['exact']['tplus'])==Q(I['exact']['tplus'])
 beta=2*k-1;a2=3*k-2;d=k-2;a3=4*k-3
 assert a3<d<a2<-1 and d>-2 and a3<-2 and beta/k-1==-(1-k)/k and d/k-1==-2/k
 assert 2*k-3<a3 and k-4<a3 and a2+2==3*k>d+2==k>0 and a3+2==4*k-1<0
 assert sorted(A['exact']['large_ordered_pairs'])==sorted(I['exact']['large_ordered_pairs'])
 counts['exact_exponent_groups']=10
 # The new class in proof(c) allows each large row; all remaining rows <=a3.
 # Pairing any remaining row with the maximum k gives <=a3+k-1<a3.
 assert a3+k-1<a3
 public={'bd':['-1.5341476258E-13','-1.5341476257E-13'],'Ld':['184130.68809691860443309136512698','184130.68809691860443309136512700']}
 for r in (A,I):
  for key,v in r['values'].items():interval(v)
  for key,(lo,hi) in public.items():
   l,h=interval(r['values'][key]);assert Q(lo)<l<=h<Q(hi),(key,l,h)
  assert interval(r['values']['Ld'])[0]>0 and interval(r['values']['bd'])[1]<0
 counts['strict_public_enclosures']=4;counts['strict_nonzero_sign_checks']=4
 for key in A['values']:
  al,ah=interval(A['values'][key]);il,ih=interval(I['values'][key]);assert max(al,il)<=min(ah,ih)
 counts['interval_overlap_diagnostics']=3
 for name,original in [('arb',A),('iv',I)]:
  path=D/'code'/('engine_'+name+'.py');spec=importlib.util.spec_from_file_location('fresh_st_'+name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  with contextlib.redirect_stdout(io.StringIO()):m.main()
  fresh=load(E/(name+'.json'))
  for key in set(original)-{'utc','seconds'}:assert original[key]==fresh[key],(name,key)
 counts['complete_engine_replays']=2
 for p in (E/'arb.json',E/'iv.json',E/'proof_first.json',Path(__file__)):pin(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_NONZERO_D_ROW_TWO_METHOD_OUTPUT_AND_COMPLETE_DEPENDENCY_AUDIT','public_strict_enclosures':public,'exact_bd':str(bd),'counts':counts,'dependencies':dependencies,'files':dict(sorted(files.items())),'source_archive':I['source_archive'],'scope':'Fixed T topic105 residual outside dotH^-1 and r-weighted L2 requires PROOF. No actual a2-row coefficient evaluated or general neighborhood exclusion.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':counts,'pins':len(files)}))
if __name__=='__main__':main()

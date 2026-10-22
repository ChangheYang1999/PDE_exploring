"""Exact endpoint/source audit and independent Simpson Peano-kernel check.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import sys,json,hashlib,math,importlib.util,contextlib,io
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_forcing_norms';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def interval(row):
 a,b=Q(row['lower_exact']),Q(row['upper_exact']);assert a<=b
 return a,b
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def main():
 A=load(E/'arb.json');I=load(E/'iv.json');pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['sha256']
 files={};counts={}
 def pin(p,h=None):
  got=sha(p)
  if h is not None:assert got==h,str(p)
  files[str(p.relative_to(B))]=got
 for data in (A,I):
  assert data['status']=='COMPUTED_REQUIRES_OUTPUT_AUDIT' and datetime.fromisoformat(data['utc'])>datetime.fromisoformat(pf['utc'])
  for p,h in data['files'].items():pin(B/p,h)
 assert sha(Path(I['source_archive']['path']))==I['source_archive']['sha256']
 dependencies={}
 for topic,fn in [('modal_repair','audit_verdict.json'),('far_profile_distance','verdict.json'),('far_residual_obstruction','verdict.json'),('normalized_tail_repair','verdict.json'),('hminus1_tail_repair','verdict.json')]:
  p=B/'research'/topic/'evidence'/fn;v=load(p);assert v.get('status',v.get('verdict','')).startswith('CONFIRMED')
  fs=v.get('files',v.get('source_and_evidence_sha256'));assert fs
  for n,h in fs.items():pin(B/n,h)
  pin(p);dependencies[topic]={'verdict_sha256':sha(p),'pins':len(fs)}
 counts['distinct_dependency_pins']=len(files)
 k=Q(A['exact']['k']);assert k==Q(I['exact']['k'])==Q(1615536043799051,9007199254740992) and 0<k<Q(1,4)
 beta=2*k-1;assert beta+1==2*k and beta+2==2*k+1 and 3*k-2<beta and k-2<beta<k and 2*k<1+k
 counts['exact_exponent_relations']=7
 for key in ('A','B_rational','B_log2'):assert Q(A['exact'][key])==Q(I['exact'][key])
 assert Q(A['exact']['A'])>0 and Q(A['exact']['B_log2'])>0
 # The Peano kernel on a unit half-width Simpson panel is
 # K(t)=-(1-t)^3*(1+3t)/72 on [0,1], and K(-t)=K(t).
 # Check the left-half polynomial identity using the full truncated powers.
 plus=mul(mul([1,-1],[1,-1]),[1,-1]);p4=mul(plus,[1,-1]);rhs=mul(plus,[1,3]);rhs=[-q/Q(72) for q in rhs]
 right=[p4[i]/24-(plus[i]/18 if i<len(plus) else 0) for i in range(5)]
 assert right==rhs
 # K(-u)=(1+u)^4/24 - [4u^3+(1+u)^3]/18.
 plus3=mul(mul([1,1],[1,1]),[1,1]);plus4=mul(plus3,[1,1]);left=[plus4[i]/24-Q((plus3[i] if i<4 else 0)+(4 if i==3 else 0))/18 for i in range(5)]
 assert left==rhs
 assert -2*sum((rhs[i]/(i+1) for i in range(5)),Q(0))==Q(1,90)
 # Scaled panel half-width h gives h^5/90; N/2 panels gives ell*h^4/180.
 N=I['exact']['N'];h=Q(I['exact']['h']);ell=Q(1,4);assert N==1024 and N%2==0 and N*h==ell and Q(N,2)*h**5/90==ell*h**4/180
 counts['exact_simpson_kernel_identities']=5
 # The independent derivative bound uses absolute Leibniz terms, so no
 # uncertain comparison or cancellation can reduce the error radius.
 G=list(map(Q,I['exact']['G_derivative_bounds']));assert G==[ell**4,4*ell**3,12*ell**2,24*ell,24]
 errlo,errhi=interval(I['simpson']['error_bound']);radius=Q(I['simpson']['added_error_upper_exact']);assert 0<errlo<=errhi==radius
 sl,sh=interval(I['simpson']['sum']);jl,jh=interval(I['values']['J']);assert jl<=sl-radius and sh+radius<=jh
 counts['simpson_enclosure_directions']=4
 public={'A':['2.27065313430059523809523809523809523809523809e-9','2.27065313430059523809523809523809523809523810e-9'],'B':['4.52279712598254949798578760017995833164792847e-7','4.52279712598254949798578760017995833164792848e-7'],'J':['0.0000228544232296','0.0000228544232302'],'C_L':['0.03135338258','0.03135338260'],'C_D':['0.0022215507882','0.0022215507884']}
 for out in (A,I):
  for key,v in out['values'].items():interval(v)
  for key,(lo,hi) in public.items():
   l,r=interval(out['values'][key]);assert Q(lo)<l<=r<Q(hi),key
  for key in ('C_L','C_D'):
   l,r=interval(out['values'][key]);assert l>Q('0.03135338258' if key=='C_L' else '0.0022215507882')
 counts['strict_public_enclosures']=10;counts['nonzero_lower_constants']=4
 for key in A['values']:
  al,ah=interval(A['values'][key]);il,ih=interval(I['values'][key]);assert max(al,il)<=min(ah,ih),key
 counts['overlap_diagnostics_only']=6
 # Full reruns, including all 1025 Simpson nodes and both E0 provenance paths.
 for name,original in [('arb',A),('iv',I)]:
  path=D/'code'/('engine_'+name+'.py');spec=importlib.util.spec_from_file_location('fresh_'+name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
  with contextlib.redirect_stdout(io.StringIO()):module.main()
  fresh=load(E/(name+'.json'))
  for key in set(original)-{'utc','seconds'}:assert fresh[key]==original[key],(name,key)
 counts['complete_engine_replays']=2
 for p in (E/'arb.json',E/'iv.json',E/'proof_first.json',Path(__file__)):pin(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_METHOD_CONSTANTS_EXACT_KERNEL_REPLAY_AND_DEPENDENCIES','public_strict_enclosures':public,'counts':counts,'dependencies':dependencies,'source_archive':I['source_archive'],'files':dict(sorted(files.items())),'scope':'Asymptotic lower constants only. Negative norms and weighted thresholds require PROOF. No finite T threshold or endpoint.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':counts,'pins':len(files)}))
if __name__=='__main__':main()

"""Independent exact source, support, projection, rounding and complete-rerun audit.
No JS/TS, servers/listeners/tunnels, RLScience, or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,hashlib,time,subprocess,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_second_row';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(v):l,h=map(F,(v['lower_exact'],v['upper_exact']));assert l<=h;return l,h
def run():
 st=time.monotonic();pins={};depcounts={}
 for name in ('modal_repair/evidence/audit_verdict.json','outer_leading_cancellation/evidence/verdict.json','normalized_tail_repair/evidence/verdict.json','hminus1_tail_repair/evidence/verdict.json'):
  p=B/'research'/name;d=json.loads(p.read_text());assert (d.get('status') or d.get('verdict')).startswith('CONFIRMED');pins[str(p.relative_to(B))]=sha(p)
  fs=d.get('files',{})
  if not fs:
   # The complete modal-repair map is also pinned in the later106 verdict.
   assert name.startswith('modal_repair/')
  for rel,h in fs.items():
   q=B/rel;assert q.resolve().is_relative_to(B) and sha(q)==h,(rel,'changed dependency');assert rel not in pins or pins[rel]==h;pins[rel]=h
  depcounts[name]=len(fs)
 first={name:json.loads((E/(name+'.json')).read_text()) for name in ('arb','iv')}
 for name,d in first.items():
  assert d['status']=='COMPUTED_REQUIRES_AUDIT'
  for rel,h in d['files'].items():assert sha(B/rel)==h;pins[rel]=h
  if name=='iv':assert sha(Path(d['source_archive']['path']))==d['source_archive']['sha256']
  for v in d['values'].values():bounds(v)
 assert first['arb']['exact']==first['iv']['exact'];ex=first['arb']['exact'];k=F(ex['k']);t=F(ex['tplus']);beta=2*k-1;a2=3*k-2;assert 0<k<F(1,4)
 p=B/'data_exact/modal_v2.json';raw=json.loads(p.read_text());assert raw['arrays']['Aout']['shape']==[260,10]
 archive=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
 with np.load(archive,allow_pickle=False) as z:
  assert sha(archive)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
  for x,hx in zip(z['Aout'].flat,raw['arrays']['Aout']['hex']):assert F(float(x))==F(float.fromhex(hx))
  assert len(raw['arrays']['Aout']['hex'])==2600
  for x,hx in zip(z['knots'],raw['arrays']['knots']['hex']):assert F(float(x))==F(float.fromhex(hx))
  assert len(z['knots'])==len(raw['arrays']['knots']['hex'])==1573
  assert F(float(z['k']))==k and F(float(z['knots'][-1]))==t
  bo=F(float(z['bo']));assert bo>120
  for col in range(3):
   ar=[F(float(x)) for x in z['Aout'][:,col]]+[F(0)]*4
   get=lambda j:ar[j] if j>=0 else F(0)
   closed=[(2*ar[0]-ar[2])/8,(2*ar[0]+ar[1]-ar[2]-ar[3])/8]+[(get(j-1)+get(j)-get(j+1)-get(j+2))/8 for j in range(2,262)]
   assert list(map(F,ex['rows'][col]))==closed
   assert closed[-1]==0
 pairs=[(j,0) for j in range(6)]+[(0,1),(1,1),(2,1),(0,2)]
 powers=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo];a3=4*k-3
 assert [(i,j) for i,x in enumerate(powers) for j,y in enumerate(powers) if x+y-1==a2]==[(0,1),(1,0)]
 assert all(x+y-1<=a3 for i,x in enumerate(powers) for j,y in enumerate(powers) if (i,j) not in ((0,0),(0,1),(1,0)))
 assert all(x-2*n-2<a3 for x in powers for n in range(1,523))
 assert a2+2==3*k and 3*k>k>0 and a3+2<0
 # Independent exact frequency projections on each of four bilinear basis entries.
 identities=0
 for aa,bb in ((k,beta),(beta,k)):
  for n in range(1,262):
   m=2*n;den=m*m-(aa+1)**2;assert den>0
   for ai in (0,1):
    A=[F(int(ai==j)) for j in (0,1)]
    fn=((aa+1-m)*A[0]+(aa+1+m)*A[1])/2
    vr=-m*fn/den;vt=(aa+1)*fn/den
    for bi in (0,1):
     C=[F(int(bi==j)) for j in (0,1)];j=n-1+bi;freq=2*j+1
     # Explicit frequency signs, independent of the closed adjacent-index formula.
     sincos=F(int(freq+m==1)+int(freq-m==1)-int(freq-m==-1),2)
     cossin=F(int(m+freq==1)+int(m-freq==1)-int(m-freq==-1),2)
     direct=bb*vr*sincos+vt*freq*cossin
     closed=fn/(2*den)*((m*(aa+bb+1)-(aa+1))*C[0]-(m*(aa+bb+1)+(aa+1))*C[1])
     assert direct==closed;identities+=1
 support=0
 for n in range(1,523):
  for j in range(522):
   contributes=abs(2*n-(2*j+1))==1
   assert contributes==(j==n-1 or j==n)
   if n>261 and j<=260:assert not contributes
   support+=1
 pub=json.loads((D/'source/public_bounds.json').read_text());public_checks=0;overlaps=0
 for name,d in first.items():
  for key,vals in pub.items():
   lo,hi=map(F,vals);l,h=bounds(d['values'][key]);assert lo<l<=h<hi<0;public_checks+=1
  zlo,zhi=bounds(d['values']['z']);assert F('-1.198605236453734890460334164888e-20')<zlo<=zhi<F('-1.198605236453734890460334164887e-20')
  # Saved scalar source identity checked as interval containment, not rounded displays.
  l0,h0=bounds(d['values']['C20']);parts=[bounds(d['values'][v]) for v in ('linear','first','second')]
  assert max(l0,sum(v[0] for v in parts))<=min(h0,sum(v[1] for v in parts))
  lh,hh=bounds(d['values']['H20']);ratio=k/(2*(1-k));assert max(lh,ratio*l0)<=min(hh,ratio*h0)
 for key in first['arb']['values']:
  l,h=bounds(first['arb']['values'][key]);ll,hh=bounds(first['iv']['values'][key]);assert max(l,ll)<=min(h,hh);overlaps+=1
 for name in ('arb','iv'):
  cp=subprocess.run([sys.executable,str(D/'code'/('engine_'+name+'.py'))],cwd=B,capture_output=True,text=True,timeout=120,env=os.environ.copy());(E/('rerun_'+name+'.log')).write_text(cp.stdout+cp.stderr);assert cp.returncode==0
  d=json.loads((E/(name+'.json')).read_text());old=first[name]
  for obj in (d,old):obj.pop('utc');obj.pop('seconds')
  assert d==old,(name,'nonreproducible complete output')
 for p in (D/'PROOF.md',D/'source/public_bounds.json',D/'code/engine_arb.py',D/'code/engine_iv.py',Path(__file__),E/'arb.json',E/'iv.json',E/'proof_first.json',E/'rerun_arb.log',E/'rerun_iv.log'):pins[str(p.relative_to(B))]=sha(p)
 pf=json.loads((E/'proof_first.json').read_text());assert pf['proof_sha256']==sha(D/'PROOF.md')
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_FINITE_AUDIT_REVIEW_STILL_OPEN','method':'Exact original-source comparison, third closed sine map, explicit signed Fourier basis projection, all support pairs, strict public bounds and two complete engine reruns','dependency_counts':depcounts,'files':pins,'counts':{'original_outer_coefficients':2600,'original_knots':1573,'third_projected_sines':786,'bilinear_basis_identities':identities,'support_pairs':support,'ordered_exponent_pairs':121,'homogeneous_comparisons':11*522,'strict_public_enclosures':public_checks,'overlap_diagnostics':overlaps,'complete_engine_reruns':2},'strict_public_bounds':pub,'seconds':time.monotonic()-st,'scope':'Numerical and independent mathematical checks complete. No actual new model review. Not FINAL and no decisive endpoint.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','counts','seconds')}))
if __name__=='__main__':run()

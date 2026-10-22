"""New exact input binding and sparse angular image audit; no producer imports."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math,time
import numpy as np
from flint import arb,fmpq,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_three_cell_linkage';E=D/'evidence'
def need(v,s):
 if not v:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':'))
def write(p,v):
 with p.open('x') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def exact(x):
 need(np.isfinite(x),'finite scalar');return F.from_float(float(x))
def abounds(x):
 need(x.is_finite(),'finite Arb');out=[]
 for y in (x.lower(),x.upper()):
  m,e=y.man_exp();out.append(F(int(m))*F(2)**int(e))
 return out

def ibounds(x):
 out=[]
 for s,m,e,bc in x._mpi_:
  need(s in (0,1) and m>=0 and m==int(m) and type(e) is int and type(bc) is int and bc>=0,'finite interval dyadic');out.append((-1 if s else 1)*F(int(m))*F(2)**e)
 return out

def hweights(j):
 raw=[(0,2),(2,-1)] if j==0 else ([(0,2),(1,1),(2,-1),(3,-1)] if j==1 else [(j-1,1),(j,1),(j+1,-1),(j+2,-1)])
 return {m:F(w,8) for m,w in raw if 0<=m<260}

def main():
 start=now();timer=time.monotonic();pins={};pathcache={};dep_records=[]
 def pin(path,h=None):
  p=Path(path);p=(p if p.is_absolute() else B/p).resolve();need(p.is_relative_to(B) or p in {B.parent/'ipmA-num/data'/n for n in ['cert_green.npz','cert_inner_green.npz','cert_outer_green.npz','trial_v2_h0.008.npz']},'allowed exact dependency path')
  stat=p.stat();key=(str(p),stat.st_size,stat.st_mtime_ns);actual=pathcache.get(key)
  if actual is None:actual=sha(p);pathcache[key]=actual
  need(h is None or h==actual,'unchanged dependency '+str(p));name=str(p.relative_to(B)) if p.is_relative_to(B) else str(p);need(name not in pins or pins[name]==actual,'consistent repeated pin');pins[name]=actual;return actual
 expected=[('radial_tm_instance','5094d932431eb3abf2a0fedce225d3cd0e15b1ff499f7ef06471d2390710e6db','CONFIRMED_SELECTED_FINITE_INPUT_ODE_ENCLOSURES'),('full_green_linkage','a026f566d277e12ed22b05ec1eb5aadfabe66449940eb3644c96cbe961fbabd5','CONFIRMED_COMPLETE_GREEN_AB_BOUNDARIES_SHARED_CANONICAL_INPUTS'),('full_t_linkage','3732110a42745c75a1f10cf1e057d0d0d6b81a087bb74e3d9289ef0b0e33635b','CONFIRMED_COMPLETE_FINITE_SPLINE_T_AND_H_MEMBERSHIP')]
 deps={};pin_assertions=0
 for name,h,status in expected:
  p=B/'research'/name/'evidence/verdict.json';pin(p,h);v=load(p);need(v['status']==status,'accepted status');deps[name]=v
  for rel,val in v['files'].items():pin(rel,val);pin_assertions+=1
  dep_records.append({'topic':name,'verdict_sha256':h,'status':status,'utc':v['utc'],'pins':len(v['files'])})
 need(deps['radial_tm_instance']['cells']==[0,4102,7808] and deps['radial_tm_instance']['modes']==261,'selected ODE scope')
 need(deps['full_green_linkage']['boundaries']==7810 and deps['full_green_linkage']['modes']==261 and deps['full_green_linkage']['entries_per_engine']==4076820,'complete A/B scope')
 need(deps['full_t_linkage']['cells']==7809 and deps['full_t_linkage']['exact_T_coefficients']==16242720 and deps['full_t_linkage']['exact_archive_H_coefficients']==3265568,'complete T/H scope')
 green=B.parent/'ipmA-num/data/cert_green.npz';gh=pin(green,'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1')
 for name,v in deps.items():need(v['files'][str(green)]==gh,'same actual target in all three accepted results')
 partpath=B/'research/middle_residual/evidence/partition_exact.json';pin(partpath,'56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2');part=load(partpath)
 need(part['grid_sha256']==gh and part['input_sha256']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6' and part['cells']==7809 and len(part['spans'])==1558,'exact trial and partition source')
 previous=None;counter=0
 for i,s in enumerate(part['spans']):
  a,b=F(s['a_exact']),F(s['b_exact']);need(s['span']==i and s['first_cell']==counter and type(s['count']) is int and s['count']>0 and a<b and (previous is None or a==previous),'ordered exact original partition');counter+=s['count'];previous=b
 need(counter==7809,'complete partition')
 with np.load(green,allow_pickle=False) as z:source={k:z[k].copy() for k in ['T_mid','T_rad','A_mid','A_rad','B_mid','B_rad','tb','tb_rad','parent']}
 for key,arr in source.items():
  need(np.isfinite(arr).all(),'finite original source array')
  if key!='parent':need(arr.dtype==np.dtype('float64'),'exact target float64')
  if key.endswith('_rad'):need((arr>=0).all(),'nonnegative target radii')
 for key in ['T_mid','T_rad']:need(source[key].shape==(7809,8,260),'T shape')
 for key in ['A_mid','A_rad','B_mid','B_rad']:need(source[key].shape==(7810,261),'A/B shape')
 need(source['tb'].shape==source['tb_rad'].shape==(7810,) and source['parent'].shape==(7809,) and source['parent'].dtype==np.dtype('int64'),'boundary/parent shapes')
 scalarpath=B/'research/flow_scalars/evidence/scalar_arrays.npz';pin(scalarpath,'aa8b3733507b58d0ea4f8a096c20187f344d5165ff6b655e3b8c3e4e992cc114')
 with np.load(scalarpath,allow_pickle=False) as z:sc=z['middle'].copy()
 need(sc.shape==(7809,36) and sc.dtype==np.dtype('float64') and np.isfinite(sc).all(),'scalar source shape')
 ctx.prec=640;ctx.threads=1;iv.dps=200;cells=[];counts={'input_arrays_identical':0,'input_scalar_entries_identical':0,'candidate_arrays_pinned':0,'coordinate_memberships':0,'length_upper_bounds':0,'E_arb640_containments':0,'E_iv200_containments':0,'exact_F_images':0,'signed_vs_collected_weights':0};stream=E/'forcing_records.jsonl';streamhash=hashlib.sha256();worst=None
 # Independently compare collected H identities to individual signed frequencies.
 signed=[{} for _ in range(262)]
 for m in range(260):
  for freq in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(freq)-1)//2; signed[j][m]=signed[j].get(m,F(0))+F(1 if freq>0 else -1,8)
 for j in range(262):
  need({m:w for m,w in signed[j].items() if w}==hweights(j),'exact independent angular identity');counts['signed_vs_collected_weights']+=1
 with stream.open('x') as output:
  for ci in [0,4102,7808]:
   matches=[s for s in part['spans'] if s['first_cell']<=ci<s['first_cell']+s['count']];need(len(matches)==1,'unique original parent');s=matches[0];a,b=F(s['a_exact']),F(s['b_exact']);index=ci-s['first_cell'];width=(b-a)/s['count'];left=a+index*width;right=left+width
   need(a<=left<right<=b and source['parent'][ci]==s['span'],'single exact span and parent')
   p=B/'research/radial_tm_instance/evidence'/('selected_v3_cell_%04d.npz'%ci);pin(p,deps['radial_tm_instance']['files'][str(p.relative_to(B))])
   with np.load(p,allow_pickle=False) as z:arrays={k:z[k].copy() for k in z}
   expectedshapes={'P_mid':(261,13),'P_rad':(261,13),'P_rem':(261,),'R_mid':(261,13),'R_rad':(261,13),'R_rem':(261,),'F_mid':(261,8),'F_rad':(261,8),'A_mid':(261,),'A_rad':(261,),'B_mid':(261,),'B_rad':(261,),'T_mid':(8,260),'T_rad':(8,260),'scalar':(36,)}
   need(set(arrays)==set(expectedshapes),'complete saved candidate')
   for k,z in arrays.items():
    need(z.shape==expectedshapes[k] and z.dtype==np.dtype('float64') and np.isfinite(z).all(),'candidate dimensions/dtype/finite')
    if k.endswith(('_rad','_rem')):need((z>=0).all(),'candidate nonnegative radii/budgets')
    counts['candidate_arrays_pinned']+=1
   for key in ['T_mid','T_rad','A_mid','A_rad','B_mid','B_rad']:
    x,y=arrays[key],source[key][ci];need(x.shape==y.shape and x.tobytes()==y.tobytes(),'entire selected input array identity '+key);counts['input_arrays_identical']+=1;counts['input_scalar_entries_identical']+=x.size
   need(arrays['scalar'].tobytes()==sc[ci].tobytes(),'entire scalar input identity');counts['input_arrays_identical']+=1;counts['input_scalar_entries_identical']+=36
   h,em,er=map(exact,arrays['scalar'][:3]);need(0<width<=h and 522*h<1 and em-er>0 and er>=0,'actual length and positive E');counts['length_upper_bounds']+=1
   for j,q in [(ci,left),(ci+1,right)]:
    mid,rad=exact(source['tb'][j]),exact(source['tb_rad'][j]);need(mid-rad<=q<=mid+rad,'exact coordinate target');counts['coordinate_memberships']+=1
   qa=arb(fmpq(left.numerator,left.denominator));qi=iv.mpf(left.numerator)/left.denominator;elist=[]
   for engine,computed in [('arb640',abounds(qa.exp())),('iv200',ibounds(iv.exp(qi)))]:
    lo,hi=computed;need(em-er<=lo<=hi<=em+er,'whole independent E containment');counts['E_'+engine+'_containments']+=1;elist.append({'engine':engine,'lower':str(lo),'upper':str(hi),'target_lower':str(em-er),'target_upper':str(em+er)})
   tm=[[exact(x) for x in row] for row in arrays['T_mid']];tr=[[exact(x) for x in row] for row in arrays['T_rad']];localworst=None
   for n in range(1,262):
    for k in range(8):
     weights={}
     for j,factor in [(n-1,F(4-2*n,2)),(n,F(4+2*n,2))]:
      for m,w in hweights(j).items():weights[k,m]=weights.get((k,m),F(0))+factor*w
     if k<7:
      for j in [n-1,n]:
       for m,w in hweights(j).items():weights[k+1,m]=weights.get((k+1,m),F(0))+F(k+1,2)*w
     center=sum((w*tm[q][m] for (q,m),w in weights.items()),F(0));radius=sum((abs(w)*tr[q][m] for (q,m),w in weights.items()),F(0));targetmid=exact(arrays['F_mid'][n-1,k]);targetrad=exact(arrays['F_rad'][n-1,k]);lo,hi=center-radius,center+radius;tl,th=targetmid-targetrad,targetmid+targetrad;margin=min(lo-tl,th-hi);need(margin>=0,'whole exact forcing image containment')
     record={'cell':ci,'n':n,'k':k,'image_lower':str(lo),'image_upper':str(hi),'target_lower':str(tl),'target_upper':str(th),'margin':str(margin)};line=canon(record)+'\n';output.write(line);streamhash.update(line.encode());counts['exact_F_images']+=1
     if localworst is None or margin<F(localworst['margin']):localworst=record
     if worst is None or margin<F(worst['margin']):worst=record
   cells.append({'cell':ci,'parent':s['span'],'left_exact':str(left),'right_exact':str(right),'length_exact':str(width),'h_upper_exact':str(h),'E':elist,'F_worst':localworst,'saved_candidate_sha256':sha(p)})
  output.flush();os.fsync(output.fileno())
 need(counts=={'input_arrays_identical':21,'input_scalar_entries_identical':15720,'candidate_arrays_pinned':45,'coordinate_memberships':6,'length_upper_bounds':3,'E_arb640_containments':3,'E_iv200_containments':3,'exact_F_images':6264,'signed_vs_collected_weights':262},'complete expected counts')
 need(sha(stream)==streamhash.hexdigest(),'whole saved comparison stream')
 for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),stream]:pin(p)
 pf=load(E/'proof_first.json');need(pf['proof_sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(start),'proof first')
 # No source may change while checking: rehash all unique dependencies once more.
 for name,h in pins.items():need(sha(Path(name) if Path(name).is_absolute() else B/name)==h,'post-check unchanged source '+name)
 out={'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_SELECTED_CANONICAL_INPUT_BINDINGS_CONDITIONAL_ON_ARCHIVE_MOMENTS','source_sha256':sha(__file__),'dependency_verdicts':dep_records,'dependency_pin_assertions':pin_assertions,'counts':counts,'cells':cells,'forcing_stream_sha256':sha(stream),'forcing_worst':worst,'seconds':time.monotonic()-timer,'runtime':{'python':sys.version,'arb_bits':640,'iv_decimal_digits':200,'threads':1},'files':dict(sorted(pins.items())),'scope':'New exact source and full forcing-box linkage of accepted93/98/99 on three selected cells. Entire canonical radial statement remains conditional on archive I/J moment membership and separately later actual-output review. No rerun of inherited complete computations; no historical-flow, other-cell, field, inverse or IPM conclusion.'}
 write(E/'checks.json',out);print(json.dumps({k:out[k] for k in ['utc','status','counts','dependency_pin_assertions','seconds']}),flush=True)
if __name__=='__main__':main()

from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import importlib.util,json,sys,time,gzip
from flint import fmpq as Q
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/scaled_rank_peer';PEER=ROOT.parent/'c1-t4/research/scaled_rank_audit'
sys.set_int_max_str_digits(0);sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def main():
 tick=time.monotonic();dest=B/'verification/result.json';assert not dest.exists();inputs={};frozen={}
 def read(p):
  p=Path(p);inputs[str(p.relative_to(ROOT))]=sha(p);return json.loads(p.read_text())
 oldpath=ROOT/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json';old=read(oldpath)
 prior=read(ROOT/'research/scaled_quotient_rank/verification/result.json')
 for rel,h in prior['inputs'].items():assert sha(ROOT/rel)==h;inputs[rel]=h
 audit=read(ROOT/'research/optimizer_quotient_audit/verification/result.json')
 for rel,h in audit['inputs'].items():assert sha(ROOT/rel)==h;inputs[rel]=h
 row=next(r for r in audit['rows'] if r['candidate']=='C1-N1-013-pairU-from007')
 assert row['new_source_sha256']==sha(oldpath) and row['all_canonical_coefficients_equal'] and row['selected_original_shapes_match']
 assert row['selected_columns']==1922 and row['nonpivot_relations']==0 and sum(b['rank'] for b in row['blocks'])==1922
 known={sha(ROOT/p):ROOT/p for p in inputs}
 def freeze(p,wanted=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert wanted is None or h==wanted
  if h in known:out=known[h];compressed=False
  else:
   out=B/'source'/p.relative_to(PEER);compressed=len(blob)>1000000
   if compressed:out=out.with_name(out.name+'.gz')
   out.parent.mkdir(parents=True,exist_ok=True);data=gzip.compress(blob,mtime=0) if compressed else blob
   if out.exists():assert out.read_bytes()==data
   else:
    with out.open('xb') as f:f.write(data)
  frozen[str(out.relative_to(ROOT))]={'source':str(p),'sha256':h,'stored_sha256':sha(out),'gzip':compressed}
  return json.loads(blob) if p.suffix=='.json' else None
 peer=freeze(PEER/'verification/result.json')
 for p,h in peer['inputs'].items():freeze(p,h)
 c=Q(4076476460239181,2251799813685248);delta=1-1/c;ps=[(3+1/c-j*delta)/2 for j in range(8)]
 assert ps==list(map(Q,peer['p_j'])) and all(p.denominator!=1 for p in ps)
 diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert diffs==list(map(Q,peer['noninteger_branch_differences'])) and all(x.denominator!=1 for x in diffs)
 rows=[];shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 for scale,ident,dirname,filename in [(25,'016','scaled_factored_weak','fields25.py'),(50,'017','scaled50_factored_weak','fields50.py')]:
  enginepath=ROOT/'research'/dirname/'code'/filename;F=module('n4_rank_recheck_'+ident,enginepath);inputs[str(enginepath.relative_to(ROOT))]=sha(enginepath)
  rawpath=ROOT/f'research/candidate_audits/data/C1-N1-{ident}-legqs{scale}-quot013/quot013_legqs{scale}_m9to15_cpu_m16_exact.json';raw=read(rawpath)
  obj=read(ROOT/f'research/candidate{ident}_holdout/verification/result.json');assert obj['raw_sha256']==sha(rawpath)
  assert len(raw['generators'])==2174 and len(old['generators'])==1922 and list(map(shape,raw['generators'][:1922]))==list(map(shape,old['generators']))
  assert {shape(g) for g in raw['generators'][1922:]}=={(j,m,('legqs',0,n,4,scale)) for j in range(1,4) for m in range(9,16) for n in range(12)}
  p=next(p for p in peer['rows'] if p['candidate']==ident);assert p['scale']==scale and p['potential_rank']==2174 and p['all_shapes_equal']
  target={ (z['m'],z['N']):z for z in p['witnesses'] };assert len(target)==84
  a=Q(scale*scale-1);v0=-1/a;t0=1-v0;witnesses=[]
  for m in range(9,16):
   for n in range(12):
    A=F.generator(m,['legqs',0,n,4,scale]);assert A.powers==(0,4+n,0)
    numerator=A.numerator_v()(v0);expected=Q(scale)**8*v0**4*comb(2*n,n)*t0**(m+n)
    assert numerator==expected and numerator!=0;coefficient=numerator/a**(4+n)
    t=target[m,n];assert t['pole_order']==4+n and Q(t['coefficient'])==coefficient
    if scale==25:
     t0old=next(z for z in prior['pole_witnesses'] if z['m']==m and z['N']==n)
     assert Q(t0old['laurent_coefficient'])==coefficient
    witnesses.append({'m':m,'N':n,'pole_order':4+n,'laurent_coefficient':str(coefficient),'independent_peer_equal':True})
  leading=4*19*18*(ps[1]-9-Q(4,scale*scale));assert leading==Q(p['mode17_coefficient']) and leading!=0
  fixture={'cl_exact':str(c),'generators':[{'j':1,'m':9,'spec':['legqs',0,0,4,scale],'coef':'1'}]};model=F.ScaledRadial(fixture)
  assert sorted(n for j,n in model.rho)==[17,19]
  A=model.rho[1,17];assert next(i for i,z in enumerate(A.P) if z)==10
  denom=Q(1)
  for factor,power in zip(F.SCALES,A.powers,strict=True):denom*=(1+factor)**power
  assert A.P[10]/denom==leading
  rows.append({'candidate':obj['candidate'],'raw_sha256':sha(rawpath),'scale':scale,'potential_dimension':2174,'generator_shapes_exact':True,'pole_witnesses':witnesses,'mode17_coefficient':str(leading),'Cartesian_density_witness_equal':True})
 for p in [B/'PROOF.md',Path(__file__),ROOT/'research/optimizer_quotient_audit/PROOF.md']:inputs[str(p.relative_to(ROOT))]=sha(p)
 assert all(sha(ROOT/p)==h for p,h in inputs.items())
 assert all(sha(ROOT/p)==d['stored_sha256'] for p,d in frozen.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'p_j':list(map(str,ps)),'noninteger_differences':list(map(str,diffs)),'inputs':inputs,'frozen_sources':frozen,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED potential dimension2174 and mode17 witness at both scales, independently agreeing with T4-321. Density injectivity is separate and remains OPEN Opus review.'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',len(rows)*84,'Laurent witnesses',sha(dest),out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

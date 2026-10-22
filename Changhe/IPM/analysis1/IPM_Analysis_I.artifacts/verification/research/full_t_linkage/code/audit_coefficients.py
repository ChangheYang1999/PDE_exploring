"""Separate output/coverage audit; exact Fraction Newton differences, no producer import."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
from datetime import datetime,timezone
from time import monotonic
import argparse,gzip,hashlib,json,math,re,resource,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/full_t_linkage';E=D/'evidence'
TRIAL_SHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
GREEN_SHA='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
ARCHIVE_SHA='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
PARTITION_SHA='56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2'

def utc():return datetime.now(timezone.utc).isoformat()
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
def unique(pairs):
 result={}
 for key,v in pairs:assert key not in result,('duplicate key',key);result[key]=v
 return result
def parse(s):return json.loads(s,object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def load(path):return parse(Path(path).read_text())
def exact_hex(s):
 m=re.fullmatch(r'(?P<sign>[+-]?)0x(?P<whole>[0-9A-Fa-f]+)\.(?P<part>[0-9A-Fa-f]*)p(?P<exp>[+-]?\d+)',s);assert m
 v=m.groupdict();numerator=int(v['whole']+v['part'],16)*(-1 if v['sign']=='-' else 1);result=Q(numerator)*Q(2)**(int(v['exp'])-4*len(v['part']))
 f=float.fromhex(s);assert math.isfinite(f) and Q.from_float(f)==result
 return result
def exact_float(v):
 v=float(v);assert math.isfinite(v);return Q(*v.as_integer_ratio())
def archive_interval(v):
 assert set(v)=={'schema','mid_m','mid_e','rad_m','rad_e'} and v['schema']=='arb-dyadic-mid-radius-v1'
 mid=Q(int(v['mid_m']))*Q(2)**int(v['mid_e']);rad=Q(int(v['rad_m']))*Q(2)**int(v['rad_e']);assert rad>=0;return mid-rad,mid+rad

def recursive_basis(knots,ell,t):
 @lru_cache(None)
 def value(i,degree):
  if degree==0:return Q(int(knots[i]<=t<knots[i+1]))
  first=Q(0) if knots[i+degree]==knots[i] else (t-knots[i])*value(i,degree-1)/(knots[i+degree]-knots[i])
  second=Q(0) if knots[i+degree+1]==knots[i+1] else (knots[i+degree+1]-t)*value(i+1,degree-1)/(knots[i+degree+1]-knots[i+1])
  return first+second
 return [value(i,7) for i in range(ell-7,ell+1)]

def newton_coefficients(values,shift,step):
 """Coefficients in u after x=shift+step*u, Newton nodes x=0,...,7."""
 diff=list(values);leading=[]
 while diff:
  leading.append(diff[0]);diff=[b-a for a,b in zip(diff,diff[1:])]
 answer=[Q(0)]*8;basis=[Q(1)]
 for r,d in enumerate(leading):
  for k,v in enumerate(basis):answer[k]+=d*v
  if r<7:
   new=[Q(0)]*(len(basis)+1)
   for k,v in enumerate(basis):new[k]+=v*(shift-r)/(r+1);new[k+1]+=v*step/(r+1)
   basis=new
 return answer

def archive_provenance():
 manifest=load(B/'research/middle_residual/evidence/knot_manifest.json');audit=load(B/'research/middle_residual/evidence/knot_audit.json')
 assert manifest['output_sha256']==ARCHIVE_SHA and audit['status']=='PASS' and audit['archive_sha256']==ARCHIVE_SHA and audit['partition_sha256']==PARTITION_SHA and audit['footer_read']
 assert audit['manifest_sha256']==sha(B/'research/middle_residual/evidence/knot_manifest.json') and audit['source_sha256']==sha(B/'research/middle_residual/code/audit_knots.py')
 dep={'source':'research/middle_residual/code/build_knot_moments.py','setup':'research/middle_residual/code/modal_setup.py','fast_moments':'research/middle_residual/code/fast_moments.py','input':'data_exact/modal_v2.json','normalization':'research/modal_repair/evidence/independent_gauss_iv.json','Cox':'research/canonical_inverse/code/exact_audit.py','ball_transport':'research/ball_transport/code/dyadic_ball.py'}
 assert {k:sha(B/v) for k,v in dep.items()}==manifest['hashes']
 return {v:sha(B/v) for v in dep.values()}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full');ap.add_argument('--allow-partial',action='store_true');args=ap.parse_args();assert args.tag.replace('_','').isalnum()
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=monotonic();path=E/(args.tag+'_spans.jsonl');summary=load(E/(args.tag+'_summary.json'))
 with path.open() as f:lines=f.readlines()
 assert lines and all(line.endswith('\n') for line in lines);header,*rows,footer=map(parse,lines);assert header['type']=='header' and header['schema']=='ipm-full-t-linkage-v1' and footer['type']=='complete'
 selected=header['selected_spans'];assert selected and selected==sorted(set(selected)) and min(selected)>=0 and max(selected)<1558;full=selected==list(range(1558));assert header['full_run']==full and (full or args.allow_partial)
 assert summary['status']==('COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT' if full else 'OPEN_PARTIAL_DIAGNOSTIC') and summary['output_sha256']==sha(path)
 assert header['files']==summary['files'] and header['arb_bits']==640 and header['exact_engine']=='python-flint fmpq matrices'
 for relative,digest in header['files'].items():assert sha(B/relative)==digest,relative
 assert summary['source_sha256']==header['files']['research/full_t_linkage/code/check_coefficients.py']==sha(D/'code/check_coefficients.py')
 for relative in ('research/full_t_linkage/PROOF.md','research/full_t_linkage/ADDENDUM.md','research/full_t_linkage/evidence/proof_first.json','research/full_t_linkage/evidence/addendum_first.json'):assert relative in header['files']
 resume_path=E/(args.tag+'_resume_events.jsonl');events=[]
 if resume_path.exists():
  assert summary['resume_events_sha256']==sha(resume_path)
  with resume_path.open() as rf:
   for line in rf:
    assert line.endswith('\n');ev=parse(line);r=ev['resumed_spans'];assert isinstance(r,int) and 0<=r<=len(rows)
    assert ev['producer_sha256']==summary['source_sha256'] and ev['header_sha256']==hashlib.sha256(json.dumps(header,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert ev['last_saved_span']==(selected[r-1] if r else None) and ev['next_span']==(selected[r] if r<len(selected) else None);events.append(ev)
 else:assert summary['resume_events_sha256'] is None
 assert events==summary['resume_events'] and summary['resumed_spans']==(events[-1]['resumed_spans'] if events else 0)
 replay_required_spans=sorted({selected[0]}|{i for ev in events for i in (ev['last_saved_span'],ev['next_span']) if i is not None})
 deps=archive_provenance()
 trial=B/'data_exact/modal_v2.json';archive=B/'research/middle_residual/evidence/original_knots.jsonl.gz';partition=B/'research/middle_residual/evidence/partition_exact.json';green=Path(header['green_path'])
 assert sha(trial)==TRIAL_SHA and sha(archive)==ARCHIVE_SHA and sha(partition)==PARTITION_SHA and sha(green)==header['green_sha256']==GREEN_SHA
 data=load(trial);assert data['degree']==7 and data['arrays']['S']['shape']==[260,1565] and data['arrays']['knots']['shape']==[1573]
 knots=list(map(exact_hex,data['arrays']['knots']['hex']));assert len(knots)==1573 and all(a<=b for a,b in zip(knots,knots[1:]));nonempty=[(i,a,b) for i,(a,b) in enumerate(zip(knots,knots[1:])) if a<b];assert len(nonempty)==1558
 S=data['arrays']['S']['hex'];assert len(S)==260*1565
 partdoc=load(partition);assert partdoc['cells']==7809 and partdoc['input_sha256']==TRIAL_SHA and partdoc['grid_sha256']==GREEN_SHA;parts=partdoc['spans'];assert len(parts)==1558
 with np.load(green,allow_pickle=False) as g:arrays={k:g[k] for k in ('T_mid','T_rad','tb','tb_rad','parent')}
 for key,value in arrays.items():
  assert np.all(np.isfinite(value)),key
  if key!='parent':assert value.dtype==np.dtype('float64')
 assert arrays['T_mid'].shape==arrays['T_rad'].shape==(7809,8,260) and np.all(arrays['T_rad']>=0)
 assert arrays['tb'].shape==arrays['tb_rad'].shape==(7810,) and np.all(arrays['tb_rad']>=0)
 assert arrays['parent'].shape==(7809,) and np.issubdtype(arrays['parent'].dtype,np.integer)
 first=0;owner={};coords={}
 for i,(part,(ell,left,right)) in enumerate(zip(parts,nonempty)):
  assert 7<=ell<1565 and part=={'span':i,'first_cell':first,'count':part['count'],'a_exact':str(left),'b_exact':str(right)} and isinstance(part['count'],int) and part['count']>0
  assert all(int(v)==i for v in arrays['parent'][first:first+part['count']])
  for j in range(part['count']+(i==1557)):
   cell=first+j;t=left+(right-left)*Q(j,part['count']);assert cell not in coords;coords[cell]=t
   mid=exact_float(arrays['tb'][cell]);rad=exact_float(arrays['tb_rad'][cell]);assert mid-rad<=t<=mid+rad
   if j<part['count']:owner[cell]=i
  first+=part['count']
 assert first==7809 and set(owner)==set(range(7809)) and set(coords)==set(range(7810))
 seed=hashlib.sha256((TRIAL_SHA+GREEN_SHA+ARCHIVE_SHA+':T').encode()).hexdigest();sample=set()
 for i in range(192):
  raw=hashlib.sha256((seed+':'+str(i)).encode()).digest();sample.add((int.from_bytes(raw[:8],'big')%7809,raw[8]%8,int.from_bytes(raw[9:17],'big')%260))
 assert len(sample)==192
 for cell in (0,4102,7808):
  for power in (0,1,7):
   for mode in (0,1,2,3,128,258,259):sample.add((cell,power,mode))
 assert header['sample_seed']==seed and header['sample_triples']==sorted(map(list,sample))
 expected_sample={key for key in sample if owner[key[0]] in selected};captured={};required={};H_required={};totals=Counter();saved_endpoint_checks=0
 def saved_value(rec,span):
  nonlocal saved_endpoint_checks
  cell,k,m=rec['cell'],rec['power'],rec['mode'];assert owner[cell]==span and 0<=k<8 and 0<=m<260 and Q(rec['t_exact'])==coords[cell]
  assert rec['target_mid_hex']==float(arrays['T_mid'][cell,k,m]).hex() and rec['target_rad_hex']==float(arrays['T_rad'][cell,k,m]).hex()
  target_mid=exact_hex(rec['target_mid_hex']);target_rad=exact_hex(rec['target_rad_hex']);assert target_rad>=0
  value=Q(rec['exact']);lo,hi=Q(rec['arb_lo']),Q(rec['arb_hi']);tl,th=target_mid-target_rad,target_mid+target_rad
  assert tl<=lo<=value<=hi<=th;saved_endpoint_checks+=1
  key=(cell,k,m)
  if key in required:assert required[key]==rec
  else:required[key]=rec
  return {'arb':min(lo-tl,th-hi),'rational':min(value-tl,th-value),'cross':min(value-lo,hi-value)}
 assert len(rows)==len(selected)==footer['spans']==summary['spans']
 for row,i in zip(rows,selected):
  part=parts[i];assert row['type']=='span' and all(row[k]==v for k,v in part.items()) and not row['failures']
  expected={'arb_contained':part['count']*2080,'rational_contained':part['count']*2080,'rational_in_arb':part['count']*2080,'archive_H_contained':2096,'deboor_cox_equalities':64};assert row['counts']==expected;totals.update(expected)
  for key in ('stream_sha256','H_stream_sha256'):assert re.fullmatch('[0-9a-f]{64}',row[key])
  assert set(row['worst_margins'])=={'arb','rational','cross','archive_H'}
  for kind in ('arb','rational','cross'):
   w=row['worst_margins'][kind];margins=saved_value(w['entry'],i);assert Q(w['margin_exact'])==margins[kind]>=0
  hw=row['worst_margins']['archive_H'];entry=hw['entry'];j,k=entry['j'],entry['power'];assert 0<=j<262 and 0<=k<8;lo,hi,value=Q(entry['target_lo']),Q(entry['target_hi']),Q(entry['exact']);assert lo<=value<=hi and Q(hw['margin_exact'])==min(value-lo,hi-value)>=0;H_required[i]=entry
  for rec in row['selected_records']:
   key=(rec['cell'],rec['power'],rec['mode']);assert key not in captured;captured[key]=rec;saved_value(rec,i)
 assert set(captured)==expected_sample and summary['selected_records']==len(captured)
 assert dict(totals)==summary['counts'] and footer['cells']==summary['cells']==header['expected_cells']==sum(parts[i]['count'] for i in selected)
 assert footer['combined_stream_sha256']==hashlib.sha256(''.join(r['stream_sha256']+r['H_stream_sha256'] for r in rows).encode()).hexdigest()
 if full:assert summary['archive_footer_read'] and summary['cells']==7809 and totals['arb_contained']==totals['rational_contained']==totals['rational_in_arb']==16242720 and totals['archive_H_contained']==3265568
 # Entire archive footer is read even for a diagnostic partial audit.
 needed_by_span={i:[] for i in selected}
 for key,rec in required.items():needed_by_span[owner[key[0]]].append(rec)
 fresh=0;fresh_H=0;proof_digest=hashlib.sha256();archive_footer=False;last=-1
 with gzip.open(archive,'rt') as f:
  ah=parse(next(f));assert ah['type']=='header' and ah['spans']==1558 and ah['cells']==7809 and ah['degree']==7 and ah['stream_modes']==261 and ah['hashes']['input']==TRIAL_SHA and ah['comparison_grid_sha256']==GREEN_SHA
  for line in f:
   rec=parse(line)
   if rec['type']=='complete':assert last==1557 and rec['spans']==1558 and rec['cells']==7809 and not f.read();archive_footer=True;break
   assert rec['type']=='span' and rec['span']==last+1;last+=1;part=parts[last];assert all(rec[k]==v for k,v in part.items())
   if last not in needed_by_span:continue
   ell,left,right=nonempty[last];h=right-left
   bases=[recursive_basis(knots,ell,left+h*Q(j+1,9)) for j in range(8)];assert all(sum(v,Q(0))==1 for v in bases)
   cache={}
   def values(mode):
    if mode<0 or mode>=260:return [Q(0)]*8
    if mode not in cache:
     control=[exact_hex(S[mode*1565+i]) for i in range(ell-7,ell+1)];cache[mode]=[sum((v*c for v,c in zip(row,control)),Q(0)) for row in bases]
    return cache[mode]
   for saved in needed_by_span[last]:
    cell,k,m=saved['cell'],saved['power'],saved['mode'];offset=Q(cell-part['first_cell'],part['count']);exact=newton_coefficients(values(m),9*offset-1,9/h)[k]
    assert exact==Q(saved['exact']) and Q(saved['arb_lo'])<=exact<=Q(saved['arb_hi']);fresh+=1
    proof_digest.update(json.dumps([cell,k,m,str(exact)],separators=(',',':')).encode()+b'\n')
   hw=H_required[last];j,k=hw['j'],hw['power'];target=rec['density_polynomials'][j][k];lo,hi=archive_interval(target);assert (lo,hi)==(Q(hw['target_lo']),Q(hw['target_hi']))
   def centered(mode):return newton_coefficients(values(mode),Q(7,2),9/h)[k]
   if j==0:v=centered(0)/4-centered(2)/8
   elif j==1:v=(2*centered(0)+centered(1)-centered(2)-centered(3))/8
   else:v=(centered(j-1)+centered(j)-centered(j+1)-centered(j+2))/8
   assert v==Q(hw['exact']) and lo<=v<=hi;fresh_H+=1;proof_digest.update(json.dumps(['H',last,j,k,str(v)],separators=(',',':')).encode()+b'\n')
 assert archive_footer and fresh==len(required) and fresh_H==len(selected)
 result={'utc':utc(),'status':'PASS_FULL_OUTPUT_AND_EXACT_NEWTON_AUDIT' if full else 'OPEN_PARTIAL_AUDIT_PASSED','full_run':full,'spans':len(rows),'cells':summary['cells'],'full_counts':dict(totals),'saved_endpoint_checks':saved_endpoint_checks,'fresh_exact_T_checks':fresh,'fresh_exact_H_checks':fresh_H,'newton_stream_sha256':proof_digest.hexdigest(),'archive_footer_read':archive_footer,'output_sha256':sha(path),'summary_sha256':sha(E/(args.tag+'_summary.json')),'source_sha256':sha(Path(__file__)),'producer_sha256':sha(D/'code/check_coefficients.py'),'inherited_source_pins':deps,'replay_required_spans':replay_required_spans,'resume_events_sha256':summary['resume_events_sha256'],'seconds':monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Audited execution plus exact Newton recomputation of selected and all worst records. Counts/hashes alone do not prove omitted calculations. No IPM endpoint.'}
 (E/(args.tag+'_output_audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='inherited_source_pins'},indent=2),flush=True)
if __name__=='__main__':main()

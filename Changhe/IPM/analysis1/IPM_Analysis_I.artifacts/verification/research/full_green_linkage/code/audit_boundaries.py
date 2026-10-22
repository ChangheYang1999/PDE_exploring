"""Independent coverage/artifact audit and K128 anchored Taylor spot checks.
Does not import the complete checker or its interval propagation routines.
"""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import argparse,gzip,hashlib,json,math,resource,sys
from bisect import bisect_right
from collections import Counter
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
from time import monotonic
import numpy as np
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
ctx.prec=1024;ctx.threads=1;K=128
B=Path(__file__).resolve().parents[3];D=B/'research/full_green_linkage';E=D/'evidence'
ARCHIVE_SHA='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
GREEN_SHA='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
TRIAL_SHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
PARTITION_SHA='56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2'

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def unique(pairs):
 out={}
 for k,v in pairs:assert k not in out,('duplicate JSON key',k);out[k]=v
 return out
def parse(s):return json.loads(s,object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite JSON '+x)))
def load(p):return parse(Path(p).read_text())
def aq(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def point(v):a,e=v.man_exp();return F(int(a))*F(2)**int(e)
def endpoints(v):
 assert v.is_finite();l,r=point(v.lower()),point(v.upper());assert l<=r;return l,r
def ball(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1';m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return aq(m)+arb(0,1)*aq(r)
def shifted(raw,shift,reverse):
 p=[ball(v) for v in raw];assert len(p)==8
 return [sum((p[k]*aq(F(math.comb(k,j))*shift**(k-j)*((-1)**j if reverse else 1)) for k in range(j,8)),arb(0)) for j in range(8)]
def poly(p,x):return sum((c*x**j for j,c in enumerate(p)),arb(0))
def taylor_solution(anchor,forcing,rate,u):
 assert 0<=u<F(1,50) and abs(rate*u)<F(263,25);coeff=[anchor]
 for j in range(K):coeff.append((rate*coeff[-1]+(forcing[j] if j<8 else arb(0)))/(j+1))
 value=poly(coeff,aq(u));ratio=abs(rate*u)/F(K+2);assert ratio<1
 tail=abs(coeff[K])*aq(u**K)*aq(abs(rate*u)/F(K+1))/(1-aq(ratio))
 upper=endpoints(tail)[1];assert upper>=0
 return value+arb(0,1)*aq(upper),upper

def source_provenance():
 audit=load(B/'research/middle_residual/evidence/knot_audit.json');manifest=load(B/'research/middle_residual/evidence/knot_manifest.json')
 assert audit['status']=='PASS' and audit['archive_sha256']==ARCHIVE_SHA and audit['partition_sha256']==PARTITION_SHA and audit['footer_read']
 assert audit['manifest_sha256']==sha(B/'research/middle_residual/evidence/knot_manifest.json')
 assert audit['source_sha256']==sha(B/'research/middle_residual/code/audit_knots.py')
 assert manifest['output_sha256']==ARCHIVE_SHA and manifest['output_bytes']==(B/'research/middle_residual/evidence/original_knots.jsonl.gz').stat().st_size
 dep={'source':'research/middle_residual/code/build_knot_moments.py','setup':'research/middle_residual/code/modal_setup.py','fast_moments':'research/middle_residual/code/fast_moments.py','input':'data_exact/modal_v2.json','normalization':'research/modal_repair/evidence/independent_gauss_iv.json','Cox':'research/canonical_inverse/code/exact_audit.py','ball_transport':'research/ball_transport/code/dyadic_ball.py'}
 assert {k:sha(B/v) for k,v in dep.items()}==manifest['hashes']
 old=load(B/'research/modal_green/evidence/selected_boundaries.json');oa=load(B/'research/modal_green/evidence/output_audit.json')
 assert oa['status']=='CONFIRMED selected180 Green entries' and oa['result_sha256']==sha(B/'research/modal_green/evidence/selected_boundaries.json')
 assert oa['audit_source_sha256']==sha(B/'research/modal_green/code/audit_output.py') and oa['calculation_source_sha256']==old['code_sha256']==sha(B/'research/modal_green/code/check_boundaries.py')
 assert oa['compared_artifact_sha256']==old['green_sha256']==GREEN_SHA and old['input_sha256']==TRIAL_SHA
 assert old['moments_source_sha256']==sha(B/'research/exponential_moments/code/moments.py') and old['scalar_input_sha256']==sha(B/'research/modal_repair/evidence/independent_gauss_iv.json')
 assert audit['sample_sha256']==sha(B/'research/residual_samples/evidence/sample_result.json')
 files={str(B/v):sha(B/v) for v in dep.values()}
 for v in ('research/middle_residual/evidence/knot_audit.json','research/middle_residual/evidence/knot_manifest.json','research/middle_residual/code/audit_knots.py','research/modal_green/evidence/selected_boundaries.json','research/modal_green/evidence/output_audit.json','research/modal_green/code/audit_output.py','research/modal_green/code/check_boundaries.py','research/exponential_moments/code/moments.py','research/residual_samples/evidence/sample_result.json'):files[v]=sha(B/v)
 fixtures={}
 for row in old['comparisons']:
  key=(row['boundary_index'],row['stream_index_n'],row['array']);assert key not in fixtures
  lo,hi=F(row['independent']['lower_exact']),F(row['independent']['upper_exact']);m=F.from_float(float.fromhex(row['exported_mid_hex']));r=F.from_float(float.fromhex(row['exported_rad_hex']));assert r>=0 and m-r<=lo<=hi<=m+r and row['verdict']=='CONTAINED';fixtures[key]=row
 assert len(fixtures)==180 and set(fixtures)=={(i,n,a) for i in old['selected_boundary_indices'] for n in old['mode_indices'] for a in ('A','B')}
 return manifest,fixtures,files

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full');ap.add_argument('--allow-partial',action='store_true');args=ap.parse_args();assert args.tag.replace('_','').isalnum()
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=monotonic()
 stream=E/(args.tag+'_spans.jsonl');summarypath=E/(args.tag+'_summary.json');summary=load(summarypath)
 with stream.open() as f:
  lines=f.readlines();assert lines and all(line.endswith('\n') for line in lines);records=[parse(x) for x in lines]
 header,*rows,footer=records;assert header['type']=='header' and header['schema']=='ipm-full-green-linkage-v1' and footer['type']=='complete'
 parts=load(B/'research/middle_residual/evidence/partition_exact.json');assert sha(B/'research/middle_residual/evidence/partition_exact.json')==PARTITION_SHA
 assert parts['input_sha256']==TRIAL_SHA and parts['grid_sha256']==GREEN_SHA and parts['cells']==7809;parts=parts['spans'];assert len(parts)==1558
 selected=header['selected_spans'];assert selected==sorted(set(selected)) and selected and min(selected)>=0 and max(selected)<1558
 full=selected==list(range(1558));assert header['full_run']==full and (full or args.allow_partial)
 assert summary['status']==('COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT' if full else 'OPEN_PARTIAL_DIAGNOSTIC')
 assert summary['output_sha256']==sha(stream) and summary['source_sha256']==sha(D/'code/check_boundaries.py')
 assert header['files']==summary['files'] and header['engines']=={'arb_bits':512,'iv_decimal_digits':180,'phi7_series_last_index':96}
 pins={}
 for relative,digest in header['files'].items():assert sha(B/relative)==digest,relative;pins[relative]=digest
 for p in (D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/proof_first.json',D/'evidence/addendum_first.json',D/'code/check_boundaries.py'):assert pins[str(p.relative_to(B))]==sha(p)
 assert pins['research/middle_residual/evidence/original_knots.jsonl.gz']==ARCHIVE_SHA
 green=Path(header['green_path']);assert header['green_sha256']==sha(green)==GREEN_SHA
 with np.load(green,allow_pickle=False) as g:arrays={k:g[k] for k in ('A_mid','A_rad','B_mid','B_rad','parent','tb','tb_rad')}
 for key,x in arrays.items():
  assert np.all(np.isfinite(x)),key
  if key!='parent':assert x.dtype==np.dtype('float64')
 for a in ('A','B'):assert arrays[a+'_mid'].shape==arrays[a+'_rad'].shape==(7810,261) and np.all(arrays[a+'_rad']>=0)
 assert arrays['tb'].shape==arrays['tb_rad'].shape==(7810,) and np.all(arrays['tb_rad']>=0)
 assert arrays['parent'].shape==(7809,) and np.issubdtype(arrays['parent'].dtype,np.integer)
 first=0;previous=None;coords={};owner={}
 for i,p in enumerate(parts):
  a,b=F(p['a_exact']),F(p['b_exact']);assert p['span']==i and p['first_cell']==first and p['count']>0 and 0<b-a<F(1,50)
  if previous is not None:assert previous==a
  assert all(int(z)==i for z in arrays['parent'][first:first+p['count']])
  for j in range(p['count']+(i==1557)):
   index=first+j;assert index not in coords;t=a+(b-a)*F(j,p['count']);coords[index]=t;owner[index]=i
   m=F.from_float(float(arrays['tb'][index]));r=F.from_float(float(arrays['tb_rad'][index]));assert m-r<=t<=m+r
  previous=b;first+=p['count']
 assert first==7809 and set(coords)==set(range(7810))
 manifest,fixtures,more=source_provenance();pins.update(more)
 seed=hashlib.sha256((ARCHIVE_SHA+GREEN_SHA).encode()).hexdigest();sample=set()
 for j in range(128):
  h=hashlib.sha256((seed+':'+str(j)).encode()).digest();sample.add((int.from_bytes(h[:8],'big')%7810,1+int.from_bytes(h[8:16],'big')%261))
 assert len(sample)==128 and header['sample_seed']==seed and header['sample_pairs']==sorted([list(x) for x in sample])
 expectedkeys=({(i,n,a) for i,n in sample for a in ('A','B')}|set(fixtures));expectedkeys={k for k in expectedkeys if owner[k[0]] in selected}
 seenbounds=set();saved={};saved_checks=0;oldchecks=0
 def check_entry(v,si):
  nonlocal saved_checks,oldchecks
  i,n,a=v['boundary'],v['n'],v['array'];assert i in coords and 1<=n<=261 and a in ('A','B') and owner[i]==si and F(v['t_exact'])==coords[i]
  assert v['target_mid_hex']==float(arrays[a+'_mid'][i,n-1]).hex() and v['target_rad_hex']==float(arrays[a+'_rad'][i,n-1]).hex()
  m=F.from_float(float.fromhex(v['target_mid_hex']));r=F.from_float(float.fromhex(v['target_rad_hex']));assert r>=0
  assert set(v['bounds'])=={'arb','iv'};ends={}
  for engine in ('arb','iv'):
   assert len(v['bounds'][engine])==2;l,h=map(F,v['bounds'][engine]);assert m-r<=l<=h<=m+r;ends[engine]=(l,h);saved_checks+=1
  assert max(ends['arb'][0],ends['iv'][0])<=min(ends['arb'][1],ends['iv'][1])
  if (i,n,a) in fixtures:
   old=fixtures[i,n,a];assert F(old['log_boundary_exact'])==coords[i] and old['exported_mid_hex']==v['target_mid_hex'] and old['exported_rad_hex']==v['target_rad_hex'];ol,oh=F(old['independent']['lower_exact']),F(old['independent']['upper_exact'])
   for l,h in ends.values():assert max(l,ol)<=min(h,oh);oldchecks+=1
  return (i,n,a),m-r,m+r,ends
 assert len(rows)==len(selected)==header['expected_spans']==summary['spans']
 for row,si in zip(rows,selected):
  part=parts[si];assert row['type']=='span' and all(row[k]==v for k,v in part.items())
  indices=set(range(part['first_cell'],part['first_cell']+part['count']+(si==1557)));assert not seenbounds&indices;seenbounds|=indices;nb=len(indices)
  assert row['boundaries']==nb and row['cross_engine_overlaps']==2*261*nb and row['failures']==[]
  assert set(row['counts'])==set(row['worst_raw_margins'])=={'A/arb','A/iv','B/arb','B/iv'}
  assert len(row['stream_sha256'])==64 and all(c in '0123456789abcdef' for c in row['stream_sha256'])
  for key in row['counts']:
   assert row['counts'][key]=={'CONTAINED':261*nb}
   w=row['worst_raw_margins'][key];entry,tl,th,ee=check_entry(w['entry'],si);a,engine=key.split('/');assert entry[2]==a
   assert F(w['margin_exact'])==min(ee[engine][0]-tl,th-ee[engine][1])>=0
  for v in row['selected_records']:
   key,*_=check_entry(v,si);assert key not in saved and key in expectedkeys;saved[key]=v
 assert set(saved)==expectedkeys and len(seenbounds)==header['expected_boundaries']==summary['boundaries']==footer['boundaries']
 assert footer['spans']==len(selected) and footer['stream_rows_sha256']==hashlib.sha256(''.join(r['stream_sha256'] for r in rows).encode()).hexdigest()
 assert summary['entries_per_engine']==2*261*len(seenbounds) and summary['selected_records']==len(saved)
 for key in ('A/arb','A/iv','B/arb','B/iv'):assert summary['all_counts'][key]=={'CONTAINED':261*len(seenbounds)}
 if full:assert seenbounds==set(range(7810)) and len(rows)==1558
 # Third method: independent direct ODE Taylor recurrence at K128.
 per_span={}
 for key in saved:per_span.setdefault(owner[key[0]],set()).add(key)
 fresh=[];archive_footer=False;last=-1;max_tail=F(0)
 with gzip.open(B/'research/middle_residual/evidence/original_knots.jsonl.gz','rt') as f:
  ah=parse(next(f));assert ah['type']=='header' and ah['hashes']==manifest['hashes'] and ah['degree']==7 and ah['stream_modes']==261 and ah['spans']==1558 and ah['cells']==7809 and ah['comparison_grid_sha256']==GREEN_SHA
  for line in f:
   assert line.endswith('\n');rec=parse(line)
   if rec['type']=='complete':assert last==1557 and rec['spans']==1558 and rec['cells']==7809 and not f.read();archive_footer=True;break
   last+=1;assert rec['type']=='span' and rec['span']==last and all(rec[k]==v for k,v in parts[last].items())
   if last not in per_span:continue
   a,b=F(rec['a_exact']),F(rec['b_exact']);h=b-a;mid=(a+b)/2;assert F(rec['polynomial_mid_exact'])==mid
   assert len(rec['density_polynomials'])==262 and all(len(p)==8 for p in rec['density_polynomials']) and len(rec['i_left'])==len(rec['j_right'])==261
   assert all(ball(v).is_zero() for v in rec['density_polynomials'][261])
   pairs=sorted({(i,n) for i,n,arr in per_span[last]})
   for i,n in pairs:
    t=coords[i];rawlo=rec['density_polynomials'][n-1];rawhi=rec['density_polynomials'][n]
    forward=shifted(rawlo,-h/2,False);backward=shifted(rawhi,h/2,True)
    im,ti=taylor_solution(ball(rec['i_left'][n-1]),forward,-(2*n+4),t-a)
    jm,tj=taylor_solution(ball(rec['j_right'][n-1]),backward,4-2*n,b-t);max_tail=max(max_tail,ti,tj)
    hv=(poly([ball(v) for v in rawlo],aq(t-mid))+poly([ball(v) for v in rawhi],aq(t-mid)))/2;expo=aq(4*t).exp()
    values={'A':expo*(hv-2*n*im),'B':expo*(2*n*jm-hv)}
    for arr,v in values.items():
     key=(i,n,arr)
     if key not in saved:continue
     old=saved[key];lo,hi=endpoints(v);mm=F.from_float(float(arrays[arr+'_mid'][i,n-1]));rr=F.from_float(float(arrays[arr+'_rad'][i,n-1]));assert mm-rr<=lo<=hi<=mm+rr,(key,'third method target')
     for previous in old['bounds'].values():l,r=map(F,previous);assert max(l,lo)<=min(r,hi),(key,'third method stream')
     if key in fixtures:
      f0=fixtures[key];l,r=F(f0['independent']['lower_exact']),F(f0['independent']['upper_exact']);assert max(l,lo)<=min(r,hi),(key,'third method old fixture')
     fresh.append({'boundary':i,'n':n,'array':arr,'t_exact':str(t),'lower_exact':str(lo),'upper_exact':str(hi),'verdict':'CONTAINED'})
 assert archive_footer and {(v['boundary'],v['n'],v['array']) for v in fresh}==expectedkeys and len(fresh)==len(expectedkeys)
 assert sha(green)==GREEN_SHA and sha(B/'research/middle_residual/evidence/original_knots.jsonl.gz')==ARCHIVE_SHA
 for path,digest in pins.items():assert sha(B/path)==digest,path
 out={'utc':utc(),'status':'PASS_FULL_OUTPUT_AND_SELECTED_THIRD_METHOD' if full else 'OPEN_PARTIAL_AUDIT_PASSED','full_run':full,'spans':len(rows),'boundaries':len(seenbounds),'entries_per_engine':2*261*len(seenbounds),'saved_endpoint_comparisons':saved_checks,'saved_old_fixture_overlaps':oldchecks,'fresh_third_method_entries':len(fresh),'third_method_arb_bits':1024,'third_method_taylor_degree':K,'max_third_method_tail_exact':str(max_tail),'fresh_entries':fresh,'source_sha256':sha(Path(__file__)),'complete_checker_sha256':sha(D/'code/check_boundaries.py'),'stream_sha256':sha(stream),'summary_sha256':sha(summarypath),'files':pins,'seconds':monotonic()-start,'scope':'Complete or explicitly partial A/B boundary computation audited; selected third-method checks do not replace complete execution. No T membership or full-flow result.'}
 (E/(args.tag+'_output_audit.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('files','fresh_entries','max_third_method_tail_exact')},indent=2))
if __name__=='__main__':main()

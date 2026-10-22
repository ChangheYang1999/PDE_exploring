"""Exhaustive radial TM audit. Whole candidate intervals must contain both engines."""
import os,sys,time,argparse,resource
from collections import Counter
from fractions import Fraction
from pathlib import Path
from common import *
import engine_arb as A
import engine_iv as B
import forcing
from flint import ctx

ENGINE_FUNCTIONS=(('arb512',A,arb_endpoints),('iv180_rational_exp',B,iv_endpoints))
COUNTS_PER_MODE={'coefficients':26,'remainders':2}

def ceil_endpoint_units(d):
 m,e=d;e+=1074
 return int(m)<<e if e>=0 else -((-int(m))>>(-e))
def floor_endpoint_units(d):
 m,e=d;e+=1074
 return int(m)<<e if e>=0 else int(m)>>(-e)

def witness(kind,engine,family,n,j,bounds,lo,hi):
 return {'kind':kind,'engine':engine,'family':family,'n':n,'j':j,'independent_lo':list(bounds[0]),'independent_hi':list(bounds[1]),'candidate_lo_units':str(lo),'candidate_hi_units':str(hi)}
def witness_valid(w):
 lo,hi=int(w['candidate_lo_units']),int(w['candidate_hi_units'])
 return inside((w['independent_lo'],w['independent_hi']),lo,hi)
def valid_row(row,cells,modes,index):
 assert row['type']=='cell' and row['cell']==cells[index] and row['modes']==modes and not row['failures']
 assert row['forcing']['count']==2088
 assert set(row['counts'])=={name for name,_,_ in ENGINE_FUNCTIONS}
 for name in row['counts']:assert row['counts'][name]=={'coefficients':26*len(modes),'remainders':2*len(modes)}
 assert len(row['E_witnesses'])==2 and len(row['witnesses'])==8
 for w in row['E_witnesses']+row['witnesses']:assert witness_valid(w)
 assert Fraction(row['b'])>Fraction(row['a']) and 0<Fraction(row['h'])<=Fraction(row['wide'])
 assert Fraction(row['b'])-Fraction(row['a'])<=Fraction(row['h'])
 assert set(row['array_manifest'])=={'P_mid','P_rad','P_rem','R_mid','R_rad','R_rem','F_mid','F_rad','A_mid','A_rad','B_mid','B_rad','T_mid','T_rad','scalar'}
 for v in row['array_manifest'].values():assert len(v['sha256'])==64 and v['dtype'] in ('<f8','>f8')

def process_cell(data,ci,modes):
 started=time.monotonic();c=data.cell(ci);d=c['arrays'];counts={};allwitnesses=[];failures=[];fallbacks=[]
 em,er=f64_units(d['scalar'][1]),f64_units(d['scalar'][2]);assert er>=0 and em-er>0
 E_witnesses=[]
 for name,engine,getbounds in ENGINE_FUNCTIONS:
  engine.setup()
  exp=A.rational_arb(c['a']).exp() if engine is A else B.exponential_rational(c['a'])
  bounds=getbounds(exp);assert inside(bounds,em-er,em+er),('E point not contained',ci,name)
  E_witnesses.append(witness('same_point_E',name,'E',0,0,bounds,em-er,em+er))
 forcing_check=forcing.check(d)
 assert forcing_check['count']==2088
 # Integer conversions are exact data decoding. Engines build independent hulls.
 fm=units_array(d['F_mid']);fr=units_array(d['F_rad'])
 dataints={key:[f64_units(x) for x in d[key]] for key in ('A_mid','A_rad','B_mid','B_rad','P_rem','R_rem')}
 pc={key:units_array(d[key]) for key in ('P_mid','P_rad','R_mid','R_rad')}
 for name,engine,getbounds in ENGINE_FUNCTIONS:
  engine.setup();counter=Counter();best={};bestscore={}
  for n in modes:
   m=n-1;inputs=(n,em,er,dataints['A_mid'][m],dataints['A_rad'][m],dataints['B_mid'][m],dataints['B_rad'][m],fm[m],fr[m])
   coefs=engine.coefficients(*inputs)
   for family,vals in zip(('P','R'),coefs):
    assert len(vals)==21
    for j,value in enumerate(vals[:13]):
     bounds=getbounds(value);mid,rad=pc[family+'_mid'][m][j],pc[family+'_rad'][m][j]
     assert rad>=0;lo,hi=mid-rad,mid+rad;passed=inside(bounds,lo,hi);counter['coefficients']+=1
     w=witness('coefficient',name,family,n,j,bounds,lo,hi)
     if not passed:failures.append(w)
     else:
      # Display ranking only; containment itself uses exact signed comparisons.
      gap=min(floor_endpoint_units(bounds[0])-lo,hi-ceil_endpoint_units(bounds[1]));assert gap>=0
      score=gap/max(rad,1);key='coefficient_'+family
      if key not in bestscore or score<bestscore[key]:bestscore[key]=score;best[key]=w
   width=c['wide'] if 522*c['wide']<1 else c['h']
   guard_fallback=width!=c['wide']
   rems=engine.remainder(n,width,*inputs[1:],coefs)
   rbounds=[getbounds(v) for v in rems]
   passed=[positive_upper_within(b,dataints[fam+'_rem'][m]) for fam,b in zip(('P','R'),rbounds)]
   if guard_fallback:fallbacks.append({'engine':name,'n':n,'reason':'rounded_width_guard','from':str(c['wide']),'to':str(c['h'])})
   if not all(passed) and width!=c['h']:
    attempt=[]
    for fam,b,ok in zip(('P','R'),rbounds,passed):attempt.append({'family':fam,'bounds':[list(x) for x in b],'budget_units':str(dataints[fam+'_rem'][m]),'passed':ok})
    fallbacks.append({'engine':name,'n':n,'reason':'rounded_width_sufficient_test_failed','from':str(width),'to':str(c['h']),'attempt':attempt})
    width=c['h'];rems=engine.remainder(n,width,*inputs[1:],coefs);rbounds=[getbounds(v) for v in rems]
    passed=[positive_upper_within(b,dataints[fam+'_rem'][m]) for fam,b in zip(('P','R'),rbounds)]
   for family,b,ok in zip(('P','R'),rbounds,passed):
    counter['remainders']+=1;budget=dataints[family+'_rem'][m];w=witness('remainder',name,family,n,20,b,0,budget);w['width']=str(width)
    if not ok:failures.append(w)
    else:
     gap=budget-ceil_endpoint_units(b[1]);assert gap>=0;score=gap/max(budget,1);key='remainder_'+family
     if key not in bestscore or score<bestscore[key]:bestscore[key]=score;best[key]=w
   # Do not keep computing a claim once a counterexample to its sufficient test occurs.
   if failures:break
  counts[name]=dict(counter)
  allwitnesses.extend(dict(best[k],display_relative_slack=bestscore[k]) for k in sorted(best))
  if failures:break
 return {'type':'cell','utc':utc(),'cell':ci,'parent_span':data.parents[ci],'a':str(c['a']),'b':str(c['b']),'h':str(c['h']),'wide':str(c['wide']),
 'modes':modes,'array_manifest':c['array_manifest'],'forcing':forcing_check,'E_witnesses':E_witnesses,'counts':counts,
 'witnesses':allwitnesses,'fallbacks':fallbacks,'failures':failures,'seconds':time.monotonic()-started,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}

def append(path,row):
 with Path(path).open('a') as f:f.write(canonical(row)+'\n');f.flush();os.fsync(f.fileno())

def inspect_stream(path,header,cells,modes,allow_partial=False):
 """Validate every complete record before truncating only an interrupted final line."""
 rows=[];footer=None;partial=None;hasher=hashlib.sha256();size=0
 with Path(path).open('rb') as f:
  for index,raw in enumerate(f):
   if not raw.endswith(b'\n'):
    assert allow_partial and not f.read(1),'partial line not at end';partial={'offset':size,'bytes':len(raw)};break
   item=parse(raw);size+=len(raw)
   if index==0:assert item==header,'header mismatch'
   elif item['type']=='cell':
    assert footer is None,'record after footer';valid_row(item,cells,modes,len(rows));rows.append(item)
   elif item['type']=='footer':
    assert footer is None and item['rows']==len(rows) and item['prior_stream_sha256']==hasher.hexdigest(),'footer mismatch';footer=item
    assert len(rows)==len(cells) and footer['complete'] is True
   else:raise AssertionError('unknown record')
   hasher.update(raw)
 assert size and (rows or size>0)
 return rows,footer,partial,hasher.hexdigest()

def expected_header(cells,modes,pins):
 return {'type':'header','schema':'radial-full-v1','cells':cells,'modes':modes,'degree':12,'orders':[20],
 'width_schedule':['ceil(2^40*h)/2^40','h'],'engine_precisions':{'arb_bits':512,'iv_decimal_digits':180,'iv_exp_terms':64},
 'input_pins':pins,'runtime':runtime(),'replay_seed':SEED,'base_replay_cells':replay_base(),'third_selection_stride':257,
 'third_modes':[1,2,3,64,261],'scope':'Exhaustive finite-input radial ODE boxes, conditional on separate canonical input membership.'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--cells',default='all');ap.add_argument('--modes',default='all');ap.add_argument('--resume',action='store_true');args=ap.parse_args()
 assert args.tag.replace('_','').isalnum();cells=list(range(7809)) if args.cells=='all' else [int(x) for x in args.cells.split(',')];modes=list(range(1,262)) if args.modes=='all' else [int(x) for x in args.modes.split(',')]
 assert cells==sorted(set(cells)) and cells and all(0<=x<7809 for x in cells)
 assert modes==sorted(set(modes)) and modes and all(1<=x<=261 for x in modes)
 pins=current_pins();header=expected_header(cells,modes,pins);path=OUT/(args.tag+'_rows.jsonl');restart_path=OUT/(args.tag+'_restarts.jsonl');start=time.monotonic()
 if path.exists():
  assert args.resume,'output exists without --resume';rows,footer,partial,_=inspect_stream(path,header,cells,modes,True)
  if footer:
   assert not partial;print(canonical({'utc':utc(),'status':'ALREADY_COMPLETE_REQUIRES_OUTPUT_AUDIT','rows':len(rows)}));return
  if partial:
   with path.open('r+b') as f:f.truncate(partial['offset']);f.flush();os.fsync(f.fileno())
  event={'utc':utc(),'completed':len(rows),'last_completed':cells[len(rows)-1] if rows else None,'first_uncompleted':cells[len(rows)] if len(rows)<len(cells) else None,'actual_interruption':bool(rows) or bool(partial),'partial_tail_removed':partial}
  append(restart_path,event)
 else:
  rows=[];append(path,header)
  if args.resume:append(restart_path,{'utc':utc(),'completed':0,'actual_interruption':False,'last_completed':None,'first_uncompleted':cells[0],'partial_tail_removed':None})
 data=Data();total=Counter()
 for row in rows:
  for name,vals in row['counts'].items():
   for k,v in vals.items():total[name+'_'+k]+=v
  total['forcing']+=row['forcing']['count']
 for ci in cells[len(rows):]:
  row=process_cell(data,ci,modes)
  if row['failures']:
   failure={'utc':utc(),'status':'OPEN_SUFFICIENT_TEST_FAILED','tag':args.tag,'failed_cell':row,'complete':False}
   (OUT/(args.tag+'_failure.json')).write_text(canonical(failure)+'\n');print(canonical({'utc':utc(),'status':failure['status'],'cell':ci}),flush=True);raise SystemExit(2)
  valid_row(row,cells,modes,len(rows));append(path,row);rows.append(row)
  for name,vals in row['counts'].items():
   for k,v in vals.items():total[name+'_'+k]+=v
  total['forcing']+=row['forcing']['count']
  if len(rows)%10==0 or len(rows)==len(cells):print(canonical({'utc':utc(),'cell':ci,'completed':len(rows),'total':len(cells),'seconds_last':row['seconds'],'fallbacks':len(row['fallbacks']),'maxrss_kib':row['maxrss_kib']}),flush=True)
  assert row['maxrss_kib']<16*1024**2
 assert current_pins()==pins,'sources changed during calculation'
 footer={'type':'footer','utc':utc(),'complete':True,'rows':len(rows),'counts':dict(total),'prior_stream_sha256':sha(path),'source_footer_read':True}
 append(path,footer)
 result={'utc':utc(),'status':'COMPUTED_REQUIRES_SEPARATE_OUTPUT_AUDIT','complete':True,'cells_complete':len(rows),'cells':cells,'modes':modes,'counts':dict(total),'rows_sha256':sha(path),'source_footer_read':True,'input_pins':pins,'seconds_this_invocation':time.monotonic()-start,'scope':header['scope']}
 (OUT/(args.tag+'_summary.json')).write_text(canonical(result)+'\n');print(canonical({k:result[k] for k in ('utc','status','cells_complete','counts','seconds_this_invocation')}),flush=True)
if __name__=='__main__':main()

"""Independent artifact validation and fresh finite-particular calculation."""
import os,argparse,time
from collections import Counter
from common import *
import engine_particular as C

def required_replay(header,events):
 cells=set(header['cells']);required=set(header['base_replay_cells'])&cells
 for event in events:
  assert isinstance(event['completed'],int) and 0<=event['completed']<=len(cells)
  if event['actual_interruption']:
   for key in ('last_completed','first_uncompleted'):
    v=event[key]
    if v is not None:
     assert v in cells;required.add(v)
 return sorted(required)

def target_interval(arrays,w):
 n=w['n'];family=w['family'];kind=w['kind']
 if kind=='same_point_E':
  assert n==0 and family=='E' and w['j']==0
  m,r=map(f64_units,arrays['scalar'][1:3]);return m-r,m+r
 assert 1<=n<=261 and family in ('P','R')
 if kind=='coefficient':
  j=w['j'];assert 0<=j<=12;m=f64_units(arrays[family+'_mid'][n-1,j]);r=f64_units(arrays[family+'_rad'][n-1,j]);return m-r,m+r
 assert kind=='remainder' and w['j']==20
 return 0,f64_units(arrays[family+'_rem'][n-1])

def audit(tag,allow_partial=False):
 start=time.monotonic();path=OUT/(tag+'_rows.jsonl');summary=load(OUT/(tag+'_summary.json'));counts=Counter();witnesses=[];rows=[];footer=None;header=None;hasher=hashlib.sha256()
 assert summary['status']=='COMPUTED_REQUIRES_SEPARATE_OUTPUT_AUDIT' and summary['complete'] and summary['source_footer_read']
 assert sha(path)==summary['rows_sha256']
 for v in summary['input_pins'].values():assert sha(v['path'])==v['sha256'];counts['current_source_pins']+=1
 assert current_pins()==summary['input_pins']
 with path.open('rb') as f:
  for raw in f:
   assert raw.endswith(b'\n'),'incomplete output line';r=parse(raw)
   if header is None:
    assert r['type']=='header' and r['schema']=='radial-full-v1';header=r
    assert r['input_pins']==summary['input_pins'] and r['runtime']==runtime()
    assert r['degree']==12 and r['orders']==[20] and r['engine_precisions']=={'arb_bits':512,'iv_decimal_digits':180,'iv_exp_terms':64}
    assert r['width_schedule']==['ceil(2^40*h)/2^40','h'] and r['replay_seed']==SEED and r['base_replay_cells']==replay_base()
    assert r['third_selection_stride']==257 and r['third_modes']==[1,2,3,64,261]
    assert header['cells']==summary['cells'] and header['modes']==summary['modes']
    if not allow_partial:assert header['cells']==list(range(7809)) and header['modes']==list(range(1,262))
   elif r['type']=='cell':
    assert footer is None and len(rows)<len(header['cells'])
    assert r['cell']==header['cells'][len(rows)] and r['modes']==header['modes'] and not r['failures']
    assert r['counts']=={name:{'coefficients':26*len(header['modes']),'remainders':2*len(header['modes'])} for name in ('arb512','iv180_rational_exp')}
    assert r['forcing']['count']==2088 and len(r['witnesses'])==8 and len(r['E_witnesses'])==2
    assert Fraction(r['b'])>Fraction(r['a']) and 0<Fraction(r['b'])-Fraction(r['a'])<=Fraction(r['h'])<=Fraction(r['wide'])
    assert 522*Fraction(r['h'])<1
    for engine,c in r['counts'].items():
     for k,v in c.items():counts[engine+'_'+k]+=v
    counts['forcing']+=2088;rows.append(r)
   else:
    assert r['type']=='footer' and footer is None and r['complete'] and r['source_footer_read']
    assert len(rows)==len(header['cells'])==r['rows']==summary['cells_complete'] and r['prior_stream_sha256']==hasher.hexdigest()
    assert r['counts']==summary['counts']=={k:counts[k] for k in summary['counts']}
    footer=r
   hasher.update(raw)
 assert header is not None and footer is not None and len(rows)==len(header['cells'])
 eventpath=OUT/(tag+'_restarts.jsonl');events=[]
 if eventpath.exists():events=[parse(x) for x in eventpath.read_text().splitlines()]
 required=required_replay(header,events);data=Data();freshrows=[]
 freshpath=OUT/(tag+'_fresh_audit.jsonl');assert not freshpath.exists(),'fresh audit output already exists; use a new tag or explicitly archive an interrupted audit'
 with freshpath.open('w') as output:
  for row_index,row in enumerate(rows):
   ci=row['cell'];c=data.cell(ci);d=c['arrays'];assert c['array_manifest']==row['array_manifest'],('candidate regeneration differs',ci)
   assert c['a']==Fraction(row['a']) and c['b']==Fraction(row['b']) and c['h']==Fraction(row['h']) and c['wide']==Fraction(row['wide']) and data.parents[ci]==row['parent_span']
   counts['candidate_arrays_regenerated']+=len(c['array_manifest'])
   assert {w['engine'] for w in row['E_witnesses']}=={'arb512','iv180_rational_exp'}
   expected={(engine,kind,fam) for engine in ('arb512','iv180_rational_exp') for kind in ('coefficient','remainder') for fam in ('P','R')};seen=set()
   for w in row['E_witnesses']+row['witnesses']:
    lo,hi=target_interval(d,w);assert (int(w['candidate_lo_units']),int(w['candidate_hi_units']))==(lo,hi)
    assert inside((w['independent_lo'],w['independent_hi']),lo,hi),('bad saved witness',ci,w)
    if w['kind']!='same_point_E':
     key=w['engine'],w['kind'],w['family'];assert key not in seen and key in expected;seen.add(key)
     if w['kind']=='remainder':assert Fraction(w['width']) in (c['h'],c['wide']) and c['h']<=Fraction(w['width']) and 522*Fraction(w['width'])<1
    counts['saved_exact_witnesses']+=1
   assert seen==expected
   # The saved sparse forcing image is compared by exact rationals, independently of the integer comparison routine.
   fw=row['forcing']['worst'];assert int(fw['margin_units_over16'])>=0
   n,k=fw['n'],fw['k'];m=Fraction(float(d['F_mid'][n-1,k]));r=Fraction(float(d['F_rad'][n-1,k]));scale=Fraction(1,16*(1<<1074))
   assert m-r<=int(fw['image_lo_units_over16'])*scale<=int(fw['image_hi_units_over16'])*scale<=m+r
   for attempt in row['fallbacks']:
    assert attempt['engine'] in ('arb512','iv180_rational_exp') and attempt['n'] in header['modes']
    assert Fraction(attempt['from'])==c['wide'] and Fraction(attempt['to'])==c['h']
    if attempt['reason']=='rounded_width_guard':assert 522*c['wide']>=1
    else:
     assert attempt['reason']=='rounded_width_sufficient_test_failed' and len(attempt['attempt'])==2
     outcomes=[]
     for test in attempt['attempt']:
      budget=f64_units(d[test['family']+'_rem'][attempt['n']-1]);assert int(test['budget_units'])==budget
      value=positive_upper_within(test['bounds'],budget);assert value==test['passed'];outcomes.append(value)
     assert not all(outcomes)
    counts['fallback_events']+=1
   selected={w['n'] for w in row['witnesses']}
   if ci in required or ci%257==0:selected.update(header['third_modes'])
   selected.intersection_update(header['modes'])
   assert selected
   records=[]
   for n in sorted(selected):
    coefs,rems=C.compute(d,n)
    for fam,seq,rem in zip(('P','R'),coefs,rems):
     for j,value in enumerate(seq[:13]):
      mid=f64_units(d[fam+'_mid'][n-1,j]);rad=f64_units(d[fam+'_rad'][n-1,j]);assert inside(arb_endpoints(value),mid-rad,mid+rad),('fresh coefficient',ci,n,fam,j)
      counts['fresh_particular_coefficients']+=1
     endpoints=arb_endpoints(rem);budget=f64_units(d[fam+'_rem'][n-1]);assert positive_upper_within(endpoints,budget),('fresh remainder',ci,n,fam)
     counts['fresh_particular_remainders']+=1
     records.append({'n':n,'family':fam,'lower':list(endpoints[0]),'upper':list(endpoints[1]),'budget_units':str(budget)})
   fresh={'cell':ci,'modes':sorted(selected),'records':records};output.write(canonical(fresh)+'\n');output.flush()
   if (row_index+1)%50==0:print(canonical({'utc':utc(),'stage':'output_audit','cell':ci,'fresh_mode_count':len(selected)}),flush=True)
  os.fsync(output.fileno())
 assert current_pins()==summary['input_pins'] and sha(path)==summary['rows_sha256']
 result={'utc':utc(),'status':'PASS_OUTPUT_AND_FRESH_PARTICULAR_AUDIT','cells_audited':len(rows),'full_middle':header['cells']==list(range(7809)) and header['modes']==list(range(1,262)),
 'counts':dict(counts),'replay_required_cells':required,'replay_seed':SEED,'fresh_arb_bits':1536,'fresh_order':22,'fresh_records_sha256':sha(freshpath),
 'input_summary_sha256':sha(OUT/(tag+'_summary.json')),'rows_sha256':sha(path),'restart_events_sha256':sha(eventpath) if eventpath.exists() else None,'source_footer_read':True,
 'source_pins':current_pins(),'seconds':time.monotonic()-start,'scope':'Artifact and supplemental particular audit; full two-method coverage is supplied by the checked producer stream, not by this selected calculation.'}
 (OUT/(tag+'_output_audit.json')).write_text(canonical(result)+'\n');print(canonical({k:result[k] for k in ('utc','status','cells_audited','full_middle','counts','seconds')}),flush=True)
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--allow-partial',action='store_true');args=ap.parse_args();audit(args.tag,args.allow_partial)

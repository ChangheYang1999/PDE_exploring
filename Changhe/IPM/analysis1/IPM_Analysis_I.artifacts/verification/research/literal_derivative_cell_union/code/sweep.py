"""Independent manual IEEE754 importer and integer endpoint-event sweep."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import json,hashlib,struct,time
B=Path(__file__).resolve().parents[3];D=B/'research/literal_derivative_cell_union';S=B/'research/weighted_derivative_scalar_norms'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def decode(v):
 need(type(v) is float,'literal binary64');bits=int.from_bytes(struct.pack('>d',v),'big');sign=-1 if bits>>63 else 1;e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e<2047,'finite data')
 return sign*((1<<52)+m if e else m),(e-1075 if e else -1074)
def ratio(n,p):return F(n,1<<p)
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();primary=json.loads((D/'evidence/merge.json').read_text());pins=dict(primary['files'])
for n,h in pins.items():need(sha(B/n)==h,'frozen first-engine inputs')
raw={};checks=0
for reg in ['outer','middle','inner']:
 raw[reg]=[]
 for j,r in enumerate(json.loads((S/'sources'/('derivative_'+reg+'.json')).read_text())['rows']):
  need(type(r['ci']) is int and r['ci']==j,'fresh actual row order');raw[reg].append((decode(r['t_a']),decode(r['h'])));checks+=2
power=max(-exp for rr in raw.values() for row in rr for man,exp in row);need(power>=0,'integer grid exponent');regions={};audit={}
for reg in ['inner','middle','outer']:regions[reg]=[(a*(1<<(ea+power)),a*(1<<(ea+power))+h*(1<<(eh+power))) for (a,ea),(h,eh) in raw[reg]]
regions['all']=sum((regions[n] for n in ['inner','middle','outer']),[])
for name,rows in regions.items():
 need(all(a<b for a,b in rows),'positive exact widths');ev=Counter()
 for a,b in rows:ev[a]+=1;ev[b]-=1
 coords=sorted(ev);count=0;gaps=[];multiplicity=0
 for a,b in zip(coords,coords[1:]):
  count+=ev[a];need(0<=count<=len(rows),'cover count invariant');multiplicity=max(multiplicity,count)
  if count==0:gaps.append([str(ratio(a,power)),str(ratio(b,power))])
 count+=ev[coords[-1]];need(count==0,'final cover count zero');r=primary['regions'][name];need(r['gaps']==gaps and r['gap_count']==len(gaps) and r['union_components']==len(gaps)+1,'all exact open components');need(r['intervals']==len(rows) and r['hull']==[str(ratio(coords[0],power)),str(ratio(coords[-1],power))],'full count and hull');missing=sum((F(b)-F(a) for a,b in gaps),F(0));need(F(r['missing_log_length'])==missing and F(r['max_gap'])==max([F(0)]+[F(b)-F(a) for a,b in gaps]),'exact gap measures');need(r['strictly_increasing_starts']==all(l[0]<rr[0] for l,rr in zip(rows,rows[1:])) is True,'independent starts monotone');need(r['strictly_increasing_ends']==all(l[1]<rr[1] for l,rr in zip(rows,rows[1:])) is True,'independent ends monotone')
 # Recover all union components independently as complement of the exact sweep gaps.
 starts=[F(r['hull'][0])]+[F(b) for a,b in gaps];ends=[F(a) for a,b in gaps]+[F(r['hull'][1])];need(r['components']==[[str(a),str(b)] for a,b in zip(starts,ends,strict=True)],'every union component')
 audit[name]={'intervals':len(rows),'distinct_endpoint_events':len(coords),'max_interior_multiplicity':multiplicity,'gap_count':len(gaps),'union_components':len(gaps)+1,'missing_log_length':str(missing),'max_gap':r['max_gap'],'missing_log_length_display':float(missing),'max_gap_display':float(F(r['max_gap']))}
need(checks==38778 and audit['all']['intervals']==19389,'all manual data conversions');need(audit['all']['gap_count']==sum(audit[n]['gap_count'] for n in ['inner','middle','outer']),'cross-region joins do not create or erase gap components')
for p in [Path(__file__),D/'evidence/merge.json',D/'evidence/merge.log']:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'unchanged independent inputs')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_INTEGER_EVENT_SWEEP_AND_ALL_EXACT_GAPS','manual_ieee_source_checks':checks,'common_grid_denominator_power':power,'regions':audit,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Finite literal source geometry only. No physical derivative bounds, certification that another producer interval has gaps, tail or norm contribution on gaps.'}
with (D/'evidence/sweep.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))

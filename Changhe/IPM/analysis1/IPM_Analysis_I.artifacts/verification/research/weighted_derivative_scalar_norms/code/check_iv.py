"""Fresh IEEE754 importer and unsimplified-weight interval calculation versus all Arb cell terms."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,gzip,hashlib,struct,ast,math,time
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/weighted_derivative_scalar_norms';iv.dps=110

def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def binary(x):
 need(type(x) is float,'literal binary64 scalar');bits=struct.unpack('>Q',struct.pack('>d',x))[0];s=bits>>63;e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e!=2047,'finite literal')
 if e==0:return (-1)**s*F(m)*F(2)**(-1074)
 return (-1)**s*F((1<<52)+m)*F(2)**(e-1075)
def ii(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ep(v):
 s,m,e,b=v;need(b>=0,'finite iv endpoint');return (-1)**s*F(m)*F(2)**e
def box(v):return list(map(ep,v._mpi_))
def overlap(a,b):need(max(a[0],b[0])<=min(a[1],b[1]),'independent interval overlap')
def ss(v):return [str(y) for y in v]
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();primary=load(D/'evidence/arb.json');par=load(D/'data_exact/parameters.json');pins=dict(primary['files'])
for n,h in pins.items():need(sha(B/n)==h,'actual primary pinned source')
params={}
for node in ast.parse((D/'sources/xnorm_cert.py').read_text()).body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ['k','L']:
  params[node.targets[0].id]=binary(ast.literal_eval(node.value))
need({n:str(v) for n,v in params.items()}==primary['parameters_exact'],'actual source parameter bytes');k=ii(params['k']);L=ii(params['L']);names=['inner','middle','outer','middle_rlt2','middle_lobe'];acc={n:[iv.mpf(0),iv.mpf(0)] for n in names};counts={n:0 for n in names};geo={};joins=[];previous=None;previous_a=None;oldreg=None;inputchecks=0;percell=0;groupchecks=0
with gzip.open(D/'data_exact/rows.jsonl.gz','rt') as exact,gzip.open(D/'evidence/cell_terms_arb.jsonl.gz','rt') as terms:
 for reg in ['inner','middle','outer']:
  rows=load(D/'sources'/('derivative_'+reg+'.json'))['rows'];gaps=[];first=None;last=None
  for j,row in enumerate(rows):
   need(type(row['ci']) is int and row['ci']==j,'fresh row identifier');rec=json.loads(next(exact));p=json.loads(next(terms));need(rec['region']==p['region']==reg and rec['index']==p['index']==j,'complete matched streams');x={n:binary(row[n]) for n in par['fields']};need({n:str(z) for n,z in x.items()}==rec['exact'],'manual IEEE versus imported exact rational');inputchecks+=len(x);a=x['t_a'];h=x['h'];end=a+h;need(h>0,'positive width');need(previous_a is None or a>previous_a,'strictly increasing literal cell starts');previous_a=a
   if first is None:first=a
   if previous is not None:
    gap=a-previous
    if oldreg==reg:gaps.append(gap)
    else:joins.append({'left_region':oldreg,'right_region':reg,'exact_gap':str(gap)})
   previous=end;oldreg=reg;last=end
   r=iv.exp(ii(a));u=r/L;m=u**3*(1+u*u)**((k-3)/2);w=m**(-2)*(1+u*u)**(-iv.mpf(3)/2);v=iv.exp(2*ii(a))*w;W=[ii(x[n]) for n in par['fields'][2:]];w00,w10,w20,w01,w11=W;A=sum((y*y for y in [w00,w10,w01]),iv.mpf(0));G=sum((y*y for y in [w00+w10,w10+w20,w01+w11]),iv.mpf(0));vals=[iv.pi*ii(h)*v*y for y in [A,G]]
   group=[reg];counts[reg]+=1
   if reg=='middle':
    rb=box(r);re=box(iv.exp(ii(end)));need(rb[1]<2 or rb[0]>2,'strict radius2');need(rb[1]<16 or rb[0]>16,'strict radius16');need(re[1]<4 or re[0]>4,'strict radius4')
    if rb[1]<2:group.append('middle_rlt2');counts['middle_rlt2']+=1
    if rb[1]<16 and re[0]>4:group.append('middle_lobe');counts['middle_lobe']+=1
   need(group==p['groups'],'independent physical-region selection');groupchecks+=1
   for z,ab in zip(vals,p['terms'],strict=True):overlap(box(z),list(map(F,ab)));percell+=1
   for n in group:
    for l,z in enumerate(vals):acc[n][l]+=z
  geo[reg]={'adjacencies':len(gaps),'positive_gaps':sum(x>0 for x in gaps),'overlaps':sum(x<0 for x in gaps),'exact_joins':sum(x==0 for x in gaps),'max_gap':str(max([F(0)]+gaps)),'min_gap':str(min([F(0)]+gaps)),'total_positive_gap':str(sum((x for x in gaps if x>0),F(0))),'first_t_exact':str(first),'last_t_exact':str(last),'first_radius_iv':ss(box(iv.exp(ii(first)))),'last_radius_iv':ss(box(iv.exp(ii(last))))}
  pg=primary['literal_interval_geometry'][reg]
  for n,z in geo[reg].items():
   if n.endswith('_iv'):overlap(list(map(F,z)),list(map(F,pg[n[:-3]+'_arb'])))
   else:need(pg[n]==z,'independent complete literal geometry')
 need(next(exact,None) is None and next(terms,None) is None,'complete streams, no missing or extra records')
need(inputchecks==135723 and percell==38778 and groupchecks==19389 and joins==primary['cross_region_joins'],'all audit counts and cross-region joins');acc['total']=[sum((acc[n][j] for n in ['outer','middle','inner']),iv.mpf(0)) for j in range(2)];counts['total']=19389
saved=load(D/'sources/xnorm_cert.json');mapping={'middle_rlt2':'r<2','middle_lobe':'4<=r<=16','middle':'middle region 0.00765<=r<=3413','outer':'outer','inner':'inner','total':'total'};roots={};comparisons=[];aggregatechecks=0
for n,vals in acc.items():
 need(counts[n]==primary['groups'][n]['cells'],'aggregate group count');roots[n]=[]
 for j,v in enumerate(vals):
  rb=box(iv.sqrt(v));overlap(rb,list(map(F,primary['groups'][n]['norm_majorants_arb'][j])));overlap(box(v),list(map(F,primary['groups'][n]['squared_norm_majorants_arb'][j])));aggregatechecks+=2;roots[n].append(ss(rb));q=binary(saved[mapping[n]][['eps_X_upper','eps_minus_dteps_X_upper'][j]]);need(rb[1]<q,'saved inflated binary64 exceeds rigorous exact scalar sum');comparisons.append({'group':n,'column':j,'saved_exact':str(q),'saved_minus_scalar_lower_bound':str(q-rb[1]),'saved_minus_scalar_upper_bound':str(q-rb[0])})
ceilings={'inner':['0.000000886954','0.0000389562'],'middle':['0.385651','585.873'],'outer':['0.00168303','0.00380058'],'middle_rlt2':['0.00142514','0.0339214'],'middle_lobe':['0.385195','585.864'],'total':['0.385655','585.873']}
for n,row in ceilings.items():
 for j,s in enumerate(row):need(F(s)>F(roots[n][j][1]),'exact strict outward display ceiling')
printed=[]
for n,row in {'middle':['0.38565','585.87'],'total':['0.38565','585.87']}.items():
 for j,s in enumerate(row):need(F(s)<F(roots[n][j][0]),'printed bound below exact scalar majorant');printed.append({'group':n,'column':j,'printed_exact':str(F(s)),'verdict':'INWARD_OF_EXACT_SAVED_MAJORANT_NOT_A_PHYSICAL_LOWER_BOUND'})
for p in [Path(__file__),D/'evidence/arb.json',D/'evidence/arb.log']:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'unchanged audit input')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_SAVED_SCALAR_NORMS_GEOMETRY_AND_ROUNDING_ONLY','iv_dps':iv.dps,'manual_ieee_scalar_checks':inputchecks,'cell_interval_overlaps':percell,'region_selection_checks':groupchecks,'aggregate_interval_overlaps':aggregatechecks,'norm_majorants_iv':roots,'strict_scalar_ceilings':ceilings,'saved_inflated_values_checked':comparisons,'inward_printed_bounds':printed,'literal_interval_geometry':geo,'cross_region_joins':joins,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Exact scalar sums and literal interval geometry only; no physical derivative validation, gap coverage or infinite tails. Numeric global inverse lower bound remains unproved.'}
with (D/'evidence/independent.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'seconds':out['seconds'],'manual_ieee_scalar_checks':inputchecks,'cell_interval_overlaps':percell,'ceilings':ceilings,'inward_printed_bounds':printed},indent=2))

"""Arb evaluation of the exact saved finite-cell majorant sums; no physical input validation."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,gzip,hashlib,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[3];D=B/'research/weighted_derivative_scalar_norms';ctx.prec=320

def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def aa(x):return arb(x.numerator)/arb(x.denominator)
def box(v):
 need(v.is_finite(),'finite Arb result');return [str(v.lower().fmpq()),str(v.upper().fmpq())]
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();manifest=load(D/'data_exact/manifest.json');par=load(D/'data_exact/parameters.json');pins={n:v['sha256'] for n,v in manifest['inputs'].items()}
for n,h in pins.items():need(sha(B/n)==h,'captured source pin')
need(sha(D/'data_exact/rows.jsonl.gz')==par['rowfile_sha256'],'exact row archive');kq=F(par['params']['k']['exact']);Lq=F(par['params']['L']['exact']);need(0<kq<1 and Lq>0,'parameters');k=aa(kq);L=aa(Lq)
names=['inner','middle','outer','middle_rlt2','middle_lobe'];sums={n:[arb(0),arb(0)] for n in names};counts={n:0 for n in names};geometry={};first={};last={};allrows=0;coeff_checks=0;joins=[];lastreg=None;previous=None
with gzip.open(D/'data_exact/rows.jsonl.gz','rt') as f,gzip.open(D/'evidence/cell_terms_arb.jsonl.gz','xt') as out:
 for line in f:
  rec=json.loads(line);reg=rec['region'];index=rec['index'];x={n:F(v) for n,v in rec['exact'].items()};a=x['t_a'];h=x['h'];end=a+h;need(h>0 and all(x[n]>=0 for n in par['fields'][2:]),'positive width and nonnegative W');need(index==counts[reg],'complete source order');counts[reg]+=1
  if reg not in geometry:geometry[reg]={'adjacencies':0,'positive_gaps':0,'overlaps':0,'exact_joins':0,'max_gap':F(0),'min_gap':F(0),'total_positive_gap':F(0)};first[reg]=a
  if previous is not None:
   gap=a-previous
   if reg==lastreg:
    z=geometry[reg];z['adjacencies']+=1;z['positive_gaps']+=int(gap>0);z['overlaps']+=int(gap<0);z['exact_joins']+=int(gap==0);z['max_gap']=max(z['max_gap'],gap);z['min_gap']=min(z['min_gap'],gap);z['total_positive_gap']+=max(gap,0)
   else:joins.append({'left_region':lastreg,'right_region':reg,'exact_gap':str(gap)})
  previous=end;lastreg=reg;last[reg]=end
  r=aa(a).exp();u=r/L;v=L*L*u**(-4)*(1+u*u)**(arb(3)/2-k);w00,w10,w20,w01,w11=(x[n] for n in par['fields'][2:]);A=w00*w00+w10*w10+w01*w01;G=(w00+w10)**2+(w10+w20)**2+(w01+w11)**2;coeff_checks+=5;terms=[arb.pi()*aa(h)*v*aa(z) for z in [A,G]]
  group=[reg]
  if reg=='middle':
   re=aa(end).exp();need(r<2 or r>2,'strict r=2 classification');need(r<16 or r>16,'strict r=16 classification');need(re<4 or re>4,'strict r=4 classification')
   if r<2:group.append('middle_rlt2');counts['middle_rlt2']+=1
   if r<16 and re>4:group.append('middle_lobe');counts['middle_lobe']+=1
  for n in group:
   for j,t in enumerate(terms):sums[n][j]+=t
  out.write(json.dumps({'region':reg,'index':index,'groups':group,'terms':[box(y) for y in terms]},separators=(',',':'))+'\n');allrows+=1
need(allrows==19389 and coeff_checks==96945 and [counts[n] for n in ['inner','middle','outer']]==[2632,7809,8948],'complete all rows');sums['total']=[sum((sums[n][j] for n in ['inner','middle','outer']),arb(0)) for j in range(2)];counts['total']=allrows
for reg,z in geometry.items():
 for key in ['max_gap','min_gap','total_positive_gap']:z[key]=str(z[key])
 z['first_t_exact']=str(first[reg]);z['last_t_exact']=str(last[reg]);z['first_radius_arb']=box(aa(first[reg]).exp());z['last_radius_arb']=box(aa(last[reg]).exp())
outputs={n:{'cells':counts[n],'squared_norm_majorants_arb':[box(y) for y in row],'norm_majorants_arb':[box(y.sqrt()) for y in row],'display':[float(y.sqrt()) for y in row]} for n,row in sums.items()}
for p in [Path(__file__),D/'PROOF.md',D/'data_exact/manifest.json',D/'data_exact/parameters.json',D/'data_exact/rows.jsonl.gz',D/'evidence/cell_terms_arb.jsonl.gz']:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'unchanged final pin')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARB_FINITE_SAVED_CELL_MAJORANT_SUMS_ONLY','rows':allrows,'scalar_coefficients':coeff_checks,'per_cell_energy_enclosures':2*allrows,'arb_bits':ctx.prec,'parameters_exact':{'k':str(kq),'L':str(Lq)},'groups':outputs,'literal_interval_geometry':geometry,'cross_region_joins':joins,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Exact saved scalar functional enclosures for the union of literal row intervals. Physical W validity, coverage of literal gaps, both omitted infinite tails, certified K numerator and global inverse remain OPEN.'}
with (D/'evidence/arb.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'rows':allrows,'seconds':out['seconds'],'groups':{n:x['display'] for n,x in outputs.items()},'gaps':{n:v['positive_gaps'] for n,v in geometry.items()},'cross_region_joins':joins},indent=2))

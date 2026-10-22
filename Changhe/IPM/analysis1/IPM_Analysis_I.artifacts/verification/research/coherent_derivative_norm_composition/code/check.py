"""Bind accepted finite sums to coherent rows; no physical majorant claim."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,gzip,hashlib,time
from flint import arb,fmpq,ctx
B=Path(__file__).resolve().parents[3];D=B/'research/coherent_derivative_norm_composition';W=B/'research/weighted_derivative_scalar_norms';G=B/'research/derivative_intended_partition';ctx.prec=320;ctx.threads=1

def need(x,m):
 if not x:raise ValueError(m)
def load(p):return json.loads(p.read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aq(x):return arb(fmpq(x.numerator,x.denominator))
def endpoint(x):return str(F(str(x.fmpq())))
def write(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();pins={};up={}
for folder,status in [(W,'CONFIRMED_CONDITIONAL_WEIGHTED_NORM_IDENTITIES_AND_EXACT_SAVED_SCALAR_AUDIT_ONLY'),(G,'CONFIRMED_COHERENT_DERIVATIVE_PARTITION_AND_CONDITIONAL_WEIGHT_THEOREM')]:
 v=load(folder/'evidence/verdict.json');need(v['status']==status and v['rows']==19389,'accepted scope')
 for n,h in v['files'].items():
  need(sha(B/n)==h,'accepted input '+n);need(n not in pins or pins[n]==h,'compatible accepted inputs');pins[n]=h
 n=str((folder/'evidence/verdict.json').relative_to(B));pins[n]=sha(B/n);up[folder.name]={'utc':v['utc'],'sha256':pins[n]}
par=load(W/'data_exact/parameters.json');geo=load(G/'data_exact/geometry.json');need(par['params']==geo['params'],'same exact k,L');fields=par['fields'];need(fields==['t_a','h','W_0_0','W_1_0','W_2_0','W_0_1','W_1_1'],'same seven scalars')
rows={r:load(W/'sources'/('derivative_'+r+'.json'))['rows'] for r in ['inner','middle','outer']};counter={r:0 for r in rows};checks=0;count=0;delta=F(0);prior=None
with gzip.open(W/'data_exact/rows.jsonl.gz','rt') as f:
 for line,g in zip(f,geo['rows'],strict=True):
  z=json.loads(line);r=z['region'];ci=z['index'];need(ci==counter[r] and (g['region'],g['ci'])==(r,ci),'one-to-one row order');row=rows[r][ci];need(row['ci']==ci and geo['regions'][r]['source_rows']==str((W/'sources'/('derivative_'+r+'.json')).relative_to(B)),'same row source')
  x={n:F(z['exact'][n]) for n in fields}
  for n in fields:need(x[n]==F.from_float(float(row[n])),'exact imported row');checks+=1
  a,b=F(g['a']),F(g['b']);need(prior is None or prior==a,'coherent join');need(0<b-a<=x['h'] and x['h']-(b-a)==F(g['h_slack']) and a-x['t_a']==F(g['offset']),'same coherent width/start');prior=b;delta=max(delta,abs(a-x['t_a']));counter[r]+=1;count+=1
need(count==19389 and checks==135723 and counter=={'inner':2632,'middle':7809,'outer':8948},'complete counts');need(delta==F(1677,629659522901737472),'exact displacement');need(F(geo['rows'][0]['a'])==F(-1389482001461413,140737488355328) and prior==F(7074968463789829,281474976710656),'exact annulus')
a=load(W/'evidence/arb.json');iv=load(W/'evidence/independent.json');old=list(map(F,iv['strict_scalar_ceilings']['total']));new=[F('0.385656'),F('585.874')];need(old==[F('0.385655'),F('585.873')],'accepted ceilings');x=4*delta;need(0<x<1,'geometric majorant');rat=1/(1-x);results=[]
for j,(c,d) in enumerate(zip(old,new)):
 for pair in [a['groups']['total']['norm_majorants_arb'][j],iv['norm_majorants_iv']['total'][j]]:need(0<=F(pair[0])<=F(pair[1])<c,'accepted root upper below old ceiling')
 slack=d*d-c*c*rat;need(slack>0,'strict rational corrected ceiling');v=(2*aq(delta)).exp()*aq(c);lo,hi=F(endpoint(v.lower())),F(endpoint(v.upper()));need(0<lo<=hi<d,'directed Arb corrected ceiling');results.append({'old_ceiling':str(c),'new_ceiling':str(d),'exact_squared_slack':str(slack),'corrected_old_ceiling_arb':[str(lo),str(hi)],'display':str(v)})
for p in [Path(__file__),D/'PROOF.md',D/'evidence/proof_first.json']:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'immutable output pins')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_ROW_BINDING_AND_CONDITIONAL_CORRECTED_CEILINGS','rows':count,'exact_scalar_comparisons':checks,'regions':counter,'parameters':par['params'],'delta':str(delta),'rational_exp4delta_upper':str(rat),'results':results,'accepted_dependencies':up,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Conditional X(E) bounds only. Physical W, weak regularity, both tails, numerator and inverse are not certified.'};write(D/'evidence/check.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['files','results']}))

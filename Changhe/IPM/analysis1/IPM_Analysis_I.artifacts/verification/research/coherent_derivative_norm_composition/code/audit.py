"""Manual IEEE to fmpq and cross-multiplied inequalities, independent iv exp."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import json,gzip,hashlib,struct,time
from flint import fmpq as Q
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/coherent_derivative_norm_composition';W=B/'research/weighted_derivative_scalar_norms';G=B/'research/derivative_intended_partition';iv.dps=100

def need(v,s):
 if not v:raise ValueError(s)
def load(p):return json.loads(p.read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def binary(v):
 bits=struct.unpack('>Q',struct.pack('>d',float(v)))[0];e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e!=2047,'finite source');a=m if e==0 else m+(1<<52);power=-1074 if e==0 else e-1075;return (-1 if bits>>63 else 1)*Q(a)*Q(2)**power

def qi(x):return iv.mpf(int(x.p))/int(x.q)
def mpq(v):
 s,m,e,bc=v;return (-1 if s else 1)*Q(int(m))*Q(2)**int(e)
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();first=load(D/'evidence/check.json');pins=dict(first['files'])
for n,h in pins.items():need(sha(B/n)==h,'actual first pin')
geo=load(G/'data_exact/geometry.json');par=load(W/'data_exact/parameters.json');need(geo['params']==par['params']==first['parameters'],'same parameter inputs');fields=par['fields']
for name,want in [('k',Q(1615536043799051,9007199254740992)),('L',Q(8614738245908811,1125899906842624))]:need(binary(float.fromhex(par['params'][name]['float_hex']))==Q(par['params'][name]['exact'])==want,'independent exact parameter')
with gzip.open(W/'data_exact/rows.jsonl.gz','rt') as f:exact=[json.loads(line) for line in f]
need(len(exact)==len(geo['rows'])==19389,'complete archives');by={(x['region'],x['index']):x for x in exact};gb={(x['region'],x['ci']):x for x in geo['rows']};need(len(by)==len(gb)==19389,'unique rows');checks=0;delta=Q(0);counts={}
for reg in ['outer','middle','inner']:
 src=load(B/geo['regions'][reg]['source_rows'])['rows'];counts[reg]=len(src)
 for ci in reversed(range(len(src))):
  row=src[ci];x=by[reg,ci];g=gb[reg,ci];need(row['ci']==ci,'source index');vals={n:binary(row[n]) for n in fields}
  for n in fields:need(vals[n]==Q(x['exact'][n]),'manual IEEE exact scalar');checks+=1
  aa,bb=Q(g['a']),Q(g['b']);need(0<bb-aa<=vals['h'] and vals['h']-(bb-aa)==Q(g['h_slack']),'independent same width');need(aa-vals['t_a']==Q(g['offset']),'independent same start');delta=max(delta,abs(aa-vals['t_a']))
last=Q(7074968463789829,281474976710656)
for g in reversed(geo['rows']):
 need(Q(g['b'])==last,'independent coherent endpoint cover');last=Q(g['a'])
need(last==Q(-1389482001461413,140737488355328),'independent first endpoint')
need(checks==135723 and counts==first['regions'] and delta==Q(first['delta']),'all exact comparisons');xx=4*delta;need(0<xx<1,'valid geometric series');results=[]
for v in first['results']:
 c,d=Q(v['old_ceiling']),Q(v['new_ceiling']);cross=d*d*(1-xx)-c*c;need(cross>0 and cross/(1-xx)==Q(v['exact_squared_slack']),'independent cross multiplication');en=iv.exp(2*qi(delta))*qi(c);lo,hi=map(mpq,en._mpi_);al,ah=map(Q,v['corrected_old_ceiling_arb']);need(0<lo<=hi<d and max(lo,al)<=min(hi,ah),'independent iv enclosure overlap');results.append({'old_ceiling':str(c),'new_ceiling':str(d),'cross_multiplied_positive_slack':str(cross),'corrected_old_ceiling_iv':[str(lo),str(hi)]})
for p in [Path(__file__),D/'evidence/check.json']:pins[str(p.relative_to(B))]=sha(p)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_ALL_ROWS_AND_CORRECTED_CEILINGS','manual_ieee_scalar_comparisons':checks,'rows':len(by),'regions':counts,'delta':str(delta),'results':results,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':first['scope']}
with (D/'evidence/audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['files','results']}))

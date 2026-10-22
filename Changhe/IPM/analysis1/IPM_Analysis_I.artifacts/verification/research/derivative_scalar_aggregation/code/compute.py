from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,gzip,struct,time,sys
import sympy as s
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_scalar_aggregation'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
start=time.monotonic();pins={}
manifest=json.loads((D/'evidence/manifest.json').read_text())
for n,a in manifest['files'].items():assert sha(B/n)==a['sha256'];pins[n]=a['sha256']
proof=json.loads((D/'evidence/proof_first.json').read_text());assert proof['proof_sha256']==sha(D/'PROOF.md')
t,th=s.symbols('t theta',real=True);f=s.Function('f')(t,th);c=s.cos(th);z=s.sin(th)
dx=lambda h:s.exp(-t)*(c*s.diff(h,t)-z*s.diff(h,th))
dy=lambda h:s.exp(-t)*(z*s.diff(h,t)+c*s.diff(h,th))
ft,fh=s.diff(f,t),s.diff(f,th);ftt,fth,fhh=s.diff(f,t,2),s.diff(f,t,th),s.diff(f,th,2)
formulas=[c*c*ftt-2*c*z*fth+z*z*fhh+(z*z-c*c)*ft+2*c*z*fh,z*z*ftt+2*c*z*fth+c*c*fhh+(c*c-z*z)*ft-2*c*z*fh,c*z*ftt+(c*c-z*z)*fth-c*z*fhh-2*c*z*ft+(z*z-c*c)*fh]
for raw,expected in zip([dx(dx(f)),dy(dy(f)),dx(dy(f))],formulas):assert s.simplify(s.exp(2*t)*raw-expected)==0
keys=['W_0_0','W_1_0','W_0_1','W_2_0','W_1_1','W_0_2','m_inf','wf_sup','W_eps_minus_dteps','W_K','W_dtK']
maxima={};regions={};total=0;source_rows={}
path=D/'data_exact/rows.jsonl.gz'
with path.open('xb') as raw,gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=1,mtime=0) as out:
 out.write((json.dumps({'type':'header','schema':'derivative-scalar-bits-v1','keys':keys,'rows':19389,'source_files':pins},sort_keys=True)+'\n').encode())
 for region,file,count in [('middle','runs__cert_deriv_middle.json',7809),('inner','runs__cert_deriv_regions_inner.json',2632),('outer','runs__cert_deriv_regions_outer.json',8948)]:
  d=json.loads((D/'sources'/file).read_text());assert d['done'] is True and len(d['rows'])==count;rm={}
  for ci,r in enumerate(d['rows']):
   assert r['ci']==ci and r['nder'] in [2,5];v={key:F.from_float(r[key]) for key in keys};assert all(x>=0 for x in v.values()) and v['m_inf']>0
   base={'W':v['W_0_0'],'gradient':v['W_1_0']+v['W_0_1'],'second_partial':v['W_2_0']+2*v['W_1_1']+v['W_0_2']+v['W_1_0']+2*v['W_0_1'],'eps_minus_Eeps':v['W_eps_minus_dteps'],'K':v['W_K'],'EK':v['W_dtK']}
   values={key:q/v['m_inf'] for key,q in base.items()};values.update({'weighted_'+key:v['wf_sup']*q/v['m_inf'] for key,q in base.items()})
   row={'type':'row','region':region,'cell':ci,'bits':{key:struct.pack('>d',r[key]).hex() for key in keys},'values_exact':{key:str(q) for key,q in values.items()}}
   out.write((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
   for name,q in values.items():
    hit={'region':region,'cell':ci,'upper_exact':str(q),'t_a_display_only':r['t_a']}
    if name not in maxima or q>F(maxima[name]['upper_exact']):maxima[name]=hit
    if name not in rm or q>F(rm[name]['upper_exact']):rm[name]=hit
   total+=1
  regions[region]=rm;source_rows[region]=count
 out.write((json.dumps({'type':'complete','rows':total,'regions':source_rows},sort_keys=True)+'\n').encode())
assert total==19389
claims={'gradient':F(4195,10000),'second_partial':F(3566,5)}
claim_results={name:{'ceiling_exact':str(q),'strictly_dominates_saved_maximum':F(maxima[name]['upper_exact'])<q} for name,q in claims.items()}
for p in [D/'PROOF.md',D/'evidence/proof_first.json',D/'evidence/manifest.json',path,Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SAVED_SCALAR_AGGREGATION_PHYSICAL_OPEN','rows':total,'expressions_per_row':12,'exact_scalar_expressions':total*12,'symbolic_Cartesian_identities':3,'maxima':maxima,'regions':regions,'claim_results':claim_results,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Exact scalar audit of decoded saved binary64 numbers only; physical derivative majorants, denominator validity, cell coverage, tails, inverse and IPM endpoint remain open.'}
with (D/'evidence/compute.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','rows','exact_scalar_expressions','claim_results','seconds']}));print(json.dumps({k:{**v,'display_only':float(F(v['upper_exact']))} for k,v in maxima.items()}))

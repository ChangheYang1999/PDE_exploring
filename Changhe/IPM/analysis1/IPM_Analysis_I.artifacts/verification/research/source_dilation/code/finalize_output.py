"""Current-file closure of topic96, with fresh high-precision output checks."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_dilation';E=D/'evidence';R=B/'notes/reviews';ctx.prec=1536
files={};pins=0
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def ff(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_EXACT_AND_TWO_ENGINE_DILATION_CHECKS'
for f,h in c['files'].items():assert sha(B/f)==h,f;files[f]=h;pins+=1
assert c['counts']['fresh_integer_norm_containments']==24 and c['counts']['integer_root_cross_multiplications']==48
assert len(c['annulus_examples'])==12
fresh=0
for row in c['annulus_examples']:
 s,ell=F(row['s']),F(row['ell']);a=qa(1+ell*ell*F(4,9));b=qa(1+ell*ell*F(25,16))
 val=arb.pi()*qa(ell**-4/(s+1))*(b**qa(s+1)-a**qa(s+1));assert val.is_finite()
 lo,hi=ff(val.lower()),ff(val.upper());il,ih=map(F,row['independent_rational_root_box']);assert 0<il<ih
 for eng,box in row['squared_Hs_Dell_bounds'].items():
  l,h=map(F,box);assert 0<l<=lo<=hi<=h and l<=il<ih<=h;fresh+=1
for name in ('source_semigroup','source_order_family'):
 p=B/'research'/name/'evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED')
 for f,h in v['files'].items():assert sha(B/f)==h,f;pins+=1
reviews={}
for kind in ('proof','closure'):
 tag='source_dilation_'+kind;m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(z['text'] for z in raw['content'] if z['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert 'accept' in ans.lower()
 reviews[tag]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
 for suffix in ('request.txt','metadata.json','response.json','response.md'):
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_AUXILIARY_SOURCE_DILATION','dependency_hash_comparisons':pins,'fresh_arb1536_containments':fresh,'producing_counts':c['counts'],'scope':'All V31(a)-(e), explicitly stated in PROOF and ADDENDUM, for each s in3.05..3.1. Exact same E,a,d; conjugated maximal domain; N_(1/ell) inverse and ell^(-s) Hs conversion. No actual R_ell value or global IPM inverse.','open':['Actual floating R_ell values','Physical rank-one feedback','Global realization, residual and nonlinear closure','Any decisive endpoint'],'reviews':reviews,'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json'),'fresh_containments':fresh},indent=2))

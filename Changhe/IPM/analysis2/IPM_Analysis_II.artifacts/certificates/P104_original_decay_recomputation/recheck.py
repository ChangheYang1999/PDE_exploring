"""Independent power restrictions and exact radial maximizer."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import arb,arb_mat,ctx
here=Path(__file__).parent;root=here.parents[2];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(root/'research/95_refit_global_hypotheses/verification'))
from recheck_norms import make_fields,upper_fields
from recheck_fast import A,endpoints,tree
def main(kind):
 ctx.prec=576;start=time.monotonic();source=here/'polynomials.json';data=json.loads(source.read_text());path=here/f'{kind}.json';cert=json.loads(path.read_text());assert cert['status']=='COMPLETE' and cert['polynomials_sha256']==sha256(source.read_bytes()).hexdigest();S,labels=make_fields(data,{'polynomials':{}},'u' if kind=='u' else 'fourth');nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p);P={}
 for key,p in S.items():
  m=arb_mat(nt+1,nz+1)
  for (i,k),v in p.items():m[i,k]=A(v)
  P[key]=m
 paths={x['path'] for x in cert['accepted']};assert len(paths)==len(cert['accepted']);tree(paths);delta=F(data['delta']);q=F(2,5);target=F(cert['target']);assert target=={'Drho':F('19.94465'),'Du':F('1.85619'),'u':F('0.97743')}[kind];records=[]
 for row in cert['accepted']:
  a,b,c,d=endpoints(row['path']);assert list(map(str,[a,b]))==row['t'] and list(map(str,[c,d]))==row['z'];vals=upper_fields(P,nt,nz,a,b,c,d,delta,labels);ss=lambda key:vals[key]**2
  angular=arb(1) if c<=0<=d else 1-A(min(abs(c),abs(d)))**2
  if kind=='u':raw=(1+A(d))/2*ss('u1')+(1-A(c))/2*ss('u2')
  elif kind=='Drho':raw=ss('ry')+angular*ss('rx')
  else:raw=2*ss('d22')+angular*(ss('d13')+ss('d31'))
  candidates=[a,b]
  if a<=q/delta<=b:candidates.append(q/delta)
  f=arb(0)
  for x in candidates:f=f.max(A(x)**A(q)*(1-A(x))**A(delta-q))
  ratio=f*raw/A(target**2);assert ratio<=1,(row['path'],ratio);records.append({'path':row['path'],'ratio':ratio.str(100),'pass':True})
  if len(records)%100==0:print(kind,len(records),time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'kind':kind,'leaves':len(records),'rows':records,'primary_sha256':sha256(path.read_bytes()).hexdigest(),'polynomials_sha256':sha256(source.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'seconds':time.monotonic()-start};(here/f'{kind}.recheck.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],kind,len(records),'PASS',out['seconds'],flush=True)
if __name__=='__main__':main(sys.argv[1])

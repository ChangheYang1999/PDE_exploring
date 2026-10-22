"""Source-bound exact polynomial construction and whole-angle Bernstein cover."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,time,hashlib,resource
from flint import fmpq_poly as Poly,fmpq
from checked_core_source import bind
from far_section_rational import construct,endpoint_polynomials
from far_poly_bounds import root,split,leaf,c12_interval
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def main():
 if not __debug__:raise RuntimeError('normal Python required')
 ap=argparse.ArgumentParser();ap.add_argument('source_json');ap.add_argument('--out',required=True);ap.add_argument('--target',default='1/10000');ap.add_argument('--seconds',type=float,default=360);args=ap.parse_args()
 t=time.monotonic();out=Path(args.out);out.mkdir(parents=True,exist_ok=True);data,binding=bind(args.source_json)
 pol=endpoint_polynomials(data);r=construct(pol,data['s'],data['alpha']);A=Poly(r['A']);ns=[Poly(p) for p in r['numerators']];c12,exp=c12_interval(data['alpha']);a=F(data['a']);mid=(c12[0]+c12[1])/2
 pmap={'A':A,**{f'N{j+1}':p for j,p in enumerate(ns)}};pmap['N123']=sum(ns[:3],Poly([]));pmap['Cmid']=fmpq(str(mid))*pmap['N123']+fmpq(str(a))*ns[3]
 state={k:root(p) for k,p in pmap.items()}
 files=[Path(__file__),Path('code/far_section_rational.py'),Path('code/far_poly_bounds.py'),Path('code/checked_core_source.py'),Path('research/interval_far_section/PROOF.md'),Path(args.source_json),Path(data['source'])]
 inp={'utc':now(),'source_json':args.source_json,'source_binding':binding,'a':str(a),'s':data['s'],'alpha':data['alpha'],'common_power':r['K'],'final_orders':r['final_orders'],'c12':[str(v) for v in c12],'exponential':exp,'polynomials':{k:[str(v) for v in p.coeffs()] for k,p in pmap.items()},'root_bernstein':{k:{'numerators':[str(v) for v in b],'denominator':str(d)} for k,(b,d) in state.items()},'hashes':{str(p):sha(p) for p in files}}
 (out/'input.json').write_text(json.dumps(inp,indent=2)+'\n');print(now(),'constructed',r['K'],[(k,p.degree()) for k,p in pmap.items()],time.monotonic()-t,flush=True)
 target=F(args.target);stack=[('',state)];leaves=[];visited=0;upper=F(0);failure=None
 while stack and time.monotonic()-t<args.seconds and visited<32768:
  path,st=stack.pop();visited+=1;check=leaf(st,c12,a)
  if check['A_lower']>0 and check['denominator_lower']>0 and check['ratio_upper']<=target:
   leaves.append(path);upper=max(upper,check['ratio_upper']);continue
  if len(path)>=28:
   stack.append((path,st));failure={'path':path,'bounds':{k:str(v) for k,v in check.items()}};break
  pairs={k:split(*v) for k,v in st.items()};stack.extend([(path+'1',{k:v[1] for k,v in pairs.items()}),(path+'0',{k:v[0] for k,v in pairs.items()})])
  if visited%64==0:print(now(),'visited',visited,'leaves',len(leaves),'remaining',len(stack),'depth',len(path),flush=True)
 cert={'utc':now(),'status':'CONFIRMED_COVER' if not stack else 'OPEN','input_sha256':sha(out/'input.json'),'target':str(target),'leaves':leaves,'remaining':len(stack),'visited':visited,'proved_upper':str(upper) if not stack else None,'failure':failure,'seconds':time.monotonic()-t,'scope':'Entire mixed far section only, conditional physical interpretation under a positive full chart; no finite-radius error or PDE existence claim.'}
 (out/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n');print(json.dumps({k:v for k,v in cert.items() if k!='leaves'},indent=2),flush=True)
if __name__=='__main__':main()

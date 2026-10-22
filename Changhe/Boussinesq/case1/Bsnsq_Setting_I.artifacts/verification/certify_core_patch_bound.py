"""Exact interval/Bernstein uniform bound for each rational Gaussian patch.
No solver imports. An unfinished cover remains OPEN.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,time
from logarithmic_chart_certificate import I,exp_enclosure,root_bernstein,validate_root,polynomial_bounds,split,sha,now

def endpoints(u,k):
 if u==1:return I(0),I(0)
 t=k*u/(1-u)
 if t>=64:return I(0,F(1,2**64)),I(0,F(64,2**64))
 f=1/exp_enclosure(t)
 return f,t*f

def factors(ul,uh,k):
 f0l,f1l=endpoints(ul,k);f0h,f1h=endpoints(uh,k)
 f0=I(f0h.a,f0l.b)
 upper=max(f1l.b,f1h.b)
 if ul<=1/(1+k)<=uh:upper=max(upper,(1/exp_enclosure(F(1))).b)
 f1=I(min(f1l.a,f1h.a),upper)
 low=min(ul*(1-ul),uh*(1-uh));high=F(1,4) if ul<=F(1,2)<=uh else max(ul*(1-ul),uh*(1-uh))
 return f0,f1,I(low,high)*f0

def patch_bound(b,d,bo,k):
 ul,uh,vl,vh=bo;f,g,a=factors(ul,uh,k);F0,G,A=factors(vl,vh,k)
 d0=I(1,3)*f*F0-I(2,F(10,3))*f*G-I(2,6)*g*F0+4*g*G
 du=I(2,6)*a*F0-4*a*G;dv=I(2,F(10,3))*f*A-4*g*A;duv=4*a*A
 p=polynomial_bounds(b,d,uh-ul,vh-vl)
 return d0*p[0,0]+du*p[1,0]+dv*p[0,1]+duv*p[1,1]

def produce(source,out,target,seconds):
 out=Path(out);out.mkdir(parents=True,exist_ok=True);raw=json.loads(Path(source).read_text());start=time.monotonic();roots=[];certs=[]
 for patch in raw['patches']:
  c=[[F(v) for v in r] for r in patch['coefficients']];b,d=root_bernstein(c);validate_root(c,b,d)
  roots.append({'coefficients':patch['coefficients'],'R':patch['R'],'L':patch['L'],'bernstein_numerators':[[str(v) for v in r] for r in b],'denominator':str(d)})
 inp={'utc':now(),'source_json':str(source),'source_json_sha256':sha(source),'source_npz_sha256':raw['source_sha256'],'patches':roots,'producer_sha256':sha(__file__),'theorem_sha256':sha('research/core_patch_chart/PROOF.md'),'target_per_patch':str(target)}
 (out/'input.json').write_text(json.dumps(inp,indent=2)+'\n')
 for ip,root in enumerate(roots):
  b=[[int(v) for v in r] for r in root['bernstein_numerators']];d=int(root['denominator']);k=(F(root['R'])/F(root['L']))**2
  stack=[('',(F(0),F(1),F(0),F(1)),b,d)];leaves=[];visited=0;bound=F(0);depth=0
  while stack and time.monotonic()-start<seconds and visited<32768:
   path,bo,b,d=stack.pop();visited+=1;depth=max(depth,len(path));r=patch_bound(b,d,bo,k);size=max(abs(r.a),abs(r.b))
   if size<=target:
    leaves.append({'path':path,'range':r.text()});bound=max(bound,size);continue
   axis=len(path)%2;l,h,dd=split(b,d,axis);lo=list(bo);hi=list(bo);mid=(bo[2*axis]+bo[2*axis+1])/2;lo[2*axis+1]=mid;hi[2*axis]=mid
   lch,hch='01' if axis==0 else '23';stack.extend([(path+hch,tuple(hi),h,dd),(path+lch,tuple(lo),l,dd)])
   if visited%128==0:print(now(),'patch',ip,'visited',visited,'remaining',len(stack),'depth',depth,flush=True)
  certs.append({'patch':ip,'remaining':len(stack),'leaves':leaves,'max_depth':depth,'visited':visited,'uniform_bound':str(bound) if not stack else None})
 result={'utc':now(),'input_sha256':sha(out/'input.json'),'status':'CONFIRMED_BOUND' if all(r['remaining']==0 for r in certs) else 'OPEN','patches':certs,'seconds':time.monotonic()-start,'scope':'Uniform normalized chart-contribution bound only; separate outer positivity and replay required.'}
 (out/'certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='patches'},indent=2),flush=True)
 print([(p['remaining'],len(p['leaves']),float(F(p['uniform_bound'])) if p['uniform_bound'] else None) for p in certs],flush=True)
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_json');ap.add_argument('--out',required=True);ap.add_argument('--bound',default='1/20');ap.add_argument('--seconds',type=float,default=180);a=ap.parse_args();produce(a.source_json,a.out,F(a.bound),a.seconds)

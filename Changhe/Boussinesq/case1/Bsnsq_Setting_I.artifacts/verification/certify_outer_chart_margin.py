"""Generate a prescribed-margin outer chart certificate for explicit component data.
Uses only the verifier's rational Bernstein routines; replay remains separate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,time
from logarithmic_chart_certificate import (root_bernstein,validate_root,direct_cheb,transcendental,q_bound,polynomial_bounds,split,sha,now)
from core_generating_mp import export_source
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--out',required=True);ap.add_argument('--delta',default='1/10');ap.add_argument('--seconds',type=float,default=240);a=ap.parse_args()
folder=Path(a.out);folder.mkdir(parents=True,exist_ok=True);source=Path(a.source);delta=F(a.delta);assert delta>0
with np.load(source,allow_pickle=False) as z:
 if 'cc' in z.files or 'core' in z.files:raise ValueError('Supply explicitly separated outer component, not patched source')
 raw=np.asarray(z['c']);assert raw.dtype==np.dtype('float64')
 c=[[F(float(v)) for v in row] for row in raw.reshape(int(z['J'])+1,int(z['Kw'])+1)];alpha=F(float(z['alpha']));s=F(float(z['se']))
 assert float(z['beta'])==3 and int(z['m'])==3 and float(z['gam'])==0 and alpha>0 and s>0
start=time.monotonic();b,d=root_bernstein(c);checks=validate_root(c,b,d);h=direct_cheb(c,F(1),F(0));assert h>0
root={'utc':now(),'coefficients':[[str(v) for v in row] for row in c],'alpha':str(alpha),'bernstein_numerators':[[str(v) for v in row] for row in b],'denominator':str(d),'source_code_sha256':sha(__file__),'center':str(h),'self_check':checks,'N':80}
(folder/'input.json').write_text(json.dumps(root,indent=2)+'\n')
(folder/'source.json').write_text(json.dumps({'utc':now(),'source':str(source),'source_sha256':sha(source),'input_sha256':sha(folder/'input.json'),'se_exact_binary64':str(s),'source_dtype':str(raw.dtype),'scope':'Explicit outer component only; no core contribution is included.'},indent=2)+'\n')
stack=[('',F(0),F(1),F(0),F(1),b,d)];leaves=[];visited=0;lower=None;depth=0
report={'start_utc':now(),'input_sha256':sha(folder/'input.json'),'requested_margin':str(delta),'code_sha256':sha(__file__)}
while stack and time.monotonic()-start<a.seconds and visited<32768:
 path,tl,th,wl,wh,b,d=stack.pop();visited+=1;depth=max(depth,len(path));T,l,l2=transcendental(alpha,tl,th)
 if T.a**6+wl**3>1:leaves.append({'path':path,'kind':'outside'});continue
 q=q_bound(polynomial_bounds(b,d,th-tl,wh-wl),T,l,l2,wl,wh)
 if q.a>=delta:
  lower=q.a if lower is None else min(lower,q.a);leaves.append({'path':path,'kind':'positive','lower':str(q.a)});continue
 axis=len(path)%2;left,right,dd=split(b,d,axis)
 if axis==0:
  mid=(tl+th)/2;stack.extend([(path+'1',mid,th,wl,wh,right,dd),(path+'0',tl,mid,wl,wh,left,dd)])
 else:
  mid=(wl+wh)/2;stack.extend([(path+'3',tl,th,mid,wh,right,dd),(path+'2',tl,th,wl,mid,left,dd)])
 if visited%128==0:print(now(),'visited',visited,'remaining',len(stack),'depth',depth,flush=True)
report.update(utc=now(),remaining=len(stack),leaves=leaves,visited=visited,seconds=time.monotonic()-start,lower_bound=str(lower) if not stack else None,verdict='CONFIRMED_OUTER_MARGIN' if not stack else 'OPEN')
(folder/'certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='leaves'},indent=2),flush=True)

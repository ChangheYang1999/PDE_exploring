"""Arb512 complete finite interior harmonic sum. No JS, servers, RLScience."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
import json,sys,time,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_modes'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):
 assert x.is_finite();l,h=ep(x.lower()),ep(x.upper());assert l<=h
 return {'lower_exact':str(l),'upper_exact':str(h),'display':x.str(32)}
def unbox(x):return aa(x['lower_exact']).union(aa(x['upper_exact']))
def run(outpath):
 assert not sys.flags.optimize;st=time.monotonic();ctx.prec=512;ctx.threads=1
 src=B/'data_exact/modal_v2.json';assert sha(src)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 z=json.loads(src.read_text());hexq=lambda x:F(float.fromhex(x));k=hexq(z['scalars_hex']['k']);L=hexq(z['scalars_hex']['L']);t=hexq(z['arrays']['knots']['hex'][-1]);ar=z['arrays']['Aout']['hex'];exps=[2*k-1,3*k-2,k-2];assert 0<k<F(1,4)
 lp=B/'research/outer_leading_cancellation/evidence/leading_result.json';lead=json.loads(lp.read_text())['residual_coefficients'];assert len(lead)==522
 h1=[aa(k/(1-k))*aa(-exps[0]*t).exp()*unbox(x['value']) for x in lead]
 hp=B/'research/hminus1_tail_quantitative/evidence/arb.json';prior=json.loads(hp.read_text());h2=list(map(unbox,prior['H2_sines']));assert len(h2)==783
 col=[hexq(ar[10*m+6]) for m in range(260)];sn=[F(0)]*261
 for m,x in enumerate(col):
  for f in (1+2*m,1-2*m,3+2*m,3-2*m):sn[(abs(f)-1)//2]+=(1 if f>0 else -1)*x/8
 hd=[-aa((5-k)*t).exp()*aa(x) for x in sn];rows=[h1,h2,hd];R=9;T=3000;q=aa(F(R*R,T*T));vals={};sums=[arb(0) for _ in range(4)]
 count=0
 for name,a,h in zip(('1','2','d'),exps,rows):
  vals['h'+name+'_freq5']=h[2]
  for j in range(4):
   ss=arb(0);power=arb(1)
   for n in range(2,len(h)):
    falling=1
    for d in range(j):falling*=2*n-1-d
    assert 2*n-a-1>0 and falling>0
    ss+=aa(F(n*falling)/(2*n-a-1))*abs(h[n])*power;power*=q;count+=1
   val=aa(R**(3-j))*aa((a-3)*F(1)).__mul__(aa(T).log()).exp()*ss
   vals['row'+name+'_j'+str(j)]=val;sums[j]+=val
 for j,val in enumerate(sums):vals['total_j'+str(j)]=val
 vals['R_b']=aa(t).exp();vals['L']=aa(L)
 files={str(p.relative_to(B)):sha(p) for p in (src,lp,hp,D/'PROOF.md',Path(__file__))}
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'Arb512 complete finite harmonic sum (1)','files':files,'exact':{'k':str(k),'L':str(L),'tplus':str(t),'R':str(R),'T':str(T),'exponents':list(map(str,exps))},'counts':{'row_lengths':list(map(len,rows)),'finite_positive_terms':count,'physical_hd_projection_inputs':len(col)},'values':{n:box(x) for n,x in vals.items()},'seconds':time.monotonic()-st}
 outpath.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({n:v['display'] for n,v in result['values'].items()}));return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=D/'evidence/arb.json');args=ap.parse_args();out=args.output.resolve();assert out.is_relative_to(D/'evidence');run(out)

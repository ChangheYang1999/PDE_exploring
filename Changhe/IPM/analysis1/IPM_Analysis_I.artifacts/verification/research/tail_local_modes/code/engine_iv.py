"""iv180 fifth sine mode plus exact quotient-norm geometric majorant.
No JS/TS, servers/listeners/tunnels, RLScience, Lean/Lake, outside writes.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time,argparse,math
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_modes'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ep(t):sg,m,e,bc=t;assert bc>=0;return F(-int(m) if sg else int(m))*F(2)**int(e)
def box(x):
 l,h=map(ep,x._mpi_);assert l<=h
 return {'lower_exact':str(l),'upper_exact':str(h),'display':str(x)}
def unbox(x):return iv.mpf([aa(x['lower_exact']).a,aa(x['upper_exact']).b])
def ff(v,j):return math.prod(range(v-j+1,v+1))
def moments():
 # Positive rational terms and a rigorous geometric tail. For m>=64,
 # the ratio of consecutive (2m+5)_j is at most (1+2/(2*64+6-j))^j.
 # After multiplication by1/4 this is below1. Sum through m=63.
 out=[]
 for j in range(4):
  s=sum((F(ff(2*m+5,j),4**m) for m in range(64)),F(0))
  rat=F(1,4)*(1+F(2,2*64+6-j))**j;assert rat<1
  first=F(ff(2*64+5,j),4**64);hi=s+first/(1-rat)
  out.append((s,hi,rat))
 return out
def run(outpath):
 assert not sys.flags.optimize;iv.dps=180;st=time.monotonic()
 arch=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
 assert sha(arch)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(arch,allow_pickle=False) as z:k=F(float(z['k']));L=F(float(z['L']));t=F(float(z['knots'][-1]));cols=z['Aout'].copy()
 assert cols.shape==(260,10) and 0<k<F(1,4);exps=[2*k-1,3*k-2,k-2];rb=iv.exp(aa(t))
 lp=B/'research/outer_leading_cancellation/evidence/leading_iv_audit.json';lead=json.loads(lp.read_text());assert lead['status']=='PASS';eps=lead['residual_coefficients'];assert len(eps)==522
 h15=aa(k)/aa(1-k)*unbox(eps[2]['value'])/(rb**aa(exps[0]))
 hp=B/'research/hminus1_tail_quantitative/evidence/iv.json';prior=json.loads(hp.read_text());assert len(prior['H2_sines'])==783;h25=unbox(prior['H2_sines'][2]);n2=unbox(prior['values']['N2'])
 c=list(map(lambda x:F(float(x)),cols[:,6]));hd5=-(rb**aa(5-k))*aa((c[1]+c[2]-c[3]-c[4])/8);nd=(rb**aa(5-k))*aa(sum(map(abs,c),F(0)))
 ns=[aa('38.37961982'),n2,nd];h5s=[h15,h25,hd5];R=9;T=3000;q=F(R*R,T*T);assert q<=F(1,4)
 mt=moments();Z=[iv.mpf([aa(l).a,aa(h).b]) for l,h,r in mt];vals={};totals=[iv.mpf(0) for _ in range(4)]
 for name,a,N,h5 in zip(('1','2','d'),exps,ns,h5s):
  vals['h'+name+'_freq5']=h5
  for j in range(4):
   bracket=aa(F(2*ff(3,j))/(3-a))*abs(h5)+N*aa(max(F(1,2),F(2)/(3-a))*q/2)*Z[j]
   val=aa(R**(3-j))*(aa(T)**aa(a))/aa(T**3)*bracket
   vals['row'+name+'_j'+str(j)]=val;totals[j]+=val
 for j,v in enumerate(totals):vals['total_j'+str(j)]=v
 vals['R_b']=rb;vals['L']=aa(L);vals['N1_ceiling']=ns[0];vals['N2']=n2;vals['Nd']=nd
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'iv180 original NPZ fifth sine mode plus quotient l1 and positive geometric-tail majorant (3)','files':{str(p.relative_to(B)):sha(p) for p in (lp,hp,D/'PROOF.md',Path(__file__))},'source_archive':{'path':str(arch),'sha256':sha(arch)},'exact':{'k':str(k),'L':str(L),'tplus':str(t),'R':str(R),'T':str(T),'exponents':list(map(str,exps))},'geometric': [{'lower_exact':str(l),'upper_exact':str(h),'tail_ratio':str(r)} for l,h,r in mt],'counts':{'separated_modes':3,'coefficient_norms':3,'geometric_partial_terms':256,'positive_majorants':12},'values':{n:box(x) for n,x in vals.items()},'seconds':time.monotonic()-st}
 outpath.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({n:v['display'] for n,v in result['values'].items()}));return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=D/'evidence/iv.json');args=ap.parse_args();out=args.output.resolve();assert out.is_relative_to(D/'evidence');run(out)

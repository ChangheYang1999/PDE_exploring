import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import sys,json,hashlib
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/conormal_feasibility/evidence';ctx.prec=320;ctx.threads=1;iv.dps=160
assert sys.flags.optimize==0
k=F(1615536043799051,9007199254740992);A=2/k-1;D=2*A+1;b0=(A+3)/2;beta3=(6*A+1)/D
alpha=F(1,20);s=F(153,50);b=F(307,100);a=F(129,20);gamma=F(129,1000);gamma_prime=1+gamma
assert gamma_prime==F(1129,1000) and 2-gamma_prime>0
margin={'alpha_positive':alpha,'alpha_below1':1-alpha,'s_over_3alpha':s-3-alpha,'b_over_s':b-s,'b_below_beta3half':beta3+F(1,2)-b,'a_over5half':a-F(11,2),'a_below6half':F(13,2)-a,'negative_delta':a*A+b0-b*D,'corner':a-F(1,2)-(D*(s-F(1,2))-1)/A,'gamma_positive':gamma,'gamma_below_k':k-gamma,'gamma_prime_below2':2-gamma_prime,'source_fast':(F('29.7494906')+b0)/A-s,'source_slow':b0-s}
assert all(v>0 for v in margin.values()) and F('10.1507252')<A<F('10.1507253')
assert margin['negative_delta']==(81*A-157)/100
amax=(A-F(3,2))/D;assert amax==beta3+F(1,2)-3
cap=A-F(3,2)-D*alpha;assert margin['negative_delta']<cap
assert F(1,2)+(D*(s-F(1,2))-1)/A==2*s-F(1,2)+(s-F(3,2))/A
assert (b*D-b0)/A==2*b-F(1,2)+(b-F(3,2))/A
assert (b*D-b0)/A-(F(1,2)+(D*(s-F(1,2))-1)/A)==(b-s)*(2+1/A)>0
values={'A':A,'delta':-margin['negative_delta'],'base_inverse_cost':1/margin['negative_delta'],'sum_graph_cost':1+1/margin['negative_delta'],'alpha_endpoint':amax,'cost_lower_bound':1/cap,'corner_a_threshold':F(1,2)+(D*(s-F(1,2))-1)/A,'delta_a_threshold':(b*D-b0)/A}
rows={}
for key,q in values.items():
 av=arb(q.numerator)/q.denominator;vv=iv.mpf(q.numerator)/q.denominator
 def af(t):m,e=t.man_exp();return F(int(m))*F(2)**int(e)
 al,ah=af(av.mid())-af(av.rad()),af(av.mid())+af(av.rad())
 def it(t):sign,m,e,bc=t;assert bc>=0;return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
 il,ih=map(it,vv._mpi_);assert al<=q<=ah and il<=q<=ih
 rows[key]={'exact':str(q),'arb_lower':str(al),'arb_upper':str(ah),'iv_lower':str(il),'iv_upper':str(ih),'display':av.str(25)}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SCALAR_FEASIBILITY_REQUIRES_REVIEW','k_exact':str(k),'source_sha256':sha(__file__),'proof_sha256':sha(B/'research/conormal_feasibility/PROOF.md'),'margins':{k:str(v) for k,v in margin.items()},'values':rows,'interval_containments':16,'scope':'Fraction inequalities are decisive; Arb/iv conversions only cross-check representation of exact rational outputs. No independently different operator computation or T3/T5 verification.'}
(E/'margins.json').open('x').write(json.dumps(o,indent=2)+'\n');print(json.dumps({'utc':o['utc'],'status':o['status'],'values':{k:v['display'] for k,v in rows.items()}},indent=2))

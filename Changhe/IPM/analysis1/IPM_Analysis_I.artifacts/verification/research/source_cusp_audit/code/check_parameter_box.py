"""Exact parameter margins with independent Arb and interval rearrangements."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3]; E=B/'research/source_cusp_audit/evidence'
ctx.prec=320;ctx.threads=1;iv.dps=160
assert sys.flags.optimize==0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
aa=lambda q:arb(F(q).numerator)/F(q).denominator
iq=lambda q:iv.mpf(F(q).numerator)/F(q).denominator
def af(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return af(x.mid())-af(x.rad()),af(x.mid())+af(x.rad())
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ie(x):assert not iv.isinf(x) and not iv.isnan(x);return tuple(map(rf,x._mpi_))
Al,Ah=map(F,['10.1507252','10.1507253']);gl,gh=map(F,['29.7494906','29.7494908'])
p=B/'research/modal_source/evidence/source_result.json'
assert sha(p)=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691'
v=json.loads(p.read_text())['final_values']
for key in ['A_trial','A_exact_solution_relation']:assert Al<F(v[key]['lower_exact'])<=F(v[key]['upper_exact'])<Ah
assert gl<F(v['g']['lower_exact'])<=F(v['g']['upper_exact'])<gh
exact={'a':(gl/(Ah-1),gh/(Al-1)),'p':((1+gl)/Ah,(1+gh)/Al),'gamma':(gl/Ah,gh/Al),'q':(Al+2-gh/(Al-1),Ah+2-gl/(Ah-1)),'s_1':(F(5,2)+(gl-F(1,2))/Ah,F(5,2)+(gh-F(1,2))/Al),'alpha_star':((1+gl)/Ah-3,(1+gh)/Al-3)}
x=aa(Al).union(aa(Ah));y=aa(gl).union(aa(gh))
ar={'a':y/(x-1),'p':(1+y)/x,'gamma':y/x,'q':x+2-y/(x-1),'s_1':(y+(x+3)/2)/x+2-2/x,'alpha_star':(1+y)/x-3}
x=iv.mpf([iq(Al).a,iq(Ah).b]);y=iv.mpf([iq(gl).a,iq(gh).b]);z=1/x
vr={'a':(y*z)/(1-z),'p':(1+y)*z,'gamma':y*z,'q':(x*x+x-2-y)/(x-1),'s_1':iq(F(5,2))+(y-iq(F(1,2)))*z,'alpha_star':(y+1-3*x)*z}
rows={}
for key,(l,h) in exact.items():
 al,ah=ae(ar[key]);il,ih=ie(vr[key]);assert al<=l<=h<=ah and il<=l<=h<=ih
 rows[key]={'lower_exact':str(l),'upper_exact':str(h),'arb_lower':str(al),'arb_upper':str(ah),'iv_lower':str(il),'iv_upper':str(ih),'display':ar[key].str(18)}
assert 3<exact['a'][0]<=exact['a'][1]<4 and 3<exact['p'][0]<=exact['p'][1]<4
assert 2<exact['gamma'][0]<=exact['gamma'][1]<3 and exact['q'][0]>F(5,2) and exact['s_1'][0]>F(21,4)
nonres=[]
for i in range(4):
 l=1+gl-i*Ah;h=1+gh-i*Al;j=l.numerator//l.denominator
 assert j<l<=h<j+1
 nonres.append({'i':i,'lower_exact':str(l),'upper_exact':str(h),'integer_below':j})
assert 1+gh-4*Al<0
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PARAMETER_BOX_REQUIRES_REVIEW','scope':'Frozen mu=1 family; not an exact solution source and not the actual trial mu. The linked modal source result was independently verified earlier.','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/source_cusp_audit/PROOF.md'),'modal_source_sha256':sha(p),'box':{'A':[str(Al),str(Ah)],'g':[str(gl),str(gh)]},'rows':rows,'nonresonance':nonres,'interval_endpoint_containments':24,'input_box_containments':3}
(E/'parameter_box.json').open('x').write(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'values':{k:v['display'] for k,v in rows.items()},'nonresonance':nonres},indent=2))

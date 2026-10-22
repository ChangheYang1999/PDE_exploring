"""Arb direct scalar formula versus exact rational exponential-series intervals."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,hashlib,json,time,platform
sys.dont_write_bytecode=True;sys.set_int_max_str_digits(200000)
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/exterior_conic_threshold';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def load(p):return json.loads(Path(p).read_text())
def a(x):x=F(x);return arb(x.numerator)/x.denominator
def arf(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def abox(x):assert x.is_finite();return arf(x.lower()),arf(x.upper())
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):p=[xx*yy for xx in x for yy in y];return min(p),max(p)
def rec(x):assert x[0]>0;return 1/x[1],1/x[0]
def div(x,y):return mul(x,rec(y))
def point(x):x=F(x);return x,x
def pw(x,n):assert x[0]>0 and n>=0;return x[0]**n,x[1]**n
def exp_series(x,N=192):
 assert 0<x<N+2
 term=F(1);s=F(1)
 for j in range(1,N+1):term*=x/j;s+=term
 first=term*x/(N+1);ratio=x/(N+2);tail=first/(1-ratio)
 return (s,s+tail),{'x':str(x),'N':N,'sum_exact':str(s),'next_term_exact':str(first),'ratio_exact':str(ratio),'tail_majorant_exact':str(tail),'range':[str(s),str(s+tail)]}
start=utc();clock=time.monotonic();vp=B/'research/exterior_flow/evidence/verdict.json';cp=B/'research/exterior_flow/evidence/checks.json'
assert sha(vp)=='2a8ae9e75b9cc64a69f950254d01af346eb12aa600ce797680953abc391551dd' and sha(cp)=='3742c1d9f5d7fc76f058fa2f4f8bff340acc253e0d6bc3e2e86f7a3855683a83'
v=load(vp);checks=load(cp);assert v['status']=='CONFIRMED'
pins=dict(v['files']);pins[str(vp.relative_to(B))]=sha(vp)
for p,h in pins.items():assert sha(B/p)==h,p
row=[q for q in checks['cases'] if q['T_exact']=='1'];assert len(row)==1;row=row[0]
P=max(F(row['P_arb']['upper_exact']),F(row['P_iv']['upper_exact']));Q=max(F(row['Q_arb']['upper_exact']),F(row['Q_iv']['upper_exact']))
assert P==F(row['joint_P_upper_exact'])>0 and Q==F(row['joint_Q_upper_exact'])>0
k=F(1615536043799051,9007199254740992);cl=1/k;omega=1-k;tb=F(2289893859708677,281474976710656);A=F(129,20);C=F(307,100);S=A+C;gamma=F(1129,1000)
assert 0<k<1 and S==F(238,25)>gamma>1 and A>0 and C>0
params={name:str(value) for name,value in [('k',k),('c_l',cl),('omega',omega),('t_b',tb),('a',A),('b',C),('S',S),('gamma',gamma),('P',P),('Q',Q)]}
ctx.prec=512;ctx.threads=1
rA=a(tb+5).exp();eA=a(-4*omega).exp();pA=a(P)*eA;qA=a(Q)*eA;muA=a(gamma)+a(S-gamma)/(1+(rA/6)**4)
bA=-(1+a(cl))+muA*a(cl)+a(S)*qA+a(S-gamma)*pA
rawA={'R':rA,'E':eA,'P5':pA,'Q5':qA,'muR':muA,'B5':bA,'s_lower':a(cl)-pA,'vi_lower':a(cl)-qA};valsA={key:abox(x) for key,x in rawA.items()}
xexp,xe=exp_series(4*omega);rB,re=exp_series(tb+5);eB=rec(xexp);pB=mul(point(P),eB);qB=mul(point(Q),eB)
muB=add(point(gamma),div(point(S-gamma),add(point(1),pw(div(rB,point(6)),4))))
bB=add(point(-1+(gamma-1)*cl),add(div(point(cl*(S-gamma)),add(point(1),pw(div(rB,point(6)),4))),mul(eB,point(S*Q+(S-gamma)*P))))
valsB={'R':rB,'E':eB,'P5':pB,'Q5':qB,'muR':muB,'B5':bB,'s_lower':sub(point(cl),pB),'vi_lower':sub(point(cl),qB)}
methods={}
for name,vals in [('arb512',valsA),('fraction_positive_series192',valsB)]:
 for key,(l,u) in vals.items():assert l<=u,key
 assert 20<vals['R'][0]<=vals['R'][1]<510000
 assert 0<vals['E'][0]<=vals['E'][1]<1 and gamma<vals['muR'][0]<=vals['muR'][1]<S
 assert vals['B5'][1]<-F(11,50) and vals['s_lower'][0]>F(557,100) and vals['vi_lower'][0]>F(557,100)
 methods[name]={key:[str(l),str(u)] for key,(l,u) in vals.items()}
for key in valsA:assert max(valsA[key][0],valsB[key][0])<=min(valsA[key][1],valsB[key][1]),key
pins[str(cp.relative_to(B))]=sha(cp)
for p in [D/'PROOF.md',E/'proof_first.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
assert load(E/'proof_first.json')['proof_sha256']==sha(D/'PROOF.md')
out={'start_utc':start,'end_utc':utc(),'seconds':time.monotonic()-clock,'status':'PASS_TWO_METHOD_EXTERIOR_CONIC_SCALARS_REQUIRES_REVIEW','parameters_exact':params,'inherited_row':row,'methods':methods,'rational_exponential_series':{'exp_four_omega':xe,'R':re},'public_strict_bounds':{'R_lower':'20','R_upper':'510000','B5_upper':'-11/50','s_lower':'557/100','vi_lower':'557/100'},'files':dict(sorted(pins.items())),'runtime':{'python':sys.version,'platform':platform.platform(),'arb_bits':512,'series_degree':192,'threads':1},'scope':'Canonical exterior theorem53 premise. All tau>=5; remaining finite coverage and global inverse/endpoints OPEN.'}
p=E/'scalars.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'end_utc':out['end_utc'],'status':out['status'],'seconds':out['seconds'],'pins':len(pins),'approx_informational':{key:[float(z) for z in pair] for key,pair in valsB.items()},'sha256':sha(p)}))

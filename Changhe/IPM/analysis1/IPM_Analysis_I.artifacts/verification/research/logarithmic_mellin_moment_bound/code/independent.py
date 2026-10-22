from pathlib import Path
from fractions import Fraction as F
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq
from mpmath import iv
iv.dps=150
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_mellin_moment_bound';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();primary=p.load(E/'check.json');p.rehash(primary['parent_files']);assert primary['proof_sha256']==p.sha(D/'PROOF.md')=='c40c8cc86a1228692a379011a2bdb772138bd2d1deba4d2330ff8dd34a7b4c70'
raw=p.load(R/'data_exact/modal_v2.json');assert p.sha(R/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
def hx(x):
 sign=-1 if x.startswith('-') else 1;x=x.lstrip('+-');man,e=x.split('p');whole,frac=man[2:].split('.');return fmpq(sign*int(whole+frac,16))*fmpq(2)**(int(e)-4*len(frac))
k=hx(raw['scalars_hex']['k']);A=(2-k)/k;DD=(4-k)/k;a=fmpq(0);s=fmpq(153,50);c=A/2-1;u=(1+k)/k;v=(s*(4-k)-1-k)/k;t=(1+k)/(4-k);w=s-t
assert 0<t<1 and 2<w<3 and DD==2*A+1
actual={n:str(x) for n,x in {'k':k,'A':A,'D':DD,'a':a,'s':s,'c':c,'u':u,'v':v,'t':t,'w':w}.items()};assert actual==primary['actual']
def Q(x):x=fmpq(x);return iv.mpf(int(x.p))/int(x.q)
def ep(x):sgn,m,e,bc=x;return F((-1 if sgn else 1)*m)*F(2)**e
def en(x):l,r=map(ep,x._mpi_);return {'lower_exact':str(l),'upper_exact':str(r)}
records=[]
def half_integral(pp,qq):
 coeff=fmpq(1);sout=iv.mpf(0);Nterms=110;pref=iv.power(iv.mpf(2),-Q(pp))
 for n in range(Nterms):
  term=pref*Q(coeff)*iv.power(iv.mpf(2),-n)/Q(pp+n);sout+=term
  # Exact Pochhammer recurrence; no gamma-function evaluation.
  coeff*=fmpq(n+1)-qq;coeff/=n+1
 assert coeff>0 and Nterms+1-qq>0 and qq>0
 first=pref*Q(coeff)*iv.power(iv.mpf(2),-Nterms)/Q(pp+Nterms)
 assert first.a>0
 tail=2*first
 out=sout+iv.mpf([0,1])*tail
 records.append({'p':str(pp),'q':str(qq),'terms':Nterms,'tail_direction':'positive','tail_upper_exact':en(tail)['upper_exact'],'partial_sum':en(sout),'half_integral':en(out),'universal_ratio_reason':'q>0 and n>=110>q-1; both positive rational factors in ratio are <1, hence ratio<1/2'})
 return out
N=(half_integral(t,w)+half_integral(w,t))/2;root=iv.sqrt(N)
values={'N':en(N),'sqrtN':en(root)}
for name,value in values.items():
 lo,hi=map(F,primary['strict_windows'][name]);il,iu=F(value['lower_exact']),F(value['upper_exact']);al,au=F(primary['arb512'][name]['lower_exact']),F(primary['arb512'][name]['upper_exact']);assert lo<il<=iu<hi and max(al,il)<=min(au,iu)
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_BETA_HALF_SERIES_WITH_EXACT_TAIL','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(primary['parent_files']),'exact_values_compared':len(actual),'iv150':values,'series':records,'strict_windows':primary['strict_windows'],'scope':'Separate hex/fmpq parameters and two convergent beta half-series, 110 terms each with proved positive geometric tails; no gamma function or primary-code import. The common beta identity remains a shared analytic dependency.'};p.write(E/'independent.json',out);print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','exact_values_compared','strict_windows']}))

from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import os,sys,json,re,hashlib
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[n]='1'
sys.dont_write_bytecode=True
import sympy as S
from mpmath import iv
iv.dps=220
R=Path(__file__).resolve().parents[3];D=R/'research/anisotropic_frozen_transport_inverse';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def literal(t):
 m=re.fullmatch(r'(-?)0x([0-9a-f]+)\.([0-9a-f]+)p([+-]?\d+)',t);assert m
 sign,whole,frac,e=m.groups();return Q((-1 if sign else 1)*int(whole+frac,16))*Q(2)**(int(e)-4*len(frac))
def pair(z):
 def f(v):sign,m,e,bc=v;assert bc>=0;return Q((-1 if sign else 1)*m)*Q(2)**e
 return {'lower_exact':str(f(z._mpi_[0])),'upper_exact':str(f(z._mpi_[1]))}
def iq(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
start=datetime.now(timezone.utc).isoformat();A=load(E/'arb.json');assert A['proof_sha256']==sha(D/'PROOF.md');assert A['code_sha256']==sha(D/'code/arb_check.py')
parent=load(R/A['parent_path']);assert sha(R/A['parent_path'])==A['parent_sha256'] and parent['files']==A['parent_files']
for n,h in parent['files'].items():assert sha(R/n)==h,n
raw=load(R/A['hex_json']['path']);assert sha(R/A['hex_json']['path'])==A['hex_json']['sha256'];k=literal(raw['scalars_hex']['k']);assert k==Q(A['inputs_exact']['k'])
a=S.Integer(6);s=S.Rational(153,50);mu=a+s-1;ell=S.Rational(1,1)/S.Rational(k.numerator,k.denominator);alpha=1-2*ell;beta=4*ell-1;d=beta-alpha;p,q=S.symbols('p q');solution=next(iter(S.linsolve([p+q-mu,alpha*p+beta*q-1],p,q)));p0,q0=solution;delta=alpha*(a-S.Rational(1,2))+beta*(s-S.Rational(1,2))-1
vals={'ell':ell,'alpha':alpha,'beta':beta,'d':d,'p':p0,'q':q0,'delta':delta,'inverse_bound':-1/delta,'axis_margin_p_minus_a_plus_half':p0-a+S.Rational(1,2)}
assert {n:str(v) for n,v in vals.items()}==A['values_exact'];assert beta>0 and d>0 and delta<0
al,be,aa,ss=S.symbols('alpha beta a s');mm=aa+ss-1;pp,qq=next(iter(S.linsolve([p+q-mm,al*p+be*q-1],p,q)));de=al*(aa-S.Rational(1,2))+be*(ss-S.Rational(1,2))-1
identities={'sum':S.cancel(pp+qq-mm),'transport':S.cancel(al*pp+be*qq-1),'p_axis_margin':S.cancel(pp-(aa-S.Rational(1,2))-de/(be-al)),'q_sobolev_margin':S.cancel(qq-(ss-S.Rational(1,2))+de/(be-al)),'conjugated_growth':S.expand((al*(aa-S.Rational(1,2))-1)+be*(ss-S.Rational(1,2))-de)}
assert all(v==0 for v in identities.values())
lI=1/iq(k);alI=1-2*lI;beI=4*lI-1;dI=beI-alI;deI=alI*iq(Q(11,2))+beI*iq(Q(64,25))-1;qI=(1-alI*iq(Q(403,50)))/dI;pI=iq(Q(403,50))-qI
ivs={'ell':lI,'alpha':alI,'beta':beI,'d':dI,'p':pI,'q':qI,'delta':deI,'inverse_bound':1/(-deI),'axis_margin_p_minus_a_plus_half':pI-iq(Q(11,2))};B={n:pair(z) for n,z in ivs.items()}
for n,z in B.items():
 qv=Q(str(vals[n]));av=A['arb512'][n];assert Q(z['lower_exact'])<=qv<=Q(z['upper_exact']);assert max(Q(z['lower_exact']),Q(av['lower_exact']))<=min(Q(z['upper_exact']),Q(av['upper_exact']))
 lo,hi=A['strict_decimal_windows'][n];assert Q(lo)<Q(z['lower_exact'])<=Q(z['upper_exact'])<Q(hi)
assert Q(B['delta']['upper_exact'])<0 and Q(B['beta']['lower_exact'])>0 and Q(B['d']['lower_exact'])>0
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_HEX_SYMBOLIC_SYSTEM_AND_IV220_REQUIRES_ACTUAL_REVIEW','code_sha256':sha(Path(__file__)),'arb_json_sha256':sha(E/'arb.json'),'parent_pin_count':len(parent['files']),'values_exact':{n:str(v) for n,v in vals.items()},'formal_identities':{n:str(v) for n,v in identities.items()},'iv220':B,'interval_pairs':9,'strict_decimal_windows':A['strict_decimal_windows'],'scope':'Frozen operator scalar application only. Analytic semigroup/domain/inverse claims are supplied by PROOF.md.'}
with (E/'iv.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','interval_pairs','strict_decimal_windows']}))

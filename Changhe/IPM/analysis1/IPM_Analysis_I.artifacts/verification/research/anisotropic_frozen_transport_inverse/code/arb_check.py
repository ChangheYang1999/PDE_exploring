from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import os,json,hashlib,sys
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[n]='1'
sys.dont_write_bytecode=True
import numpy as np
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/anisotropic_frozen_transport_inverse';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def aq(q):return arb(q.numerator)/q.denominator
def ends(v):
 def f(z):m,e=z.man_exp();return Q(int(m))*Q(2)**int(e)
 return {'lower_exact':str(f(v.lower())),'upper_exact':str(f(v.upper()))}
def decimal_integer(n,places=12):
 u=abs(n);den=10**places;return ('-' if n<0 else '')+str(u//den)+'.'+str(u%den).zfill(places)
start=datetime.now(timezone.utc).isoformat();pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['proof_sha256'];parent='research/higher_center_weight_quasimodes/evidence/verdict.json';assert sha(R/parent)=='cfa4a0b1a83aa34df06362a7d47a3d642c0a4cdde6927e4b022419dbd7958ec8';v=load(R/parent)
for n,h in v['files'].items():assert sha(R/n)==h,n
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';hp=R/'data_exact/modal_v2.json';assert sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874';assert sha(hp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
with np.load(npz,allow_pickle=False) as z:k=Q.from_float(float(z['k']))
a=Q(6);s=Q(153,50);mu=a+s-1;ell=1/k;alpha=1-2*ell;beta=4*ell-1;d=6*ell-2;delta=Q(97,50)-Q(19,25)*ell;p=(beta*mu-1)/d;q=(1-alpha*mu)/d;inv=-1/delta
assert 0<k<Q(1,2) and beta>0 and d==beta-alpha>0 and delta<0
assert p+q==mu and alpha*p+beta*q==1;assert p-(a-Q(1,2))==delta/d and q-(s-Q(1,2))==-delta/d
assert delta==alpha*(a-Q(1,2))+beta*(s-Q(1,2))-1
vals={'ell':ell,'alpha':alpha,'beta':beta,'d':d,'p':p,'q':q,'delta':delta,'inverse_bound':inv,'axis_margin_p_minus_a_plus_half':p-a+Q(1,2)}
kA=aq(k);lA=1/kA;alphaA=1-2*lA;betaA=4*lA-1;dA=6*lA-2;deltaA=aq(Q(97,50))-aq(Q(19,25))*lA
Avals={'ell':lA,'alpha':alphaA,'beta':betaA,'d':dA,'p':(betaA*aq(mu)-1)/dA,'q':(1-alphaA*aq(mu))/dA,'delta':deltaA,'inverse_bound':-1/deltaA,'axis_margin_p_minus_a_plus_half':deltaA/dA}
B={n:ends(z) for n,z in Avals.items()};windows={}
for n,qv in vals.items():
 assert Q(B[n]['lower_exact'])<=qv<=Q(B[n]['upper_exact']);floor=qv.numerator*10**12//qv.denominator;l,u=decimal_integer(floor-1),decimal_integer(floor+1);assert Q(l)<Q(B[n]['lower_exact'])<=Q(B[n]['upper_exact'])<Q(u);windows[n]=[l,u]
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_NPZ_FROZEN_SCALARS_AND_ARB512_REQUIRES_INDEPENDENT_CHECK','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'parent_path':parent,'parent_sha256':sha(R/parent),'parent_status':v['status'],'parent_files':v['files'],'parent_pin_count':len(v['files']),'npz':{'path':str(npz.relative_to(R)),'sha256':sha(npz)},'hex_json':{'path':str(hp.relative_to(R)),'sha256':sha(hp)},'inputs_exact':{'k':str(k),'a':str(a),'s':str(s),'mu':str(mu)},'values_exact':{n:str(qv) for n,qv in vals.items()},'arb512':B,'strict_decimal_windows':windows,'scope':'Exact frozen central coefficients and the specified logarithmic space only; no full IPM operator estimate.'}
with (E/'arb.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'windows':windows,'parent_pins':len(v['files'])}))

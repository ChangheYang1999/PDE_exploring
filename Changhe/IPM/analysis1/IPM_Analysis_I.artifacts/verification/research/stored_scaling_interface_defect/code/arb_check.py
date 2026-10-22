from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import os,hashlib,json,sys
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True
import numpy as np
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/stored_scaling_interface_defect';E=D/'evidence';NUM=R.parent/'ipmA-num'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def f(x):return Q.from_float(float(x))
def aa(q):return arb(q.numerator)/q.denominator
def ends(z):
 def q(v):m,e=v.man_exp();return Q(int(m))*Q(2)**int(e)
 assert z.is_finite();return {'lower_exact':str(q(z.lower())),'upper_exact':str(q(z.upper()))}
def write(p,v):
 with p.open('x') as out:json.dump(v,out,indent=2);out.write('\n')
start=datetime.now(timezone.utc).isoformat();pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['proof_sha256']
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';hexp=R/'data_exact/modal_v2.json';assert sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874';assert sha(hexp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
snap={}
for n in ['modal_fit.py','trial_green.py','trial_jets.py']:
 src=NUM/'src'/n;dest=D/'sources'/n;b=src.read_bytes()
 with dest.open('xb') as out:out.write(b)
 assert src.read_bytes()==b;snap[str(dest.relative_to(R))]={'original_path':str(src),'sha256':sha(dest)}
source=(D/'sources/modal_fit.py').read_text();assert 'self.tmin, self.t0 = float(self.knots[0]), float(self.knots[-1])' in source
with np.load(npz,allow_pickle=False) as z:
 S=z['S'];M,nb=S.shape;assert (M,nb)==(260,1565) and int(z['p'])==7 and z['knots'].shape==(1573,)
 for n,shape in [('D',(260,7)),('Ei',(260,7)),('Aout',(260,10)),('Eo',(260,7))]:assert z[n].shape==shape
 knots=[f(v) for v in z['knots']];a,b=knots[0],knots[-1];assert all(v==a for v in knots[:8]) and all(v==b for v in knots[-8:]);assert all(x<=y for x,y in zip(knots,knots[1:]));assert a<knots[8] and knots[-9]<b
 Ji=[Q(m==0)+sum(map(f,z['D'][m]),Q(0))+f(z['Ei'][m,0])-f(S[m,0]) for m in range(M)]
 Jo=[sum(map(f,z['Aout'][m]),Q(0))+f(z['Eo'][m,0])-f(S[m,-1]) for m in range(M)]
assert all(Ji) and all(Jo)
P=lambda v:v[0]/4+(v[1]-v[2]-v[3])/8
T=lambda v:v[0]/4-v[2]/8
pi,po=P(Ji),P(Jo);ti,to=T(Ji),T(Jo)
inner=-aa(a*2).exp()*aa(pi);outer=aa(b*2).exp()*aa(po);sigma=inner+outer
source_diff=(aa(2*a).exp()*aa(ti+pi)-aa(2*b).exp()*aa(to+po))/4
vals={'inner_strain_term':inner,'outer_strain_term':outer,'Sigma_K_pw':sigma,'Sigma_source_minus_canonical':source_diff}
A={n:ends(v) for n,v in vals.items()};assert not sigma.contains(0) and not source_diff.contains(0)
out={'utc':datetime.now(timezone.utc).isoformat(),'start_utc':start,'status':'PASS_EXACT_NPZ_JUMPS_AND_ARB512_INTERFACE_MOMENTS_REQUIRES_INDEPENDENT_CHECK','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'npz':{'path':str(npz.relative_to(R)),'sha256':sha(npz)},'hex_json':{'path':str(hexp.relative_to(R)),'sha256':sha(hexp)},'source_snapshots':snap,'shapes':{'M':M,'nb':nb,'degree':7},'a_exact':str(a),'b_exact':str(b),'join_inner_minus_spline':[str(v) for v in Ji],'join_outer_minus_spline':[str(v) for v in Jo],'nonzero_inner':sum(v!=0 for v in Ji),'nonzero_outer':sum(v!=0 for v in Jo),'P_inner':str(pi),'P_outer':str(po),'F1_inner':str(ti),'F1_outer':str(to),'arb512':A,'scope':'Literal unjoined dyadics and ideal source-only convention. Exactly joined canonical trial excluded.'}
write(E/'arb.json',out)
print(json.dumps({'utc':out['utc'],'status':out['status'],'nonzero_joins':[out['nonzero_inner'],out['nonzero_outer']],'moments':{n:z.str(24) for n,z in vals.items()}}))

"""Restrict the accepted r^5 majorant to a smaller disk, in two engines."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];IV='69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc'
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x,engine):
 if engine=='arb':assert x.is_finite();lo,hi=dy(x.lower()),dy(x.upper())
 else:assert not iv.isnan(x) and not iv.isinf(x);lo,hi=map(rf,x._mpi_)
 assert 0<=lo<=hi;return lo,hi

def run(T=F(7)):
 t=time.monotonic();T=F(T);assert T>=F(5,2);ctx.prec=384;iv.dps=160
 vp=B/'research/inner_majorant/evidence/verdict.json';assert sha(vp)==IV;v=json.loads(vp.read_text());assert v['status']=='CONFIRMED'
 paths=['research/inner_majorant/PROOF.md','research/inner_majorant/evidence/inner_result.json','research/inner_majorant/evidence/inner_iv_audit.json','research/inner_majorant/evidence/exact_inner_coefficients.json']
 for p in paths:assert sha(B/p)==v['files'][p]
 old,ind=[json.loads((B/p).read_text()) for p in paths[1:3]];B5=max(F(next(c for c in d['cases'] if c['T_exact']=='5/2')['values']['B5']['upper_exact']) for d in [old,ind]);assert B5>0
 co=json.loads((B/paths[3]).read_text());ta=F(co['ta_exact']);L=F(old['L_exact']);k=F(old['k_exact']);assert L>0 and 0<k<F(1,2)
 ar=aa(ta-T).exp();au=ar/aa(L);aw=aa(B5)*ar**5;am=au**3*(1+au*au)**aa((k-3)/2);awm=aw/am
 ir=iv.exp(iq(ta-T));iu=ir/iq(L);iw=iq(B5)*iv.exp(iq(5*(ta-T)));iwm=iq(B5*L**3)*iv.exp(iq(2*(ta-T))+iq((3-k)/2)*iv.log(1+iu*iu))
 a={'W':aw,'W_over_m':awm};i={'W':iw,'W_over_m':iwm}
 for d in [F(0),F(1,2),F(1,2)-k]:a['weighted_'+str(d)]=awm*(1+au)**aa(d);i['weighted_'+str(d)]=iwm*iv.exp(iq(d)*iv.log(1+iu))
 a['L2_squared']=arb.pi()*awm**2*aa(L*L/2)*(1+au*au).log()
 i['L2_squared']=iv.pi*iwm**2*iq(L*L/2)*iv.log1p(iu*iu)
 values={}
 for key in a:
  al,ah=ends(a[key],'arb');il,ih=ends(i[key],'iv');assert max(al,il)<=min(ah,ih)
  values[key]={'arb':{'lower_exact':str(al),'upper_exact':str(ah)},'iv':{'lower_exact':str(il),'upper_exact':str(ih)},'upper_exact':str(max(ah,ih))}
 return {'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_REQUIRES_SOURCE_REVIEW','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/inner_cells/PROOF.md'),'inner_verdict_sha256':IV,'dependency_pins':{p:sha(B/p) for p in paths},'T_exact':str(T),'base_majorant_T_exact':'5/2','B5_upper_exact':str(B5),'ta_exact':str(ta),'L_exact':str(L),'k_exact':str(k),'values':values,'overlap_checks':len(values),'Arb_bits':384,'iv_dps':160,'seconds':time.monotonic()-t,'scope':'Complete disk tau<=-T, using the already accepted uniform B5 at T=5/2. No recomputation of canonical moments or B5 is claimed. Scalar evaluation uses different W/m factorizations, and log versus log1p for the area integral.'}
if __name__=='__main__':
 r=run();p=B/'research/inner_cells/evidence/tail7.json';p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'values':{k:float(F(v['upper_exact'])) for k,v in r['values'].items()}}))

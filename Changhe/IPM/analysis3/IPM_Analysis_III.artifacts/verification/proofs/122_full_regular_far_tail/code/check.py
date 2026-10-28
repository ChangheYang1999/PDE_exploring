import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,hashlib,time
from flint import arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('tailbase',LANE/'proofs/120_far_tail_certificate/code/check.py');B=importlib.util.module_from_spec(sp);sp.loader.exec_module(B)
P=B.P;G=B.G;aa=B.aa;ANG=B.ANG

def cosine_poly(v,N):
 co=[arb(0)]*(2*N+1);co[N]=v[0]
 for j in range(1,len(v)):co[N+j]=co[N-j]=v[j]/2
 return arb_poly(co)
def cross(p,q,mm,N):
 prod=p*q
 return prod[2*N]+sum((2*prod[2*N+j]*aa(mm[j]) for j in range(1,2*N+1)),arb(0))
def main():
 ctx.prec=512;ctx.threads=1;start=time.monotonic();d=B.lightweight();cache=G.load_cache(d)
 k=d.k;ell=1/aa(k);a0=k-3;ae=k-7;b0=k-1
 h=G.density_eps(d,'outer');pe,qe,_,_=G.outer_eps(d,cache)
 reg=set(d.alphas);vreg={e+2 for e in reg}
 hm=[G.EP({e:p for e,p in x.terms.items() if e not in reg}) for x in h]
 dhm=[x.scale(3)+x.deriv() for x in hm];dh=[x.scale(3)+x.deriv() for x in h]
 lhm=[x.scale(3*ell-1)+x.deriv().scale(ell) for x in hm]
 pr=[G.EP({e:p for e,p in x.terms.items() if e in vreg}) for x in pe];qr=[G.EP({e:p for e,p in x.terms.items() if e in vreg}) for x in qe]
 px=[G.EP({e:p for e,p in x.terms.items() if e not in vreg}) for x in pe];qx=[G.EP({e:p for e,p in x.terms.items() if e not in vreg}) for x in qe]
 coeff={}
 def add(e,row):
  out=coeff.setdefault(e,[arb(0)]*523)
  for j,v in enumerate(row):out[j]+=v
 for i,e in enumerate(d.alphas):
  hv=[r[i] for r in d.A]
  if e!=a0:add(e,[aa((3+e)/k-1)*x for x in hv])
  for f in d.alphas:
   pv=[x.terms[f+2][0] for x in pr];qv=[x.terms[f+2][0] for x in qr]
   row=P.residual_sines(hv,[aa(e)*x for x in hv],pv,qv,arb(0))
   for j,x in enumerate(hv):row[j]+=x
   add(e+f+2,row)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'density_term':i,'seconds':time.monotonic()-start}),flush=True)
 keys=sorted(coeff,reverse=True);assert keys[0]==2*k-4 and all(2*e+F(27,4)<0 for e in keys)
 gam=[];qs=[];mass=ANG.beta_mass();mm=ANG.moments(1044)
 for e in keys:
  co=P.cofactor(coeff[e]);gam.append(ANG.axis(co));qs.append(ANG.quotient(co))
 ref=json.loads((LANE/'proofs/117_far_residual_leading_term/evidence/check.json').read_text())
 assert gam[0].overlaps(arb(ref['axis_coefficient_tau']['ball']))
 assert (mass*ANG.normalized_square(qs[0],mm)).overlaps(arb(ref['remainder_coefficient_tau']['ball']))
 N=max(len(q) for q in qs)-1;polys=[cosine_poly(q,N) for q in qs];gram={}
 for i in range(len(keys)):
  for j in range(i+1):gram[i,j]=mass*cross(polys[i],polys[j],mm,N)
 print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'regular_exponents':len(keys),'gram_ready':True,'seconds':time.monotonic()-start}),flush=True)
 cn=aa(4*522**4*(2*522+1));rerr=2*ae+F(27,4);rows=[]
 for T in [F(18),F(20),F(25),F(30)]:
  shift=T-d.tp;er=arb(0);ej=arb(0)
  for i,e in enumerate(keys):
   for j in range(i+1):
    f=keys[j];fac=(aa(F(27,4)*T+(e+f)*shift)).exp()/aa(-(e+f+F(27,4)))
    if i!=j:fac*=2
    er+=fac*gram[i,j];ej+=fac*gam[i]*gam[j]
  assert er>0 and ej>0
  raw=B.total(lhm,ae,shift)+B.total(pr,b0,shift)*B.total(dhm,F(-6),shift)+B.total(px,F(-4),shift)*B.total(dh,a0,shift)+B.total(qr,b0,shift)*B.total(hm,F(-6),shift,True)+B.total(qx,F(-4),shift)*B.total(h,a0,shift,True)
  de=cn*raw*(aa(F(27,8)*T)).exp()/aa(-rerr).sqrt()
  rr=B.tailpair(er.sqrt(),mass.sqrt()*de);yy=B.tailpair((er+ej).sqrt(),(1+mass).sqrt()*de)
  row={'T':str(T),'regular_remainder_energy':G.rec(er),'regular_axis_energy':G.rec(ej),'raw_error_bound':G.rec(raw),'remainder':rr,'full_Y':yy};rows.append(row)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'T':str(T),'rem':er.str(18),'relative_error':yy['relative_error_bound']['ball'],'full_lower':yy['energy_lower']['ball'],'full_upper':yy['energy_upper']['ball'],'seconds':time.monotonic()-start}),flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','bits':512,'original_sha256':d.sha,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'regular_exponents':[str(e) for e in keys],'rows':rows,'seconds':time.monotonic()-start}
 (ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':'PASS','seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()

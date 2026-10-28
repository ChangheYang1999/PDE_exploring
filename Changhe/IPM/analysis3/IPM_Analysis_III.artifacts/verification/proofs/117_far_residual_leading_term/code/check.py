import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,hashlib,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('far_check',LANE/'proofs/105_residual_norm_point_audit/code/check_points.py');P=importlib.util.module_from_spec(sp);sp.loader.exec_module(P)
G=P.G;ANG=P.ANG;aa=P.aa
ctx.prec=512;ctx.threads=1;start=time.monotonic();d=G.M.Data();G.check_hash(d);cache=G.load_cache(d)
k=d.k;ell=1/aa(k);a0=k-3;a1=2*k-4;fac=(2*aa(d.tp)).exp()
A=[row[0] for row in d.A];B=[row[1] for row in d.A]
pp=[];qq=[]
for n in range(1,262):
    i=A[n-1]/aa(a0+2*n+4);j=A[n]/aa(2*n-4-a0)
    pp.append(n*fac*(j-i));qq.append(fac*(n*(j+i)-(A[n]+A[n-1])/2))
pe,qe,_,_=G.outer_eps(d,cache)
for n in range(261):
    assert (pe[n].terms[k-1][0]-pp[n]).contains(0)
    assert (qe[n].terms[k-1][0]-qq[n]).contains(0)
S=P.residual_sines(A,[aa(a0)*v for v in A],pp,qq,arb(0))
for j in range(len(A)):S[j]+=A[j]+(1-ell)*B[j]
bs=P.cofactor(S);gam=ANG.axis(bs);q=ANG.quotient(bs);mm=ANG.moments(1044)
ER=ANG.beta_mass()*ANG.normalized_square(q,mm);assert ER>0
scale=(-2*aa(a1)*aa(d.tp)).exp();rate=4*k-F(5,4)
maxj=max(range(len(S)),key=lambda j:float(S[j].abs_upper()))
results=[]
for t in [F(33,4),F(30)]:
    rh,drh,pv,qv,_=P.point(d,cache,t);ss=P.residual_sines(rh,drh,pv,qv,ell)
    b=P.cofactor(ss);ga=ANG.axis(b);qu=ANG.quotient(b)
    wt=(aa(F(27,4)*t)).exp();ee=ANG.beta_mass()*ANG.normalized_square(qu,mm)
    pred=scale*ER*(aa(rate*t)).exp()
    results.append({'t':str(t),'axis':G.rec(wt*ga**2),'remainder':G.rec(wt*ee),'leading_remainder':G.rec(pred),'remainder_ratio_to_leading':G.rec(wt*ee/pred)})
    print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'t':str(t),'axis':(wt*ga**2).str(18),'rem':(wt*ee).str(18),'ratio':(wt*ee/pred).str(18),'seconds':time.monotonic()-start}),flush=True)
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','precision_bits':512,'original_sha256':d.sha,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'alpha0':str(a0),'alpha1':str(a1),'physical_degree':str(2*k-1),'energy_rate':str(rate),'tplus':str(d.tp),'axis_coefficient_tau':G.rec(gam),'remainder_coefficient_tau':G.rec(ER),'axis_coefficient_t':G.rec(scale*gam**2),'remainder_coefficient_t':G.rec(scale*ER),'nonzero_sine_index':maxj,'nonzero_sine_coefficient':G.rec(S[maxj]),'points':results,'seconds':time.monotonic()-start}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({key:out[key] for key in ['date','status','energy_rate','remainder_coefficient_t','seconds']}),flush=True)

import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,shutil,importlib.util
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];ctx.prec=256;ctx.threads=1
p=LANE.parent/'s2-num/work/fsec_ang.py';shutil.copy2(p,ROOT/'evidence/source/fsec_ang.py');spec=importlib.util.spec_from_file_location('padding_ang',ROOT/'evidence/source/fsec_ang.py');A=importlib.util.module_from_spec(spec);spec.loader.exec_module(A)
def aa(f):f=F(f);return arb(f.numerator)/f.denominator
def rec(v):return {'ball':v.str(60),'lower':str(v.lower().fmpq()),'upper':str(v.upper().fmpq())}
I0=2*arb.pi().sqrt()*aa(F(1,4)).gamma()/aa(F(3,4)).gamma();beta=aa(F(3,2)).gamma()*aa(F(1,4)).gamma()/aa(F(7,4)).gamma();exactG11=8*beta;rows=[]
for nm in [531,533]:
 nq=nm-2;mom=np.empty(2*nq+3);mom[0]=float(I0)
 for j in range(1,len(mom)):mom[j]=-mom[j-1]*(2*j-1.5)/(2*j-.5)
 ii=np.arange(nq)[:,None];jj=np.arange(nq)[None,:];AH=.5*(mom[abs(ii-jj)]-mom[ii+jj+1]);M4,DIV=A.div_cos4(nm);rr=[];qcols=[]
 for m in [1,2]:
  g=A.factor_cos2m_modes(nm,m)-(-1)**m*A.x2y_modes(nm);q,res=DIV(g);qex=np.zeros(nq);qex[0]=2 if m==1 else -6
  if m==2:qex[1]=2
  diff=[F.from_float(float(v))-F.from_float(float(e)) for v,e in zip(q,qex)];l2=sum((v*v for v in diff),F(0));err=aa(l2).sqrt();assert err>aa(F(1,10**9));qcols.append(q)
  rr.append({'m':m,'coefficient_error_l2_exact':rec(err),'max_coefficient_error':str(max(abs(v) for v in diff)),'division_residual_float':float(res),'weighted_gram_diagonal_float':float(q@AH@q),'leading_coefficients_float':q[:8].tolist()})
 qmat=np.array(qcols).T;C=qmat.T@AH@qmat;rows.append({'nm':nm,'nq':nq,'templates':rr,'angular_gram_float':C.tolist(),'G11_relative_error_float':float(C[0,0]/float(exactG11)-1)})
obs=json.loads((ROOT/'evidence/check.json').read_text())['m1_S1_comparison'];pred=rows[1]['angular_gram_float'][0][0]/rows[0]['angular_gram_float'][0][0]-1
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED_NUMERICAL_DIVISION_ERROR','rows':rows,'exact_G11':rec(exactG11),'predicted_m1_G_change':pred,'observed_m1_G_relative_frobenius':obs['G_relative_frobenius_difference'],'difference_prediction_error':abs(abs(pred)-obs['G_relative_frobenius_difference']),'scope':'computed double pseudoinverse coefficients interpreted as exact binary rationals, compared against exact polynomial quotient; no exact operator singular value','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'snapshot_sha256':hashlib.sha256((ROOT/'evidence/source/fsec_ang.py').read_bytes()).hexdigest()}
assert obj['difference_prediction_error']<1e-12
(ROOT/'evidence/angular_padding.json').write_text(json.dumps(obj,indent=2)+'\n')
print('predicted G ratio change',pred,'observed',obs['G_relative_frobenius_difference'])
for row in rows:print(row['nm'],[(r['m'],r['coefficient_error_l2_exact']['ball'],r['division_residual_float']) for r in row['templates']])

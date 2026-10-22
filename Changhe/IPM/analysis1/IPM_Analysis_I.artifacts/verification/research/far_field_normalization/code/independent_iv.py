"""Separate mpmath.iv arithmetic, direct exact JSON parsing, no strain_arb imports."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,re,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
BASE=Path(__file__).resolve().parents[3];iv.dps=70
raw=json.loads((BASE/'data_exact/x3.json').read_text());cert=json.loads((BASE/'research/canonical_inverse/evidence/strain_arb_20_32_result.json').read_text())
def exact(v):return F.from_float(float.fromhex(v))
def v(q):return iv.mpf(q.numerator)/q.denominator
# Parse the printed endpoint enclosures as exact decimal intervals, independent of Arb.
def decimal_bounds(text):
 text=text.strip('[]');parts=text.split(' +/- ');mid=F(parts[0]);rad=F(parts[1]) if len(parts)>1 else F(0);return mid-rad,mid+rad
def exported_hull(row):
 lo=decimal_bounds(row['lower'])[0];hi=decimal_bounds(row['upper'])[1];return iv.mpf([v(lo).a,v(hi).b])
k=v(exact(raw['scalars_hex']['k']));L=v(exact(raw['scalars_hex']['L']));p=6+2*k/(2-k)
coeff=[exact(x) for x in raw['z_hex']];knots=[exact(x) for x in raw['spline_knots_hex']];M=raw['integers']['angular']+1;n=raw['integers']['degree'];count=raw['integers']['singular'];assert count==6
modes=[]
for m in range(M):modes.append([F(0)]+[coeff[1+m*n+i] for i in range(n)])
tail=coeff[1+M*n:];assert len(tail)==count and tail==coeff[-6:]
Csum=sum((max(map(abs,row)) for row in modes),F(0));Ct=sum(map(abs,tail),F(0));Ctp=sum((j*j*abs(c) for j,c in enumerate(tail)),F(0))
Ds=[]
for row in modes:Ds.append(max(F(7)*abs(row[i+1]-row[i])/(knots[i+8]-knots[i+1]) for i in range(n)))
Bp=((p-2)/p)**((p-2)/2)*2/p;Mbound=iv.exp(v(Csum)+v(Ct)*Bp)
H=3-k+(1-k)*v(sum(Ds,F(0)))+v(sum((max(map(abs,row)) for row in modes[2:]),F(0)))+Bp*(p*v(Ct)+2*(1-k)*v(Ctp))
c=exported_hull(cert['strain']);a=iv.sqrt((3/k-1)/c);newL=L*a;dist=Mbound*H*iv.ln(a)*iv.exp((3-k)*iv.ln(a))
# Exact cos(2*m*pi/4), separately reduced modulo four.
cs=[1,0,-1,0];S0=v(sum((cs[m%4]*modes[m][-1] for m in range(M)),F(0)))+iv.power(2,-p/2)*v(sum(tail,F(0)))
theta0=iv.power(L,3-k)*iv.power(2,-iv.mpf(3)/2)*iv.exp(S0);leading=(k*(1+c)/3-1)*theta0
pub={'L_star':('7.65142460388744','7.65142460388754'),'weighted_factor_distance_bound':('0','0.00001477'),'Theta0_at_pi_over_4':('90.81020983980597','90.81020983980599'),'canonical_residual_leading_coefficient_at_pi_over_4':('-0.00000005592854','-0.00000005592647')}
results={'L_star':newL,'weighted_factor_distance_bound':dist,'Theta0_at_pi_over_4':theta0,'canonical_residual_leading_coefficient_at_pi_over_4':leading,'H1':H,'M':Mbound,'a':a}
for name,(lo,hi) in pub.items():assert results[name].a>=iv.mpf(lo) and results[name].b<=iv.mpf(hi),(name,str(results[name]))
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256((BASE/'data_exact/x3.json').read_bytes()).hexdigest(),'precision_decimal_digits':iv.dps,'method':'mpmath.iv; exact Fraction input and coefficient maxima; no imports from the Arb implementation','values':{key:str(value) for key,value in results.items()},'public_outward_bounds':pub,'verdict':'CONFIRMED'}
(BASE/'research/far_field_normalization/evidence/independent_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

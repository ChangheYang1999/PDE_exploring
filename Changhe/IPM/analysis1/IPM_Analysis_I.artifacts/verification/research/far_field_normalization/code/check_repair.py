"""Outward normalization repair and its weighted factor distance, exact X3 input."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from strain_arb import Data,aa,jsball
ctx.prec=192;ctx.threads=1;d=Data();raw=d.raw
cp=BASE/'research/canonical_inverse/evidence/strain_arb_20_32_result.json';ch=hashlib.sha256(cp.read_bytes()).hexdigest()
assert ch=='16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db'
scalar=json.loads(cp.read_text())['strain'];c=arb(scalar['lower']).union(arb(scalar['upper']));target=3/d.k-1
assert target>c and c>0 and d.k>0 and d.k<1
factor=(target/c).sqrt();logfactor=factor.log();newL=d.L*factor
z=[F.from_float(float.fromhex(v)) for v in raw['z_hex']];nr=raw['integers']['degree'];nm=d.nm
co=[[F(0)]+z[1+m*nr:1+(m+1)*nr] for m in range(nm)]
assert len(co[0])==len(d.t)-8
cms=[max(map(abs,row)) for row in co];derivs=[]
for row in co:
 derivs.append(max(F(7)*abs(row[i+1]-row[i])/(d.t[i+8]-d.t[i+1]) for i in range(nr)))
ctprime=sum((j*j*abs(z[-6+j]) for j in range(6)),F(0))
Rs=(1-d.k)*aa(sum(derivs,F(0)))+aa(sum(cms[2:],F(0)))+d.bp*(d.p*d.ct+2*(1-d.k)*aa(ctprime))
H1=3-d.k+Rs;distance=d.global_M*H1*logfactor*((3-d.k)*logfactor).exp()
Saxis45=sum((aa(row[-1])*[1,0,-1,0][m%4] for m,row in enumerate(co)),arb(0))+arb(2)**(-d.p/2)*sum(d.tc,arb(0))
theta0=d.L**(3-d.k)*arb(2)**(-arb(3)/2)*Saxis45.exp();leading=(d.k*(1+c)/3-1)*theta0
assert leading<0
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':d.sha,'scalar_certificate_sha256':ch,'c_target':jsball(target),'scale_ratio_a':jsball(factor),'log_scale_ratio':jsball(logfactor),'L_star':jsball(newL),'L_star_minus_L':jsball(newL-d.L),'canonical_cl_k_minus_one':jsball(d.k*(1+c)/3-1),'Theta0_at_pi_over_4':jsball(theta0),'canonical_residual_leading_coefficient_at_pi_over_4':jsball(leading),'spline_derivative_maxima_sum_exact':str(sum(derivs,F(0))),'radial_log_derivative_bound_H1':jsball(H1),'weighted_factor_distance_bound':jsball(distance),'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','scope':'Scalar repair and far-field leading residual only, not a full residual norm or a solution.'}
(BASE/'research/far_field_normalization/evidence/repair_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
spec={'base_exact_data':'x3.json','base_exact_data_sha256':d.sha,'change':'Replace only scale L by L_star. All other exact dimensionless inputs remain those in x3.json.','exact_definition':'L_star = L * sqrt((3/k - 1)/c0), where c0 is the canonical scalar strain integral of the exact base X3 density. Take the positive square root.','scalar_definition_reference':'../research/canonical_inverse/PROOF.md','scalar_enclosure_reference':'../research/canonical_inverse/evidence/strain_arb_20_32_result.json','certified_enclosure_L_star':out['L_star'],'not_a_binary64_assignment':True,'error_bound_reference':'../research/far_field_normalization/evidence/repair_bounds.json'}
(BASE/'data_exact/x3_scalar_repair.json').write_text(json.dumps(spec,indent=2)+'\n');print(json.dumps(out),flush=True)

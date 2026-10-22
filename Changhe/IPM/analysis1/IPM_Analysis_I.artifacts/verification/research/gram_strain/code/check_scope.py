from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_strain'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
prompt=B/'PROMPT.md';text=prompt.read_text();wanted=[r'\boxed{3c_l-c=1,\qquad c_l=\frac{1+\psi_{xy}(0,0)}3.}',r'\boxed{c[h]=\frac13\,\psi[h]_{xy}(0,0),\quad -\Delta\psi[h]=\partial_x h.}'];bindings=[]
for w in wanted:
 assert text.count(w)==1;bindings.append({'text':w,'line':text[:text.index(w)].count('\n')+1})
# Affine coefficients ordered(c_l,Sigma,constant), acting on x^2 y.
x=(1,-1,0);y=(1,1,0);action=tuple(2*a+b for a,b in zip(x,y));assert action==(3,-1,0)
# Norm majorant at gamma=k+1/2-delta has exponent -1-2delta.
# Affine ordering(k,delta,constant).
growth=(1,-1,F(1,2));weight=(-2,0,-2);radial=tuple(2*a+b for a,b in zip(growth,weight));assert radial==(0,-2,-1)
a=json.loads((D/'evidence/compute.json').read_text());b=json.loads((D/'evidence/independent.json').read_text());assert b['status']=='PASS_INDEPENDENT_FOURIER_BETA_MACHIN_INTEGER_ROOT_AND_OUTPUT_AUDIT'
for r in [a,b]:
 for n,h in r['files'].items():assert sha(B/n)==h,n
assert F(a['public']['speed_variation']['strict_upper_exact'])==F('0.001268515316')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PROMPT_NORMALIZATION_AND_SCOPE_ALGEBRA','prompt_bindings':bindings,'center_action_cl_sigma_constant':action,'far_majorant_k_delta_constant':list(map(str,radial)),'files':{str(p.relative_to(B)):sha(p) for p in [prompt,D/'ADDENDUM.md',D/'evidence/compute.json',D/'evidence/independent.json',Path(__file__)]}}
p=D/'evidence/scope_check.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],sha(p))

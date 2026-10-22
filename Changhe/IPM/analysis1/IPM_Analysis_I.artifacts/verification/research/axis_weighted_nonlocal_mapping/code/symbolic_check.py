from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
sys.dont_write_bytecode=True
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/axis_weighted_nonlocal_mapping';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def read_poly(d,vars):return sum(S.Rational(v)*S.prod(x**int(e) for x,e in zip(vars,key.split(','))) for key,v in d.items())
start=datetime.now(timezone.utc).isoformat();A=load(E/'fraction.json');assert sha(D/'PROOF.md')==A['proof_sha256'] and sha(D/'code/fraction_check.py')==A['code_sha256'];parent=load(R/A['parent_path']);assert sha(R/A['parent_path'])==A['parent_sha256'] and parent['files']==A['parent_files']
for n,h in parent['files'].items():assert sha(R/n)==h,n
u,v,U,V=S.symbols('u v U V',real=True);kernel=S.expand(S.det(S.Matrix([[u,v],[U,V]]))**2);assert S.expand(kernel-read_poly(A['gram_square_kernel'],[u,v,U,V]))==0
AA,BB,DD=S.symbols('A B D',real=True);integ=kernel.subs({u**2:AA,U**2:AA,v**2:DD,V**2:DD}).subs(u*v,BB).subs(U*V,BB);assert S.expand(integ-2*(AA*DD-BB**2))==0;assert S.expand(integ-read_poly(A['gram_double_integral'],[AA,BB,DD]))==0
matrix=S.Matrix([[AA,BB],[BB,DD]]);vec=S.Matrix([-BB/AA,1]);proj=S.simplify(matrix*vec);assert proj[0]==0 and S.cancel(proj[1]-(AA*DD-BB**2)/AA)==0;assert S.expand(AA*proj[1]-read_poly(A['fifth_projection_cleared'],[AA,BB,DD]))==0
z,a,b=S.symbols('z a b');laurent=a*(z**3-z**-3)/(2*S.I)+b*(z**5-z**-5)/(2*S.I);polynomial=S.Poly(S.expand(2*S.I*z**5*laurent),z);assert polynomial.coeff_monomial(z**10)==b and polynomial.coeff_monomial(z**8)==a;assert S.solve(polynomial.all_coeffs(),[a,b])=={a:0,b:0}
x,y,C=S.symbols('x y C',real=True);stream=C*S.im(S.expand((x+S.I*y)**4))/4;velocity=S.Matrix([-S.diff(stream,y),S.diff(stream,x)]);rho=x**2*y;image=S.expand(velocity.dot(S.Matrix([S.diff(rho,x),S.diff(rho,y)])));assert S.expand(image-C*read_poly(A['degree_five_image_divided_by_C'],[x,y]))==0
axis=S.diff(image,x,2).subs(x,0);assert axis==10*C*y**3 and S.expand(axis-C*read_poly(A['axis_second_derivative_divided_by_C'],[x,y]))==0;assert image.subs(x,0)==0 and S.diff(image,x).subs(x,0)==0
for i in range(2):assert S.expand(velocity[i]-C*read_poly(A['velocity_cubic'][i],[x,y]))==0
for row in A['sine_parities']:
 n=row['sine_mode'];sn=S.im(S.expand((x+S.I*y)**n));assert S.expand(sn-read_poly(row['numerator'],[x,y]))==0 and S.expand(sn.subs(x,-x)-sn)==0 and S.expand(sn.subs(y,-y)+sn)==0
weight_a=S.symbols('a',real=True);threshold=S.solve_univariate_inequality(4-2*weight_a<=-1,weight_a);assert threshold.as_set()==S.Interval(S.Rational(5,2),S.oo)
n=S.symbols('n',nonzero=True);assert S.simplify(((n-1)-(n-1))/(4*n))==0 and S.simplify(((n-1)+(n+1))/(4*n))==S.Rational(1,2)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_SYMPY_LAURENT_GRAM_AXIS_CHECKS_REQUIRES_ACTUAL_REVIEW','code_sha256':sha(Path(__file__)),'fraction_json_sha256':sha(E/'fraction.json'),'parent_pin_count':len(parent['files']),'gram_determinant':str(matrix.det()),'exact_zero_third_projection':str(proj[0]),'exact_positive_fifth_projection_formula':str(proj[1]),'frequency_independence_solution':{'a':'0','b':'0'},'quartic_stream':str(stream),'degree_five_image':str(image),'axis_second_derivative':str(axis),'threshold':str(threshold),'scope':'Symbolic identities and parent pins only. No finite matrix sample, numerical integral or spectral evidence is used.'}
with (E/'symbolic.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))

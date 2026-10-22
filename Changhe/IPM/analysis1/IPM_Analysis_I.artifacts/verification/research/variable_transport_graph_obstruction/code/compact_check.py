from pathlib import Path
import sys,os
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import sympy as S
R=Path(__file__).resolve().parents[3];P=R/'research/variable_transport_graph_obstruction';E=P/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();proof=E/'compact_proof_first.json';assert p.load(proof)['proof_sha256']==p.sha(P/'COMPACT_VELOCITY_PROOF.md')=='1079a79a6995ed608fc21d60e221c90a3e9d253ca3fc6574456d0b3752d63342'
x,y,beta,A,D,n=S.symbols('x y beta A D n',positive=True);z=S.symbols('z',real=True);bb=S.Function('b');b=bb(S.log(x),y);phase=D*S.log(x)+A*S.log(y);f=x**beta*b*S.exp(S.I*n*phase);base=x**beta*S.exp(S.I*n*phase)
bz=S.Subs(S.Derivative(bb(z,y),z),z,S.log(x));bzz=S.Subs(S.Derivative(bb(z,y),z,z),z,S.log(x));by=S.diff(b,y);byy=S.diff(b,y,y)
Rphi=D*D/x**2+A*A/y**2;B1=D/x**2*(2*bz+(2*beta-1)*b)+2*A/y*by-A/y**2*b;B0=(bzz+(2*beta-1)*bz+beta*(beta-1)*b)/x**2+byy
lap=S.expand((S.diff(f,x,x)+S.diff(f,y,y))/base);checks={};checks['complete_cartesian_laplacian']=S.simplify(lap-(-n*n*Rphi*b+S.I*n*B1+B0));checks['unoscillated_log_laplacian']=S.simplify(lap.subs(n,0)-B0)
u1=S.expand(-S.diff(f,x,y)/base);u2=S.expand(S.diff(f,x,x)/base);checks['leading_velocity_1']=S.simplify(u1.coeff(n,2)-D*A*b/(x*y));checks['leading_velocity_2']=S.simplify(u2.coeff(n,2)+D*D*b/x**2);checks['canonical_curl_identity']=S.simplify(S.diff(S.diff(f,x,x),x)-S.diff(-S.diff(f,x,y),y)-S.diff(S.diff(f,x,x)+S.diff(f,y,y),x));checks['canonical_divergence_identity']=S.simplify(S.diff(-S.diff(f,x,y),x)+S.diff(S.diff(f,x,x),y))
assert all(v==0 for v in checks.values()),checks
out={'start_utc':start,'utc':p.now(),'status':'PASS_DIRECT_CARTESIAN_COMPACT_POTENTIAL_IDENTITIES','proof_sha256':p.sha(P/'COMPACT_VELOCITY_PROOF.md'),'code_sha256':p.sha(Path(__file__)),'symbolic_identities':{n:str(v) for n,v in checks.items()},'scope':'Analytic canonical uniqueness and norm/domain statements require the full proof; no such claim follows from symbolic zero checks.'};p.write(E/'compact_check.json',out);print(out)

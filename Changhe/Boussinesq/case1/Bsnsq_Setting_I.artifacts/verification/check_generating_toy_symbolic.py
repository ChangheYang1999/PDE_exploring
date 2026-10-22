"""Exact physical-Laplacian manufacture with an explicitly invertible chart."""
from pathlib import Path
import datetime,hashlib,json
import sympy as s
x,e,y,a=s.symbols('x e y a',real=True)
G=x*e+e**3+x*x*e
Y=s.diff(G,x);A=s.diff(Y,e);B=s.diff(Y,x)
eta=y/(1+2*x)
p=3*x*Y+e*s.diff(G,e)-6*G
P=s.factor(p.subs(e,eta));Theta=a*eta
U1=-s.diff(P,y);U2=s.diff(P,x);O=-s.diff(P,x,2)-s.diff(P,y,2)
M=5*s.diff(G,e)-e*s.diff(G,e,2);V=M/A
formula=(1+B*B)/A*s.diff(V,e)-B*s.diff(V,x)-(s.diff(B,x)-B*s.diff(A,x)/A)*V-e*(s.diff(A,x)-B*s.diff(A,e)/A)+B
checks={'chart_inverse':s.simplify(Y.subs(e,eta)-y),'Omega_formula':s.simplify(formula.subs(e,eta)-O),'W1':s.simplify(V.subs(e,eta)-(3*x+U1)),'W2':s.simplify((B*V+e*A).subs(e,eta)-(3*y+U2)),'temperature_transport':s.simplify((3*x+U1)*s.diff(Theta,x)+(3*y+U2)*s.diff(Theta,y)-Theta),'divergence':s.simplify(s.diff(U1,x)+s.diff(U2,y))}
assert all(v==0 for v in checks.values())
out=Path('candidate_audits/lead_snap48/vorticity_refined/toy_symbolic.json')
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'G':str(G),'physical_Psi':str(P),'physical_Omega':str(s.factor(O)),'checks':{k:str(v) for k,v in checks.items()},'passed':True,'scope':'Local chart x>-1/2; symbolic verification of generating-coordinate differential identities using direct physical derivatives, not a Boussinesq solution or canonical full-plane example.'}
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))

"""Own exact finite-order tests for P230, after its full informal proof."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,hashlib,time
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks={};values={}
root=Path(__file__).resolve().parents[1];v=root/'research/230_finite_axis_jet_obstruction/verification'
def eq(name,a,b=0):
 d=s.factor(s.cancel(s.expand(a-b)));checks[name]=d==0;values[name]=str(d)
def truth(name,x):checks[name]=bool(x)
k,y,x=s.symbols('k y x',real=True);beta=s.symbols('beta',positive=True);A0=s.symbols('A0',nonzero=True)
alpha=(beta-2)/2;L=1+3*beta/2;a=s.Function('a')(y);phi=s.Function('phi')(y)
# Axis equation independently from general even/odd Taylor fields.
f=s.Function('f')(y);theta=x*x*f/2;w2=phi+x*x*s.Function('z')(y);w1=x*(2*beta-s.diff(phi,y))
axis=s.expand(w1*s.diff(theta,x)+w2*s.diff(theta,y)-(beta-2)*theta).coeff(x,2)*2
eq('axis_temperature_equation',axis,phi*s.diff(f,y)+(3*beta+2-2*s.diff(phi,y))*f)
eq('axis_scale_equation',axis.subs(f,A0/a**2).doit()*a**2/(-2*A0),s.diff(phi,y)+phi*s.diff(a,y)/a-L)
N=s.symbols('N',integer=True,positive=True);M=2*N+4
eq('residual_vanishing_order_exceeds_degree',M-1-(2*N+1),2)
truth('M_at_least8',M.subs(N,2)>=8)
# Test exact even cutoffs at ordinary exponents and the endpoint beta8.
for b,n,m in [(s.Rational(3),8,20),(s.Rational(4),6,16),(s.Rational(5),4,12),(s.Rational(8),4,12),(s.Rational(9),2,8),(s.Rational(5,2),14,32)]:
 cut=3*b/(b-2);nn=2*s.floor(cut/2)
 truth(f'beta{b}_N',nn==n);truth(f'beta{b}_M',2*nn+4==m)
 truth(f'beta{b}_strict_next_even',nn<=cut<nn+2)
 for j in range(int(nn)+2,2*int(nn)+3,2):truth(f'beta{b}_jet{j}_strict_gap',j*(s.Rational(1,2)-1/b)-s.Rational(3,2)>0)
# Exact division identity for a general smooth finite remainder, at two orders.
for m in (8,12):
 E=s.Function('E')(k,y);V=s.Function('V')(k,y);S=A0*k*k/2+k**(m+2)*E
 Q=a*((beta-2)*S-V*s.diff(S,y))/s.diff(S,k)
 quotient=a*(-alpha*m*E-alpha*k*s.diff(E,k)-V*s.diff(E,y))/(A0+k**m*((m+2)*E+k*s.diff(E,k)))
 eq(f'M{m}_smooth_division_quotient',(Q-a*alpha*k)/k**(m+1),quotient)
# Physical differentiation and exact polynomial degrees on two nontrivial fixtures.
records={}
for nn,b in [(2,s.Integer(9)),(4,s.Integer(5))]:
 m=2*nn+4;aa=1+y*y;AA=y+y**3/3;kk=x/aa;al=(b-2)/2;ll=1+3*b/2
 P=-s.Rational(3,7)*k*k+(s.Rational(2,11)*k**4 if nn==4 else 0);g=1+2*y+y*y
 D=ll*AA+P;vp2=D/aa;vp1=aa*al*k+k*s.diff(aa,y)*vp2
 # The perturbation is exactly divergence free, and begins at the claimed orders.
 dv2=k**m*g/aa;dq=-k**(m+1)*s.diff(g,y)/(m+1);dv1=dq+k*s.diff(aa,y)*dv2
 def dx(f):return s.diff(f,k)/aa
 def dy(f):return s.diff(f,y)-k*s.diff(aa,y)/aa*s.diff(f,k)
 eq(f'N{nn}_comparison_divergence',dx(vp1)+dy(vp2),2*b)
 eq(f'N{nn}_perturbation_divergence',dx(dv1)+dy(dv2))
 op=dy(vp1)-dx(vp2);od=dy(dv1)-dx(dv2)
 BB=s.diff(aa,y,2)/aa-2*s.diff(aa,y)**2/aa**2
 eq(f'N{nn}_physical_curl_formula',op,ll*k*s.diff(aa,y)+k*D*BB-(1+k*k*s.diff(aa,y)**2)*s.diff(P,k)/aa**2)
 pp=s.diff(aa,y)/aa;pn=s.expand(P).coeff(k,nn)
 rpoly=s.expand(aa*(vp1*dx(op)+vp2*dy(op)+op-2*k/aa))
 # A0=2 in these fixtures.
 eq(f'N{nn}_highest_residual_coefficient',rpoly.coeff(k,2*nn+1),pn**2*(s.diff(pp,y,2)-2*(nn+1)*pp*s.diff(pp,y)))
 truth(f'N{nn}_residual_degree_bound',s.Poly(rpoly,k).degree()<=2*nn+1)
 # O(k^(M-1)) is sharp for the vorticity and can be sharp for the residual.
 odpoly=s.Poly(s.expand(od),k);low=min(mon[0] for mon in odpoly.monoms());truth(f'N{nn}_curl_remainder_order',low==m-1)
 rd=s.expand(aa*((vp1+dv1)*dx(op+od)+(vp2+dv2)*dy(op+od)+(op+od)-2*k/aa)-rpoly)
 rdpoly=s.Poly(rd,k);lowR=min(mon[0] for mon in rdpoly.monoms());truth(f'N{nn}_residual_remainder_order',lowR==m-1)
 truth(f'N{nn}_all_comparison_coefficients_protected',lowR>2*nn+1)
 # Temperature need not equal the comparison off axis. It agrees to order M.
 S=k*k+y*k**(m+2);physT=s.expand((vp1+dv1)*dx(S)+(vp2+dv2)*dy(S)-(b-2)*S)
 lowT=min(mon[0] for mon in s.Poly(physT,k).monoms());truth(f'N{nn}_temperature_residual_order',lowT>=m+2)
 for order in range(4,m+1,2):eq(f'N{nn}_finite_temperature_jet{order}',s.diff(S,k,order).subs(k,0))
 first=s.diff(S,k,m+2).subs(k,0);eq(f'N{nn}_first_uncontrolled_jet',first,s.factorial(m+2)*y)
 truth(f'N{nn}_not_separable_ratio',s.diff(first,y)!=0)
 records[str(nn)]={'M':m,'curl_order':low,'residual_order':lowR,'temperature_defect_order':lowT,'polynomial_degree':s.Poly(rpoly,k).degree()}
 print('fixture',nn,records[str(nn)],flush=True)
# Independent general Riccati linearization.
n=s.symbols('n',integer=True,positive=True);K=s.symbols('K');p=s.diff(a,y)/a;vv=a**(-(n+1))
eq('Riccati_linearization',(s.diff(vv,y,2)+(n+1)*K*vv)/vv,-(n+1)*(s.diff(p,y)-(n+1)*p*p-K))
truth('proof_precedes_controls',json.loads((v/'proof_before_checks.json').read_text())['written_utc']<start)
end=datetime.now(timezone.utc).isoformat();data={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-t0,'checks':checks,'all_passed':all(checks.values()),'differences':values,'fixtures':records,'proof_sha256':hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite symbolic fixtures verify remainder arithmetic, not existence. General-order proof is in PROOF.md. No numerics-lane or lead code.'}
(v/'checks.json').write_text(json.dumps(data,indent=2,default=str)+'\n');print(json.dumps({q:data[q] for q in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('checks',len(checks),'failed',[q for q,w in checks.items() if not w])

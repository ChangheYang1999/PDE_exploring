"""Annular duality certificate. Exact source algebra plus Arb tail majorants."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import sys,json,hashlib,time
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'05_tails'/'verification'))
sys.path.insert(0,str(BASE/'02_energy'/'verification'))
from check_tail import density_stream,advection,add_sine
from farfield_matrix_certificate import A,differentiate,binomial
ctx.prec=768
sys.set_int_max_str_digits(0)
start=time.monotonic()
d=json.loads((BASE/'source_audit/state131_exact.json').read_text())
c=Q(d['exact_parameters']['cl']);g=1/c;delta=1-g;qlead=2*g-1
# Reconstruct the canonical coefficient vector again from the original JSON.
sys.path.insert(0,str(BASE/'source_audit'))
from recover_state import LOW,HIGH,CANON,INDEX,qhex,taylor_generator
original=Path('case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json')
raw=original.read_bytes();assert hashlib.sha256(raw).hexdigest()==d['source_json_sha256']
snapshot=json.loads(raw);low=list(map(qhex,snapshot['P_hex']))
assert c==low[0]
strain=[4*taylor_generator(*ijk,c).get((2,2),Q(0)) for ijk in LOW]
low[0]=(1-c-sum((u*v for u,v in zip(strain[1:],low[1:])),Q(0)))/strain[0]
restored=[Q(0)]*860
for v,ijk in zip(low,LOW):restored[INDEX[ijk]]+=v
norms=list(map(qhex,snapshot['frozen_Nn_hex']))
for v,(j,m,n) in zip(map(qhex,snapshot['high_hex']),HIGH):
 for k in range(n+1):restored[INDEX[j,m,max(5,m)+k]]+=v*norms[n]*(-1)**(n-k)*comb(n,k)*comb(n+k,k)
coeff=list(map(Q,d['canonical_coefficients']))
assert restored==coeff and CANON==list(map(tuple,d['canonical_order']))
params=[(3+g-j*delta)/2 for j in range(4)]
assert len(coeff)==len(d['canonical_order'])==860
assert all(abs(params[j]-k)<26 and 2*m<=18 for j,m,k in d['canonical_order'])
assert all(abs(g+3-j*delta)+2*m+6<32 for j,m,k in d['canonical_order'])
absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,d['canonical_order']) if jj==j),Q(0)) for j in range(4)]
cut=1;R=arb(2)**32;dens={};stream={};powers={};field={3:[],4:[]}
for j in range(4):
 for a in range(cut+1):
  C={}
  for v,(jj,m,k) in zip(coeff,d['canonical_order']):
   if jj==j:C[2*m]=C.get(2*m,Q(0))+v*binomial(params[j]-k,a)
  p=g-j*delta-2*a;powers[j,a]=p
  dens[j,a],stream[j,a]=density_stream(C,p+3)
  deriv={(0,0):{('c',n):v for n,v in C.items() if v}}
  for order in range(1,5):
   for nx in range(order+1):
    ny=order-nx;prev=deriv[nx-1,ny] if nx else deriv[nx,ny-1]
    deriv[nx,ny]=differentiate(prev,p+4-order,'x' if nx else 'y')
   if order>=3:
    bound=max(sum(map(abs,deriv[nx,order-nx].values()),Q(0)) for nx in range(order+1))
    field[order].append((j,a,bound))
E={}
for key,F in dens.items():E[key]={n:(c*powers[key]-1)*v for n,v in F.items() if (c*powers[key]-1)*v}
for (i,a),P in stream.items():
 for (j,b),F in dens.items():
  out=E.setdefault((i+j+1,a+b),{})
  for n,v in advection(P,F,powers[i,a]+1,powers[j,b]).items():add_sine(out,n,v)
E={k:{n:v for n,v in F.items() if v} for k,F in E.items() if any(F.values())}
ep={k:g-k[0]*delta-2*k[1] for k in E}
assert all(p<=qlead for p in ep.values())
assert [k for k,p in ep.items() if p==qlead]==[(1,0)]
prior=json.loads((BASE/'05_tails/verification/state131_tail.json').read_text())
assert E[1,0]=={int(n):Q(v) for n,v in prior['E_coefficients']['1'].items()}
a0=cut+1;M={};T={};ratios={}
for order in [3,4]:
 M[order]=sum((A(v)*R**A(-j*delta-2*a) for j,a,v in field[order]),arb(0))
 ratio=A(Q(a0+26,a0+1)*Q(2*a0+34,2*a0+32)**order)/R**2
 assert ratio<1;ratios[order]=ratio
 T[order]=A(comb(a0+25,a0)*(2*a0+32)**order)*R**(-2*a0)*sum((A(absj[j])*R**A(-j*delta) for j in range(4)),arb(0))/(1-ratio)
Ctail=(2*arb(2).sqrt()*A(c)*T[4]+2*T[3])*R**A(delta)+4*(T[3]*M[4]+M[3]*T[4]+T[3]*T[4])
# Independent exact polynomial integrations, without hard-coded integral results.
chi=[Q(4),Q(-12),Q(13),Q(-6),Q(1)]
def mul(x,y):
 z=[Q(0)]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]+=a*b
 return z
def integ(x):return sum((a*Q(2**(i+1)-1,i+1) for i,a in enumerate(x)),Q(0))
deriv=[i*chi[i] for i in range(1,len(chi))]
assert integ(chi)==Q(1,30) and integ(mul(chi,chi))==Q(1,630)
assert integ([Q(0)]+mul(deriv,deriv))==Q(1,35)
rows=[];pairing_sum=arb(0);energy_sum=Q(0)
for m in sorted(E[1,0]):
 assert m%2==1
 B=sum((A(abs(F.get(m,Q(0))))*R**A(ep[k]-qlead) for k,F in E.items() if ep[k]<qlead),arb(0))
 b=A(abs(E[1,0][m]))-B-2*Ctail
 assert b>0
 dm=Q(1,35)+Q(m*m,630)
 pairing_sum+=A(abs(E[1,0][m])/dm)*b
 energy_sum+=E[1,0][m]**2/dm
 low=arb.pi().sqrt()*b*R**A(qlead+2)*arb(5)**A(Q(-11,10))/(30*A(Q(1,35)+Q(m*m,630)).sqrt())
 high=arb(2)**A(Q(53,2))*low/6
 exponent=0
 while high>arb(2)**(exponent+1):exponent+=1
 rows.append({'m':m,'leading_coefficient':str(E[1,0][m]),'nonleading_upper':B.str(60),'signed_coefficient_lower':b.str(60),'L_lower':low.str(60),'N_lower':high.str(60),'certified_N_greater_than_2_power':exponent})
 print('mode',m,'L lower',low.str(12),'N lower',high.str(12),'power',exponent,flush=True)
assert rows
best=max(rows,key=lambda x:x['certified_N_greater_than_2_power'])
combined_low=arb.pi().sqrt()*pairing_sum*R**A(qlead+2)*arb(5)**A(Q(-11,10))/(30*A(energy_sum).sqrt())
combined_high=arb(2)**A(Q(53,2))*combined_low/6
combined_power=0
while combined_high>arb(2)**(combined_power+1):combined_power+=1
assert combined_power>=82
print('COMBINED',combined_low.str(30),combined_high.str(30),'power',combined_power,flush=True)
# Independently evaluate the complete potential by Cartesian jets at large points.
from field_eval import State
full=State(131,768);point_checks=[]
for scale,xx,yy in [(1,Q(0),Q(1)),(1,Q(3,5),Q(4,5)),(2,Q(5,13),Q(12,13))]:
 rr=scale*R;X=rr*A(xx);Y=rr*A(yy);z=acb(A(xx),A(yy))
 trunc=sum((rr**A(ep[k])*sum((A(v)*(z**n).imag for n,v in es.items()),arb(0)) for k,es in E.items()),arb(0))
 exact=full.evaluate(X,Y)['residual'];err=abs(exact-trunc)/rr**A(qlead)
 assert err.is_finite() and err<Ctail
 point_checks.append({'scale':scale,'x_over_r':str(xx),'y_over_r':str(yy),'exact_residual':exact.str(60),'normalized_error':err.str(60)})

files=['17_weight_radius/RESIDUAL_PROOF.md','17_weight_radius/PROOF.md','16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md','source_audit/state131_exact.json','source_audit/recover_state.py','source_audit/field_eval.py','05_tails/verification/check_tail.py','02_energy/verification/farfield_matrix_certificate.py']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED V089','state':131,'canonical_sha256':d['canonical_serialization_sha256'],'source_sha256':d['source_json_sha256'],'precision_bits':ctx.prec,'Q':cut,'R':str(2**32),'gamma':str(g),'q':str(qlead),'M':{str(k):v.str(60) for k,v in M.items()},'T':{str(k):v.str(60) for k,v in T.items()},'tail_ratio':{str(k):v.str(60) for k,v in ratios.items()},'pointwise_tail_error_coefficient':Ctail.str(60),'rows':rows,'best_single_mode_power':best['certified_N_greater_than_2_power'],'combined_L_lower':combined_low.str(60),'combined_N_lower':combined_high.str(60),'best_power_lower_bound':combined_power,'gap_power_lower_bound':combined_power+46,'point_checks':point_checks,'dependencies':{f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
sectors={'powers':{str(k):str(v) for k,v in ep.items()},'coefficients':{str(k):{str(n):str(v) for n,v in F.items()} for k,F in E.items()},'derivative_bounds':{str(d):[[j,a,str(v)] for j,a,v in rows] for d,rows in field.items()}}
Path(__file__).with_name('annular_residual_sectors.json').write_text(json.dumps(sectors,indent=2)+'\n')

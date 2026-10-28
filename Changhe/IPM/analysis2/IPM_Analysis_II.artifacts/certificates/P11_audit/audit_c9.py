"""Independent C9 combined annular certificate; no numerics code imported."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import sys,json,hashlib,time
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'05_tails'/'verification'))
sys.path.insert(0,str(BASE/'02_energy'/'verification'))
from check_tail import density_stream,advection,add_sine
from farfield_matrix_certificate import A,differentiate,binomial
ctx.prec=384
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
cut=int(sys.argv[1]) if len(sys.argv)>1 else 3
assert cut in [3,4]
R=arb(2)**19;dens={};stream={};powers={};field={3:[],4:[]}
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

def tail(R):
 a0=cut+1;M={};T={};ratios={}
 for order in [3,4]:
  M[order]=sum((A(v)*R**A(-j*delta-2*a) for j,a,v in field[order]),arb(0))
  ratio=A(Q(a0+26,a0+1)*Q(2*a0+34,2*a0+32)**order)/R**2
  assert ratio<1;ratios[order]=ratio
  T[order]=A(comb(a0+25,a0)*(2*a0+32)**order)*R**(-2*a0)*sum((A(absj[j])*R**A(-j*delta) for j in range(4)),arb(0))/(1-ratio)
 C=(2*arb(2).sqrt()*A(c)*T[4]+2*T[3])*R**A(delta)+4*(T[3]*M[4]+M[3]*T[4]+T[3]*T[4])
 cross=sum((sum((A(abs(v)) for v in es.values()),arb(0))*R**A(ep[k]-qlead) for k,es in E.items() if k[1]>cut),arb(0))
 return C+cross,{'derivative_tail':{str(k):v.str(60) for k,v in T.items()},'ratio':{str(k):v.str(60) for k,v in ratios.items()},'cross_sector_error':cross.str(60)}

# Independent log-coordinate quadrature of the combined test.
chi=[Q(4),Q(-12),Q(13),Q(-6),Q(1)]
def multiply(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def exact_integral(poly):return sum((v*Q(2**(i+1)-1,i+1) for i,v in enumerate(poly)),Q(0))
square=multiply(chi,chi);dc=[i*chi[i] for i in range(1,len(chi))]
assert exact_integral([Q(0)]+multiply(dc,dc))==Q(1,35)
log2=arb(2).log()
I=A(square[0])*log2+sum((A(v*Q(2**i-1,i)) for i,v in enumerate(square) if i),arb(0))
am={m:e/(Q(1,35)+Q(m*m,630)) for m,e in E[1,0].items()}
norm=(arb.pi()*sum((A(a*a)*(A(Q(1,35))+m*m*I) for m,a in am.items()),arb(0))).sqrt()
prod=Path('numerics/data/wnorm_cert_multi_131.json')
producer_bytes=prod.read_bytes();pd=json.loads(producer_bytes)
assert norm.overlaps(arb(pd['normDphi_ball']))
C={k:sum((a*F.get(m,Q(0)) for m,a in am.items()),Q(0)) for k,F in E.items() if k[1]<=cut}
C={k:v for k,v in C.items() if v}
ints={}
for power in set(ep[k] for k in C)|{qlead}:
 def integrand(z,analytic):
  t=z.exp();weight=(-arb(11)/10*(1+(2*z).exp()).log(analytic=analytic)).exp()
  return weight*(t-1)**2*(2-t)**2*(A(power+2)*z).exp()
 integral=acb.integral(integrand,0,log2)
 assert integral.is_finite() and integral.imag.contains(0) and integral.real>0
 ints[power]=integral.real
print('energy integrals',I.str(35),A(Q(1,35)).str(25),'norm',norm.str(40),flush=True)
rows=[]
for rp in [31,32,35]:
 R=arb(2)**rp;Ct,td=tail(R)
 pair=arb.pi()*sum((A(v)*R**A(ep[k]+2)*ints[ep[k]] for k,v in C.items()),arb(0))
 rem=4*Ct*sum((A(abs(v)) for v in am.values()),arb(0))*R**A(qlead+2)*ints[qlead]
 assert pair>rem
 low=(pair-rem)/norm;high=arb(2)**A(Q(53,2))*low/6
 Lint=int(low.lower().floor().unique_fmpz());Nint=int(high.lower().floor().unique_fmpz())
 assert low>Lint and high>Nint
 pp=pd['results']['2^'+str(rp)]
 if cut==3:assert pair.overlaps(arb(pp['pairing_ball']))
 assert low>arb(pp['L_lower_pub']) and low>arb(pp['L_lower_int'])
 assert high>arb(pp['N_lower_pub_2^26.5_over_6'])
 mantissa,exponent=pp['L_lower_exact_binary_man_exp']
 assert isinstance(exponent,int) and str(int(mantissa))==mantissa
 saved_binary=A(Q(int(mantissa))*(Q(2)**exponent))
 upper_quotient=(pair+rem)/norm
 binary_verdict=('CONFIRMED lower endpoint' if saved_binary<low else 'REFUTED lower endpoint of this test' if saved_binary>upper_quotient else 'OPEN with this independent remainder')
 if cut==4:
  base_record=json.loads(Path(__file__).with_suffix('.json').read_text())
  base_row=next(r for r in base_record['rows'] if r['R_power']==rp)
  assert abs(pair-arb(base_row['pairing']))<rem+arb(base_row['remainder'])
  assert saved_binary<low
 row={'R_power':rp,'tail_majorant':Ct.str(65),'pairing':pair.str(65),'remainder':rem.str(65),'L_witness_lower':low.str(65),'N_witness_lower':high.str(65),'strict_L_integer_lower':Lint,'strict_N_integer_lower':Nint,'producer_pairing_overlap':bool(pair.overlaps(arb(pp['pairing_ball']))),'producer_published_lower_bounds_confirmed':True,'tail_details':td,'producer_binary_lower_man_exp':pp['L_lower_exact_binary_man_exp'],'producer_binary_verdict':binary_verdict,'binary_excess_over_quotient_upper':(saved_binary-upper_quotient).str(65)}
 rows.append(row)
 print('R',rp,'L>',Lint,'N>',Nint,'producer passes',flush=True)
files=['numerics_audit/C9_PROOF.md','numerics_audit/C8_PROOF.md','source_audit/state131_exact.json','source_audit/recover_state.py','05_tails/verification/check_tail.py','02_energy/verification/farfield_matrix_certificate.py','20_real_velocity/RESIDUAL_PROOF.md']
assert prod.read_bytes()==producer_bytes, 'Producer record changed during audit'
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED independent C9 lower bounds','precision_bits':ctx.prec,'source_sha256':d['source_json_sha256'],'canonical_sha256':d['canonical_serialization_sha256'],'producer_record_sha256':hashlib.sha256(producer_bytes).hexdigest(),'Q':cut,'angular_integral':I.str(65),'gradient_norm':norm.str(65),'rows':rows,'radial_integrals':{str(p):v.str(65) for p,v in ints.items()},'exact_sector_pairings':{str(k):str(v) for k,v in C.items()},'dependencies':{f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
destination=Path(__file__).with_suffix('.json') if cut==3 else Path(__file__).with_name(Path(__file__).stem+'_Q4.json')
if cut==4:
 out['dependencies']['numerics_audit/BINARY_ENDPOINT_PROOF.md']=hashlib.sha256((BASE/'numerics_audit/BINARY_ENDPOINT_PROOF.md').read_bytes()).hexdigest()
 out['dependencies']['numerics_audit/'+Path(__file__).stem+'.json']=hashlib.sha256(Path(__file__).with_suffix('.json').read_bytes()).hexdigest()
 out['all_binary_endpoints_independently_confirmed']=True
destination.write_text(json.dumps(out,indent=2)+'\n')
print('DONE',out['seconds'],flush=True)

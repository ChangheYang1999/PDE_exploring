"""Fresh exact N-B reconstruction, Laurent residuals and annular duality.
All computation is serial. No numerical producer code is imported.
"""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import sys,json,hashlib,time
from flint import fmpq as Q,arb,acb,ctx
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'13_algebraic_repair/verification'))
from audit_repair import clean,add,cosine,derivative,derivatives,conv
sys.path.insert(0,str(BASE/'source_audit'))
import recover_state as rec
sys.path.insert(0,str(BASE/'11_residual_norms/verification'))
from audit_norms import direct_chi
ctx.prec=768
AB=lambda x:arb(str(x))

def choose(b,n):
 ans=Q(1)
 for k in range(n):ans*= (b-k)/(k+1)
 return ans

def reconstruct(name):
 source=Path('numerics/data')/(name+'.json')
 raw=source.read_bytes();d=json.loads(raw);c=Q(d['cl']);A={}
 for row in d['generators']:
  j,m=row['j'],row['m'];spec=row['spec'];v=Q(row['coef'])
  if spec[0]=='mono':terms={spec[1]:Q(1)}
  else:
   assert spec[0]=='leg';w,n=spec[1:]
   terms={w+h:Q((-1)**(n-h)*comb(n,h)*comb(n+h,h)) for h in range(n+1)}
  for h,b in terms.items():
   key=j,m,m+h;A[key]=A.get(key,Q(0))+v*b
 A=clean(A)
 serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(A.items()))+'\n'
 sh=hashlib.sha256(serial.encode()).hexdigest();rh=hashlib.sha256(raw).hexdigest()
 old=json.loads((BASE/'19_nb_candidates/verification'/(name+'.audit.json')).read_text())
 assert sh==old['canonical_sha256'] and rh==old['source_sha256']
 assert c==Q(4076476460239181,2251799813685248)
 assert all(0<=j<=5 and 0<=m<=59 and m<=k<=75 for j,m,k in A)
 return c,A,{'source_sha256':rh,'canonical_sha256':sh,'generator_count':len(d['generators']),'canonical_count':len(A),'old_audit':old}

def sectors(A,c,Qcut=3):
 g=1/c;delta=1-g;pj={j:(3+g-j*delta)/2 for j in range(6)}
 assert all(abs(pj[j]-k)<76 and abs(3+g-j*delta)+2*m+6<128 for j,m,k in A)
 moments={(j,q):{} for j in range(6) for q in range(Qcut+1)}
 for (j,m,k),v in A.items():
  for q in range(Qcut+1):
   M=moments[j,q];M[m]=M.get(m,Q(0))+v*choose(pj[j]-k,q)
 moments={k:clean(v) for k,v in moments.items()}
 rho={};vel={};grad={};powers={};bounds={3:[],4:[]}
 for key,M in moments.items():
  j,q=key;s=3+g-j*delta-2*q;H=cosine(M);p=s-3;powers[key]=p
  # Store the actual density as i*rho and stream function as i*psi.
  # A y derivative introduces a further i, whose square contributes -1.
  rho[key]=add((-1,derivatives(H,s,'xxy')),(1,derivatives(H,s,'yyy')))
  psi=derivatives(H,s,'xy')
  vel[key]=(derivative(psi,p+1,'y'),derivative(psi,p+1,'x'))
  grad[key]=(derivative(rho[key],p,'x'),derivative(rho[key],p,'y'))
  for d in (3,4):
   value=max(sum((abs(v) for v in derivatives(H,s,'x'*nx+'y'*(d-nx)).values()),Q(0)) for nx in range(d+1))
   bounds[d].append((j,q,value))
 E={key:add((c*powers[key]-1,F)) for key,F in rho.items()}
 # Laurent convolution uses exact FLINT polynomial multiplication.
 for (i,q), (ux,uy) in vel.items():
  for (j,b),(dx,dy) in grad.items():
   key=i+j+1,q+b
   E[key]=add((1,E.get(key,{})),(1,conv(ux,dx)),(-1,conv(uy,dy)))
 E={k:v for k,v in E.items() if v};ep={k:g-k[0]*delta-2*k[1] for k in E}
 pstar=g-6*delta
 assert all(p<=pstar for p in ep.values())
 assert [k for k,p in ep.items() if p==pstar]==[(6,0)]
 sine={}
 for key,F in E.items():
  assert F.get(0,Q(0))==0 and all(F.get(-m,Q(0))==-v for m,v in F.items())
  assert all(m%2 for m in F)
  sine[key]={m:-2*v for m,v in F.items() if m>0}
 return moments,sine,ep,bounds

def tails(A,c,bounds,T,Qcut=3):
 g=1/c;delta=1-g;pstar=g-6*delta;q0=Qcut+1
 absj={j:sum((abs(v) for (jj,m,k),v in A.items() if jj==j),Q(0)) for j in range(6)}
 M={};Td={};ratio={}
 for order in (3,4):
  M[order]=sum((AB(v)*T**AB(-j*delta-2*q) for j,q,v in bounds[order]),arb(0))
  ratio[order]=AB(Q(q0+76,q0+1)*Q(2*q0+130,2*q0+128)**order)/T**2
  assert ratio[order]<1
  Td[order]=AB(Q(comb(q0+75,q0)*(2*q0+128)**order))*T**(-2*q0)*sum((AB(absj[j])*T**AB(-j*delta) for j in range(6)),arb(0))/(1-ratio[order])
 assert 2*q0>g-pstar and 2*q0>2*g-1-pstar
 Ctail=(2*arb(2).sqrt()*AB(c)*Td[4]+2*Td[3])*T**AB(g-pstar)+4*(Td[3]*M[4]+M[3]*Td[4]+Td[3]*Td[4])*T**AB(2*g-1-pstar)
 return Ctail,{'component_M':{str(k):v.str(65) for k,v in M.items()},'component_T':{str(k):v.str(65) for k,v in Td.items()},'tail_ratios':{str(k):v.str(65) for k,v in ratio.items()},'Ctail':Ctail.str(65)}

def point_test(A,c,E,ep,T,Ctail):
 pstar=1/c-6*(1-1/c);rows=[]
 for xx,yy in [(Q(0),Q(1)),(Q(3,5),Q(4,5))]:
  X=T*AB(xx);Y=T*AB(yy);ch=direct_chi(A,c,X,Y)
  rho=-ch[2,1]-ch[0,3];rx=-ch[3,1]-ch[1,3];ry=-ch[2,2]-ch[0,4]
  ux=-ch[1,2];uy=ch[2,1];full=(AB(c)*X+ux)*rx+(AB(c)*Y+uy)*ry-rho
  z=acb(AB(xx),AB(yy))
  zs={m:(z**m).imag for F in E.values() for m in F}
  trunc=sum((T**AB(ep[key])*sum((AB(v)*zs[m] for m,v in F.items()),arb(0)) for key,F in E.items()),arb(0))
  err=abs(full-trunc)/T**AB(pstar)
  assert err.is_finite() and err<Ctail,('independent point tail error',err,Ctail)
  rows.append({'direction':[str(xx),str(yy)],'actual_full_residual':full.str(65),'truncated_residual':trunc.str(65),'normalized_error_upper_ball':err.str(65),'passes_uniform_remainder':True})
 return rows

def run(names):
 start=time.monotonic();rec.HERE=HERE
 rec.COPY=Path('case4/IPM_case4.artifacts')
 c0,C0,orig=rec.read_state(131);c0=Q(str(c0))
 original_m0={}
 for v,(j,m,k) in zip(C0,rec.CANON):
  if j==0:original_m0[m]=original_m0.get(m,Q(0))+Q(str(v))
 original_m0=clean(original_m0)
 common=None;results=[]
 for name in names:
  t0=time.monotonic();c,A,meta=reconstruct(name);assert c==c0
  print('RECONSTRUCTED',name,'canonical',len(A),flush=True)
  moments,E,ep,bounds=sectors(A,c)
  assert moments[0,0]==original_m0 and not moments[0,1] and not moments[1,1]
  lead=E[6,0]
  if common is None:common=lead
  else:assert lead==common
  L2=(arb.pi()*AB(sum((v*v for v in lead.values()),Q(0)))).sqrt()
  oldlead=next(x for x in meta['old_audit']['residual_sectors'] if (x['h'],x['q'])==(6,0))
  assert L2.overlaps(arb(oldlead['full_angular_L2']))
  meta.pop('old_audit')
  print('EXACT SECTORS',name,len(E),'leading L2',L2.str(18),'seconds',time.monotonic()-t0,flush=True)
  dm={m:Q(1,35)+Q(m*m,630) for m in lead}
  S=sum((v*v/dm[m] for m,v in lead.items()),Q(0));angularA=sum((abs(v)/dm[m] for m,v in lead.items()),Q(0))
  pstar=ep[6,0];cross={key:sum((v*F.get(m,Q(0))/dm[m] for m,v in lead.items()),Q(0)) for key,F in E.items() if key!=(6,0)}
  witness=[]
  for Tpower in [31,35]:
   T=arb(2)**Tpower;R=arb(2)**31;Ct,td=tails(A,c,bounds,T)
   B=sum((AB(-v)*T**AB(ep[key]-pstar) for key,v in cross.items() if v<0),arb(0))
   b=AB(S)-B-2*Ct*AB(angularA)
   assert b>0,('signed pairing not positive',name,Tpower,b,AB(S),B,Ct)
   W=(1+4*T*T/(R*R))**(arb(-11)/10)
   lower=arb.pi().sqrt()*b*T**AB(pstar+2)*W*arb(2)**AB(pstar+1)/(30*AB(S).sqrt())
   Nlower=arb(2)**(arb(53)/2)*lower/6
   exponent=0
   while Nlower>arb(2)**(exponent+1):exponent+=1
   lowint=int(lower.lower().floor().unique_fmpz());nint=int(Nlower.lower().floor().unique_fmpz())
   assert lower>lowint and Nlower>nint
   checks=point_test(A,c,E,ep,T,Ct)
   row={'T_power':Tpower,'R_power':31,'p_star':str(pstar),'finite_negative_cross_upper':B.str(65),'signed_pairing_coefficient_lower':b.str(65),'leading_energy':str(S),'angular_absolute_sum':str(angularA),'weight_lower_ball':W.str(65),'L_lower_witness_ball':lower.str(65),'N_lower_witness_ball':Nlower.str(65),'certified_L_integer_lower':lowint,'certified_N_integer_lower':nint,'certified_N_power_lower':exponent,'certified_gap_over_eta_power_lower':exponent+35,'tail':td,'independent_point_checks':checks}
   witness.append(row)
   print('CERT',name,'T',Tpower,'L>',lowint,'N>',nint,'Npower',exponent,'gap',exponent+35,flush=True)
  files=['23_admissible_tail_gap/PROOF.md','13_algebraic_repair/verification/audit_repair.py','19_nb_candidates/verification/audit_exact.py','19_nb_candidates/verification/'+name+'.audit.json','source_audit/recover_state.py','11_residual_norms/verification/audit_norms.py','11_residual_norms/verification/compact_norms.py','02_energy/verification/compact_matrix.py','18_fractional_constants/PROOF.md','16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md']
  out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED particular candidate bounds','name':name,'precision_bits':ctx.prec,**meta,'original_source_sha256':orig['source_json_sha256'],'original_canonical_sha256':orig['canonical_serialization_sha256'],'Q':3,'retained_residual_sector_count':len(E),'leading_residual_full_angular_L2':L2.str(65),'leading_sine_coefficients':{str(m):str(v) for m,v in lead.items()},'all_nonzero_sector_powers':{str(k):str(p) for k,p in ep.items()},'all_sectors_above_p_star_zero':True,'witnesses':witness,'best_certified_N_power':max(w['certified_N_power_lower'] for w in witness),'dependencies':{f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-t0}
  (HERE/(name+'.annular.json')).write_text(json.dumps(out,indent=2)+'\n')
  allsectors={'candidate':name,'source_sha256':meta['source_sha256'],'canonical_sha256':meta['canonical_sha256'],'powers':{str(k):str(v) for k,v in ep.items()},'sine_coefficients':{str(k):{str(m):str(v) for m,v in F.items()} for k,F in E.items()},'component_bounds':{str(d):[[j,q,str(v)] for j,q,v in rows] for d,rows in bounds.items()},'exact_cross_coefficients':{str(k):str(v) for k,v in cross.items()}}
  (HERE/(name+'.sectors.json')).write_text(json.dumps(allsectors,indent=2)+'\n')
  results.append({'name':name,'seconds':out['seconds'],'best_N_power':out['best_certified_N_power']})
 print('DONE',time.monotonic()-start,json.dumps(results),flush=True)
if __name__=='__main__':run(sys.argv[1:] or ['nb_stableA2_exact','nb_stableA3_exact'])

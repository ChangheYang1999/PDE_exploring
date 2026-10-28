"""Independent exact Gram tests, fresh original recovery and leading-sector check."""
from pathlib import Path
from fractions import Fraction as Rat
from datetime import datetime, timezone
import sys,json,hashlib,time
from flint import fmpq as Q, arb, ctx
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'source_audit'))
import recover_state as rec
sys.path.insert(0,str(BASE/'13_algebraic_repair/verification'))
from audit_repair import clean,add,cosine,derivative,derivatives,conv
ctx.prec=512
start=time.monotonic()

def scalar(f,g,exps):
 return sum((v*w/(exps[i]+exps[j]+1) for i,v in f.items() for j,w in g.items()),Q(0))
def subtract(f,g,c):return clean({i:f.get(i,Q(0))-c*g.get(i,Q(0)) for i in f.keys()|g.keys()})
small=[]
for values in [['-2/5','-1/5','1/10','7/5','2'],['0','1','2','5','8'],['-49/100','-48/100','-1/3','3/4','29/10','10']]:
 exps=list(map(Q,values));n=len(exps)
 # Project the first monomial on later ones, in reverse order, in exact rationals.
 later=[]
 for j in range(1,n):
  p={j:Q(1)}
  for b,bn in later:p=subtract(p,b,scalar(p,b,exps)/bn)
  bn=scalar(p,p,exps);assert bn>0;later.append((p,bn))
 residual={0:Q(1)}
 for b,bn in later:residual=subtract(residual,b,scalar(residual,b,exps)/bn)
 dsq=1/(2*exps[0]+1)
 for a in exps[1:]:dsq*=((a-exps[0])/(a+exps[0]+1))**2
 assert scalar(residual,residual,exps)==dsq
 # Separately Gram-Schmidt increasingly and inspect every dilation matrix entry.
 orth=[]
 for j in range(n):
  p={j:Q(1)}
  for b,bn in orth:p=subtract(p,b,scalar(p,b,exps)/bn)
  norm=scalar(p,p,exps);assert sum(p.values(),Q(0))**2==(2*exps[j]+1)*norm
  orth.append((p,norm))
 frob=Q(0)
 for j,(p,pn) in enumerate(orth):
  dp={k:exps[k]*v for k,v in p.items()}
  for i,(q,qn) in enumerate(orth):
   entry=scalar(dp,q,exps);sq=entry**2/(pn*qn);frob+=sq
   if i>j:assert entry==0
   elif i==j:assert entry/pn==exps[j]
   else:assert sq==(2*exps[i]+1)*(2*exps[j]+1)
 expected=sum((a*a for a in exps),Q(0))+sum(((2*exps[i]+1)*(2*exps[j]+1) for i in range(n) for j in range(i+1,n)),Q(0))
 assert frob==expected
 small.append({'exponents':values,'distance_squared':str(dsq),'dilation_Frobenius_squared':str(frob),'all_entries_exact':True})
rec.HERE=HERE;rec.COPY=Path('case4/IPM_case4.artifacts')
c0,coefs,meta=rec.read_state(131);c=Q(str(c0));gamma=1/c;delta=1-gamma
assert meta['canonical_serialization_sha256']=='4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01'
leading={}
for key,v in zip(rec.CANON,coefs):
 j,m,k=key
 if j==0:leading[m]=leading.get(m,Q(0))+Q(str(v))
leading=clean(leading)
p=BASE/'10_tail_splice/verification/state131_splice.json';td=json.loads(p.read_text())
C={int(n)-1:{int(m)//2:Q(v) for m,v in row['cosine_coefficients'].items()} for n,row in td['homogeneous_potential_orders'].items()}
assert C[0]==leading and set(C)==set(range(6))
rho={};vel={};grad={}
for j in range(6):
 s=3+gamma-j*delta;H=cosine(C[j]);power=s-3
 rho[j]=add((-1,derivatives(H,s,'xxy')),(1,derivatives(H,s,'yyy')))
 psi=derivatives(H,s,'xy');vel[j]=(derivative(psi,power+1,'y'),derivative(psi,power+1,'x'))
 grad[j]=(derivative(rho[j],power,'x'),derivative(rho[j],power,'y'))
residuals={}
for h in range(7):
 terms=[(c*(gamma-h*delta)-1,rho.get(h,{}))]
 for i in range(6):
  j=h-1-i
  if 0<=j<6:
   ux,uy=vel[i];dx,dy=grad[j];terms.extend([(1,conv(ux,dx)),(-1,conv(uy,dy))])
 E=add(*terms);residuals[h]=E
 if h<6:assert not E
assert residuals[6]
sine={m:-2*v for m,v in residuals[6].items() if m>0}
annp=BASE/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json';ann=json.loads(annp.read_text())
assert sine=={int(m):Q(v) for m,v in ann['leading_sine_coefficients'].items()}
# Independently evaluate the power set and constants as FLINT rationals.
a0=7*delta/2-2;aa=sorted({ell*delta/2+k-2 for ell in range(1,13) for k in range(155) if ell*delta/2+k-2>=a0})
assert len(aa)==1852 and aa[0]==a0>Q(-1,2)
D2=arb(1)/(2*arb(a0)+1)
for a in aa[1:]:D2*=(arb(a-a0)/arb(a+a0+1))**2
# Double pair sum via a running prefix, separately from the first program.
cd2=Q(0);prefix=Q(0)
for a in aa:cd2+=a*a+(2*a+1)*prefix;prefix+=2*a+1
cd=arb(cd2).sqrt()
H2=arb.pi()/2*D2*sum((arb(v)**2/(m*m+(1+2*cd)**2) for m,v in sine.items()),arb(0))
H=H2.sqrt();N=(1-arb(34)/2**18)*(arb(20)/21*2**18).sqrt()*H
assert H>arb('2.67750e-7') and N>arb('0.00013376') and N*1572864>210
old=json.loads((HERE/'muntz_bound.json').read_text())
assert H.overlaps(arb(old['Hminus_lower'])) and N.overlaps(arb(old['Route_U_N_lower_at_s_2minus18']))
assert cd2==Q(old['C_D_squared_exact']) and D2.overlaps(arb(old['D'])**2)
# All currently exact candidates fit the finite index set and moment contract.
candidates=[]
for name in ['nb_stableA2_exact','nb_stableA3_exact','nb_stableA4_exact','nb_stableA5_exact','nb_Mpen_exact']:
 cp=BASE/'19_nb_candidates/verification'/(name+'.audit.json');cand=json.loads(cp.read_text())
 assert all(0<=j<=5 and 0<=m<=59 and m<=k<=75 for j,m,k in cand['canonical_order'])
 assert cand['leading_six_potential_branches_equal_stationary'] and cand['first_descendant_branches_zero']==[0,1]
 candidates.append({'name':name,'audit_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'canonical_sha256':cand['canonical_sha256']})
files=[HERE.parent/'PROOF.md',HERE/'muntz_bound.py',HERE/'muntz_bound.json',p,annp,BASE/'source_audit/recover_state.py',BASE/'13_algebraic_repair/verification/audit_repair.py',BASE/'11_residual_norms/PROOF.md',BASE/'11_residual_norms/verification/compact_norms.py',BASE/'02_energy/verification/compact_matrix.py']
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED exact algebra and numerical lower bounds; lead proof review CORRECT 07:41Z','precision_bits':ctx.prec,'small_Gram_checks':small,'original_source_hash':meta['source_json_sha256'],'original_canonical_hash':meta['canonical_serialization_sha256'],'leading_sector_recomputed_from_stationary_branches':True,'stationary_lower_sectors_exact_zero':list(range(6)),'e_modes':len(sine),'e_max_mode':max(sine),'leading_full_circle_L2':(arb.pi()*sum((arb(v)**2 for v in sine.values()),arb(0))).sqrt().str(65),'Hminus_bound':H.str(65),'Route_U_N_bound':N.str(65),'ratio_to_eta':(N*1572864).str(65),'candidate_membership':candidates,'dependencies':{str(f.relative_to(BASE)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},'code_hash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

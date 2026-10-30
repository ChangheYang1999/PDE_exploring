from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import json, sys, time
from flint import fmpq as Q, arb, arb_poly, ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/weak_mesh_comparison'
sys.path.insert(0,str(ROOT/'research/projected_residual/code'))
from build import candidate_source, read_projection, destination
sys.path.insert(0,str(ROOT/'research/localized_weak_probe/code'))
from beta_scale import integral,supremum,groups,ap,ar,Radial,U
sys.set_int_max_str_digits(0)
def digest(p): return sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=2048;name='C1-N1-007-d2w-j7-e2bal'
 src=candidate_source(name)
 assert digest(src)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
 peerpath=BASE/'source/N1_007_weak_float.json'
 peer=json.loads(peerpath.read_text(),parse_float=str)
 assert peer['sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
 model=Radial(src);projected,metadata=read_projection(name)
 F=[(ell,ap(P(U))) for ell,P in projected.items()]
 bg=groups(model,['u1','u2']);cg=groups(model,['rho_x','rho_y'])
 oldpath=ROOT/f'research/projected_residual/verification/{name}_probe_2048.json'
 old={row['k']:row for row in json.loads(oldpath.read_text())['probes']}
 rows=[]
 for k in range(9):
  weight=arb_poly([5,2*k-4])
  B2=arb.pi()/2*sum((integral(P*weight*weight,b,2*k+1) for b,P in bg.items()),arb(0))
  C2=arb.pi()/2*sum((integral(P,b,2*k+1) for b,P in cg.items()),arb(0))
  a=Q(2*k+2);l0=3*model.c+1+2*model.c*k;l1=2*model.c*(k+2)
  A2=arb.pi()/2*ar((l0*l0-2*l0*l1*a/(a+2)+l1*l1*a*(a+1)/((a+2)*(a+3)))/(a*(a+1)))
  assert A2>0 and B2>0 and C2>0
  A,B,C=A2.sqrt(),B2.sqrt(),C2.sqrt();D=A+B+C
  pair=arb.pi()/2*sum((integral(P,ell*model.delta/2-1,k+1) for ell,P in F),arb(0))
  I=abs(pair);assert I>0
  H=arb(1) if k==0 else supremum(k,2)+2*k*supremum(k,3)+4*supremum(k+1,2)
  m=2*I/(D+(D*D+4*H*I).sqrt())
  vals={'pairing':pair,'I':I,'A':A,'B':B,'C':C,'D':D,'H':H,'m':m}
  keys={'I':'I_k','A':'A_k','B':'B_k','C':'C_k','D':'D_k','H':'H_k','m':'m_lower_bound'}
  diff={key:((ar(Q(str(Fraction(str(peer['NORM-T-WEAK-v1_a0'][str(k)][pk])))))-vals[key])/vals[key]).str(35) for key,pk in keys.items()}
  checks={}
  if k in old:
   for key,ok in {'pairing':'pairing','A':'A','B':'B_weighted','C':'C','D':'D','H':'gradient_sup_upper_ball','m':'L2_radius_lower'}.items():
    checks[key]=bool(vals[key].overlaps(arb(old[k][ok])))
   assert all(checks.values())
  rows.append({'k':k,'exact_balls':{key:value.str(80) for key,value in vals.items()},'peer_relative_difference':diff,'previous_exact_overlap':checks})
  print('k',k,'m',m.str(20),'peer relative',diff['m'],flush=True)
 exact_best=max(rows,key=lambda row:float(arb(row['exact_balls']['m']).mid()))
 paths=[src,destination(name),oldpath,peerpath,BASE/'source/N1_weak_tests.py',Path(__file__),BASE/'PROOF.md',ROOT/'research/projected_residual/PROOF.md',ROOT/'research/localized_weak_probe/PROOF.md',ROOT/'research/localized_weak_probe/BETA_EVALUATION.md',ROOT/'research/projected_residual/code/build.py',ROOT/'research/localized_weak_probe/code/beta_scale.py',ROOT/'research/localized_weak_probe/code/evaluate.py',ROOT/'research/radial_fourier/code/radial.py']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':ctx.prec,'inputs':{str(p.relative_to(ROOT)):digest(p) for p in paths},'rows':rows,'best_tested_k':exact_best['k'],'best_exact_ball':exact_best['exact_balls']['m'],'elapsed_seconds':time.monotonic()-start,'status':'N4-origin, OPEN peer for new k values; matched-probe FLOAT diagnostic'}
 with (BASE/'verification/candidate007.json').open('x') as s:json.dump(out,s,indent=2);s.write('\n')
 print('DONE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

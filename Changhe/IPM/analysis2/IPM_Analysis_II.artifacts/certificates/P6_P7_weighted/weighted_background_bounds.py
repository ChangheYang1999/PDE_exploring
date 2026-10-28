"""Independent exact-sector bounds needed by the large-radius weighted theorem."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import sys,json
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'02_energy'/'verification'))
from farfield_matrix_certificate import A,add,differentiate,binomial
ctx.prec=384
CHOICES={'chi12':'xyy','chi21':'xxy','chi13':'xyyy','chi22':'xxyy','chi31':'xxxy','chi04':'yyyy','chi41':'xxxxy','chi32':'xxxyy','chi23':'xxyyy','chi14':'xyyyy','chi05':'yyyyy'}

def run(state):
 d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
 c=Q(d['exact_parameters']['cl']);gam=1/c;dr=1-gam
 assert Q(2,5)<dr<Q(1,2)
 coeff=list(map(Q,d['canonical_coefficients']));p=[(3+gam-j*dr)/2 for j in range(4)]
 assert all(abs(p[j]-k)<26 for j,m,k in d['canonical_order'])
 absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,d['canonical_order']) if j==jj),Q(0)) for j in range(4)]
 sectors={}
 for j in range(4):
  for q in range(7):
   T={}
   for v,(jj,m,k) in zip(coeff,d['canonical_order']):
    if jj==j:add(T,'c',2*m,v*binomial(p[j]-k,q))
   for label,axes in CHOICES.items():
    U=T
    for di,axis in enumerate(axes):U=differentiate(U,2*p[j]-2*q-di,axis)
    sectors[j,q,label]=sum(map(abs,U.values()),Q(0))
 R=arb(100);q0=7;norm={};tails={}
 for order in (3,4,5):
  ratio=A(Q(q0+26,q0+1)*Q(2*q0+34,2*q0+32)**order)/R**2
  assert ratio<1
  tails[order]=A(comb(q0+25,q0)*(2*q0+32)**order)*R**(-2*q0)/(1-ratio)*sum((A(absj[j])*R**A(-j*dr) for j in range(4)),arb(0))
 for label,axes in CHOICES.items():
  norm[label]=sum((A(v)*R**A(-j*dr-2*q) for (j,q,k),v in sectors.items() if k==label),arb(0))+tails[len(axes)]
 G4=((norm['chi31']+norm['chi13'])**2+(norm['chi22']+norm['chi04'])**2).sqrt()
 G5=((norm['chi41']+norm['chi23'])**2+2*(norm['chi32']+norm['chi14'])**2+(norm['chi23']+norm['chi05'])**2).sqrt()
 U3=(norm['chi12']**2+norm['chi21']**2).sqrt()
 U4=(2*norm['chi22']**2+norm['chi13']**2+norm['chi31']**2).sqrt()
 U5=(norm['chi41']**2+3*norm['chi32']**2+3*norm['chi23']**2+norm['chi14']**2).sqrt()
 fac=R**A(Q(2,5)-dr)
 far={'C_rho':fac*(G4+G5),'C_U':fac*U3,'C_DU':fac*U4,'C_D2U':fac*U5}
 local={'C_rho':R**A(Q(2,5))*(11*arb(2).sqrt()+R*77),'C_U':R**A(Q(2,5))*A(Q(14,5)),'C_DU':R**A(Q(2,5))*A(Q(14,5)),'C_D2U':R**A(Q(7,5))*35}
 target={'C_rho':2**16,'C_U':2**5,'C_DU':2**5,'C_D2U':2**15}
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,'input_sha256':d['canonical_serialization_sha256'],'precision_bits':ctx.prec,'delta':'2/5','split_radius':100,'exact_tail_cutoff':6,'binomial_majorant':26,'field_sector_coefficients':{k:v.str(55) for k,v in norm.items()},'tail_coefficients':{str(k):v.str(55) for k,v in tails.items()},'local_bounds':{k:v.str(55) for k,v in local.items()},'exterior_bounds':{k:v.str(55) for k,v in far.items()},'certified_upper_bounds':target}
 for k in target:
  assert local[k]<target[k],(state,k,'local',local[k])
  assert far[k]<target[k],(state,k,'far',far[k])
 Rbig=arb(2)**200;s=A(Q(11,5))
 error=(arb(2)**53*target['C_rho']+target['C_DU']+target['C_rho']+s*(9*target['C_U']+2*target['C_DU']+target['C_D2U']/arb(2).sqrt()))/Rbig**A(Q(2,5))
 assert error<arb(1)/5
 out['radius_2pow200_error_upper']=error.str(55)
 out['coercivity_lower']=(arb(2)/5-error).str(55)
 out['inverse_bound']=5
 Path(__file__).with_name(f'state{state:03d}_weighted_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
 print(state,'far', {k:v.str(15) for k,v in far.items()},'error',error.str(20),flush=True)
if __name__=='__main__':
 for state in (88,131):run(state)

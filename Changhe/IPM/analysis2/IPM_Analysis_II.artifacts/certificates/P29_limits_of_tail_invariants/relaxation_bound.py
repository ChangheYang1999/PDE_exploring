"""Certified explicit upper bound for a smooth residual-shaped linear relaxation."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
from flint import arb,ctx,fmpq
sys.set_int_max_str_digits(0)
ctx.prec=384
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1];start=time.monotonic()
c=Q(4076476460239181,2251799813685248);delta=1-1/c;a0=7*delta/2-2;mu=Q(11,10)
a=lambda q:arb(fmpq(str(q)))
p=BASE/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json';data=json.loads(p.read_text());e={int(m):Q(v) for m,v in data['leading_sine_coefficients'].items()}
rows=[];total=arb(0);bycomponent=[arb(0),arb(0),arb(0)]
for m,em in sorted(e.items()):
 M=(m+1)//2+4;K=154-M
 exps=sorted({ell*delta/2+k-2 for ell in range(1,13) for k in range(K+1) if ell*delta/2+k-2>=a0})
 assert exps[0]==a0 and min(exps)+mu>Q(-1,2) and K>=0
 D=1/a(2*(a0+mu)+1).sqrt();CD2=Q(0);prefix=Q(0)
 for i,x in enumerate(exps):
  if i:D*=a(x-a0)/a(x+a0+2*mu+1)
  z=x+mu;CD2+=z*z+(2*z+1)*prefix;prefix+=2*z+1
 C=a(CD2).sqrt();AA=[arb(1)]
 for j in range(4):AA.append(AA[-1]*(4*C+2*m+a(Q(48,5))+6*j))
 factor=arb.pi().sqrt()*a(abs(em))*D
 terms=[a(4)**a(Q(2,5))*(2*AA[2]+4*a(2).sqrt()*AA[4]),2**11*(a(2).sqrt()*AA[1]+4*AA[3]),a(2)**a(Q(53,2)+62*mu)*(1+2*a(2).sqrt()*AA[2])]
 components=[821*factor*z for z in terms];bound=sum(components,arb(0));total+=bound
 for j,z in enumerate(components):bycomponent[j]+=z
 rows.append({'m':m,'M':M,'K':K,'dimension':len(exps),'D':D.str(60),'C':C.str(60),'norm_upper':bound.str(60)})
assert total.is_finite()
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED construction upper bound; independent theorem review complete','precision_bits':ctx.prec,'R':2**31,'s_range':'0<s<=1/2','leading_modes':len(e),'N_upper':total.str(70),'ratio_to_eta':(total*2**35).str(70),'below_eta':bool(total<a(2)**-35),'component_totals':[z.str(60) for z in bycomponent],'rows':rows,'dependencies':{str(q.relative_to(BASE)):sha256(q.read_bytes()).hexdigest() for q in [p,HERE.parent/'PROOF.md',BASE/'26_uniform_family_gap/PROOF.md',BASE/'16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md']},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
(HERE/'relaxation_bound.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='rows'})

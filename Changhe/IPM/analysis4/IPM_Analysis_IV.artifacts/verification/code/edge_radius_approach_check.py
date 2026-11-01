"""Interval root brackets and finite scaled gaps for the edge-radius asymptotic."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from flint import arb,fmpq,ctx
from gmpy2 import mpq as Q
ctx.prec=512;start=time.monotonic()
source=sorted(Path('research/115_top_coefficient_asymptotic/verification').glob('*/checks.json'))[-1]
raw=source.read_bytes();data=json.loads(raw);assert data['all_algebraic_checks_pass']
ball=lambda q:arb(fmpq(str(q)))
text=lambda x:x.str(35,radius=True)
rows=[];counts=dict(root_brackets=0,positive_radius_gaps=0,positive_mean_gaps=0,monotone_radii=0,monotone_means=0)
for case in data['rows']:
 delta=Q(case['delta']);B=case['B'];dq=delta/(1-delta);etaq=B-delta
 d,eta=ball(dq),ball(etaq);a=2/eta;b=2*(B-1)/eta;nu=1/b
 beta=a.gamma()*b.gamma()/(a+b).gamma();R=4*d*(a*beta)**(1/a)
 kappa=4*d*(a*b*beta)**nu*nu/(1-nu).gamma()
 Cr=B*R*kappa/(4*d*(B-1)*(1+nu));Cm=B*kappa/(2*d*eta*nu)
 g=[arb(v) for v in case['coefficients_times_R_power']]
 coeff=[B*g[i]/(2*d*(eta*i+2)) for i in range(len(g))]
 previous_R=None;previous_mu=None
 for K in [1,2,3,6,10,20,30,64,128,256,512]:
  def polynomial(t):
   value=arb(0)
   for i in range(K,0,-1):value=(value+coeff[i])*t
   return value-1
  lo=Q(1);hi=Q(2)
  assert polynomial(ball(lo))<0
  while polynomial(ball(hi))<0:hi*=2
  assert polynomial(ball(hi))>0
  for _ in range(96):
   mid=(lo+hi)/2;value=polynomial(ball(mid))
   if value<0:lo=mid
   elif value>0:hi=mid
   else:raise AssertionError(('insufficient root precision',case['delta'],B,K))
  assert polynomial(ball(lo))<0<polynomial(ball(hi));counts['root_brackets']+=1
  t=ball(lo).union(ball(hi));RK=R*t;mu=sum((i*coeff[i]*t**i for i in range(1,K+1)),arb(0))
  assert RK>R;counts['positive_radius_gaps']+=1
  assert mu<b;counts['positive_mean_gaps']+=1
  if previous_R is not None:
   assert RK<previous_R;assert mu>previous_mu
   counts['monotone_radii']+=1;counts['monotone_means']+=1
  previous_R,previous_mu=RK,mu
  rows.append(dict(delta=str(delta),B=B,K=K,radius_ratio_lower=str(lo),radius_ratio_upper=str(hi),R_K=text(RK),R_full=text(R),mean=text(mu),mean_limit=text(b),C_radius=text(Cr),C_mean=text(Cm),scaled_radius_gap_over_constant=text((RK-R)*arb(K)**(1+nu)/Cr),scaled_mean_gap_over_constant=text((b-mu)*arb(K)**nu/Cm)))
 print(json.dumps(dict(delta=str(delta),B=B,last=rows[-1],elapsed_s=time.monotonic()-start)),flush=True)
now=datetime.now(timezone.utc);root=Path('research/116_edge_radius_approach/verification')/now.strftime('%Y%m%dT%H%M%SZ');(root/'sources').mkdir(parents=True)
result=dict(checked_at_utc=now.isoformat(timespec='seconds'),precision_bits=512,input_path=str(source),input_sha256=sha256(raw).hexdigest(),all_bracket_checks_pass=True,counts=counts,rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Certified finite brackets and comparisons only; no convergence rate is inferred from these tests.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for p in [Path(__file__),Path('research/116_edge_radius_approach/PROOF.md')]: (root/'sources'/(p.name+'.txt')).write_bytes(p.read_bytes())
manifest={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file()};(root/'MANIFEST.json').write_text(json.dumps(dict(files=manifest),indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),counts=counts,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

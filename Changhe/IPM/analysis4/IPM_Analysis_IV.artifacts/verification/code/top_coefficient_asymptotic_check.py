"""Positive Arb recurrence and exact low-prefix checks for the top asymptotic."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,fmpq,ctx
ctx.prec=512
start=time.monotonic();N=512
ball=lambda x:arb(fmpq(str(x)))
text=lambda x:x.str(36,radius=True)
counts=dict(positive_kernels=0,positive_coefficients=0,exact_prefix_inclusions=0,boundary_partial_sum_bounds=0)
rows=[]
for deltaq in [Q(1,3),Q(2,3),Q(4,9)]:
 for B in [2,4,6]:
  dq=deltaq/(1-deltaq);etaq=B-deltaq;aq=2/etaq;bq=2*(B-1)/etaq
  d,eta,a,b=map(ball,[dq,etaq,aq,bq]);nu=1/b
  beta=a.gamma()*b.gamma()/(a+b).gamma();R=4*d*(a*beta)**(1/a)
  C=(a*b*beta)**nu;kappa=4*d*C*nu/(1-nu).gamma()
  inv=[arb(0)]+[1/(eta*i+2) for i in range(1,N+1)]
  g=[arb(0),R];selected=[]
  for n in range(2,N+1):
   total=arb(0)
   for i in range(1,n//2+1):
    j=n-i;kernel=B*(j*inv[i]+i*inv[j])-1
    assert kernel>0;counts['positive_kernels']+=1
    total+=(1 if i==j else 2)*kernel*g[i]*g[j]
   g.append(total/(4*d*(n-1)))
   assert g[-1]>0;counts['positive_coefficients']+=1
   if n in [16,32,64,128,256,512]:
    normalized=g[n]*arb(n)**(1+nu)/kappa
    selected.append(dict(n=n,coefficient_times_R_power=text(g[n]),ratio_to_asymptotic=text(normalized),relative_error=text(normalized-1),successive_ratio_times_R=text(g[n]/g[n-1])))
  h=[Q(0),Q(1)]
  for n in range(2,21):h.append(sum((Q(2*B*(n-i))/(etaq*i+2)-1)*h[i]*h[n-i] for i in range(1,n))/(4*dq*(n-1)))
  for n in range(1,21):
   assert (g[n]/R**n).contains(fmpq(str(h[n])));counts['exact_prefix_inclusions']+=1
  sumH=sum(g,arb(0));sumJ=sum((g[n]*inv[n] for n in range(1,N+1)),arb(0))
  assert sumH<4*d and sumJ<2*d/B;counts['boundary_partial_sum_bounds']+=2
  row=dict(delta=str(deltaq),B=B,N=N,a=str(aq),b=str(bq),nu=text(nu),radius=text(R),kappa=text(kappa),sumH_through_N=text(sumH),sumH_limit=text(4*d),sumJ_through_N=text(sumJ),sumJ_limit=text(2*d/B),selected=selected,coefficients_times_R_power=[v.str(64,radius=True) for v in g])
  rows.append(row)
  print(json.dumps(dict(delta=str(deltaq),B=B,last=selected[-1],elapsed_s=time.monotonic()-start)),flush=True)
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');root=Path('research/115_top_coefficient_asymptotic/verification')/stamp;(root/'sources').mkdir(parents=True)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),precision_bits=512,maximum_order=N,all_algebraic_checks_pass=True,counts=counts,rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Finite arithmetic checks and finite comparison with the proposed asymptotic constant. No extrapolation is used as proof.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for p in [Path('code/top_coefficient_asymptotic_check.py'),Path('research/115_top_coefficient_asymptotic/PROOF.md')]: (root/'sources'/(p.name+'.txt')).write_bytes(p.read_bytes())
manifest={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file()}
(root/'MANIFEST.json').write_text(json.dumps(dict(files=manifest),indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),counts=counts,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

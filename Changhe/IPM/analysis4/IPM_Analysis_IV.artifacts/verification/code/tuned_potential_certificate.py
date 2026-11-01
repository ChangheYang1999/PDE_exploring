"""Finite exact Cartesian checks of the pure-to-potential series inverse."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import cartesian_verify as cv
import logarithmic_verify as lv
from gmpy2 import mpq as Q
start=time.monotonic()
root=Path('research/121_tuned_potential_series')
counts=dict(basis_inputs=0,linear_combination_inputs=0,poisson_identities=0,potential_identities=0,large_order_bounds=0,log_degree_checks=0)
rows=[]

def sine_norm(field):
 return sum((abs(v) for modes in field.amplitudes('sine').values() for v in map(Q,modes.values())),Q(0))

def check(n,B,amplitudes,H,tag):
 p=Q(1)-Q(2*n,3)
 f=cv.sin_field(p,amplitudes)
 g=cv.poisson(f)
 if n%3==0 and n>=6:g=g+cv.sin_field(p+1,{2*n//3-2:H})
 assert (g.laplace().scale(-1)-f.dx()).zero();counts['poisson_identities']+=1
 fl,gl=lv.LogField.pure(f),lv.LogField.pure(g)
 pot,ux,uy=lv.reconstruct(fl,gl)
 rr,pp,_,_=lv.from_potential(pot)
 assert (rr-fl).zero() and (pp-gl).zero();counts['potential_identities']+=1
 assert pot.degree()<= (1 if n in [3,6] else 0);counts['log_degree_checks']+=1
 assert max((abs(m) for d in pot.terms.values() for m in d),default=0)<=B*n-2
 cos=pot.amplitudes('cosine')
 Cnorm=sum((abs(Q(v)) for v in cos.get('0',{}).values()),Q(0))
 if n>=12:
  bound=Q(9*B*(1+9*(B+1)**2),n)*sum(map(abs,amplitudes.values()),Q(0))+Q(9,n*n)*sine_norm(gl)
  assert Cnorm<=bound;counts['large_order_bounds']+=1
 else:bound=None
 counts['basis_inputs' if tag=='basis' else 'linear_combination_inputs']+=1
 rows.append(dict(n=n,B=B,kind=tag,H=str(H),potential_log_degree=pot.degree(),potential_norm=str(Cnorm),norm_bound=None if bound is None else str(bound),all_identities_exact=True))

try:
 # Every input density basis in the checked support, plus arbitrary prescribed
 # harmonic stream; avoid exactly the forbidden compatibility basis.
 for B in [2,4,6]:
  for n in [1,2,3,4,5,6,7,8,9,10,11,12,15,18,24,30]:
   frequencies=[m for m in range(1,B*n,2) if not(n%3==0 and n>=6 and m==2*n//3-3)]
   for m in frequencies:check(n,B,{m:Q(1)},Q(0),'basis')
   amplitudes={m:Q((-1)**i*(i+1),i+2) for i,m in enumerate(frequencies)}
   for H in [Q(-7,3),Q(11,5)]:check(n,B,amplitudes,H,'mixed')
  print(json.dumps(dict(B=B,counts=counts,elapsed_s=time.monotonic()-start)),flush=True)
 # The three exceptional logarithmic identities are checked directly.
 exceptional=[]
 for s,m in [(Q(2),0),(Q(2),2),(Q(0),0)]:
  pot=lv.LogField(s,{1:cv.cos_field(s,{m:Q(1)}).modes})
  f,g,_,_=lv.from_potential(pot)
  exceptional.append(dict(s=str(s),frequency=m,density=f.amplitudes('sine'),stream=g.amplitudes('sine')))
 expected=[({'0':{'1':'-4/1'}},{'0':{'2':'1/1'}}),({'0':{'1':'4/1','3':'4/1'}},{'0':{'4':'-1/2'}}),({}, {'0':{'2':'-1/1'}})]
 for actual,(ff,gg) in zip(exceptional,expected):assert actual['density']==ff and actual['stream']==gg
 now=datetime.now(timezone.utc)
 result=dict(checked_at_utc=now.isoformat(timespec='seconds'),all_checks_pass=True,counts=counts,exceptional_logarithmic_identities=exceptional,rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Finite exact identity and bound checks. The infinite assertion is proved separately in PROOF.md.')
 (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 for p in [Path(__file__),Path('code/cartesian_verify.py'),Path('code/logarithmic_verify.py')]: (root/'sources'/(p.name+'.txt')).write_bytes(p.read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_checks_pass=True,counts=counts,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 print(json.dumps(dict(error_type=type(exc).__name__,error=str(exc))),flush=True)
 raise SystemExit(1)

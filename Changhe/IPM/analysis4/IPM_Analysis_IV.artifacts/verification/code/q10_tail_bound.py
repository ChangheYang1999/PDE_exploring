"""Certify Q10 root-five remaining responses and exact prefix-majorant boxes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,fmpq,fmpq_poly,ctx
from certificate_admission import read,ref,checkref
from certified_initial_majorants import endpoints
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/294_q10_tail_prefix');BASE=Path('research/282_period_ten_symbolic_response/verification')
def save(p,d):
 raw=json.dumps(clean(d),separators=(',',':')).encode();p.write_bytes(gzip.compress(raw,mtime=0));return ref(p)
def ev(p,I):
 v=arb(0)
 for c in reversed(list(p)):v=v*I+arb(c)
 return v
poly=lambda c:fmpq_poly([fmpq(v) for v in c])
start=time.monotonic();ctx.prec=1536
prefix=ROOT/'verification/Q10_root5_checks.json.gz';data=read(prefix);assert data['all_checks_pass'] and data['maximum_order']==120
for r in data['inputs']+[data['exact_prefix']]:checkref(r)
rootfile=Path(data['inputs'][0]['path']);roots=read(rootfile);interval=roots['real_roots'][4]['interval'];I=arb(fmpq(interval[0])).union(arb(fmpq(interval[1])))
gen=read(BASE/'reduced_generic.json.gz');fac=read(BASE/'factors.json');small=read(BASE/'small_responses.json.gz')
NN=list(map(poly,gen['numerator_by_b_degree']));D=poly(gen['denominator']);lim=poly(fac['limit_coefficients']);sm={r['k']:poly(r['coefficients']) for r in small['small']}
assert D.degree()==109 and D[109]==1 and len(NN)==11
argument=fmpq_poly([21,1]);NS=[p(argument) for p in NN];DS=D(argument);assert all(c>0 for c in DS)
lv=ev(lim,I);assert lv>0 or lv<0;sign=1 if lv>0 else -1
norms={r['n']:r for r in data['norms']};hs={r['n']:r for r in data['harmonics']};cases=[]
for M in [10,12]:
 N=10*M;minimum=min([endpoints(abs(lv))[0]]+[endpoints(abs(ev(sm[k],I)))[0] for k in range(M,21)])
 assert minimum>0;s=F(1)
 while s>=minimum/2:s/=2
 while 2*s<minimum/2:s*=2
 trials=[]
 for attempt in range(64):
  tail=[];valid=True
  for j in range(110):
   P=fmpq_poly([sign*col[j]-(fmpq(s.numerator,s.denominator)*DS[j] if b==0 else 0) for b,col in enumerate(NS)])
   value=ev(P,I);valid=valid and bool(value>0)
   tail.append(dict(degree=j,enclosure=value.str(55)))
  finite=[]
  for k in range(M,21):
   value=ev(sm[k],I);sgn=1 if value>0 else -1;gap=sgn*value-arb(fmpq(s.numerator,s.denominator));valid=valid and bool(gap>0)
   finite.append(dict(k=k,sign=sgn,gap=gap.str(55)))
  trials.append(dict(s=str(s),passed=valid))
  if valid:break
  s/=2
 assert valid
 density=[F(norms[n]['density_bound']) for n in range(1,N+1)];harmonics=[F(0)]+[F(hs[n]['bound']) for n in range(20,N,10)]
 L=F(75,29);kappa=F(208,5)*F(N+1,N);majorant=PrefixMajorant(1,10,4,density,harmonics,s,L,kappa);baseline=certificate(majorant,2)
 q=baseline['w_dyadic_exponent'];best=dict(q=q,w=F(1,2**q),radius_exponent=F(q,2),box=baseline['box'],image=baseline['image'],Y0=baseline['Y0'],maximum_ratio=baseline['maximum_ratio'],proposal='exact baseline');attempts=[]
 for q in range(q,0,-1):
  candidate,attempt=try_box(majorant,q);attempts.append(attempt)
  if candidate is None:break
  best=candidate
 box=dict(h=1,Q=10,B=4,N=N,M=M,s=s,L=L,kappa=kappa,initial_density=density,initial_harmonics=harmonics,constant=majorant.constant,J=majorant.J,Y0=majorant.Y0,baseline=baseline,adaptive=best,attempts=attempts)
 br=save(ROOT/f'verification/Q10_root5_N{N}_tail_box.json.gz',box)
 cases.append(dict(N=N,M=M,K=21,s=str(s),tail_sign=sign,root_interval=interval,tail_coefficients=tail,finite_checks=finite,trials=trials,q=best['q'],box=br))
 print(json.dumps(clean(dict(N=N,M=M,s=s,q=best['q'],elapsed_s=time.monotonic()-start))),flush=True)
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,bits=1536,Q=10,root_index=5,cases=cases,prefix=ref(prefix),inputs=[ref(BASE/n) for n in ['reduced_generic.json.gz','factors.json','small_responses.json.gz']]+[ref(rootfile)],actual_elapsed_s=time.monotonic()-start)
save(ROOT/'verification/tail_checks.json.gz',out);(ROOT/'sources/q10_tail_bound.py').write_bytes(Path(__file__).read_bytes())

"""Directed necessary radii for the period-seven/eight two-mode roots."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from pure_cartesian_ball import refine_root,ball
from certified_initial_majorants import pack
ROOT=Path('research/259_period_seven_eight_necessary_radii')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def fresh(q):return arb(q.numerator)/q.denominator
def main():
 start=time.monotonic();groups=[]
 for Q,number in [(7,253),(8,256)]:
  folder=next(Path('research').glob(str(number)+'_*'));src=folder/'verification/obstruction_checks.json';raw=src.read_bytes();data=json.loads(raw);assert data['all_checks_pass']
  entry=data['prefix_polynomials'];packed=Path(entry['path']).read_bytes();assert sha256(packed).hexdigest()==entry['sha256'];decoded=gzip.decompress(packed);assert sha256(decoded).hexdigest()==entry['raw_sha256'];exact=json.loads(decoded)
  delta=F(2,Q);d=F(2,Q-2);eta=4-delta;a=2/eta;beta=6/eta
  assert (a,beta,1-1/beta)==(F(Q,2*Q-1),F(3*Q,2*Q-1),F(Q+1,3*Q))
  hs=[F(0),F(1)];tops=[]
  for n in range(1,2*Q+1):
   if n>1:hs.append(sum((8*(n-j)/(eta*j+2)-1)*hs[j]*hs[n-j] for j in range(1,n))/(4*d*(n-1)))
   coeff=list(map(F,exact['fields']['f'][str(n)]['sine_polynomials'][str(4*n-1)]));assert coeff==[F(0)]*n+[(-1)**(n-1)*hs[n]] and hs[n]>0,('top',Q,n)
   tops.append(dict(n=n,frequency=4*n-1,scalar_coefficient=str(hs[n])))
  values=[]
  for bits in [512,1024]:
   ctx.prec=bits;ball.cache_clear();aa=fresh(a);bb=fresh(beta);RH=4*fresh(d)*((aa*aa.gamma()*bb.gamma()/(aa+bb).gamma()).log()/aa).exp();roots=[]
   for row in data['real_roots']:
    b,I=refine_root(list(map(int,data['primitive_coefficients'])),row['interval'],bits+64);assert not b.contains(0)
    threshold=((abs(b)/RH).log()/fresh(delta)).exp();roots.append((b,I,threshold))
   values.append((RH,roots))
  assert values[0][0].overlaps(values[1][0]);rows=[]
  for i,(old,new) in enumerate(zip(values[0][1],values[1][1]),1):
   b,I,radius=new;assert old[0].overlaps(b) and old[2].overlaps(radius)
   den=10**30;lo=int((radius.lower()*den).floor().unique_fmpz());hi=int((radius.upper()*den).ceil().unique_fmpz());assert fresh(F(lo,den))<radius<fresh(F(hi,den))
   small=10**9;slo=int((radius.lower()*small).floor().unique_fmpz());assert fresh(F(slo,small))<radius
   rows.append(dict(root_index=i,root_interval=I,root=b.str(55,radius=True),necessary_radius=radius.str(65,radius=True),necessary_radius_ball=pack(radius),radius_bounds_exact=[str(F(lo,den)),str(F(hi,den))],safe_decimal_lower=f'{slo//small}.{slo%small:09d}'))
  groups.append(dict(Q=Q,delta=str(delta),a=str(a),beta=str(beta),four_d=str(4*d),R_H=values[-1][0].str(65,radius=True),R_H_ball=pack(values[-1][0]),rows=rows,exact_top_checks=tops,source=dict(path=str(src),sha256=sha256(raw).hexdigest()),prefix_source=entry))
  print(json.dumps(dict(at=stamp(),Q=Q,all_checks_pass=True,roots=len(rows),exact_top_orders=2*Q,actual_elapsed_s=time.monotonic()-start)),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,arithmetic_bits=[512,1024],groups=groups,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/period_necessary_radii.py').write_bytes(Path('code/period_necessary_radii.py').read_bytes())
 print(json.dumps(dict(at=stamp(),all_checks_pass=True,actual_elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)

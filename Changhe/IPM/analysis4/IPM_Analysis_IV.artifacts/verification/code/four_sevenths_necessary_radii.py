"""Directed necessary constants and exact highest-sector checks at delta4/7."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,gzip,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from pure_cartesian_ball import refine_root,ball
from certified_initial_majorants import pack
ROOT=Path('research/248_four_sevenths_necessary_radii')
SOURCE=Path('research/239_four_sevenths_two_mode/verification/obstruction_checks.json')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def fresh(q):return arb(q.numerator)/q.denominator

def main():
 start=time.monotonic();src=json.loads(SOURCE.read_bytes());assert src['all_checks_pass'];entry=src['prefix_polynomials'];raw=Path(entry['path']).read_bytes();assert sha256(raw).hexdigest()==entry['sha256'];exact=json.loads(gzip.decompress(raw) if entry['path'].endswith('.gz') else raw)
 delta=F(4,7);d=F(4,3);eta=4-delta;a=2/eta;beta=6/eta
 assert (a,beta,a+beta,1-1/beta)==(F(7,12),F(7,4),F(7,3),F(3,7))
 hs=[F(0),F(1)];tops=[]
 for n in range(1,8):
  if n>1:hs.append(sum((8*(n-j)/(eta*j+2)-1)*hs[j]*hs[n-j] for j in range(1,n))/(4*d*(n-1)))
  coeff=list(map(F,exact['fields']['f'][str(n)]['sine_polynomials'][str(4*n-1)]));wanted=[F(0)]*n+[(-1)**(n-1)*hs[n]]
  assert coeff==wanted and hs[n]>0,('top',n);tops.append(dict(n=n,frequency=4*n-1,scalar_coefficient=str(hs[n])))
 values=[]
 for bits in [512,1024]:
  ctx.prec=bits;ball.cache_clear();aa=fresh(a);bb=fresh(beta);RH=4*fresh(d)*((aa*aa.gamma()*bb.gamma()/(aa+bb).gamma()).log()/aa).exp();roots=[]
  for data in src['real_roots']:
   b,I=refine_root(list(map(int,src['primitive_coefficients'])),data['interval'],bits+64);assert b>0;threshold=((b/RH).log()/fresh(delta)).exp();roots.append((b,I,threshold))
  values.append((RH,roots))
 assert values[0][0].overlaps(values[1][0]);rows=[]
 for i,(safe,row0,row1) in enumerate(zip(['0.0127184','0.0430461','0.880537'],values[0][1],values[1][1]),1):
  b,I,radius=row1;assert row0[0].overlaps(b) and row0[2].overlaps(radius);assert fresh(F(safe))<radius
  den=10**24;lo=int((radius.lower()*den).floor().unique_fmpz());hi=int((radius.upper()*den).ceil().unique_fmpz());assert fresh(F(lo,den))<radius<fresh(F(hi,den))
  rows.append(dict(root_index=i,root_interval=I,root=b.str(60,radius=True),necessary_radius=radius.str(70,radius=True),necessary_radius_ball=pack(radius),radius_bounds_exact=[str(F(lo,den)),str(F(hi,den))],safe_decimal_lower=safe))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,arithmetic_bits=[512,1024],R_H=values[-1][0].str(70,radius=True),R_H_ball=pack(values[-1][0]),rows=rows,exact_top_checks=tops,source=dict(path=str(SOURCE),sha256=sha256(SOURCE.read_bytes()).hexdigest()),prefix_source=entry,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/four_sevenths_necessary_radii.py').write_bytes(Path('code/four_sevenths_necessary_radii.py').read_bytes());print(json.dumps({k:v for k,v in out.items() if k not in ['R_H_ball','exact_top_checks','rows']}));print(json.dumps([{k:v for k,v in row.items() if k not in ['necessary_radius_ball','root_interval']} for row in rows]))
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)]);(ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));raise SystemExit(1)

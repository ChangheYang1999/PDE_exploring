"""Exact low top coefficients and directed necessary radii for three profiles."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from extremal_single_exact import ExactSingle,coefficient,poisson,parse,Q
from certified_initial_majorants import pack
ROOT=Path('research/245_extremal_necessary_radii')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def fresh(x):return arb(x.numerator)/x.denominator
def main():
 started=time.monotonic();rows=[]
 for h,period,expected_a,expected_b in [(2,5,F(5,18),F(35,18)),(2,7,F(7,33),F(21,11)),(3,13,F(13,114),F(221,114))]:
  delta=F(2*h,period);mode=period+2*h-2;B=mode+1;eta=B-delta;d=delta/(1-delta);a=2/eta;b=2*mode/eta
  assert (a,b)==(expected_a,expected_b)
  r=ExactSingle(h,period);r.setf(1,parse(r.p(1),{str(mode):['1']}));r.setg(1,poisson(r.F[1]));hs=[F(0),F(1)];tops=[]
  for n in range(2,5):
   r.setf(n,r.density(n));r.setg(n,poisson(r.F[n]))
   scalar=sum((2*B*(n-i)/(eta*i+2)-1)*hs[i]*hs[n-i] for i in range(1,n))/(4*d*(n-1));hs.append(scalar)
   actual=F(str(coefficient(r.F[n],B*n-1)));assert actual==(-1)**(n-1)*scalar and scalar>0
   tops.append(dict(n=n,top_exact=str(actual),scalar_exact=str(scalar)))
  values=[]
  for bits in [512,1024]:
   ctx.prec=bits;aa=fresh(a);bb=fresh(b);dd=fresh(d)
   RH=4*dd*((aa*aa.gamma()*bb.gamma()/(aa+bb).gamma()).log()/aa).exp()
   radius=(-RH.log()/fresh(delta)).exp();values.append((RH,radius))
  assert all(x.overlaps(y) for x,y in zip(*values));RH,radius=values[-1]
  den=10**24;lo=int((radius.lower()*den).floor().unique_fmpz());hi=int((radius.upper()*den).ceil().unique_fmpz())
  assert fresh(F(lo,den))<radius<fresh(F(hi,den))
  rows.append(dict(h=h,Q=period,delta=str(delta),mode=mode,B=B,a=str(a),b=str(b),boundary_power=str(1-1/b),amplitude_power=str(1/delta),R_H=RH.str(70,radius=True),R_H_ball=pack(RH),necessary_radius=radius.str(70,radius=True),necessary_radius_ball=pack(radius),radius_bounds_exact=[str(F(lo,den)),str(F(hi,den))],top_checks=tops))
 result=dict(checked_at_utc=stamp(),all_checks_pass=True,arithmetic_bits=[512,1024],rows=rows,actual_elapsed_s=time.monotonic()-started)
 (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 for name in ['extremal_necessary_radii.py','extremal_single_exact.py','laurent_log_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({**result,'rows':[{k:v for k,v in row.items() if not k.endswith('_ball') and k!='top_checks'} for row in rows]}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)

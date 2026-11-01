"""Directed necessary-radius specialization for the Candidate-shaped profiles."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball
from certified_initial_majorants import pack
ROOT=Path('research/238_candidate_top_radius')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();p=Path('research/02_candidate007/data/leading_exact.json');d=json.loads(p.read_text())
 assert sha256(Path(d['input']).read_bytes()).hexdigest()==d['input_sha256']
 alpha=F(d['density']['19'])/F(d['density']['1']);assert alpha>0
 delta=F(4,9);B=20;eta=B-delta;a=2/eta;b=2*(B-1)/eta;nu=1/b;assert (a,b,nu)==(F(9,88),F(171,88),F(88,171))
 values=[]
 for bits in [512,1024]:
  ctx.prec=bits;aa=ball(mpq(str(a)));bb=ball(mpq(str(b)));al=ball(mpq(str(alpha)))
  beta=aa.gamma()*bb.gamma()/(aa+bb).gamma()
  RH=arb(16)/5*((aa*beta).log()/aa).exp();R=((al/RH).log()*arb(9)/4).exp()
  values.append((al,RH,R))
 assert all(x.overlaps(y) for x,y in zip(*values))
 al,RH,R=values[-1]
 displayed=[('alpha','0.00010215176','0.000000000005',al),('R_H','1.28042563177806','0.000000000000005',RH),('necessary_radius','0.00000000060153','0.000000000000005',R)]
 checks=[dict(quantity=name,display=number,tolerance=tol,agrees=bool(abs(value-arb(number))<arb(tol))) for name,number,tol,value in displayed]
 lower=int((R.lower()*10**20).floor().unique_fmpz());upper=int((R.upper()*10**20).ceil().unique_fmpz())
 assert arb(lower)/10**20<R<arb(upper)/10**20
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,arithmetic_bits=[512,1024],source=dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest(),authoritative_sha256=d['input_sha256']),
  alpha_exact=str(alpha),alpha=al.str(70,radius=True),alpha_ball=pack(al),R_H=RH.str(70,radius=True),R_H_ball=pack(RH),necessary_radius=R.str(70,radius=True),necessary_radius_ball=pack(R),
  radius_bounds_exact=[str(F(lower,10**20)),str(F(upper,10**20))],a=str(a),b=str(b),nu=str(nu),boundary_second_derivative_power=str(1-nu),leading_amplitude_exponent='9/4',display_checks=checks,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/candidate_top_radius.py').write_bytes(Path(__file__).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if not k.endswith('_ball') and k!='alpha_exact'}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)

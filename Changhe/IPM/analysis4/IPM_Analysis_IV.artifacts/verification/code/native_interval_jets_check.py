from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import time,sys,json,random,traceback
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from native_interval_jets import NativeJet,enclose_native
from taylor_response_enclosure import Jet
from pure_cartesian_ball import ball
from extremal_single_probe import ExtremalResponse
from certified_initial_majorants import pack
from unpack_dyadic4 import unpack
ROOT=Path('research/249_native_interval_jets')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();ctx.prec=768;ctx.cap=10;rng=random.Random(20261031);ops=0
 for degree in range(1,8):
  for rep in range(12):
   a=[arb(rng.randrange(-9,10))/7 for j in range(degree+1)];b=[arb(rng.randrange(-9,10))/11 for j in range(degree+1)];b[0]=arb(2)
   if rep%2:a[1]=a[1]+arb(0,arb(1)/100)
   na,nb=NativeJet(a,degree),NativeJet(b,degree);ma,mb=Jet(a,degree),Jet(b,degree)
   for native,manual in [(na+nb,ma+mb),(na-nb,ma-mb),(na*nb,ma*mb),(na/nb,ma/mb),(3/nb,3/mb),(-na,-ma)]:
    assert all(x.overlaps(y) for x,y in zip(native.c,manual.c));ops+=1
 try:NativeJet([arb(1)],5)/NativeJet([arb(0,1)],5)
 except AssertionError:zero_rejected=True
 else:raise AssertionError('zero denominator accepted')
 oldcap=ctx.cap;ctx.cap=4
 try:NativeJet([arb(1)],5)
 except AssertionError:cap_rejected=True
 else:raise AssertionError('insufficient cap accepted')
 finally:ctx.cap=oldcap
 response=ExtremalResponse(3,13);begin=time.monotonic();a=F(0);b=F(1,3808);value=enclose_native(response,a,b,5);native_s=time.monotonic()-begin
 p=Path('research/242_single_seventeen_six_thirteenths/verification/jet_probe.json');data=json.loads(p.read_text());old=next(row for row in data['rows'] if row['a']=='0' and row['b']=='1/3808' and row['degree']==5)
 assert value.overlaps(arb(*unpack(old['enclosure'])))
 for t in [a,b,(a+b)/2]:assert value.contains(response.compact(ball(mpq(str(t)))))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,coefficient_operation_cases=ops,zero_denominator_rejected=zero_rejected,precision_cap_rejected=cap_rejected,native_elapsed_s=native_s,manual_elapsed_s=old['elapsed_s'],native_enclosure=pack(value),native_display=value.str(40,radius=True),manual_source=dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()),actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 for name in ['native_interval_jets.py','native_interval_jets_check.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps(out),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)]);(ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)

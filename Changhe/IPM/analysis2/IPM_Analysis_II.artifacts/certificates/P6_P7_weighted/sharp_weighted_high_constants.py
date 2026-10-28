"""Independent rational and interval arithmetic for the smaller weighted X norm."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent
A=lambda q:arb(Q(q).numerator)/Q(q).denominator
C3=Q(560,3)+9+32+Q(81,5)+288+Q(8192,3)
assert C3==Q(48938,15) and C3<3263
assert C3*C3+88<2**24
assert Q(2**24,20)-C3*C3-88>=-Q(3,2)*2**24
th=Q(1,62);al=Q(1,124);sig=Q(1,5)
assert (1-th)/20-Q(3,2)*th==Q(1,40)
assert 6*1092<2**13 and 6*38038<2**18
assert 13+5*th<14
cg=1/(2*(arb.pi()*A(th)*(1+A(th))).sqrt())
ch=2**(-A(al))/arb.pi().sqrt()*((2+A(al)).gamma()*(A(th)-A(al)).gamma()/(2+A(th)).gamma()).sqrt()
assert cg<4 and ch<9
assert 9*2**14<2**20 and 2*2**16*arb(4)**A(al)<2**20
assert 2*2**14*(1+8)<2**20
cc=arb(2**14)+4*arb(2**20)/(arb.pi()*A(al)*(1+A(al)))+2**A((1+sig)/2)/(2*arb.pi()*(1-A(sig))).sqrt()
assert cc<2**29
p=256;k=260;gap=p*(1+al)+2-k
assert gap==Q(2,31)
cm=(2*arb.pi()/A(gap))**A(Q(1,p))*arb(2**20)/(1+A(al))
assert cm<2**21
assert 40*(1+2**20+2**21+2**29)<2**36
assert Q(13,2)*(2**16+5)<2**19
assert 2**24>=1 and 2**22>=1 and 2**31>=26
proof=HERE.parent/'SHARP_WEIGHTED_HIGH_PROOF.md'
inputs=[HERE/'sharp_weighted_h2_constants.json',HERE/'r2_extra_audit.json',HERE/'weighted_high_constants.json']
for f in inputs[:2]:assert json.loads(f.read_text())['status']=='CONFIRMED'
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'CONFIRMED','ledger':'V076','third_cross_coefficient':str(C3),'third_absorbed_debt':str(C3*C3+88),'E3_E2_squared_coefficient':str(2**24),'theta':str(th),'alpha':str(al),'semigroup_decay':'1/40','inverse':40,'local_H2_cutoff_bound':2**13,'local_H3_cutoff_bound':2**18,'interpolated_cutoff_bound':2**14,'gradient_bound':2**16,'holder_bound':2**20,'moment_bound':2**21,'strain_bound':2**29,'combined_inverse_bound':2**36,'low_bilinear_bound':2**19,'gradient_embedding_constant':cg.str(60),'gradient_holder_constant':ch.str(60),'strain_bound_before_rounding':cc.str(60),'moment_bound_before_rounding':cm.str(60),'input_hashes':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs},'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

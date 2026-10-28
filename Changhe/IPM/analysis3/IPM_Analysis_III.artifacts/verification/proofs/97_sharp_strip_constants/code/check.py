from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import hashlib,json
ctx.threads=1
runs=[]
for prec in (256,384):
 ctx.prec=prec
 a=arb(17)/4;v=arb(7)/4;e=arb(1).exp()
 P=256/(6*e**4*(1-1/v)**4);Q=27/(2*e**3*(1-1/v)**3);M=1/(e*(1-1/v))
 Af=P*v**(a-arb(9)/2)/(2*(9-2*a)).sqrt()
 An=v**a*((1+v/e)*(1+2*(v*v-1/(v*v))/(e*e))).sqrt()
 Ar=M/(2*(2*a+1)).sqrt()/v**(a+arb(1)/2)+4/(e*e)/(2*(2*a-3)).sqrt()/v**(a-arb(3)/2)
 Bf=Q*v**(a-arb(9)/2)/(2*(9-2*a).sqrt())
 Bn=v**a*(2*(1+(v-1/v)/e)).sqrt()
 Br=M/(2*(2*a+1).sqrt())/v**(a+arb(1)/2)+(1/e)/(2*(2*a-1).sqrt())/v**(a-arb(1)/2)
 A=Af+An+Ar;B=1+Bf+Bn+Br
 B0=1/e/(2*a-1).sqrt();B1=(2/e)**2/(2*a-3).sqrt();B2=(3/e)**3/(2*a-5).sqrt()
 DA=A+B1/(9-2*a).sqrt();DB=B+B0/(9-2*a).sqrt()
 vals={'CA':A,'CB':B,'DA':DA,'DB':DB,'B0':B0,'B1':B1,'B2':B2}
 bounds={'CA':(38436,1000),'CB':(24534,1000),'DA':(38762,1000),'DB':(24724,1000),'B0':(134331,1000000),'B1':(230829,1000000),'B2':(718533,1000000)}
 for key,value in vals.items():
  num,den=bounds[key]
  assert value<arb(num)/den,(key,value)
 assert A<39 and DA<39 and B<25 and DB<25
 runs.append({'bits':prec,'values':{k:str(x) for k,x in vals.items()},'upper_rationals':bounds})
p=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','arithmetic':'directed Arb balls; exact rational parameters','a':'17/4','split_ratio':'7/4','runs':runs,'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(o['date'],o['status'])

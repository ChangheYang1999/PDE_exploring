from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[3]
source=root/'proofs/15_modal_source/evidence/source_512_result.json'
data=json.loads(source.read_text())['results']['whole']
def endpoints(name):return [Q(data[name][side+'_exact']) for side in ('lower','upper')]
A0,A1=endpoints('wprime');u0,u1=endpoints('mu');g0,g1=endpoints('g');s=Q(41,20)
slow=(1+A0/2-Q(31,20)*u1,1+A1/2-Q(31,20)*u0)
fast=(1+g0+u0/2-Q(31,20)*A1,1+g1+u1/2-Q(31,20)*A0)
diff=g0-s*(A1-u0)
assert diff>0 and Q('4.5253')<slow[0]<slow[1]<Q('4.5255')
assert Q('15.5157')<fast[0]<fast[1]<Q('15.5161')
boxslow=1+Q(10,2)-Q(31,20)*Q(101,100)
boxfast=1+29+Q(99,200)-Q(31,20)*Q(51,5)
assert boxslow==Q(8869,2000) and boxfast==Q(2937,200)
def show(interval):
 out={'lower_exact':str(interval[0]),'upper_exact':str(interval[1])}
 scale=10**14;lo=interval[0].numerator*scale//interval[0].denominator;hi=-((-interval[1].numerator*scale)//interval[1].denominator)
 out['decimal_lower']=f'{lo//scale}.{lo%scale:014d}';out['decimal_upper']=f'{hi//scale}.{hi%scale:014d}';return out
proof=Path(__file__).resolve().parents[1]/'PROOF.md'
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_domain':'results.whole','slow_margin':show(slow),'fast_margin':show(fast),'fast_minus_slow_lower_exact':str(diff),'rectangular_box_slow':str(boxslow),'rectangular_box_fast':str(boxfast)}
(proof.parent/'evidence/check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('date','slow_margin','fast_margin')},indent=2))

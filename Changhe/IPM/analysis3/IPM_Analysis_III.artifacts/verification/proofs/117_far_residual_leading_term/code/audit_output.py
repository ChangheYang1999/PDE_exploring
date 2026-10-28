from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'evidence/check.json';d=json.loads(p.read_text());k=F(1615536043799051,2**53)
assert d['status']=='PASS' and F(d['physical_degree'])==2*k-1 and F(d['energy_rate'])==4*k-F(5,4)<0
assert d['proof_sha256']==hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()
assert d['code_sha256']==hashlib.sha256((ROOT/'code/check.py').read_bytes()).hexdigest()
checks={}
def bound(key,rec,lo,hi):
 assert F(lo)<F(rec['lower_exact'])<=F(rec['upper_exact'])<F(hi)
 checks[key]=[lo,hi]
bound('remainder_coefficient_t',d['remainder_coefficient_t'],'4577286933.12061','4577286933.12062')
bound('remainder_coefficient_tau',d['remainder_coefficient_tau'],'8.51862206231728e-17','8.51862206231729e-17')
bound('t_33_4_remainder',d['points'][0]['remainder'],'4618467.1665640262','4618467.1665640263')
bound('t_33_4_axis',d['points'][0]['axis'],'0.0063924626364420086','0.0063924626364420088')
bound('t_30_ratio',d['points'][1]['remainder_ratio_to_leading'],'0.9999999044311651','0.9999999044311653')
assert F(d['nonzero_sine_coefficient']['upper_exact'])<0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':checks,'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(ROOT/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

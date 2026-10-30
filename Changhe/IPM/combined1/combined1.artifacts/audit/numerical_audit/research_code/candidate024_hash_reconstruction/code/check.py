from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate024_hash_reconstruction'
sha=lambda b:sha256(b).hexdigest()
def main():
 start=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);b=p.read_bytes();s=sha(b);assert h is None or s==h;inputs[str(p.relative_to(R))]=s;return b
 prep=json.loads(bind(B/'verification/PREPARE.json'));bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 notes=bind(B/'source/N1_NOTES_1152.md',prep['source_notes_sha256']).decode()
 assert "'Objective rows (81? no: 67):' -> 'Objective rows (67):'" in notes
 audit=json.loads(bind(R/'research/candidate024_holdout/verification/result.json',prep['source_prior_audit_sha256']))
 p=R/'research/candidate024_holdout/source/N1_HELDOUT_024.md';current=bind(p,audit['current_heldout_sha256'])
 before=b'Objective rows (81? no: 67):';after=b'Objective rows (67):'
 assert current.count(after)==1 and before not in current
 old=current.replace(after,before,1);assert old.replace(before,after,1)==current
 oldp=B/'source/RECONSTRUCTED_claimed_091313_HELDOUT_024.md'
 with oldp.open('xb') as f:f.write(old)
 bind(oldp)
 parse=lambda text:[[int(n),int(K)] for line in text.decode().splitlines() if line.startswith('- the ') for n,K in re.findall(r'(\d+):(\d+)',line)]
 currentpairs=parse(current);oldpairs=parse(old);expected=[[r['n'],r['K']] for r in audit['probe_rows']]
 assert currentpairs==oldpairs==expected and len(currentpairs)==60
 actual=sha(old);claimed=audit['other_claimed_sha256'];matched=actual==claimed
 assert all(sha((R/p).read_bytes())==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'current_sha256':sha(current),'reconstructed_sha256':actual,'claimed_former_sha256':claimed,'hash_matches_claim':matched,'old_string':before.decode(),'new_string':after.decode(),'one_replacement_only':True,'all_other_bytes_equal':True,'current_pairs':currentpairs,'reconstructed_pairs':oldpairs,'all60_pairs_preserved':True,'inputs':inputs,'verdict':'CONFIRMED proposed complete byte explanation' if matched else 'REFUTED proposed single-edit complete byte explanation','historical_timestamps':'OPEN as independently observed events; publisher assertions only','foreign_code_executed':False}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['inputs','current_pairs','reconstructed_pairs']}),flush=True);print('result_sha256',sha(p.read_bytes()),flush=True)
if __name__=='__main__':main()

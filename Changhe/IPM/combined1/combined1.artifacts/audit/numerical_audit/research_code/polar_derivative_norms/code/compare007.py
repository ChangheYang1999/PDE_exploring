"""Independent canonical identity, complete mode audit and N3 norm comparison."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];D=R/'research/polar_derivative_norms';NAME='C1-N1-007-d2w-j7-e2bal'
ctx.prec=2048

def H(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def main():
 tick=time.monotonic();folder=D/'verification'/NAME;p=folder/'full.json';full=json.loads(p.read_text());mp=folder/'manifest.json';m=json.loads(mp.read_text())
 assert full['candidate']==NAME and full['complete'] and not full['missing_modes']
 assert full['completed_modes']==m['modes']==list(range(1,320,2)) and full['manifest_sha256']==H(mp)
 assert m['labels']==['rF','G1','P2'] and all(H(R/path)==value for path,value in m['inputs'].items())
 src=R/f'research/candidate_audits/data/{NAME}/canonical.json';can=json.loads(src.read_text())
 peerfile=R/'research/whole_plane_norms/source/candidate007/N3_norms_v02.json';peer=json.loads(peerfile.read_text());peercode=peerfile.with_name('N3_e2norms.py')
 assert H(peerfile)=='f32f726d2301cc6d691ec3b195610857a60d68f3603a083ec0275ec22fef71f8'
 assert H(peercode)==peer['code_sha256']
 entries={tuple(k):Q(v) for k,v in zip(can['order'],can['coefficients']) if Q(v)}
 serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(entries.items()))+'\n'
 assert sha256(serial.encode()).hexdigest()==can['canonical_serialization_sha256']==peer['canonical_sha256']
 assert can['source_sha256']==peer['source_sha256'] and Q(can['cl'])==Q(peer['cl'])
 modes=[]
 for n in m['modes']:
  path=folder/f'modes/mode_{n:03d}.json';rec=json.loads(path.read_text());assert H(path)==full['mode_sha256'][str(n)] and rec['manifest_sha256']==H(mp) and rec['mode']==n
  assert rec['trace_identities']>0 and set(rec['norms'])==set(m['labels'])
  for label in m['labels']:
   for side in ['lower','upper']:
    z=arb(rec['norms'][label][f'energy_{side}_ball']);assert z>0 and z.rel_accuracy_bits()>150
   assert all(Q(row['diagonal_exponent'])>-1 for row in rec['endpoints'][label])
  modes.append(rec)
 rows=[]
 for label in m['labels']:
  own=full['norms'][label];other=peer['norms'][label];assert other['status']=='FINITE'
  ol=arb(own['norm_lower_ball']);ou=arb(own['norm_upper_ball']);pl=arb(other['norm_lower_ball']);pu=arb(other['norm_upper_ball'])
  totalchecks={side:sum((arb(rec['norms'][label][f'energy_{side}_ball']) for rec in modes),arb(0)).sqrt().overlaps(arb(own[f'norm_{side}_ball'])) for side in ['lower','upper']};assert all(totalchecks.values())
  if label=='P2':checks={'own_interval_ordered':bool(ol<ou),'peer_interval_ordered':bool(pl<pu),'own_lower_below_peer_upper':bool(ol<pu),'peer_lower_below_own_upper':bool(pl<ou)}
  else:checks={'lower_balls_overlap':ol.overlaps(pl),'upper_balls_overlap':ou.overlaps(pu)}
  assert all(checks.values()),(label,checks)
  rows.append({'label':label,'own_lower':own['norm_lower_ball'],'own_upper':own['norm_upper_ball'],'peer_lower':other['norm_lower_ball'],'peer_upper':other['norm_upper_ball'],'independent_enclosures_overlap':checks,'reassembled_total_checks':totalchecks})
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':NAME,'canonical_entries':len(entries),'canonical_semantic_sha256':peer['canonical_sha256'],'source_sha256':can['source_sha256'],'modes':160,'exact_trace_identities':sum(rec['trace_identities'] for rec in modes),'rows':rows,'inputs':{str(path.relative_to(R)):H(path) for path in [src,peerfile,peercode,p,mp,Path(__file__)]},'elapsed_seconds':time.monotonic()-tick,'status':'Independent rF, G1 and weighted P2 enclosures CONFIRMED; no existence claim'}
 dest=D/'verification/candidate007_N3_comparison.json'
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()

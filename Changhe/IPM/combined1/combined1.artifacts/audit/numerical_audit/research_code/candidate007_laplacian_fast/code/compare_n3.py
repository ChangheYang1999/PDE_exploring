"""Compare complete polar and Cartesian weighted Laplacian enclosures."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/candidate007_laplacian_fast'
def H(p):return sha256(Path(p).read_bytes()).hexdigest()
def new(p,o):
 with Path(p).open('x') as f:json.dump(o,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();ctx.prec=1024
 manifest=BASE/'source/N3_v01_manifest.json';m=json.loads(manifest.read_text())
 for name,rec in m['files'].items():assert H(BASE/'source'/name)==rec['sha256']
 peerpath=BASE/'source/N3_wlap_v01.json';p=json.loads(peerpath.read_text())
 oldpath=ROOT/'research/whole_plane_norms/source/candidate007/N3_norms_v02.json';old=json.loads(oldpath.read_text())
 assert p['source_sha256']==old['source_sha256'] and p['canonical_sha256']==old['canonical_sha256'] and p['cl']==old['cl']
 ownpath=BASE/'verification/full.json';q=json.loads(ownpath.read_text());assert q['complete'] and not q['missing_modes'] and q['completed_modes']==list(range(1,320,2))
 own={r['a']:r for r in q['weights']};want=['0','1/5','1/4','2/5','1/2','3/5','3/4','4/5','1','5/4','3/2'];assert sorted(p['WLAP'])==sorted(want)
 rows=[]
 for a in want:
  r=p['WLAP'][a];lo,hi=arb(r['LB']),arb(r['UB']);our=arb(own[a]['norm'])
  assert lo>0 and hi>0 and our>0 and min(lo.rel_accuracy_bits(),hi.rel_accuracy_bits(),our.rel_accuracy_bits())>150
  # Each peer endpoint is the rounded endpoint of an enclosing square root ball.
  # Its tiny display radius is itself preserved in a containing interval.
  peer=lo.union(hi);assert peer.overlaps(our),(a,peer,our)
  rows.append({'a':a,'own_norm':own[a]['norm'],'N3_lower':r['LB'],'N3_upper':r['UB'],'interval_overlap':True})
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':q['candidate'],'complete_modes':160,'weights_compared':11,'rows':rows,'source_sha256':p['source_sha256'],'canonical_sha256':p['canonical_sha256'],'prior_canonical_confirmation_sha256':H(ROOT/'research/polar_derivative_norms/verification/candidate007_N3_comparison.json'),'peer_result_sha256':H(peerpath),'own_result_sha256':H(ownpath),'source_manifest_sha256':H(manifest),'code_sha256':H(__file__),'proof_sha256':H(BASE/'PROOF.md'),'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED11whole-plane weighted Laplacian norms; twelfth own weight remains OPENpeer'}
 new(BASE/'verification/N3_comparison_v01.json',out)
 print('CONFIRMED',len(rows),'weights;160modes',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

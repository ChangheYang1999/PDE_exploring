"""Publish the checked foreign-gate proof route; preserve earlier sealed documents."""
from datetime import datetime, timezone
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import re
ROOT=Path('bot_research/experiments/validation/reviews/final_navigation_001')
INDEX=Path('bot_research/experiments/validation/analysis/README.md')
REVIEW=Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
OUT=ROOT/'root_publication_004'
def sha(b):return hashlib.sha256(b).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
started=now()
assert not OUT.exists()
pins={'foreign_attack_control_flow_001/PROOF.md':'30dc386a91057b5a635ee3acfdbec4d7b8fd0a60dd8563be94254fb1bfc6b6ca','foreign_attack_control_flow_001/REVIEW.md':'3809629412715395224fd348130ac0198153a3e0c74152a83ae6945f79aa08d5','root_foreign_gate_review_001.json':'ee646bb88fe245bb3ebdf27665892d7e55370d66ce1470f561d38be7c62d5215'}
for name,want in pins.items():assert sha((REVIEW/name).read_bytes())==want,name
before=INDEX.read_bytes()
assert sha(before)=='a06cddf3fc12a3432a5af9786673a474a6707f9b4b1e7474537738e882d53179'
published=now()
block='- Added '+published+': the [foreign attack-gate reading order](../reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/INDEX.md) links a [conditional source proof](../reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/PROOF.md), [retained-history review](../reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/REVIEW.md) and [independent recount](../reviews/frr7_frr8_late_af5_001/root_foreign_gate_review_001.json). The ordinary AF5/g1 attack helper checks the foreign-map hold; finishing and doom have separate predicates and no such check. No legal-game counterexample is established. The 45 retained histories contain no accepted minion purchase in the 356 inspected rounds after the scripted opening and before round 11. This corrects the shared-guard explanation without changing the separate 120-condition outcome comparison.\n'
links=[]
for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',block):
 p=INDEX.parent/target
 assert p.is_file(),target
 b=p.read_bytes()
 links.append({'label':label,'target_relative_to_analysis':target,'project_path':str(p.resolve().relative_to(Path.cwd())),'sha256':sha(b),'bytes':len(b)})
after=before.rstrip(b'\n')+b'\n'+block.encode()
OUT.mkdir()
(OUT/'index_before.md.gz').write_bytes(gzip.compress(before,mtime=0))
(OUT/'index_after.md.gz').write_bytes(gzip.compress(after,mtime=0))
(OUT/'index.diff').write_text(''.join(difflib.unified_diff(before.decode().splitlines(keepends=True),after.decode().splitlines(keepends=True),fromfile='analysis/README.md before',tofile='analysis/README.md after')))
INDEX.write_bytes(after)
assert INDEX.read_bytes()==after
r={'schema':'root-navigation-publication-004','started_utc':started,'published_utc':published,'completed_utc':now(),'verdict':'CONFIRMED','index_path':str(INDEX),'index_before_sha256':sha(before),'index_after_sha256':sha(after),'review_inputs':pins,'added_links':links,'scope':'Append one source-proof reading route; all sealed reviews, guides, proofs and prior failures unchanged.','script_sha256':sha(Path(__file__).read_bytes())}
(OUT/'RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'receipt':str(OUT/'RECEIPT.json'),'sha256':sha((OUT/'RECEIPT.json').read_bytes()),'published_utc':published,'index_after_sha256':sha(after),'links':len(links)},indent=2))

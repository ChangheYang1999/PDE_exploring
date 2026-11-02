"""Append the independently checked AF5 reading route without changing sealed pages."""
from datetime import datetime, timezone
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import re

ROOT = Path('bot_research/experiments/validation/reviews/final_navigation_001')
INDEX = Path('bot_research/experiments/validation/analysis/README.md')
REVIEW = Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
OUT = ROOT / 'root_publication_003'
def sha(b): return hashlib.sha256(b).hexdigest()
def stamp(): return datetime.now(timezone.utc).isoformat()
started = stamp()
assert not OUT.exists()
expected = {
 'af5_matrix_extension/PROOF.md': '2d82fbdb2c2fc1f91f0f09656ab07489c73f60dc6a758432fe9ee3453e5d0240',
 'root_review_002.json': '2494c99caf1970368b043be9cd89f72679d8a002f15866a6ce3109ea1753e5b0',
 'hp_erratum_001/ERRATUM.md': 'bb6d6a38d95ea39df7e1de115830ee91e8f4435f0afd49ff486cc023360dfb41',
 'root_hp_erratum_review_002.json': '7dfb575ec6e7e87042695167b9e316e030fc37c8ca7cdc0b36d208d23775db3b',
}
for name, wanted in expected.items(): assert sha((REVIEW/name).read_bytes()) == wanted, name
before = INDEX.read_bytes()
assert sha(before) == '491adf6bc5c548256502c89d712851755ad6b63d4881a0e48642021004dbabe6'
published = stamp()
block = ('- Added '+published+': the [AF5 finite-matrix reading order](../reviews/frr7_frr8_late_af5_001/af5_matrix_extension/INDEX.md) leads to its [standalone proof](../reviews/frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md) and [independent record and rational checks](../reviews/frr7_frr8_late_af5_001/root_review_002.json). In the specified eleven-policy WDL matrix, every optimal mixture assigns one third each to AF5 and the guard, and splits the remaining third between P5 and AS1C. The seven other policies have zero weight. The proof also allows the two added fortress rows with unmeasured AF5 entries and their mutual entry under its stated bounds. This is a conditional finite-table result. For the associated frr8 games, use the [HP erratum](../reviews/frr7_frr8_late_af5_001/hp_erratum_001/ERRATUM.md) and its [independent recount](../reviews/frr7_frr8_late_af5_001/root_hp_erratum_review_002.json): AF5 finishes 790:735 in both seats. The original sealed review retains its incorrect 795:740 sentence as historical evidence.\n')
links=[]
for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', block):
 p=INDEX.parent/target
 assert p.is_file(),target
 data=p.read_bytes()
 links.append({'label':label,'target_relative_to_analysis':target,'project_path':str(p.resolve().relative_to(Path.cwd())),'sha256':sha(data),'bytes':len(data)})
after=before.rstrip(b'\n')+b'\n'+block.encode()
OUT.mkdir()
(OUT/'index_before.md.gz').write_bytes(gzip.compress(before,mtime=0))
(OUT/'index_after.md.gz').write_bytes(gzip.compress(after,mtime=0))
(OUT/'index.diff').write_text(''.join(difflib.unified_diff(before.decode().splitlines(keepends=True),after.decode().splitlines(keepends=True),fromfile='analysis/README.md before',tofile='analysis/README.md after')))
INDEX.write_bytes(after)
assert INDEX.read_bytes()==after
receipt={'schema':'root-navigation-publication-003','started_utc':started,'published_utc':published,'completed_utc':stamp(),'verdict':'CONFIRMED','index_path':str(INDEX),'index_before_sha256':sha(before),'index_after_sha256':sha(after),'review_inputs':expected,'added_links':links,'scope':'Append one final AF5 reading-route bullet and explicit precedence of the retained HP erratum. All sealed proofs, guides, reviews and historical errors remain byte-identical.','script_sha256':sha(Path(__file__).read_bytes())}
(OUT/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':str(OUT/'RECEIPT.json'),'sha256':sha((OUT/'RECEIPT.json').read_bytes()),'published_utc':published,'index_after_sha256':sha(after),'added_links':len(links)},indent=2))

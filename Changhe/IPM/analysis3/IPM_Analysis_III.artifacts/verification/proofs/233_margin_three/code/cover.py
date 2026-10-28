from pathlib import Path
from fractions import Fraction as F
import json,gzip,hashlib
LANE=Path(__file__).resolve().parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def reconstruct(target=F(3)):
 bpath=LANE/'proofs/68_independent_global_coefficients/evidence/full.json';opath=LANE/'proofs/82_margin_refinement/evidence/refinement.json.gz';pp=LANE/'proofs/193_old_margin_refinement/evidence';base=json.loads(bpath.read_text());old=json.loads(gzip.decompress(opath.read_bytes()));meta=json.loads((pp/'metadata.json').read_text());aud=json.loads((pp/'audit.json').read_text());res=json.loads((pp/'result.json').read_text());assert aud['status']=='CONFIRMED';assert sha(pp/'replacements.jsonl.gz')==res['journal_sha256']==aud['journal_sha256'];assert sha(bpath)==meta['base_sha256'];assert sha(opath)==meta['old_sha256']
 changed=set();all_leaves=[]
 with gzip.open(pp/'replacements.jsonl.gz','rt') as f:
  for line in f:
   row=json.loads(line)
   for rec in row['records']:
    key=(row['row'],*rec['parent'][:2]);assert key not in changed;changed.add(key)
    for child in rec['children']:all_leaves.append((row['row'],['193',rec['parent'][0],rec['parent'][1],child[0]],child[1:5],F(child[5])))
 for j,leaf in enumerate(old['leaves']):
  if (leaf['root'][0],'refined',j) not in changed:all_leaves.append((leaf['root'][0],['82',j],[leaf['t0'],leaf['t1'],leaf['a0'],leaf['a1']],F(leaf['ma_lower']['lower_exact'])))
 parents=[];keptroots=[];keptleaves=0;lowest=None
 for i in meta['kept_roots']:
  row=base['records'][i];lo=F(row['ma_lower']['lower_exact'])
  if lo>=target:keptroots.append(i);lowest=lo if lowest is None else min(lo,lowest)
  else:
   for j in range(128):parents.append(dict(row=i,id=['68',i,j],box=[row['left_exact'],row['right_exact'],str(F(j,256)),str(F(j+1,256))]))
 assert len(all_leaves)==281535 and len(meta['kept_roots'])==1352
 for i,ident,box,lo in all_leaves:
  if lo>=target:keptleaves+=1;lowest=lo if lowest is None else min(lo,lowest)
  else:parents.append(dict(row=i,id=ident,box=box))
 return base,parents,dict(kept_roots=keptroots,kept_leaves=keptleaves,lowest_kept_exact=str(lowest),prior_hashes={str(p.relative_to(LANE)):sha(p) for p in (bpath,opath,pp/'metadata.json',pp/'result.json',pp/'audit.json',pp/'replacements.jsonl.gz')})

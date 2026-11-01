"""Replace redundant old canonical coefficient exports by exact reconstruction recipes."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,pickle,time,sys
sys.dont_write_bytecode=True
from read_checkpoint_archive import read_bytes as read_checkpoint
from read_selected_archive import reconstruct
start=time.monotonic()
candidates=[]
for p in Path('research/82_weighted_loss_criterion').glob('update_N*/verification/input_checkpoint.pkl.gz'):
 if not p.exists():continue
 try:N=int(p.parts[-3].split('_')[1][1:])
 except (IndexError,ValueError):continue
 candidates.append((N,str(p),p))
N,_,base=max(candidates);assert N>320
rawbase=read_checkpoint(base);digest=sha256(rawbase).hexdigest();basebytes=len(rawbase);state=pickle.loads(rawbase);del rawbase
root=Path('research/64_log_precision_updates/verification');manifest_path=root/'RECIPE_MANIFEST.json'
manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else dict(format='byte-exact JSON reconstructed from preserved checkpoint',recipes=[],skipped=[])
for p in sorted(root.glob('log_sin1_c3_p512_N*/selected_packed_coefficients.json.gz')):
 try:sourceN=int(p.parent.name.split('_N',1)[1].split('_',1)[0])
 except (IndexError,ValueError):continue
 if sourceN>=N:continue
 compressed=p.read_bytes();raw=gzip.decompress(compressed);old=json.loads(raw)
 recipe=dict(format_version=1,base_checkpoint=str(base),base_sha256=digest,base_bytes=basebytes,base_maximum_order=N,original_path=str(p.with_suffix('')),original_bytes=len(raw),original_sha256=sha256(raw).hexdigest(),old_gzip_path=str(p),old_gzip_bytes=len(compressed),old_gzip_sha256=sha256(compressed).hexdigest(),top_level_order=list(old),header={k:v for k,v in old.items() if k not in ['f','g']},field_order={k:list(old[k]) for k in ['f','g']})
 try:restored=reconstruct(recipe,state=state)
 except (AssertionError,KeyError):
  item=dict(path=str(p),reason='current base does not reproduce exact original JSON bytes')
  manifest['skipped'].append(item);print(json.dumps(item),flush=True);continue
 assert restored==raw
 recipe['verified_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 recipepath=p.with_suffix('.recipe.json');assert not recipepath.exists()
 recipepath.write_text(json.dumps(recipe,indent=2)+'\n')
 # Re-read the recipe and repeat the complete reconstruction before removing the gzip.
 assert reconstruct(json.loads(recipepath.read_text()),state=state)==raw
 manifest['recipes'].append(dict(recipe_path=str(recipepath),**{k:recipe[k] for k in ['base_checkpoint','base_sha256','original_path','original_bytes','original_sha256','old_gzip_bytes','old_gzip_sha256','verified_at_utc']}))
 manifest['actual_elapsed_s']=time.monotonic()-start;manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
 p.unlink();print(json.dumps(manifest['recipes'][-1]),flush=True)
(root/'RECIPE_README.md').write_text('''# Exact reconstruction recipes for old coefficient exports

Some old canonical selected-coefficient JSON gzip files are represented by `.json.recipe.json` files. Each recipe records the preserved full checkpoint dependency, original JSON field order, unchanged metadata, selected order lists, byte count and SHA256. Every reconstruction was compared byte for byte with the original before its gzip was removed. The current selected export is kept directly.

Use `code/read_selected_archive.py ORIGINAL_JSON_GZ_PATH --output RESTORED_JSON_PATH` from the lane directory. The reader follows any later VCDIFF archive of the referenced checkpoint, verifies its original hash, reconstructs the JSON and checks the complete original byte count and SHA256. The output path must not already exist. Account for its uncompressed size and the lane disk limit before restoring. Scripts frozen with earlier audits expect the original filename; restore it when rerunning them, or use the archive reader in new scripts.

RECIPE_MANIFEST.json records both original gzip and JSON hashes. ARCHIVE_MANIFEST.json is historical evidence of the earlier gzip conversion and remains unchanged. Original gzip bytes are not needed by the mathematical checks; original uncompressed bytes are exactly recoverable.
''')
print(json.dumps(dict(complete=True,base=str(base),archived=len(manifest['recipes']),skipped=len(manifest['skipped']),actual_elapsed_s=time.monotonic()-start)),flush=True)

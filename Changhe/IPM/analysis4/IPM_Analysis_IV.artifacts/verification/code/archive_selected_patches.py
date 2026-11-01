"""Archive old selected JSON by exact sparse differences from a preserved checkpoint."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,pickle,time,sys
sys.dont_write_bytecode=True
from read_checkpoint_archive import read_bytes as read_checkpoint
from read_selected_archive import reconstruct
start=time.monotonic()
root=Path('research/64_log_precision_updates/verification')
base=Path('research/82_weighted_loss_criterion/update_N329_20261031T093225Z/verification/input_checkpoint.pkl.gz')
rawbase=read_checkpoint(base);digest=sha256(rawbase).hexdigest();basebytes=len(rawbase);state=pickle.loads(rawbase);del rawbase
manifest_path=root/'PATCH_RECIPE_MANIFEST.json'
manifest=dict(format='byte-exact selected JSON via sparse patches',recipes=[])
def differences(old,new,path):
 if isinstance(old,dict) and isinstance(new,dict):
  assert list(old)==list(new)
  for key in old:yield from differences(old[key],new[key],path+[key])
 elif isinstance(old,list) and isinstance(new,list):
  assert len(old)==len(new)
  for i,(x,y) in enumerate(zip(old,new)):yield from differences(x,y,path+[i])
 elif old!=new:yield [path,old]
for p in sorted(root.glob('log_sin1_c3_p512_N*/selected_packed_coefficients.json.gz')):
 N=int(p.parent.name.split('_N')[1].split('_')[0])
 if N>=300:continue
 compressed=p.read_bytes();raw=gzip.decompress(compressed);old=json.loads(raw)
 recipe=dict(format_version=2,base_checkpoint=str(base),base_sha256=digest,base_bytes=basebytes,base_maximum_order=329,original_path=str(p.with_suffix('')),original_bytes=len(raw),original_sha256=sha256(raw).hexdigest(),old_gzip_path=str(p),old_gzip_bytes=len(compressed),old_gzip_sha256=sha256(compressed).hexdigest(),top_level_order=list(old),header={k:v for k,v in old.items() if k not in ['f','g']},field_order={k:list(old[k]) for k in ['f','g']})
 new={key:({n:state[key][int(n)] for n in old[key]} if key in ['f','g'] else old[key]) for key in old}
 baseline=(json.dumps(new)+'\n').encode();new=json.loads(baseline)
 patch=list(differences(old,new,[]));patchraw=(json.dumps(patch,separators=(',',':'))+'\n').encode();patchgz=gzip.compress(patchraw,compresslevel=6,mtime=0)
 assert len(patchgz)<len(compressed)//2
 patchpath=p.with_suffix('.patch.json.gz');assert not patchpath.exists()
 recipe.update(baseline_bytes=len(baseline),baseline_sha256=sha256(baseline).hexdigest(),patch_file=str(patchpath),patch_bytes=len(patchraw),patch_sha256=sha256(patchraw).hexdigest(),patch_gzip_bytes=len(patchgz),patch_gzip_sha256=sha256(patchgz).hexdigest(),patch_count=len(patch),only_radius_changes=all(len(path)==5 and path[-1]==2 for path,_ in patch))
 patchpath.write_bytes(patchgz)
 assert reconstruct(recipe,state=state)==raw
 recipe['verified_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 recipepath=p.with_suffix('.recipe.json');assert not recipepath.exists();recipepath.write_text(json.dumps(recipe,indent=2)+'\n')
 assert reconstruct(json.loads(recipepath.read_text()),state=state)==raw
 manifest['recipes'].append(dict(recipe_path=str(recipepath),**{key:recipe[key] for key in ['original_bytes','original_sha256','patch_count','only_radius_changes','old_gzip_bytes','patch_gzip_bytes','verified_at_utc']}))
 manifest['actual_elapsed_s']=time.monotonic()-start;manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
 p.unlink();print(json.dumps(manifest['recipes'][-1]),flush=True)
print(json.dumps(dict(complete=True,actual_elapsed_s=time.monotonic()-start,total_saved_bytes=sum(r['old_gzip_bytes']-r['patch_gzip_bytes'] for r in manifest['recipes']))),flush=True)

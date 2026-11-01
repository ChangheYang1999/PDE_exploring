"""Read a selected-coefficient JSON or its byte-verified checkpoint recipe."""
from pathlib import Path
from hashlib import sha256
import gzip,json,pickle
from read_checkpoint_archive import read_bytes as read_checkpoint

def reconstruct(recipe,state=None,base_raw=None):
 if state is None:
  base_raw=read_checkpoint(recipe['base_checkpoint'])
  assert len(base_raw)==recipe['base_bytes'] and sha256(base_raw).hexdigest()==recipe['base_sha256']
  state=pickle.loads(base_raw)
 obj={}
 for key in recipe['top_level_order']:
  if key in ['f','g']:obj[key]={n:state[key][int(n)] for n in recipe['field_order'][key]}
  else:obj[key]=recipe['header'][key]
 raw=(json.dumps(obj)+'\n').encode()
 if recipe.get('format_version',1)==2:
  assert len(raw)==recipe['baseline_bytes'] and sha256(raw).hexdigest()==recipe['baseline_sha256']
  obj=json.loads(raw)
  compressed=Path(recipe['patch_file']).read_bytes()
  assert len(compressed)==recipe['patch_gzip_bytes'] and sha256(compressed).hexdigest()==recipe['patch_gzip_sha256']
  patchraw=gzip.decompress(compressed)
  assert len(patchraw)==recipe['patch_bytes'] and sha256(patchraw).hexdigest()==recipe['patch_sha256']
  patches=json.loads(patchraw);assert len(patches)==recipe['patch_count']
  for path,value in patches:
   current=obj
   for key in path[:-1]:current=current[key]
   current[path[-1]]=value
  raw=(json.dumps(obj)+'\n').encode()
 assert len(raw)==recipe['original_bytes'] and sha256(raw).hexdigest()==recipe['original_sha256']
 return raw

def read_bytes(path):
 path=Path(path)
 if path.exists():
  raw=path.read_bytes();return gzip.decompress(raw) if path.suffix=='.gz' else raw
 recipe_path=path.with_suffix('.recipe.json') if path.suffix=='.gz' else path.with_suffix(path.suffix+'.recipe.json')
 recipe=json.loads(recipe_path.read_text());return reconstruct(recipe)

if __name__=='__main__':
 import argparse,sys
 parser=argparse.ArgumentParser();parser.add_argument('path');parser.add_argument('--output');args=parser.parse_args()
 raw=read_bytes(args.path)
 if args.output:
  out=Path(args.output);assert not out.exists();out.write_bytes(raw)
 else:sys.stdout.buffer.write(raw)

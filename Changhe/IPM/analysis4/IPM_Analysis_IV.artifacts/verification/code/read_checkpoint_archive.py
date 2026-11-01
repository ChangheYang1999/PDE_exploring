"""Load exact original pickle bytes, including a verified VCDIFF archive fallback."""
from pathlib import Path
from hashlib import sha256
import gzip,json,os,subprocess

def read_bytes(path):
 path=Path(path)
 if path.exists():
  raw=path.read_bytes()
  return gzip.decompress(raw) if path.suffix=='.gz' else raw
 meta=json.loads(path.with_suffix('.archive.json').read_text());base=read_bytes(meta['base_path']);assert sha256(base).hexdigest()==meta['base_uncompressed_sha256']
 patch=Path(meta['patch_path']);assert sha256(patch.read_bytes()).hexdigest()==meta['patch_sha256']
 fd=os.memfd_create('checkpoint-base')
 try:
  view=memoryview(base)
  while view:
   n=os.write(fd,view);view=view[n:]
  os.lseek(fd,0,os.SEEK_SET)
  raw=subprocess.run(['xdelta3','-q','-d','-D','-R','-c','-B',str(1 << (len(base)-1).bit_length()),'-s',f'/proc/self/fd/{fd}',str(patch)],pass_fds=(fd,),check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=300).stdout
 finally:os.close(fd)
 assert len(raw)==meta['original_uncompressed_bytes'] and sha256(raw).hexdigest()==meta['original_uncompressed_sha256']
 return raw

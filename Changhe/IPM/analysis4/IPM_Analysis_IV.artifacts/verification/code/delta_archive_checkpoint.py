"""Byte-exact checkpoint archive using a retained base and VCDIFF, with verification."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,os,subprocess,time

def digest_file(path):
 h=sha256()
 with open(path,'rb') as f:
  for chunk in iter(lambda:f.read(2**20),b''):h.update(chunk)
 return h.hexdigest()
def inflate_fd(path):
 fd=os.memfd_create('checkpoint-archive');h=sha256();size=0
 with gzip.open(path,'rb') as f:
  for chunk in iter(lambda:f.read(2**20),b''):
   os.write(fd,chunk);h.update(chunk);size+=len(chunk)
 os.lseek(fd,0,os.SEEK_SET)
 return fd,h.hexdigest(),size
def main():
 ap=argparse.ArgumentParser();ap.add_argument('base');ap.add_argument('target');ap.add_argument('--remove-original',action='store_true');ap.add_argument('--decode-timeout',type=int,default=100);ap.add_argument('--reuse-patch',action='store_true');a=ap.parse_args();start=time.monotonic()
 base,target=Path(a.base),Path(a.target);patch=target.with_suffix('.vcdiff');manifest=target.with_suffix('.archive.json')
 assert not manifest.exists()
 assert patch.exists() if a.reuse_patch else not patch.exists()
 fd_b,hash_b,size_b=inflate_fd(base);fd_t,hash_t,size_t=inflate_fd(target);fd_out=os.memfd_create('verified-checkpoint')
 cmd=['xdelta3','-q','-e','-1','-D','-R','-A','-B',str(1 << (size_b-1).bit_length()),'-s',f'/proc/self/fd/{fd_b}',f'/proc/self/fd/{fd_t}',str(patch)]
 if not a.reuse_patch:subprocess.run(cmd,pass_fds=(fd_b,fd_t),check=True,timeout=420,stderr=subprocess.PIPE)
 subprocess.run(['xdelta3','-q','-d','-D','-R','-c','-B',str(1 << (size_b-1).bit_length()),'-s',f'/proc/self/fd/{fd_b}',str(patch)],pass_fds=(fd_b,),stdout=fd_out,stderr=subprocess.PIPE,check=True,timeout=a.decode_timeout)
 os.lseek(fd_out,0,os.SEEK_SET);h=sha256();size=0
 for chunk in iter(lambda:os.read(fd_out,2**20),b''):h.update(chunk);size+=len(chunk)
 assert size==size_t and h.hexdigest()==hash_t
 result=dict(verified_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),format='VCDIFF of exact uncompressed checkpoint bytes',base_path=str(base),base_uncompressed_sha256=hash_b,base_uncompressed_bytes=size_b,original_path=str(target),original_compressed_sha256=digest_file(target),original_compressed_bytes=target.stat().st_size,original_uncompressed_sha256=hash_t,original_uncompressed_bytes=size_t,patch_path=str(patch),patch_sha256=digest_file(patch),patch_bytes=patch.stat().st_size,byte_exact_roundtrip=True,original_removed=False,actual_elapsed_s=time.monotonic()-start)
 manifest.write_text(json.dumps(result,indent=2)+'\n')
 if a.remove_original:
  assert result['patch_bytes']<result['original_compressed_bytes']
  target.unlink();result['original_removed']=True;manifest.write_text(json.dumps(result,indent=2)+'\n')
 for fd in [fd_b,fd_t,fd_out]:os.close(fd)
 print(json.dumps(result),flush=True)
if __name__=='__main__':
 try:main()
 except subprocess.CalledProcessError as e:print(json.dumps(dict(error='xdelta failed',returncode=e.returncode)));raise SystemExit(1)
 except Exception as e:print(json.dumps(dict(error=type(e).__name__,message=str(e))));raise SystemExit(1)

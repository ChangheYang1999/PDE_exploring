"""Freeze a live checkpoint as a byte-verified VCDIFF against retained evidence."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,os,pickle,shutil,subprocess,time,sys
sys.dont_write_bytecode=True
from read_checkpoint_archive import read_bytes

def write_fd(data):
 fd=os.memfd_create('ipm-byte-archive');view=memoryview(data)
 while view:
  count=os.write(fd,view);view=view[count:]
 os.lseek(fd,0,os.SEEK_SET);return fd

def main():
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('base');p.add_argument('--result-file',required=True);a=p.parse_args();start=time.monotonic()
 assert shutil.disk_usage('.').free>20*10**9
 raw=Path(a.source).read_bytes();state=pickle.loads(raw)
 assert (state['A'],state['B'],state['prec'],state['ring'])==('2','3',512,'arb')
 N=max(state['f']);assert max(state['g'])==N;del state
 base=read_bytes(a.base);base_state=pickle.loads(base);baseN=max(base_state['f']);del base_state;assert N>baseN
 hraw=sha256(raw).hexdigest();hbase=sha256(base).hexdigest();window=1 << (len(base)-1).bit_length()
 fd_b=write_fd(base);fd_t=write_fd(raw);fd_p=os.memfd_create('ipm-vcdiff')
 command=['xdelta3','-q','-e','-1','-D','-R','-A','-c','-B',str(window),'-s',f'/proc/self/fd/{fd_b}',f'/proc/self/fd/{fd_t}']
 subprocess.run(command,pass_fds=(fd_b,fd_t),stdout=fd_p,stderr=subprocess.PIPE,check=True,timeout=420)
 os.lseek(fd_p,0,os.SEEK_SET)
 patch=b''.join(iter(lambda:os.read(fd_p,2**20),b''));os.lseek(fd_p,0,os.SEEK_SET)
 restored=subprocess.run(['xdelta3','-q','-d','-D','-R','-c','-B',str(window),'-s',f'/proc/self/fd/{fd_b}',f'/proc/self/fd/{fd_p}'],pass_fds=(fd_b,fd_p),stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,timeout=300).stdout
 assert restored==raw;del restored
 used=int(subprocess.run(['du','-s','-B1','.'],capture_output=True,text=True,check=True).stdout.split()[0]);assert used+len(patch)<2_975_000_000
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');root=Path('research/82_weighted_loss_criterion')/f'update_N{N}_{stamp}'
 (root/'verification').mkdir(parents=True);target=root/'verification/input_checkpoint.pkl.gz';patchpath=target.with_suffix('.vcdiff');patchpath.write_bytes(patch)
 result=dict(verified_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),format='VCDIFF of exact uncompressed checkpoint bytes',base_path=a.base,base_uncompressed_sha256=hbase,base_uncompressed_bytes=len(base),original_path=str(target),original_uncompressed_sha256=hraw,original_uncompressed_bytes=len(raw),patch_path=str(patchpath),patch_sha256=sha256(patch).hexdigest(),patch_bytes=len(patch),byte_exact_roundtrip=True,original_removed=False,original_not_materialized=True,maximum_order=N,base_maximum_order=baseN,actual_elapsed_s=time.monotonic()-start)
 target.with_suffix('.archive.json').write_text(json.dumps(result,indent=2)+'\n')
 manifest=dict(frozen_at_utc=result['verified_at_utc'],source_path=a.source,input_path=str(target),maximum_order=N,raw_bytes=len(raw),raw_sha256=hraw,archive_format=result['format'],archive_path=str(patchpath),archive_bytes=len(patch),archive_sha256=result['patch_sha256'],root=str(root))
 (root/'verification/input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');Path(a.result_file).write_text(json.dumps(manifest,indent=2)+'\n')
 for fd in [fd_b,fd_t,fd_p]:os.close(fd)
 print(json.dumps(result),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as e:
  import traceback
  print(json.dumps(dict(error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])),flush=True);raise SystemExit(1)

from pathlib import Path
import json,gzip,time,sys
sys.dont_write_bytecode=True
start=time.monotonic()
for N in [210,240,245,255,260,270,280,290]:
 p=next(Path('research/64_log_precision_updates/verification').glob(f'log_sin1_c3_p512_N{N}_*/selected_packed_coefficients.json.gz'))
 raw=gzip.decompress(p.read_bytes());o=json.loads(raw)
 print(json.dumps(dict(N=N,bytes=len(raw),trailing_newline=raw.endswith(b'\n'),default_exact=json.dumps(o).encode()==raw,newline_exact=(json.dumps(o)+'\n').encode()==raw,indent_exact=json.dumps(o,indent=2).encode()==raw,top_keys=list(o),elapsed_s=time.monotonic()-start)),flush=True)

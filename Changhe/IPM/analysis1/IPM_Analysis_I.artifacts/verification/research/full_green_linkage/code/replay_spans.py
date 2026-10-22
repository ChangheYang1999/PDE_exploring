"""Diagnostic replay of whole complete-method streams with fresh caches."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,importlib.util,json,sys
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/full_green_linkage';E=D/'evidence'
p=D/'code/check_boundaries.py';sp=importlib.util.spec_from_file_location('complete_boundary_checker',p);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full');ap.add_argument('--allow-partial',action='store_true');args=ap.parse_args();assert args.tag.replace('_','').isalnum()
 stream=E/(args.tag+'_spans.jsonl');lines=stream.read_text().splitlines();header=json.loads(lines[0]);footer=json.loads(lines[-1]);rows={r['span']:r for r in map(json.loads,lines[1:-1])}
 assert header['type']=='header' and footer['type']=='complete' and (header['full_run'] or args.allow_partial)
 assert header['files']['research/full_green_linkage/code/check_boundaries.py']==c.sha(p)
 for relative,digest in header['files'].items():assert c.sha(B/relative)==digest
 seed=header['sample_seed'];wanted={0,1557}
 for j in (0,1):wanted.add(int.from_bytes(hashlib.sha256((seed+':span:'+str(j)).encode()).digest()[:8],'big')%1558)
 wanted&=set(rows);assert wanted
 with c.np.load(header['green_path'],allow_pickle=False) as g:arrays={k:g[k] for k in ('A_mid','A_rad','B_mid','B_rad')}
 assert c.sha(header['green_path'])==c.GREEN_SHA
 compared=[]
 with gzip.open(B/'research/middle_residual/evidence/original_knots.jsonl.gz','rt') as f:
  ah=json.loads(next(f));assert ah['comparison_grid_sha256']==c.GREEN_SHA
  for line in f:
   rec=json.loads(line)
   if rec['type']=='complete':break
   si=rec['span']
   if si not in wanted:continue
   digest=hashlib.sha256();count=0;c.expa.cache_clear();c.convolution.cache_clear()
   for index,t,n,values in c.evaluate_span(rec):
    for name,engines in values.items():
     bounds={eng:c.ends(v) for eng,v in engines.items()}
     m=F.from_float(float(arrays[name+'_mid'][index,n-1]));r=F.from_float(float(arrays[name+'_rad'][index,n-1]));assert r>=0
     for lo,hi in bounds.values():assert m-r<=lo<=hi<=m+r
     assert max(bounds['arb'][0],bounds['iv'][0])<=min(bounds['arb'][1],bounds['iv'][1])
     data={'boundary':index,'n':n,'array':name,'t_exact':str(t),'target_mid_hex':float(arrays[name+'_mid'][index,n-1]).hex(),'target_rad_hex':float(arrays[name+'_rad'][index,n-1]).hex(),'bounds':{eng:list(map(str,q)) for eng,q in bounds.items()}}
     digest.update(json.dumps(data,separators=(',',':'),sort_keys=True).encode()+b'\n');count+=1
   assert count==2*261*rows[si]['boundaries'] and digest.hexdigest()==rows[si]['stream_sha256'],(si,'replay hash mismatch')
   compared.append({'span':si,'entries_per_engine':count,'stream_sha256':digest.hexdigest()});print(json.dumps(compared[-1]),flush=True)
 assert {r['span'] for r in compared}==wanted
 assert c.sha(header['green_path'])==c.GREEN_SHA and c.sha(B/'research/middle_residual/evidence/original_knots.jsonl.gz')==c.ARCHIVE_SHA
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_DIAGNOSTIC_WHOLE_SPAN_REPLAY','full_input_run':header['full_run'],'spans':compared,'stream_sha256':c.sha(stream),'checker_sha256':c.sha(p),'source_sha256':c.sha(Path(__file__)),'scope':'Fresh same-method replay with empty caches. This is diagnostic, not an independent third method or an omitted-span proof.'}
 (E/(args.tag+'_replay.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

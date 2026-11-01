"""Selected exact Cartesian checks of the extended prime-denominator scan."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from hashlib import sha256
import argparse,json,sys,time
sys.dont_write_bytecode=True
from flint import arb,fmpq,ctx
from rational_scan_audit import compute
ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='67:50');args=ap.parse_args()
ctx.prec=640;start=time.monotonic();now=datetime.now(timezone.utc)
root=Path('research/80_compatibility_size_criterion/verification')/('extended_scan_'+now.strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
source=Path('../a4-num/notes/kappa_scan_arb.jsonl');raw=source.read_bytes();(root/'sources/numerics_scan.jsonl').write_bytes(raw)
reported={(r['p'],r['a']):r for r in map(json.loads,raw.splitlines())}
for name in ['extended_kappa_exact_audit.py','rational_scan_audit.py','laurent_log_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
rows=[]
for pair in args.pairs.split(','):
 p,a=map(int,pair.split(':'));assert (p,a) in reported
 result=compute(Fraction(a,p),{1:'1'},p);result.pop('density_at_resonance')
 k=fmpq(result['kappa_exact']);assert k!=0
 log=abs(arb(k)).log()/arb(10).log();ref=reported[(p,a)]
 difference=abs(log-arb(ref['log10_abs_kappa']));assert difference<arb('1e-10')
 result.update(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),p=p,a=a,log10_abs_kappa=log.str(40,radius=True),log10_abs_kappa_over_p=(log/p).str(40,radius=True),reported_float_difference=difference.str(20,radius=True),reported_certified_nonzero=ref['certified_nonzero'],reported_status=ref['status'],matches_reported_log_to_1e_minus_10=True)
 assert ref['certified_nonzero'] and ref['status']=='incompatible'
 (root/('p'+str(p)+'_a'+str(a)+'.json')).write_text(json.dumps(result,indent=2)+'\n')
 brief={key:value for key,value in result.items() if key not in ['kappa_exact','forcing_exact']};rows.append(brief);print(json.dumps(brief),flush=True)
 summary=dict(checked_at_utc=now.isoformat(timespec='seconds'),source_path=str(source),source_sha256=sha256(raw).hexdigest(),actual_elapsed_s=time.monotonic()-start,rows=rows)
 (root/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),actual_elapsed_s=time.monotonic()-start,completed=len(rows))),flush=True)

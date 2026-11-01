"""Aggregate and independently decode every completed prime-resonance certificate."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import isqrt,gcd
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
ctx.prec=640;start=time.monotonic();root=Path('research/80_compatibility_size_criterion/verification/complete_prime_scan');root.mkdir(exist_ok=True)
source=Path('../a4-num/notes/kappa_scan_arb.jsonl');raw=source.read_bytes();target=[json.loads(line) for line in raw.splitlines()];refs={(r['p'],r['a']):r for r in target};assert len(refs)==len(target)==502
available={};summaries={}
for path in sorted(root.parent.glob('cartesian_arb_scan_*/checks.json')):
 data=json.loads(path.read_text());summaries[str(path)]=dict(sha256=sha256(path.read_bytes()).hexdigest(),completed_count=data['completed_count'],arithmetic_bits=data['precision_bits'])
 for row in data['rows']:
  p,a=row['p'],row['a'];rp=path.parent/f'p{p}_a{a}.json';full=json.loads(rp.read_text());available.setdefault((p,a),[]).append((rp,full))
assert refs.keys()<=available.keys()
rows=[];duplicates=0;exact=0;checks=0;maxrel=arb(0);maxdiff=arb(0);primes=set()
for (p,a),ref in sorted(refs.items()):
 assert 4<=a<p and a%2==0 and gcd(a,p)==1 and all(p%d for d in range(2,isqrt(p)+1));primes.add(p)
 cases=available[(p,a)];path,item=cases[0];ball=arb(*unpack(item['kappa_dyadic_ball']));assert not ball.contains(0)
 assert item['first_resonance_order']==p and item['resonant_stream_frequency']==a-2 and item['forcing_nonzero'] and item['certified_nonzero']
 for otherpath,other in cases[1:]:
  second=arb(*unpack(other['kappa_dyadic_ball']));assert second.overlaps(ball) and not second.contains(0);duplicates+=1
 log=abs(ball).log()/arb(10).log();difference=abs(log-arb(ref['log10_abs_kappa']));assert difference<arb('1e-9');maxdiff=maxdiff.max(difference)
 relative=ball.rad()/abs(ball.mid());maxrel=maxrel.max(relative)
 checks+=item['forbidden_and_symmetry_checks'];exact+=int(item.get('independent_exact_value_contained',False))
 rows.append(dict(p=p,a=a,delta_exact=item['delta_exact'],certificate_path=str(path),certificate_sha256=sha256(path.read_bytes()).hexdigest(),kappa_dyadic_ball=item['kappa_dyadic_ball'],log10_abs_kappa=log.str(40,radius=True),log10_abs_kappa_over_p=(log/p).str(40,radius=True),certified_nonzero=True,original_forbidden_and_symmetry_checks=item['forbidden_and_symmetry_checks']))
summary=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,target_count=len(refs),certified_nonzero_count=len(rows),source_path=str(source),source_sha256=sha256(raw).hexdigest(),source_bytes=len(raw),primes=sorted(primes),minimum_delta=min((arb(a)/p for p,a in refs),key=lambda x:float(x.mid())).str(30,radius=True),maximum_delta=max((arb(a)/p for p,a in refs),key=lambda x:float(x.mid())).str(30,radius=True),duplicate_certificates_compared=duplicates,certificates_with_separate_exact_value_check=exact,original_forbidden_and_symmetry_checks=checks,maximum_relative_radius=maxrel.str(40,radius=True),maximum_source_float_log_difference=maxdiff.str(40,radius=True),arithmetic_bits=ctx.prec,actual_elapsed_s=time.monotonic()-start,rows=rows,batch_summaries=summaries,scope='Finite nonvanishing at502 specified rational centers for f1=sin(theta). No density of such centers, infinite subsequence or irrational divergence condition follows from this scan.')
(root/'checks.json').write_text(json.dumps(summary,indent=2)+'\n');(root/'source_scan.jsonl').write_bytes(raw);(root/'aggregate_prime_certificates.py.txt').write_bytes(Path(__file__).read_bytes())
files={p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.iterdir() if p.is_file() and p.name!='MANIFEST.json'};(root/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['rows','batch_summaries']}),flush=True)

"""Bind and accept the independent scalar partial-fraction audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/rational_pole_moments';DEST=BASE/'reviews/T4'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=2048
 own=json.loads((BASE/'verification/result.json').read_text());peer=json.loads((DEST/'result.json').read_text());manifest=json.loads((DEST/'MANIFEST.json').read_text())
 assert all(H(DEST/name)==row['sha256'] for name,row in manifest['files'].items())
 assert peer['all_passed'] and peer['proof_sha256']==H(DEST/'PROOF.md') and peer['code_sha256']==H(DEST/'check.py')
 for name,p in [('N4_PROOF.md',BASE/'PROOF.md'),('moments.py',BASE/'code/moments.py'),('N4_check.py',BASE/'code/check.py'),('N4_result.json',BASE/'verification/result.json')]:assert peer['source_hashes'][name]==H(p)
 assert len(own['fixtures'])==31 and len(peer['fixtures'])==39
 data={z['name']:z for z in peer['fixtures']};assert len(data)==39
 checks=[]
 for a in own['fixtures']:
  b=data[a['name']]
  assert Q(a['b'])==Q(b['b']) and list(map(Q,a['numerator']))==list(map(Q,b['numerator']))
  assert [(Q(x),k) for x,k in a['factors']]==[(Q(x),k) for x,k in b['factors']]
  comparisons={key:arb(b['own']).overlaps(arb(a[key])) for key in ['value','independent_value']}
  assert all(comparisons.values()) and all(b['comparisons'].values()) and b['accuracy_bits']>250
  checks.append({'name':a['name'],'comparisons':comparisons,'peer_comparison_flags':b['comparisons']})
 extras=set(data)-{z['name'] for z in own['fixtures']}
 assert extras=={f'resonance_{k}' for k in range(2,9)}|{'near_integrability_endpoint'}
 assert all(all(data[k]['comparisons'].values()) and data[k]['accuracy_bits']>250 for k in extras)
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):H(p) for p in [Path(__file__),BASE/'verification/result.json',DEST/'result.json',DEST/'MANIFEST.json',DEST/'ACCEPTANCE_PROOF.md']},'original_fixture_count':31,'additional_fixture_count':8,'comparisons':checks,'extra_names':sorted(extras),'all_passed':True,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-190 scalar primitive and fixture application; no candidate norm claim'}
 with (DEST/'ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('ACCEPTED scalar',out['utc'],out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

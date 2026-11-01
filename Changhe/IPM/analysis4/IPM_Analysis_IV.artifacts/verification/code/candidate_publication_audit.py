"""Exact polar extraction and frozen Candidate 007 publication-table audit."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime,timezone
from collections import defaultdict
import json,re,sys,time
sys.dont_write_bytecode=True
ROOT=Path('research/295_candidate_publication_audit')
t0=time.monotonic()
def ref(p):
 p=Path(p);return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def clean(d):return {k:v for k,v in d.items() if v}
def parse(d):return {int(k):F(v) for k,v in d.items()}
archive_path=Path('research/02_candidate007/data/leading_exact.json')
old=json.loads(archive_path.read_text());source=Path(old['input']);data=json.loads(source.read_text())
manifest=source.with_name('MANIFEST.json');man=json.loads(manifest.read_text());sector=source.with_name('sector_table.json')
assert ref(source)['sha256']==old['input_sha256']==next(x['sha256'] for x in man['coefficient_files'] if x['name']==source.name)
assert ref(manifest)['sha256']==old['manifest_sha256']
assert ref(sector)['sha256']==old['sector_table_sha256']==man['sector_table']['sha256']
c=F(data['cl_exact']);assert c==F(man['c_l_exact'])==F(old['c'])==F(4076476460239181,2**51)
gamma=1/c;delta=1-gamma;q=3+gamma;s=q-2
assert gamma==F(old['gamma']) and delta==F(old['delta'])==F(1824676646553933,4076476460239181)
C=defaultdict(F);count=0
for row in data['generators']:
 if row['j']!=0:continue
 assert row['spec'][0] in ('mono','leg')
 C[int(row['m'])]+=F(row['coef']);count+=1
C=clean(C);assert count==old['branch_zero_generators']==416
assert {2*m:v for m,v in C.items()}==parse(old['potential'])
D={m:(q*q-4*m*m)*v for m,v in C.items()}
a={1:-s*D.get(0,F(0))+q*D.get(1,F(0))/2}
for k in range(1,max(C)+1):a[2*k+1]=F(2*k-q+2)*D.get(k,F(0))/2+F(q+2*k)*D.get(k+1,F(0))/2
a=clean(a);assert a==parse(old['density']) and sorted(a)==list(range(1,20,2))
dx=defaultdict(F)
for m,v in C.items():
 ell=2*m;dx[ell+1]+=(q-ell)*v/2;dx[abs(ell-1)]+=(q+ell)*v/2
b=defaultdict(F)
for ell,v in clean(dx).items():
 for mode,value in [(ell+1,(q-1-ell)*v/2),(ell-1,-(q-1+ell)*v/2)]:
  if mode:b[abs(mode)]+=(1 if mode>0 else -1)*value
b=clean(b);assert b==parse(old['stream'])
for ell,v in b.items():
 assert 2*(ell*ell-(gamma+1)**2)*v==(gamma-ell+1)*a.get(ell-1,F(0))+(gamma+ell+1)*a.get(ell+1,F(0))
paper=Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md');text=paper.read_text()
start=text.index('### 8.5 Candidate 007');end=text.index('\n## ',start)
excerpt=text[start:end];snapshot=ROOT/'sources/theory_section_8_5.md';snapshot.write_text(excerpt)
rows=re.findall(r'- \$a_\{(\d+)\}\$: \$u=(-?\d+)\$, \$v=(\d+)\$',excerpt)
published={int(m):F(int(u),int(v)) for m,u,v in rows};assert len(rows)==10 and published==a
assert '4076476460239181/2^{51}' in excerpt and '1824676646553933/4076476460239181' in excerpt
result=dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,method='direct Fraction polar derivatives, independent of Cartesian operators',inputs=[ref(p) for p in [source,manifest,sector,archive_path]],publication_full_source_at_snapshot=ref(paper),publication_excerpt=ref(snapshot),c=str(c),gamma=str(gamma),delta=str(delta),branch_zero_generators=count,nonzero_potential_moments=len(C),density_coefficients=len(a),stream_coefficients=len(b),poisson_identities=len(b),publication_rational_pairs=len(rows),density={str(m):str(v) for m,v in a.items()},actual_elapsed_s=time.monotonic()-t0)
(ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'sources/candidate_publication_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ('inputs','density')}))

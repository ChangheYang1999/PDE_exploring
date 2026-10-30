"""Own exact checks accompanying the independently reviewed analytic proof."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,time,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]; B=ROOT/'research/scaled_density_injectivity'
def sha(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);d=sha(p);assert h is None or h==d,(p,h,d)
  inputs[str(p.relative_to(ROOT))]=d;return p
 def read(p):return json.loads(bind(p).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 for n,d in prep['sources'].items():bind(B/'source'/n,d['sha256'])
 own=read(ROOT/'research/scaled_rank_peer/verification/result.json')
 for p,h in own['inputs'].items():bind(ROOT/p,h)
 for p,d in own['frozen_sources'].items():bind(ROOT/p,d['stored_sha256'])
 assert own['verdict'].startswith('CONFIRMED potential dimension2174')
 shapes=read(B/'source/T4322_shapes.json');output=(B/'source/check_T4322.out').read_text()
 assert output.rstrip().endswith('all checks passed')
 review=(B/'source/REVIEWS_v33.md').read_text();accept=(B/'source/T4_ACCEPTANCE.md').read_text()
 assert 'T4-322 is AUDITED:' in review and 'T4-322 is AUDITED.' in accept
 c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma
 ps=[2-(j+1)*delta/2 for j in range(8)]
 assert list(map(str,ps))==own['p_j']
 diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert list(map(str,diffs))==own['noninteger_differences']
 checks['eight_noninteger_branches']=all(p.denominator!=1 for p in ps)
 checks['twenty_eight_noninteger_differences']=all(p.denominator!=1 for p in diffs)
 checks['growth_below_four']=2*ps[0]==3+gamma<4
 checks['fourth_derivative_decay']=gamma-1<0
 checks['new_growth_strictly_smaller']=all(2*ps[j]-8<3+gamma for j in (1,2,3))
 oldpath=ROOT/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json';old=read(oldpath)
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 oldshapes=sorted(map(shape,old['generators']));assert len(set(oldshapes))==1922
 assert sha(oldpath)==shapes['sources']['old_basis.json']
 assert oldshapes==sorted((j,m,tuple(s)) for j,m,s in shapes['shapes']['old_basis.json']['gens'])
 rows=[]
 for num,R in [(16,25),(17,50)]:
  name=f'C1-N1-{num:03d}-legqs{R}-quot013';directory=ROOT/'research/candidate_audits/data'/name
  manifest=read(directory/'MANIFEST.json');entry=manifest['coefficient_files'][0];rawp=bind(directory/entry['name'],entry['sha256']);raw=read(rawp)
  label=f'candidate{num:03d}.json';assert sha(rawp)==shapes['sources'][label] and Q(raw['cl_exact'])==c
  actual=sorted(map(shape,raw['generators']));peer=sorted((j,m,tuple(s)) for j,m,s in shapes['shapes'][label]['gens'])
  expected=sorted(oldshapes+[(j,m,('legqs',0,N,4,R)) for j in (1,2,3) for m in range(9,16) for N in range(12)])
  assert actual==peer==expected and len(set(actual))==2174
  rank=next(r for r in own['rows'] if r['candidate']==name)
  assert rank['raw_sha256']==sha(rawp) and rank['potential_dimension']==2174 and len(rank['pole_witnesses'])==84
  assert all(w['independent_peer_equal'] and Q(w['laurent_coefficient'])!=0 for w in rank['pole_witnesses'])
  rows.append({'candidate':name,'raw_sha256':sha(rawp),'exact_shapes':2174,'potential_rank_dependency':2174,'density_rank':2174,'Laurent_witnesses':84,'all_peer_shapes_equal':True})
 assert all(checks.values()) and all(sha(ROOT/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'branch_exponents':list(map(str,ps)),'branch_differences':list(map(str,diffs)),'growth_exponent':str(3+gamma),'fourth_derivative_exponent':str(gamma-1),'rows':rows,'own_rank_dependency_sha256':sha(ROOT/'research/scaled_rank_peer/verification/result.json'),'inputs':inputs,'foreign_code_executed':False,'analytic_review':'Full proof reread; Opus R1-036 accepted through T4-332. Finite arithmetic is evidence for its exact hypotheses, not a replacement for the proof.','verdict':'CONFIRMED density injectivity and density dimension 2174 for both exact scaled spaces; no quantitative conditioning or inverse claim'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['verdict'],sha(B/'verification/result.json'),out['elapsed_seconds'])
if __name__=='__main__':main()

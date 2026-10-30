"""Finite exact composition audit. Reuses accepted integral certificates."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,re,time
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(rel):return json.loads((B/rel).read_text())
def enclosure(s):
 s=str(s).strip()
 if s.startswith('['):
  assert s.endswith(']') and ' +/- ' in s,s
  mid,err=s[1:-1].split(' +/- ');m=Q(mid);e=Q(err);assert e>=0
  return m-e,m+e
 q=Q(s);return q,q
def abs_lower(lo,hi):
 assert lo<=hi
 if lo>0:return lo
 if hi<0:return -hi
 return Q(0)
def exact(q):return str(q)
checks=[]
def check(label,condition):
 assert condition,label
 checks.append(label)
start=time.monotonic();captured=datetime.now(timezone.utc).isoformat()
for entry in read('data/manifest.json'):
 check('file '+entry['local'],sha(B/entry['local'])==entry['sha256'])
reg=read('data/registry.json')['rows'];cov=read('data/coverage.json');families=read('data/families.json');floor=Q(cov['floor_exact']);common=Q(families['scalar_upper_exact']);graded=Q(families['graded_upper_exact'])
check('complete frozen registry',[r['number'] for r in reg]==list(range(1,28)))
check('exactly24 witnesses',[r['number'] for r in cov['rows']]==[i for i in range(2,27) if i!=11])
check('cases001011027 kept separate',[r['number'] for r in cov['separate_cases']]==[1,11,27])
for r in reg:
 d=read(r['manifest']);check(f"registry ID {r['number']}",d['id']==r['id'])
 check(f"raw hash {r['number']}",d['coefficient_files'][0]['sha256']==r['raw_sha256'])
 check(f"exponent {r['number']}",Q(d['c_l_exact'])==Q(r['c_exact'])==Q('4076476460239181/2251799813685248'))
rows=[]
for row in cov['rows']:
 n=row['number'];regrow=reg[n-1];d=read(row['result'])
 check(f'result hash {n}',sha(B/row['result'])==row['result_sha256'])
 check(f'proof hash {n}',sha(B/row['proof'])==row['proof_sha256'])
 check(f'raw ID binding {n}',regrow['id']==row['id'] and regrow['raw_sha256']==row['raw_sha256'])
 inputsha=d.get('source_sha256',d.get('canonical_sha256'))
 check(f'actual input binding {n}',inputsha==row['input_sha256'])
 if row['proof_hash_embedded']:
  ph=d.get('proof_sha256')
  if ph is None:
   vals=[v for k,v in d['inputs'].items() if k.endswith('/PROOF.md') and v==row['proof_sha256']]
   check(f'embedded proof unique {n}',len(vals)==1);ph=vals[0]
  check(f'embedded proof binding {n}',ph==row['proof_sha256'])
 if row['bridge_kind']=='raw':check(f'raw numerical input {n}',inputsha==row['raw_sha256'])
 else:
  br=read(row['bridge']);key='source_sha256' if row['bridge_kind']=='local_canonical_build' else 'generator_sha256'
  check(f'raw canonical bridge {n}',br[key]==row['raw_sha256'] and br['canonical_sha256']==inputsha)
  if row['bridge_kind']=='local_canonical_build':check(f'embedded build binding {n}',sha(B/row['bridge'])==d['build_sha256'])
 review=(B/row['review_excerpt']).read_text()
 check(f'accepted review {n}',review.startswith('## '+row['review_ledger']) and 'CONFIRMED' in review)
 if 'rows' in d:
  rs=[r for r in d['rows'] if r['k']==row['probe_k']];check(f'unique localized probe {n}',len(rs)==1);v=rs[0]
  lo,hi=enclosure(v['pairing']);D=enclosure(v['D'])[1];H=enclosure(v['gradient_sup_upper_ball'])[1]
  check(f'localized independent comparisons {n}',all(v['comparisons'].values()))
 else:
  v=d;lo,hi=enclosure(v['pairing'])
  D=enclosure(v['D'])[1] if 'D' in v else enclosure(v['M'])[1]+enclosure(v['C'])[1]
  cert=v.get('sup_certificate',v.get('gradient_certificate'));check(f'gradient certificate present {n}',isinstance(cert,dict) and 'H_upper_exact' in cert)
  H=Q(cert['H_upper_exact'])
  if 'comparisons' in v:check(f'accepted independent scalar comparisons {n}',all(v['comparisons'].values()))
 I=abs_lower(lo,hi)
 check(f'positive norm coefficients {n}',I>0 and D>0 and H>0)
 gap=I-D*floor-H*floor**2;check(f'strict weak floor {n}',gap>0)
 rows.append({'number':n,'id':row['id'],'I_lower_exact':exact(I),'D_upper_exact':exact(D),'H_upper_exact':exact(H),'tested_L2_floor_exact':str(floor),'positive_gap_exact':exact(gap),'result_sha256':row['result_sha256'],'proof_sha256':row['proof_sha256'],'review':row['review_ledger'],'verdict':'CONFIRMED fixed-c no correction of L2 norm <=1/1000, reusing accepted integrals'})
fr=[]
check('eight scalar instances',len(families['rows'])==8)
for row in families['rows']:
 mu=Q(row['mu']);C=Q(row['C']);cu=Q(row['cU']);sqrtw=Q(row['sqrtW2']);check('positive tuple '+row['name'],min(mu,C,cu,sqrtw)>0)
 b2=4*mu**3/(27*C*cu**2*sqrtw**2)
 check('cubic optimum '+row['name'],mu-3*C*(mu/(3*C))==0)
 check('common scalar ceiling '+row['name'],b2<common**2)
 fr.append({'name':row['name'],'critical_s_exact':str(mu/(3*C)),'L2_ceiling_squared_exact':str(b2),'common_upper_exact':str(common)})
check('common scalar below weak floor',common<floor)
check('graded squared formula',Q(50)**2/(651**2*28248)==Q(families['graded_square_exact']))
check('graded cubic optimum',Q(1,2)-3*4708*Q(1,28248)==0)
check('graded rational outward comparison',168**2<28248 and Q(50,651*168)==graded)
check('graded below weak floor',graded<floor)
check('trans statL common scalar ceiling',graded/512<common)
mat=read('source/matrix_rows.json');check('matrix all105 rows',[x['row'] for x in mat]==list(range(1,106)))
# Reparse the frozen table to detect a stale derived row file.
lines=(B/'source/closure_matrix.md').read_text().splitlines();table=[]
for line in lines:
 if re.match(r'^\|\s*\d+\s*\|',line):
  vals=[x.strip() for x in re.split(r'(?<!\\)\|',line)[1:-1]]
  check('matrix field count '+vals[0],len(vals)==11);table.append(vals)
check('matrix derived rows count',len(table)==len(mat))
for d,v in zip(mat,table):
 check('matrix source row '+str(d['row']),list(d.values())==[int(v[0])]+v[1:])
coverage=[];seen=set()
for r in mat:
 ids=sorted(set(map(int,re.findall(r'C1-N1-(\d{3})',r['candidate']))))
 for n in ids:
  check(f'matrix registered candidate {n}',1<=n<=27);seen.add(n)
  if n in [11,27]:status='OPEN; no accepted witness in this audit';check(f'open matrix case {n} row{r["row"]}','OPEN' in r['status'])
  elif n==1:status='L2 forcing inapplicable; stronger annular L2 exclusion pending Opus review'
  else:status='fixed-c scalar/original-graded balls excluded by strict weak floor; any dyadic row separate'
  coverage.append({'number':n,'matrix_row':r['row'],'framework':r['framework'],'matrix_status':r['status'],'H18_scope':status})
check('every registered snapshot appears in matrix',seen==set(range(1,28)))
result={'started_utc':captured,'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'checker_sha256':sha(Path(__file__)),'proof_sha256':sha(B/'PROOF.md'),'manifest_sha256':sha(B/'data/manifest.json'),'checks_passed':len(checks),'weak_candidates':rows,'scalar_families':fr,'graded_relaxed_upper_exact':str(graded),'trans_statL_relaxed_upper_exact':str(graded/512),'matrix_coverage':coverage,'separate_cases':cov['separate_cases'],'verdict':'CONFIRMED finite exact composition for24fixed-c L2 witnesses and stated scalar/original-graded margins.001 stronger conclusion OPEN independent Opus review;011and027OPEN. No integral recomputation.'}
(B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n')
(B/'verification/checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print('PASS',len(checks),'checks;',len(rows),'weak candidates;',len(fr),'scalar instances;',len(coverage),'matrix candidate rows;',result['elapsed_s'],'seconds')

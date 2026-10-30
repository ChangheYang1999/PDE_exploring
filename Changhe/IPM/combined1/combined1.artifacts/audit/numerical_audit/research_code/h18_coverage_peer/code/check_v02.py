"""Own exact-rational finite composition, using accepted input certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/h18_coverage_peer'
def h(data):return sha256(data).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def interval(text):
 text=str(text).strip()
 if text.startswith('['):
  match=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',text);assert match,text
  mid,rad=map(Q,match.groups());assert rad>=0;return mid-rad,mid+rad
 x=Q(text);return x,x

def main():
 t0=time.monotonic();start=now();checks={};inputs={};cache={}
 def ck(name,value):
  assert name not in checks,name
  checks[name]=bool(value);assert value,name
 def bind(path,expected=None):
  path=Path(path);path=path if path.is_absolute() else B/path;assert path.resolve().is_relative_to(R)
  data=path.read_bytes();digest=h(data)
  if expected:assert digest==expected,(path,digest,expected)
  inputs[str(path.relative_to(R))]=digest;return data
 prep=json.loads(bind('verification/PREPARE.json'));ck('proof preceded checker',not prep['checker_exists'])
 for name,key in [('PROOF.md','proof_sha256'),('STORAGE_PROOF_v03.md','storage_proof_sha256'),('STORAGE_PROOF_v02.md','gzip_proof_sha256'),('code/freeze.py','first_freezer_sha256'),('code/freeze_v02.py','second_freezer_sha256'),('code/freeze_v03.py','freeze_code_sha256')]:bind(name,prep[key])
 bind(Path(__file__).resolve());bind('DISPLAY_PROOF_v02.md');bind('code/check.py');bind(R/'logs/h18_coverage_peer.out')
 manifest=json.loads(bind('source/MANIFEST.json',prep['manifest_sha256']));index={}
 for entry in manifest:
  ck('unique '+entry['local'],entry['local'] not in index)
  raw=bind(entry['storage'],entry['stored_sha256']);ck('stored bytes '+entry['local'],len(raw)==entry['stored_bytes'])
  data=gzip.decompress(raw) if entry['gzip'] else raw
  ck('decoded hash '+entry['local'],h(data)==entry['sha256'] and len(data)==entry['bytes'])
  index[entry['local']]=entry;cache[entry['local']]=data
 def read(name):return json.loads(cache[name])
 def txt(name):return cache[name].decode()
 def t4(name):return read('source/T4/'+name)
 reg=t4('data/registry.json')['rows'];coverage=t4('data/coverage.json');family=t4('data/families.json');peer=t4('verification/result.json');T2=read('source/T2/artifacts/data/review_t4_459_results.json')
 ck('T4 target proof',peer['proof_sha256']==h(cache['source/T4/PROOF.md']))
 ck('T4 target checker',peer['checker_sha256']==h(cache['source/T4/code/check.py']))
 ck('T4 manifest',peer['manifest_sha256']==h(cache['source/T4/data/manifest.json']))
 ck('T4 success',peer['checks_passed']==806)
 ck('T2 success',T2['checks']==189 and T2['fails']==[])
 for name,expected in T2['inputs'].items():ck('T2 input '+name,index['source/T2_inputs/'+name]['sha256']==expected)
 review=txt('source/T2/reviews/REVIEW_T4_459.md')
 ck('T2 review binds exact target',peer['proof_sha256'] in review and h(cache['source/T4/verification/result.json']) in review and 'CONFIRMED' in review and 'CLAIMED by c1-t2' in review)
 ck('frozen registry 27',[r['number'] for r in reg]==list(range(1,28)))
 numbers=[n for n in range(2,27) if n!=11]
 ck('24 assigned witnesses',[r['number'] for r in coverage['rows']]==numbers)
 ck('T4 witness order',[r['number'] for r in peer['weak_candidates']]==numbers)
 ck('T2 witness order',[r['number'] for r in T2['B']['rows']]==numbers)
 floor=Q(coverage['floor_exact']);ck('common floor',floor==Q(1,1000));rows=[]
 for r,pr,tr in zip(coverage['rows'],peer['weak_candidates'],T2['B']['rows']):
  n=r['number'];registry=reg[n-1];original=t4(registry['manifest']);d=t4(r['result'])
  ck(f'{n} raw registry',registry['id']==original['id']==r['id'] and registry['raw_sha256']==original['coefficient_files'][0]['sha256']==r['raw_sha256'])
  ck(f'{n} exponent',Q(original['c_l_exact'])==Q(registry['c_exact'])==Q('4076476460239181/2251799813685248'))
  ck(f'{n} result hash',h(cache['source/T4/'+r['result']])==r['result_sha256']==pr['result_sha256'])
  ck(f'{n} proof hash',h(cache['source/T4/'+r['proof']])==r['proof_sha256']==pr['proof_sha256'])
  source_hash=d.get('source_sha256',d.get('canonical_sha256'));ck(f'{n} numerical input',source_hash==r['input_sha256'])
  if r['bridge_kind']=='raw':ck(f'{n} raw numerical source',source_hash==r['raw_sha256'])
  else:
   bridge=t4(r['bridge']);raw_key='source_sha256' if r['bridge_kind']=='local_canonical_build' else 'generator_sha256'
   ck(f'{n} exact canonical bridge',bridge[raw_key]==r['raw_sha256'] and bridge['canonical_sha256']==source_hash)
   if r['bridge_kind']=='local_canonical_build':ck(f'{n} build hash',d['build_sha256']==h(cache['source/T4/'+r['bridge']]))
  if r['proof_hash_embedded']:
   proof=d.get('proof_sha256');proofs=list(d.get('inputs',{}).values())
   ck(f'{n} embedded proof',proof==r['proof_sha256'] if proof else r['proof_sha256'] in proofs)
  excerpt=txt('source/T4/'+r['review_excerpt']);ck(f'{n} accepted review',excerpt.startswith('## '+r['review_ledger']) and 'CONFIRMED' in excerpt)
  if 'rows' in d:
   choices=[x for x in d['rows'] if x['k']==r['probe_k']];ck(f'{n} unique probe',len(choices)==1);v=choices[0]
   D=interval(v['D'])[1];H=interval(v['gradient_sup_upper_ball'])[1]
  else:
   v=d;D=interval(v['D'])[1] if 'D' in v else interval(v['M'])[1]+interval(v['C'])[1]
   cert=v.get('sup_certificate',v.get('gradient_certificate'));H=Q(cert['H_upper_exact'])
  if 'comparisons' in v:ck(f'{n} source comparisons',all(v['comparisons'].values()))
  lo,hi=interval(v['pairing']);I=lo if lo>0 else -hi if hi<0 else Q(0)
  ck(f'{n} positivity',min(I,D,H)>0);gap=I-D*floor-H*floor**2;ck(f'{n} exact gap',gap>0)
  ck(f'{n} T4 exact comparison',(I,D,H,gap)==tuple(Q(pr[k]) for k in ['I_lower_exact','D_upper_exact','H_upper_exact','positive_gap_exact']))
  display=Q(tr['root_lower']);display_gap=I-D*display-H*display**2
  scale=10**18;low=0;bound=I/D*scale;high=-(-bound.numerator//bound.denominator)
  while high-low>1:
   mid=(low+high)//2;q=Q(mid,scale)
   if I-D*q-H*q*q>0:low=mid
   else:high=mid
  lower=Q(low,scale);ck(f'{n} own directed root',lower>floor and I-D*lower-H*lower**2>0 and I-D*Q(high,scale)-H*Q(high,scale)**2<=0)
  rows.append({'number':n,'candidate':r['id'],'raw_sha256':r['raw_sha256'],'I_lower_exact':str(I),'D_upper_exact':str(D),'H_upper_exact':str(H),'gap_at_1e_minus3_exact':str(gap),'own_root_floor_exact':str(lower),'T2_root_display':str(display),'T2_display_is_strict_endpoint_root_floor':display_gap>0,'T2_display_polynomial_exact':str(display_gap)})
 common=Q(family['scalar_upper_exact']);ck('scalar common ceiling',common==Q(3793,10**9)<floor)
 fr=[];ck('eight families',len(family['rows'])==8)
 for r,pr in zip(family['rows'],peer['scalar_families']):
  name=r['name'];mu,C,cU,w=map(Q,[r['mu'],r['C'],r['cU'],r['sqrtW2']]);ck(name+' positive',min(mu,C,cU,w)>0)
  critical=mu/(3*C);ceiling2=4*mu**3/(27*C*cU**2*w**2)
  ck(name+' critical',mu-3*C*critical==0);ck(name+' ceiling',ceiling2<common**2)
  ck(name+' T4 exact',pr['name']==name and Q(pr['critical_s_exact'])==critical and Q(pr['L2_ceiling_squared_exact'])==ceiling2)
  fr.append({'name':name,'critical_s_exact':str(critical),'ceiling_squared_exact':str(ceiling2)})
 graded=Q(25,54684);gsq=Q(50)**2/(651**2*28248);trans=graded/512
 ck('graded derivative',Q(1,2)-3*4708*Q(1,28248)==0)
 ck('graded exact square',gsq==Q(625,2992882662)==Q(family['graded_square_exact']))
 ck('graded directed ceiling',168**2<28248 and Q(50,651*168)==graded and gsq<graded**2 and graded<floor)
 ck('trans statL implication',trans<common and trans==Q(peer['trans_statL_relaxed_upper_exact'])==Q(T2['E']['trans_statL_L2_upper']))
 ck('graded agreement',graded==Q(family['graded_upper_exact'])==Q(peer['graded_relaxed_upper_exact'])==Q(T2['E']['graded_upper']))
 for path,expected in inputs.items():assert h((R/path).read_bytes())==expected,('changed input',path)
 result={'started_utc':start,'finished_utc':now(),'elapsed_s':time.monotonic()-t0,'checks':checks,'checks_passed':len(checks),'inputs':inputs,'decoded_manifest_files':len(manifest),'nearest_rounded_T2_displays_not_strict_floors':[x['number'] for x in rows if not x['T2_display_is_strict_endpoint_root_floor']],'weak_candidates':rows,'scalar_families':fr,'graded_upper_exact':str(graded),'trans_statL_upper_exact':str(trans),'verdict':'CONFIRMED finite composition of24 accepted fixed-c L2 witnesses; eight scalar tuples and original graded/trans/statL margins only. No new integration, arbitrary-weight extension, dyadic implication, inverse or existence.'}
 (B/'verification/result_v02.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['finished_utc','elapsed_s','checks_passed','decoded_manifest_files','nearest_rounded_T2_displays_not_strict_floors','verdict']}))
if __name__=='__main__':main()

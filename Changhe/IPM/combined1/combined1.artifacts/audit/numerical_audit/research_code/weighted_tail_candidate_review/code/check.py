"""Independent raw Cartesian comparison of the complete T4-292 sector prefix."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip, importlib.util, json, sys, time
from flint import arb, ctx, fmpq as Q
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/weighted_tail_candidate_review'
sys.set_int_max_str_digits(0)
spec=importlib.util.spec_from_file_location('n4_raw_weighted_tail',ROOT/'research/generator_sector_audit/code/direct.py')
D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
def normmap(d):return {int(n):Q(v) for n,v in d.items() if Q(v)}
def canonical(d):return {tuple(k):Q(v) for k,v in zip(d['order'],d['coefficients'],strict=True) if Q(v)}
def encode(d):return {str(n):str(v) for n,v in sorted(d.items()) if v}
def hash_object(d):return sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 started=time.monotonic();ctx.prec=512;dest=BASE/'verification/result.json';assert not dest.exists()
 mp=BASE/'source/MANIFEST_v02.json';manifest=json.loads(mp.read_text());inputs={str(mp.relative_to(ROOT)):sha(mp)}
 def frozen(name):
  item=manifest['files'][name];p=BASE/'source'/name;b=p.read_bytes()
  assert sha256(b).hexdigest()==item['frozen_sha256']
  decoded=gzip.decompress(b) if item['gzip'] else b
  assert len(decoded)==item['original_bytes'] and sha256(decoded).hexdigest()==item['sha256']
  inputs[str(p.relative_to(ROOT))]=sha(p)
  return decoded
 for name in manifest['files']:frozen(name)
 peer=json.loads(frozen('T4_result.json'));rows={r['candidate']:r for r in peer['rows']}
 common=None;out=[]
 # Compare the previously audited007 profiles through independent raw coefficients.
 reference=ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal'
 rmanifest=reference/'MANIFEST.json';rm=json.loads(rmanifest.read_text());rr=reference/rm['coefficient_files'][0]['name']
 assert sha(rr)==rm['coefficient_files'][0]['sha256'];rd=json.loads(rr.read_text())
 aa,cc,gg,_,_,_=D.sectors(rd,qmax=1,hmax=0)
 common={}
 for j in range(4):
  s=aa(j,0)+3;psi=D.dy(D.dx(cc[j,0],s,'c'),s-1,'c')
  common[j]=(gg[j,0],psi)
 inputs[str(rr.relative_to(ROOT))]=sha(rr);inputs[str(rmanifest.relative_to(ROOT))]=sha(rmanifest)
 for ident in ['006','008','009','012','013','014']:
  tick=time.monotonic();directory=next((ROOT/'research/candidate_audits/data').glob(f'C1-N1-{ident}-*'))
  name=directory.name;man=directory/'MANIFEST.json';m=json.loads(man.read_text());assert len(m['coefficient_files'])==1
  raw=directory/m['coefficient_files'][0]['name'];assert sha(raw)==m['coefficient_files'][0]['sha256']
  for line in (directory/'SHA256SUMS').read_text().splitlines():
   digest,filename=line.split(None,1);filename=filename.lstrip('*');assert Path(filename).name==filename and sha(directory/filename)==digest
  can=directory/'canonical.json';audit=ROOT/'research/candidate_audits/verification'/f'{name}.json';aud=json.loads(audit.read_text())
  assert aud['all_forbidden_zero'] and aud['B0n_exact'] and aud['canonical_sha256']==sha(can) and aud['generator_sha256']==sha(raw)
  owncanonical=json.loads(can.read_text());peer_can=json.loads(frozen(f'T4_{ident}_canonical.json'))
  assert canonical(owncanonical)==canonical(peer_can) and peer_can['source_sha256']==sha(raw)
  exact=json.loads(frozen(f'T4_{ident}_sectors.json.gz'));pr=rows[ident]
  assert manifest['files'][f'T4_{ident}_sectors.json.gz']['sha256']==pr['exact_data_sha256']
  assert exact['source']['sha256']==pr['source']['sha256']==manifest['files'][f'T4_{ident}_canonical.json']['sha256']
  data=json.loads(raw.read_text());c=Q(data['cl_exact']);gamma=1/c;delta=1-gamma
  assert c==Q(4076476460239181,2251799813685248)==Q(exact['c_exact'])
  alpha,C,G,E,grouped,summary=D.sectors(data,qmax=1,hmax=8)
  assert len(exact['sectors'])==len(E)==len(grouped)==18
  assert Q(summary['omitted_exponent_upper_bound'])==max(gamma-9*delta,gamma-4)<-3
  coefficient_count=0;sector_records=[];ownprofiles={}
  for row in exact['sectors']:
   k,l=int(row['K']),int(row['L']);h=k-1;key=h,l;a=alpha(h,l)
   density=G.get(key,{})
   s=a+3;psi=D.dy(D.dx(C.get(key,{}),s,'c'),s-1,'c')
   residual=E[key]
   assert a==Q(row['exponent_exact'])
   for field,values in [('density',density),('stream',psi),('residual',residual)]:
    assert values==normmap(row[field]),(ident,k,l,field)
    coefficient_count+=len(set(values)|set(map(int,row[field])))
   lhs={n:((a+1)**2-n*n)*v for n,v in psi.items() if ((a+1)**2-n*n)*v}
   rhs={n:-v for n,v in D.dx(density,a,'s').items() if v}
   assert lhs==rhs,(ident,k,l,'Poisson')
   if h<4 and l==0:
    assert (density,psi)==common[h]
    ownprofiles[str(h)]={'density':encode(density),'stream':encode(psi)}
   sector_records.append({'K':k,'L':l,'exponent_exact':str(a),'density_modes':len(density),'stream_modes':len(psi),'residual_modes':len(residual),'complete_map_sha256':hash_object({'density':encode(density),'stream':encode(psi),'residual':encode(residual)})})
  ordered=sorted(E,key=lambda key:alpha(*key),reverse=True);nz=[key for key in ordered if E[key]]
  assert [[h+1,l] for h,l in nz]==pr['nonzero_sector_set']
  first=nz[0];a=alpha(*first);threshold=a+1
  assert first==(3,1) and [first[0]+1,first[1]]==pr['first_nonzero_sector']
  assert a==Q(pr['first_exponent_exact'])==4*gamma-5
  assert threshold==Q(pr['excluded_weight_upper_exact'])==4*gamma-4
  assert a>Q(summary['omitted_exponent_upper_bound']) and summary['leading_certified_by_complete_prefix']
  norm=(arb.pi()*ar(sum((v*v for v in E[first].values()),Q(0)))).sqrt()
  assert norm>0 and norm.overlaps(arb(pr['first_residual_angular_norm']))
  descendant=[[h+1,l] for h,l in ordered if l==1 and G.get((h,l))]
  assert descendant==pr['nonzero_first_descendant_density_set']
  for p in [man,raw,can,audit,directory/'SHA256SUMS']:inputs[str(p.relative_to(ROOT))]=sha(p)
  result={'candidate':name,'raw_sha256':sha(raw),'own_canonical_sha256':sha(can),'peer_canonical_sha256':manifest['files'][f'T4_{ident}_canonical.json']['sha256'],'exact_canonical_map_equality':True,'all18_maps_equal':True,'all18_Poisson_identities':True,'compared_coefficients':coefficient_count,'sectors':sector_records,'first_nonzero_sector':[4,1],'first_exponent_exact':str(a),'excluded_weight_upper_exact':str(threshold),'first_angular_norm':norm.str(100),'omitted_exponent_upper_bound':summary['omitted_exponent_upper_bound'],'first_four_density_and_stream_profiles_equal_007':True,'profiles_sha256':hash_object(ownprofiles),'elapsed_seconds':time.monotonic()-tick}
  out.append(result);print('CONFIRMED',ident,coefficient_count,'coefficients','norm',norm.str(24),'seconds',result['elapsed_seconds'],flush=True)
 for p in [Path(__file__),BASE/'PROOF.md',ROOT/'research/generator_sector_audit/code/direct.py',ROOT/'research/generator_sector_audit/PROOF.md',ROOT/'research/multiscale_generators/PROOF.md',ROOT/'research/multiscale_generators/code/moments.py',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/sector_audit/code/sectors_flint.py',ROOT/'research/candidate_tailrec/verification/result.json']:
  inputs[str(p.relative_to(ROOT))]=sha(p)
 assert all(sha(ROOT/p)==h for p,h in inputs.items())
 record={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'inputs':inputs,'rows':out,'total_exact_coefficients_compared':sum(row['compared_coefficients'] for row in out),'all_sources_rechecked':True,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-started,'verdict':'CONFIRMED T4-292 coefficient claims and application of the separately audited weighted-tail obstruction under the exact PROOF hypotheses'}
 with dest.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
 print('RESULT',sha(dest),'seconds',record['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

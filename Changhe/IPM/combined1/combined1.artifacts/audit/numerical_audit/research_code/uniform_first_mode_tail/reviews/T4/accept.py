from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,os,shutil,sys,time
from flint import arb,ctx,fmpq as Q,fmpq_poly as Poly
ROOT=Path(__file__).resolve().parents[4];BASE=Path(__file__).resolve().parent;PEER=ROOT.parent/'c1-t4/research'
sys.set_int_max_str_digits(0);sys.path.insert(0,str(ROOT/'research/projected_residual/code'))
from build import read_projection,destination
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
ar=lambda x:arb(Q(x).numerator)/arb(Q(x).denominator)
def beta(a,b):return ar(a).gamma()*ar(b).gamma()/ar(a+b).gamma()
def main():
 start=time.monotonic();ctx.prec=2048;count=0
 def check(test):
  nonlocal count
  assert test,count
  count+=1
 pp=PEER/'uniform_weak_tail_audit/verification/result.json'
 check(sha(pp)=='b7b9f5c4fba7ee41cb58d983daec50e7febe71437f39d7e548651a2b120343e7')
 shutil.copy2(pp,BASE/'T4_result.json');peer=json.loads((BASE/'T4_result.json').read_text())
 paths=[ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json',ROOT/'research/far_pairing_audit/reviews/T4/source/weak_probe_audit/code/reproduce.py',ROOT/'research/far_pairing_audit/reviews/T4/T4_result.json',ROOT/'research/far_pairing_audit/reviews/T4/source/full_far_pairing/PROOF.md',ROOT/'research/full_test_tail/PROOF.md',ROOT/'research/full_test_tail/verification/MANIFEST.json',ROOT/'research/uniform_first_mode_tail/PROOF.md',ROOT/'research/uniform_first_mode_tail/code/check.py',ROOT/'research/uniform_first_mode_tail/verification/result.json',destination('C1-N1-007-d2w-j7-e2bal')]
 cache={sha(p):p for p in paths};frozen={}
 for text,digest in peer['inputs'].items():
  src=Path(text);check(src.is_file() and sha(src)==digest)
  rel=src.relative_to(PEER);dst=BASE/'source'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
  encoding='identity'
  if digest in cache:
   if not dst.exists():dst.symlink_to(os.path.relpath(cache[digest],dst.parent))
   check(sha(dst)==digest)
  elif src.stat().st_size>20_000_000:
   dst=Path(str(dst)+'.gz');encoding='gzip'
   if not dst.exists():
    with src.open('rb') as inp,gzip.open(dst,'xb',compresslevel=5) as out:shutil.copyfileobj(inp,out)
   with gzip.open(dst,'rb') as inp:check(sha256(inp.read()).hexdigest()==digest)
  else:
   if not dst.exists():shutil.copy2(src,dst)
   check(sha(dst)==digest)
  frozen[text]={'path':str(dst.relative_to(ROOT)),'source_sha256':digest,'stored_sha256':sha(dst),'encoding':encoding}
 projection,meta=read_projection('C1-N1-007-d2w-j7-e2bal');c,delta=Q(meta['cl']),Q(meta['delta']);V=Poly([1,-1])
 dataitem=frozen[str(PEER/'uniform_weak_tail_audit/data/full_sine1_v_projection.json')]
 with gzip.open(ROOT/dataitem['path'],'rt') as f:data=json.load(f)
 check(data['canonical_sha256']==meta['source_sha256'] and Q(data['c'])==c and Q(data['delta'])==delta)
 other={row['ell']:Poly([Q(x) for x in row['coefficients']]) for row in data['rows']};check(set(other)==set(projection))
 prepared=[];nb=0;metadata=[]
 for ell,p in sorted(projection.items()):
  pv=p(V);check(pv==other[ell] and pv(V)==p);b=ell*delta/2;selected=[(j,q) for j,q in enumerate(pv) if q]
  for j,q in selected:check(b+j>Q(4,3));nb+=1
  metadata.append({'ell':ell,'degree':pv.degree(),'valuation':selected[0][0],'nonzero_coefficients':len(selected),'minimum_beta':str(b+selected[0][0])})
  prepared.append((b,pv))
 ownpath=ROOT/'research/uniform_first_mode_tail/verification/result.json';own=json.loads(ownpath.read_text());oldrows={r['K0']:r for r in own['rows']}
 check(peer['all_projection_coefficients_exactly_equal'] and peer['all_nonzero_beta_gt_four_thirds'])
 check(metadata==peer['branches']==own['branches'] and peer['minimum_beta_exact']==own['minimum_beta_exact'])
 farpath=ROOT/'research/far_pairing_audit/reviews/T4/T4_result.json';farrows={r['K']:r for r in json.loads(farpath.read_text())['rows']}
 newrow=None;accepted=[]
 for r in peer['rows']:
  K=r['K0'];U=arb(r['U']);check(U.overlaps(arb(r['U_direct'])) and min(r['accuracy_bits'])>150)
  check(all(r['checks'].values()) and U<ar(Q(r['strict_upper_exact'])))
  for key in ['I_direct','I_parts']:check(arb(r['signed_pairing']).overlaps(arb(farrows[K][key])))
  if K in oldrows:
   s=oldrows[K]
   for key in ['U','U_direct']:check(arb(r[key]).overlaps(arb(s[key])))
   check(arb(r['signed_pairing']).overlaps(arb(s['complete_signed_pairing'])))
   check(Q(r['strict_upper_exact'])==Q(s['strict_upper_exact']))
  else:
   check(K==3000000);positive,direct,signed=arb(0),arb(0),arb(0)
   for b,p in prepared:
    moment=beta(b,K+2)
    for j,q in enumerate(p):
     if q:positive+=ar(abs(q))*moment;direct+=ar(abs(q))*beta(b+j,K+2);signed+=ar(q)*moment
     moment*=ar((b+j)/(b+K+2+j))
   factor=(arb.pi()/2).sqrt()*ar(2*K+3)/ar(c+1);ownU=factor*positive;ownDirect=factor*direct;signed*=arb.pi()/2
   check(ownU.overlaps(ownDirect) and ownU.overlaps(U) and min(ownU.rel_accuracy_bits(),ownDirect.rel_accuracy_bits())>150)
   check(signed.overlaps(arb(r['signed_pairing'])) and ownU<ar(Q(r['strict_upper_exact'])))
   check(ar(Q(r['strict_upper_exact']))<ar(Q(4769166867,10**12)))
   newrow={'K0':K,'U':ownU.str(100),'U_direct':ownDirect.str(100),'signed_pairing':signed.str(100),'strict_upper_exact':r['strict_upper_exact'],'below_confirmed_incumbent':True}
  accepted.append({'K0':K,'strict_upper_exact':r['strict_upper_exact'],'all_comparisons_passed':True})
 check(len(accepted)==7 and newrow is not None)
 out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED N4-222/225 via T4-285, plus independently reproduced K0=3000000 cutoff; test-value ceiling only',
      'checks_passed':count,'exact_nonzero_coefficients_checked':nb,'peer_result_sha256':sha(BASE/'T4_result.json'),'own_result_sha256':sha(ownpath),
      'peer_inputs_frozen':frozen,'review_sha256':sha(ROOT/'research/uniform_first_mode_tail/review_plan_T4.md'),'acceptance_code_sha256':sha(Path(__file__)),
      'own_inputs':{str(p.relative_to(ROOT)):sha(p) for p in [*paths,ROOT/'research/far_pairing_audit/reviews/T4/ACCEPTANCE.json',ROOT/'research/projected_residual/code/build.py',ROOT/'research/radial_fourier/code/radial.py']},
      'rows':accepted,'independent_new_cutoff':newrow,'peer_elapsed_seconds':peer['elapsed_seconds'],'elapsed_seconds':time.monotonic()-start}
 with (BASE/'ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('ACCEPTED',count,'COEFFICIENTS',nb,'SECONDS',out['elapsed_seconds'],'UTC',out['utc'],flush=True)
if __name__=='__main__':main()

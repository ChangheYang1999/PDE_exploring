"""Exact complete007 pairings and a finite asymptotic-model error."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/far_pairing_audit'
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'research/projected_residual/code'))
from build import read_projection,destination
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import U
NAME='C1-N1-007-d2w-j7-e2bal'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(x):
 x=Q(x);return arb(x.numerator)/arb(x.denominator)
def binary(x):return Q(*float(x).as_integer_ratio())
def beta(a,b):
 a,b=Q(a),Q(b);assert a>0 and b>0
 return ar(a).gamma()*ar(b).gamma()/ar(a+b).gamma()
def binomial(a,n):
 ans=Q(1)
 for j in range(n):ans*=Q(a-j,j+1)
 return ans

def whole(prepared,K):
 vtotal=arb(0);ttotal=arb(0);branch=[]
 for ell,b,P,Qv in prepared:
  start=beta(b,K+2);mv=mt=start;vs=ts=arb(0)
  for j,c in enumerate(Qv):
   vs+=ar(c)*mv;mv*=ar((b+j)/(b+K+2+j))
  for j,c in enumerate(P):
   ts+=ar(c)*mt;mt*=ar(Q(K+2+j)/(b+K+2+j))
  assert vs.overlaps(ts),(K,ell)
  branch.append({'ell':ell,'endpoint_overlap':True,'v_accuracy_bits':vs.rel_accuracy_bits(),'t_accuracy_bits':ts.rel_accuracy_bits()})
  vtotal+=vs;ttotal+=ts
 vtotal*=arb.pi()/2;ttotal*=arb.pi()/2
 assert abs(vtotal)>0 and abs(ttotal)>0 and vtotal.overlaps(ttotal)
 assert min(vtotal.rel_accuracy_bits(),ttotal.rel_accuracy_bits())>150
 return vtotal,ttotal,branch

def run():
 start=time.monotonic();ctx.prec=2048
 src=ROOT/f'research/candidate_audits/data/{NAME}/canonical.json'
 auditpath=ROOT/f'research/candidate_audits/verification/{NAME}.json';audit=json.loads(auditpath.read_text())
 assert H(src)==audit['canonical_sha256'] and audit['all_forbidden_zero'] and all(audit['snapshot_hashes_confirmed'].values())
 projection,metadata=read_projection(NAME);ppath=destination(NAME)
 reportpath=ROOT/f'research/projected_residual/verification/{NAME}_build.json';report=json.loads(reportpath.read_text())
 assert report['projection_sha256']==H(ppath) and report['exact_full_residual_projection_match']
 assert report['source_sha256']==H(src)==metadata['source_sha256']
 fullcache=ROOT/f'research/whole_plane_norms/data/{NAME}_D0.json.gz'
 # The independent projection report binds its original full comparison.
 # Rehashing the large cache is unnecessary: it is not an input to this run.
 c=Q(metadata['cl']);delta=Q(metadata['delta']);assert delta==1-1/c
 prepared=[]
 for ell,P in sorted(projection.items()):
  pv=P(U);assert pv(U)==P and ell*delta/2>0
  prepared.append((ell,ell*delta/2,P,pv))
 peerpath=BASE/'source/N1_007_far_weak.json';peer=json.loads(peerpath.read_text())
 manifest=json.loads((BASE/'source/MANIFEST.json').read_text())
 for name,record in manifest['files'].items():assert H(BASE/'source'/name)==record['sha256']
 assert peer['sha256']==audit['generator_sha256'] and binary(peer['exp_min'])==-7
 rows=[]
 for ell,b,P,pv in prepared:
  for q in range(4):
   exponent=1-ell*delta-2*q
   if exponent < -7:continue
   coefficient=sum((p*binomial(-b-j,q) for j,p in enumerate(P)),Q(0))
   if coefficient:rows.append({'ell':ell,'q':q,'exponent':str(exponent),'sine1_exact':str(coefficient)})
 rows.sort(key=lambda r:Q(r['exponent']),reverse=True)
 assert len(rows)==len(peer['sectors_sin1'])
 conversion=[]
 for row,fp in zip(rows,peer['sectors_sin1'],strict=True):
  e,s=Q(row['exponent']),Q(row['sine1_exact']);ef,sf=binary(fp[0]),binary(fp[1])
  ed=abs(e-ef);sd=abs(s-sf)/abs(s)
  assert ed<Q(1,10**14) and sd<Q(1,10**13),(row['ell'],row['q'],float(ed),float(sd))
  conversion.append({'ell':row['ell'],'q':row['q'],'exponent_error':str(ed),'amplitude_relative_error':str(sd)})
 q4=sum((p*binomial(-delta/2-j,4) for j,p in enumerate(projection[1])),Q(0))
 q4path=ROOT/'research/numerics_v06_audit/verification/result.json';q4old=json.loads(q4path.read_text())
 q4reference=next(r for r in q4old['rows'] if r['q']==4)
 assert q4 and q4==Q(q4reference['linear_residual_sine1_exact']) and 1-delta-8==Q(q4reference['density_exponent'])
 print('PREPARED','sectors',len(rows),'q4',ar(q4).str(22),'seconds',time.monotonic()-start,flush=True)
 referencepath=ROOT/f'research/projected_residual/verification/{NAME}_probe_2048.json';reference=json.loads(referencepath.read_text())
 assert reference['source_sha256']==H(src) and reference['projection_sha256']==H(ppath)
 small={r['k']:r for r in reference['probes']};large={r['k']:r for r in peer['rows']}
 ks=sorted(set(small)|set(large)|{3_000_000})
 records=[]
 for K in ks:
  tick=time.monotonic();I,J,branches=whole(prepared,K)
  record={'K':K,'I_v_endpoint':I.str(100),'I_t_endpoint':J.str(100),'endpoints_overlap':True,'relative_accuracy_bits':[I.rel_accuracy_bits(),J.rel_accuracy_bits()],'branches':branches}
  if K in small:
   assert I.overlaps(arb(small[K]['pairing']));record['previous_small_index_overlap']=True
  if K>=min(large):
   terms=[(arb.pi()/2*ar(Q(row['sine1_exact']))*beta(K+(Q(row['exponent'])+3)/2,(1-Q(row['exponent']))/2)) for row in rows]
   total=sum(terms,arb(0));absolute=sum(map(abs,terms),arb(0));error=I-total;relative=abs(error)/abs(I)
   assert abs(total)>0 and total.rel_accuracy_bits()>150 and absolute>0
   record.update({'I_truncated_exact_sectors':total.str(100),'global_pairing_error':error.str(100),'absolute_pairing_error':abs(error).str(100),'relative_pairing_error':relative.str(100),'model_cancellation_fraction':(abs(total)/absolute).str(100),'leading_model_pairing':terms[0].str(100),'last_model_pairing':terms[-1].str(100),'last_term_bounds_actual_error':bool(abs(error)<=abs(terms[-1]))})
   if K in large:
    old=large[K];fp=ar(binary(old['I_far']));record['published_model_absolute_relative_error']=(abs(abs(total)-fp)/abs(total)).str(80)
   print('K',K,'full',I.str(22),'model',total.str(22),'relativeerror',relative.str(14),'seconds',time.monotonic()-tick,flush=True)
  else:print('CAL',K,I.str(24),'seconds',time.monotonic()-tick,flush=True)
  record['elapsed_seconds']=time.monotonic()-tick;records.append(record)
 paths=[src,auditpath,ppath,reportpath,referencepath,q4path,peerpath,BASE/'source/MANIFEST.json',BASE/'source/N1_far_weak.py',Path(__file__),BASE/'PROOF.md',ROOT/'research/projected_residual/PROOF.md',ROOT/'research/projected_residual/code/build.py',ROOT/'research/radial_fourier/code/radial.py',ROOT/'research/numerics_v06_audit/PROOF.md',ROOT/'research/numerics_v06_audit/source/numerics_v06.md']
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':NAME,'precision_bits':ctx.prec,'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},'projection_full_comparison_report_bound':True,'complete_projected_branches':len(prepared),'sector_count':len(rows),'exact_model_sectors':rows,'floating_table_conversion':conversion,'q4_exact':str(q4),'q4_independent_potential_agreement':True,'q4_exponent':str(1-delta-8),'finite_model_is_full_residual':False,'rows':records,'elapsed_seconds':time.monotonic()-start,'verdict':'OPEN independent peer for new whole-plane pairings and model errors; q4 independently reproduces N4-195 algebra'}
 out=BASE/'verification/result.json'
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('DONE',result['utc'],'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':run()

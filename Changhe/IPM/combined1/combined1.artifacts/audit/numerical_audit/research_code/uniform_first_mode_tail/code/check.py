from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,time,os,signal
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/uniform_first_mode_tail'
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'research/projected_residual/code'))
from build import read_projection,destination
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import U
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(x):
 x=Q(x);return arb(x.numerator)/arb(x.denominator)
def beta(a,b):return ar(a).gamma()*ar(b).gamma()/ar(a+b).gamma()
def state(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]
 except FileNotFoundError:return None
begin=datetime.now(timezone.utc).isoformat();start=time.monotonic();stopped=[]
try:
 ctx.prec=2048;pid=286853;s=state(pid)
 if s and s not in ['T','Z','X']:os.kill(pid,signal.SIGSTOP);stopped.append(pid)
 if s:
  p=Path(f'/proc/{pid}/task/{pid}/children')
  for text in p.read_text().split() if p.exists() else []:
   child=int(text);s=state(child)
   if s and s not in ['T','Z','X']:os.kill(child,signal.SIGSTOP);stopped.append(child)
 name='C1-N1-007-d2w-j7-e2bal';projection,meta=read_projection(name)
 src=ROOT/f'research/candidate_audits/data/{name}/canonical.json';pp=destination(name)
 oldpath=ROOT/'research/far_pairing_audit/verification/result.json';old=json.loads(oldpath.read_text())
 assert sha(src)==meta['source_sha256']=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
 assert old['inputs'][str(pp.relative_to(ROOT))]==sha(pp) and old['projection_full_comparison_report_bound']
 acceptance=ROOT/'research/far_pairing_audit/reviews/T4/ACCEPTANCE.json';accepted=json.loads(acceptance.read_text());assert accepted['own_result_sha256']==sha(oldpath)
 c=Q(meta['cl']);delta=Q(meta['delta']);assert c==Q(4076476460239181,2251799813685248) and delta==1-1/c
 prepared=[];degrees=[];betas=[]
 for ell,P in sorted(projection.items()):
  pv=P(U);assert pv(U)==P
  selected=[(j,q) for j,q in enumerate(pv) if q];assert selected
  b=ell*delta/2
  for j,q in selected:assert b+j>Q(4,3);betas.append(b+j)
  prepared.append((ell,b,pv));degrees.append({'ell':ell,'degree':pv.degree(),'valuation':selected[0][0],'nonzero_coefficients':len(selected),'minimum_beta':str(b+selected[0][0])})
 references={r['K']:r for r in old['rows']};rows=[]
 for K in [10**5,10**6,10**7,10**8,10**9,10**10]:
  positive=arb(0);positive_direct=arb(0);signed=arb(0)
  for ell,b,p in prepared:
   val=beta(b,K+2)
   for j,q in enumerate(p):
    if q:
     positive+=ar(abs(q))*val;signed+=ar(q)*val
     # Direct Gamma values are independent of the finite recurrence.
     positive_direct+=ar(abs(q))*beta(b+j,K+2)
    val*=ar((b+j)/(b+K+2+j))
  signed*=arb.pi()/2;assert signed.overlaps(arb(references[K]['I_v_endpoint']))
  factor=(arb.pi()/2).sqrt()*ar(2*K+3)/ar(c+1)
  bound=factor*positive;direct=factor*positive_direct
  assert bound.overlaps(direct) and min(bound.rel_accuracy_bits(),direct.rel_accuracy_bits())>150
  # Ceiling rounded upward to an exact decimal, never inferred from a midpoint.
  scale=10**18;upper=Q(int((bound.upper()*scale).ceil().unique_fmpz())+1,scale)
  assert bound<ar(upper)
  rec={'K0':K,'uniform_integer_scope':f'all integers K >= {K}','U':bound.str(100),'U_direct':direct.str(100),'accuracy_bits':[bound.rel_accuracy_bits(),direct.rel_accuracy_bits()],'strict_upper_exact':str(upper),'complete_signed_pairing':signed.str(100),'peer_pairing_overlap':True,'global_monotonicity_hypothesis_checked':True,'below_one_e_minus_four':bool(bound<ar(Q(1,10000))),'below_173_e_minus_six':bool(bound<ar(Q(173,10**6)))}
  rows.append(rec);print('K0',K,'U',bound.str(25),'strict_upper',str(upper),'seconds',time.monotonic()-start,flush=True)
 inputs=[src,pp,oldpath,acceptance,BASE/'PROOF.md',Path(__file__),ROOT/'research/projected_residual/code/build.py',ROOT/'research/radial_fourier/code/radial.py']
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):sha(p) for p in inputs},'candidate':name,'precision_bits':ctx.prec,'denominator_hypothesis':'D_K >= A_K; H_K >= 0. Separated test only.','minimum_beta_exact':str(min(betas)),'all_nonzero_beta_gt_four_thirds':True,'branches':degrees,'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'OPEN independent review of uniform first-mode separated-test tail ceilings'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
finally:
 for pid in reversed(stopped):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
 pause={'began_utc':begin,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'stopped_and_resumed_pids':stopped}
 with (BASE/'verification/pause.json').open('x') as f:json.dump(pause,f,indent=2);f.write('\n')

from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
import importlib.util,gzip,hashlib,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent
helper=R/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('tail_exact_polar',helper);M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
T,V=Poly([0,1]),Poly([1,-1]);sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
def beta(a,b):return ar(a).gamma()*ar(b).gamma()/ar(a+b).gamma()
def main():
 ctx.prec=2048;start=time.monotonic();src=R/'taylor_projection/source/canonical007.json'
 peerpath=B/'source/N4_numerator_result.json';peer=json.loads(peerpath.read_text())
 with gzip.open(B/'source/N4_projection.json.gz','rt') as f:oldprojection=json.load(f)
 assert sha(src)==oldprojection['source_sha256']
 assert sha(B/'source/N4_projection.json.gz') in peer['inputs'].values()
 old={r['ell']:Poly([Q(int(n),int(r['denominator'])) for n in r['numerator']]) for r in oldprojection['rows']}
 c,delta,rho,stream=M.fields(json.loads(src.read_text()));assert c==Q(oldprojection['cl']) and delta==Q(oldprojection['delta'])
 A=defaultdict(Poly);BB=defaultdict(Poly);g0=1-4*T;count=0
 for (j,n),p in rho.items():
  if n==1:A[j+1]-=p*((2*c+1)+c*g0);BB[j+1]-=2*c*V*p
 for (j,m),p in stream.items():
  D=M.td(p,(j+1)*delta/2,2)
  for (k,n),q in rho.items():
   if abs(n-m)!=1:continue
   sig=1 if n>m else -1;ell=j+k+2;count+=1
   A[ell]+=q*(sig*m*p*g0-D)/2;BB[ell]+=sig*m*V*q*p
 P={};prepared=[];minbeta=None;metadata=[]
 for ell in sorted(A):
  quotient,rem=divmod(BB[ell],V);assert not rem
  p=A[ell]-2*BB[ell]-T*BB[ell].derivative()+(ell*delta/2-1)*T*quotient
  assert p==old[ell]
  pv=p(V);assert pv(V)==p;P[ell]=pv;b=ell*delta/2
  selected=[(j,q) for j,q in enumerate(pv) if q]
  assert selected and all(b+j>Q(4,3) for j,q in selected)
  mb=b+selected[0][0];minbeta=mb if minbeta is None else min(minbeta,mb)
  metadata.append({'ell':ell,'degree':pv.degree(),'valuation':selected[0][0],'nonzero_coefficients':len(selected),'minimum_beta':str(mb)})
  prepared.append((ell,b,pv))
 assert set(P)==set(old) and metadata==peer['branches'] and minbeta==Q(peer['minimum_beta_exact'])
 print('EXACT_PROJECTION',len(P),'branches',count,'pairs','minbeta',minbeta,'seconds',time.monotonic()-start,flush=True)
 datapath=B/'data/full_sine1_v_projection.json'
 data={'canonical_sha256':sha(src),'c':str(c),'delta':str(delta),'rows':[{'ell':ell,'coefficients':[str(q) for q in p]} for ell,p in P.items()]}
 with datapath.open('x') as f:json.dump(data,f);f.write('\n')
 ownpath=R/'full_far_pairing/verification/result.json';own=json.loads(ownpath.read_text());ownrows={r['K']:r for r in own['rows']}
 peerrows={r['K0']:r for r in peer['rows']};rows=[]
 for K in sorted(set(peerrows)|{3000000}):
  positive=arb(0);direct=arb(0);signed=arb(0)
  for ell,b,p in prepared:
   moment=beta(b,K+2)
   for j,q in enumerate(p):
    if q:
     positive+=ar(abs(q))*moment;signed+=ar(q)*moment
     direct+=ar(abs(q))*beta(b+j,K+2)
    moment*=ar((b+j)/(b+K+2+j))
  factor=(arb.pi()/2).sqrt()*ar(2*K+3)/ar(c+1);U=factor*positive;Ud=factor*direct;signed*=arb.pi()/2
  assert U.overlaps(Ud) and min(U.rel_accuracy_bits(),Ud.rel_accuracy_bits())>150
  flags={'positive_direct_recurrence':True}
  if K in ownrows:
   flags['own_signed_direct']=signed.overlaps(arb(ownrows[K]['I_direct']))
   flags['own_signed_parts']=signed.overlaps(arb(ownrows[K]['I_parts']))
  if K in peerrows:
   old=peerrows[K]
   flags.update({'peer_U':U.overlaps(arb(old['U'])),'peer_U_direct':U.overlaps(arb(old['U_direct'])),'peer_signed':signed.overlaps(arb(old['complete_signed_pairing'])),'peer_strict_upper':bool(U<ar(Q(old['strict_upper_exact'])))})
   upper=Q(old['strict_upper_exact'])
  else:
   upper=Q(int((U.upper()*10**18).ceil().unique_fmpz())+1,10**18);assert U<ar(upper)
  assert all(flags.values()),(K,flags)
  beat=bool(U<ar(Q(4769166867,10**12)))
  if K==3000000:assert beat
  rows.append({'K0':K,'U':U.str(100),'U_direct':Ud.str(100),'signed_pairing':signed.str(100),'strict_upper_exact':str(upper),'checks':flags,'below_confirmed_incumbent':beat,'accuracy_bits':[U.rel_accuracy_bits(),Ud.rel_accuracy_bits()]})
  print('K0',K,'U',U.str(30),'below_incumbent',beat,'seconds',time.monotonic()-start,flush=True)
 paths=[src,helper,Path(__file__),B/'PROOF.md',datapath,ownpath,R/'full_far_pairing/PROOF.md',*sorted((B/'source').iterdir())]
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in paths},'all_projection_coefficients_exactly_equal':True,'all_nonzero_beta_gt_four_thirds':True,'minimum_beta_exact':str(minbeta),'branches':metadata,'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-222 and N4-225: complete-test uniform integer tail ceilings; no upper bound on solution distance'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

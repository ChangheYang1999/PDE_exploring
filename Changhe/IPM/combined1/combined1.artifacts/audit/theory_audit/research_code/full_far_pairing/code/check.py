from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
import importlib.util,hashlib,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1];RESEARCH=BASE.parent
primitive=RESEARCH/'weak_probe_audit/code/reproduce.py'
s=importlib.util.spec_from_file_location('full_far_polar',primitive);M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
T,V=Poly([0,1]),Poly([1,-1])
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
def beta(a,b):
 a,b=Q(a),Q(b);assert a>0 and b>0
 return ar(a).gamma()*ar(b).gamma()/ar(a+b).gamma()
def choose(a,q):
 b=Q(1)
 for k in range(q):b*=Q(a-k)/Q(k+1)
 return b
def integrate(P,b,K):
 m=beta(K+2,b);val=arb(0)
 for i,q in enumerate(P):
  if q:val+=ar(q)*m
  m*=ar(Q(K+i+2)/(K+i+2+b))
 return val
def main():
 ctx.prec=2048;start=time.monotonic();src=RESEARCH/'taylor_projection/source/canonical007.json';state=json.loads(src.read_text());peerpath=BASE/'source/N4_result.json';peer=json.loads(peerpath.read_text())
 assert sha(src) in peer['inputs'].values()
 c,delta,rho,stream=M.fields(state);A=defaultdict(Poly);B=defaultdict(Poly);q0=1-4*T;count=0
 for (j,n),R in rho.items():
  if n==1:A[j+1]-=R*((2*c+1)+c*q0);B[j+1]-=2*c*V*R
 for (j,m),S in stream.items():
  D=M.td(S,(j+1)*delta/2,2)
  for (k,n),R in rho.items():
   if abs(n-m)!=1:continue
   sig=1 if n>m else -1;ell=j+k+2;count+=1
   A[ell]+=R*(sig*m*S*q0-D)/2;B[ell]+=sig*m*V*R*S
 P={}
 for ell in sorted(A):
  quotient,rem=divmod(B[ell],V);assert not rem
  P[ell]=A[ell]-2*B[ell]-T*B[ell].derivative()+(ell*delta/2-1)*T*quotient
 print('BUILT',len(P),'branches','pairs',count,'seconds',time.monotonic()-start,flush=True)
 sectors=[]
 for ell,pol in P.items():
  for q in range(4):
   e=1-ell*delta-2*q
   if e < -7:continue
   coef=sum((p*choose(-ell*delta/2-i,q) for i,p in enumerate(pol)),Q(0))
   if coef:sectors.append({'ell':ell,'q':q,'exponent':str(e),'sine1_exact':str(coef)})
 sectors.sort(key=lambda r:Q(r['exponent']),reverse=True)
 assert sectors==peer['exact_model_sectors']
 q4=sum((p*choose(-delta/2-i,4) for i,p in enumerate(P[1])),Q(0))
 assert q4 and q4==Q(peer['q4_exact'])
 print('EXACT_SECTORS',len(sectors),'q4_agrees','seconds',time.monotonic()-start,flush=True)
 records=[]
 for old in peer['rows']:
  K=old['K'];parts=sum((integrate(A[ell]+K*B[ell],ell*delta/2,K) for ell in P),arb(0))*arb.pi()/2
  direct=sum((integrate(pol,ell*delta/2,K) for ell,pol in P.items()),arb(0))*arb.pi()/2
  flags={'parts_direct':parts.overlaps(direct),'peer_v':parts.overlaps(arb(old['I_v_endpoint'])),'peer_t':parts.overlaps(arb(old['I_t_endpoint']))}
  assert all(flags.values()),(K,flags)
  assert min(parts.rel_accuracy_bits(),direct.rel_accuracy_bits())>150 and abs(parts)>0
  record={'K':K,'I_parts':parts.str(100),'I_direct':direct.str(100),'accuracy_bits':[parts.rel_accuracy_bits(),direct.rel_accuracy_bits()],'checks':flags}
  if 'I_truncated_exact_sectors' in old:
   terms=[arb.pi()/2*ar(Q(r['sine1_exact']))*beta(K+(Q(r['exponent'])+3)/2,(1-Q(r['exponent']))/2) for r in sectors]
   model=sum(terms,arb(0));error=parts-model;absolute=sum(map(abs,terms),arb(0));relative=abs(error)/abs(parts)
   quantities={'I_truncated_exact_sectors':model,'global_pairing_error':error,'absolute_pairing_error':abs(error),'relative_pairing_error':relative,'model_cancellation_fraction':abs(model)/absolute,'leading_model_pairing':terms[0],'last_model_pairing':terms[-1]}
   mflags={k:z.overlaps(arb(old[k])) for k,z in quantities.items()};assert all(mflags.values()),(K,mflags)
   record.update({k:z.str(100) for k,z in quantities.items()});record['model_checks']=mflags
   record['last_term_bounds_actual_error']=bool(abs(error)<=abs(terms[-1]));assert record['last_term_bounds_actual_error']==old['last_term_bounds_actual_error']
  records.append(record);print('K',K,'I',parts.str(22),'verified',True,'seconds',time.monotonic()-start,flush=True)
 inputs=[src,peerpath,primitive,BASE/'PROOF.md',Path(__file__)]
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in inputs},'method':'Independent polar weak integration by parts; exact radial adjoint recovers first-sine projection','stream_density_pairs':count,'residual_branches':len(P),'exact_model_sectors':sectors,'q4_exact':str(q4),'all_exact_sector_comparisons':True,'rows':records,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED independent polar reproduction of full pairings and finite-model errors at listed indices'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

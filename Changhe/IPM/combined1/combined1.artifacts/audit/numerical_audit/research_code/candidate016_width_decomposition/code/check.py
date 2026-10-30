"""Exact enclosure-width audit; no source integration and no peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,os,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_width_decomposition'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();out=B/'verification/result.json';assert not out.exists()
 manifest=json.loads((B/'verification/PROOF_FIRST.json').read_text());assert not manifest['checker_exists'] and not manifest['result_exists']
 checks=[]
 def ck(v,label):
  checks.append({'check':label,'pass':bool(v)});assert v,label
 for p,h in manifest['inputs'].items():ck(sha(R/p)==h,'input '+p)
 rows=[]
 for P,tv,mv,lo,hi in [(47,'v04','v02',Q(6805,10000),Q(6815,10000)),(63,'v05','v03',Q(6825,10000),Q(6835,10000))]:
  t=json.loads((R/f'research/candidate016_angular_tail_bound/verification/result_{tv}.json').read_text())
  m=json.loads((R/f'research/candidate016_multimode_complete_bounds/verification/result_{mv}.json').read_text())
  ck(t['prefix']==m['prefix']==P and t['raw_sha256']==m['raw_sha256'],'candidate prefix '+str(P))
  q={d['n']:Q(d['q_upper_exact']) for d in t['modes']};sel=m['selected_modes'];ell={d['n']:Q(d['selected_lower']) for d in sel};js={d['n']:Q(d['selected_improvement']) for d in sel};N=P+2
  ck(list(q)==list(range(1,P+1,2)) and list(ell)==list(range(1,32,2)),'complete recorded sets '+str(P))
  RU=Q(t['full_rF_square_upper_exact']);V=RU/N**2+sum((Q(1,n*n)-Q(1,N*N))*v for n,v in q.items());L=sum(e*e for e in ell.values());U=V-sum(js.values())
  ck(L==Q(m['H_lower_square_exact']) and U==Q(m['H_upper_square_exact']),'recomposed endpoints '+str(P))
  gaps={n:q[n]/(n*n)-js[n]-ell[n]**2 for n in ell};D=sum(gaps.values());T=(RU-sum(q[n] for n in ell))/N**2+sum((Q(1,n*n)-Q(1,N*N))*q[n] for n in range(33,P+1,2))
  ck(all(v>0 for v in gaps.values()) and T>0,'positive low-mode gaps and remainder '+str(P))
  ck(U-L==D+T,'exact split '+str(P));share=D/(U-L);ck(lo<share<hi,'exact containing share interval '+str(P))
  rows.append({'prefix':P,'low_mode_gap_exact':str(D),'total_width_exact':str(U-L),'tail_remainder_exact':str(T),'low_mode_share_exact':str(share),'share_strict_lower_exact':str(lo),'share_strict_upper_exact':str(hi),'share_FLOAT':float(share)})
 ck(rows[0]['low_mode_gap_exact']==rows[1]['low_mode_gap_exact'],'low-mode gaps unchanged')
 dot=lambda a,b:sum(Q(x)*Q(y) for x,y in zip(a,b));examples=[]
 for A,g,z,exact,label in [((1,1,1),(1,0,0),(0,1,0),Q(1),'all upper error'),((1,1),(1,0),(0,0),Q(2),'all lower error')]:
  lower=dot(A,g)**2/dot(g,g);improve=dot(A,z)**2/dot(z,z) if dot(z,z) else Q(0);upper=dot(A,A)-improve
  ck(upper-lower==1,'unit gap '+label)
  ck((exact-lower,upper-exact)==((0,1) if label=='all upper error' else (1,0)),'error attribution '+label)
  examples.append({'label':label,'lower':str(lower),'upper':str(upper),'actual_squared_norm':str(exact),'dual_error':str(exact-lower),'upper_error':str(upper-exact)})
 inputs=dict(manifest['inputs']);inputs.update({str(p.relative_to(R)):sha(p) for p in [Path(__file__),B/'verification/PROOF_FIRST.json']})
 result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'verdict':'CONFIRMED finite width split and attribution limitation; dual-only attribution OPEN','checks':checks,'check_count':len(checks),'inputs':inputs,'widths':rows,'counterexamples':examples,'new_source_integrals':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',sha(out));print([(r['prefix'],r['share_FLOAT']) for r in rows])
if __name__=='__main__':main()

"""Exact counterexample to a rounded producer-note interval inference."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time,os
R=Path(__file__).resolve().parents[3];B=R/'research/producer_share_display'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 assert os.sched_getaffinity(0)=={57}and os.getpriority(os.PRIO_PROCESS,0)==19
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();target=B/'verification/result.json';assert not target.exists();checks=[]
 def ck(v,label):checks.append({'check':label,'pass':bool(v)});assert v,label
 m=json.loads((B/'verification/PROOF_FIRST.json').read_text());ck(not m['checker_exists']and not m['result_exists'],'proof first')
 repair=json.loads((B/'verification/REPAIR_FIRST_v02.json').read_text());ck(not repair['checker_v02_exists'],'repair proof before version2');m['inputs'].update(repair['inputs']);m['inputs'][str((B/'verification/REPAIR_FIRST_v02.json').relative_to(R))]=sha(B/'verification/REPAIR_FIRST_v02.json')
 for p,h in m['inputs'].items():ck(sha(R/p)==h,'bound '+p)
 s=(B/'source/N1_note1851.md').read_text()
 for text in ['0.37668932470589 < G0 < 0.37668932470590','[756.5312630768, 757.8514372426]','(385.7299, 385.7299)','[0.2591, 0.2600]','above 1/4','G0 unregularized']:
  ck(text in s,'literal '+text)
 gl,gu,xl,xu=map(Q,['0.37668932470589','0.37668932470590','756.5312630768','757.8514372426']);yl,yu=1024*gl,1024*gu;rl,ru=(yl/xu)**2,(yu/xl)**2
 ck(0<gl<gu and 0<xl<xu,'positive ordered premises');ck(Q('385.7298684988')<yl<yu<Q('385.7298684989'),'safe strict y interval');ck(Q('385.7299')-Q('.00005')<yl<yu<Q('385.7299')+Q('.00005'),'valid nearest summary385.7299');ck(not Q('385.7299')<Q('385.7299'),'printed equal-endpoint open interval empty');ck(Q('.25')<Q('.2590')<rl<ru<Q('.2600'),'safe quotient enclosure and quarter bound');ck(rl<Q('.2591'),'lower monotonicity endpoint below printed LB');g=(gl+gu)/2;x=xu;r=(1024*g/x)**2;ck(gl<g<gu and xl<=x<=xu,'counterexample obeys premises');ck(rl<r<Q('.2591')<ru,'counterexample violates proposed lower endpoint');ck(Q('.2591')-Q('.00005')<rl<Q('.2591')+Q('.00005'),'printed lower endpoint was nearest-rounded');ck(Q('.2600')-Q('.00005')<ru<Q('.2600')+Q('.00005'),'printed upper endpoint nearest-rounded')
 inputs=dict(m['inputs']);inputs.update({str(p.relative_to(R)):sha(p)for p in [Path(__file__),B/'verification/PROOF_FIRST.json']});result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'inputs':inputs,'checks':checks,'check_count':len(checks),'premises':dict(zip(['g_lo','g_hi','x_lo','x_hi'],map(str,[gl,gu,xl,xu]))),'y_interval_exact':[str(yl),str(yu)],'r_interval_exact':[str(rl),str(ru)],'counterexample':{'g':str(g),'x':str(x),'r':str(r)},'safe_display':{'y':['385.7298684988','385.7298684989'],'r':['0.2590','0.2600']},'verdict':'REFUTED two literal interval readings; CONFIRMED quotient exceeds one quarter','actual_fractional_share_below02591':'OPEN; not inferred from this counterexample','existing438_440_conclusion_changed':False,'candidate_verdict_changes':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-tick}
 with target.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'bindings',sha(target),result['elapsed_seconds'])
if __name__=='__main__':main()

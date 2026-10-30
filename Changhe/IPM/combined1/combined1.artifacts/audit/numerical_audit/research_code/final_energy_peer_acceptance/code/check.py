"""Finite independent verification of T4-509's propagated endpoints."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,re,time,os
R=Path(__file__).resolve().parents[3];B=R/'research/final_energy_peer_acceptance'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def ball(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 c,e=map(Q,m.groups());assert e>=0
 return c-e,c+e
def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();checks=[]
 def ck(v,label):checks.append({'check':label,'pass':bool(v)});assert v,label
 m=read(B/'verification/PROOF_FIRST.json');ck(not m['checker_exists'] and not m['result_exists'],'proof and copies precede code')
 for p,h in m['inputs'].items():ck(sha(R/p)==h,'bound '+p)
 p=read(B/'source/T4_result.json');ck(sha(B/'source/T4_result.json')=='323735b9140289d9eb07508a4f07be2feb0f735466e0d6f207adf1ab966d8aae','nominated T4-509 root')
 mapped={r['peer_relative']:r for r in m['rows'] if 'peer_relative'in r};ck(len(mapped)==17,'all17peerinputs')
 for rel,h in p['inputs'].items():ck(mapped[rel]['sha256']==h and sha(R/mapped[rel]['local'])==h,'T4 binding '+rel)
 ck(p['check_count']==len(p['checks'])==95 and all(x['pass'] for x in p['checks']),'T4 listed checks consistent')
 a=read(R/'research/final_energy_share_attribution/verification/result.json');root=read(R/'research/registered_norm_assembly/verification/result.json');g0=read(R/'research/registered_norm_assembly/source/N4_G0.json');ds=read(R/'research/registered_norm_assembly/source/N4_derivatives.json');comp={}
 for k,d in [('G0',g0),('G1',ds['norms']['G1']),('P2',ds['norms']['P2'])]:
  l=ball(d['norm_lower_ball']);u=ball(d['norm_upper_ball']);comp[k]=(min(l[0],u[0]),max(l[1],u[1]));ck(0<comp[k][0]<=comp[k][1],'positive '+k)
 count=0
 for name,w in [('E_star',{'P2':1,'G1':2**14,'G0':2**18}),('E_w',{'P2':1,'G1':2**15,'G0':2**20})]:
  own=next(x for x in a['energy_shares'] if x['energy']==name);peer=next(x for x in p['energy_shares'] if x['energy']==name);ck(own['weights']==peer['weights']==w,'same weights '+name);sqs={k:(v*comp[k][0]**2,v*comp[k][1]**2) for k,v in w.items()};SL=sum(x[0] for x in sqs.values());SU=sum(x[1] for x in sqs.values())
  for k,(L,U) in sqs.items():
   loose=(L/SU,U/SL);tight=(L/(L+SU-U),U/(U+SL-L));z=own['shares'][k];t=peer['shares'][k]
   ck(loose==(Q(z['lower_exact']),Q(z['upper_exact'])),'own endpoints '+name+' '+k);ck(loose==tuple(map(Q,t['loose_exact'])),'peer loose '+name+' '+k);ck(tight==tuple(map(Q,t['tight_exact'])),'peer tight '+name+' '+k);ck(0<loose[0]<=tight[0]<=tight[1]<=loose[1]<1,'containment '+name+' '+k);count+=2
   if name=='E_star':
    n={'G0':14,'G1':72,'P2':14}[k];ck(Q(2*n-1,200)<loose[0]<=loose[1]<Q(2*n+1,200),'nearest percent '+k)
 sharp=next(x for x in root['instances'] if x['label']=='sharpw');U=ball(sharp['upper_comparison']['ball'])[1];actual=2**20*comp['G0'][0]**2/U**2
 ck(actual==Q(a['actual_fractional_sharpw_G0_share_lower_exact'])==Q(p['actual_fractional_sharpw_G0_share_lower_exact']),'same actual sharpw lower');ck(actual>Q(1,4),'actual fractional G0 share >1/4');ck(p['actual_fractional_P2_G1_shares']=='OPEN','other fractional shares OPEN');ck(not p['new_integrals'] and not p['peer_code_executed'],'T4 scope');ck(p['disputed_frozen_lines']==a['disputed_frozen_lines']==[[226,227],[993,994]],'same disputed lines')
 inputs=dict(m['inputs']);inputs.update({str(x.relative_to(R)):sha(x) for x in [Path(__file__),B/'verification/PROOF_FIRST.json']});result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'inputs':inputs,'checks':checks,'check_count':len(checks),'original_share_endpoints':count,'T4_input_count':len(mapped),'actual_fractional_G0_share_lower_exact':str(actual),'verdict':'CONFIRMED T4-509 finite acceptance of N4-438','fractional_P2_G1_shares':'OPEN','new_integrals':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'bindings',sha(out))
if __name__=='__main__':main()

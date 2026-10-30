"""Finite exact energy-share audit of accepted prefreeze components."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib,json,os,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/final_energy_share_attribution';A=R/'research/registered_norm_assembly'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ball(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 c,e=map(Q,m.groups());assert e>=0
 return c-e,c+e

def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 tick=time.monotonic();start=datetime.now(timezone.utc).isoformat();out=B/'verification/result.json';assert not out.exists()
 m=json.loads((B/'verification/PROOF_FIRST.json').read_text());assert not m['checker_exists'] and not m['result_exists'];checks=[]
 def ck(v,label):
  checks.append({'check':label,'pass':bool(v)});assert v,label
 for p,h in m['inputs'].items():ck(sha(R/p)==h,'bound '+p)
 root=json.loads((A/'verification/result.json').read_text());ck(sha(A/'verification/result.json')=='78210aeee3ae5f7f215dc4058ac20120fc5158b78ce8b668555a5bcf2f449c48','accepted root180')
 report=(R/'research/final_report_numerical/source/report_v01.md').read_text().splitlines()
 for a,b in [(226,227),(993,994)]:
  text=' '.join(report[a-1:b]);ck('squared sharpw norm' in text and '72 percent' in text and '14 percent' in text,'disputed frozen lines '+str((a,b)))
 raw0=json.loads((A/'source/N4_G0.json').read_text());rawD=json.loads((A/'source/N4_derivatives.json').read_text());ck(rawD['complete'],'complete derivative input')
 comps={}
 for k,d in [('G0',raw0),('G1',rawD['norms']['G1']),('P2',rawD['norms']['P2'])]:
  lo=ball(d['norm_lower_ball']);hi=ball(d['norm_upper_ball']);comps[k]=(min(lo[0],hi[0]),max(lo[1],hi[1]));ck(0<comps[k][0]<=comps[k][1],'positive containing '+k)
 rows=[]
 for name,weights in [('E_star',{'P2':1,'G1':2**14,'G0':2**18}),('E_w',{'P2':1,'G1':2**15,'G0':2**20})]:
  sq={k:(w*comps[k][0]**2,w*comps[k][1]**2) for k,w in weights.items()};S=(sum(t[0] for t in sq.values()),sum(t[1] for t in sq.values()));shares={}
  for k,(a,b) in sq.items():
   lo,hi=a/S[1],b/S[0];ck(0<lo<=hi<1,'proper '+name+' '+k)
   if name=='E_star':
    target={'P2':14,'G1':72,'G0':14}[k];ck(Q(2*target-1,200)<lo<=hi<Q(2*target+1,200),'rounding cell '+k)
    peer=root['E_star_energy_shares'][k];pl,pu=Q(peer['strict_lower_exact']),Q(peer['strict_upper_exact']);ck(pl<lo<=hi<pu,'accepted180 share containment '+k)
   shares[k]={'lower_exact':str(lo),'upper_exact':str(hi),'midpoint_FLOAT':float((lo+hi)/2)}
  rows.append({'energy':name,'weights':weights,'shares':shares})
 sharp=next(x for x in root['instances'] if x['label']=='sharpw');ck(sharp['s_exact']=='1/5184' and sharp['w1']==2**15 and sharp['w2']==2**20,'sharpw definition')
 U=ball(sharp['upper_comparison']['ball'])[1];bound=2**20*comps['G0'][0]**2/U**2;ck(bound>Q(1,4),'actual fractional sharpw G0 share exceeds1/4')
 inputs=dict(m['inputs']);inputs.update({str(p.relative_to(R)):sha(p) for p in [Path(__file__),B/'verification/PROOF_FIRST.json']})
 result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'verdict':'CONFIRMED E_star attribution and sharpw G0 share>1/4; REFUTED frozen sharpw72/14/14 attribution','inputs':inputs,'checks':checks,'check_count':len(checks),'energy_shares':rows,'actual_fractional_sharpw_G0_share_lower_exact':str(bound),'actual_fractional_sharpw_G0_share_lower_FLOAT':float(bound),'disputed_frozen_lines':[[226,227],[993,994]],'new_integrals':False,'candidate_verdict_changes':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'bindings',sha(out));print([(r['energy'],{k:s['midpoint_FLOAT'] for k,s in r['shares'].items()}) for r in rows]);print('actual sharpw G0 share lower FLOAT',float(bound))
if __name__=='__main__':main()

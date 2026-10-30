"""Accept T4-510 in its stated three-row scope using own exact endpoints."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,re,os,time
R=Path(__file__).resolve().parents[3];B=R/'research/rounded_table_peer_acceptance'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
def ball(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 c,e=map(Q,m.groups());assert e>=0;return c-e,c+e

def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();checks=[]
 def ck(v,label):checks.append({'check':label,'pass':bool(v)});assert v,label
 m=read(B/'verification/PROOF_FIRST.json');ck(not m['checker_exists'] and not m['result_exists'],'proof and copies before code')
 for rel,h in m['inputs'].items():ck(sha(R/rel)==h,'bound '+rel)
 p=read(B/'source/T4_result.json');ck(sha(B/'source/T4_result.json')=='6ba3bab79e2994191220acc1dab98952fd9ce5a618b837c0b316ce63f8cb4c63','nominated T4-510 root');mapped={x['peer_relative']:x for x in m['rows'] if 'peer_relative'in x};ck(len(mapped)==13,'all13peerinputs')
 for rel,h in p['inputs'].items():ck(mapped[rel]['sha256']==h and sha(R/mapped[rel]['local'])==h,'peer binding '+rel)
 ck(len(p['checks'])==p['check_count']==59 and all(x['pass']for x in p['checks']),'59peerflags consistent')
 a=read(R/'research/final_numerical_display_audit/verification/result.json');d=read(R/'research/whole_plane_norms/verification/d2_G0_ball_2048.json');q0=[ball(d[k])for k in ('norm_lower_ball','norm_upper_ball')];q0=(min(x[0]for x in q0),max(x[1]for x in q0));c=read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json')['norms']['rF'];rf=tuple(Q(c[k])for k in ('accepted_lower_exact','accepted_upper_exact'));lines=(R/'research/final_report_numerical/source/report_v01.md').read_text().splitlines()
 ck(p['target_sha256']==sha(R/'research/final_report_numerical/source/report_v01.md'),'same frozen target');ck(p['table_heading_line']==a['table_heading_line']==1050 and'residual LB'in lines[1049],'same heading')
 old='../candidate016_complete_forcing_audit/source/component_acceptance.json';new='source/input_04_comparison_G0_rF_G1_P2_v01.json';ck(mapped[old]['sha256']==mapped[new]['sha256']==sha(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json'),'T4-467 source identical')
 ck(len(p['rows'])==len(a['not_directed_lower_bound'])==3,'exactly3rows');rows=[]
 for row,line,dval,unit,interval,text in [(20,1069,Q('4.99'),Q('.01'),q0,'4.99'),(37,1086,Q('4.99'),Q('.01'),q0,'4.99'),(80,1129,Q('7.1457012'),Q('.0000001'),rf,'7.1457012')]:
  L,U=interval;t=next(x for x in p['rows']if x['table_row']==row);z=next(x for x in a['not_directed_lower_bound']if x['table_row']==row)
  ck(t['frozen_line']==z['frozen_line']==line and lines[line-1].startswith('| '+str(row)+' |')and text in lines[line-1],'literal row'+str(row));ck(dval==Q(t['display_exact'])==Q(z['display']),'display'+str(row));ck(unit==Q(t['unit_exact']),'unit'+str(row));ck(interval==(Q(t['lower_exact']),Q(t['upper_exact']))==(Q(z['quantity_lower']),Q(z['quantity_upper'])),'own derived endpoints'+str(row));ck(dval-unit/2<L<=U<dval+unit/2,'nearest cell'+str(row));ck(0<L<=U<dval,'not lower bound'+str(row));ck(dval-U==Q(t['display_minus_upper_exact'])==Q(z['display_minus_upper']),'exact defect'+str(row));rows.append({'row':row,'line':line,'lower_exact':str(L),'upper_exact':str(U),'display_exact':str(dval),'defect_exact':str(dval-U)})
 inputs=dict(m['inputs']);inputs.update({str(x.relative_to(R)):sha(x)for x in [Path(__file__),B/'verification/PROOF_FIRST.json']});result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'inputs':inputs,'checks':checks,'check_count':len(checks),'rows':rows,'peer_inputs':13,'verdict':'CONFIRMED T4-510 narrow acceptance of439 heading and three counterexamples','other439supplemental_checks':'not accepted here','new_integrals':False,'peer_code_executed':False,'candidate_verdict_changes':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'bindings',sha(out))
if __name__=='__main__':main()

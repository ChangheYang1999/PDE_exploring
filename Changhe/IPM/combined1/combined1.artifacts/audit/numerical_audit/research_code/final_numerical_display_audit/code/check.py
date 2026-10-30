"""Exact finite audit of frozen report displays; no source integrals."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib,json,re,os,time
R=Path(__file__).resolve().parents[3];B=R/'research/final_numerical_display_audit'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ball(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 c,e=map(Q,m.groups());assert e>=0
 return c-e,c+e
def load(p):return json.loads((R/p).read_text())
def interval(d):return ball(d['norm_lower_ball'])[0],ball(d['norm_upper_ball'])[1]
def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 tick=time.monotonic();start=datetime.now(timezone.utc).isoformat();out=B/'verification/result.json';assert not out.exists()
 m=load('research/final_numerical_display_audit/verification/PROOF_FIRST.json');assert not m['checker_exists'] and not m['result_exists'];checks=[]
 def ck(v,label):
  checks.append({'check':label,'pass':bool(v)});assert v,label
 for p,h in m['inputs'].items():ck(sha(R/p)==h,'input '+p)
 text=(R/'research/final_report_numerical/source/report_v01.md').read_text();lines=text.splitlines()
 ck(sha(R/'research/final_report_numerical/source/report_v01.md')=='7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743','nominated report')
 heading=next((i+1 for i,s in enumerate(lines) if '| residual LB |' in s),None);ck(heading is not None,'literal lower-bound heading')
 d2=interval(load('research/whole_plane_norms/verification/d2_G0_ball_2048.json'))
 d016=load('research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json');components={k:(Q(v['accepted_lower_exact']),Q(v['accepted_upper_exact'])) for k,v in d016['norms'].items()}
 defects=[]
 for number,token,a,b,d,u in [(20,'G0 = 4.99',*d2,Q('4.99'),Q('.01')),(37,'G0 = 4.99',*d2,Q('4.99'),Q('.01')),(80,'7.1457012',*components['rF'],Q('7.1457012'),Q('.0000001'))]:
  hits=[(i+1,s) for i,s in enumerate(lines) if s.startswith('| '+str(number)+' |')];ck(len(hits)==1,'unique row'+str(number));ln,s=hits[0];ck(token in s,'display row'+str(number));ck(0<a<=b<d,'not lower bound row'+str(number));ck(d-u/2<a<=b<d+u/2,'valid nearest display row'+str(number));defects.append({'table_row':number,'frozen_line':ln,'display':str(d),'quantity_lower':str(a),'quantity_upper':str(b),'display_minus_upper':str(d-b)})
 raw0=load('research/registered_norm_assembly/source/N4_G0.json');rawD=load('research/registered_norm_assembly/source/N4_derivatives.json');g0=interval(raw0);g1=interval(rawD['norms']['G1']);ck(rawD['complete'],'complete007 derivatives')
 for label,x,ds in [('G0',g0,'0.3766893247'),('G1',g1,'3.4391037868')]:
  d=Q(ds);u=Q('1e-10');ck(d-u/2<x[0]<=x[1]<d+u/2,'007 nearest '+label);ck(ds in text,'report007 '+label)
 elementary_sq=2**15*g1[0]**2+2**20*g0[0]**2;ck(elementary_sq>Q('732.35')**2,'007 elementary 732.35');ck(1024*g0[0]>Q('385.72'),'007 elementary385.72')
 hs=load('research/background_sobolev/verification/C1-N1-007-d2w-j7-e2bal.json');cover=load('research/candidate_background_cover/verification/C1-N1-007-d2w-j7-e2bal_theta_2_25_768.json');hsi=ball(hs['gradient_identity_conditional_HS_upper']);ck(hsi[1]<Q('.72817'),'007 HS upper display');ck(Q('.728155')<hsi[0]<=hsi[1]<Q('.728165'),'007 HS nearest .72816');ck(cover['complete_partition'] and cover['all_pass'] and not cover['pending'] and not cover['inconclusive'],'007 complete accepted cover');ck(cover['tau']=='2/25','007 cover threshold');ck(ball(cover['signed_rate_lower'])[0]>Q('2.00215453001767'),'007 signed rate')
 ns=load('research/negative_norm_forcing_assembly/verification/result.json');targets={'FW-A2-Db':('606.739447','606.910169'),'FW-A2-Da':('606.818074','606.820306'),'FW-T-TB-rebal-v1':('606.503334','607.180020'),'FW-T-TB-sharp-v1':('604.299619','609.698720')};ratios={}
 ck(len(ns['instances'])==4,'four Ns instances')
 for row in ns['instances']:
  key=row['framework'];L,U=map(Q,targets[key]);ck(Q(row['strict_necessary_norm_lower'])==L and Q(row['strict_norm_upper'])==U,'Ns endpoint '+key);tau=Q(row['threshold_exact']);ck(tau>0 and L/tau>5700000,'Ns ratio '+key);ck(all(s in text for s in targets[key]),'Ns displayed '+key);ratios[key]=str(L/tau)
 a,b=components['G0'];ck(Q('.30888635')<a<=b<Q('.30888645'),'016 nearest G0 .3088864')
 order=load('research/candidate016_full_forcing/verification/result_v03.json')['XSW_pair_ordering'];ck(len(order)==5,'five matched norms')
 for row in order:ck(row['strict_007_less_than_016'] and Q(row['baseline007_upper_exact'])<Q(row['candidate016_lower_exact']),'strict same-norm ordering '+row['framework'])
 minima={}
 for name,candidate,ds in [('candidate015_dyadic_peer','C1-N1-015','1.242922259074'),('joint_scaled_dyadic016','C1-N1-016-legqs25-quot013','1.253908386497'),('candidate017_dyadic_preparation','C1-N1-017-legqs50-quot013','1.221854480167')]:
  p='research/'+name+'/verification/'+('result_v02.json' if name=='candidate015_dyadic_peer' else 'result.json');d=load(p);cells=d['cells'] if name=='candidate015_dyadic_peer' else d['results'][candidate]['seven_cells'];ck(len(cells)==7,'seven cells '+candidate)
  floors=[]
  for j,cell in enumerate(cells):
   floor=Q(cell['strict_ratio_floor']);ck(cell['excluded'] and floor>1,'accepted excluded cell '+candidate+' '+str(j));ck(ball(cell['ratio'])[0]>floor,'strict ratio retained '+candidate+' '+str(j));floors.append(floor)
  low=min(floors);ck(low==Q(ds),'minimum floor '+candidate);minima[candidate]=str(low)
 inputs=dict(m['inputs']);inputs.update({str(p.relative_to(R)):sha(p) for p in [Path(__file__),B/'verification/PROOF_FIRST.json']})
 result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'inputs':inputs,'checks':checks,'check_count':len(checks),'table_heading_line':heading,'not_directed_lower_bound':defects,'Ns_ratio_floors':ratios,'dyadic_ratio_floors':minima,'elementary_squared_lower_exact':str(elementary_sq),'new_integrals':False,'candidate_verdict_changes':False,'scope':'Selected finite display audit; underlying source proofs retained; complete017upper remains OPEN.','verdict':'CONFIRMED listed supplemental checks and nearest displays; REFUTED blanket interpretation of residual LB heading','elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'bindings',sha(out));print('heading',heading,'defects',[(x['table_row'],x['frozen_line']) for x in defects])
if __name__=='__main__':main()

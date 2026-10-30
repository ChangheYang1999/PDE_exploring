"""Change audit and strict nonunit optimizer check. No candidate integration."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import difflib,gzip,hashlib,json,sys,time
from flint import arb,fmpq,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');ctx.prec=p['precision_bits'];doc=(B/'source/THEORY_FINAL.md').read_text();base=(B/'../theory_v08_published_audit/source/THEORY_FINAL.md').read_text()
need('proof before checker',read('data/PROOF_FIRST.json')['checker_exists'] is False)
changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,base.splitlines(),doc.splitlines()).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
need('all24 frozen changed blocks',changes==read('data/changes.json') and len(changes)==24)
for topic,count in p['accepted_counts'].items():
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count)
for phrase in p['required_phrases']:need('target phrase '+phrase,phrase in doc)
old=read('../candidate016_cross_archive_audit/verification/result.json');optimizer=[]
for n in [1,3]:
 source=json.loads(gzip.decompress((B/f'../candidate016_cross_archive_audit/source/cross_mode_{n:03d}.json.gz').read_bytes()))
 row=next(x for x in old['rows'] if x['n']==n and x['kind']=='cross')
 a=arb.pi()*arb(fmpq(source['a_over_pi_exact']));b=arb(row['pairing_from_saved_groups']);err=a+b
 need(str(n)+' strict signs',a>0 and b<0 and err>0)
 need(str(n)+' error upper',err<arb(p['sum_upper']))
 displacement=err/a;loss=err**2/a;tstar=-b/a
 need(str(n)+' strictly nonunit minimizer',tstar<1 and tstar>0 and displacement>0 and displacement<arb(p['displacement_upper']))
 need(str(n)+' strictly positive loss',loss>0 and loss<arb(p['loss_upper']))
 need(str(n)+' complete-square agreement',(a+2*b+b*b/a).overlaps(loss))
 optimizer.append({'n':n,'a_plus_b':err.str(100),'one_minus_tstar':displacement.str(100),'t1_loss':loss.str(100),'exact_optimizer':'-b/a'})
comp=read('../candidate016_dual_replay_audit/source/components.json')['norms'];L={k:Q(v['accepted_lower_exact']) for k,v in comp.items()};U={k:Q(v['accepted_upper_exact']) for k,v in comp.items()};W=Q(20,21)*2**18
baseE=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2
threshold=Q(p['H_sufficient']);upper007=Q(p['007_E2_upper']);actualH=Q(old['H_strict_lower_exact'])
need('H threshold sufficient',baseE+W*threshold**2>upper007**2)
need('H margin exceeds1.39percent and rounds1.4',Q('1.0139')<actualH/threshold<Q('1.014'))
need('actualH lower square',Q(old['H_lower_square_exact'])>actualH**2)
need('strict E2 comparison',baseE+W*Q(old['H_lower_square_exact'])==Q(old['E2_lower_square_exact'])>Q(p['016_E2_lower'])**2>upper007**2)
need('registered017diagnostic factor',Q(p['017_diagnostic_lower'])/Q(p['graded_upper'])>Q('1.303'))
report=(B/'../frozen_report_1630_audit/source/FINAL_REPORT.md').read_text();note=(B/'source/T1_note55.md').read_text()
for val in ['606.8181534','606.8202172','605.4068697','605.9589546','0.6144195987']:need('registered display '+val,val in report)
need('inward007 lower',Q('606.8181535')>Q('606.8181534'))
need('inward007 upper',Q('606.8202171')<Q('606.8202172'))
need('inward017 lower',Q('605.4068698')>Q('605.4068697'))
need('inward017 upper',Q('605.9589545')<Q('605.9589546'))
need('conditional007017 gap',Q('606.8181534')-Q('605.9589546')>Q('.8591'))
need('007 coarse upper compatible',Q('606.8202172')<upper007)
need('T1 acknowledges repair','605.4068697' in note and '606.8181534' in note)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'target_sha256':sha(B/'source/THEORY_FINAL.md'),'changed_blocks':len(changes),'optimizer_checks':optimizer,'H_sufficient':p['H_sufficient'],'H_margin_factor_exact':str(actualH/threshold),'margin_display_scope':'1.4percent approximate; strict margin exceeds1.39percent','conditional017_E2_gap_lower':'.8591','foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED draft53 repaired scope and finite arithmetic. REFUTED exact optimal t=1, both modes have 0<a+b. REFUTED inward printed007/017 display endpoints as source enclosures. General474 now accepted481 and longer prefix480 are subsequent status updates. No new existence or017 certificate.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',r['elapsed_seconds'],'seconds')
for row in optimizer:print(row)

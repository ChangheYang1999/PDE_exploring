"""Read-only producer records; no producer code is imported or executed."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys,traceback,math
R=Path('research/hydrostatic_tail_rule_provenance');V=R/'verification';checks=[];bindings={}
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p).resolve();p.relative_to(Path.cwd().resolve());hh=sha(p);ck('binding '+str(p),(h is None or hh==h)and(str(p)not in bindings or hh==bindings[str(p)]));bindings[str(p)]=hh;return p
num=r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'
regions=['0, 0.1','0.1, 1','1, 100','100, 1e+300']
footer='   node arrays saved to artifacts/data/hs_points_export/hsG_c2.0_N160_log_nodes_resolved.npz (x, y, V1, V2, g, g_xi, g_y, R_h, N_f at all 6400 evaluated nodes; sha256 of the state recorded)'
def parse(text,q,export=False):
 rows=[z.rstrip()for z in text.splitlines()]
 if export:
  if q!=2 or len(rows)!=7 or rows[-1]!=footer:raise ValueError('exact export metadata footer')
  rows=rows[:-1]
 if len(rows)!=6:raise ValueError('exactly header/four regions/argmax')
 head=rows[0]
 if not head.startswith('hsG_c2.0_N160_log.pt 160x40 c=2.0: solver node |F|max (maps) 1.243e-07;  resolved evaluator'):raise ValueError('state/dimensions/c/F header')
 suffix=' AT THE SAME NODES (6400 points):' if q is None else f' (32, 10x16, 400, q={q}); rows: M collocation angles AT THE SAME NODES (6400 points):'
 prefix='hsG_c2.0_N160_log.pt 160x40 c=2.0: solver node |F|max (maps) 1.243e-07;  resolved evaluator'
 if q not in (None,2,3)or head!=prefix+suffix:raise ValueError('explicit rule/header')
 vals=[]
 for z,region in zip(rows[1:5],regions):
  pat=r'   r in \['+re.escape(region)+r'\): max \|R_h\| ('+num+r')   max \|R_h\|/N_f ('+num+r')   max N_f ('+num+r')   median \|R_h\|/N_f ('+num+r')'
  m=re.fullmatch(pat,z)
  if m is None:raise ValueError('region row '+region)
  if not all(math.isfinite(float(x))and float(x)>=0 for x in m.groups()):raise ValueError('nonnegative summary')
  vals.append(m.groups())
 pat=r'   argmax \|R_h\|/N_f at \(x, y\) = \(('+num+r'), ('+num+r')\), r = ('+num+r'), theta = ('+num+r') deg; R_h ('+num+r'), N_f ('+num+r')'
 m=re.fullmatch(pat,rows[5])
 if m is None or not all(math.isfinite(float(z))for z in m.groups()):raise ValueError('finite argmax line')
 return dict(header=head,export_footer=footer if export else None,numeric_lines=rows[1:],regional_tokens=vals,argmax_tokens=m.groups())
def chronological(text):
 lines=text.splitlines();prefix=['start ','q3 ch100 done ','DONE ']
 if len(lines)!=3 or not all(s.startswith(p)for s,p in zip(lines,prefix)):raise ValueError('three complete launch timestamps')
 times=[datetime.strptime(s[len(p):],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)for s,p in zip(lines,prefix)]
 if not(times[0]<=times[1]<=times[2]<=datetime.now(timezone.utc)):raise ValueError('chronological actual log records')
 return [t.isoformat()for t in times]
def same(a,b):
 if a['numeric_lines']!=b['numeric_lines']:raise ValueError('printed numeric lines differ')
def reject(n,fn):
 try:fn()
 except ValueError:ck(n,True)
 else:raise AssertionError('did not reject '+n)
def manufacture():
 prefix='hsG_c2.0_N160_log.pt 160x40 c=2.0: solver node |F|max (maps) 1.243e-07;  resolved evaluator'
 base=prefix+' (32, 10x16, 400, q=2); rows: M collocation angles AT THE SAME NODES (6400 points):\n'
 for r in regions:base+=f'   r in [{r}): max |R_h| 1.000e-6   max |R_h|/N_f 2.000e-6   max N_f 1.000e0   median |R_h|/N_f 1.00e-6\n'
 base+='   argmax |R_h|/N_f at (x, y) = (1, 2), r = 2.236, theta = 63.4 deg; R_h 1e-6, N_f 0.5\n'
 a=parse(base,2);same(a,parse(base,2));ck('synthetic equal complete record',True)
 reject('changed numeric token',lambda:same(a,parse(base.replace('1.000e-6','1.001e-6',1),2)))
 reject('wrong q',lambda:parse(base,3));reject('wrong dimensions',lambda:parse(base.replace('160x40','160x41'),2))
 reject('missing row',lambda:parse('\n'.join(base.splitlines()[:-2]+base.splitlines()[-1:]),2))
 reject('duplicate region',lambda:parse(base.replace('0.1, 1','0, 0.1'),2))
 reject('malformed residual field',lambda:parse(base.replace('1.000e-6','nan',1),2))
 reject('overflowing numerical token',lambda:parse(base.replace('1.000e-6','1e999',1),2))
 old=base.replace(' (32, 10x16, 400, q=2); rows: M collocation angles','');parse(old,None);ck('synthetic old header',True)
 reject('changed argmax token',lambda:same(a,parse(base.replace('(1, 2)', '(1, 3)'),2)))
 reject('malformed argmax line',lambda:parse(base.replace('theta =','theta IS'),2))
 reject('interior blank line',lambda:parse(base.replace('   r in [0, 0.1)', '\n   r in [0, 0.1)'),2))
 pp=parse(base+footer+'\n',2,export=True);same(a,pp);ck('exact export footer',pp['export_footer']==footer)
 reject('changed export footer',lambda:parse(base+footer.replace('all 6400','all 6401')+'\n',2,export=True))
 reject('missing export footer',lambda:parse(base,2,export=True))
 reject('export footer without explicit mode',lambda:parse(base+footer+'\n',2))
 reject('extra line',lambda:parse(base+'irrelevant\n',2))
 tt='start 2026-10-20T12:44:21Z\nq3 ch100 done 2026-10-20T12:44:22Z\nDONE 2026-10-20T12:44:23Z\n';chronological(tt);ck('synthetic ordered times',True)
 reject('nonchronological times',lambda:chronological(tt.replace('12:44:22','12:44:20')))
 reject('missing DONE',lambda:chronological('\n'.join(tt.splitlines()[:-1])))
 reject('future timestamp',lambda:chronological(tt.replace('DONE 2026-10-20','DONE 2999-10-20')))
 da=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());bind(V/'SOURCE_INPUTS.json',da['bindings'][str((V/'SOURCE_INPUTS.json').resolve())])
 for p in [__file__,R/'CONTROLLED_RECORD_PROOF.md',R/'CONTROLLED_RECORD_REPAIR_PROOF.md',R/'CONTROLLED_EXPORT_FOOTER_PROOF.md']:bind(p)
 return dict(status='PASS_CONTROLLED_RECORD_MANUFACTURES',utc=now(),count=len(checks),checks=checks,bindings=bindings)
def preflight():
 b=Path('research/new_node_export_record_audit/verification');fin=json.loads(bind(b/'FINAL_BINDINGS.json').read_text());e=[]
 for p in [b/'SOURCE_INPUTS.json',b/'EXPORT_INPUTS.json',b/'producer_export_script.py',Path('research/accurate_map_final_audit/verification/hs_node_check_c2_N160.txt'),b/'exports/hs_node_check_c2_N160_export.txt']:
  bind(p,fin['bindings'][str(p)]);e.append(dict(path=str(p),relative_key_present=True,sha256=sha(p)))
 old=Path('research/accurate_map_final_audit/verification/hs_node_check_c2_N160.txt');new=b/'exports/hs_node_check_c2_N160_export.txt'
 for p,q,ex in [(old,None,False),(new,2,True)]:e.append(dict(path=str(p),header=parse(p.read_text(),q,export=ex)['header'],export_mode=ex))
 da=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());note=bind(V/'producer_note175.txt',da['bindings'][str((V/'producer_note175.txt').resolve())]).read_text()
 ck('precise recorded chunk phrase','with exponent 2 (chunks of\n1500)' in note)
 for p in [__file__,R/'CONTROLLED_RECORD_REPAIR_PROOF.md',R/'CONTROLLED_EXPORT_FOOTER_PROOF.md',V/'CONTROLLED_RECORD_MANUFACTURES.json']:bind(p)
 return dict(status='PASS_323_RELATIVE_SCHEMA_AND_ACCEPTED_HEADERS',utc=now(),count=len(checks),checks=checks,bindings=bindings,records=e,scope='Preflight on accepted323 records only; no controlledq2/q3 comparison or candidate inverse.')

def run():
 mf=json.loads(bind(V/'CONTROLLED_RECORD_MANUFACTURES.json').read_text());ck('manufactures passed',mf['status']=='PASS_CONTROLLED_RECORD_MANUFACTURES'and mf['count']==len(mf['checks'])and all(z['passed']for z in mf['checks']))
 for p,h in mf['bindings'].items():bind(p,h)
 src=Path('../numerics/runs');log=(src/'q_test.out').read_bytes();times=chronological(log.decode());ck('launch complete',True,times)
 out=V/'controlled_records';out.mkdir(exist_ok=True);sources=[]
 for n in ['q_test.out','launch_q_test.sh','hs_node_check_c2_N160_q3_ch100.txt','hs_node_check_c2_N160_q2_ch100.txt']:
  p=src/n;a=p.read_bytes();b=p.read_bytes();ck('stable immediate bytes '+n,a==b);target=out/n
  if target.exists():ck('preserve prior frozen '+n,target.read_bytes()==a)
  else:target.write_bytes(a)
  bind(target);sources.append(dict(source=str(p.resolve()),frozen=str(target),sha256=sha(target),scope='local record bytes, not execution authentication'))
 ck('captured log matches completion', (out/'q_test.out').read_bytes()==log)
 shell=(out/'launch_q_test.sh').read_text()
 for q in [2,3]:ck('recorded launch env '+str(q),f'HS_Q={q} HS_CH=100 python3 src/hs_node_check.py runs/hsG_c2.0_N160_log.pt > runs/hs_node_check_c2_N160_q{q}_ch100.txt 2>&1' in shell)
 b323=Path('research/new_node_export_record_audit/verification');fin=json.loads(bind(b323/'FINAL_BINDINGS.json').read_text());ck('323 accepted',fin['status']=='CONFIRMED_FINITE_NEW_NODE_EXPORT_RECORD_AUDIT')
 sourcecfg=json.loads(bind(b323/'SOURCE_INPUTS.json',fin['bindings'][str(b323/'SOURCE_INPUTS.json')]).read_text())
 for z in sourcecfg['files']:bind(z['frozen'],z['sha256'])
 checker=bind(b323/'producer_export_script.py',fin['bindings'][str(b323/'producer_export_script.py')]).read_text();ck('recorded export default chunk1500','environ.get("HS_CH", "1500")'in checker)
 prov=json.loads(bind(V/'SOURCE_INPUTS.json').read_text())
 for z in prov['files']:bind(z['frozen'],z['sha256'])
 da=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());note=bind(V/'producer_note175.txt',da['bindings'][str((V/'producer_note175.txt').resolve())]).read_text();ck('recorded export chunk1500 note','with exponent 2 (chunks of\n1500)' in note)
 old=Path('research/accurate_map_final_audit/verification/hs_node_check_c2_N160.txt');new=b323/'exports/hs_node_check_c2_N160_export.txt'
 for p in [old,new]:bind(p,fin['bindings'][str(p)])
 cfg=json.loads(bind(b323/'EXPORT_INPUTS.json',fin['bindings'][str(b323/'EXPORT_INPUTS.json')]).read_text())['states'][0]
 ck('S160 export identity',cfg['tag']=='S160'and cfg['N']==160 and cfg['M']==40 and cfg['state_sha256']=='60e3a92f81620d109192e1557e5da3e27d4d8b0c534fac63afd07dac09c9ac20');bind(cfg['state'],cfg['state_sha256']);bind(cfg['export'],cfg['export_sha256'])
 a=parse(old.read_text(),None);b=parse(new.read_text(),2,export=True);c=parse((out/'hs_node_check_c2_N160_q3_ch100.txt').read_text(),3);d=parse((out/'hs_node_check_c2_N160_q2_ch100.txt').read_text(),2)
 same(a,c);ck('q3 ch100 equals old every numeric line',True)
 same(b,d);ck('q2 ch100 equals export ch1500 every numeric line',True)
 diffs=[dict(region=regions[i],field=['absolute_R','normalized_Rf','max_Nf','median_Rf'][j],q3=x,q2=y)for i,(aa,bb)in enumerate(zip(c['regional_tokens'],d['regional_tokens']))for j,(x,y)in enumerate(zip(aa,bb))if x!=y]
 argdiff=[dict(field=['x','y','r','theta_degrees','R_h','N_f'][j],q3=x,q2=y)for j,(x,y)in enumerate(zip(c['argmax_tokens'],d['argmax_tokens']))if x!=y]
 ck('regional and argmax differences recorded',True,dict(regional=diffs,argmax=argdiff))
 for p,h in list(bindings.items()):bind(p,h)
 return dict(status='CONFIRMED_CONTROLLED_PRINTED_RECORD_EQUALITIES_REQUIRES_REVIEW',utc=now(),count=len(checks),checks=checks,bindings=bindings,sources=sources,times=times,records=dict(old=a,export=b,q3_ch100=c,q2_ch100=d),changed_region_tokens=diffs,changed_argmax_tokens=argdiff,scope='Printed local record equality only. Historical execution, unrounded equality, inverse accuracy and causal proof remain OPEN. Primary IPM UNRESOLVED.')
if __name__=='__main__':
 try:
  if sys.argv[1:]==['--manufactures']:d=manufacture();name='CONTROLLED_RECORD_MANUFACTURES.json'
  elif sys.argv[1:]==['--preflight']:d=preflight();name='CONTROLLED_PREFLIGHT.json'
  elif not sys.argv[1:]:d=run();name='CONTROLLED_RECORD_CHECKS.json'
  else:raise ValueError('unsupported args')
  (V/name).write_text(json.dumps(d,indent=2)+'\n');print(d['status'],d['count'])
 except Exception:
  (V/('CONTROLLED_FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')).write_text(json.dumps(dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise

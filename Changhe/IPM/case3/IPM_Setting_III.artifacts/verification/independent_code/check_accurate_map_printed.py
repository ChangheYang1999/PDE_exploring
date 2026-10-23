"""Exact printed-record transcription check. No producer execution or inverse inference."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,json,hashlib,re,sys,traceback
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
R=Path('research/accurate_map_final_audit');V=R/'verification';checks=[];bindings={};numeric=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);s=sha(p);ck('binding '+str(p),(h is None or h==s)and(str(p)not in bindings or bindings[str(p)]==s));bindings[str(p)]=s;return p
NUM=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
def interval(t):
 if not isinstance(t,str)or not re.fullmatch(NUM,t):raise ValueError('invalid decimal')
 a=re.split('[eE]',t);e=int(a[1])if len(a)>1 else 0
 if abs(e)>1000:raise ValueError('exponent')
 h=F(10)**(e-(len(a[0].split('.')[1])if'.'in a[0]else 0));v=F(t);return(v-h/2,v+h/2)
def contained(a,b):return b[0]<=a[0]<=a[1]<=b[1]
def literal(n):
 if isinstance(n,ast.Constant)and isinstance(n.value,str):return n.value
 if isinstance(n,ast.Name)and n.id=='CHK':return'TODO checker sentence'
 if isinstance(n,ast.BinOp)and isinstance(n.op,ast.Add):return literal(n.left)+literal(n.right)
 if isinstance(n,(ast.Tuple,ast.List)):return[literal(v)for v in n.elts]
 raise ValueError('nonliteral AST')
def replacements(source):
 t=ast.parse(source);b=[n for n in t.body if isinstance(n,ast.AugAssign)and isinstance(n.target,ast.Name)and n.target.id=='body'];f=[n for n in t.body if isinstance(n,ast.Assign)and isinstance(n.targets[0],ast.Name)and n.targets[0].id=='_fix']
 if len(b)!=1 or len(f)!=1:raise ValueError('replacement groups')
 rows=literal(b[0].value)
 for old,new in literal(f[0].value):
  if rows[0][1].count(old)!=1:raise ValueError('ambiguous patch')
  rows[0][1]=rows[0][1].replace(old,new)
 return rows

def main():
 for p in [__file__,R/'PRINTED_RECORD_PROOF.md',R/'FINAL_PROVENANCE_AND_COVERAGE_PROOF.md']:bind(p)
 for token,oracle in [('1.23',(F(245,200),F(247,200))),('-1.2e-3',(-F(25,20000),-F(23,20000))),('0',(F(-1,2),F(1,2)))]:ck('rational interval '+token,interval(token)==oracle)
 ck('source containment hand oracle',contained(interval('1.234'),interval('1.23'))and not contained(interval('1.235'),interval('1.23')))
 ck('closed endpoint hand oracle',contained((F(1),F(2)),(F(1),F(2))))
 for token in ['NaN','Inf','1/3','1e1001','']:
  try:interval(token)
  except ValueError:ck('malformed refused '+token,True)
  else:raise AssertionError('bad accepted')
 for bad in ['run()','a.b','1','f"{x}"']:
  try:literal(ast.parse(bad,mode='eval').body)
  except ValueError:ck('nonliteral refused '+bad,True)
  else:raise AssertionError('execution admitted')
 d=json.loads(bind(V/'RECORD_CHECKS.json').read_text());ck('record gate',d['status']=='PASS_FROZEN_ACCURATE_MAP_RECORD_CONSISTENCY'and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
 states={z['tag']:z for z in d['records']};result={k:v['result']for k,v in states.items()};rows=replacements(bind(V/'lead_reps320_v3.py').read_text());lst=bind(V/'lead_draft_list_v3.txt').read_text()
 for old,new in rows:ck('literal replacement list agreement',old in lst and new.replace('TODO checker sentence','The checker [...].')in lst)
 text=' '.join(z[1]for z in rows);ck('three replacement groups',len(rows)==3)
 def val(label,t,x,clause=None,printed=False):
  ck('token context '+label,t in(text if clause is None else clause)and(clause is None or clause in text));q=interval(x)if printed else(F(float(x)),F(float(x)));ok=contained(q,interval(t));numeric.append(dict(label=label,report=t,source=str(x),source_scope='printed source interval'if printed else'exact dyadic saved metadata',target=list(map(str,interval(t))),source_interval=list(map(str,q)),passed=ok));ck('numeric '+label,ok,numeric[-1])
 for tag,t in [('A','5.3e-3'),('B','2.8e-9'),('C','3.7e-8'),('E','8.1e-6'),('G80','2.6e-5'),('G96','8.1e-6'),('G112','6.6e-6'),('G128','2.3e-6')]:val(tag+' raw node norm',t,result[tag]['nodes_Fmax'])
 for tag,idx,t in [('B',2,'9.7e-2'),('C',2,'5.4e-2'),('B',3,'0.60'),('C',3,'0.18'),('E',2,'3.15e-5'),('E',3,'5.4e-7'),('E',0,'4.7e-4')]:val(tag+' sampled region '+str(idx),t,result[tag]['sampled'][idx][3])
 for tag,t in [('B','7.17e6'),('C','2.28e6')]:val(tag+' rmax',t,states[tag]['midpoint_rmax'])
 tokens=dict(annulus=['1.03e-4','3.15e-5','2.38e-5','7.98e-6'],far=['7.9e-7','5.4e-7','4.7e-7','6.7e-8'],core=['2.1e-3','4.7e-4','2.1e-4','1.7e-5'],delta=['-4.8e-3','-1.12e-3','-3.7e-4','-9.4e-6'],E=['+120.4','+34.70','+7.75','-1.570'],B=['+211.5','+54.81','+12.75','-9.552'],B6E=['-510.7','-153.4','-33.75','-0.13'],rmax=['1.1e6','2.3e6','4.2e6','7.2e6'])
 for i,tag in enumerate(['G80','G96','G112','G128']):
  z=result[tag]
  for key,index in [('annulus',2),('far',3),('core',0)]:val(tag+' '+key,tokens[key][i],z['sampled'][index][3])
  for key,field in [('delta','centre_defect_single'),('E','E'),('B','B')]:val(tag+' '+key,tokens[key][i],z[field])
  # Exact dyadic subtraction avoids a second rounded computation.
  x=F(z['B'])-6*F(z['E']);t=tokens['B6E'][i];ck('exact B minus6E '+tag,interval(t)[0]<=x<=interval(t)[1]and t in text,dict(value=str(x),token=t));numeric.append(dict(label=tag+' Bminus6E',report=t,source=str(x),passed=True))
  val(tag+' rmax',tokens['rmax'][i],states[tag]['midpoint_rmax'])
 val('E center','-1.12e-3',result['E']['centre_defect_single']);val('E cubic','+34.71',result['E']['E'])
 ck('decreasing sampled defects',all(result[a]['sampled'][k][3]>result[b]['sampled'][k][3]for a,b in zip(['G80','G96','G112'],['G96','G112','G128'])for k in [0,2,3]))
 ck('decreasing recorded center magnitude',all(abs(result[a]['centre_defect_single'])>abs(result[b]['centre_defect_single'])for a,b in zip(['G80','G96','G112'],['G96','G112','G128'])))
 for field,bound in [('E',9),('B',22)]:ck('strict last cubic change '+field,abs(F(result['G112'][field])-F(result['G128'][field]))>bound)
 def cauchy(name,pair,lineindex=0):
  s=bind(V/name).read_text();lines=[l for l in s.splitlines()if l.startswith(pair)];ck('cauchy schema '+name,len(lines)>lineindex and'19649 points (401 log radii 1e-3..1e7 x 49 angles incl. both axes)'in s);line=lines[lineindex];suf=line.split('->',1)[1].split(None,1)[1];a=re.findall(NUM,suf);ck('15 region columns '+name,len(a)==15);return a
 seq=[]
 for pair,t in [('80x20 -> 96x24','2.67e-2'),('96x24 -> 112x28','2.29e-3'),('112x28 -> 128x32','3.82e-3')]:
  x=cauchy('hs_cauchy_acc6_fine_seq.txt',pair)[6];seq.append(F(x));val('sequence '+pair,t,x,printed=True)
 ck('recorded differences nonmonotone',seq[2]>seq[1])
 val('standard128 vs G128','0.22',cauchy('hs_cauchy_acc_fine_vs_std.txt','128x32 -> 128x32')[6],printed=True)
 val('standard160 vs G128','0.16',cauchy('hs_cauchy_acc6_128_vs_std160.txt','160x40 -> 128x32')[6],printed=True)
 note=bind(V/'producer_note167.md').read_text();ck('E G96 difference note only','states differ by 9.7e-7 in the same metric.'in note and'by 9.7e-7 in the'in text)
 for name,first,cnt,ts in [('hs_node_check_c2_N160.txt','hsG_c2.0_N160_log.pt',6400,['1.3e-5','4.4e-5','3.6e-5','8.6e-5']),('hs_node_check_c2_N128_acc6_fine.txt','hsQ_c2.0_N128_acc6_fine.pt',12288,['1.5e-5','2.4e-5','1.0e-5','2.9e-8'])]:
  s=bind(V/name).read_text();ck('node record identity '+name,s.startswith(first)and str(cnt)+' points'in s);a=re.findall(r'max \|R_h\|/N_f ('+NUM+')',s);ck('four node regions '+name,len(a)==4)
  for i,(t,x)in enumerate(zip(ts,a)):val(name+' region '+str(i),t,x,printed=True)
 for n,ts in [(192,['3.2e-5','2.4e-5','2.9e-5','1.1e-5']),(224,['3.3e-5','4.6e-5','4.9e-5','2.2e-5'])]:
  p=Path('research/hydrostatic_larger_node_audit/verification')/('producer_hs_node_check_c2_N'+str(n)+'.txt');s=bind(p).read_text();a=re.findall(r'max \|R_h\|/N_f ('+NUM+')',s);ck('larger four node regions '+str(n),len(a)==4)
  for i,(t,x)in enumerate(zip(ts,a)):val(str(n)+' node region '+str(i),t,x,printed=True)
  val(str(n)+' node raw','1.8e-7'if n==192 else'1.3e-7',re.search(r'\(maps\) ('+NUM+')',s)[1],printed=True)
 val('160 node raw','1.2e-7',re.search(r'\(maps\) ('+NUM+')',(V/'hs_node_check_c2_N160.txt').read_text())[1],printed=True)
 for name,changes,modes in [('hs_angular_scan_acc128.txt',[31,32,32,32],[33,32,32,32]),('hs_angular_scan_acc6_fine128.txt',None,[22,27,2])]:
  s=bind(V/name).read_text();a=[int(x)for x in re.findall(r'dominant cos 2k theta mode k = (\d+)',s)];b=[int(x)for x in re.findall(r'sign changes over the quadrant (\d+)',s)];ck('angular mode records '+name,a==modes);ck('angular sign records '+name,changes is None or b==changes)
 for phrase in ['normalized residual R_h/N_f','interpolated onto the collocation rays','finite scans do not establish a mechanism','finite scans, which do not exclude aliasing','Four states establish neither convergence nor a limit','TODO checker sentence']:ck('scope phrase '+phrase,phrase in text)
 for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
 out=dict(status='PASS_PRINTED_ACCURATE_MAP_RECORDS_WITH_OPEN_TEXT_SCOPE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,numeric_count=len(numeric),numeric=numeric,required_repairs=['Replace exact centre defects by evaluations of the exact center formula, or explicitly state that the displayed values are floating-point evaluations and cite own rational scalars once complete.','CHK must distinguish producer-record checks at160/oversampled128 all-node sets from318 independent192/224 and320 independent between-node/center/function results.','Lead draft timeline05:21 currently describes the already installed report88 node comparison, not the new accurate-map draft. Repair assembled chronology when preparing draft89.'],scope='Record transcription only. Independent inverse/center/common-grid results await320;192/224 all-node independent results await318. Actual complete draft and CHK still OPEN.')
 p=V/'PRINTED_RECORD_CHECKS.json';p.write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),len(numeric))
if __name__=='__main__':
 try:main()
 except Exception:
  p=V/('PRINTED_RECORD_FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json');p.write_text(json.dumps(dict(checks=checks,bindings=bindings,numeric=numeric,error=traceback.format_exc()),indent=2)+'\n');raise

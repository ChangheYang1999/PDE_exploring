from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,re,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=384
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==m['proof_sha256']
for rel,h in m['inputs'].items():assert sha(B/rel)==h,rel
text=(B/'source/numerics_v12.md').read_text();final=(B/'source/NUMERICS_FINAL.md').read_text()
p=json.loads((B/'data/parameters.json').read_text());checks=[];tables={};ratios=[]
def check(name,test,value=None):
 assert test,name
 checks.append({'claim':name,'value':str(value) if value is not None else None})
for number,child in [(1,'024'),(2,'025')]:
 part=text.split('## '+str(number)+'. ',1)[1].split('\n## ',1)[0];rows={}
 for line in part.splitlines():
  v=[x.strip() for x in line.strip('|').split('|')]
  match=re.match(r'\((\d+), (\d+)\) \[registered, HELD OUT\]',v[0])
  if match:
   key=tuple(map(int,match.groups()));assert key not in rows
   rows[key]={'r_peak':Q(v[1]),'016':Q(v[2]),'022':Q(v[3]),'023':Q(v[4]),child:Q(v[5])}
 assert len(rows)==25;tables[child]=rows
 check(child+' full registered grid',set(rows)=={(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]})
for row in p['comparisons']:
 r=tables[row['table']][tuple(row['probe'])];value=r[row['numerator']]/r[row['denominator']]
 check(row['name'],Q(row['lower'])<value<Q(row['upper']),value)
 ratios.append(dict(row,exact_ratio=str(value)))
 check(row['name']+' raw source values',str(r[row['numerator']])==str(Q(row['raw_numerator'])) and str(r[row['denominator']])==str(Q(row['raw_denominator'])))
 check(row['name']+' stated radius',r['r_peak']==Q(row['r_peak']))
five=[tables['025'][(n,600)]['025']/tables['025'][(n,600)]['016'] for n in [19,23,25,29,31]]
check('025 K600 four of five decrease',sum(r<1 for r in five)==4)
check('025 K600 four reduction factors between2and30',all(2<1/r<30 for r in five if r<1))
check('025 all ten K1800 andK2400 increase',all(r['025']>r['016'] for (n,k),r in tables['025'].items() if k>=1800))
part=next(line for line in final.splitlines() if line.startswith('- C1-N1-026 (tag'))
num=r'[0-9]+(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?'
pattern=r'\((\d+),(\d+)\) ('+num+') / ('+num+') / ('+num+')'
r26={tuple(map(int,x[:2])):list(map(Q,x[2:])) for x in re.findall(pattern,part)}
for row in p['026_comparisons']:
 values=r26[tuple(row['probe'])];value=values[2]/values[1]
 check(row['name'],Q(row['lower'])<value<Q(row['upper']),value)
 check(row['name']+' raw values',values[1]==Q(row['raw_parent']) and values[2]==Q(row['raw_child']))
 ratios.append(dict(row,exact_ratio=str(value)))
check('026 K600 four of five decrease',sum(r26[(n,600)][2]<r26[(n,600)][1] for n in [19,23,25,29,31])==4)
factors=[]
for n in ['023','024']:
 weak=json.loads((B/'source'/f'{n}_weak.json').read_text());point=json.loads((B/'source'/f'{n}_point.json').read_text())
 floor=Q(weak['strict_lower_exact']);check(n+' exact floor',floor==Q(p['floors'][n]))
 ratio=floor/Q(25,54684);lo,hi=p['graded_factors'][n]
 check(n+' graded factor proper rounding',Q(lo)<ratio<Q(hi),ratio)
 factors.append({'candidate':n,'ceiling':'25/54684','exact_floor_ratio':str(ratio),'safe_lower':lo,'unsafe_lower_from_this_witness':hi})
 gap=arb(point['uniform_graded_gap']);lo,hi=p['gaps'][n]
 check(n+' point gap safe lower and rounded up display',arb(lo)<gap<arb(hi),gap)
 if n=='023':
  ratio=floor/Q('0.0000028496');check('023 sharpw factor proper rounding',Q('924.6')<ratio<Q('924.7'),ratio)
 if n=='024':
  check('024 finished before v12',datetime.fromisoformat(weak['utc'])<datetime.fromisoformat('2026-10-29T12:32:15+00:00'))
for key in ['RUN_1. Reading of the GPU phase','this header is clean','| candidate | LOSS (MID 16) |','024 is OPEN pending','Both versions precede the 10:37Z launch.']:
 check('document contains '+key,key in text)
check('024 MID32 source statement','optimization objective evaluated on the MID 32 radial rule' in text)
check('no source-code execution',True)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'check_count':len(checks),'source_bindings':len(m['inputs']),'registered_rows_parsed':50,'comparisons':ratios,'factors':factors,'checks':checks,'foreign_code_executed':False,'scope':'Exact internal consistency of printed FLOAT data, documentary labels, accepted witness arithmetic; no candidate evaluation','verdict':'REFUTED uniform summary ranges; corrected comparisons CONFIRMED'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',len(checks),'checks',r['utc'],'elapsed',r['elapsed_s'])

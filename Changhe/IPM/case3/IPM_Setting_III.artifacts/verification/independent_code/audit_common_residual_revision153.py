"""Result287 revision153: literal source decimals, no double rounding."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
import json,hashlib,re,traceback,sys
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';Q=V/'revision153';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];rows=[];sources=[]
mode='adaptive'if '--adaptive'in sys.argv else'fixed';out=dict(status='RUNNING',mode=mode,started_utc=utc(),checks=checks,comparisons=rows,sources=sources,proof_sha256=sha(R/'REVISION153_PROOF.md'),driver_sha256=sha(__file__),input_sha256=sha(Q/'INPUTS.json'),summary_sha256=sha(V/'SUMMARY.json'),scope='Empirical reproduction of actual decimal tokens on the common finite grid. No continuum bound or IPM endpoint. Fixed-only mismatches are provisional.')
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save():
 out['updated_utc']=utc();(Q/('ADAPTIVE_COMPARISON.json'if mode=='adaptive'else'FIXED_COMPARISON.json')).write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
def record(source,c,N,M,region,metric,token,line):
 ck('literal token '+source+str((c,N,region,metric)),bool(re.fullmatch(r'[+-]?\d+(?:\.\d*)?(?:e[+-]?\d+)?',token))and F(token)>=0)
 sources.append(dict(source=source,c=c,N=N,M=M,region=region,metric=metric,token=token,line=line))
try:
 inp=json.loads((Q/'INPUTS.json').read_text())
 for x in inp['files']:ck('frozen revision '+x['path'],sha(x['path'])==x['sha256'])
 s=json.loads((V/'SUMMARY.json').read_text());ck('fixed summary complete',s['status']=='PASS'and all(x['passed']for x in s['checks']));ck('fixed summary driver',s['driver_sha256']==sha('independent_code/summarize_hydrostatic_common_residuals.py'))
 for p,h in s['source_sha256'].items():ck('fixed source '+p,sha(p)==h)
 fixed={(t['c'],t['N'],t['region'],t['metric']):t for t in s['comparisons']};ck('unique70 original records',len(fixed)==70 and len(s['comparisons'])==70)
 for c,filename in [(2,'producer_hs_common_res_c2.txt'),(3,'producer_hs_common_res_c3_hsG.txt')]:
  lines=(Q/filename).read_text().splitlines();ck('q2 header '+str(c),'q = 2'in lines[0]and'per region: max |R_h| / max |R_h|/N_f'in lines[0]);seen=set()
  for no,line in enumerate(lines,1):
   m=re.fullmatch(r'(\d+)x(\d+)\s+(.+)',line)
   if not m:continue
   N,M=int(m[1]),int(m[2]);ck('unique artifact row '+str((c,N)),N not in seen);seen.add(N);values=m[3].split();ck('artifact ten tokens '+str((c,N)),len(values)==10);ck('artifact state shape '+str((c,N)),sum(t['c']==c and t['N']==N for t in s['rows'])==1 and M==N//4)
   for i,token in enumerate(values):record(filename,c,N,M,i//2,['Rh','Rf'][i%2],token,no)
  ck('artifact exact sizes '+str(c),seen==({96,128,160,192}if c==2 else{64,96,128}))
 text=(Q/'producer_NUM_REPORT.md').read_text();anchor='    (10) Residuals on ONE common point set with ONE evaluator';ck('unique item10 anchor',text.count(anchor)==1);block=text[text.index(anchor):];block=block[:block.index('    (Tokens to two significant digits')];report2=[];report3=[]
 for no,line in enumerate(block.splitlines(),1):
  if 'c = 2:'in line:line=line.split('c = 2:',1)[1]
  if 'c = 3:'in line:
   for part in line.split('c = 3:',1)[1].split(';'):
    m=re.fullmatch(r'\s*(\d+)x(\d+)\s+(.+?)\s*',part);ck('parse report c3 segment',m is not None,part);N,M=int(m[1]),int(m[2]);values=m[3].split();ck('five c3 report ratios '+str(N),len(values)==5);report3.append(N)
    for k,token in enumerate(values):record('report',3,N,M,k,'Rf',token,no)
   continue
  m=re.fullmatch(r'\s*(\d+)x(\d+)c?\s+(.+?)\s*\((.+)\)\s*',line)
  if m:
   N,M=int(m[1]),int(m[2]);values=m[3].split();raw=m[4];raw=raw[len('|R_h| '):]if raw.startswith('|R_h| ')else raw;abs_values=[z.strip()for z in raw.split(',')];ck('report c2 schema '+str(N),len(values)==5 and len(abs_values)==3);report2.append(N)
   for k,token in enumerate(values):record('report',2,N,M,k,'Rf',token,no)
   for k,token in enumerate(abs_values,2):record('report',2,N,M,k,'Rh',token,no)
 ck('report exact states',report2==[96,128,160,192]and report3==[64,96,128]);ck('117literal comparisons',len(sources)==117);ck('unique source tokens',len({(t['source'],t['c'],t['N'],t['region'],t['metric'])for t in sources})==117)
 adaptive={}
 if mode=='adaptive':
  a=json.loads((V/'ADAPTIVE_SUMMARY.json').read_text());ck('adaptive summary complete',a['status']=='PASS'and all(x['passed']for x in a['checks']));ck('adaptive summary driver',a['driver_sha256']==sha('independent_code/summarize_common_residual_adaptive.py'));out['adaptive_summary_sha256']=sha(V/'ADAPTIVE_SUMMARY.json')
  for p,h in a['source_sha256'].items():ck('adaptive source '+p,sha(p)==h)
  adaptive={(t['c'],t['N'],t['region'],t['metric']):t for t in a['tokens']};ck('70adaptive references',len(adaptive)==70)
 for t in sources:
  key=(t['c'],t['N'],t['region'],t['metric']);old=fixed[key];val=F.from_float(old['value']);center=F(t['token']);half=F(10)**Decimal(t['token']).as_tuple().exponent/2;diff=val-center;inside=abs(diff)<=half;row=dict(**t,tag=old['tag'],index=old['index'],fixed_value=old['value'],half_width=str(half),fixed_signed_difference=str(diff),fixed_agrees=inside,verdict='OPEN',scope='Provisional fixed-rule comparison; adaptive and local derivative followup pending.');rows.append(row)
  if mode=='adaptive':
   ref=adaptive[key];av=F.from_float(ref['adaptive_value']);adiff=av-center;ainside=abs(adiff)<=half;emp=ref['empirical_sensitivity'];distance=min(abs(abs(adiff)-half),abs(abs(diff)-half));stable=distance>10*F.from_float(emp);same=(adiff>half and diff>half)or(adiff< -half and diff< -half);verdict='CONFIRMED'if inside and ainside and stable else'REFUTED'if not inside and not ainside and same and stable else'OPEN';row.update(adaptive_value=ref['adaptive_value'],adaptive_index=ref['adaptive_index'],adaptive_agrees=ainside,adaptive_signed_difference=str(adiff),minimum_rounding_margin=str(distance),observed_sensitivity=emp,verdict=verdict,coverage=ref['coverage'],scope='Finite-grid reproduction with tenfold observed quadrature sensitivity margin; no rigorous enclosure, and local derivative followup is separate.')
 out.update(status='PASS',count=len(checks),finished_utc=utc());save();print('PASS',len(checks),mode,utc())
 for source in ['producer_hs_common_res_c2.txt','producer_hs_common_res_c3_hsG.txt','report']:
  z=[x for x in rows if x['source']==source];print(source,'tokens',len(z),'fixed mismatches',sum(not x['fixed_agrees']for x in z),'verdicts',{k:sum(x['verdict']==k for x in z)for k in ['CONFIRMED','REFUTED','OPEN']})
  for x in z:
   if not x['fixed_agrees']:print('MISMATCH',x['c'],x['N'],x['region'],x['metric'],x['token'],x['fixed_value'])
except Exception:
 out.update(status='FAIL',count=len(checks),finished_utc=utc(),traceback=traceback.format_exc());save();raise

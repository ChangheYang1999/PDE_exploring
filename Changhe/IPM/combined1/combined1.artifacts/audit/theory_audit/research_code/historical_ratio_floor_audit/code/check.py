"""Exact directed ratio floors from rational squares; no floating arithmetic."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from decimal import Decimal
from math import isqrt
import json,hashlib,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads((B/p).read_text());checks=[]
def ck(s,b,value=None):
 assert bool(b),(s,value);checks.append({'claim':s,'value':str(value) if value is not None else None})
def unit(s):return Q(10)**Decimal(s).as_tuple().exponent
def rows_after(text,heading):
 part=text.split(heading,1)[1];out=[];started=False
 for ln in part.splitlines():
  line=ln.strip()
  if line.startswith('|---'):started=True;continue
  if started and line.startswith('|'):out.append([x.strip() for x in line.strip('|').split('|')])
  elif started:break
 return out
m=read('data/manifest.json');ck('proof first',m['proof_written_before_checker'])
for p,h in m['inputs'].items():ck('input '+p,sha(B/p)==h)
for r in read('data/input_sources.json')['inputs']:ck('frozen '+r['local'],sha(B/r['local'])==r['sha256'])
p=read('data/parameters.json');pr=read('source/T2_result.json');br=read('source/brackets_result.json')
ck('accepted exact brackets',br['check_count']==166 and br['proof_sha256']==sha(B/'source/brackets_PROOF.md'))
ck('peer clean finite report',pr['checks']==67 and pr['fails']==[])
sq={r['name']:Q(r['supremum_square_exact']) for r in br['rows']};sq['graded']=Q(br['graded']['square_exact'])
bindings=[]
for name,f in [('c1-t2/notes/T2_FINAL_SUMMARY.md','T2_summary.md'),('c1-t2/handoff/T2_to_T1_v01.md','T2_handoff.md'),('c1-t2/reviews/REVIEW_T4ALT.md','T2_ALT.md'),('c1-t2/artifacts/data/family_ceilings_exact_results.json','T2_brackets.json')]:
 a=pr['inputs'][name];b=sha(B/'source'/f);bindings.append({'source':name,'historical_sha256':a,'frozen_sha256':b,'match':a==b})
 if f in ['T2_ALT.md','T2_brackets.json']:ck('immutable peer input '+f,a==b)
summary=(B/'source/T2_summary.md').read_text();srows=rows_after(summary,'| candidate | fixed-c L2 distance > | source |');ck('five summary rows',[r[0].split()[0] for r in srows]==['007','005','008','d2','Mpen2']);out={};corrected=[]
for r in srows:
 name=r[0].split()[0];d=Q(r[1].split()[0]);ck(name+' positive distance',d>0)
 for f,k in zip(r[3:6],['TB-sharp','sharpw','graded']):
  budget=Q(p['summary_budgets'][k]);u=unit(f);ratio=d/budget;n=(ratio/u).__floor__();fl=n*u
  ck(k+' printed budget upper',budget*budget>sq[k]);ck(name+' '+k+' exact floor',fl<=ratio<fl+u)
  ck(name+' '+k+' printed is floor',Q(f)==fl);ck(name+' '+k+' exclusion',fl>1)
  peer=pr['summary_section5'][name+' / '+k];ck(name+' '+k+' peer agreement',Q(peer['floor'])==fl and peer['printed_is_lower_bound'])
  out[name+' / '+k]={'floor_exact':str(fl),'ratio_exact':str(ratio),'unit_exact':str(u),'printed':f}
ck('old d2 summary value not lower',Q('1.04e5')>Q('0.29552675')/Q('2.8496e-6'))
for title,fn,heading,key in [('handoff O3','T2_handoff.md','| family | L2 budget | d2 T4-048 (0.0029920) |','distances_O3'),('REVIEW_T4ALT C4','T2_ALT.md','| framework | L2 budget | d2 (0.29552675) |','distances_C4')]:
 rows=rows_after((B/'source'/fn).read_text(),heading);ck(title+' six rows',len(rows)==6);bad=0
 for r,k in zip(rows,p['families']):
  for ds,f in zip(p[key],r[2:]):
   d=Q(ds);u=unit(f);t=d*d/(sq[k]*u*u);n=isqrt(t.numerator//t.denominator);fl=n*u;lower=Q(f)**2*sq[k]<=d*d
   ck(title+' '+k+' '+ds+' exact squared floor',Q(n*n)<=t<Q((n+1)**2));ck(title+' '+k+' '+ds+' exclusion',fl>1)
   peer=pr[title][ds+' / '+k];ck(title+' '+k+' '+ds+' peer floor',Q(peer['floor'])==fl and peer['printed_is_lower_bound']==lower)
   if not lower:
    bad+=1;ck(title+' '+k+' '+ds+' one unit to floor',Q(f)-fl==u)
   corrected.append({'table':title,'family':k,'distance_exact':str(d),'printed':f,'unit_exact':str(u),'square_scaled_ratio_exact':str(t),'integer_floor':n,'floor_exact':str(fl),'printed_is_lower_bound':lower})
 ck(title+' expected defect count',bad==pr[title+' not lower bounds']==(13 if title=='handoff O3' else 8))
q=Q('0.29552675')**2/sq['graded'];ck('O5 647 is above certified quotient',Q(647**2)>q>Q(646**2),q)
for z,h in m['inputs'].items():ck('unchanged '+z,sha(B/z)==h)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'summary_rows':out,'historical_rows':corrected,'historical_input_bindings':bindings,'historical_defects':{'O3':13,'C4':8},'additional_prose_caution':'O5 at least647 is not justified by the certified d2 floor divided by exact graded supremum; the quotient lies between646 and647. This does not refute a stronger actual PDE distance bound.','proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'foreign_code_executed':False,'spatial_integrals_repeated':False,'verdict':'CONFIRMED exact floors and T2 defect counts; REFUTED lower-factor interpretation of21historical entries, stronger actual-distance bound OPEN; exclusions unchanged'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print('PASS',len(checks),r['utc'],r['elapsed_seconds']);print('Historical entries:',len(corrected),'Defects:',r['historical_defects'])
for z in corrected:
 if not z['printed_is_lower_bound']:print(z['table'],z['family'],z['distance_exact'],z['printed'],'->',z['floor_exact'])

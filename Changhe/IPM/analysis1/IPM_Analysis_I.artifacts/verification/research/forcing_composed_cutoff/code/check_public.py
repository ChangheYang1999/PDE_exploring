"""Exact comparison of all current table ceilings against frozen JSON endpoints."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import re,json,hashlib,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1]
p=D/'source/NUM_REPORT_7_10.md';text=p.read_text();v21=json.loads((D/'source/runs/forcing/v21_p9_merged.json').read_text());v11=json.loads((D/'source/runs/forcing/v11_p9_merged.json').read_text());number=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?';checks=[]
normlines=[l for l in text.splitlines() if l.startswith('| ||tau eps~||') or l.startswith('| N_500')];assert len(normlines)==6
for l,lam,key in zip(normlines,['1.0']*3+['500.0']*3,['bound_order3','bound_order4','bound_order_3_1']*2):
 fields=l.split(' | ');assert len(fields)==4
 for version,v,col in [('v21',v21,1),('v11',v11,2)]:
  s=fields[col].replace('*','').strip();assert re.fullmatch(number,s);q=Q(s);z=Q.from_float(v['results'][lam][key]);assert q>=z
  checks.append({'label':version+':'+lam+':'+key,'display':s,'saved_exact':str(z),'margin':str(q-z)})
rows=[l for l in text.splitlines() if re.match(r'^\| \([0-4],[0-4]\)',l)];assert len(rows)==5
for order,l in enumerate(rows):
 fields=l.split('|');keys=re.findall(r'\(([0-4]),([0-4])\)',fields[1]);assert len(keys)==order+1 and all(int(a)+int(b)==order for a,b in keys)
 for ball,col in [('B94',fields[2]),('B3',fields[3])]:
  vals=[v.strip() for v in re.sub(r'\([^)]*\)','',col).strip().split(',')];assert len(vals)==len(keys)
  for (a,b),s in zip(keys,vals):
   assert re.fullmatch(number,s);key=a+'_'+b;z=Q.from_float(v21['sup_D_eps'][ball][key]);assert v21['sup_D_eps'][ball][key]==v11['sup_D_eps'][ball][key];q=Q(s);assert q>=z
   checks.append({'label':ball+':'+key,'display':s,'saved_exact':str(z),'margin':str(q-z)})
assert len(checks)==42
grads={}
for ball,s in [('B94','6.816e-5'),('B3','9.889e-5')]:
 assert s in text;g=v21['sup_D_eps'][ball];q2=sum(Q.from_float(g[k])**2 for k in ['1_0','0_1']);assert q2<Q(s)**2
 grads[ball]={'ceiling':s,'squared_exact':str(q2),'squared_margin':str(Q(s)**2-q2)}
con=[]
for a,b,c in [('0.3181','1.5700','0.4995'),('473','3.5769','1691.9')]:
 assert a+' x '+b+' < '+c in text;assert Q(a)*Q(b)<Q(c);con.append({'factors':[a,b],'ceiling':c,'margin':str(Q(c)-Q(a)*Q(b))})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_REPAIRED_PUBLIC_UPWARD_DISPLAYS','report_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'table_count':len(checks),'checks':checks,'gradient_squared_tests':grads,'scalar_products':con,'scope':'Upward display of saved outputs and conditional scalar products; physical forcing and global inverse remain OPEN.'}
(D/'evidence/public.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(checks))

"""Check every changed decimal and the full primary table in report version 33."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v33'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ceil(q,n):
 t=q*10**n;k=-((-t.numerator)//t.denominator);return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
 hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 def accept(rel,v):
  p=R/rel;d=json.loads(p.read_text());assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
  for name,h in d['sha256'].items():assert sha(R/name)==h,name
  return d
 cross=accept('05_team_audit/cross4096/recombination/verification/accepted.json','V219')
 radial=accept('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/cross4096_values/accepted.json','V220')
 prev=R/'05_team_audit/report_v32/table_v209_v210.json';table=json.loads(prev.read_text());bind(prev)
 report=B/'FINAL_REPORT.md';text=report.read_text();assert 'Draft version 33,' in text
 dr={Q(x['alpha']):x for x in radial['rows']};rows=[]
 for r in table['rows']:
  a=Q(r['alpha']);line=next(x for x in text.splitlines() if x.startswith('| '+str(float(a))+' |'))
  c=[x.strip() for x in line.split('|')[1:-1]]
  uc=Q(r['selected_upper_C']['exact_safe_endpoint']);ud=min(Q(r['selected_upper_D']['exact_safe_endpoint']),Q(dr[a]['safe_upper_D']))
  lc=Q(r['selected_lower']['exact_safe_endpoint']);ld=Q(r['selected_lower_D']['exact_safe_endpoint'])
  assert c[4]==ceil(uc,6) and c[5]==ceil(ud,6),(a,c)
  assert Q(c[6])<=lc and Q(c[8].strip('*'))<=ld
  assert Q(c[9])>=uc/lc and Q(c[10])>=ud/ld
  assert Q(c[9])-Q(ceil(uc/lc,4))<=Q(1,10000)
  assert Q(c[10])-Q(ceil(ud/ld,4))<=Q(1,10000)
  rows.append(dict(alpha=str(a),upper_C=c[4],upper_D=c[5],ratio_C=c[9],ratio_D=c[10]))
 for r in cross['rows']:assert r['safe_upper_D'] in text
 for r in radial['rows']:
  if Q(r['alpha'])>=Q(1,20):assert r['safe_upper_D'] in text
 for a,s in [(Q(1,20),'2.62e-5'),(Q(1,10),'4.96e-5'),(Q(1,5),'8.81e-5'),(Q(3,10),'1.15e-4'),(Q(1,2),'1.37e-4'),(Q(3,4),'1.02e-4'),(Q(9,10),'4.92e-5'),(Q(99,100),'5.41e-6')]:assert Q(s)<=Q(dr[a]['gain_lower'])
 assert 'gives more at the listed exponents' in text
 assert '$2.453123\\le D_{1/2}\\le2.645105$' in text
 for p in [report,B/'PROOF.md',B/'lead_diff.txt',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V227',verdict='CONFIRMED',rows=rows,sha256=hashes,scope='All version33 changes and complete primary table; prior accepted theorem audits retained')
 (B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V227 all checks passed')
if __name__=='__main__':main()

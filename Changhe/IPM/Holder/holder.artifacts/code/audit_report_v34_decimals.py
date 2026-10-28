"""Exact endpoint checks for every changed numerical bound in report v34."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v34'
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
 accept('05_team_audit/report_v33/accepted.json','V227')
 tail=accept('08_improved_upper_bounds/explicit_second_term/tail_series/numerical_values/accepted.json','V225')
 radial=accept('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/numerical_values/accepted.json','V226')
 old=accept('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/cross4096_values/accepted.json','V220')
 table_path=B/'table_v225_v226.json';table=json.loads(table_path.read_text());bind(table_path)
 report=B/'FINAL_REPORT.md';text=report.read_text();assert 'Draft version 34,' in text
 rows=[]
 for r in table['rows']:
  a=Q(r['alpha']);line=next(x for x in text.splitlines() if x.startswith('| '+str(float(a))+' |'))
  cells=[x.strip() for x in line.split('|')[1:-1]]
  uc,ud,lc,ld=(Q(r[k]['exact_safe_endpoint']) for k in ['selected_upper_C','selected_upper_D','selected_lower','selected_lower_D'])
  assert cells[4]==ceil(uc,6) and cells[5]==ceil(ud,6),(a,cells)
  assert Q(cells[6])<=lc and Q(cells[8].strip('*'))<=ld
  assert Q(cells[9])>=uc/lc and Q(cells[10])>=ud/ld
  assert Q(cells[9])-Q(ceil(uc/lc,4))<=Q(1,10000)
  assert Q(cells[10])-Q(ceil(ud/ld,4))<=Q(1,10000)
  rows.append(dict(alpha=str(a),upper_C=cells[4],upper_D=cells[5],ratio_C=cells[9],ratio_D=cells[10]))
 for value in ['637.0245603580','637.4271355465','127.7386138886','128.1421848905','64.0890268187','64.4938379166','2.4754617576','2.7251476744']:
  assert value in text and any(x.get('safe_upper')==value for x in tail['rows']),value
 for r in radial['rows']:assert r['safe_upper'] in text,r
 rr={Q(x['alpha_or_epsilon']):x for x in radial['rows'] if x['kind']=='unperturbed'}
 oo={Q(x['alpha']):x for x in old['rows']}
 for a,new,prior in [(Q(1,20),'2.94e-5','2.62e-5'),(Q(1,10),'5.56e-5','4.96e-5'),(Q(1,5),'9.88e-5','8.81e-5'),(Q(3,10),'1.29e-4','1.15e-4'),(Q(1,2),'1.53e-4','1.37e-4'),(Q(3,4),'1.15e-4','1.02e-4'),(Q(9,10),'5.51e-5','4.92e-5'),(Q(99,100),'6.06e-6','5.41e-6')]:
  assert Q(new)<=Q(rr[a]['gain_lower']) and Q(prior)<=Q(oo[a]['gain_lower']),a
 assert '$2.453123\\le D_{1/2}\\le2.645088$' in text
 assert 'the calibration is assumed, not established' in text
 for p in [report,B/'PROOF.md',B/'changes.diff',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V229',verdict='CONFIRMED',rows=rows,sha256=hashes,scope='All version34 changes and complete primary table; preceding accepted theorem audits retained')
 (B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V229 all checks passed')
if __name__=='__main__':main()

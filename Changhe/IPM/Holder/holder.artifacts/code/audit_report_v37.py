"""Audit report37 against exact accepted upper and lower certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v37'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ceil(q,n):
 t=q*10**n;k=-((-t.numerator)//t.denominator);return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);args=ap.parse_args();hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 def accept(p,v):
  d=json.loads(p.read_text());assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
  for n,h in d['sha256'].items():assert sha(R/n)==h,n
  return d
 accept(R/'05_team_audit/report_v36/accepted.json','V238')
 root=R/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density'
 accept(root/'supplemental_disks/verification/accepted.json','V234')
 upper=accept(root/'supplemental_disks/numerical_values/accepted.json','V235')
 previous=accept(root/'numerical_values/accepted.json','V231')
 lower=accept(R/'05_team_audit/note14_certificate/producer_fine_a75/quadratic_recombination/accepted.json','V237')
 p=R/'05_team_audit/report_v34/table_v225_v226.json';tab=json.loads(p.read_text());bind(p)
 p=B/'FINAL_REPORT.md';text=p.read_text();assert 'Draft version 37,' in text
 vals={Q(r['alpha_or_epsilon']):Q(r['safe_upper']) for r in upper['rows'] if r['mode']=='finite'};rows=[]
 for r in tab['rows']:
  a=Q(r['alpha']);line=next(x for x in text.splitlines() if x.startswith('| '+str(float(a))+' |'));cells=[x.strip() for x in line.split('|')[1:-1]]
  uc,ud,lc,ld=(Q(r[k]['exact_safe_endpoint']) for k in ['selected_upper_C','selected_upper_D','selected_lower','selected_lower_D'])
  ud=min(ud,vals.get(a,ud))
  if a==Q(3,4):ld=Q(lower['safe_D_lower'])
  assert cells[4]==ceil(uc,6) and cells[5]==ceil(ud,6),(a,cells)
  assert Q(cells[6])<=lc and Q(cells[8].strip('*'))<=ld
  assert Q(cells[9])>=uc/lc and Q(cells[10])>=ud/ld
  assert Q(cells[9])-Q(ceil(uc/lc,4))<=Q(1,10000) and Q(cells[10])-Q(ceil(ud/ld,4))<=Q(1,10000)
  rows.append(dict(alpha=str(a),upper_C=cells[4],upper_D=cells[5],lower_D=cells[8].strip('*'),ratio_D=cells[10]))
 for r in upper['rows']:assert r['safe_upper'] in text,r
 gains={Q(r['alpha_or_epsilon']):Q(r['gain_lower']) for r in previous['rows'] if r['kind']=='unperturbed'}
 for r in upper['rows']:
  if r['kind']=='unperturbed':gains[Q(r['alpha_or_epsilon'])]+=Q(r['gain_lower'])
 for a,g in [('1/20','3.12e-5'),('1/10','5.92e-5'),('1/5','1.05e-4'),('3/10','1.37e-4'),('1/2','1.63e-4'),('3/4','1.22e-4'),('9/10','5.87e-5'),('99/100','6.45e-6')]:assert Q(g)<=gains[Q(a)],(a,g)
 p=R/'05_team_audit/note14_certificate/producer_fine_a75/quadratic_recombination/independent_audit.json';d=json.loads(p.read_text());bind(p)
 assert d['task_count']==3961 and d['cells']==59232568 and d['selected']['epsilon']=='8292312018375231/5000000000000000000'
 assert Q('2.3948343')<=Q(d['selected']['I0']['lower'])<=Q(d['selected']['I0']['upper'])<=Q('2.3977111')
 assert lower['selected_task_replays']==70 and lower['selected_cells']==2396908
 assert Q('2.8943')<Q(lower['safe_D_lower'])
 for fragment in ['2.8948343532','2.3948343,2.3977111','2396908','it is not a complete independent replay of all cells','the calibration is assumed, not established','the two savings are alternatives and are not added','P_i(t)=c_i^2-a_i^2-4c_it+4t^2+4c_it^3-4t^4','2sa_i<1','2.453123\\le D_{1/2}\\le2.645079']:
  assert fragment in text,fragment
 for p in [B/'FINAL_REPORT.md',B/'PROOF.md',B/'changes.diff',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',sha256=hashes,rows=rows,scope='Complete version37 change audit: Theorem3.10(d), V235 upper values, V237 lower value and partial replay scope, exact table rounding and ratios, and all changed consequences')
 (B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],args.ledger,'all checks passed')
if __name__=='__main__':main()

"""Check all version35 numerical changes against accepted exact endpoints."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v35'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ceil(q,n):
 t=q*10**n;k=-((-t.numerator)//t.denominator);return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
 hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 def accept(p,v):
  d=json.loads(p.read_text());assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
  for n,h in d['sha256'].items():assert sha(R/n)==h,n
  return d
 accept(R/'05_team_audit/report_v34/accepted.json','V229')
 new=accept(R/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/numerical_values/accepted.json','V231')
 tp=R/'05_team_audit/report_v34/table_v225_v226.json';tab=json.loads(tp.read_text());bind(tp)
 report=B/'FINAL_REPORT.md';text=report.read_text();assert 'Draft version 35,' in text
 vals={Q(r['alpha_or_epsilon']):Q(r['safe_upper']) for r in new['rows'] if r['mode']=='finite'};rows=[]
 for r in tab['rows']:
  a=Q(r['alpha']);line=next(x for x in text.splitlines() if x.startswith('| '+str(float(a))+' |'));cells=[x.strip() for x in line.split('|')[1:-1]]
  uc,ud,lc,ld=(Q(r[k]['exact_safe_endpoint']) for k in ['selected_upper_C','selected_upper_D','selected_lower','selected_lower_D'])
  ud=min(ud,vals.get(a,ud));assert cells[4]==ceil(uc,6) and cells[5]==ceil(ud,6),(a,cells)
  assert Q(cells[6])<=lc and Q(cells[8].strip('*'))<=ld
  assert Q(cells[9])>=uc/lc and Q(cells[10])>=ud/ld
  assert Q(cells[9])-Q(ceil(uc/lc,4))<=Q(1,10000) and Q(cells[10])-Q(ceil(ud/ld,4))<=Q(1,10000)
  rows.append(dict(alpha=str(a),upper_C=cells[4],upper_D=cells[5],ratio_C=cells[9],ratio_D=cells[10]))
 for r in new['rows']:assert r['safe_upper'] in text,r
 gains={Q(r['alpha_or_epsilon']):Q(r['gain_lower']) for r in new['rows'] if r['kind']=='unperturbed'}
 for a,g in [('1/20','3.01e-5'),('1/10','5.71e-5'),('1/5','1.01e-4'),('3/10','1.33e-4'),('1/2','1.58e-4'),('3/4','1.18e-4'),('9/10','5.66e-5'),('99/100','6.23e-6')]:assert Q(g)<=gains[Q(a)]
 assert '$2.453123\\le D_{1/2}\\le2.645084$' in text
 assert 'the calibration is assumed, not established' in text
 for p in [report,B/'PROOF.md',B/'changes.diff',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V236',verdict='CONFIRMED',rows=rows,sha256=hashes,scope='All version35 changes, including Theorem3.10(c), complete primary upper table and ratio claims')
 (B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V236 all checks passed')
if __name__=='__main__':main()

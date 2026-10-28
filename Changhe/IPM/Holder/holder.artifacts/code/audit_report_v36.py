"""Audit report36 changes, exact table rounding and directed excess claims."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v36'
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
 accept(R/'05_team_audit/report_v35/accepted.json','V236')
 lower=accept(R/'05_team_audit/note14_certificate/replay_fine_a75/full_quadratic/accepted.json','V233')
 upper=accept(R/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/numerical_values/accepted.json','V231')
 p=R/'05_team_audit/report_v34/table_v225_v226.json';tab=json.loads(p.read_text());bind(p)
 p=B/'FINAL_REPORT.md';text=p.read_text();assert 'Draft version 36,' in text
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
  if a==Q(1,1000):csmall=uc
 auditp=R/'05_team_audit/note14_certificate/replay_fine_a75/full_quadratic/independent_audit.json';d=json.loads(auditp.read_text());bind(auditp)
 assert d['task_count']==1220 and d['cells']==27946926 and d['selected']['epsilon']=='1/100'
 assert Q('2.3938332')<=Q(d['selected']['I0']['lower'])<=Q(d['selected']['I0']['upper'])<=Q('2.3987032')
 assert Q('2.8943')-Q(lower['safe_D_lower'])<Q(1,1000)
 ctx.prec=320;excess=arb(str(csmall))-2000/arb.pi();assert excess<arb('0.4048')
 for fragment in ['2.8938332593','2.3938332,2.3987032','the calibration is assumed, not established','K_C=\\frac{\\ell_C^2+\\frac14}\\pi+Z+B_C(\\rho)+E(\\rho)L(\\rho)','S(\\varepsilon)\\le S^+_{64}(\\varepsilon)','the two savings are alternatives and are not added']:
  assert fragment in text,fragment
 for p in [B/'FINAL_REPORT.md',B/'PROOF.md',B/'changes.diff',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V238',verdict='CONFIRMED',sha256=hashes,rows=rows,C_excess_at_one_thousandth=excess.str(40),scope='Complete version36 change audit, including V233 lower endpoint, table rounding, explicit Taylor constants, normalization clarifications, and heuristic wording')
 (B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V238 all checks passed')
if __name__=='__main__':main()

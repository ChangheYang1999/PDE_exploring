"""Audit the frozen version38 report against accepted exact certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json,re
from flint import arb,ctx
R=Path(__file__).resolve().parents[1]; B=R/'05_team_audit/report_v38'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dec(q,n,up):
 t=q*10**n;k=-((-t.numerator)//t.denominator) if up else t.numerator//t.denominator
 return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
 hashes={}
 def bind(p): hashes[str(p.relative_to(R))]=sha(p)
 def accept(path,ledger):
  p=R/path;d=json.loads(p.read_text());assert d['ledger']==ledger and d['verdict']=='CONFIRMED';bind(p);return d
 accept('05_team_audit/report_v37/accepted.json','V240')
 old=accept('05_team_audit/final_integrity/accepted.json','V241')
 lower=accept('05_team_audit/note14_certificate/producer_fine_a50/quadratic_recombination/accepted.json','V239')
 p=B/'table_snapshot.json';tab=json.loads(p.read_text());bind(p)
 assert sha(p)==sha(R/'data/verified_table.json')
 assert sha(p)==sha(R/'05_team_audit/final_integrity/table_snapshot.json')
 text=(B/'FINAL_REPORT.md').read_text();assert 'Draft version 38, 2026-10-28T14:58Z.' in text
 rows=[];ratios=[];gaps=[]
 for r in tab['rows']:
  a=Q(r['alpha']);line=next(x for x in text.splitlines() if x.startswith('| '+str(float(a))+' |'))
  cells=[x.strip().strip('*') for x in line.split('|')[1:-1]]
  uc,ud,lc,ld=(Q(r[k]['exact_safe_endpoint']) for k in ['selected_upper_C','selected_upper_D','selected_lower','selected_lower_D'])
  for i,q,up in [(4,uc,True),(5,ud,True),(6,lc,False),(8,ld,False)]:assert cells[i]==dec(q,6,up),(a,i,cells[i])
  cr=dec(Q(cells[4])/Q(cells[6]),4,True);dr=dec(Q(cells[5])/Q(cells[8]),4,True)
  assert cells[9]==cr and cells[10]==dr,(a,cells[9:],cr,dr)
  gap=dec(ld-uc,4,False);gaps.append(gap);ratios.append(dr)
  rows.append(dict(alpha=str(a),upper_C=cells[4],upper_D=cells[5],lower_C=cells[6],lower_D=cells[8],ratio_C=cr,ratio_D=dr,gap=gap))
 assert ', '.join(ratios[:-1])+' and '+ratios[-1] in text
 assert '$'+gaps[0]+'$' in text
 for gap in gaps:assert '$'+gap+'$' in text,gap
 assert lower['task_count']==4019 and lower['cells']==24900260
 assert lower['selected_task_replays']==52 and lower['selected_cells']==1129918
 assert Q('0.0099201')<=Q(lower['epsilon'])<Q('0.0099202')
 p=R/'05_team_audit/note14_certificate/producer_fine_a50/quadratic_recombination/independent_audit.json'
 d=json.loads(p.read_text());bind(p);i=d['selected']['I0'];lo=Q(i['lower']);hi=Q(i['upper'])
 assert Q('1.9542144')<=lo<=hi<=Q('1.9586939')
 assert Q('2.4542')<=lo+Q(1,2)<=hi+Q(1,2)<=Q('2.4587')
 assert Q(lower['safe_D_lower'])<=lo+Q(1,2)
 p=B/'local_circle_composite_a50.json';local=json.loads(p.read_text());bind(p)
 def balls(o):
  if isinstance(o,str) and o.startswith('[') and '+/-' in o:yield o
  elif isinstance(o,dict):
   for v in o.values():yield from balls(v)
  elif isinstance(o,list):
   for v in o:yield from balls(v)
 ctx.prec=256;values=list(balls(local))
 phase=next(arb(v) for v in values if v.startswith('[2.043011603939'))
 small=next(arb(v) for v in values if v.startswith('[0.151542482124'))
 assert phase<arb('2.04301160395') and small<arb('0.15154248213')
 combined=arb('2.04301160395')/(arb.pi()/64).cos()+arb('0.15154248213')
 assert combined<arb('2.1970179509')
 for frag in [r'flow may pass through cells with $m_j=0$',r'physical density is $R^{-2}$',r'opposite-sign pairs (points in adjacent quadrants',r'2.4542144708',r'1.9542144,1.9586939',r'1129918',r'it is not a complete independent replay of all cells',r'2.454214\le D_{1/2}\le2.645079',r'[2.4542,2.4587]']:
  assert frag in text,frag
 assert '1.0783' not in text and '$0.2597$' not in text and '$0.2483$' not in text
 for p in [B/'FINAL_REPORT.md',B/'PROOF.md',B/'changes.diff',R/'13_transport_duality/finite_flow_lifting/PROOF.md',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V243',verdict='CONFIRMED',sha256=hashes,rows=rows,refined_intermediate_combination=str(combined),scope='Complete version38 difference audit, zero-mass flow lifting, coordinate normalization, profile sign labels, exact table and consequences; no new fine-mesh replay')
 (B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V243 all checks passed')
if __name__=='__main__':main()

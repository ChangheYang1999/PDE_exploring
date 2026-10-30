"""Independent finite decimal/text audit; no publisher imports or PDE certification."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_v14_review'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();mf=json.loads((B/'source/MANIFEST.json').read_text());inputs={}
 for e in mf['files'].values():
  p=R/e['path'];assert sha(p)==e['sha256'];inputs[e['path']]=e['sha256']
 assert not mf['checker_exists'] and sha(B/'PROOF.md')==mf['proof_sha256']
 for p in [B/'PROOF.md',B/'source/MANIFEST.json',Path(__file__),B/'code/freeze.py']:inputs[str(p.relative_to(R))]=sha(p)
 def load(name,dec=False):return json.loads((R/mf['files'][name]['path']).read_text(),parse_float=Decimal if dec else float)
 text=(R/mf['files']['publication']['path']).read_text();data={n:load(n,True) for n in ['016','022','023','024','025','026','027','028']}
 def value(c,p):return data[c]['probes'][f'{p[0]}:{p[1]}']['m_lower_bound']
 def fmt(x,form):return format(float(x),form)
 reg=[(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]]
 blocks=re.findall(r'^\| probe \(n, K\).*?(?=^Largest held-out value)',text,re.M|re.S)
 tables={};checks={};issues=[];printed=[];countchecks=[]
 for block in blocks:
  labels=[s.strip() for s in block.splitlines()[0].split('|')[1:-1]][2:];c=labels[-1];rows=[]
  for line in block.splitlines()[2:]:
   if not line.startswith('| ('):continue
   cells=[s.strip() for s in line.split('|')[1:-1]];p=tuple(map(int,re.match(r'\((\d+), (\d+)\)',cells[0]).groups()));rows.append(p)
   for label,display in zip(labels,cells[2:],strict=True):
    raw=value(label,p);good=fmt(raw,'.2e')==display;printed.append({'table':c,'candidate':label,'n':p[0],'K':p[1],'display':display,'source_decimal':str(raw),'pass':good})
   held=('HELD IN' in cells[0]);expected=c in ['025','026'] and p[0] in range(19,32,2) and p[1]-(p[0]-1)//2 in [128,512]
   countchecks.append({'table':c,'n':p[0],'K':p[1],'held_in_label':held,'expected':expected,'pass':held==expected})
  assert len(rows)==50 and len(set(rows))==50 and rows[:25]==reg
  tables[c]={'candidates':labels,'probes':rows}
 checks['all_five_tables']=set(tables)==set(['024','025','026','027','028'])
 checks['all1000_displayed_values']=len(printed)==1000 and all(x['pass'] for x in printed)
 checks['all250_held_in_labels']=len(countchecks)==250 and all(x['pass'] for x in countchecks)
 comps={};ratio_checks=[]
 for new,old in [('027','022'),('027','026'),('028','022'),('028','027'),('028','016')]:
  line=next(x for x in text.splitlines() if x.startswith(f'- {new} vs {old} '));lead,summary=line.split(' Counts and factors:',1)
  groups=re.findall(r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)',lead)
  assert len(groups)==25
  rows=[]
  for ns,ks,ov,nv,rf in groups:
   p=(int(ns),int(ks));a,b=Q(value(old,p)),Q(value(new,p));q=b/a
   row={'n':p[0],'K':p[1],'old_decimal':str(value(old,p)),'new_decimal':str(value(new,p)),'ratio_exact':str(q),'ratio_FLOAT_decimal_approx':float(q),'sign':(q>1)-(q<1),'displayed_sign':(Q(nv)>Q(ov))-(Q(nv)<Q(ov))}
   rows.append(row);ratio_checks.append({'comparison':f'{new}/{old}','n':p[0],'K':p[1],'old_display':ov,'new_display':nv,'factor_display':rf,'pass':fmt(a,'.2e')==ov and fmt(b,'.2e')==nv and fmt(q,'.2f')==rf})
  assert [(r['n'],r['K']) for r in rows]==reg
  dec=sum(r['sign']<0 for r in rows);inc=sum(r['sign']>0 for r in rows);low=min(rows,key=lambda r:Q(r['ratio_exact']));high=max(rows,key=lambda r:Q(r['ratio_exact']))
  m=re.search(r'decreases (\d+), increases (\d+); min factor ([0-9.]+) at \((\d+), (\d+)\), max ([0-9.]+) at \((\d+), (\d+)\)',summary);assert m
  dc,ic,mn,mi,mk,mx,ma,mb=m.groups();summaryok=int(dc)==dec and int(ic)==inc and mn==fmt(Q(low['ratio_exact']),'.4f') and mx==fmt(Q(high['ratio_exact']),'.4f') and (int(mi),int(mk))==(low['n'],low['K']) and (int(ma),int(mb))==(high['n'],high['K'])
  large=re.findall(r'\((\d+), (\d+)\) ([0-9.]+)',summary.split('K >= 1800 factors:',1)[1]);assert len(large)==10
  largechecks=[]
  for n,k,v in large:
   r=next(r for r in rows if (r['n'],r['K'])==(int(n),int(k)));assert int(k)>=1800
   largechecks.append({'n':int(n),'K':int(k),'printed':v,'pass':fmt(Q(r['ratio_exact']),'.4f')==v})
  comps[f'{new}/{old}']={'rows':rows,'counts_decrease_equal_increase':[dec,25-dec-inc,inc],'displayed_counts_decrease_equal_increase':[sum(r['displayed_sign']==s for r in rows) for s in [-1,0,1]],'minimum':low,'maximum':high,'summary_pass':summaryok,'largeK_checks':largechecks}
 checks['all125_new_ratio_displays']=len(ratio_checks)==125 and all(r['pass'] for r in ratio_checks)
 checks['all_five_ratio_summaries']=all(c['summary_pass'] for c in comps.values())
 checks['all50_largeK_factors']=all(r['pass'] for c in comps.values() for r in c['largeK_checks'])
 band={}
 c=comps['027/022'];lo=Q(c['minimum']['ratio_exact']);hi=Q(c['maximum']['ratio_exact'])
 for name,a,b in [('literal',Q('.826'),Q('1.343')),('stored_decimal_extrema',lo,hi)]:
  rec={}
  for label,pred in [('K_le1200',lambda r:r['K']<=1200),('K_ge1800',lambda r:r['K']>=1800)]:
   rr=[r for r in comps['028/027']['rows'] if pred(r)];outside=[{'n':r['n'],'K':r['K'],'ratio_exact':r['ratio_exact'],'direction':'below' if Q(r['ratio_exact'])<a else 'above'} for r in rr if Q(r['ratio_exact'])<a or Q(r['ratio_exact'])>b]
   rec[label]={'total':len(rr),'outside_count':len(outside),'outside':outside}
  band[name]={'lower':str(a),'upper':str(b),'subsets':rec}
 checks['H18_eleven_small_one_large_both_bands']=all(r['subsets']['K_le1200']['outside_count']==11 and r['subsets']['K_ge1800']['outside_count']==1 and [(x['n'],x['K']) for x in r['subsets']['K_ge1800']['outside']]==[(31,1800)] for r in band.values())
 held={}
 for n in ['025','026']:
  rows=[]
  for mode in range(19,32,2):
   for base in [128,512]:
    K=base+(mode-1)//2;x=data[n]['probes'][f'{mode}:{K}'];rows.append({'n':mode,'K':K,'I_signed_mesh_decimal':str(x['I_signed_mesh']),'m_proxy_decimal':str(x['m_lower_bound'])})
  held[n]={'rows':rows,'abs_I_min':str(min(abs(Q(r['I_signed_mesh_decimal'])) for r in rows)),'abs_I_max':str(max(abs(Q(r['I_signed_mesh_decimal'])) for r in rows)),'m_min':str(min(Q(r['m_proxy_decimal']) for r in rows)),'m_max':str(max(Q(r['m_proxy_decimal']) for r in rows))}
 pub=datetime.fromisoformat('2026-10-29T14:44:45+00:00');accepted={e['number']:Q(e['accepted_floor']) for e in load('accepted_distances')['entries']};floorline=next(l for l in text.splitlines() if 'Certified floors (CONFIRMED)' in l);floors=[]
 for n,f in re.findall(r'(0\d\d) > ([0-9.]+)',floorline):floors.append({'candidate':n,'display':f,'accepted_floor':str(accepted[int(n)]),'pass':Q(f)<=accepted[int(n)]})
 checks['six_short_distance_floors_conservative']=len(floors)==6 and all(x['pass'] for x in floors)
 checks['024_actual_middle_order32']=load('N4_024_holdout.json')['comparison_parameters']['middle_order024']==32
 checks['026_actual81rows']=len(load('N4_026_holdout.json')['exact_objective_rows'])==81
 checks['016_cells_complete_before_publication']=datetime.fromisoformat(load('N4_016_cells.json')['utc'])<pub
 checks['015_cells_complete_before_publication']=datetime.fromisoformat(load('015_cells')['utc'])<pub
 checks['025_audits_complete_before_publication']=all(datetime.fromisoformat(load(n)['utc'])<pub for n in ['N4_025_holdout.json','N4_025_shape_peer.json','N4_025_weak.json'])
 lines=text.splitlines()
 for key,term,verdict in [('wrong024MIDsummary','LOSS = last accepted objective on the MID 16 rule','REFUTED'),('wrong024MIDstep','024: 5 accepted steps','REFUTED'),('missing026rowexception','021 and 025 use 81 rows','REFUTED'),('unsupported_endpoint_certificate',"a certified bound is c1-n4's",'OPEN'),('stale016cells','CLAIMED pending c1-n4','REFUTED'),('rawI_vs_m','pairing rows at weight 1e16 (025, 026) are satisfied','REFUTED'),('overbroad_product_unavailability','two-scale product keys for 020 to 028 are not available','REFUTED')]:
  hits=[{'line':i+1,'text':l} for i,l in enumerate(lines) if term in l];assert hits;issues.append({'issue':key,'verdict':verdict,'locations':hits})
 optimizer_lines=[l for l in lines if l.startswith('Optimizer report (MID ')];checks['five_complete_optimizer_report_lines']=len(optimizer_lines)==5 and all(re.fullmatch(r'Optimizer report \(MID (?:16|32)\): P2 [0-9.e+\-]+ G1 [0-9.e+\-]+ G0 [0-9.e+\-]+ rF [0-9.e+\-]+ supF [0-9.e+\-]+',l) for l in optimizer_lines)
 weak=(R/mf['files']['N1_weak_tests3.py']['path']).read_text();opt=(R/mf['files']['N1_ipm_opt3.py']['path']).read_text();run=(R/mf['files']['N1_run_quot.py']['path']).read_text()
 checks['distinct_I_and_m']=all(t in weak for t in ["'I_signed_mesh': I","'m_lower_bound': m",'m = 2*abs(I)/(D+math.sqrt(D*D+4*H*abs(I)))'])
 checks['perstep_projection_precedes_norm']=opt.index('a_new = self.taylor_project(a_new)')<opt.index('drho = self.fields(a_new - a)')
 checks['initial_projection_separate']='a_start = prob.taylor_project(a0, iters=8)' in run
 checks['all_input_hashes_unchanged']=all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'all_checks_pass':all(checks.values()),'all_table_value_checks':printed,'all_probe_label_checks':countchecks,'all_ratio_display_checks':ratio_checks,'comparisons':comps,'H18_bands':band,'held_in_quantities':held,'conservative_floors':floors,'optimizer_lines_literal_only':optimizer_lines,'issues':issues,'scope':'CONFIRMED finite FLOAT tables and ratios when flags pass; no quadrature certification and no027/028 PDE acceptance. Selected source/status claims refuted or unsupported as detailed.'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',out['all_checks_pass'],sha(B/'verification/result.json'))
 for k,v in checks.items():
  if not v:print('FAILED',k)
 for n,c in comps.items():print(n,c['counts_decrease_equal_increase'],c['minimum']['ratio_FLOAT_decimal_approx'],c['maximum']['ratio_FLOAT_decimal_approx'])
 for n,r in held.items():print(n,{k:float(Q(v)) for k,v in r.items() if k!='rows'})
 assert all(checks.values())
if __name__=='__main__':main()

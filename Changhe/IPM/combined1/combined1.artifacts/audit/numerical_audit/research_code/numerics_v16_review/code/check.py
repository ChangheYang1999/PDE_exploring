"""Independent finite decimal/text audit; no publisher imports or PDE certification."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_v16_review'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();mf=json.loads((B/'source/MANIFEST.json').read_text());inputs={}
 for e in mf['files'].values():
  p=R/e['path'];assert sha(p)==e['sha256'];inputs[e['path']]=e['sha256']
 assert not mf['checker_exists'] and sha(B/'PROOF.md')==mf['proof_sha256']
 for p in [B/'PROOF.md',B/'source/MANIFEST.json',B/'source/publication.diff',Path(__file__)]:inputs[str(p.relative_to(R))]=sha(p)
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
  large=re.findall(r'\((\d+), (\d+)\) ([0-9]+[.][0-9]+)',summary.split('K >= 1800 factors:',1)[1]);assert len(large)==10
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
 pub=datetime.fromisoformat('2026-10-29T16:06:03+00:00');accepted={e['number']:Q(e['accepted_floor']) for e in load('accepted_distances')['entries']};floorline=next(l for l in text.splitlines() if 'Certified floors (CONFIRMED)' in l);floors=[]
 for n,f in re.findall(r'(0\d\d) > ([0-9.]+)',floorline):floors.append({'candidate':n,'display':f,'accepted_floor':str(accepted[int(n)]),'pass':Q(f)<=accepted[int(n)]})
 checks['six_short_distance_floors_conservative']=len(floors)==6 and all(x['pass'] for x in floors)
 checks['024_actual_middle_order32']=load('N4_024_holdout.json')['comparison_parameters']['middle_order024']==32
 checks['026_actual81rows']=len(load('N4_026_holdout.json')['exact_objective_rows'])==81
 checks['016_cells_complete_before_publication']=datetime.fromisoformat(load('N4_016_cells.json')['utc'])<pub
 checks['015_cells_complete_before_publication']=datetime.fromisoformat(load('015_cells')['utc'])<pub
 checks['025_audits_complete_before_publication']=all(datetime.fromisoformat(load(n)['utc'])<pub for n in ['N4_025_holdout.json','N4_025_shape_peer.json','N4_025_weak.json'])
 lines=text.splitlines()
 checks['016_P2_complete_before_publication']=datetime.fromisoformat(load('N4_016_complete')['utc'])<pub and all(load('N4_016_complete')['checks'].values())
 checks['017_cells_complete_before_publication']=datetime.fromisoformat(load('N4_017_cells')['utc'])<pub
 issues=[]
 sec6=text.split('## 6. Status and next runs',1)[1]
 for name,good,bad in [('016_P2','016 G0, rF, G1, P2 all CONFIRMED','P2 under comparison'),('017_cells','accepted both ways, matrix row 106','CLAIMED), as this lane'),('radial_degree','functions of degrees l = 12..23','functions n = 12..23'),('registered_radius','r about 20 to 40','r 20 to 50')]:
  checks['repaired_'+name]=good in sec6 and bad not in sec6
 if "028's diag2, the last computation of this lane" in sec6:
  issues.append({'issue':'stale_last_computation','verdict':'REFUTED','scope':'Documentary chronology only','text':"Section6 still calls028 diag2 the last computation, although section0 records later Newton and cell evaluations."})
 checks['repaired_summary_024rule']='LOSS (MID 16; 024 MID 32)' in text
 checks['repaired_summary_81rows']='021, 025 and 026 use 81 rows' in text
 checks['separate_mesh_endpoint_scope']='this mesh-step sum is not one' in text
 checks['firstmode_not_heldout']='not held-out evidence' in text and 'objective penalizes the raw pairings' in text
 first={n:load(n+'_weaktests2.json',True)['NORM-T-WEAK-v1_a0'] for n in ['027','028']}
 ks=list(map(int,first['027']));checks['same27firstmodeindices']=len(ks)==27 and list(first['027'])==list(first['028'])
 firstrows=[]
 for k in ks:
  old=Q(first['027'][str(k)]['m_lower_bound']);new=Q(first['028'][str(k)]['m_lower_bound']);ratio=new/old
  firstrows.append({'k':k,'027':str(old),'028':str(new),'ratio_exact':str(ratio),'ratio_float':float(ratio)})
 selected=[64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
 displays=['2.32','6.48','120','6.29','4.94','5.83','8.05','7.12','3.10','0.653','0.106','0.0385','3.22']
 for k,tok in zip(selected,displays):
  ratio=next(Q(v['ratio_exact']) for v in firstrows if v['k']==k)
  checks[f'firstmode_ratio_{k}']=Q(fmt(ratio,'.3g'))==Q(tok)
 maxima={n:max(first[n],key=lambda k:Q(first[n][k]['m_lower_bound'])) for n in first}
 checks['firstmode_maxima']=maxima=={'027':'2048','028':'512'}
 checks['firstmode_maximum_displays']=fmt(first['027']['2048']['m_lower_bound'],'.2e')=='1.78e-04' and fmt(first['028']['512']['m_lower_bound'],'.2e')=='5.49e-04'
 diagnostics={};finalrows={};normdiff={};attempts={}
 for n in ['027','028']:
  log=(R/mf['files'][n+'_log']['path']).read_text();stdout=(R/mf['files'][n+'_stdout']['path']).read_text()
  iterations=re.findall(r'^it\s+(\d+) obj ([0-9.e+\-]+) -> ([0-9.e+\-]+) (ACC|rej)',log,re.M)
  attempts[n]={'attempted':len(iterations),'accepted':sum(v[3]=='ACC' for v in iterations)}
  checks[n+'_60attempts']=len(iterations)==60 and [int(v[0]) for v in iterations]==list(range(1,61))
  checks[n+'_accepted_count']=attempts[n]['accepted']=={'027':38,'028':39}[n]
  final=next(l for l in stdout.splitlines() if l.startswith('FINAL (FLOAT,'))
  parsed=dict(re.findall(r'(P2|G1|G0|rF|supF) ([0-9.e+\-]+)',final))
  pubpart=text.split('## 2'+{'027':'c','028':'d'}[n]+'.',1)[1].split('## ',1)[0]
  checks[n+'_final_optimizer_displays']=all(k+' '+v in pubpart for k,v in parsed.items())
  diag=load(n+'_diag2.json',True);diagnostics[n]={k:str(diag[k]) for k in ['G0','G1','P2','rF','H','supF']}
  for key,form in [('G0','.4f'),('G1','.3f'),('P2','.1f'),('rF','.3f'),('H','.4f'),('supF','.4f')]:
   label='sup|F|' if key=='supF' else key;checks[n+'_MID32_'+key]=label+' '+fmt(diag[key],form) in pubpart
  normdiff[n]={k:str(abs(Q(diag[k])/Q(parsed[k])-1)) for k in ['G0','G1','P2','rF']}
  checks[n+'_MID32_MID16_finite_difference']=all(Q(v)<Q('.009') for v in normdiff[n].values())
  row=next(l for l in stdout.splitlines() if l.startswith('FINAL pairings:'))
  finalrows[n]=[Q(t) for t in row.split(':',1)[1].split()];checks[n+'_67_final_rows']=len(finalrows[n])==67
 checks['nine_MID16_pairings_larger']=all(abs(finalrows['028'][ks.index(k)])>abs(finalrows['027'][ks.index(k)]) for k in selected[:9])
 penalties={}
 for name,inds in [('all67',range(67)),('first27',range(27)),('nine', [ks.index(k) for k in selected[:9]])]:
  sums={n:10**12*sum((finalrows[n][i]**2 for i in inds),Q(0)) for n in ['027','028']}
  penalties[name]={'027':str(sums['027']),'028':str(sums['028']),'ratio_exact':str(sums['028']/sums['027'])}
 for name,display,form in [('all67','9.45','.2f'),('first27','12.9','.1f'),('nine','27.1','.1f')]:checks[name+'_printed_penalty_ratio']=fmt(Q(penalties[name]['ratio_exact']),form)==display
 checks['rounded_total_penalties']=fmt(Q(penalties['all67']['027']),'.0f')=='249' and fmt(Q(penalties['all67']['028']),'.0f')=='2351'
 checks['printed_pairing_maxima']=fmt(max(abs(x) for x in finalrows['027']),'.3e')=='5.643e-06' and fmt(max(abs(x) for x in finalrows['028']),'.3e')=='1.555e-05'
 optimizer_lines=[l for l in lines if l.startswith('Optimizer report (MID ')];checks['five_complete_optimizer_report_lines']=len(optimizer_lines)==5 and all(re.fullmatch(r'Optimizer report \(MID (?:16|32)\): P2 [0-9.e+\-]+ G1 [0-9.e+\-]+ G0 [0-9.e+\-]+ rF [0-9.e+\-]+ supF [0-9.e+\-]+',l) for l in optimizer_lines)
 weak=(R/mf['files']['N1_weak_tests3.py']['path']).read_text();opt=(R/mf['files']['N1_ipm_opt3.py']['path']).read_text();run=(R/mf['files']['N1_run_quot.py']['path']).read_text()
 checks['distinct_I_and_m']=all(t in weak for t in ["'I_signed_mesh': I","'m_lower_bound': m",'m = 2*abs(I)/(D+math.sqrt(D*D+4*H*abs(I)))'])
 checks['perstep_projection_precedes_norm']=opt.index('a_new = self.taylor_project(a_new)')<opt.index('drho = self.fields(a_new - a)')
 checks['initial_projection_separate']='a_start = prob.taylor_project(a0, iters=8)' in run
 # Added v16 finite data. All bounds below concern serialized decimals only.
 newsection=text.split('## 0. Changes since numerics_v15',1)[1].split('## 0a.',1)[0]
 newton={}
 expected_newton={'027':{'G0_mesh':'0.2762','linearized_residual_L2':'0.1864','h0_L2':'1.166e-2','quadratic_term_L2':'1.97e-3','pair0':'1.59e-6','pair1':'3.04e-6','reduction':'32'},'028':{'G0_mesh':'0.2442','linearized_residual_L2':'0.1618','h0_L2':'1.182e-2','quadratic_term_L2':'1.96e-3','pair0':'7.49e-6','pair1':'3.68e-6','reduction':'34'}}
 for n,e in expected_newton.items():
  d=load(n+'_newton',True);nr={}
  checks[n+'_newton_source']=d['sha256']==data[n]['sha256'] and Q(d['lam'])==Q('1e-6') and 'Gauss 24/panel x midpoint 180' in d['rule']
  for k,f in [('G0_mesh','.4f'),('linearized_residual_L2','.4f'),('h0_L2','.3e'),('quadratic_term_L2','.2e')]:
   checks[n+'_newton_'+k]=Q(fmt(d[k],f))==Q(e[k]) and e[k] in newsection;nr[k]=str(d[k])
  for key,target in [('pairings_F','pair0'),('pairings_linearized','pair1')]:
   v=d[key]['7:131'];checks[n+'_'+key]=Q(fmt(v,'.2e'))==Q(e[target]) and e[target] in newsection;nr[key]=str(v)
  reduction=100*(1-Q(d['linearized_residual_L2'])/Q(d['G0_mesh']))
  checks[n+'_reduction_percent']=Q(e['reduction'])-Q(1,2)<reduction<Q(e['reduction'])+Q(1,2)
  nr['reduction_exact']=str(reduction);newton[n]=nr
  log=(R/mf['files'][n+'_newton_log']['path']).read_text()
  checks[n+'_newton_final_log']='written' in log and 'quadratic term' in log
 checks['newton_scope']='FLOAT upper bounds' in newsection and '007 only' in newsection and 'no inverse claim' in newsection
 code=(R/mf['files']['N1_newton_step.py']['path']).read_text()
 checks['newton_central_difference_and_density']=all(t in code for t in ['eps = 1e-4','Jd = (Fe-Fm)/(2*eps)',"h0 = Fdd[('rho', (0, 0))]",'LAM','r_max=1e4'])
 cells={};thresholds=list(map(Q,['15.88162','8.716729','4.799949','2.565236','1.263642','0.5028299','0.06411577']))
 wanted_values={'026':['21.51','18.69','16.51','14.80','13.43','12.32','11.40'],'027':['19.79'],'028':['21.23','18.73','16.78','15.21','13.91','12.82','11.89']}
 wanted_ratios={'026':['1.35','2.14','3.44','5.77','10.63','24.50','177.82'],'027':['1.25','2.00','3.24','5.49','10.21','23.70','172.89'],'028':['1.34','2.15','3.50','5.93','11.01','25.50','185.47']}
 for n in wanted_values:
  d=load(n+'_cells',True);rows=d['cells'];checks[n+'_cells_source']=d['sha256']==data[n]['sha256'] and len(rows)==7 and 'Gauss 32/panel' in d['rule'];outrows=[]
  for i,r in enumerate(rows):
   q=Q(r['N_h_modes_1_3_FLOAT']);thr=Q(r['threshold_at_l']);ratio=q/thr
   checks[f'{n}_cell{i}_geometry']=list(map(Q,r['cell']))==[Q(i,4),Q(i+1,4)] and thr==thresholds[i]
   checks[f'{n}_cell{i}_ratio']=abs(ratio-Q(r['ratio']))<Q('1e-12') and ratio>1 and Q(fmt(ratio,'.2f'))==Q(wanted_ratios[n][i]) and wanted_ratios[n][i] in newsection
   checks[f'{n}_cell{i}_norm_assembly']=abs(q*q-Q(r['mode1'])**2-Q(r['mode3'])**2)<Q('1e-10')
   if i<len(wanted_values[n]):checks[f'{n}_cell{i}_value']=Q(fmt(q,'.2f'))==Q(wanted_values[n][i]) and wanted_values[n][i] in newsection
   outrows.append({'cell':list(map(str,r['cell'])),'norm_decimal':str(q),'ratio_exact':str(ratio),'threshold_decimal':str(thr)})
  cells[n]=outrows
 checks['cell_scope']='FLOAT proxies, no dyadic verdict' in newsection
 energy={};wanted_energy={'007':'606.82','013':'605.29','016':'628.83','017':'605.63','021':'597.58','022':'603.35','025':'673.09','026':'615.79','027':'587.47','028':'567.09'}
 for n,v in wanted_energy.items():
  d=load(n+'_energy_diag',True);co={k:Q(d[k]) for k in ['P2','G1','G0','H']};sq=co['P2']**2+2**14*co['G1']**2+2**18*co['G0']**2+Q(20,21)*2**18*co['H']**2;e=Q(v)
  checks[n+'_energy_display']=(e-Q(1,200))**2<sq<(e+Q(1,200))**2 and n+' '+v in newsection
  checks[n+'_energy_rule']='Gauss 32/panel' in d['rule']
  if 'E2_proxy_raw_with_H' in d:checks[n+'_saved_energy_assembly']=abs(Q(d['E2_proxy_raw_with_H'])**2-sq)<Q('1e-7')
  energy[n]={'components_exact':{k:str(x) for k,x in co.items()},'square_exact':str(sq),'display':v,'source_candidate_sha256':d['sha256']}
 checks['energy_scope']='mesh values, not bounds' in newsection and 'no ordering of correction distances' in newsection
 prior=load('v15_result');checks['accepted_v15_allchecks']=prior['all_checks_pass'] and all(prior['checks'].values())
 checks['all_input_hashes_unchanged']=all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'all_checks_pass':all(checks.values()),'all_table_value_checks':printed,'all_probe_label_checks':countchecks,'all_ratio_display_checks':ratio_checks,'comparisons':comps,'H18_bands':band,'held_in_quantities':held,'conservative_floors':floors,'optimizer_lines_literal_only':optimizer_lines,'firstmode_rows':firstrows,'firstmode_maxima':maxima,'diagnostics':diagnostics,'MID32_MID16_relative_difference_exact':normdiff,'optimizer_attempts':attempts,'penalties_from_rounded_final_rows':penalties,'issues':issues,'scope':'CONFIRMED finite FLOAT tables and ratios when flags pass; no quadrature certification and no027/028 PDE acceptance. Four repeated source/status claims refuted as detailed. First-mode and penalty comparisons use finite FLOAT source decimals only.'}
 out.update({'newton_displays':newton,'new_cells':cells,'energy_displays':energy,'scope':'CONFIRMED finite FLOAT displays and repaired prior prose; no027/028 PDE certification. One stale last-computation description refuted.'})
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',out['all_checks_pass'],sha(B/'verification/result.json'))
 for k,v in checks.items():
  if not v:print('FAILED',k)
 for n,c in comps.items():print(n,c['counts_decrease_equal_increase'],c['minimum']['ratio_FLOAT_decimal_approx'],c['maximum']['ratio_FLOAT_decimal_approx'])
 for n,r in held.items():print(n,{k:float(Q(v)) for k,v in r.items() if k!='rows'})
 assert all(checks.values())
if __name__=='__main__':main()

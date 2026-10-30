"""Finite literal/source audit. No publisher imports or numerical PDE claims."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_v13_audit';sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();mf=json.loads((B/'source/MANIFEST.json').read_text());inputs={}
 for fn,e in mf['files'].items():
  p=B/'source'/fn;assert sha(p)==e['sha256'];inputs[str(p.relative_to(R))]=e['sha256']
 assert sha(B/'PROOF.md')==mf['proof_sha256']
 for p in [Path(__file__),B/'PROOF.md',B/'source/MANIFEST.json',B/'verification/PROOF_FIRST.json']:inputs[str(p.relative_to(R))]=sha(p)
 read=lambda n:json.loads((B/'source'/n).read_text());text=(B/'source/numerics_v13.md').read_text();data={n:read(f'N1_{n}_weaktests3.json') for n in ['016','022','023','024','025','026']};pub=datetime.fromisoformat('2026-10-29T13:13:19+00:00')
 tables={};printed_checks=[];identities=[]
 for n,heading,end in [('024','## 1. C1-N1-024','## 2. C1-N1-025'),('025','## 2. C1-N1-025','## 2c.'),('026','## 2b. C1-N1-026','## 3.')]:
  section=text.split(heading,1)[1].split(end,1)[0];table={}
  for line in section.splitlines():
   if '[registered, HELD OUT]' not in line:continue
   cells=[x.strip() for x in line.split('|')[1:-1]];pair=tuple(map(int,re.search(r'\((\d+), (\d+)\)',cells[0]).groups()));assert pair not in table;table[pair]=dict(zip(['016','022','023',n],cells[2:],strict=True))
   for label,value in table[pair].items():
    original=data[label]['probes'][f'{pair[0]}:{pair[1]}']['m_lower_bound'];printed_checks.append({'candidate':label,'n':pair[0],'K':pair[1],'table_value':value,'stored_float':original,'formats_equal':format(original,'.2e')==value})
  assert set(table)=={(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]};tables[n]=table
 assert all(r['formats_equal'] for r in printed_checks)
 for a in ['024','025','026']:
  for pair,row in tables[a].items():
   for parent in ['016','022','023']:identities.append(row[parent]==tables['024'][pair][parent])
 assert all(identities)
 comps={}
 for new,old in [('023','016'),('024','016'),('025','016'),('026','022')]:
  rows=[];source=tables[new] if new!='023' else tables['024']
  for (n,K),r in source.items():
   a,b=Q(r[old]),Q(r[new]);ap,bp=(Q(str(data[c]['probes'][f'{n}:{K}']['m_lower_bound'])) for c in [old,new]);q=b/a;fq=bp/ap
   rows.append({'n':n,'K':K,'printed_old':str(a),'printed_new':str(b),'ratio_printed_exact':str(q),'ratio_printed_approx':float(q),'printed_sign':(b>a)-(b<a),'stored_FLOAT_ratio_exact':str(fq),'stored_FLOAT_ratio_approx':float(fq),'stored_FLOAT_sign':(bp>ap)-(bp<ap)})
  stats={}
  for representation in ['printed','stored_FLOAT']:
   key='ratio_printed_exact' if representation=='printed' else 'stored_FLOAT_ratio_exact';count={str(z):sum(r[representation+'_sign']==z for r in rows) for z in [-1,0,1]};sub={}
   for label,pred in [('all',lambda r:True),('decreased',lambda r:r[representation+'_sign']<0),('increased',lambda r:r[representation+'_sign']>0),('K_ge_1800',lambda r:r['K']>=1800)]:
    selected=[r for r in rows if pred(r)];values=[Q(r[key]) for r in selected];sub[label]={'count':len(values),'min_exact':str(min(values)),'max_exact':str(max(values)),'min_approx':float(min(values)),'max_approx':float(max(values))}
   stats[representation]={'counts_decrease_equal_increase':[count[str(z)] for z in [-1,0,1]],'subsets':sub}
  comps[new+'_vs_'+old]={'rows':rows,'statistics':stats}
 find=lambda which,n,k:next(r for r in comps[which]['rows'] if (r['n'],r['K'])==(n,k))
 weak=(B/'source/N1_weak_tests3.py').read_text();opt=(B/'source/N1_ipm_opt3.py').read_text();run=(B/'source/N1_run_quot.py').read_text();held={}
 for n in ['025','026']:
  rows=[]
  for mode in range(19,32,2):
   for base in [128,512]:
    K=(mode-1)//2+base;r=data[n]['probes'][f'{mode}:{K}'];rows.append({'n':mode,'K':K,'I_signed_mesh':r['I_signed_mesh'],'m_lower_bound_FLOAT':r['m_lower_bound'],'D_FLOAT':r['D'],'H_bound_mesh_FLOAT':r['H_bound_mesh']})
  held[n]={'rows':rows,'abs_I_FLOAT_min':min(abs(r['I_signed_mesh']) for r in rows),'abs_I_FLOAT_max':max(abs(r['I_signed_mesh']) for r in rows),'m_FLOAT_min':min(r['m_lower_bound_FLOAT'] for r in rows),'m_FLOAT_max':max(r['m_lower_bound_FLOAT'] for r in rows)}
 checks={
 'clean_header_now':text.count('1. Reading of the GPU phase')==1 and 'ACK 11:52Z in RUN_STATUS' in text,
 'all300_table_values_match_stored_FLOAT_rounding':len(printed_checks)==300 and all(r['formats_equal'] for r in printed_checks),
 'all_parent_columns_agree':all(identities),
 '025_decreased_ratio_below_claimed026':Q(find('025_vs_016',25,600)['ratio_printed_exact'])<Q('0.26'),
 '025_K1800_n31_exceeds158':Q(find('025_vs_016',31,1800)['ratio_printed_exact'])>Q('1.58'),
 '025_K1800_n29_exceeds158':Q(find('025_vs_016',29,1800)['ratio_printed_exact'])>Q('1.58'),
 '024_K600_n19_exceeds157':Q(find('024_vs_016',19,600)['ratio_printed_exact'])>Q('1.57'),
 '026_fall_count_not7':comps['026_vs_022']['statistics']['stored_FLOAT']['counts_decrease_equal_increase'][0]!=7,
 '024_rise_count_not16':comps['024_vs_016']['statistics']['stored_FLOAT']['counts_decrease_equal_increase'][2]!=16,
 'raw_pairing_and_proxy_keys_distinct':"'I_signed_mesh': I" in weak and "'m_lower_bound': m" in weak and 'D = A+B+C' in weak and 'm = 2*abs(I)/(D+math.sqrt(D*D+4*H*abs(I)))' in weak,
 'objective_penalizes_raw_pairing':'sqrt(wpair) I_k' in opt and 'def pairings(self, F)' in opt,
 'per_step_projection_included':opt.index('a_new = self.taylor_project(a_new)')<opt.index('drho = self.fields(a_new - a)'),
 'initial_projection_separate':'a_start = prob.taylor_project(a0, iters=8)' in run,
 'MID16_summary_false_for024':'| LOSS (MID 16) |' in text and 'LOSS = last accepted objective on the MID 16 rule' in text and read('N4_024_holdout.json')['comparison_parameters']['middle_order024']==32,
 'unqualified_certificate_attribution_present':text.count("a certified bound is c1-n4's")==3,
 '025_own_shape_completed_before_publication':datetime.fromisoformat(read('N4_025_holdout.json')['utc'])<pub,
 '025_own_weak_completed_before_publication':datetime.fromisoformat(read('N4_025_weak.json')['utc'])<pub,
 '025_independent_shape_completed_before_publication':datetime.fromisoformat(read('N4_025_shape_peer.json')['utc'])<pub,
 '016_conditional_cells_completed_before_publication':datetime.fromisoformat(read('N4_016_cells.json')['utc'])<pub,
 'stale_FLOAT_only_and_dyadic_labels':'have FLOAT values only' in text and 'CLAIMED pending c1-n4' in text,
 'all_three_optimizer_report_lines_truncated':len(re.findall(r'^Optimizer report \(MID (?:16|32)\): \d{5}e\+02 G1',text,re.M))==3,
 'causal_and_prospective_wording_present':'Separates the row effect' in text and 'new mid-field freedom goes into rF first' in text and 'isolates\n   the effect of the rows' in text,
 'generic_multiscale_unavailability_present':'the two-scale product keys for 020 to 028 are not available' in text,
 }
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 assert all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'publication_sha256':sha(B/'source/numerics_v13.md'),'inputs':inputs,'checks':checks,'table_comparisons':comps,'all_printed_value_checks':printed_checks,'held_in_quantities':held,'launch_metadata_record':'source/launch_filesystem_metadata.json','historical_same_shell_order_independently_observed':False,'mathematical_FLOAT_values_certified':False,'issues':['false025subsetranges','false024rangeandcounts','false026counts','MID16blanketlabelsfor024','rawIversusm','unsupportedactualendpointdistanceattribution','threeoptimizerreporttokenstruncated','stale025ownand016dyadicstatus','unsupportedcausalwording','multiscaleproductavailabilityscope'],'verdict':'REFUTED specified literal claims and unsupported attributions; present filesystem metadata CONFIRMED as observed, historical command order OPEN; existing mathematical certificates unchanged','elapsed_seconds':time.monotonic()-start}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',sha(B/'verification/result.json'))
 for name,c in comps.items():print(name,json.dumps(c['statistics']))
 print('HELD_IN_RANGES',json.dumps({n:{k:v for k,v in r.items() if k!='rows'} for n,r in held.items()}))
if __name__=='__main__':main()

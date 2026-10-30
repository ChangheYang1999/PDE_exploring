from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_v12_audit'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();m=json.loads((B/'source/MANIFEST.json').read_text());inputs={}
 for name,e in m['files'].items():
  p=B/'source'/name;assert sha(p)==e['sha256'];inputs[str(p.relative_to(R))]=sha(p)
 assert sha(B/'PROOF.md')==m['proof_sha256']
 for p in [B/'PROOF.md',B/'source/MANIFEST.json',Path(__file__)]:inputs[str(p.relative_to(R))]=sha(p)
 text=(B/'source/numerics_v12.md').read_text();section=text.split('## 2. C1-N1-025',1)[1].split('## 3.',1)[0];rows=[]
 for line in section.splitlines():
  if '[registered, HELD OUT]' not in line:continue
  cells=[x.strip() for x in line.split('|')[1:-1]];n,K=map(int,re.search(r'\((\d+), (\d+)\)',cells[0]).groups());a,b=Q(cells[2]),Q(cells[-1]);rows.append({'n':n,'K':K,'printed016':cells[2],'printed025':cells[-1],'ratio025_to016_exact':str(b/a),'ratio016_to025_exact':str(a/b),'ratio025_to016_approx':float(b/a)})
 assert len(rows)==25
 find=lambda n,k:next(r for r in rows if (r['n'],r['K'])==(n,k))
 weak=(B/'source/N1_weak_tests3.py').read_text();opt=(B/'source/N1_ipm_opt3.py').read_text();run=(B/'source/N1_run_quot.py').read_text()
 checks={'header_spliced':text.count('1. Reading of the GPU phase')==2 and 'ACK 11:52Z in RUN_1.' in text,'clean_header_claim_false':"this header is clean" in text,'K600_n19_worsens_over24':Q(find(19,600)['ratio025_to016_exact'])>24,'K600_n29_improvement_below3':Q(find(29,600)['ratio016_to025_exact'])<3,'K600_n31_improvement_below3':Q(find(31,600)['ratio016_to025_exact'])<3,'K1200_n25_ratio_over3':Q(find(25,1200)['ratio025_to016_exact'])>3,'K1200_n31_decreases':Q(find(31,1200)['ratio025_to016_exact'])<1,'quantity_keys_distinct':"'I_signed_mesh': I" in weak and "'m_lower_bound': m" in weak and 'm = 2*abs(I)/(D+math.sqrt(D*D+4*H*abs(I)))' in weak,'per_step_projection_precedes_norm':opt.index('a_new = self.taylor_project(a_new)')<opt.index('drho = self.fields(a_new - a)'),'initial_projection_separate':'a_start = prob.taylor_project(a0, iters=8)' in run,'wrong_MID16_column': '| LOSS (MID 16) |' in text and 'LOSS = last accepted objective on the MID 16 rule' in text,'accepted024_counterevidence':json.loads((B/'source/N4_024_holdout.json').read_text())['comparison_parameters']['middle_order024']==32}
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 out={'utc':datetime.now(timezone.utc).isoformat(),'publication_sha256':sha(B/'source/numerics_v12.md'),'inputs':inputs,'checks':checks,'printed_table_ratios':rows,'mathematical_values_certified':False,'verdict':'REFUTED listed literal summaries and labels; existing rigorous exclusions unchanged; actual endpoint density-change bound OPEN','elapsed_seconds':time.monotonic()-start}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['verdict'],sha(B/'verification/result.json'))
if __name__=='__main__':main()

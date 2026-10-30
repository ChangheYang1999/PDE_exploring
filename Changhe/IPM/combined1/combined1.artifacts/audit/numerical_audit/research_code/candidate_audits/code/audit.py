from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time,shutil
from flint import ctx,fmpq,arb
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/refit_audit/code'))
from convert import convert
from sectors_flint import sectors,aq,enc
BASE=ROOT/'research/candidate_audits'
SHARED=ROOT.parent/'c1-shared/candidate_snapshots'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name):
 start=time.monotonic();ctx.prec=384;src=SHARED/name;dest=BASE/'data'/name;dest.mkdir(exist_ok=True)
 for namepart in ['SHA256SUMS','MANIFEST.json']:
  if not (dest/namepart).exists():shutil.copy2(src/namepart,dest/namepart)
 checks={}
 for line in (dest/'SHA256SUMS').read_text().splitlines():
  sha,filename=line.split(None,1);filename=filename.lstrip('*')
  assert Path(filename).name==filename
  if not (dest/filename).exists():shutil.copy2(src/filename,dest/filename)
  checks[filename]=digest(dest/filename)==sha;assert checks[filename]
 manifest=json.loads((dest/'MANIFEST.json').read_text());assert manifest['id']==name
 gen=manifest['coefficient_files'][0]['name'];raw=json.loads((dest/gen).read_text())
 if 'cl' not in raw:raw['cl']=raw['cl_exact']
 normalized=dest/'normalized_generators.json';normalized.write_text(json.dumps(raw,indent=2)+'\n')
 state=convert(normalized);state['source_sha256']=digest(dest/gen)
 can=dest/'canonical.json';can.write_text(json.dumps(state,indent=2)+'\n')
 baseline=json.loads((ROOT/'research/baseline/data/state131_independent.json').read_text())
 _,bC,bG,_=sectors(baseline,qmax=0)
 alpha,C,G,E=sectors(state,qmax=1,hmax=max(7,max(j for j,m,k in state["order"])+1))
 rows=[];prior=json.loads((dest/'sector_table.json').read_text());priorrows={fmpq(x['exponent_exact']):x for x in prior['rows']}
 for (h,q),poly in sorted(E.items(),key=lambda item:alpha(*item[0]),reverse=True):
  energy=sum((v*v for v in poly.values()),fmpq(0));norm=(arb.pi()*aq(energy)).sqrt()
  row={'h':h,'q':q,'exponent':enc(alpha(h,q)),'exponent_arb':aq(alpha(h,q)).str(40),
       'exact_zero':not poly,'full_circle_norm':norm.str(60),'quadrant_norm':(norm/2).str(60),
       'sine_coefficients':{str(n):enc(v) for n,v in sorted(poly.items())}}
  previous=priorrows.get(alpha(h,q))
  if previous is not None:
   row['prior_status_agrees']=(previous['status']=='EXACT-ZERO')==row['exact_zero'];assert row['prior_status_agrees']
   row['prior_full_circle_norm']=previous['full_circle_L2']
   row['prior_float_relative_difference']=abs(float(norm.mid())-previous['full_circle_L2'])/max(1.,abs(float(norm.mid())))
   assert row['prior_float_relative_difference']<1e-12
  rows.append(row)
  if alpha(h,q)>=-2:print(h,q,row['exact_zero'],row['full_circle_norm'],flush=True)
 out={'candidate':name,'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
      'snapshot_hashes_confirmed':checks,'manifest_sha256':digest(dest/'MANIFEST.json'),
      'generator_sha256':digest(dest/gen),'canonical_sha256':digest(can),'code_sha256':digest(Path(__file__)),
      'generator_count':state['generator_count'],'canonical_nonzero_count':len(state['order']),
      'c_exact':state['cl'],'a0_exact':state['a0'],'a0_arb':aq(fmpq(state['a0'])).str(60),
      'strain_exact':state['strain'],'B0n_exact':fmpq(state['strain'])==1-fmpq(state['cl']),
      'c_equal_state131':fmpq(state['cl'])==fmpq(baseline['cl']),
      'leading_potential_equal_state131':C[0,0]==bC[0,0],'leading_density_equal_state131':G[0,0]==bG[0,0],
      'all_forbidden_zero':all(not P for (h,q),P in E.items() if alpha(h,q)>=-2),
      'first_nonzero_sector':next(row for row in rows if not row['exact_zero']),
      'sectors':rows,'elapsed_seconds':time.monotonic()-start}
 (BASE/'verification'/f'{name}.json').write_text(json.dumps(out,indent=2)+'\n')
 print('a0',out['a0_arb'],'B0n',out['B0n_exact'],'tailfixed',out['leading_density_equal_state131'],'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run(sys.argv[1])

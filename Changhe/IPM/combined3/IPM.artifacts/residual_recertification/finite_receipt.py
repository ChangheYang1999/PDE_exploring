"""Exact rational whole-annulus assembly and source/code binding receipt."""
import argparse,gzip,json,hashlib,sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--repo-root',type=Path,default=Path('/mnt/d/Changhe_D/PDE_exploring'));args=p.parse_args()
 folder=args.directory;config=json.loads((folder/'configuration.json').read_text());count=config['panels'];paths=sorted(folder.glob('panel_*.json.gz'));assert len(paths)==count,(len(paths),count)
 lower=Q(0);upper=Q(0);errors=Q(0);maxerror=Q(0);E2=Q(0);E3=Q(0);edge=Q(config['rmin']);layouts=Counter();degrees=[];precisions=set();files={}
 for i,path in enumerate(paths):
  with gzip.open(path,'rt')as fp:d=json.load(fp)
  assert d['status']=='CERTIFIED_FINITE_RESIDUAL_PANEL'and d['index']==i
  a,b,c,h=map(Q,[d[k]for k in ['left','right','center','halfwidth']]);assert a==edge and b>a and c==(a+b)/2 and h==(b-a)/2
  R,H=Q(d['cauchy_radius']),Q(d['residual_majorant_upper']);assert 0<h<R/2 and R<=c/8 and H>0
  K=d['degree'];q=h/R;tail=H*q**(K+1)/(1-q);assert Q(d['L2']['residual_remainder_l1_upper'])>=tail
  lo,hi=map(Q,[d['L2'][k]for k in ['energy_lower','energy_upper']]);assert 0<=lo<=hi
  lower+=lo;upper+=hi;e=Q(d['L2']['analytic_error_upper']);assert e>=0;errors+=e;maxerror=max(maxerror,e)
  E2+=Q(d['high_order']['E2_upper']);E3+=Q(d['high_order']['E3_upper']);degrees.append(K);precisions.add(d['precision']);layouts[d.get('convolution_layout','legacy')]+=1;edge=b;files[path.name]=digest(path)
 assert edge==Q(config['rmax'])
 root=args.repo_root;inputs={'base007':root/'Changhe/IPM/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json','phi013':root/'Changhe/IPM/combined2/IPM.artifacts/exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json'}
 source_hashes={k:digest(v)for k,v in inputs.items()};assert source_hashes==config['source_hashes']
 codefolder=Path(__file__).resolve().parent;codes={k:digest(codefolder/k)for k in ['finite.py','finite_fast.py','run_finite.py','run_finite_legacy.py','high_order.py','finite_receipt.py']}
 sourcecode=root/'Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/fields013.py'
 out={'status':'COMPLETE_FRESH_FINITE_ANNULUS_CERTIFICATE','fixed_c':'4076476460239181/2251799813685248','source_hashes':source_hashes,'source_paths':{k:str(v.relative_to(root))for k,v in inputs.items()},'source_evaluator_sha256':digest(sourcecode),'code_sha256':codes,'configuration_sha256':digest(folder/'configuration.json'),'domain':{'left':config['rmin'],'right':config['rmax'],'panels':count,'complete_exact_adjacency':True,'center_halfwidth_identities':True,'cauchy_disk_containment':True},'L2_energy_lower':str(lower),'L2_energy_upper':str(upper),'L2_analytic_error_upper_sum':str(errors),'L2_analytic_error_upper_max':str(maxerror),'E2_upper':str(E2),'E3_upper':str(E3),'degree_min':min(degrees),'degree_max':max(degrees),'precision_bits':sorted(precisions),'counts_by_convolution_layout':dict(layouts),'raw_files_sha256':files,'historical_residual_dependencies':False,'scope':'Actual residual on the finite annulus only. Whole-plane assembly additionally requires the fresh origin and exterior certificates.'}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['raw_files_sha256','L2_energy_lower','L2_energy_upper','L2_analytic_error_upper_sum','L2_analytic_error_upper_max','E2_upper','E3_upper']},indent=2));print('L2 energy upper',float(upper),'analytic error sum',float(errors),'E2',float(E2),'E3',float(E3),flush=True)
if __name__=='__main__':main()

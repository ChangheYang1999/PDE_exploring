"""Cross-check residual Kronecker convolution against existing Acb layout.

The check covers every output mode and radial Taylor order0,1,2 at five
radii. It is an independent algebraic implementation check; certification
comes from the validated producer and its whole-plane raw enclosures.
"""
import argparse,json,sys
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--fast',action='store_true');p.add_argument('--repo-root',type=Path,default=Path('/mnt/d/Changhe_D/PDE_exploring'));p.add_argument('--output',type=Path,required=True);args=p.parse_args()
 source=args.repo_root/'Changhe/IPM/combined3/IPM.artifacts/coercivity_residual'
 sys.path.insert(0,str(source));import fields013
 from finite import Evaluator,residual_taylor,SOURCE_HASHES
 if args.fast:
  from finite_fast import residual_taylor_fast as residual_taylor
 import residual_modal_screen as original
 e=Evaluator(640,max_density_order=1,max_velocity_order=0);original.E=e;rows=[]
 for radius in ['1/1000','1/3','1','10','10000']:
  new=residual_taylor(e,radius,2);old=original.residual_jets(radius,2);checks=0
  for n,series in new.items():
   for k in range(3):
    rhs=-2*old[k][2*original.SHIFT+n].imag
    assert series[k].overlaps(rhs),(radius,n,k,series[k],rhs)
    checks+=1
  rows.append({'radius':radius,'checks':checks,'pass':True})
 out={'status':'PASS','convolution_layout':'parity_compressed'if args.fast else'legacy','rows':rows,'source_hashes':SOURCE_HASHES,'checks':sum(row['checks']for row in rows)}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()

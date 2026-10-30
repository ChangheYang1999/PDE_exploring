from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time
from flint import ctx,arb,fmpq
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,pshift
from norms import derivative,norm

def run(name):
 ctx.prec=768;start=time.monotonic()
 path=ROOT/f'research/candidate_audits/data/{name}/canonical.json' if name.startswith('C1-N1-') else ROOT/(f'research/baseline/data/{name}_independent.json' if name.startswith('state') else f'research/refit_audit/data/{name}_canonical.json')
 model=Radial(path);D={(0,0):{(j+1,'s',n):pshift(P,2) for (j,n),P in model.rho.items()}}
 for d in range(3):
  for nx in range(d+2):D[d+1,nx]=derivative(D[d,0],d,'y',model.delta) if nx==0 else derivative(D[d,nx-1],d,'x',model.delta)
  for nx in range(1,d+1):assert D[d+1,nx]==derivative(D[d,nx],d,'y',model.delta)
 out={'candidate':name,'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'norms':{}}
 for d in [2,3]:
  row=norm(D,d,model.delta);out['norms'][f'D{d}rho']=row
  print(name,d,row['status'],row.get('norm_upper_ball'),flush=True)
 for label,weights in [('D_rho_x',{1:1,2:1}),('D_rho_y',{0:1,1:1})]:
  out['norms'][label]=norm(D,2,model.delta,multiplicities=weights)
 assert fmpq(out['norms']['D_rho_x']['unweighted_rational_sum'])+fmpq(out['norms']['D_rho_y']['unweighted_rational_sum'])==fmpq(out['norms']['D2rho']['unweighted_rational_sum'])
 X=arb(out['norms']['D_rho_x']['norm_upper']);Y=arb(out['norms']['D_rho_y']['norm_upper'])
 out['gradient_identity_conditional_HS_upper']=(((arb(2).log()-arb(1)/2)*X**2+(3*arb(2).log()-2)*Y**2)/(16*arb.pi())).sqrt().str(60)
 const=((4*arb(2).log()-1)/(8*arb.pi())).sqrt()
 out['T4_conditional_HS_constant']=const.str(50)
 out['T4_conditional_HS_upper']=(const*arb(out['norms']['D2rho']['norm_upper'])).str(50)
 out['elapsed_seconds']=time.monotonic()-start
 (ROOT/f'research/background_sobolev/verification/{name}.json').write_text(json.dumps(out,indent=2)+'\n')
 print('gradient identity conditional HS upper',out['gradient_identity_conditional_HS_upper'],flush=True)
 print('conditional HS upper',out['T4_conditional_HS_upper'],'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:] or ['state131']:run(name)

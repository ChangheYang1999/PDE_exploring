"""Exploratory two-engine whole-cell calculation, no numerical acceptance."""
import sys,os,json,time,resource,argparse,hashlib
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
sys.dont_write_bytecode=True
import engine_arb as a,engine_iv as b
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/outer_derivative_cells/evidence'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--left',required=True);ap.add_argument('--right',required=True);ap.add_argument('--tag',required=True);args=ap.parse_args();assert args.tag.replace('_','').isalnum()
 started=datetime.now(timezone.utc).isoformat();ad=a.setup();bd=b.setup();x=a.cell(ad,args.left,args.right,True);y=b.cell(bd,args.left,args.right,x);assert y['coefficient_overlap_checks']==522*33
 x.pop('coefficients');z={'start_utc':started,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXPLORATORY_COMPLETE_CELL_NOT_ACCEPTED','arb':x,'iv':y,'sources':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(__file__).parent.glob('*.py')}}
 with (OUT/(args.tag+'.json')).open('x') as f:json.dump(z,f,indent=2);f.write('\n')
 print(json.dumps({'status':z['status'],'utc':z['utc'],'arb_seconds':x['seconds'],'iv_seconds':y['seconds'],'input_checks':y['derivative_input_checks'],'coefficient_checks':y['coefficient_overlap_checks'],'arb_B':[v['display'] for v in x['B']],'iv_B':[v['display'] for v in y['B']],'norm_square_upper':[str(max(F(x['norm_squares'][p]['upper_exact']),F(y['norm_squares'][p]['upper_exact']))) for p in range(2)]}),flush=True)
if __name__=='__main__':main()

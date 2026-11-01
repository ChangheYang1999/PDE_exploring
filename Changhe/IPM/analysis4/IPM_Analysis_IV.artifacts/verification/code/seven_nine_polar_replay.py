"""Independent exact polar check of the two first tuning blocks and log constants."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from contextlib import redirect_stdout
import io,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
ROOT=Path('research/251_seven_nine_potential_logs')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();p=Path('../a4-lead/code/tuned/hh_tune.py');raw=p.read_bytes();saved=ROOT/'sources/lead_hh_tune.py';saved.write_bytes(raw)
 source=ROOT/'verification/checks.json';data=json.loads(source.read_text());assert data['all_checks_pass'];rows=[]
 for row in data['rows']:
  period=row['Q'];ns={'__name__':'__main__'};buf=io.StringIO();args=sys.argv[:];sys.argv=['lead_hh_tune.py',str(period),'2',str(period+2),'1']
  try:
   with redirect_stdout(buf):exec(compile(raw,'lead_hh_tune.py','exec'),ns)
  finally:sys.argv=args
  f=ns['F'][period];maxk=(max(f)-1)//2;D={maxk+1:F(0)}
  for k in range(maxk,0,-1):D[k]=(f.get(2*k+1,F(0))-k*D[k+1])/(k+1)
  beta=D[2]/8;H=ns['Hk'];lam=beta-H;R=ns['R0'];sigma=ns['sig']
  assert beta==F(row['beta_pure_exact']) and H==F(row['H_Q_exact']) and lam==F(row['lambda_exact']) and R==F(row['R1_exact']) and sigma==F(row['sigma1_exact'])
  obstruction=R+sigma*beta;assert obstruction==sigma*lam and obstruction!=0
  path=ROOT/f'verification/polar_Q{period}.out';path.write_text(buf.getvalue())
  rows.append(dict(Q=period,all_five_exact_constants_agree=True,pure_obstruction_exact=str(obstruction),pure_obstruction_nonzero=True,source_log=dict(path=str(path),sha256=sha256(path.read_bytes()).hexdigest())))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,rows=rows,exact_source=dict(path=str(source),sha256=sha256(source.read_bytes()).hexdigest()),polar_source=dict(path=str(saved),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/polar_replay.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/seven_nine_polar_replay.py').write_bytes(Path('code/seven_nine_polar_replay.py').read_bytes());print(json.dumps(out),flush=True)
if __name__=='__main__':main()

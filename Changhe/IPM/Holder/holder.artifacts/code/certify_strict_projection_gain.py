"""Certify a uniform saving after the independent analytic cross-read."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
import argparse, hashlib, json
R=Path(__file__).resolve().parents[1]
B=R/'08_improved_upper_bounds/local_projection/strict_increment'
P=R/'08_improved_upper_bounds/phase_interpolation/verification/accepted.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def endpoint(x, high=False):return Q(str((x.upper() if high else x.lower()).fmpq()))
def ceil10(x):
 k=-((-x*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);ap.add_argument('--cross-read',required=True);args=ap.parse_args()
 cross=(R/args.cross_read).resolve();assert cross.is_relative_to(R)
 proof=B/'PROOF.md';text=cross.read_text();assert sha(proof) in text and 'no error' in text.lower()
 hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 parent=load(P);assert parent['verdict']=='CONFIRMED' and parent['ledger']=='V177'
 for name,h in parent['sha256'].items():assert sha(R/name)==h;bind(R/name)
 inputs=[r for r in parent['rows'] if r['operator']=='D'];assert [Q(r['alpha']) for r in inputs]==[Q(3,10),Q(1,2),Q(3,4),Q(9,10)]
 assert 60025>58320 and Q(164,3969)<Q(1,4)
 rows=[]
 for row in inputs:
  a=Q(row['alpha']);old=Q(row['safe_upper']);ctx.prec=384
  aa=arb(str(a));eta=arb(82)/321489*aa*(1-aa)*(arb(11)/9)**(aa-2)
  lo,hi=endpoint(eta),endpoint(eta,True);assert 0<lo<=hi
  bound=old-lo;safe=ceil10(bound)
  ctx.prec=768;AA=arb(str(a));ee=arb(1)/9
  fresh=(arb(82)/49)*AA*(1-AA)*ee**4*((1+2*ee).log()*(AA-2)).exp()
  assert lo<=endpoint(fresh)<=endpoint(fresh,True)<=hi
  assert old-endpoint(fresh)<=bound<=Q(safe)<bound+Q(1,10**10)
  assert Q(safe)<old
  rows.append(dict(alpha=str(a),previous_upper=row['safe_upper'],eta_lower=str(lo),eta_upper=str(hi),eta_ball=eta.str(45),safe_upper_D=safe))
 for p in [P,proof,B/'verification/PROOF.md',cross,Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',precision_bits=[384,768],rows=rows,sha256=hashes,method='Strict projection remainder at radius h/2; independent ball recomputation of the saving and exact rational upward rounding')
 (B/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['time_utc'],args.ledger,'CONFIRMED')
 for row in rows:print(row['alpha'],row['eta_ball'],row['safe_upper_D'])
if __name__=='__main__':main()

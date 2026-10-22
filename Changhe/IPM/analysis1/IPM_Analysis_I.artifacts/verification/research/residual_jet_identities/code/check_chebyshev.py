"""Independent exact integer polynomial recurrence; no trigonometric numerics."""
from pathlib import Path
from datetime import datetime,timezone
from flint import fmpz_poly
import argparse,hashlib,json,time,sys
assert not sys.flags.optimize
ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,required=True);ap.add_argument('--end',type=int,required=True);args=ap.parse_args();assert 0<=args.start<args.end<=261
D=Path(__file__).resolve().parents[1];t0=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=sha(D/'PROOF.md');first=json.loads((D/'evidence/first.json').read_text());assert proof==first['proof_sha256']
x=fmpz_poly([0,1]);twox=2*x;T=[fmpz_poly([1]),x];U=[fmpz_poly([1]),twox]
for k in range(1,1043):T.append(twox*T[-1]-T[-2]);U.append(twox*U[-1]-U[-2])
assert len(T)==len(U)==1044
# T_k(cos theta)=cos(k theta); sin(theta)*U_k(cos theta)=sin((k+1)theta).
# These hold from addition formula and the exact recurrences. Products below
# are formed by their own recurrence in a, not by the candidate identity.
pairs=0;coefficient_equalities=0;maxdegree=0;digest=hashlib.sha256();branch={'a_lt_b':0,'a_gt_b':0}
for j in range(args.start,args.end):
 b=2*j+1
 rp,rc=2*U[b-1],twox*U[b-1] # a=0,1:2T_a U_(b-1)
 tp,tc=fmpz_poly([]),2*T[b]  # a=0,1:2U_(a-1) T_b, with U_-1=0
 for a in range(1,523):
  if a%2==0:
   n=a//2;delta=b-a;assert delta!=0
   sign=1 if delta>0 else -1
   rhsr=U[a+b-1]+sign*U[abs(delta)-1]
   rhst=U[a+b-1]-sign*U[abs(delta)-1]
   assert rc==rhsr,(n,j,'radial')
   assert tc==rhst,(n,j,'tangent')
   assert rc.degree()==tc.degree()==a+b-1<=1042
   pairs+=1;coefficient_equalities+=len(rc)+len(tc);maxdegree=max(maxdegree,rc.degree());branch['a_lt_b' if delta>0 else 'a_gt_b']+=1
   digest.update(f'{n},{j},{a+b-1},{sign},{abs(delta)-1};'.encode())
  rp,rc=rc,twox*rc-rp
  tp,tc=tc,twox*tc-tp
assert pairs==261*(args.end-args.start)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_EXACT_CHEBYSHEV_CURRENT_J_RANGE',start_j=args.start,end_j=args.end,n_start=1,n_end_inclusive=261,pairs=pairs,polynomial_identities=2*pairs,coefficient_equalities=coefficient_equalities,maximum_degree=maxdegree,branch_counts=branch,recurrence_degree_limit=1043,index_digest=digest.hexdigest(),proof_sha256=proof,code_sha256=sha(Path(__file__)),seconds=time.monotonic()-t0,scope='Every pair in this exact j range by independent integer polynomial recurrences; full result requires contiguous0..261coverage. No numerical enclosure claim.')
p=D/'evidence'/f'chebyshev_{args.start:03d}_{args.end:03d}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],pairs,coefficient_equalities,out['seconds'])

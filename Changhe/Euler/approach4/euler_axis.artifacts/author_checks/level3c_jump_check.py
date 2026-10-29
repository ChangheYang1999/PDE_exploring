# Lead cross-check of the verifier's exact fifth-derivative jumps of a registered level-3c field (refined_basis/level3c):
# recompute the fifth x-derivative jumps at the verifier's rational angle with scipy's BSpline in float64 and compare them with
# the exact rational jumps. Usage: python3 checks/level3c_jump_check.py NAME (NAME = the verifier's registration alias).
import sys, json, datetime, time, numpy as np
from fractions import Fraction as F
from scipy.interpolate import BSpline
t0=time.time(); name=sys.argv[1]
V='independent_validation/'
NT=V+'research/nested_trial_validation/'
latest=open(NT+'refined_basis/level3c/data/latest.txt').read().strip()
vr=json.load(open(V+latest)); rows={r['name']:r for r in vr['rows']}; row=rows[name]
rec=json.load(open(NT+'data/'+name+'.json'))
N,na=rec['intervals'],rec['angular_count']
raw=np.array([float(F(s)) for s in rec['coefficients']])
m=float(F(row['mu_exact'])); Pl=[1.0,m]
for n in range(1,2*na-1): Pl.append(((2*n+1)*m*Pl[-1]-n*Pl[-2])/(n+1))
coef=np.array([sum(raw[4+i*na+j]*m*Pl[2*j] for j in range(na)) for i in range(N+5)])
br=np.array([float(F(s)) for s in rec['binary_breaks']]); kn=np.concatenate([[br[0]]*5,br,[br[-1]]*5])
vals=BSpline(kn,coef,5).derivative(5)(0.5*(br[1:]+br[:-1])); jumps=vals[1:]-vals[:-1]
ex=np.array([float(F(s)) for s in row['all_jumps_exact']]); d=np.abs(jumps-ex).max(); sc=np.abs(ex).max()
res=[]
def check(n,ok,v=None): res.append(dict(check=n,ok=bool(ok),value=v)); print('PASS' if ok else 'FAIL',n,'' if v is None else v)
check('%d intervals, %d angular functions, breaks strictly increasing on [-7, 7]'%(N,na),br[0]==-7 and br[-1]==7 and np.all(np.diff(br)>0))
check('scipy jumps agree with the exact jumps (max abs diff / max |jump|)',len(ex)==N-1 and d<=1e-8*sc,'%.3e / %.6g'%(d,sc))
nz=int(np.sum(np.abs(jumps)>1e3*d)); i=int(np.argmax(np.abs(jumps)))
check('nonzero jumps (margin 1e3 x discrepancy) and the largest inside (-7, 7)',nz==int(row['nonzero_jumps']) and -7<br[i+1]<7,
      '%d of %d; largest %.10g at x = %.4f (verifier %.10g at x = %.4f)'%(nz,N-1,jumps[i],br[i+1],row['fifth_jump_display'],row['x_display']))
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),name=name,verifier_results=latest,
         all_pass=all(r['ok'] for r in res),wall_seconds=round(time.time()-t0,1),checks=res)
json.dump(out,open('author_checks/level3c_jump_check_output.json','w'),indent=1)
print('all pass',out['all_pass'])

"""Exact finite constants for the first three poles near delta2/5."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
import tuned_cartesian_exact as ce
ROOT=Path('research/216_repeated_near_resonant_poles')
start=time.monotonic();ce.p=lambda n:ce.K(1)-ce.K(2*n)/5
ff={1:ce.sine(ce.p(1),1)};gg={1:ce.poisson(ff[1])}
for n in range(2,11):
    total=ce.F(ce.p(n),{})
    for i in range(1,n):total=total+ce.adv(gg[i],ff[n-i])
    ff[n]=total.scale(ce.K(3)/(2*(n-1)));ff[n].check_sine()
    if n<10:gg[n]=ce.poisson(ff[n])
R=ff[10].sine(1);assert R
source=Path('research/130_period_five_tuning/verification/obstruction_checks.json');old=json.loads(source.read_text());assert sp.cancel(R.as_expr()-sp.sympify(old['coefficients_ascending'][0]))==0
values={}
for k in [2,3]:
    n=5*k;e=ce.sine(ce.p(n)+1,2*k-2);U={};V={}
    for r in range(1,6):
        total=ce.adv(e,ff[r])
        for s in range(1,r):total=total+ce.adv(V[s],ff[r-s])+ce.adv(gg[r-s],U[s])
        U[r]=total.scale(ce.K(3)/(2*(n+r-1)));U[r].check_sine()
        if r<5:V[r]=ce.poisson(U[r])
    values[k]=U[5].sine(2*k-1);assert values[k]
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,delta='2/5',R=str(R.as_expr()),sigma={str(k):str(v.as_expr()) for k,v in values.items()},leading_poles={'10':dict(pole_order=1,coefficient=str((R/20).as_expr())),'15':dict(pole_order=2,coefficient=str((R*values[2]/600).as_expr())),'20':dict(pole_order=3,coefficient=str((R*values[2]*values[3]/24000).as_expr()))},source=dict(path=str(source),sha256=sha256(source.read_bytes()).hexdigest()),actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/checks.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['repeated_near_resonant_poles.py','tuned_cartesian_exact.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
print(json.dumps(record,indent=2))

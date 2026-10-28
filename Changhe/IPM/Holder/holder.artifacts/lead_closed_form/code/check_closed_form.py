"""Rigorous check of the closed-form bounds (Theorem 9.3 of the report):
   R(t) <= kappa/(1-t) + c          on [0, 199/200]   (part 1),
   F_b <= F*,  F_b + 1/2 <= G*      on [199/200, 1)   (part 2),
where F*(a) = 2^(1-a) a_2(a)/a + kappa/(1-a) + c and G*(a) = 2^(1-a) A_a/a + 1/2 + kappa/(1-a) + c.
Part 1.  On each segment [a,b] of consecutive nodes of one group (data/remainders.json), log R <= E, the chord through
(a, log R_a), (b, log R_b) (log-convexity, Theorem 9.2 (i); at a=0 by continuity).  Split [a,b] into N equal rational
pieces [p,q]; exp(E) is monotone on [p,q], hence at most its larger endpoint value, and kappa/(1-t)+c >= kappa/(1-p)+c.
Part 2.  With delta=1-a, delta*F_b(a) = 2 a_2 s^a/a.  We prove 2 a_2 s^a/a < delta*L + kappa + c*delta for L = L_C
and L = L_D on M closed subintervals of [199/200,1] with interval exponent arguments; a_3 uses the positive series
with proved tail of the original upper certificate (code/check_explicit_bounds.py).
All evaluations are 200/256-bit Arb balls at exact rational points or intervals.
Usage: python3 code/check_closed_form.py kappa c N M"""
from pathlib import Path
import json, sys, hashlib
from fractions import Fraction as Fr
from datetime import datetime, timezone
from flint import arb, ctx, fmpq
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'code'))
from check_explicit_bounds import positive_integral
ctx.prec=256
pi=arb.pi()
def q(x): return arb(fmpq(x.numerator,x.denominator))
kap=Fr(sys.argv[1]); c=Fr(sys.argv[2]); N=int(sys.argv[3]); M=int(sys.argv[4])
d=json.loads((ROOT/'data/remainders.json').read_text())['nodes']
groups={}
for r in d:
    for g in r['groups']: groups.setdefault(g,[]).append((Fr(r['alpha']),Fr(r['R'])))
assert groups[0][0][0]==0 and groups[max(groups)][-1][0]==Fr(199,200)
for g in sorted(groups)[:-1]: assert groups[g][-1][0]==groups[g+1][0][0]
worst1=None; nseg=0
for g,L in sorted(groups.items()):
    for (a,Ra),(b,Rb) in zip(L,L[1:]):
        nseg+=1; la=q(Ra).log(); lb=q(Rb).log()
        def ex(t):
            s=(t-a)/(b-a); return ((1-q(s))*la+q(s)*lb).exp()
        for i in range(N):
            p=a+(b-a)*Fr(i,N); qq=a+(b-a)*Fr(i+1,N)
            m=(q(kap)/(1-q(p))+q(c))-arb.max(ex(p),ex(qq))
            if not m>0: print('FAIL part 1',g,a,b,p,qq,m); sys.exit(1)
            if worst1 is None or m.lower()<worst1[0]: worst1=(m.lower(),g,str(p),str(qq))
lo=Fr(199,200); worst2={'C':None,'D':None}
for i in range(M):
    a=q(lo+(1-lo)*Fr(i,M)).union(q(lo+(1-lo)*Fr(i+1,M)))
    a2=arb(2)**(1+a/2)/(pi*(a+2))
    a3=3*arb(2)**a/pi*(3*positive_integral(a,0)-4*positive_integral(a,1))
    b=arb(2)**(a+1)/(3*pi); s=(2*a3+(1-a)*b)/(2*a2)
    lhs=2*a2*s**a/a
    LC=2**(1-a)*a2/a; LD=2**(1-a)*((a+2)/2).gamma()/(2*pi.sqrt()*((a+3)/2).gamma()*a)
    for k,Lk in [('C',LC),('D',LD)]:
        m=(1-a)*Lk+q(kap)+q(c)*(1-a)-lhs
        if not m>0: print('FAIL part 2',k,i,m); sys.exit(1)
        if worst2[k] is None or m.lower()<worst2[k][0]: worst2[k]=(m.lower(),i)
res=dict(time_utc=datetime.now(timezone.utc).isoformat(),kappa=str(kap),c=str(c),pieces_per_segment=N,segments=nseg,
         part1_min_margin_lower=str(worst1[0]),part1_worst=dict(group=worst1[1],piece=[worst1[2],worst1[3]]),
         end_subintervals=M,part2_min_margin_lower={k:str(v[0]) for k,v in worst2.items()},
         source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['data/remainders.json','code/check_closed_form.py','code/check_explicit_bounds.py']},
         verdict='PASS: C_a <= F*(a) and D_a <= G*(a) for every 0<a<1, given Theorems 3.1, 3.5 and the nodal certificates of Theorem 9.2.')
(ROOT/'results/closed_form_check.json').write_text(json.dumps(res,indent=1)+'\n')
print('PASS', {k:res[k] for k in ['kappa','c','segments','part1_min_margin_lower','part2_min_margin_lower']})

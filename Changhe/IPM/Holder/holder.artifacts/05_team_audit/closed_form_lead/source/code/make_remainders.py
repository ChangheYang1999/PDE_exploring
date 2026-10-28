"""Nodal upper values of the regular remainders in the uniform comparison (Theorem 9.2).
Theorem 3.5 family: the nodal upper value is U = L + R, with the explicit local term
  L_C = 2^(1-a) a_2(a)/a = 4*2^(-a/2)/(pi a (a+2))   for C,     L_D = 2^(1-a) A_a/a + 1/2   for D,
and the same remainder R = sec(pi/64) * max over 17 phases of (compact part + exterior part).  We store
R_i >= U_C(a_i) - L_C(a_i), checked to agree with U_D(a_i) - L_D(a_i) up to 1e-8 (the larger is kept).
Theorem 3.7 family: U' = S_a(1/64) + R', and we store R'_i >= U'(a_i) - S_a(1/64).
Values are rounded up to 6 decimals; at a node shared by two groups the larger value is kept, which is valid for
both.  The extra node a=0 (group 0 only) bounds lim_{a->0+} R(a) (code/combine_alpha0.py)."""
from pathlib import Path
import json, math, hashlib
from fractions import Fraction as Fr
from flint import arb, ctx, fmpq
ROOT=Path(__file__).resolve().parents[1]; ctx.prec=200
SRC=['data/uniform_result_thm35_pass3.json','data/uniform_result_thm37_pass3.json','data/remainder_a0.json']
a35,a37,z=[json.loads((ROOT/s).read_text()) for s in SRC]
def q(x): return arb(fmpq(x.numerator,x.denominator))
def LC(x):
    a=q(x); return 4*arb(2)**(-a/2)/(arb.pi()*a*(a+2))
def LD(x):
    a=q(x); A=((a+2)/2).gamma()/(2*arb.pi().sqrt()*((a+3)/2).gamma()); return 2*A*arb(2)**(-a)/a+arb(1)/2
def S(x, d=Fr(1,64)):
    a=q(x); dd=q(d); a2=2**(1+a/2)/(arb.pi()*(a+2)); return 2*a2*dd**a/a+(1+2*dd)**a*dd**2/(2*(1-dd)**2)
def exact_upper(b):
    m,e=b.upper().man_exp(); return Fr(int(m))*Fr(2)**int(e)
def up6(x): return Fr(math.ceil(x*10**6),10**6)
nodes={}
for g in sorted(a35['nodal_upper'],key=int):
    n35=a35['nodal_upper'][g]; n37=a37['nodal_upper'][g]; has37=n37['C']!=n35['C']
    assert n37['D']==n35['D']
    for k in n35['C']:
        x=Fr(k); e=nodes.setdefault(x,{'R':Fr(0),'Rp':None,'groups':[]}); e['groups'].append(int(g))
        rc=exact_upper(arb(n35['C'][k])-LC(x)); rd=exact_upper(arb(n35['D'][k])-LD(x))
        assert abs(rc-rd)<Fr(1,10**8), (k,float(rc),float(rd))
        e['R']=max(e['R'],up6(max(rc,rd)))
        if has37:
            rp=up6(exact_upper(arb(n37['C'][k])-S(x))); e['Rp']=rp if e['Rp'] is None else max(e['Rp'],rp)
assert Fr(0) not in nodes and z['alpha']=='0'
nodes[Fr(0)]={'R':Fr(z['R']),'Rp':None,'groups':[0]}
rows=sorted(nodes.items())
def dec(x): return None if x is None else f"{float(x):.6f}"
for k,e in rows: assert Fr(dec(e['R']))==e['R'] and (e['Rp'] is None or Fr(dec(e['Rp']))==e['Rp'])
out=dict(description=__doc__, source_sha256={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in SRC+['code/make_remainders.py']},
         nodes=[dict(alpha=str(k),groups=e['groups'],R=dec(e['R']),R_thm37=dec(e['Rp'])) for k,e in rows])
(ROOT/'data/remainders.json').write_text(json.dumps(out,indent=1)+'\n')
print(len(rows),'nodes written to data/remainders.json')

"""Exact coefficient-radius audit, independent of unproved remainder formulas."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast, hashlib, json, math, time
import numpy as np
from flint import arb,ctx
D=Path(__file__).resolve().parents[1];ctx.prec=512;start=time.monotonic();u=F(1,2**53)
def a(x):return arb(x.numerator)/x.denominator
minimum=None;count=0
for K in range(2,1025):
    g=K*u/(1-K*u);G=2*K*u/(1-2*K*u);cd=F(K,2)/(1-K*u);cp=F(3*K,2)/(1-(K+2)*u)
    assert G*(1-g)==2*g
    margin=(1-(K+2)*u)/(1-2*K*u)-1
    slack=4*(K+1)-(1+G)*(cd+cp)
    assert margin>=0 and slack>0
    gam=np.nextafter(2*K*float(u)/(1-2*K*float(u)),np.inf)
    assert F.from_float(gam)>=G
    if K>2:assert a(margin)>0
    assert a(slack)>0
    minimum=slack if minimum is None else min(minimum,slack); count+=1
# Load only definitions. There is no invocation of producer main or Certifier.
src=(D/'source/src/midrad.py').read_text(); ns={'__name__':'audited_midrad'};exec(compile(src,'frozen_midrad','exec'),ns)
ast_src=ast.parse((D/'source/src/cert_forcing.py').read_text())
classes=ast.Module(body=[n for n in ast_src.body if isinstance(n,ast.ClassDef) and n.name in ['Cell','BiTM']],type_ignores=[])
exec(compile(ast.fix_missing_locations(classes),'frozen_two_classes','exec'),ns)
ns['mag']=lambda obj: ns['succ'](np.abs(obj.m)+obj.r)
MR,Cell,BiTM=ns['MR'],ns['Cell'],ns['BiTM'];rng=np.random.default_rng(20261021)
tests=[];checked=0
for case,(qs,qp,kind) in enumerate([(1,1,'radius'),(2,2,'mixed'),(3,2,'zero_radius'),(2,1,'subnormal'),(2,2,'subnormal'),(12,8,'radius'),(12,8,'mixed')]):
    sh=(qs+1,qp+1);am=rng.integers(-8,9,sh).astype(float)/16;bm=rng.integers(-8,9,sh).astype(float)/8
    ar=rng.integers(0,8,sh).astype(float)/16;br=rng.integers(0,8,sh).astype(float)/16
    if kind=='radius':am.fill(0);bm.fill(0)
    if kind=='zero_radius':ar.fill(0);br.fill(0)
    if kind=='subnormal':am*=2.0**-530;bm*=2.0**-530;ar*=2.0**-530;br*=2.0**-530
    cl=Cell(0.125,0.0625,qs,qp);res=BiTM(MR(am,ar),0.0,cl)*BiTM(MR(bm,br),0.0,cl)
    AF=[[F.from_float(x) for x in z.ravel()] for z in [am,ar,bm,br]]
    f_am,f_ar,f_bm,f_br=AF
    for q in range(qs+1):
        for p in range(qp+1):
            lo=F(0);hi=F(0)
            for q1 in range(q+1):
                for p1 in range(p+1):
                    i=q1*(qp+1)+p1;j=(q-q1)*(qp+1)+(p-p1)
                    alo,ahi=f_am[i]-f_ar[i],f_am[i]+f_ar[i];blo,bhi=f_bm[j]-f_br[j],f_bm[j]+f_br[j]
                    vals=[alo*blo,alo*bhi,ahi*blo,ahi*bhi];lo+=min(vals);hi+=max(vals)
            m=F.from_float(res.c.m[q,p]);r=F.from_float(res.c.r[q,p]);assert m-r<=lo and m+r>=hi,(case,q,p)
            checked+=1
    tests.append(dict(qs=qs,qp=qp,kind=kind,coefficient_checks=(qs+1)*(qp+1)))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_CONDITIONAL_SCALAR_LOOP_LEMMA',K_values=count,coefficient_cases=tests,coefficient_enclosures=checked,minimum_underflow_slack=str(minimum),seconds=time.monotonic()-start,source_sha256=hashlib.sha256((D/'source/src/cert_forcing.py').read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((D/'MULTIPLICATION_LEMMA.md').read_bytes()).hexdigest(),scope='Full untruncated polynomial coefficient radius only. Does not prove polynomial truncation, remainder operations, actual BLAS, or full forcing bounds. Synthetic finite tests supplement the analytic all-input theorem, not replace it.')
(D/'evidence/product_lemma_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

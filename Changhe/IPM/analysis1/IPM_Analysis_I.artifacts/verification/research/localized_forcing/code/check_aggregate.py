"""Independent exact expansion and Arb composition of all saved forcing rows.

The inputs F0,F1,FL,FL1,FL2 and area are hypotheses, not validated here.
The exact method expands both integrands into nine moment sums; Arb uses
unexpanded per-row formulas. No producer arithmetic routine is imported.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from collections import Counter
import json, hashlib, time
from flint import arb, ctx
from mpmath import iv
D=Path(__file__).resolve().parents[1]; ctx.prec=512; iv.dps=160
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bf(x):return arb(x.numerator)/x.denominator
def box(x):
    return {'lower':str(F(str(x.lower().fmpq()))),'upper':str(F(str(x.upper().fmpq()))),'display':str(x)}
def ivf(x):return iv.mpf(x.numerator)/x.denominator
def ivbox(x):
    out={}
    for name,(sgn,man,exp,bc) in zip(('lower','upper'),x._mpi_):
        q=F((-1 if sgn else 1)*man)*(F(2)**exp);out[name]=str(q)
    return out
t0=time.monotonic(); start=utc()
path=D/'source/runs/forcing/p9_K64_n16_P8_merged.json'; raw=json.loads(path.read_text()); rows=raw['cells']
parts=[json.loads((D/'source'/p).read_text()) for p in raw['merged_from']]
assert sum([p['cells'] for p in parts],[])==rows
assert [c for p in parts for c in p['chunk']]==list(range(4096,4109))
params=['delta','cutoff','KSUB','ntheta','KP','Qs','Qp','theta_max','radial_cells_cover','green','trial','x_star_bracket','code_version','s','cutoff_poly_step']
for p in parts:
    assert p['done'] is True
    for k in params:assert p[k]==raw[k],k
    assert set(p['results'])==set(raw['results'])
keys=[tuple(r[k] for k in ['ci','q','ks','kp']) for r in rows]
assert len(set(keys))==len(keys)==raw['n_subcells_in_support']
assert all(4096<=ci<=4108 and 0<=q<16 and 0<=ks<64 and 0<=kp<8 for ci,q,ks,kp in keys)
# Different algebraic implementation: coefficients of the polynomial in lambda^2.
names=['A','B','C','D','E','F','G','H','J']; exact={k:F(0) for k in names}; balls={l:[arb(0),arb(0)] for l in [1,500]}
first_product_failure=[]
for ind,row in enumerate(rows):
    vals=[F.from_float(row[k]) for k in ['area','F0','F1','FL','FL1','FL2']]
    area,f0,f1,fl,fl1,fl2=vals
    assert all(x>=0 for x in vals)
    terms=[f0*f0,f0*fl,fl*fl,f1*f1,f1*fl1,fl1*fl1,f0*fl2,fl*fl2,fl2*fl2]
    for k,x in zip(names,terms):exact[k]+=area*x
    ba,b0,b1,bl,bl1,bl2=[arb(row[k]) for k in ['area','F0','F1','FL','FL1','FL2']]
    for lam in [1,500]:
        l2=lam*lam; balls[lam][0]+=ba*(l2*(l2*b0+bl)**2+(l2*b1+bl1)**2)
        balls[lam][1]+=ba*(l2*l2*b0+2*l2*bl+bl2)**2
    # Independently verify the fully saved first three Leibniz bounds.
    t0q,t1q,tlq,g0,g1,gl=[F.from_float(row[k]) for k in ['T0','T1','TL','G0','G1','GL']]
    for key,bound,needed in [('F0',f0,t0q*g0),('F1',f1,t0q*g1+t1q*g0),('FL',fl,t0q*gl+2*t1q*g1+g0*tlq)]:
        if bound<needed:first_product_failure.append((ind,key,str(bound-needed)))
assert not first_product_failure,first_product_failure[:5]
results={}
for lam in [1,500]:
    l2=F(lam*lam); A,B,C,V,E,W,G,H,J=[exact[k] for k in names]
    e3=l2**3*A+l2*l2*(2*B+V)+l2*(C+2*E)+W
    e4=l2**4*A+4*l2**3*B+l2*l2*(2*G+4*C)+4*l2*H+J
    b3,b4=balls[lam]
    assert b3.contains(bf(e3)) and b4.contains(bf(e4))
    stored=raw['results'][str(float(lam))]
    s3,s4=F.from_float(stored['I3']),F.from_float(stored['I4'])
    assert s3>=e3 and s4>=e4
    a3,a4=bf(s3),bf(s4)
    # Exact rational exponents; the second method instead takes the twentieth root
    # of the monomial I3^9 I4, through an interval logarithm and exponential.
    norm3=a3.sqrt(); norm4=a4.sqrt(); n31=(a3**(arb(9)/20))*(a4**(arb(1)/20))
    v3,v4=ivf(s3),ivf(s4); vn31=iv.exp(iv.log(v3**9*v4)/20)
    sec=ivbox(vn31); pri=box(n31)
    assert max(F(sec['lower']),F(pri['lower']))<=min(F(sec['upper']),F(pri['upper']))
    for key,b in [('bound_order3',norm3),('bound_order4',norm4),('bound_order_3_1',n31)]:assert arb(stored[key])>=b
    ceilings=['2.84903','2696.18','5.65330'] if lam==1 else ['4.43139','4583.92','8.87175']
    for s,b in zip(ceilings,[norm3,norm4,n31]):assert arb(s)>b
    results[str(lam)]=dict(exact_row_I3=str(e3),exact_row_I4=str(e4),arb_row_I3=box(b3),arb_row_I4=box(b4),saved_I3_minus_exact=str(s3-e3),saved_I4_minus_exact=str(s4-e4),norm3=box(norm3),norm4=box(norm4),norm31=pri,independent_iv_norm31=sec,strict_conditional_ceilings=ceilings)
# Downstream consequences evaluated with the rounded-up conditional bounds.
assert F('0.3181')*F('5.65330')<F('1.7984')
assert F(473)*F('8.87175')<F('4196.4')
# Componentwise gradient bounds must be combined for a Euclidean claim.
grad={}
for ball in ['B94','B3']:
    ss=raw['sup_D_eps'][ball]; v=(arb(ss['1_0'])**2+arb(ss['0_1'])**2).sqrt();grad[ball]=box(v)
old=D.parents[0]/'flow_certificate/evidence/source/cert_resid.py'
new=D/'source/src/cert_resid.py'; line='    self._last_eps = eps          # stash of the per-mode TMs of d_t^i eps_N (used by cert_forcing.py; added shift 4, arithmetic unchanged)\n'
assert new.read_text().count(line)==1
stash_only=new.read_text().replace(line,'')==old.read_text()
assert stash_only
out=dict(start_utc=start,end_utc=utc(),seconds=time.monotonic()-t0,status='CONFIRMED_CONDITIONAL_SAVED_ROW_POSTPROCESSING_ONLY',merged_sha256=sha(path),rows=len(rows),parts=len(parts),exact_moments={k:str(v) for k,v in exact.items()},results=results,grad_norm_upper_from_saved_components=grad,three_Leibniz_formulas_checked=3*len(rows),source_stash_only=stash_only,old_source_sha256=sha(old),new_source_sha256=sha(new),midrad_sha256=sha(D/'source/src/midrad.py'),stale_merged_metadata={k:raw[k] for k in ['partial','n_radial_cells','radial_cells']},scope='Conditional on saved per-cell geometric and derivative bounds. FL1,FL2 have omitted G2F/T2F inputs. No full physical forcing certificate, no endpoint.')
(D/'evidence/aggregate_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['end_utc'],out['status'],'rows',len(rows),'seconds',out['seconds'])
for lam,r in results.items():print(lam,r['norm31']['display'],r['strict_conditional_ceilings'])

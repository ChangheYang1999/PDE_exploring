"""Two-engine disk coverage and exact parent-knot linkage."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
import json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=256;iv.dps=100
part=B/'research/middle_residual/evidence/partition_exact.json';p=json.loads(part.read_text());points=[];last=None
for span in p['spans']:
 a,z=F(span['a_exact']),F(span['b_exact']);n=span['count'];assert n>0 and a<z and span['first_cell']==len(points)
 if last is not None:assert last==a
 points.extend(a+(z-a)*j/n for j in range(n));last=z
points.append(last);assert len(points)==7810 and all(a<z for a,z in zip(points,points[1:]))
g=json.loads((D/'evidence/geometry_arb.json').read_text());raw=json.loads((D/'source/runs/forcing/p9_K64_n16_P8_merged.json').read_text())
def ff(v):return F.from_float(float(v))
def ar(v):return arb(v.numerator)/v.denominator
def ir(v):return iv.mpf(v.numerator)/v.denominator
checks=0
for c in g['cells']:
 i=c['ci'];a,z=points[i:i+2];assert ff(c['tb'])-ff(c['tb_rad'])<=a<=ff(c['tb'])+ff(c['tb_rad']);assert ff(c['next_tb'])-ff(c['next_tb_rad'])<=z<=ff(c['next_tb'])+ff(c['next_tb_rad']);assert z-a<=ff(c['h_up'])<=64*ff(c['hk']);checks+=3
xslo,xshi=map(ff,raw['x_star_bracket']);r3=F(99,2000);th=ff(raw['theta_max']);dth=th/16;w=ff(g['w_up']);assert dth/2<=w
for q in range(16):
 c=dth*F(2*q+1,2);assert c-w<=q*dth and c+w>=(q+1)*dth;checks+=2
A=[ar(xslo-r3)-ar(points[4096]).exp(),ar(points[4109]).exp()-ar(xshi+r3),ar(th)-(ar(r3)/ar(xslo)).asin()]
I=[ir(xslo-r3)-iv.exp(ir(points[4096])),iv.exp(ir(points[4109]))-ir(xshi+r3),iv.sin(ir(th))-ir(r3)/ir(xslo)]
assert 0<th<F(1,100)
assert all(x.lower()>0 for x in A) and all(x.a>0 for x in I)
res=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_EXACT_PARTITION_DISK_COVERAGE',partition_sha256=hashlib.sha256(part.read_bytes()).hexdigest(),exact_points=7810,local_points=[str(v) for v in points[4096:4110]],exact_checks=checks,arb_positive_margins=list(map(str,A)),iv_positive_margins=list(map(str,I)),iv_angular_test='sin(theta_max)>3delta/p_min, with0<theta_max<.01',scope='Disk3delta covered for all source brackets, relative to exact canonical partition. Residual/Green coefficients and full forcing remain OPEN.')
(D/'evidence/coverage.json').write_text(json.dumps(res,indent=2)+'\n');print(res['utc'],res['status'],checks)

"""Manufactured sign certificates, corruption check, and physical derivatives."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,time,hashlib
import mpmath as mp
from exact_temperature_certificate import load_input,coefficients,certify,audit_tree,span_fields
root=Path('research/102_exact_temperature_monotonicity/verification');start=time.monotonic();mp.mp.dps=60
out={'started_utc':datetime.now(timezone.utc).isoformat(),'manufactures':[],'cartesian':[]}
def negative_exists(tree):return 'negative_box' in tree or ('axis' in tree and (negative_exists(tree['left']) or negative_exists(tree['right'])))
for name,rows,shouldpass in [('positive_constant',[[Q(1)]*4],True),('negative_constant',[[Q(-1)]*4],False),('positive_mixed',[[Q(1)]*4,[Q(1,10)]*4,[Q(j,60) for j in range(4)]],True)]:
 data={'basis_exponent':'3','L':'1','degree':3,'knots':['0']*4+['1']*4,'coefficients':[[str(v) for v in row] for row in rows]}
 path=root/(name+'.input.json');path.write_text(json.dumps(data,indent=2)+'\n');d,spans=load_input(path);trees=[];verified=True;stats={'visited':0,'leaves':0,'max_depth':0}
 for span in spans:
  A,B,mats=coefficients(d,span);tree=certify(mats,A,B,0,14,stats);trees.append({'span':span,'tree':tree});verified &= audit_tree(mats,A,B,tree,{'leaves':0})
 assert verified==shouldpass,(name,stats)
 if not shouldpass:assert any(negative_exists(row['tree']) for row in trees)
 cert={'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'spans':trees,'stats':stats};root.joinpath(name+'.certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
 out['manufactures'].append({'name':name,'confirmed':verified,'stats':stats})
 print(name,verified,stats,flush=True)
# Overclamping makes the origin mask insufficient; reject it before signs.
for endpoint in [0,1]:
 knots=(['0']*5+['1']*4) if endpoint==0 else (['0']*4+['1']*5)
 bad={'basis_exponent':'3','L':'1','degree':3,'knots':knots,'coefficients':[['1']*5,['0']*5,['0']+['1/100']*4]}
 bp=root/('overclamped_'+str(endpoint)+'.input.json');bp.write_text(json.dumps(bad,indent=2)+'\n')
 try:load_input(bp)
 except AssertionError:pass
 else:raise AssertionError('overclamped endpoint was accepted')
out['overclamped_endpoints_rejected']=True
# A forged positive leaf is rejected for the negative input.
data,spans=load_input(root/'negative_constant.input.json');A,B,mats=coefficients(data,spans[0]);assert not audit_tree(mats,A,B,{'positive':['1','1']},{'leaves':0});out['forged_positive_leaf_rejected']=True
# Independent physical Cartesian differentiation for the mixed manufacture.
data,spans=load_input(root/'positive_mixed.input.json');A,B,fields=span_fields(data,spans[0])
def mq(q):return mp.mpf(q.numerator)/q.denominator
def ev(p,t,eta):return sum(mq(v)*t**i*eta**j for (i,j),v in p.items())
def F(x,y):
 r2=x*x+y*y;z=(1+r2)**(-mp.mpf(1)/6);t=1-z
 # P1 rho T1(eta)=-y/(10 sqrt(1+r²)), and P2=t/20.
 radial2=(t/r2 if r2 else mp.mpf(1)/6)
 return z**5*(1-y/(10*mp.sqrt(1+r2))+radial2*(y*y-x*x)/20)
for radius in ['0.0001','0.3','2','100']:
 for cx,sy in [(Q(3,5),Q(4,5)),(Q(-5,13),Q(12,13))]:
  r=mp.mpf(radius);x=r*mq(cx);y=r*mq(sy);z=(1+r*r)**(-mp.mpf(1)/6);t=1-z;eta=-y/r;rho=r/mp.sqrt(1+r*r)
  Frep=z**5*(ev(fields[0],t,eta)+rho*ev(fields[1],t,eta));Srep=z**5*(ev(fields[2],t,eta)+rho*ev(fields[3],t,eta));actual=F(x,y);S=2*actual+x*mp.diff(lambda xx:F(xx,y),x)
  eF=abs(Frep-actual);eS=abs(Srep-S);assert max(eF,eS)<mp.mpf('1e-45')
  out['cartesian'].append({'r':radius,'cos':str(cx),'sin':str(sy),'F_error':str(eF),'S_error':str(eS)})
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'manufacture_checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)

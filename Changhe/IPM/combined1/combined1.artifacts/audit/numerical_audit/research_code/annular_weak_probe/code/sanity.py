"""Coordinate-change checks against direct homogeneous radial scaling."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import sys,importlib.util,json,time
from flint import fmpq as Q,fmpq_poly,arb,arb_poly,ctx
path=Path(__file__).with_name('evaluate.py')
spec=importlib.util.spec_from_file_location('annular_evaluation',path)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
ctx.prec=1024;start=time.monotonic();S=a.S;q=a.QPOL;W=a.WPOL

def bernstein(P):
 n=P.degree()
 return [sum((P[k]*Q(comb(j,k),comb(n,k)) for k in range(j+1)),Q(0)) for j in range(n+1)]
assert bernstein(q(1+3*S))==list(map(Q,['0','0','27/2','0','0']))
assert bernstein((q+2*S*q.derivative())(1+3*S))==list(map(Q,['0','27','135/2','-108','0']))
rows=[]
for rs in ['1','7/3','1024']:
 R=Q(rs);lo=a.ar(1/(1+4*R*R));hi=a.ar(1/(1+R*R))
 def integrate(terms):return sum((a.ar(v*R**(-2*k))*a.integral(P,b,lo,hi) for k,v,b,P in terms),arb(0))
 # F=y: direct physical scaling gives pi*R^2/2 integral s*q(s) ds.
 terms=[(k,v,Q(-3-k),a.AU**(k+1)) for k,v in enumerate(q) if v]
 actual=arb.pi()/a.ar(2*R*R)*integrate(terms)
 exact=arb.pi()/2*a.ar(R*R*a.exact_integral(S*q,Q(1),Q(4)))
 assert actual.overlaps(exact)
 # U1=r*sin(theta) corresponds to a=3,b_j=2,Q_j=1.
 actualB=arb.pi()/a.ar(2*R**4)*integrate(a.prepared_terms({Q(1):arb_poly([1])},W))
 exactB=arb.pi()/2*a.ar(a.exact_integral(S*W,Q(1),Q(4)))
 assert actualB.overlaps(exactB)
 # rho_x=1 corresponds to a=4,b_j=2,Q_j=1 and the cosine-zero factor2.
 actualC=arb.pi()/a.ar(2*R**4)*integrate(a.prepared_terms({Q(1):arb_poly([2])},q*q))
 exactC=arb.pi()*a.ar(a.exact_integral(S*q*q,Q(1),Q(4)))
 assert actualC.overlaps(exactC)
 rows.append({'R':rs,'F_y_pairing_overlap':True,'linear_velocity_overlap':True,'constant_gradient_overlap':True,
              'pairing':actual.str(60),'B_squared':actualB.str(60),'C_squared':actualC.str(60)})
 print('R',rs,'all_three_scaling_checks_pass',flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'checks':rows,
 'bernstein_coefficients_confirmed':True,'source_code_sha256':sha256(path.read_bytes()).hexdigest(),
 'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(a.ROOT/'research/annular_weak_probe/verification/scaling_checks_1024.json').write_text(json.dumps(out,indent=2)+'\n')

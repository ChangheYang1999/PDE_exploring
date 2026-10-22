"""Analytically specified polynomials, exact matrix/axis checks and malformed inputs."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import check_coefficients as c
from flint import arb,fmpq,fmpq_mat
counts={};cases=[]
for case,(left,right) in enumerate([(fmpq(-7,3),fmpq(5,7)),(fmpq(0),fmpq(1)),(fmpq(23,32),fmpq(1499,2048))]):
 assert left<right;h=right-left;knots=[left]*8+[right]*8
 Z=fmpq_mat([[fmpq((-1)**(k+m)*(case+1)*(m+1)*(k+2),2**(k+case)) for m in range(260)] for k in range(8)])
 S=[[sum((Z[k,m]*fmpq(math.comb(i,k),math.comb(7,k)) for k in range(i+1)),fmpq(0)) for i in range(8)] for m in range(260)]
 actual,equalities=c.exact_parent(knots,S,7,left,right);assert actual==Z and equalities==64
 A=c.exact_shift(Z,h,fmpq(1,2));H=c.forward_angular_exact(A);inv=c.inverse_angular([[c.a(x) for x in row] for row in H])
 for child,count in [(0,1),(0,11),(1,11),(5,11),(10,11),(1,1)]:
  off=fmpq(child,count);expected=c.exact_shift(Z,h,off);got=c.arb_shift(inv,h*(off-fmpq(1,2)))
  for k in range(8):
   for m in range(260):
    lo,hi=c.endpoints(got[k][m]);assert lo<=expected[k,m]<=hi
    # Direct expansion of the known monomials, outside matrix routines.
    direct=sum((Z[j,m]*math.comb(j,k)*off**(j-k)/h**k for j in range(k,8)),fmpq(0));assert direct==expected[k,m]
 cases.append({'left':str(left),'right':str(right),'exact_coefficients':2080,'shifts':6,'arb_enclosures':12480,'matrix_loop_consistency_equalities':12480})
# Irregular clamped knots, every interior node, distinct from Bernstein cases.
knots=[fmpq(-1)]*8+[fmpq(-3,7),fmpq(1,9),fmpq(5,8)]+[fmpq(2)]*8
node_equalities=0
for ell,(left,right) in enumerate(zip(knots,knots[1:])):
 if left==right:continue
 for i in range(1,10):
  t=left+(right-left)*fmpq(i,10);a=c.cox_values(knots,ell,t);b=c.deboor_weights(knots,ell,t);assert a==b and sum(a,fmpq(0))==1;node_equalities+=8
# Independent direct triangular inverse with exact rationals.
H=c.forward_angular_exact(fmpq_mat([[fmpq((m+2)*(k+5),k+1) for m in range(260)] for k in range(8)]));recovered=[[fmpq(0)]*8 for _ in range(263)]
for m in range(259,0,-1):
 for k in range(8):recovered[m][k]=8*H[m+1][k]-recovered[m+1][k]+recovered[m+2][k]+recovered[m+3][k]
for k in range(8):recovered[0][k]=4*H[0][k]+recovered[2][k]/2
for m in range(260):
 for k in range(8):assert recovered[m][k]==fmpq((m+2)*(k+5),k+1)
faults=[]
def must_fail(name,fun):
 try:fun()
 except (ValueError,AssertionError,OverflowError):faults.append(name)
 else:raise AssertionError(('guard accepted',name))
for value in ('nan','inf','-inf','0x1.00000000000001p+0','0x1p+1'):must_fail('hex:'+value,lambda v=value:c.rathex(v))
for value in (float('nan'),float('inf'),float('-inf')):must_fail('float:'+str(value),lambda v=value:c.ratfloat(v))
for value in ('{"a":1,"a":2}','{"x":NaN}','{"x":Infinity}'):must_fail('json:'+value,lambda v=value:c.strict_json(v))
for value in (arb.nan(),arb.pos_inf(),arb.neg_inf()):must_fail('arb:'+str(value),lambda v=value:c.endpoints(v))
bad={'schema':'arb-dyadic-mid-radius-v1','mid_m':'0','mid_e':'0','rad_m':'-1','rad_e':'0'};must_fail('negative-radius',lambda:c.decode(bad))
for value in ('0x0.0p+0','-0x0.0p+0','0x1.0000000000000p-1022','0x0.0000000000001p-1022','0x1.fffffffffffffp+1023','-0x1.0000000000000p+0'):assert c.rathex(value)==c.ratfloat(float.fromhex(value))
assert c.classify(fmpq(0),fmpq(1),fmpq(0),fmpq(1))=='CONTAINED';assert c.classify(fmpq(-1),fmpq(0),fmpq(0),fmpq(1))=='OVERLAP_ONLY';assert c.classify(fmpq(2),fmpq(3),fmpq(0),fmpq(1))=='DISJOINT'
result={'utc':c.utc(),'status':'PASS_DIAGNOSTIC_ONLY','cases':cases,'irregular_node_component_equalities':node_equalities,'triangular_exact_equalities':2080,'faults_rejected':faults,'source_sha256':c.sha(Path(__file__)),'producer_sha256':c.sha(c.D/'code/check_coefficients.py'),'scope':'Manufactured polynomials and finite guards only. No actual full T membership claim.'};(c.E/'manufactured.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

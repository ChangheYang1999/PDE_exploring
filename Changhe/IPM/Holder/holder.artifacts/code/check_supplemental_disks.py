"""Exact Bernstein certificate for four supplemental disks."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];B=R/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks'
def main():
 d=json.loads((B.parent.parent/'larger_disks/optimal_axis_disks/numerical_values/accepted.json').read_text())
 c0=Q(d['root']['chosen_c']);a0=1-c0
 pairs=[(Q(41,100),Q(3,40)),(Q(29,100),Q(1,25)),(Q(9,40),Q(3,125)),(Q(7,40),Q(7,500))]
 allpairs=[(c0,a0)]+pairs;separations=[]
 for i,(c,a) in enumerate(allpairs):
  assert 0<a<c/2 and c+a<=1
  for j,(cc,aa) in enumerate(allpairs[:i]):
   margin=abs(c-cc)-a-aa;assert margin>=0,(i,j,margin)
   separations.append(dict(i=i,j=j,margin=str(margin)))
 records=[]
 for c,a in pairs:
  p=[c*c-a*a,-4*c,Q(4),4*c,Q(-4)];pieces=[]
  for i in range(256):
   l=Q(3*i,1024);h=Q(3,1024)
   dd=[sum((p[k]*comb(k,j)*l**(k-j)*h**j for k in range(j,5)),Q(0)) for j in range(5)]
   bb=[sum((dd[j]*Q(comb(k,j),comb(4,j)) for j in range(k+1)),Q(0)) for k in range(5)]
   assert min(bb)>0,(c,a,i,min(bb),float(min(bb)))
   pieces.append(dict(left=str(l),right=str(l+h),bernstein=[str(z) for z in bb]))
  records.append(dict(c=str(c),a=str(a),minimum_coefficient=str(min(Q(v) for row in pieces for v in row['bernstein'])),pieces=pieces))
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),result='EXACT_GEOMETRY_PASSED',disks=records,separations=separations,main_disk=dict(c=str(c0),a=str(a0)),sha256={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),B/'PROOF.md',B.parent.parent/'larger_disks/optimal_axis_disks/numerical_values/accepted.json']},scope='Geometry only; no operator endpoint accepted')
 (B/'geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['result'])
 for row in records:print(row['c'],row['a'],row['minimum_coefficient'])
if __name__=='__main__':main()

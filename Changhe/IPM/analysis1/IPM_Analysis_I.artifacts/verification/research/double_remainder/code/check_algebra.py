"""Integer polynomial verification of the IPM kernel and all finite commutators."""
import sys,json,hashlib,math,time
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/double_remainder/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def clean(p):return {k:v for k,v in p.items() if v}
def add(p,q):
 o=p.copy()
 for k,v in q.items():o[k]=o.get(k,0)+v
 return clean(o)
def scale(p,c):return clean({k:c*v for k,v in p.items()})
def shift(p,i,j):return {(a+i,b+j):v for (a,b),v in p.items()}
def derivative(p,axis):
 return {(a-(axis==0),b-(axis==1)):(a if axis==0 else b)*v for (a,b),v in p.items() if (a if axis==0 else b)>0}
def radial(p):return add(shift(p,2,0),shift(p,0,2))
def diff_quotient(p,d,axis):return add(radial(derivative(p,axis)),scale(shift(p,1-axis,axis),-2*d)),d+1
# shift by (1,0) or (0,1) is multiplication by the differentiated coordinate.
def symbol_comm(p,d,axis):
 return add(scale(radial(shift(derivative(p,axis),1-axis,axis)),-1),scale(shift(p,2*(1-axis),2*axis),2*d)),d+1
def kernel_comm(p,d,axis):
 return add(radial(add(p,shift(derivative(p,axis),1-axis,axis))),scale(shift(p,2*(1-axis),2*axis),-2*d)),d+1
def iterate(p,d,operation,word):
 for axis in word:p,d=operation(p,d,axis)
 return p,d

def analytic_kernel(a,b,component):
 n=a+b+2;factor=(-1)**(a+b)*math.factorial(a+b+1);out={}
 for j in range(n+1):
  phase=(b-j)%4;part=0
  if component==0:part={0:1,2:-1}.get(phase,0) # real K2
  else:part={1:1,3:-1}.get(phase,0) # imaginary K1
  if part:out[(n-j,j)]=factor*math.comb(n,j)*part
 return out

def stirling_rows(n):
 rows=[[1]]
 for p in range(n):
  prev=rows[-1];rows.append([(r+1)*(prev[r] if r<len(prev) else 0)+(prev[r-1] if r else 0) for r in range(p+2)])
 return rows

def main():
 start=time.monotonic();kernel_count=0;comm_count=0;hom_count=0
 kbases=[{(2,0):1,(0,2):-1},{(1,1):-2}]
 for a in range(10):
  for b in range(7):
   for comp,base in enumerate(kbases):
    p,d=iterate(base,2,diff_quotient,[0]*a+[1]*b);assert p==analytic_kernel(a,b,comp) and d==a+b+2;kernel_count+=1
 sbases=[{(1,1):1},{(2,0):-1}];rows=[]
 for p in range(4):
  for q in range(4):
   polynomials=[]
   for base in sbases:
    u,d=iterate(base,1,symbol_comm,[0]*p+[1]*q);v,e=iterate(base,1,symbol_comm,[1]*q+[0]*p);w,f=iterate(base,1,symbol_comm,[0]*(p+q))
    assert u==v==scale(w,(-1)**q) and d==e==f==1+p+q;comm_count+=2
    assert all(a+b==2*d for a,b in u);hom_count+=1;polynomials.append(u)
   for base in kbases:
    u,d=iterate(base,2,kernel_comm,[0]*p+[1]*q);v,e=iterate(base,2,kernel_comm,[1]*q+[0]*p);w,f=iterate(base,2,kernel_comm,[0]*(p+q))
    assert u==v==scale(w,(-1)**q) and d==e==f==2+p+q;comm_count+=2
    assert all(a+b==2*d-2 for a,b in u);hom_count+=1
   A0=1 if p==q==0 else sum(abs(c) for u in polynomials for c in u.values())
   rows.append({'p':p,'q':q,'L2_vector_upper_integer':A0,'symbols':[{'denominator_power':1+p+q,'integer_coefficients':[[a,b,c] for (a,b),c in sorted(u.items())]} for u in polynomials]})
 st=stirling_rows(8);st_count=0
 for p,row in enumerate(st):
  for j in range(26):
   assert sum(v*math.factorial(j)//math.factorial(j-r) for r,v in enumerate(row) if r<=j)==(j+1)**p;st_count+=1
 # Exact positive coefficients of (10), so D_pq[a,b]=integer/(2*pi).
 drows=[]
 for p in range(4):
  for q in range(4):
   table=[]
   for a in range(7):
    row=[]
    for b in range(4):
     total=0
     for r in range(p+1):
      for s in range(q+1):
       for i in range(min(a,r)+1):
        for j in range(min(b,s)+1):total+=st[p][r]*st[q][s]*math.comb(a,i)*math.comb(b,j)*(math.factorial(r)//math.factorial(r-i))*(math.factorial(s)//math.factorial(s-j))*math.factorial(r+a-i+s+b-j+1)
     assert total>0;row.append(str(total))
    table.append(row)
   drows.append({'p':p,'q':q,'derivative_numerators_over_2pi':table})
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ALGEBRA','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/double_remainder/PROOF.md'),'checks':{'kernel_derivative_polynomials':kernel_count,'commutator_order_and_homogeneous_sign':comm_count,'homogeneous_degrees':hom_count,'Stirling_monomial_identities':st_count,'positive_kernel_constants':16*7*4},'multiplier_bounds':rows,'kernel_bounds':drows,'seconds':time.monotonic()-start,'scope':'Exact finite polynomial checks supporting the analytic general-order induction, not a formal proof. No sampled Fourier supremum used; sum absolute coefficients gives a rigorous upper bound.'}
 (E/'algebra.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['multiplier_bounds','kernel_bounds']}))
if __name__=='__main__':main()

"""Independent grouped-polynomial identity for a complete compact table."""
from flint import fmpq as Q,fmpq_poly as Poly
NAMES=('linear','ux','uy','rx','ry')
def normalize(s,e,d,B,name,n):
 s,B=Q(s),Q(B)
 assert s>0 and e in (0,1) and type(d)is int and d>=0 and type(n)is int and name in NAMES
 if s==1:d=0
 if d==0:s=Q(1)
 k=int(B.numerator)//int(B.denominator)
 return (s,e,d,B-k,name,n),k

def verify(groups,document):
 source={};target={};seen=set();nonzero=0;polynomials=0
 for _,scale,fields in groups:
  for name in NAMES:
   e,B,d,modes=fields[name];assert Q(d).denominator==1;d=int(d)
   for n,p in modes.items():
    key,k=normalize(scale,e,d,B,name,int(n));bucket=source.setdefault(key,{})
    bucket[k]=bucket.get(k,Poly([]))+p;polynomials+=1
 for row in document['rows']:
  s=Q(row['scale_exact']);e=row['radial_power'];a=Q(row['one_plus_exponent_exact']);d=row['scale_exponent']
  assert type(e)is int and e in (0,1) and type(d)is int and d>=0 and s>0
  assert (s!=1 or d==0) and (d!=0 or s==1)
  factor=(s,e,a,d);assert factor not in seen;seen.add(factor)
  assert set(row['coefficients'])==set(NAMES);row_count=0
  for name,modes in row['coefficients'].items():
   for text,value in modes.items():
    n=int(text);assert str(n)==text;q=Q(value);assert q!=0
    key,k=normalize(s,e,d,a+d,name,n);bucket=target.setdefault(key,{})
    bucket[k]=bucket.get(k,Q(0))+q;nonzero+=1;row_count+=1
  assert row_count>0
 assert len(seen)==document['combined_radial_factors']
 assert nonzero==document['combined_nonzero_coefficients']
 assert polynomials==document['input_polynomials']
 z=Poly([Q(1),Q(-1)]);powers={0:Poly([Q(1)])};checked=0
 for key in set(source)|set(target):
  S,T=source.get(key,{}),target.get(key,{})
  b=min(set(S)|set(T));left=Poly([])
  for k,p in S.items():
   exponent=k-b
   if exponent not in powers:powers[exponent]=z**exponent
   left+=p*powers[exponent]
  coefficients=[Q(0)]*(max(T,default=b)-b+1)
  for k,q in T.items():coefficients[k-b]+=q
  assert left(z)==Poly(coefficients),('compact grouped identity',tuple(map(str,key)))
  checked+=1
 return {'grouped_polynomial_identities':checked,'source_polynomials':polynomials,'table_radial_factors':len(seen),'table_nonzero_coefficients':nonzero,'exact_equality':True}

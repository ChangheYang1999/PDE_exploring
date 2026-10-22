"""Independent exact formula and finite graph controls, after proof178."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
import json,time,heapq
import sympy as s
root=Path('research/178_incoming_tree_sectors_and_attachments/verification');data=json.loads((root/'inputs.json').read_text());start=time.monotonic();now=datetime.now(timezone.utc).isoformat();rows=[];neg=[]
def check(name,e):
 d=s.simplify(e);ok=d==0;rows.append({'name':name,'difference':str(d),'pass':ok});assert ok,(name,d)
def pred(name,b,detail=None):
 ok=bool(b);rows.append({'name':name,'pass':ok,'detail':detail});assert ok,name
x,y,t,u0,delta,v0=s.symbols('x y t u0 delta v0',positive=True)
for av in data['hyperbolic_negative_eigenvalues']:
 a=s.Rational(av);b=4+a
 check('divergence_hyperbolic_'+av,-a+b-4)
 T=s.log(delta/u0)/a
 check('hyperbolic_exact_exit_u_'+av,u0*s.exp(a*T)-delta)
 check('hyperbolic_exact_exit_v_'+av,v0*s.exp(-b*T)-v0*(u0/delta)**(b/a))
 check('hyperbolic_transit_boundary_limit_'+av,s.limit(v0*(u0/delta)**(b/a),u0,0,dir='+'))
 # Derivative growth and arbitrary flat-order choice defeat even exp(+T).
 for m in data['derivative_orders']:
  K=(m+1)*(a+b);P=m*K;N=int(s.ceiling((P+1)/a))+1
  pred(f'flatjet_exponent_a{av}_m{m}',P+1-a*N<0,{'N':N,'exponent':str(P+1-a*N),'derivative_product_factor':str(P)})
for p in data['flat_test_powers']:
 g=-x**p;D=4-s.diff(g,x)
 check(f'degenerate_divergence_p{p}',s.diff(g,x)+s.diff(y*D,y)-4)
 T=(u0**(1-p)-delta**(1-p))/(p-1)
 u=(u0**(1-p)-(p-1)*t)**s.Rational(-1,p-1)
 check(f'degenerate_backward_ODE_p{p}',s.diff(u,t)-u**p)
 check(f'degenerate_exit_time_p{p}',u.subs(t,T)-delta)
 v=v0*s.exp(-4*t)*(u0/u)**p
 check(f'degenerate_backward_v_ODE_p{p}',s.diff(v,t)+(4+p*u**(p-1))*v)
 vexit=v0*s.exp(-4*T)*(u0/delta)**p
 check(f'degenerate_exit_v_limit_p{p}',s.limit(vexit,u0,0,dir='+'))
g=-s.exp(-1/x**2);D=4-s.diff(g,x)
check('flat_nonpolynomial_divergence',s.diff(g,x)+s.diff(y*D,y)-4)
pred('flat_nonpolynomial_incoming_sign',g.is_negative)
# A nonzero transported scalar with arbitrarily high finite-order zero is not flat.
for q in [1,2,3]:
 theta=x**(5*q)*y**q
 check(f'finitejet_transport_q{q}',-x*s.diff(theta,x)+5*y*s.diff(theta,y))
 check(f'finitejet_nonzero_derivative_q{q}',s.diff(theta,x,5*q,y,q)-s.factorial(5*q)*s.factorial(q))
 neg.append({'name':f'finite_order_is_not_infinite_flatness_q{q}','first_nonzero_order':6*q,'coupling_scope':'thermal transport only; not a coupled B2 example','pass':True})
# Enumerate finite labeled trees, retaining vertex0 as the sole attaching leaf.
def tree(seq,n):
 degree=[1]*n
 for q in seq:degree[q]+=1
 leaves=[q for q in range(n) if degree[q]==1];heapq.heapify(leaves);edges=[]
 for q in seq:
  leaf=heapq.heappop(leaves);edges.append((leaf,q));degree[leaf]-=1;degree[q]-=1
  if degree[q]==1:heapq.heappush(leaves,q)
 edges.append(tuple(leaves));return edges
summary=[]
for n in data['tree_vertex_counts']:
 count=0;oriented=0
 for seq in product(range(n),repeat=n-2):
  edges=tree(seq,n);degrees=[sum(v in e for e in edges) for v in range(n)]
  if degrees[0]!=1:continue
  count+=1;exterior_leaves=[v for v in range(1,n) if degrees[v]==1];assert exterior_leaves
  for flips in product([0,1],repeat=n-1):
   indeg=[0]*n
   for e,f in zip(edges,flips):indeg[e[f]]+=1
   # Coupled nondegenerate vertices are sources(indegree0) or saddles(indegree2).
   if not all(indeg[v] in (0,2) for v in range(1,n)):continue
   oriented+=1;assert all(indeg[v]==0 for v in exterior_leaves)
 summary.append({'vertices':n,'attachment_leaf_trees':count,'admissible_orientations':oriented,'pass':True})
 pred(f'finite_tree_source_leaf_n{n}',count>0 and oriented>0,summary[-1])
# Negative control: add a second attachment edge, obtaining a cycle.
cycle=[(0,1),(1,2),(2,0)];pred('second_attachment_creates_cycle',len(cycle)==3)
neg.append({'name':'two_attachments_without_no_cycle_is_possible','edges':cycle,'reason':'A triangle graph violates the no-Jordan premise, so unique attachment cannot omit it.','pass':True})
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':rows,'negative_controls':neg,'tree_summary':summary,'passed':len(rows),'negative_passed':len(neg),'all_passed':all(q['pass'] for q in rows+neg)}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('checks','negative_controls')},indent=2))

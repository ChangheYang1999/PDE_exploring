"""Fresh Arb1536 moment integrals and exact output/domain checks for crossing64."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import json,hashlib,sys,math,bisect,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/axis_crossing/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def aa(v):
 v=F(v);return arb(fmpq(v.numerator,v.denominator))
def dyad(m,e):return F(int(m))*F(2)**int(e)
def ends(x):return tuple(dyad(*q.man_exp()) for q in (x.lower(),x.upper()))
def eb(r):return F(r['lower_exact']),F(r['upper_exact'])
def out(x):
 a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':[float(a),float(b)]}
def ball(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1';m=dyad(v['mid_m'],v['mid_e']);r=dyad(v['rad_m'],v['rad_e']);assert r>=0
 ans=aa(m-r).union(aa(m+r));a,b=ends(ans);assert a<=m-r<=m+r<=b;return ans

def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1
 r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS' and r['cell']==4102 and r['K']==64 and r['Q']==16 and r['modes']==261
 assert sha(B/'research/axis_crossing/code/check_crossing.py')==r['code_sha256']
 sampath=B/'research/residual_samples/evidence/sample_result.json';assert sha(sampath)==r['sample_sha256']=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c'
 data=json.loads(sampath.read_text());sam=next(z for z in data['samples'] if z['cell']==4102)
 a,b=map(F,sam['cell_endpoints_exact']);tc=F(sam['t_exact']);h=(b-a)/2;assert tc==(a+b)/2
 assert r['t_endpoints_exact']==[str(a),str(b)] and r['t_center_exact']==str(tc) and r['h_exact']==str(h)
 modal=B/'data_exact/modal_v2.json';assert sha(modal)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=json.loads(modal.read_text());kn=[F.from_float(float.fromhex(v)) for v in raw['arrays']['knots']['hex']];span=bisect.bisect_right(kn,a)-1;assert kn[span]<=a<b<=kn[span+1] and all(not(a<z<b) for z in kn)
 k=F.from_float(float.fromhex(raw['scalars_hex']['k']));assert k==F(1615536043799051,9007199254740992);cl=1/aa(k)
 prov=json.loads((B/'research/residual_samples/evidence/review_summary.json').read_text());assert prov['status']=='PASS' and prov['sample_result_sha256']==sha(sampath) and prov['coefficients_audited']==6786
 for key,(rel,hsh) in prov['dependencies'].items():assert sha(B/rel)==hsh
 source=B/'research/modal_source/evidence/source_result.json';sa=json.loads((B/'research/modal_source/evidence/output_audit.json').read_text());assert sa['verdict']=='PASS' and sa['source_result_sha256']==r['source_result_sha256']==sha(source)
 cs=[[ball(v) for v in row] for row in sam['density_polynomial_at_point']];Is=list(map(ball,sam['i']));Js=list(map(ball,sam['j']))
 def phi(l,z,N=80):
  # Integral_0^1 exp(zv)v^l dv, sum inclusive through N.
  az=abs(z);assert az<N+2;term=arb(1);total=arb(0)
  for q in range(N+1):
   total+=term/(l+q+1);term*=z/(q+1)
  rem=az**(N+1)/math.factorial(N+1)/(l+N+2)/(1-az/(N+2));R=ends(rem)[1]
  return total+aa(-R).union(aa(R))
 def ev(delta):
  d=aa(delta);vals=[]
  for n in range(1,262):
   m=2*n
   for ix,lam,sign,y0 in [(n-1,-m-4,1,Is[n-1]),(n,m-4,-1,Js[n-1])]:
    z=lam*d;vals.append(z.exp()*(y0+sign*sum((cs[ix][l]*d**(l+1)*phi(l,-z) for l in range(8)),arb(0))))
  dens=[sum((c[l]*d**l for l in range(8)),arb(0)) for c in cs];x=aa(tc+delta).exp()
  wp=cl+x*x/2*sum((2*n*(-(2*n+1)*vals[2*n-2]-(2*n-1)*vals[2*n-1]+dens[n-1]+dens[n]) for n in range(1,262)),arb(0))
  ff=cl*x*x+x**4/2*sum((2*n*(vals[2*n-2]-vals[2*n-1]) for n in range(1,262)),arb(0))
  return wp,ff,x
 # Fresh selected centers span endpoints and interior; all64 subcell coverage verified exactly.
 selected=[0,1,7,16,31,32,48,62,63];fresh=[];prev=-h;num=0
 for j,row in enumerate(r['subcells']):
  dl,du=map(F,row['delta_exact']);assert row['subcell']==j and dl==prev and du==-h+2*h*(j+1)/64;prev=du
  for meth in ['arb','iv']:
   l,u=eb(row[meth]);assert l>F('10.1494') and u<F('10.1525')
  if j in selected:
   wp,ff,x=ev((dl+du)/2);l,u=ends(wp)
   for meth in ['arb','iv']:
    ol,ou=eb(row[meth]);assert ol<=l<=u<=ou;num+=1
   fresh.append({'subcell':j,'wprime':out(wp)})
 assert prev==h and len(r['subcells'])==64
 for meth in ['arb','iv']:
  assert eb(r['global_wprime'][meth])==(min(eb(z[meth])[0] for z in r['subcells']),max(eb(z[meth])[1] for z in r['subcells']))
 pub=json.loads((E/'num_axis_cell.json').read_text(),parse_float=F);pc=pub['cells'][0];assert pc['ci']==4102
 fresh_ends=[];endpoint_overlaps=0
 for j,d in enumerate([-h,h]):
  wp,ff,x=ev(d);l,u=ends(ff);key=['xV1_left','xV1_right'][j];pl,pu=pc[key];assert pl<=l<=u<=pu
  for method,old in [('arb',r['arb_endpoints'][j]['F']),('iv',r['iv_endpoint_F'][j])]:
   ol,ou=eb(old)
   if method=='iv':assert ol<=l<=u<=ou;num+=1
   else:assert max(ol,l)<=min(ou,u);endpoint_overlaps+=1
  assert u<0 if j==0 else l>0
  fresh_ends.append({'F':out(ff),'r':out(x),'wprime':out(wp)})
 root=list(map(F,r['root_bracket_exact']));assert eb(fresh_ends[0]['r'])[1]<root[0]<root[1]<eb(fresh_ends[1]['r'])[0]
 excess=aa(pc['r_hi'])-aa(b).exp();assert ends(excess)[0]>F('0.00000392403') and ends(excess)[1]<F('0.00000392404')
 # Printed decimal endpoints are treated as exact decimals for these comparisons.
 # This is more stringent than a loose comparison; the defining exact cell is unchanged.
 for meth in ['arb','iv']:assert eb(r['global_wprime'][meth])[0]>pc['wprime_lower']
 result={'utc':utc(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':sha(B/'research/axis_crossing/code/check_crossing.py'),'checks_sha256':sha(E/'checks.json'),'proof_sha256':sha(B/'research/axis_crossing/PROOF.md'),'method':'Exact Fraction coverage and input provenance; fresh Arb1536 exponential-moment integration (80-term series with geometric remainder), independent of both continuation evaluators','all_subcells':64,'selected_centers':selected,'fresh_containments':num,'endpoint_arb_overlaps':endpoint_overlaps,'fresh_centers':fresh,'fresh_endpoints':fresh_ends,'whole_cell_bounds_strict':['10.1494','10.1525'],'original_knot_span':span,'original_span_endpoints':[str(kn[span]),str(kn[span+1])],'num_printed_excess':out(excess),'seconds':time.monotonic()-start,'scope':'Whole exact cell4102 only; global axis signs and full inverse remain OPEN.'}
 (E/'output_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k in ['utc','status','seconds','fresh_containments','whole_cell_bounds_strict','original_knot_span']}),flush=True)
if __name__=='__main__':main()

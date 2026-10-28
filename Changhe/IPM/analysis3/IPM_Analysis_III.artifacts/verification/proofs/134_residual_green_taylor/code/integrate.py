"""Original-data interval Taylor integration, one process and one thread."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial,comb
import importlib.util,json,hashlib,time,argparse,bisect
from flint import arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
def load(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
P=load('ipoint',LANE/'proofs/105_residual_norm_point_audit/code/check_points.py')
G=P.G;M=G.M;ANG=P.ANG;aa=P.aa
CENTER=523

def absup(x):return arb(x.abs_upper())
def series(ep,center,half,degree):
 co=[arb(0)]*(degree+1);err=arb(0);h=aa(half)
 for e,p in ep.shift(center).terms.items():
  assert len(p)<=degree+1
  z=aa(e)*h;za=absup(z);ex=[arb(1)]
  for j in range(1,degree+1):ex.append(ex[-1]*z/j)
  for i,v in enumerate(p):
   vh=v*h**i
   for j in range(i,degree+1):co[j]+=vh*ex[j-i]
   if e:err+=absup(vh)*za.exp()*za**(degree-i+1)/factorial(degree-i+1)
 return co,absup(err)

def inner_eps(d,cache):
 H=G.density_eps(d,'inner');fac=(2*aa(d.tm)).exp();J0=list(map(arb,cache['J_inner']));pe=[];qe=[]
 for n in range(1,262):
  ii=H[n-1].particular(2*n+4);jj=P.j_part(H[n],2*n-4)
  hom=J0[n-1]-jj.atzero()
  if n==1:
   c=3/aa(d.k)-1;assert (fac*hom).overlaps(c);hom=c/fac
  jj.addterm(2*n-4,[hom])
  pe.append((jj+ii.scale(-1)).expmul(2).scale(n*fac))
  qe.append(((jj+ii).scale(n)+(H[n]+H[n-1]).scale(F(-1,2))).expmul(2).scale(fac))
 return H,pe,qe

def spline_eps(d,cache,span,center):
 a,b=d.knots[span:span+2];ix=d.spans.index(span);rows=d.poly(span).tolist()
 H=M.shift_rows(rows,aa(center-a)/aa(b-a),aa(b-a));hs=[G.EP({0:[H[j][n] for j in range(8)]}) for n in range(262)]
 il=list(map(arb,cache['I_left'][ix]));jr=list(map(arb,cache['J_right'][ix]));left=aa(center-a);right=aa(b-center);pe=[];qe=[];fac=(2*aa(center)).exp()
 for n in range(1,262):
  aa_n=2*n+4;bb=2*n-4;pi=M.phi_direct(-aa_n*left);pj=M.phi_direct(-bb*right)
  iv=(-aa_n*left).exp()*il[n-1]+sum(((-1)**j*H[j][n-1]*left**(j+1)*pi[j] for j in range(8)),arb(0))
  jv=(-bb*right).exp()*jr[n-1]+sum((H[j][n]*right**(j+1)*pj[j] for j in range(8)),arb(0))
  ii=hs[n-1].particular(aa_n);ii.addterm(-aa_n,[iv-ii.atzero()])
  jj=P.j_part(hs[n],bb);jj.addterm(bb,[jv-jj.atzero()])
  pe.append((jj+ii.scale(-1)).expmul(2).scale(n*fac))
  qe.append(((jj+ii).scale(n)+(hs[n]+hs[n-1]).scale(F(-1,2))).expmul(2).scale(fac))
 return hs,pe,qe

def transpose(v):return [list(x) for x in zip(*v)]
def pack(vectors,kind,angular,stride):
 out=[arb(0)]*((2*CENTER+1)*stride)
 for j,row in enumerate(vectors):
  for n,c in enumerate(row):
   freq=2*(n+1) if angular=='even' else 2*n+1
   out[(CENTER+freq)*stride+j]=c
   out[(CENTER-freq)*stride+j]=c if kind=='cos' else -c
 return arb_poly(out)

def residual_series(hs,ds,ps,qs,ell):
 nh=len(hs);nv=len(ps);degree=nh+nv-2;stride=degree+1
 sd=[[3*v+ds[j][n] for n,v in enumerate(row)] for j,row in enumerate(hs)]
 ct=[[(2*n+1)*v/2 for n,v in enumerate(row)] for row in hs]
 pc=[[v/2 for v in row] for row in ps]
 out=pack(qs,'sin','even',stride)*pack(ct,'cos','odd',stride)-pack(pc,'cos','even',stride)*pack(sd,'sin','odd',stride)
 rows=[]
 for j in range(degree+1):
  row=[out[(2*CENTER+2*n+1)*stride+j] for n in range(523)]
  if j<nh:
   for n in range(262):row[n]+=(3*ell-1)*hs[j][n]+ell*ds[j][n]
  rows.append(row)
 return rows

def window(d,cache,l,r,degree,endcache,mm,mass):
 mid=(l+r)/2;half=(r-l)/2;hh=aa(half)
 if mid<d.tm:he=endcache['inner'][0];shift=mid-d.tm;origin=d.tm;kind='inner'
 elif mid>d.tp:he=endcache['outer'][0];shift=mid-d.tp;origin=d.tp;kind='outer'
 else:
  span=bisect.bisect_right(d.knots,mid)-1;assert d.knots[span]<=l<r<=d.knots[span+1]
  a,b=d.knots[span:span+2];H=M.shift_rows(d.poly(span).tolist(),aa(mid-a)/aa(b-a),aa(b-a))
  he=[G.EP({0:[H[j][n] for j in range(8)]}) for n in range(262)]
  shift=F(0);origin=mid;kind='spline'
 de=[e.deriv() for e in he]
 def batch(eps,deg):
  x=[series(e,shift,half,deg) for e in eps]
  return transpose([v[0] for v in x]),sum((v[1] for v in x),arb(0))
 hd=7 if kind=='spline' else degree
 hs,eh=batch(he,hd);ds,ed=batch(de,hd)
 src=[series(e.expmul(2).scale((2*aa(origin)).exp()),shift,half,degree) for e in he]
 rh,dh,pp,qq,ppt=P.point(d,cache,mid);fac=(2*aa(mid)).exp()
 ps=[[arb(0)]*261 for _ in range(degree+1)];qs=[[arb(0)]*261 for _ in range(degree+1)]
 ep=arb(0);eq=arb(0)
 for n in range(1,262):
  ri,eri=src[n-1];rj,erj=src[n]
  rr=qq[n-1]+fac*(rh[n-1]+rh[n])/2
  ii=[(rr-pp[n-1])/(2*n)];jj=[(rr+pp[n-1])/(2*n)]
  li=-(2*n+2);lj=2*n-2
  for j in range(degree+1):
   ii.append(hh*(li*ii[-1]+ri[j])/(j+1));jj.append(hh*(lj*jj[-1]-rj[j])/(j+1))
  ei=(abs(li)*hh).exp()*(absup(ii[-1])+hh*eri)
  ej=(abs(lj)*hh).exp()*(absup(jj[-1])+hh*erj)
  ep+=n*(ei+ej);eq+=n*(ei+ej)+(eri+erj)/2
  for j in range(degree+1):
   ps[j][n-1]=n*(jj[j]-ii[j]);qs[j][n-1]=n*(jj[j]+ii[j])-(ri[j]+rj[j])/2
  assert ps[1][n-1].overlaps(hh*ppt[n-1])
 hnorm=sum((absup(v) for row in hs for v in row),arb(0));dnorm=sum((absup(v) for row in ds for v in row),arb(0))
 htnorm=sum(((2*n+1)*absup(v) for row in hs for n,v in enumerate(row)),arb(0))
 et=sum(((2*n+1)*series(e,shift,half,hd)[1] for n,e in enumerate(he)),arb(0)) if kind!='spline' else arb(0)
 pnorm=sum((absup(v) for row in ps for v in row),arb(0));qnorm=sum((absup(v) for row in qs for v in row),arb(0))
 ell=1/aa(d.k);eraw=absup(3*ell-1)*eh+absup(ell)*ed
 eraw+=ep*(3*hnorm+dnorm)+pnorm*(3*eh+ed)+ep*(3*eh+ed)
 eraw+=eq*htnorm+qnorm*et+eq*et
 rows=residual_series(hs,ds,ps,qs,ell);norms=[]
 for j,row in enumerate(rows):
  co=P.cofactor(row);gam=ANG.axis(co);q=ANG.quotient(co);sq=gam**2+mass*ANG.normalized_square(q,mm)
  if sq.lower()<0:assert sq.contains(0);sq=arb(0).union(sq.upper())
  norms.append(sq.sqrt())
 err=(1+mass).sqrt()*aa(4*522**4*(2*522+1))*eraw
 var=sum((absup(v) for v in norms[1:]),arb(0))+absup(err)
 lo=max(arb(0),(norms[0]-var).lower());hi=(norms[0]+var).upper()
 beta=F(-1,2) if r<=0 else F(27,4);assert l>=0 or r<=0
 wg=(aa(beta*l)).exp()*(aa(beta*(r-l))).expm1()/aa(beta)
 out={'kind':kind,'left':str(l),'right':str(r),'degree':degree,'energy_lower':G.rec(lo**2*wg),'energy_upper':G.rec(hi**2*wg),'center_norm':G.rec(norms[0]),'variation_bound':G.rec(var),'raw_remainder':G.rec(eraw),'angular_remainder_bound':G.rec(err),'algorithm':'green_ode_taylor','velocity_derivative_overlap':'PASS'}
 sins=P.residual_sines(rh,dh,pp,qq,ell)
 assert all(a.overlaps(b) for a,b in zip(rows[0],sins))
 out['center_overlap']='PASS'
 return out

def inner_tail(d,endcache,T,mass):
 he,pe,qe=endcache['inner'];nu=F(3,2);shift=T-d.tm
 def remove0(ep):return G.EP({e:p for e,p in ep.terms.items() if e!=0})
 def maj(ep,rate):
  ans=arb(0)
  for e,p in ep.shift(shift).terms.items():
   if all(v==0 for v in p):continue
   assert e>=rate,(e,rate)
   if e==rate:
    assert all(v==0 for v in p[1:]);ans+=absup(p[0])
   else:ans+=sum((absup(v)*factorial(j)/aa(e-rate)**j for j,v in enumerate(p)),arb(0))
  return absup(ans)
 def total(eps,rate,theta=False):
  return sum(((2*n+1 if theta else 1)*maj(ep,rate) for n,ep in enumerate(eps)),arb(0))
 hp=[remove0(ep) for ep in he];pp=[remove0(ep) for ep in pe];qp=[remove0(ep) for ep in qe]
 # Exact constant profile and strain are removed as a proven identity.
 for n,ep in enumerate(he):
  assert ep.terms.get(F(0),[arb(0)])==[aa(F(1,4)) if n in (0,1) else arb(0)]
 for n in range(261):
  for ep in (pe[n],qe[n]):
   vv=ep.terms.get(F(0),[arb(0)]);assert len(vv)==1
   assert vv[0].overlaps(3/aa(d.k)-1) if n==0 else vv[0]==0
 ell=1/aa(d.k);c=3*ell-1
 dh=[ep.scale(3)+ep.deriv() for ep in he];dhp=[ep.scale(3)+ep.deriv() for ep in hp]
 lp=[ep.scale(3*ell-1)+ep.deriv().scale(ell) for ep in hp]
 raw=total(lp,nu)+absup(c)*(total(dhp,nu)+total(hp,nu,True))+total(pp,nu)*total(dh,0)+total(qp,nu)*total(he,0,True)
 bound=(1+mass)*aa(4*522**4*1045)**2*raw**2*aa(-T/2).exp()/aa(2*nu-F(1,2))
 return {'T':str(T),'rate':str(nu),'raw_bound':G.rec(raw),'energy_upper':G.rec(bound),'energy_lower':G.rec(arb(0))}

def partition(d,Tleft=F(-40),Tright=F(20)):
 cuts=set([Tleft,Tright,F(0)]+d.knots)
 x=d.tm;step=F(1,125)
 while x>Tleft:
  x=max(Tleft,x-step);cuts.add(x);step=min(F(1,2),2*step)
 x=d.tp;step=F(1,125)
 while x<Tright:
  x=min(Tright,x+step);cuts.add(x);step=min(F(1,10),2*step)
 return list(zip(sorted(cuts)[:-1],sorted(cuts)[1:]))

def production(args,d,cache,endcache,mm,mass,start):
 target=ROOT/'evidence'/args.tag;target.mkdir(exist_ok=True)
 source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
 assert hashlib.sha256(source.read_bytes()).hexdigest()==d.sha
 outer_path=LANE/'proofs/122_full_regular_far_tail/evidence/check.json'
 outer_data=json.loads(outer_path.read_text());outer=next(r['full_Y'] for r in outer_data['rows'] if F(r['T'])==20)
 bounds=partition(d);inner=inner_tail(d,endcache,F(-40),mass)
 meta={'date_started':datetime.now(timezone.utc).isoformat(),'status':'IN_PROGRESS','bits':args.bits,'degree':args.degree,'source_sha256':d.sha,'source_path':str(source),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'green_sha256':hashlib.sha256(G.CACHE.read_bytes()).hexdigest(),'scalar_sha256':hashlib.sha256(M.SCALAR.read_bytes()).hexdigest(),'outer_source_sha256':hashlib.sha256(outer_path.read_bytes()).hexdigest(),'inner_tail':inner,'outer_tail':outer,'base_partition':[[str(a),str(b)] for a,b in bounds]}
 meta_path=target/'metadata.json';journal=target/'leaves.jsonl';done={}
 if journal.exists():
  old=json.loads(meta_path.read_text())
  if 'seed_provenance' in old:meta['seed_provenance']=old['seed_provenance']
  for key in ('bits','degree','source_sha256','code_sha256','proof_sha256','green_sha256','scalar_sha256','outer_source_sha256','base_partition'):assert old[key]==meta[key],key
  for line in journal.read_text().splitlines():
   row=json.loads(line);done[row['leaf_id']]=row
 else:meta_path.write_text(json.dumps(meta,indent=2)+'\n')
 count=len(done)
 def walk(l,r,leaf_id,depth=0):
  nonlocal count
  if leaf_id in done:return
  # Existing descendants mean a previous shift had already subdivided this leaf.
  descendants=any(key.startswith(leaf_id+'.') for key in done)
  if not descendants:
   row=window(d,cache,l,r,args.degree,endcache,mm,mass)
   err=arb(row['angular_remainder_bound']['ball']);cn=arb(row['center_norm']['ball'])
   accepted = err < max(arb('1e-40'),cn*arb('0.005')) or aa(F(row['energy_upper']['upper_exact'])) < arb('0.000001')
   if accepted or depth>=12:
    assert accepted
    row['leaf_id']=leaf_id;row['date']=datetime.now(timezone.utc).isoformat();row['depth']=depth
    with journal.open('a') as f:f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush();os.fsync(f.fileno())
    done[leaf_id]=row;count+=1
    print(json.dumps({'date':row['date'],'leaf':leaf_id,'count':count,'left':str(l),'right':str(r),'kind':row['kind'],'energy_upper':row['energy_upper']['ball'],'seconds':time.monotonic()-start}),flush=True)
    return
  mid=(l+r)/2;walk(l,mid,leaf_id+'.0',depth+1);walk(mid,r,leaf_id+'.1',depth+1)
 for index,(l,r) in enumerate(bounds):walk(l,r,str(index))
 rows=sorted(done.values(),key=lambda row:F(row['left']))
 assert F(rows[0]['left'])==-40 and F(rows[-1]['right'])==20
 assert all(F(a['right'])==F(b['left']) for a,b in zip(rows,rows[1:]))
 sums={side:sum((F(row['energy_'+side][side+'_exact']) for row in rows),F(0)) for side in ('lower','upper')}
 for tail in (inner,outer):
  for side in ('lower','upper'):sums[side]+=F(tail['energy_'+side][side+'_exact'])
 meta.update(status='COMPUTED_PENDING_AUDIT',date_finished=datetime.now(timezone.utc).isoformat(),leaf_count=len(rows),seconds=time.monotonic()-start,energy_sum_lower_exact=str(sums['lower']),energy_sum_upper_exact=str(sums['upper']),norm_lower=G.rec(aa(sums['lower']).sqrt()),norm_upper=G.rec(aa(sums['upper']).sqrt()),journal_sha256=hashlib.sha256(journal.read_bytes()).hexdigest())
 meta_path.write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps({'status':meta['status'],'norm_lower':meta['norm_lower']['ball'],'norm_upper':meta['norm_upper']['ball'],'seconds':meta['seconds']}),flush=True)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=28);ap.add_argument('--bits',type=int,default=384);ap.add_argument('--pilot',default='0,4,8,10,15,-10');ap.add_argument('--production',action='store_true');ap.add_argument('--tag',default='production_28');args=ap.parse_args()
 ctx.prec=args.bits;ctx.threads=1;start=time.monotonic();M.SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz';d=M.Data();cache=G.load_cache(d);endcache={'inner':inner_eps(d,cache),'outer':(G.density_eps(d,'outer'),*G.outer_eps(d,cache)[:2])};mm=ANG.moments(1044);mass=ANG.beta_mass();results=[]
 if args.production:return production(args,d,cache,endcache,mm,mass,start)
 for st in args.pilot.split(','):
  t=F(st)
  if d.tm<t<d.tp:
   span=bisect.bisect_right(d.knots,t)-1;l,r=d.knots[span:span+2]
   if l<0<r:l=F(0) if t>=0 else l;r=r if t>=0 else F(0)
  else:l=t-F(1,20);r=t+F(1,20)
  row=window(d,cache,l,r,args.degree,endcache,mm,mass);results.append(row)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'t':st,'energy_lo':row['energy_lower']['ball'],'energy_hi':row['energy_upper']['ball'],'center':row['center_norm']['ball'],'variation':row['variation_bound']['ball'],'remainder':row['angular_remainder_bound']['ball'],'seconds':time.monotonic()-start}),flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'PILOT_PENDING_AUDIT','bits':args.bits,'degree':args.degree,'source_sha256':d.sha,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':results,'seconds':time.monotonic()-start}
 (ROOT/'evidence'/f'pilot_{args.degree}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()

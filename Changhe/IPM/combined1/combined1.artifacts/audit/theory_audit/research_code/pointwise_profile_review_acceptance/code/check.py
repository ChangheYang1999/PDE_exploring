from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx,fmpq
from geometry import velocity,dot,prod,add
B=Path(__file__).resolve().parents[1];start=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for rel,h in m['inputs'].items():assert sha(B/rel)==h,rel
p=json.loads((B/'data/parameters.json').read_text());ctx.prec=p['precision_bits']
peer=json.loads((B/'source/peer_result.json').read_text());orig=json.loads((B/'source/T4_415_result.json').read_text());copy=json.loads((B/'source/peer_copy_result.json').read_text());capold=json.loads((B/'source/T4_422_result.json').read_text());shold=json.loads((B/'source/T4_414_result.json').read_text())
def clean(j):return {k:([{k1:v1 for k1,v1 in r.items() if k1!='elapsed_s'} for r in v] if k=='rows' else v) for k,v in j.items() if k not in ['utc','elapsed_s']}
assert clean(orig)==clean(copy)
assert sha(B/'source/restored_review414.md')=='221b113543dc815315d771563c9c0b9618919663db794720f55887169221ab51'
assert sha(B/'source/peer_check.py')=='0604be55a73822bf978d1422ad9de731c72e00fed22ce4610b4ecc69e7ab281d'
assert sha(B/'source/peer_log.txt')=='b319c3bacf128d4b3691098f7eb10d7e30322da2697553fc5f57959e401364c4'
assert sha(B/'source/peer_result.json')=='59034a6c3f429a5c68e0809b7ad2e8ff1b1c5822bb031af90ff98c070c06765a'
checks=[]
def require(name,b,val=None):
 assert b,name
 checks.append({'claim':name,'value':str(val) if val is not None else None})
def ar(x):
 if isinstance(x,fmpq):return arb(x.p)/int(x.q)
 x=Q(str(x));return arb(x.numerator)/x.denominator
c=Q(p['c']);q=1/c-4;delta=1-1/c;D=5*c-1;alpha=-2*q-2;E=Q(p['E']);S=2*delta**2/(alpha*(alpha+delta)*(alpha+2*delta));pi=arb.pi()
assert E==Q(93,250) and S==1/alpha-2/(alpha+delta)+1/(alpha+2*delta)
trip=lambda v:((v[0]+v[2])/2,(v[0]-v[2])/2,v[1])
def value(t,cc,ss):return t[0]+t[1]*cc+t[2]*ss
def arc_lower(t,cl,sl,cr,sr):
 ll=value(t,cl,sl);rr=value(t,cr,sr)
 if -t[1]*sl+t[2]*cl>0 or -t[1]*sr+t[2]*cr<0:return min(ll.lower(),rr.lower())
 return (t[0]-(t[1]*t[1]+t[2]*t[2]).sqrt()).lower()
def eval_sine(f,x,derivative=False):return sum((ar(v)*(n*(n*x).cos() if derivative else (n*x).sin()) for n,v in f.items()),arb(0))
def den_coeff(f):
 out=prod(f,f,True)
 out={n:v*fmpq(str(q*q)) for n,v in out.items()}
 for n,v in prod({n:n*v for n,v in f.items()},{n:n*v for n,v in f.items()}).items():add(out,n,v)
 return out
rows=[];total_rect=0;den_cells=0
for name in ['007','013','014']:
 tick=time.monotonic();ep=json.loads((B/f'data/{name}_endpoint.json').read_text());a={int(n):fmpq(v) for n,v in ep['F12'].items()};pp={int(n):fmpq(v) for n,v in ep['P'].items()};f2={n:100000*v for n,v in pp.items()};va=velocity(a,fmpq(str(q+2)));vb=velocity(f2,fmpq(str(q+2)));ff=[dot(va,va),dot(va,vb),dot(vb,vb)]
 degrees=sorted(set().union(*[set(t) for t in ff]));require(name+' even finite degrees',all(n%2==0 for n in degrees) and max(degrees)<=44)
 co={n:tuple(ar(x) for x in trip([t.get(n,fmpq(0)) for t in ff])) for n in degrees}
 cells=peer['C'][name]['cells'];NN=p['peer_theta_cells'];hh=pi/(4*NN)
 require(name+' peer theta/witness mesh',peer['C']['theta_cells']==NN and peer['C']['witness_cells']==NN)
 require(name+' exact coverage',Q(cells[0]['cell'][0])==Q(-1,2) and Q(cells[-1]['cell'][1])==Q(1,2) and all(Q(l['cell'][1])==Q(r['cell'][0]) for l,r in zip(cells,cells[1:])))
 require(name+' projective cells',len(cells)==17 and all(Q(t['cell'][1])-Q(t['cell'][0])==Q(1,12*2**t['depth']) for t in cells))
 fj=[];fpj=[];fppj=[]
 for j in range(NN):
  th=(2*j+1)*hh;interval=(th-hh).union(th+hh);sc={n:(n*th).sin_cos() for n in degrees};ci={n:(n*interval).cos() for n in degrees}
  fj.append(tuple(sum((co[n][k]*sc[n][1] for n in degrees),arb(0)) for k in range(3)))
  fpj.append(tuple(sum((-n*co[n][k]*sc[n][0] for n in degrees),arb(0)) for k in range(3)))
  fppj.append(tuple(sum((-n*n*co[n][k]*ci[n] for n in degrees),arb(0)) for k in range(3)))
 cert=[]
 for cell in cells:
  l,r=map(Q,cell['cell']);require(name+' arc width',0<r-l<Q(1,2));dw=cell['witness'];require(name+' witness',0<=dw<=NN)
  phi=dw*pi/(2*NN);v=[(ar(q)*eval_sine(f,phi),eval_sine(f,phi,True)) for f in [a,f2]]
  base=tuple(ar(E*E)*z for z in trip([v[0][0]**2+v[0][1]**2,v[0][0]*v[1][0]+v[0][1]*v[1][1],v[1][0]**2+v[1][1]**2]))
  left=2*pi*ar(l);right=2*pi*ar(r);sl,cl=left.sin_cos();sr,cr=right.sin_cos();sa,ca=left.union(right).sin_cos();minimum=None;argmin=None
  for j in range(NN):
   up=value(fppj[j],ca,sa).upper();rem=hh*hh*max(up,arb(0))/2
   lower=min(arc_lower(tuple(base[k]-fj[j][k]-sign*hh*fpj[j][k] for k in range(3)),cl,sl,cr,sr) for sign in [-1,1])-rem
   assert lower>0,(name,cell,j,lower)
   if minimum is None or lower.lower()<minimum:minimum=lower.lower();argmin=j
  total_rect+=NN
  require(name+' directed cell margin',minimum>ar(cell['min_gap_lower']),minimum)
  require(name+' minimum theta index',argmin==cell['argmin_theta_cell'])
  cert.append({'left_pi':str(l),'right_pi':str(r),'minimum':minimum.str(28),'argmin':argmin})
 # New lower coefficient: exact rational selected direction and rigorous denominator maximum.
 z=Q(peer['D'][name]['w']);theta=ar(peer['D'][name]['theta0']);f={n:a.get(n,fmpq(0))+fmpq(str(z))*f2.get(n,fmpq(0)) for n in set(a)|set(f2)}
 vv=velocity(f,fmpq(str(q+2)));num=dot(vv,vv);numerator=sum((ar(v)*(n*theta).cos() for n,v in num.items()),arb(0)).sqrt();dc=den_coeff(f);require(name+' denominator even degrees',all(n%2==0 for n in dc))
 h=pi/(4*p['denominator_cells']);m2=sum((n*n*abs(ar(v)) for n,v in dc.items()),arb(0));gup=arb(0)
 for j in range(p['denominator_cells']):
  x=(2*j+1)*h;sc={n:(n*x).sin_cos() for n in dc};v=sum((ar(b)*sc[n][1] for n,b in dc.items()),arb(0));dv=sum((-n*ar(b)*sc[n][0] for n,b in dc.items()),arb(0));upper=(v+h*abs(dv)+h*h*m2/2).upper();gup=max(gup,upper)
 den_cells+=p['denominator_cells'];lo=numerator/gup.sqrt();require(name+' optimal coefficient lower',lo>ar(p['lower_coefficients'][name]),lo);require(name+' coefficient room',ar(E)-lo<ar(peer['D'][name]['margin_93_250_minus_lower_upper']),ar(E)-lo)
 # Exact Fourier projection and all cap/room bounds.
 aa={n:Q(str(v)) for n,v in a.items()};ps={n:Q(str(v)) for n,v in pp.items()};modes=set(aa)|set(ps);proj=sum(aa.get(n,0)**2 for n in modes)-sum(aa.get(n,0)*ps.get(n,0) for n in modes)**2/sum(ps.get(n,0)**2 for n in modes)
 b=(pi*ar(proj)).sqrt()/(4*ar(c));g0=sum(int(n)*Q(v) for n,v in ep['Theta0'].items());tt=ar(p['angles'][name]);av=eval_sine(a,tt);ad=eval_sine(a,tt,True);pv=eval_sine(pp,tt);pd=eval_sine(pp,tt,True);Phi=abs(ar(q)*(av*pd-ad*pv))/(4*ar(c)*(ar(q*q)*pv*pv+pd*pd).sqrt());H=ar(p['H0'][name]);require(name+' H lower',Phi>H)
 old=next(r for r in capold['rows'] if r['candidate']==name);vv0=ar(next(r for r in shold['rows'] if r['candidate']==name)['v0_exact']);pref=(2*pi).sqrt()*H/(ar(D)*b);rzero=(pref*ar(E*g0))**ar(1/delta);rvel=(pref*(vv0+ar(E*g0)))**ar(1/delta);cap=b*rzero**ar(q+1)*ar(S).sqrt();capv=b*rvel**ar(q+1)*ar(S).sqrt();pr=peer['F'][name]
 require(name+' original cap enclosure',ar(old['cap_enclosure']['lower_exact'])<cap<ar(old['cap_enclosure']['upper_exact']))
 require(name+' peer cap enclosure',ar(pr['cap_lower'])<cap<ar(pr['cap_upper']),cap)
 require(name+' peer r0 lower',rzero>ar(pr['r0_lower']),rzero)
 require(name+' peer optimistic V cap',capv<ar(pr['cap_V_lead_upper']),capv)
 targetrows={}
 Sigma=ar('1/2')+arb(2)**ar(3-q)+arb(2)**ar(1-q)+arb(2)**ar(2-q)/ar(q+5)
 for key,beta in p['betas'].items():
  beta=ar(beta);ratio=cap/beta;ratioV=capv/beta;crit=ar(D)*b/((2*pi).sqrt()*H*ar(g0))*(b*ar(S).sqrt()/beta)**ar(delta/(-q-1));row=old['targets'][key];prr=pr['targets'][key]
  require(name+' '+key+' original ratio',ar(row['ratio_enclosure']['lower_exact'])<ratio<ar(row['ratio_enclosure']['upper_exact']))
  require(name+' '+key+' peer ratio',ar(prr['ratio_lower'])<ratio<ar(prr['ratio_upper']))
  require(name+' '+key+' peer V ratio',ratioV<ar(prr['ratio_V_lead_upper']))
  require(name+' '+key+' peer critical',crit<ar(prr['Ecrit_upper']))
  require(name+' '+key+' flags',bool(ratio>1)==row['ceiling_exceeds_target'] and bool(ratio<1)==row['ceiling_below_target'] and bool(ratio>1)==bool(crit>ar(E)))
  critPhi=crit*H/Phi;room=critPhi-ar(E);require(name+' '+key+' room upper',room<ar(prr['room_93_250_Phi_V0_upper']))
  require(name+' '+key+' V room upper',room-vv0/ar(g0)<ar(prr['room_93_250_Phi_Vlead_upper']))
  rb=(b/(beta*ar(alpha).sqrt()))**ar(1/(-q-1));jlb=Sigma*(5/rb)**ar(delta)
  if key in p['remainder_ratio_lower']:
   require(name+' '+key+' remainder factor',room>0 and jlb/room>ar(p['remainder_ratio_lower'][key][name]),jlb/room)
  else:require(name+' negative graded room',room<0,room)
  targetrows[key]={'ratio':ratio.str(28),'ratio_with_V0':ratioV.str(28),'critical_E':crit.str(28),'room_Phi':room.str(28),'J_over_H_lower':jlb.str(28)}
 require(name+' peer original finite checks',all(pr['checks'].values()))
 rows.append({'candidate':name,'projective_cells':len(cells),'rectangles':len(cells)*NN,'cells':cert,'coefficient_lower':lo.str(32),'cap':cap.str(32),'cap_with_V0':capv.str(32),'targets':targetrows,'elapsed_s':time.monotonic()-tick})
 print('PASS',name,'rectangles',len(cells)*NN,'coefficient',lo.str(18),'seconds',time.monotonic()-tick,flush=True)
require('peer cap count',peer['F']['checks_total']==114)
require('all rectangles',total_rect==78336)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'angular_rectangles':total_rect,'denominator_cells':den_cells,'rows':rows,'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'peer_review_sha256':sha(B/'source/review.md'),'foreign_code_executed':False,'verdict':'CONFIRMED angular and conditional radial claims;415 and422 AUDITED, with lower-coefficient scope restricted to the angular inequality'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print('ALL PASS',len(checks),total_rect,den_cells,r['utc'],r['elapsed_s'],flush=True)

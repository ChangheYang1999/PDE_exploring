"""Independent exact scalar audit of both proposed T2-R3 boxes."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/l2_family_floor/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import ar
from floor import distance
from pipeline import digest
ctx.prec=512;start=time.monotonic();pi=arb.pi();smax=ar(Q(1,1024))
m1=pi.sqrt()/2*((1-smax)/2).gamma();wc=ar(Q(8,5))*arb(5).sqrt()*arb(6)**ar(Q(-3,5))
k1u=m1;k1w=m1+ar(Q(8,5));cru=ar(Q(3,2))*m1;crw=cru+ar(Q(32,15));c8=1+wc*3*pi/4;dtop=1+wc*pi/2
q=1/(2*pi.sqrt());ps=arb(2)**smax*(1+smax).sqrt()*q
Pw=ps*(1+wc*m1*smax)+wc*m1*smax*q
Ap=ar(Q(4,5))*q+q*(1+4*wc*m1*smax)+2*Pw;Bp=ar(Q(9,5))*Pw
assert Ap>q+ps and Ap+Bp<ar(Q(8,5))
parts={};hashes={}
for label in ['G0','G1','P2','Q3']:
 path=ROOT/f'research/whole_plane_norms/verification/d2_{label}_ball_2048.json';d=json.loads(path.read_text())
 parts[label]=(arb(d['norm_lower_ball']),arb(d['norm_upper_ball']));hashes[label]=digest(path)
fp=ROOT/'research/sector_audit/verification/stationary_principal.json';d=json.loads(fp.read_text());delta=1-1/Q(d['cl'])
E4=(pi*ar(sum((Q(v)**2 for v in d['branches'][3]['forcing_sin'].values()),Q(0)))).sqrt()
wp=ROOT/'research/point_witness/verification/cartesian_witnesses.json';witness=json.loads(wp.read_text())['rows']
rows=[]
for name,w1,w2,mu,Cprime,isq,R,eta,bl in [
 ('FW-T-T4L2-sharp-v1',16384,262144,Q(259,1000),401,88,Q(147,200000),Q(76219,10**9),Q(1037,10000)),
 ('FW-T-T4L2-sharpw-v1',32768,1048576,Q(97,250),397,72,Q(1351,10**6),Q(4207,2*10**7),Q(1557,10000))]:
 s=Q(1,isq**2);a=Q(1,2)-mu;b=-Q(347,10);c=Q(-5);dd=w1*(Q(9,10)-mu)-40;e=-3*w1;f=w2*(2-mu)
 minors=[a,a*dd-b*b,a*dd*f+2*b*c*e-a*e*e-dd*c*c-f*b*b];assert all(x>0 for x in minors)
 K00=dtop*2+c8*6+(crw+2*k1w)*24+k1w*32;K01=k1w*(160+160)/arb(w1).sqrt();K02=k1w*2048/arb(w2).sqrt()
 K11=2+6+(cru+k1u)*24+k1u*32;K12=k1u*80*arb(w1).sqrt()/arb(w2).sqrt();K22=2+6+cru*24+k1u*32
 krows=[K00+(K01+K02)/2,K11+(K01+K12)/2,K22+(K02+K12)/2];assert all(v<Cprime for v in krows)
 beta=mu-Cprime*s-Q(8,5)*R*isq;assert beta>=bl and eta<=bl*R
 cs=1/(4*pi*ar(s)*(1+ar(s))).sqrt();contract=cs*ar(R)/2;slope=ar(Q(7,10))-cs*ar(R);assert contract<1 and slope>0
 lower=((1-ar(Q(48,25)*s))**2*parts['P2'][0]**2+w1*parts['G1'][0]**2+w2*parts['G0'][0]**2).sqrt()
 Eup=(parts['P2'][1]**2+w1*parts['G1'][1]**2+w2*parts['G0'][1]**2).sqrt();Cw=max(1+Q(32,25)+w1,1+Q(w2,w1))
 upper=Eup**(1-ar(s))*(2*parts['Q3'][1]**2+ar(Cw)*Eup**2)**ar(s/2)+ar(Q(48,25)*s)*Eup
 points=[]
 for row in witness:
  assert Q(row['point'][0])==0 and abs(Q(row['point'][1]))>=Q(1,2)
  fs=row['fields'];c0r=ar(R)/(4*pi*(1+ar(s))).sqrt();c1sr=ar(R)/(4*(pi*ar(s)*(1+ar(s))).sqrt())
  gap=abs(arb(fs['residual']))-(c1sr*arb(fs['velocity_norm'])+c0r*(1+arb(fs['gradient_norm']))+c0r*c1sr)
  points.append({'candidate':row['candidate'],'point':row['point'],'symmetric_gap':gap.str(65),'excluded':bool(gap>0)})
 def ratio(K):return arb(w2).sqrt()*E4*distance(4,K,delta)[0]/arb(2).sqrt()/ar(eta)
 low,high=75,100000;assert ratio(low)>1 and ratio(high)<1
 while high-low>1:
  mid=(low+high)//2;v=ratio(mid)
  if v>1:low=mid
  elif v<1:high=mid
  else:raise ArithmeticError('boundary interval overlaps one')
 # Direct finite product confirms the faster gamma-ratio evaluation at the boundary.
 direct=arb(w2).sqrt()*E4*distance(4,low,delta,True)[0]/arb(2).sqrt()/ar(eta)
 assert direct.overlaps(ratio(low)) and direct>1
 row={'framework':name,'w1':w1,'w2':w2,'s':str(s),'R':str(R),'eta':str(eta),'mu':str(mu),'Cprime':Cprime,
      'base_minors':list(map(str,minors)),'commutator_row_sums':[x.str(70) for x in krows], 'beta':str(beta),
      'beta_lower':str(bl),'self_map_slack':str(bl*R-eta),'contraction':contract.str(70),'slope_margin':slope.str(70),
      'raw_conversion_constant':str(Cw),'d2_X_lower':lower.str(70),'d2_X_upper':upper.str(70),'d2_lower_ratio':(lower/ar(eta)).str(70),
      'point_tests':points,'four_branch_last_excluded_degree':low,'four_branch_first_inconclusive_degree':high,
      'four_branch_last_ratio':ratio(low).str(65),'four_branch_next_ratio':ratio(high).str(65),'direct_product_checked':True}
 rows.append(row);print(name,'beta',beta,'Xlower',lower.str(20),'B4last',low,flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'rows':rows,'component_sha256':hashes,
     'code_sha256':digest(Path(__file__)),'point_source_sha256':digest(wp),'sector_source_sha256':digest(fp),
     'rough_bound':(Ap+Bp).str(70),'elapsed_seconds':time.monotonic()-start,
     'scope':'Scalar audit conditional on the analytic T2-R3 theorem. Point and finite-family exclusions have their separately stated hypotheses.'}
(ROOT/'research/l2_box_audit/verification/T2_R3.json').write_text(json.dumps(out,indent=2)+'\n')

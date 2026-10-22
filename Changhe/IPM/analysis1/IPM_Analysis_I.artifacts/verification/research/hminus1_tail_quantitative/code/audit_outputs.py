"""Independent exact source, Fourier, quotient, rounding and full-rerun audit.
No JavaScript/TypeScript, servers/listeners/tunnels, RLScience, Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,hashlib,sys,time,subprocess,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_quantitative';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def box(x):
 l,h=map(F,(x['lower_exact'],x['upper_exact']));assert l<=h;return l,h
def signed_sine(f):return ((abs(f)-1)//2,1 if f>0 else -1)
def cc(i):return (-1 if i%2 else 1)*(i//2+1)
def run():
 start=time.monotonic();pins={};dependencies={};counts={}
 for topic,fn in (('modal_repair','audit_verdict'),('outer_leading_cancellation','verdict'),('normalized_tail_repair','verdict'),('hminus1_tail_repair','verdict'),('single_tail_second_row','verdict'),('source_jet_corrections','verdict')):
  p=B/'research'/topic/'evidence'/(fn+'.json');d=read(p);assert (d.get('status') or d.get('verdict')).startswith('CONFIRMED'),topic
  pins[str(p.relative_to(B))]=sha(p);dependencies[topic]={'sha256':sha(p),'status':d.get('status',d.get('verdict')),'pins':len(d.get('files',{}))}
  for rel,h in d.get('files',{}).items():
   q=B/rel;assert q.resolve().is_relative_to(B) and sha(q)==h,rel
   assert rel not in pins or pins[rel]==h;pins[rel]=h
 prior=read(B/'research/normalized_tail_repair/evidence/verdict.json')['public_bounds']
 assert prior['N_upper']=='38.37961982' and prior['I_abs_upper']=='0.03893786140' and prior['C_upper']=='0.334616'
 for key,v in (('N',prior['N_upper']),('I_H',prior['I_abs_upper']),('C',prior['C_upper'])):
  lo,hi=map(F,prior['strict_intervals'][key]);assert max(abs(lo),abs(hi))<F(v)
 counts['distinct_prior_pins']=len(pins)
 first={name:read(E/(name+'.json')) for name in ('arb','iv')};pub=read(D/'source/public_bounds.json')
 assert set(pub)==set(first['arb']['values'])==set(first['iv']['values']) and len(pub)==22
 for name,d in first.items():
  assert d['status']=='COMPUTED_REQUIRES_AUDIT';assert len(d['H2_sines'])==783 and len(d['H2_quotient'])==782
  for rel,h in d['files'].items():assert sha(B/rel)==h;pins[rel]=h
  if 'source_archive' in d:assert sha(Path(d['source_archive']['path']))==d['source_archive']['sha256']
  for key,(lo,hi) in pub.items():
   l,h=box(d['values'][key]);assert F(lo)<l<=h<F(hi),(name,key)
  for group in ('H2_sines','H2_quotient'):
   for row in d[group]:box(row)
  # A separate exact rational norm enclosure from every saved quotient interval.
  intervals=[box(row) for row in d['H2_quotient']]
  nlo=sum((min(abs(l),abs(h)) if l*h>0 else F(0) for l,h in intervals),F(0))
  nhi=sum((max(abs(l),abs(h)) for l,h in intervals),F(0))
  assert F(pub['N2'][0])<nlo<=nhi<F(pub['N2'][1])
  # The sine-row and quotient projection are two compatible interval constructions.
  for index,weights in ((0,{0:2,2:-1}),(1,{0:2,1:1,2:-1,3:-1})):
   lo=hi=F(0)
   for j,w in weights.items():
    ll,hh=intervals[j];lo+=min(w*ll,w*hh)/8;hi+=max(w*ll,w*hh)/8
   ll,hh=box(d['H2_sines'][index]);assert max(lo,ll)<=min(hi,hh)
  assert box(d['values']['H20'])==box(d['H2_sines'][0])
  assert F('-298.795137988')<box(d['H2_sines'][0])[0]<=box(d['H2_sines'][0])[1]<F('-298.795137987')
 assert first['arb']['exact']==first['iv']['exact'];ex=first['arb']['exact'];k=F(ex['k']);L=F(ex['L']);t=F(ex['tplus']);beta=2*k-1;a2=3*k-2;ad=k-2
 assert 0<k<F(1,4) and L<9 and beta+1==2*k and a2+1==3*k-1 and ad+1==k-1
 assert list(map(F,ex['exponents']))==[beta,a2,ad]
 raw=read(B/'data_exact/modal_v2.json');ar=raw['arrays'];archive=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
 with np.load(archive,allow_pickle=False) as z:
  assert sha(archive)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
  assert z['Aout'].shape==(260,10) and ar['Aout']['shape']==[260,10] and len(ar['Aout']['hex'])==2600
  for x,hx in zip(z['Aout'].flat,ar['Aout']['hex']):assert F(float(x))==F(float.fromhex(hx))
  assert len(z['knots'])==len(ar['knots']['hex'])==1573
  for x,hx in zip(z['knots'],ar['knots']['hex']):assert F(float(x))==F(float.fromhex(hx))
  assert F(float(z['k']))==k and F(float(z['L']))==L and F(float(z['knots'][-1]))==t
  bo=F(float(z['bo']));assert bo>120
  columns=[[F(float(x)) for x in z['Aout'][:,col]] for col in (0,1,2,6)]
 # Third independent source sine map: adjacent closed coefficients vs signed products.
 for q in columns:
  get=lambda j:q[j] if 0<=j<260 else F(0)
  direct=[F(0)]*262
  for m,v in enumerate(q):
   for p in (1,3):
    for f in (p+2*m,p-2*m):j,s=signed_sine(f);direct[j]+=s*v/8
  closed=[(2*get(0)-get(2))/8,(2*get(0)+get(1)-get(2)-get(3))/8]+[(get(j-1)+get(j)-get(j+1)-get(j+2))/8 for j in range(2,262)]
  assert direct==closed and direct[-1]==0
 counts.update(original_outer_coefficients=2600,original_knots=1573,third_sine_projections=1048)
 # Exact generating-function recurrence for the collected inverse.
 for j in range(2*783):assert sum(w*(cc(j-i) if j>=i else 0) for i,w in enumerate((1,1,-1,-1)))==int(j==0)
 M=781;tests=0
 for basis in range(M+1):
  # Build 8E without rationals, then apply both inversions to all782 outputs.
  eig=[0]*(M+2)
  for p in (1,3):
   for f in (p+2*basis,p-2*basis):j,s=signed_sine(f);eig[j]+=s
  sparse=[(j,v) for j,v in enumerate(eig) if v]
  collected=[sum(cc(j-1)*v for j,v in sparse if j>=1)]
  assert collected[0]%2==0;collected[0]//=2
  collected += [sum(cc(j-m-1)*v for j,v in sparse if j>=m+1) for m in range(1,M+1)]
  expect=[int(j==basis) for j in range(M+1)];assert collected==expect
  poly=[0]*(2*M+4)
  for j,v in sparse:poly[M+2+j]+=v;poly[M+1-j]-=v
  for root in (-1,-1,1):
   quotient=[0]*(len(poly)-1);quotient[-1]=poly[-1]
   for j in range(len(quotient)-2,-1,-1):quotient[j]=poly[j+1]+root*quotient[j+1]
   assert poly[0]+root*quotient[0]==0;poly=quotient
  assert poly[M]%2==0
  synthetic=[poly[M]//2]+[poly[M+j] for j in range(1,M+1)]
  assert synthetic==expect and all(poly[M-j]==poly[M+j] for j in range(1,M+1));tests+=len(expect)*2
 counts.update(quotient_basis_vectors=M+1,quotient_matrix_entries=tests,collected_recurrence_coefficients=2*783)
 # Reconstruct all signed Fourier supports with symbolic unit Vr and W separately.
 # Laurent coefficients represent 2i times an odd sine; multiplication by cos
 # has coefficients1/2, and derivative has p/2 at both signs.
 support=0
 for na,nc in ((261,522),(522,261)):
  maxfreq=2*na+2*nc-1;assert maxfreq==1565
  for n in range(1,na+1):
   for j in range(nc):
    p=2*j+1;freq=2*n
    radial={};tangent={}
    for sf,sv in ((p,1),(-p,-1)):
     for cf in (freq,-freq):radial[sf+cf]=radial.get(sf+cf,0)+sv
    for sf,sv in ((freq,1),(-freq,-1)):
     for cf in (p,-p):tangent[sf+cf]=tangent.get(sf+cf,0)+sv*p
    sine_r={};sine_t={}
    for f in (p+freq,p-freq):ii,sg=signed_sine(f);sine_r[ii]=sine_r.get(ii,0)+sg
    for f in (freq+p,freq-p):ii,sg=signed_sine(f);sine_t[ii]=sine_t.get(ii,0)+sg*p
    assert all(radial.get(2*i+1,0)==v for i,v in sine_r.items())
    assert all(tangent.get(2*i+1,0)==v for i,v in sine_t.items())
    assert all(abs(f)<=1565 and abs(f)%2 for f in radial)
    support+=1
 counts['signed_Fourier_support_pairs']=support
 denom=0
 for aa,end in ((k,261),(beta,522),(a2,783),(ad,261)):
  for n in range(1,end+1):
   c=aa+1;expanded=4*n*n-c*c;assert expanded==(2*n-c)*(2*n+c)>0
   assert -(1/(2*n-c)+1/(2*n+c))/2==-2*n/expanded
   assert (1/(2*n-c)-1/(2*n+c))/2==c/expanded
   denom+=1
 counts['positive_Green_and_partial_fraction_identities']=denom
 # Polynomial cutoff moments and exact falling-factorial geometric sums.
 b=[F(0)]*17
 for i in range(9):
  for j in range(9):b[i+j]+=F(math.comb(8,i)*(-1)**(8-i)*math.comb(8,j)*2**(8-j)*(-1)**j)
 B0=sum(v*F(2**(i+1)-1,i+1) for i,v in enumerate(b));Jb=sum(v*F(2**(i+2)-1,i+2) for i,v in enumerate(b))
 assert B0==F(math.factorial(8)**2,math.factorial(17)) and Jb==F(1,145860)==3*B0/2
 moments=[F(4,3),F(4,9),F(20,27),F(44,27)]
 sums=[]
 for j in range(4):
  poly=[1]
  for d in range(j):
   out=[0]*(len(poly)+1)
   for i,v in enumerate(poly):out[i]+=(3-d)*v;out[i+1]+=2*v
   poly=out
  sums.append(sum(v*moments[i] for i,v in enumerate(poly)))
 assert sums==list(map(F,ex['Sj']))==[F(4,3),F(44,9),F(416,27),F(1312,27)]
 for aa in (beta,a2,ad):
  m=max(F(1,2),2/(3-aa))
  assert m==(2/(3-aa) if aa>-1 else F(1,2)) and aa-3<0
  for n in range(2,784):assert F(n)/(2*n-aa-1)<=m
 counts.update(exact_beta_moments=2,exact_geometric_sums=4,m_factor_inequalities=3*782)
 # Recheck inherited source endpoints in both maps, not only their file hashes.
 source_path=B/'research/source_jet_corrections/evidence/checks.json'
 assert str(source_path.relative_to(B)) in pins
 source=read(source_path)
 for mapping in ('exact_ranges','portable_bounds'):
  dl,dh=box(source[mapping]['D']);cl,ch=box(source[mapping]['C'])
  assert F('6.70197e-7')<dl<=dh and 0<cl<=ch<F('30.0230')
 plo,phi=map(F,source['root_bracket_exact']);assert 0<plo<=phi<9
 # Independent rational Taylor enclosure for Rb=exp(t), with a geometric
 # majorant of the positive tail after order128. Ratios decrease thereafter.
 term=total=F(1)
 for j in range(1,129):term*=t/j;total+=term
 assert 0<t<9 and t/130<1
 radius_lo=total;radius_hi=total+(term*t/129)/(1-t/130)
 assert F('3412.96685816')<radius_lo<=radius_hi<F('3412.96685817')
 assert 2*9<3000<radius_lo<=radius_hi<10000 and L<10000
 assert F(pub['local_T10000_j0'][1])<F('1e-8') and F(pub['local_T10000_j1'][1])<F('1e-8')
 margin=F('6.70197e-7')-F('30.0230')*F('1e-8');assert margin>F('3.69e-7')
 counts.update(strict_public_endpoint_tests=44,independent_quotient_norm_tests=2,source_margin_tests=3,source_endpoint_directions=4,source_location_tests=1,independent_radius_taylor_terms=129,admissible_radius_tests=3)
 overlaps=0
 for group in ('H2_sines','H2_quotient'):
  for x,y in zip(first['arb'][group],first['iv'][group]):l,h=box(x);ll,hh=box(y);assert max(l,ll)<=min(h,hh);overlaps+=1
 for key in pub:l,h=box(first['arb']['values'][key]);ll,hh=box(first['iv']['values'][key]);assert max(l,ll)<=min(h,hh);overlaps+=1
 counts['interval_overlap_diagnostics']=overlaps
 for name in ('arb','iv'):
  cp=subprocess.run([sys.executable,str(D/'code'/('engine_'+name+'.py'))],cwd=B,capture_output=True,text=True,timeout=90,env=os.environ.copy());(E/('rerun_'+name+'.log')).write_text(cp.stdout+cp.stderr);assert cp.returncode==0
  old=first[name];new=read(E/(name+'.json'))
  for d in (old,new):d.pop('utc');d.pop('seconds')
  assert old==new,(name,'complete output differs')
 counts['complete_engine_reruns']=2
 cv=read(E/'integer_convolution_checks.json');assert cv['cases']==96 and cv['output_boxes_checked']==723 and cv['engine_sha256']==sha(D/'code/engine_iv.py')
 counts.update(exact_integer_convolution_test_cases=96,exact_integer_test_boxes=723)
 ac=read(E/'arb_convolution_checks.json');assert ac['cases']==64 and ac['output_boxes_checked']==568 and ac['engine_sha256']==sha(D/'code/engine_arb.py')
 counts.update(arb_convolution_test_cases=64,arb_convolution_test_boxes=568)
 assert read(E/'proof_first.json')['proof_sha256']==sha(D/'PROOF.md')
 for p in (D/'PROOF.md',D/'ADDENDUM.md',D/'source/public_bounds.json',D/'code/engine_arb.py',D/'code/engine_iv.py',D/'code/check_integer_convolution.py',Path(__file__),E/'arb.json',E/'iv.json',E/'proof_first.json',E/'addendum_first.json',E/'integer_convolution_checks.json',D/'code/check_arb_convolution.py',E/'arb_convolution_checks.json',E/'rerun_arb.log',E/'rerun_iv.log'):pins[str(p.relative_to(B))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_FINITE_AUDIT_REQUIRES_COLLABORATIVE_CLOSURE','dependencies':dependencies,'counts':counts,'strict_public_bounds':pub,'source_margin_exact':str(margin),'radius_taylor_enclosure':{'lower_exact':str(radius_lo),'upper_exact':str(radius_hi),'terms':129,'public_strict_lower':'3412.96685816','public_strict_upper':'3412.96685817'},'source_archive':{'path':str(archive),'sha256':sha(archive)},'files':dict(sorted(pins.items())),'seconds':time.monotonic()-start,'scope':'Both interval engines and independent exact audit completed. No inverse or global residual norm ceiling, no decisive endpoint.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({key:out[key] for key in ('utc','status','counts','seconds')}))
if __name__=='__main__':run()

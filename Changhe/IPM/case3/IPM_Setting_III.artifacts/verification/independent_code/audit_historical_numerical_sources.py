from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from decimal import Decimal
import ast,hashlib,json,math,re
from q_checkpoint_reader import QCheckpoint
R=Path('research/historical_numerical_source_audit');V=R/'verification';D=V/'records';checks=[];findings=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();flat=lambda s:' '.join(s.split())
def ck(name,b,e=None):checks.append(dict(name=name,passed=bool(b),evidence=e))
def decint(s):
 q=Decimal(s);u=Decimal(10)**q.as_tuple().exponent
 return float(q-u/2),float(q+u/2)
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def inprinted(x,s):a,b=decint(s);return a<=x<=b
def field(s,k):return re.search(r'(?<!\w)'+re.escape(k)+r'=([+\-\d.eE]+)',s)[1]
for z in json.loads((V/'INPUTS.json').read_text())['files']:ck('hash '+Path(z['frozen']).name,sha(z['frozen'])==z['sha256'])
# Exact arithmetic tests of the center formula, without an inverse claim.
for ell in [Fraction(3,2),Fraction(2),Fraction(14,5),Fraction(33,10)]:
 for c in [Fraction(-2),Fraction(-1,3),Fraction(0),Fraction(2,3)]:
  a=Fraction(7,3);y=Fraction(1,10**5);rho=a*y;transport=(ell+c)*y*a;rr=transport-rho;nf=abs(transport)+abs(rho)
  ck('manufactured center '+str((ell,c)),abs(rr)/nf==abs(ell+c-1)/(abs(ell+c)+1))
source=(D/'refine_fixed.py').read_text();ck('forced diagnostic source',"np.abs(ev['R']-mu*ev['y']*phi)/ev['Nf']"in source.replace(' ',''),source[source.find('ev='):source.find('ev=')+500])
ck('accepted seed threshold',re.search(r"if\s+info\['nF'\]\s*<\s*1e-8",source)is not None)
fixed=[]
for ell in [2.8,3.3]:
 rows=[s for s in (D/f'rf_s2_cl{ell}.log').read_text().splitlines()if s.startswith('cl=')and'forced-eq'in s];ck(f'fixed{ell} four rows',len(rows)==4)
 for row in rows:
  n=int(field(row,'N'));m=int(field(row,'M'));it=int(field(row,'it'));f=float(re.search(r'-> \|F\|=([\deE.+-]+)',row)[1]);mu=float(field(row,'mu'));c=float(field(row,'c'));a0=float(field(row,'a0'));vals=list(map(float,row.split('[<.1,.1-1,1-100,>100]=')[1].split('cheb')[0].split()))
  ck(f'fixed{ell}N{n} size',m==n//2);ck(f'fixed{ell}N{n} forcing nonzero',abs(mu)>.7);ck(f'fixed{ell}N{n} end condition',(n==48 and f<1e-12)or(n>48 and it==120 and 1e-5<f<1e-3))
  delta=ell+c-1;lim=abs(delta)/(abs(1+delta)+1);ck(f'fixed{ell}N{n} unforced center much larger than forced samples',lim>100*max(vals))
  fixed.append(dict(cl=ell,N=n,M=m,iterations=it,node_f=f,mu=mu,a0=a0,logged_strain=c,forced_regions=vals,unforced_center_limit_from_logged_strain=lim))
report=(D/'FINAL_REPORT.d72trial_v4.md').read_text();sec46=flat(report[report.index('\n4.6 '):report.index('\n4.7 ')]);sec47=flat(report[report.index('\n4.7 '):report.index('\n4.8 ')])
ck('historical forced diagnostic mislabeled', 'between-node maxima of |R|/N_f near 8e-6 and 2.5e-5'in sec46)
findings.append(dict(item='fixed-cl residual label',verdict='REFUTED',claim='Those fixed-cl maxima are unforced |R|/Nf.',correction='They are |R-mu*y*phi|/Nf; six refined solves stop at iteration caps.'))
# Reconstruct the origin coefficient from all stored binary coefficients, independently of producer routines.
releases=[]
for c0 in ['3.0','1.5']:
 for n in [64,96,128]:
  for width in ['0.25','0.125']:
   tag=f'qlsrel_cl{c0}_N{n}_Lf{width}';log=(D/(tag+'.log')).read_text();row=[s for s in log.splitlines()if s.startswith('QL release ')];ck(tag+' one final row',len(row)==1);row=row[0].split('): ',1)[1]
   obj=QCheckpoint(V/'states'/(tag+'.pt'));a=sum((Fraction.from_float(float(x))*(-1)**j for j,x in enumerate(obj.coeff[0])),Fraction());cl=obj.cl
   ck(tag+' exact a0 matches log',inprinted(float(a),field(row,'a0')),dict(exact=str(a),log=field(row,'a0')));ck(tag+' cl matches log',inprinted(cl,field(row,'cl')))
   ck(tag+' dimensions',obj.N==n and obj.M==n//4);ck(tag+' physical forcing width metadata',obj.Lf==float(width));ck(tag+' fixed start exponent',abs(obj.kappa-float(c0)/(float(c0)-1))<1e-14);ck(tag+' released parameter differs from fixed map',abs(cl-float(c0))>.01)
   ck(tag+' own Cartesian reader origin agreement',abs(float(obj.rho(0.,1e-12))/1e-12-float(a))<2e-10)
   state=dict(tag=tag,cl_start=float(c0),N=n,width=float(width),cl=cl,a0=float(a),a0_exact=str(a),iterations=int(field(row,'its')),logged_Fmax=float(field(row,'|F|max')),source_header=log.splitlines()[0],sha256=sha(obj.path),map_p=obj.kappa,tail_exponent=obj.p,far_floor=abs(cl*obj.p-1)/(cl*obj.p+1))
   releases.append(state)
comparisons=[]
for c0 in [3.,1.5]:
 for n in [64,96,128]:
  a,b=[z for z in releases if z['cl_start']==c0 and z['N']==n];comparisons.append(dict(cl_start=c0,N=n,cl_width_quarter=a['cl'],cl_width_eighth=b['cl'],a0_width_quarter=a['a0'],a0_width_eighth=b['a0'],cl_relative_difference=abs(b['cl']-a['cl'])/abs(a['cl']),a0_relative_difference=abs(b['a0']-a['a0'])/abs(a['a0']),same_cl_five_decimals=f"{a['cl']:.5f}"==f"{b['cl']:.5f}",same_a0_three_decimals=f"{a['a0']:.3f}"==f"{b['a0']:.3f}",same_a0_three_significant=f"{a['a0']:.3g}"==f"{b['a0']:.3g}"))
ck('width digit claim present','same stall to the digits shown'in sec47)
ck('width digit claim counterexample64',not next(z for z in comparisons if z['cl_start']==3 and z['N']==64)['same_cl_five_decimals'])
ck('width digit claim counterexample96',not next(z for z in comparisons if z['cl_start']==1.5 and z['N']==96)['same_a0_three_decimals'])
ck('width three-significant claim counterexample128',not next(z for z in comparisons if z['cl_start']==3 and z['N']==128)['same_a0_three_significant'])
findings.append(dict(item='two-width agreement',verdict='REFUTED',claim='Agreement at all shown digits at64/96 and three significant digits at128.',max_cl_relative_difference=max(z['cl_relative_difference']for z in comparisons),max_a0_relative_difference=max(z['a0_relative_difference']for z in comparisons),correction='Nearby but unequal stalls; report the actual differences.'))
table=[]
for line in report.splitlines():
 m=re.match(r'\s+(3|1\.5)\s+(64|96|128)x(16|24|32)\s+([\d.]+)\s+([\d.]+)\s+([\deE.+-]+)\s+',line)
 if m:
  c0,n,_,cl,a0,f=m.groups();z=next(s for s in releases if s['cl_start']==float(c0)and s['N']==int(n)and s['width']==.25);good_cl=inprinted(z['cl'],cl);good_a=inprinted(z['a0'],a0);ck(z['tag']+' table cl precision',good_cl);ck(z['tag']+' table expected a0 outcome',good_a==(not(float(c0)==1.5 and int(n)==64)))
  table.append(dict(tag=z['tag'],printed_cl=cl,printed_a0=a0,cl_correct=good_cl,a0_correct=good_a,corrected_a0=f"{z['a0']:.3f}"))
ck('five table rows',len(table)==5)
findings.append(dict(item='release table a0 start1.5 N64',verdict='REFUTED',old='5.321',correct='5.322',value=next(z['a0']for z in releases if z['cl_start']==1.5 and z['N']==64 and z['width']==.25)))
# The q_free lineage is identified by its bytes, source header, and independent numeric metadata.
tag='qfree_cl1.5_N128_Lf0.25';log=(D/(tag+'.log')).read_text();q=QCheckpoint(V/'states'/(tag+'.pt'));a=sum((Fraction.from_float(float(x))*(-1)**j for j,x in enumerate(q.coeff[0])),Fraction());end=[s for s in log.splitlines()if s.startswith('Q release')or s.startswith('QF release')]
ck('709 checkpoint identity',sha(q.path)=='709d48d4781dd57cdd7758d71e4b89204ace9befcb225074f235fd5af21adc2b');ck('709 exact cl metadata',abs(q.cl-1.0200000000539495)<1e-15);ck('709 exact a0',abs(float(a)-.1056747227844456)<1e-15);ck('709 rebuilt map identity',abs(q.kappa-q.cl/(q.cl-1))<1e-12);ck('709 forced start source','qls_cl1.5_N128_Lf0.25.pt'in log.splitlines()[0]);ck('709 driver source', 'q_free' in log.splitlines()[0])
lineage=dict(sha256=sha(q.path),cl=q.cl,a0=float(a),a0_exact=str(a),map_p=q.kappa,header=log.splitlines()[0],prior_independent_result46='evidence/q_evaluations/qfree_cl1.5_N128_Lf0.25_logwide/comparison.json',prior_comparison_sha256=sha('evidence/q_evaluations/qfree_cl1.5_N128_Lf0.25_logwide/comparison.json'))
# Independently parse all27 early-time departure runs.
expected={}
for line in (D/'drW_chain_departure_actualtime.txt').read_text().splitlines():
 if not line.startswith('dr'):continue
 m=re.search(r'^(\S+)\s+a0\s+([\d.]+)\s+t1 ([\d.]+) t2 ([\d.]+)\s+rate\(actual\)\s+([\d.]+) \(([\d.]+) a0\).*nominal-0.4 value\s+([\d.]+)\]\s+cw=0 at (.*)',line);assert m,line
 name,a0,t1,t2,rate,rel,nom,stop=m.groups();expected[name]=dict(rate=rate,a0=a0,t1=t1,t2=t2,relative=rel,nominal=nom,stop=stop,source='drW_chain_departure_actualtime.txt')
for name,rate in [('drG_chain128_local_rc13','18.46'),('drG_chain128_cheb_rc10','16.83'),('drG_chain128_cheb_rc8','15.53')]:expected[name]=dict(rate=rate,source='drG_chain128_basis_cutoff.txt')
for name,rate in [('drF_chain64_frozen','1.04'),('drF_chain128_frozen','109.60'),('drF_chain128_frozen_h004','0.74'),('drF_chain128_full_h004','15.84'),('drF_chain64_frozenU','0.52'),('drF_chain128_frozenU','3.63'),('drF_chain64_frozenc','13.60'),('drF_chain128_frozenc','15.84'),('drF_chain64_frozenU_h2','0.57'),('drF_chain64_frozenc_h2','13.68'),('drF_chain96_frozenU','3.80'),('drF_chain96_frozenc','14.84'),('drF_chain96_full','15.96')]:expected[name]=dict(rate=rate,source='drF_frozen_velocity.txt'if name=='drF_chain128_frozen'else'drF_frozen_split.txt')

def slope_bounds(a,b):
 t1,t2=decint(a[0]),decint(b[0]);z1,z2=decint(a[5]),decint(b[5]);nn=[math.log(z2[0]/z1[1]),math.log(z2[1]/z1[0])];dd=[t2[0]-t1[1],t2[1]-t1[0]];assert dd[0]>0
 vv=[x/y for x in nn for y in dd];return min(vv),max(vv)
rates=[]
for name,e in expected.items():
 text=(D/(name+'.log')).read_text();rows=[s.split('|',1)[0].split()for s in text.splitlines()if re.match(r'^\s+\d+\.\d+\s',s)];ck(name+' numeric rows',len(rows)>3);a=min(rows,key=lambda z:abs(float(z[0])-.1));b=min(rows,key=lambda z:abs(float(z[0])-.5));gap=float(b[0])-float(a[0]);num=math.log(float(b[5])/float(a[5]));rate=num/gap;bounds=slope_bounds(a,b);claim=decint(e['rate']);ck(name+' logged rate rounding consistent',overlap(bounds,claim),dict(printed_arithmetic=rate,decimal_input_bounds=bounds,reported=e['rate']));ck(name+' rate present in source summary',e['rate']in(D/e['source']).read_text())
 strict=[z for z in rows if .1<=float(z[0])<=.5];tt=[float(z[0])for z in strict];zz=[math.log(float(z[5]))for z in strict];mt=sum(tt)/len(tt);mz=sum(zz)/len(zz);ols=sum((t-mt)*(z-mz)for t,z in zip(tt,zz))/sum((t-mt)**2 for t in tt)
 stops=re.findall(r'# tau ([\d.]+): c_w = .*<= 0.*STOP',text);final=re.findall(r'# FINAL.*?tau[ =]+([\d.]+)',text);last=float(final[-1])if final else float(rows[-1][0]);stop=stops[-1]if stops else None
 if 't1'in e:
  ck(name+' actual selected times',float(a[0])==float(e['t1'])and float(b[0])==float(e['t2']));ck(name+' nominal-rate rounding',overlap((bounds[0]*gap/.4,bounds[1]*gap/.4),decint(e['nominal'])))
  a0lo,a0hi=decint(rows[0][4]);cwlo,cwhi=decint(rows[0][2]);prod=[x*y for x in[a0lo,a0hi]for y in[cwlo,cwhi]];a0interval=min(prod),max(prod);ck(name+' initial unregauged a0 rounding',overlap(a0interval,decint(e['a0'])))
  relbounds=bounds[0]/a0interval[1],bounds[1]/a0interval[0];ck(name+' rate/a0 rounding',overlap(relbounds,decint(e['relative'])))
  if e['stop'].startswith('not reached'):
   claimedlast=float(re.search(r'last tau ([\d.]+)',e['stop'])[1]);ck(name+' no logged crossing',stop is None);ck(name+' last periodic time agrees with summary',abs(float(rows[-1][0])-claimedlast)<.005,dict(last_periodic=float(rows[-1][0]),last_final=last,printed=claimedlast))
   if name in ['drW_C3.0_chain128','drW_C3.0_chain160']:
    target={'drW_C3.0_chain128':1.3848,'drW_C3.0_chain160':1.4215}[name];ck(name+' separately identified final time',last==target);ck(name+' numerical blowup stop disclosed in primary log','# repeated blow-up: stop'in text and'stopped_at_cw0 False'in text)
  else:ck(name+' crossing time',stop is not None and abs(float(stop)-float(e['stop']))<5e-5,dict(found=stop,expected=e['stop']))
 rates.append(dict(name=name,reported=e['rate'],selected_t1=float(a[0]),selected_t2=float(b[0]),z1=float(a[5]),z2=float(b[5]),secant=rate,decimal_input_bounds=bounds,nominal_denominator_rate=num/.4,ols_strict_window=ols,stop=stop,last_time=last,last_periodic_time=float(rows[-1][0]),initial_a0star=float(rows[0][4]),metadata=ast.literal_eval(text.splitlines()[0][text.splitlines()[0].index('{'):]),unstable_original=(name=='drF_chain128_frozen')))
ck('27 dynamic runs',len(rates)==27)
# Synthetic tests distinguish actual-time secants from nominal slopes and regression.
for lam in [-.5,1.,15.7]:
 t1,t2=.1041,.5088;z1,z2=math.exp(lam*t1),math.exp(lam*t2);s=math.log(z2/z1)/(t2-t1);ck('synthetic exponential '+str(lam),abs(s-lam)<1e-13);ck('synthetic nominal differs '+str(lam),abs(math.log(z2/z1)/.4-lam)>1e-3)
ck('actual versus regression differs',any(abs(z['secant']-z['ols_strict_window'])>.1 for z in rates))
drs=(D/'dr.py').read_text();ck('rate observable uses fitted derivative',"info['Fp']"in drs and 'rho_tau' in drs);ck('unstable predecessor disclosed','h = 0.0115 frozen run above was RK4-unstable'in(D/'drF_frozen_velocity.txt').read_text())
ck('short step refinement does not imply whole trajectory convergence',float(next(z for z in rates if z['name']=='drZ_chain64_h0.002875')['last_time'])==1.)
findings.append(dict(item='rate window and terminal-time wording',verdict='REPAIRS_REQUIRED',correction='Use actual-time logarithmic secants between rows nearest0.1 and0.5. C3N128/N160 final restored states are at1.3848/1.4215 after numerical blowup stops;1.35/1.40 are periodic-row times. Step-refinement runs end at1.0.'))
findings.append(dict(item='27 pseudo-time secants',verdict='CONFIRMED',scope='Printed primary-log arithmetic with decimal-rounding compatibility, not a continuum growth rate or rigorous trajectory estimate.'))
findings.append(dict(item='709d48d4 lineage and center',verdict='CONFIRMED',scope='Exact bytes and independent stored-coefficient sum; result46 inverse computation not rerun.'))
out=dict(status='PASS'if all(z['passed']for z in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),fixed=fixed,releases=releases,width_comparisons=comparisons,table=table,lineage=lineage,rates=rates,findings=findings,verdict='REPAIRS_REQUIRED',scope='Independent source arithmetic and exact center reconstruction. No producer modules executed; no new global residual bounds; no decisive endpoint.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print(json.dumps([z for z in checks if not z['passed']],indent=2));print(json.dumps(findings,indent=2))
raise SystemExit(out['status']!='PASS')

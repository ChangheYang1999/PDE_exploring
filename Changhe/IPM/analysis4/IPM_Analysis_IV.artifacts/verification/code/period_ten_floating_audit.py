"""Finite Q10 float checks against exact polynomial targets and decimal fits."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from hashlib import sha256
import json,gzip,re,sys,time,math
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,fmpq,fmpq_poly,ctx
ROOT=Path('research/298_period_ten_floating_audit')
BASE=Path('research/282_period_ten_symbolic_response/verification')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_text())
def save(n,d):
 r=json.dumps(d,separators=(',',':')).encode();p=ROOT/'verification'/n;p.write_bytes(gzip.compress(r,mtime=0) if p.suffix=='.gz' else r+b'\n')
def poly(c):return fmpq_poly([fmpq(x) for x in c])
def ev(p,z):
 y=arb(0)
 for c in reversed(list(p)):y=y*z+arb(c)
 return y
def a(x):
 v=Fraction(str(x));return arb(fmpq(v.numerator,v.denominator))
def fit(rows):
 blocks=[]
 for j in range(max(rows)//10):
  ns=list(range(10*j+1,10*(j+1)+1))
  if all(n in rows for n in ns):blocks.append([Fraction(10*(j+1))]+[max(rows[n][c] for n in ns) for c in range(2)])
 out=[]
 for lo in [100,150,200]:
  ss=[r for r in blocks if r[0]>=lo];m=len(ss);sx=sum(r[0] for r in ss);sxx=sum(r[0]**2 for r in ss);den=m*sxx-sx*sx;assert den>0
  channels=[]
  for c in [1,2]:
   sy=sum(r[c] for r in ss);sxy=sum(r[0]*r[c] for r in ss);slope=(m*sxy-sx*sy)/den;intercept=(sy-slope*sx)/m
   mse=sum((slope*r[0]+intercept-r[c])**2 for r in ss)/m
   channels.append(dict(channel='f' if c==1 else 'g',slope=str(slope),intercept=str(intercept),A=(a(slope)*arb(10).log()).exp().str(55),R=(a(slope*Fraction(5))*arb(10).log()).exp().str(55),rms=a(mse).sqrt().str(55)))
  out.append(dict(lo=lo,first_endpoint=int(ss[0][0]),last_endpoint=int(ss[-1][0]),blocks=m,channels=channels))
 return out

def main():
 start=time.monotonic();ctx.prec=768
 prereq=read(BASE/'checks.json');assert prereq['all_checks_pass']
 gen=read(BASE/'reduced_generic.json.gz');sm=read(BASE/'small_responses.json.gz')
 cols=[poly(c) for c in gen['numerator_by_b_degree']];den=poly(gen['denominator']);small={r['k']:poly(r['coefficients']) for r in sm['small']}
 prefixp=Path('research/281_period_ten_finite_algebra/verification/prefix_polynomials.json.gz');pd=read(prefixp)
 obsp=Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json');od=read(obsp);assert od['all_checks_pass']
 fields={kind:{int(n):[poly(c) for c in row['sine_polynomials'].values()] for n,row in data.items()} for kind,data in pd['fields'].items()}
 fitp=ROOT/'sources/fit_hhf_Q10_N300.out';fitp.write_bytes(Path('../a4-lead/code/tuned/fit_hhf_Q10_N300.out').read_bytes());fittext=fitp.read_text();results=[]
 for index in range(1,15):
  source=Path('../a4-lead/code/tuned')/f'hhf_Q10h1_root{index}_N300_f64.out';p=ROOT/'sources'/source.name;p.write_bytes(source.read_bytes());text=p.read_text();header=text.splitlines()[0]
  assert 'Q=10 h=1' in header and 'dtype=float64' in header and '# done, last density order 300,' in text
  rb=Fraction(re.search(r'f_1=1:1,3:([^ ]+)',header)[1]);eps=Fraction(re.search(r'eps=([^ ]+)',header)[1]);assert eps in [Fraction(1,16),Fraction(1,2),Fraction(1)]
  binary=Fraction.from_float(float(rb));I=arb(fmpq(od['real_roots'][index-1]['interval'][0])).union(arb(fmpq(od['real_roots'][index-1]['interval'][1])));B=a(binary)
  rows={};tuning={}
  for line in text.splitlines():
   if line.startswith('n '):
    _,n,f,g=line.split();assert all(math.isfinite(float(v)) for v in [f,g]);rows[int(n)]=(Fraction(f),Fraction(g))
   elif line.startswith('k '):
    v=line.split();tuning[int(v[1])]=Fraction(v[6])
  assert set(rows)==set(range(1,300)) and set(tuning)==set(range(2,30))
  norms=[];responses=[]
  for kind in ['f','g']:
   for n,terms in fields[kind].items():
    norm=sum((abs(ev(t,I)) for t in terms),arb(0));assert norm>0
    log=norm.log()/arb(10).log();error=abs(a(rows[n][0 if kind=='f' else 1])-log)
    norms.append(dict(n=n,channel=kind,reference_log=log.str(55),absolute_log_discrepancy=error.str(55)))
  for k,printed in tuning.items():
   pol=small[k] if k<21 else fmpq_poly([c(k)/den(k) for c in cols]);v=ev(pol,I);w=ev(pol,B);assert not v.contains(0) and not w.contains(0)
   errors=[abs((a(printed)-v)/v),abs((a(printed)-w)/w),abs((w-v)/v)]
   responses.append(dict(k=k,printed=str(printed),exact_response=v.str(55),binary_response=w.str(55),relative_exact=errors[0].str(55),relative_binary=errors[1].str(55),relative_root_effect=errors[2].str(55)))
  fits=fit(rows);line=next(v for v in fittext.splitlines() if v.startswith(source.name+' '));printedfits=re.findall(r'n>=(\d+) A_f=([^ ]+) A_g=([^ ]+) rms=([^ ]+)',line);assert len(printedfits)==3
  for f,pr in zip(fits,printedfits):
   lo,pf,pg,rms=pr;assert f['lo']==int(lo)
   assert abs(arb(f['channels'][0]['A'])-a(pf))<a('0.00005') and abs(arb(f['channels'][1]['A'])-a(pg))<a('0.00005')
   assert abs(arb(f['channels'][0]['rms'])-a(rms))<a('0.005')
  maxima={}
  for label,vs in [('norm_log',[arb(r['absolute_log_discrepancy']) for r in norms])]+[(label,[arb(r[label]) for r in responses]) for label in ['relative_exact','relative_binary','relative_root_effect']]:
   v=max(vs,key=lambda v:float(v.mid()));bound=Fraction(1,10**20)
   while not all(x<a(bound) for x in vs):bound*=10
   maxima[label]=dict(value=v.str(45),strict_bound=str(bound))
  out=dict(root_index=index,source=ref(p),header=header,amplitude=str(eps),binary_input=str(binary),root_interval=od['real_roots'][index-1]['interval'],announced_density_order=300,last_printed_order=max(rows),maximum_fit_endpoint=290,norm_comparisons=len(norms),response_comparisons=len(responses),maxima=maxima,norms=norms,responses=responses,fits=fits,printed_fit_rounding_matches=True)
  results.append(out);save('partial.json.gz',dict(results=results));print(json.dumps(dict(at=now(),root=index,maxima=maxima,elapsed_s=time.monotonic()-start)),flush=True)
 inputs=[ref(p) for p in [BASE/'checks.json',BASE/'reduced_generic.json.gz',BASE/'small_responses.json.gz',prefixp,obsp,fitp]]
 result=dict(at=now(),all_checks_pass=True,bits=ctx.prec,results=results,inputs=inputs,actual_elapsed_s=time.monotonic()-start,scope='Finite low-order norms and all printed affine responses; exact fits of printed decimals; high-order coefficients not enclosed.')
 save('checks.json.gz',result)
 for p in [Path('code/period_ten_floating_audit.py'),Path('../a4-lead/code/tuned/hh_float.py'),Path('../a4-lead/code/tuned/fit_hhf.py')]:(ROOT/'sources'/p.name).write_bytes(p.read_bytes())
 print(json.dumps(dict(at=now(),complete=True,elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  import traceback
  d=dict(at=now(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(x.filename).name,line=x.lineno) for x in traceback.extract_tb(exc.__traceback__)])
  save('FAILURE.json',d);print(json.dumps(d),flush=True);raise SystemExit(1)

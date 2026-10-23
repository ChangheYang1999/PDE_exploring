"""Result299: three-state independent function evaluation, not an inverse test."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
import hashlib,json,re,math,traceback,resource
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from scalar_mp_hydrostatic_density import ScalarMPDensity
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3));torch.set_num_threads(1)
R=Path('research/hydrostatic_224_function_difference');V=R/'verification';P=Path('research/hydrostatic_function_space_audit/verification');Q=Path('research/hydrostatic_c2_resolved_224_audit/verification');checks=[];bindings={};utc=lambda:datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);x=sha(p)
 if h:ck('hash '+str(p),x==h)
 bindings[str(p)]=x;return p
def token_interval(token):
 half=F(10)**Decimal(token).as_tuple().exponent/2;return F(token)-half,F(token)+half,half
def token_agrees(value,token):
 lo,hi,_=token_interval(token);return lo<=F(value)<=hi
bounds=[(0,.1),(.1,1),(1,100),(100,1e4),(1e4,1e7)];names=['inner','subunit','annulus','far','outer']
def compare(a,b,coords,mask_radius,weight_radius=None):
 x,y=coords;r=np.hypot(x,y)if weight_radius is None else weight_radius;dg=abs(a[:,0]-b[:,0]);dgrad=np.hypot(a[:,1]-b[:,1],a[:,2]-b[:,2]);den=abs(b[:,0]);wf=np.sqrt(1+r);wg=1/wf
 metrics={'field':(dg,wf),'gradient':(dgrad,wg),'pointwise_relative':(dg,den)}
 masks={name:(mask_radius>=lo)&(mask_radius<hi)for name,(lo,hi)in zip(names,bounds)};masks.update(full_sample=np.ones(len(r),dtype=bool),outer_boundary=mask_radius==1e7);out={}
 for name,mask in masks.items():
  z=dict(count=int(mask.sum()),zero_over_zero=int((mask&(den==0)&(dg==0)).sum()),nonzero_over_zero=int((mask&(den==0)&(dg!=0)).sum()))
  for key,(nu,de)in metrics.items():
   ids=np.flatnonzero(mask&(de>0))
   if not len(ids):z[key]=None;continue
   j=int(ids[np.argmax(nu[ids]/de[ids])]);z[key]=dict(value=float(nu[j]/de[j]),index=j,x=float(x[j]),y=float(y[j]),numerator=float(nu[j]),denominator=float(de[j]))
  positive=mask&(den>0);small=positive&(den/wf<=1e-12);z['near_zero_positive_count']=int(small.sum());z['least_positive_weighted_density']=float(np.min(den[positive]/wf[positive]))if positive.any()else None
  z['field_scale']=float(np.max(den[mask]/wf[mask]))if mask.any()else None;z['gradient_scale']=float(np.max(np.hypot(b[mask,1],b[mask,2])/wg[mask]))if mask.any()else None;out[name]=z
 return out

def main():
 out=dict(status='RUNNING',started_utc=utc(),pid=os.getpid(),checks=checks,bindings=bindings,states=[],comparisons={},tokens=[])
 def save():
  out['updated_utc']=utc()
  def diagnostic(value):
   if isinstance(value,float) and not math.isfinite(value):return str(value)
   if isinstance(value,dict):return {k:diagnostic(v)for k,v in value.items()}
   if isinstance(value,list):return [diagnostic(v)for v in value]
   return value
  text=json.dumps(diagnostic(out)if out['status']=='FAIL'else out,indent=2,allow_nan=False)+'\n';tmp=V/'RUN.json.tmp';tmp.write_text(text);tmp.replace(V/'RUN.json')
 save()
 try:
  for p in [__file__,R/'PROOF.md',R/'REVIEW_RESOLUTION_PROOF.md',V/'INPUTS.json',R/'MANUFACTURE_PROOF.md',R/'SECOND_REVIEW_RESOLUTION_PROOF.md',R/'THIRD_REVIEW_RESOLUTION_PROOF.md',V/'PRODUCER_SOURCE.json',V/'MANUFACTURES.json',V/'PREPARATION.json']+[Path('independent_code')/n for n in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','scalar_mp_hydrostatic_density.py']]:bind(p)
  manufactures=json.loads((V/'MANUFACTURES.json').read_text());ck('manufactures complete',manufactures['status']=='PASS'and all(t['passed']for t in manufactures['checks']));
  ck('executing driver is manufactured driver',sha(__file__)==manufactures['bindings']['independent_code/audit_hydrostatic_224_function.py'])
  for p,h in manufactures['bindings'].items():bind(p,h)
  producer=json.loads((V/'PRODUCER_SOURCE.json').read_text());bind(producer['frozen'],producer['sha256'])
  inp=json.loads((V/'INPUTS.json').read_text());bind(inp['producer_firstlook']['path'],inp['producer_firstlook']['sha256'])
  for p,h in inp['dependencies'].items():bind(p,h)
  prev=json.loads((P/'REVIEW_REPAIRS.json').read_text());ck('276375complete',prev['status']=='PASS'and prev['count']==375==len(prev['checks'])and all(x['passed']for x in prev['checks']))
  for p,h in prev['dependencies'].items():bind(p,h)
  oldgate=json.loads((P/'CHECKS.json').read_text());ck('276 arithmetic gate',oldgate['status']=='PASS'and all(x['passed']for x in oldgate['checks']))
  prior_driver=bind('independent_code/audit_hydrostatic_function_space.py',oldgate['driver_sha256']);prior_text=prior_driver.read_text();ck('276 identical shifted recipe and exact axes',all(t in prior_text for t in ['rr2=10**(-3+(np.arange(277)+.371)/277*10)','th2=np.r_[0,(np.arange(39)+.271)/39*np.pi/2,np.pi/2]','sy[::len(th2)]=0;sx[len(th2)-1::len(th2)]=0']))
  for p,h in oldgate['code_sha256'].items():bind(Path('independent_code')/p,h)
  source=json.loads((Q/'SOURCE_GATE.json').read_text());ck('289source16complete',source['status']=='PASS'and len(source['checks'])==16 and all(x['passed']for x in source['checks']));bind(Q/'INPUTS.json',source['input_sha256'])
  for p,h in source['modules'].items():bind(p,h)
  middle=next(s for s in json.loads((P/'INPUTS.json').read_text())['states']if s['tag']=='hsG_c2.0_N160_log');bind(middle['state']['path'],middle['state']['sha256'])
  old=next(s for s in json.loads((P/'INPUTS.json').read_text())['states']if s['tag']=='hsG_c2.0_N192_log');new=json.loads((Q/'INPUTS.json').read_text())['states'][0]
  bind(old['state']['path'],old['state']['sha256']);bind(new['frozen'],new['sha256']);ck('frozen attempt2identity',new['sha256']=='7c5ec5f1ce8a749ae2f9aac120a0c2fa839c108e429d50db4c664b55497e840e')
  arrpath=P/'hsG_c2.0_N192_log_independent.npz';bind(arrpath,prev['array_hashes'][str(arrpath)]);f=dict(np.load(arrpath));X,Y=f['X'],f['Y'];radial=np.geomspace(1e-3,1e7,401);ang=np.linspace(0,np.pi/2,49);rr=np.repeat(radial,49)
  ck('common19649geometry',len(X)==19649 and np.max(abs(X-(radial[:,None]*np.cos(ang)).ravel())/(1+rr))<2e-14 and np.max(abs(Y-(radial[:,None]*np.sin(ang)).ravel())/(1+rr))<2e-14)
  r2=10**(-3+(np.arange(277)+.371)/277*10);t2=np.r_[0,(np.arange(39)+.271)/39*np.pi/2,np.pi/2];xx=(r2[:,None]*np.cos(t2)).ravel();yy=(r2[:,None]*np.sin(t2)).ravel();yy[::41]=0;xx[40::41]=0;rshift=np.repeat(r2,41);ck('independent11357geometry',len(xx)==11357 and np.all(yy[::41]==0)and np.all(xx[40::41]==0))
  coords={'common':(X,Y),'shifted':(xx,yy)};fields={};prior_arrays={}
  for n in [160,192]:
   ap=P/('hsG_c2.0_N'+str(n)+'_log_independent.npz');bind(ap,prev['array_hashes'][str(ap)]);prior_arrays[n]=dict(np.load(ap));ck(str(n)+' exact common coordinates',np.array_equal(prior_arrays[n]['X'],X)and np.array_equal(prior_arrays[n]['Y'],Y))
  for n,path in [(160,middle['state']['path']),(192,old['state']['path']),(224,new['frozen'])]:
   print('START',n,utc(),flush=True)
   with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(path)
   ck(str(n)+'metadata',(q.N,q.M,q.cl,q.kappa,q.p,q.L)==(n,n//4,2.,2.,.5,1.));j=CartesianQJet(q);fields[n]={}
   for label,(x,y)in coords.items():
    z=j.jet(x,y);ck(str(n)+label+'finite schema',z.shape==(len(x),4)and np.isfinite(z).all());ck(str(n)+label+'horizontal parity',np.all(z[y==0,0]==0)and np.all(z[y==0,1]==0));fields[n][label]=z
   if n in prior_arrays:ck(str(n)+' prior independent recomputation',np.array_equal(fields[n]['common'],prior_arrays[n]['jet']))
   probes=[]
   for px,py in ([]if n==160 else[(.037,.021),(.73,1.17),(0.,36.7),(1234.,3456.),(0.,1e7)]):
    values=[]
    for digits in [72,108]:
     with mp.workdps(digits):
      m=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);mj=m.jet(px,py);ck(str(n)+' scalar MP shape '+str((px,py,digits)),len(mj)==4 and all(isinstance(z,mp.mpf)for z in mj));values.append([mp.nstr(v,digits)for v in mj[:3]])
    with mp.workdps(108):
     v72=list(map(mp.mpf,values[0]));v108=list(map(mp.mpf,values[1]));r=mp.sqrt(mp.mpf(px)**2+mp.mpf(py)**2);scales=[mp.sqrt(1+r),1/mp.sqrt(1+r),1/mp.sqrt(1+r)];precision=max(abs(a-b)/s for a,b,s in zip(v72,v108,scales));doublefull=j.jet(px,py);ck(str(n)+' scalar Cartesian shape '+str((px,py)),doublefull.shape==(4,));double=doublefull[:3];error=max(abs(mp.mpf(float(a))-b)/s for a,b,s in zip(double,v108,scales));ck(str(n)+' MP precision '+str((px,py)),precision<mp.mpf('1e-55'),mp.nstr(precision,20));ck(str(n)+' Cartesian MP '+str((px,py)),error<mp.mpf('2e-9'),mp.nstr(error,20));
     centered=[]
     for factor in [mp.mpf(1),mp.mpf('.5')]:
      hx=mp.mpf('1e-28')*(1+abs(mp.mpf(px)))*factor;hy=mp.mpf('1e-28')*(1+abs(mp.mpf(py)))*factor;cx=(m.density(mp.mpf(px)+hx,py)-m.density(mp.mpf(px)-hx,py))/(2*hx);cy=(m.density(px,mp.mpf(py)+hy)-m.density(px,mp.mpf(py)-hy))/(2*hy);centered.append([cx,cy])
     fdchange=max(abs(a-b)/s for a,b,s in zip(centered[0],centered[1],scales[1:]));fdagreement=max(abs(a-b)/s for a,b,s in zip(centered[1],v108[1:],scales[1:]));ck(str(n)+' explicit centered step agreement '+str((px,py)),fdagreement<mp.mpf('1e-35'),mp.nstr(fdagreement,30));probes.append(dict(x=px,y=py,values=values,precision=mp.nstr(precision,30),weighted_error=mp.nstr(error,30),centered_values=[[mp.nstr(a,100)for a in z]for z in centered],centered_step_change=mp.nstr(fdchange,30),centered_agreement=mp.nstr(fdagreement,30)))
   outfile=V/(str(n)+'_fields.npz');np.savez_compressed(outfile,**{label:z for label,z in fields[n].items()});bind(outfile);out['states'].append(dict(N=n,source=path,sha256=sha(path),probes=probes));save();print('DONE',n,utc(),flush=True)
  for n in [192,224]:
   den=abs(fields[n]['common'][:,0]);ck(str(n)+' positive denominator regularizer invisibility',np.array_equal(den[den>0]+1e-300,den[den>0]))
  earlier=next(p for p in oldgate['pairs']if p['old']=='hsG_c2.0_N160_log'and p['new']=='hsG_c2.0_N192_log');out['baseline']={};out['annulus_increase']={}
  for label,mask in [('common_nominal',rr),('common_hypot',np.hypot(X,Y)),('shifted',np.hypot(xx,yy))]:
   key='shifted'if label=='shifted'else'common';out['comparisons'][label]=compare(fields[192][key],fields[224][key],coords[key],mask,mask);out['baseline'][label]=compare(fields[160][key],fields[192][key],coords[key],mask,mask)
   save();ck(label+' no nonzero/zero',all(z['nonzero_over_zero']==0 for z in out['comparisons'][label].values()));ck(label+' baseline no nonzero/zero',all(z['nonzero_over_zero']==0 for z in out['baseline'][label].values()))
   oldkey={'common_nominal':'from_intended_radius_masks','common_hypot':'from_export_coordinates','shifted':'independent_grid'}[label]
   for region in names:
    for metric in ['field','gradient','pointwise_relative']:
     aa=out['baseline'][label][region][metric];bb=earlier[oldkey][region][metric];ck(label+' defined baseline '+region+' '+metric,aa is not None and bb is not None,dict(recomputed=aa,previous=bb));av=aa['value'];bv=bb['value'];ck(label+' baseline '+region+' '+metric,abs(av-bv)<=128*np.finfo(float).eps*max(abs(av),abs(bv)),dict(recomputed=av,previous=bv))
   out['annulus_increase'][label]={}
   for metric in ['field','gradient','pointwise_relative']:
    aa=out['baseline'][label]['annulus'][metric];bb=out['comparisons'][label]['annulus'][metric];ck(label+' defined positive annulus baseline '+metric,aa is not None and bb is not None and aa['value']>0,dict(previous=aa,current=bb));av=aa['value'];bv=bb['value'];out['annulus_increase'][label][metric]=dict(previous=av,current=bv,ratio=bv/av,increased=bv>av)
  header=(V/'producer_firstlook.txt').read_text().splitlines();ck('producer printed column definitions','columns per region: max|dg|/(1+r)^p, max|dg|/|g_b|, max|d grad g|/(1+r)^(p-1)'in header[0]);ck('producer half open masks',all(t in header[1]for t in ['[0,0.1)','[0.1,1)','[1,100)','[100,10000)','[10000,1e+07)']))
  line=next(l for l in (V/'producer_firstlook.txt').read_text().splitlines()if l.startswith('192x48 -> 224x56'));tokens=line.split('224x56',1)[1].split();ck('fifteen actual decimal tokens',len(tokens)==15)
  for i,token in enumerate(tokens):
   region=names[i//3];metric=['field','pointwise_relative','gradient'][i%3];value=out['comparisons']['common_nominal'][region][metric]['value'];lo,hi,half=token_interval(token);inside=token_agrees(value,token);out['tokens'].append(dict(region=region,metric=metric,printed=token,value=value,half_width=str(half),agrees=inside))
  # A mismatch is an audit finding, not a driver failure.
  out['token_disagreement_count']=sum(not t['agrees']for t in out['tokens']);out['mask_conventions']={'common_nominal':'Nominal radius in masks and weights; outer_boundary is the nominal final ring','common_hypot':'Physical hypot radius in masks and weights; boundary need not equal the nominal final ring','shifted':'Physical hypot radius in masks and weights','full_sample':'All supplied points, including the outer ring'};out['production_history']='Different production modes and optimization histories; no increase is attributed to resolution alone.'
  out.update(status='PASS',count=len(checks),finished_utc=utc(),scope='Finite auxiliary trial function differences; these trials do not demonstrate convergence. No continuum norm ordering, inverse claim, convergence theorem or full-plane endpoint.');save();print('PASS',len(checks),out['annulus_increase'],utc(),flush=True)
 except Exception:
  out.update(status='FAIL',count=len(checks),finished_utc=utc(),traceback=traceback.format_exc());save();raise
if __name__=='__main__':main()

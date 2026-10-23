"""Independent arithmetic hand oracles and malformed-artifact tests."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,gzip,copy,math,traceback
import numpy as np
import larger_node_independent_arithmetic as q
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';D=V/'final_arithmetic_manufactures';D.mkdir(exist_ok=True);checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def reject(n,fn):
 try:fn()
 except (ValueError,ArithmeticError,AssertionError,TypeError,KeyError)as e:ck(n,True,str(e));return
 ck(n,False)
def chunk(folder,d):
 folder.mkdir(exist_ok=True);(folder/'chunk_0000000.json.gz').write_bytes(gzip.compress(json.dumps(d,sort_keys=True).encode(),mtime=0))
try:
 for p in [__file__,q.__file__,R/'FINAL_ARITHMETIC_PROOF.md',R/'FINAL_DIAGNOSTIC_ORDER_PROOF.md',R/'FINAL_DESIGN_REVIEW_RESOLUTION_PROOF.md']:bindings[str(p)]=sha(p)
 a=q.residual(F(1),F(2),list(map(F,[3,-2,4])),list(map(F,[5,-6])));ck('hand R,Nf,Nv',a==[F(-25),F(25),F(43),F(1),F(25,43)])
 a=q.residual(F(0),F(0),[F(0)]*4,[F(0)]*2);ck('both denominators zero undefined',a==[0,0,0,None,None]and q.same_round(None,float('nan'))and not q.same_round(None,0.))
 ck('exact binary64 interpretation',q.f(.1)==F(3602879701896397,36028797018963968))
 xy=np.array([[.05,0.],[.2,0.],[.3,0.]]);rr=np.array([[0,0,0,np.nan,np.nan],[1,2,3,.5,1/3],[-1,2,3,.5,1/3]])
 s=q.summarize(xy,rr);ck('undefined region and empty regions',s[0]['metrics']['Rf']['index']is None and s[0]['metrics']['Rf']['undefined_count']==1 and s[2]['count']==s[3]['count']==0);ck('first index exact ties',all(s[1]['metrics'][k]['index']==1 for k in ['absR','Rf','Rv']))
 f=q.four(F(1),F(2),list(map(F,[3,-2,4])),list(map(F,[4,-1,6])),list(map(F,[5,-6])),list(map(F,[7,-3])));ck('hand four combinations',f==dict(R00='-25',R10='-23',R01='-17',R11='-7',cross='8'))
 rows=[list(map(F,z))for z in [[1,-2],[-3,4],[5,-6]]];m,p,n=q.moments(rows,[F(1,2),F(1),F(2)],list(map(F,[2,3,4])),[0,1,2]);ck('hand six moments',m==list(map(F,[1,-2,-9,12,20,-24])));ck('hand six components',q.components(m,F(2))==list(map(F,[-11,-26,23,-12,-20,-48])))
 l=q.ledgers(m,p,n,F(2));ck('hand signed V1',l['components']['V1']==dict(positive='9',negative='-20',total='-11',sum_absolute='29',cancellation_ratio='29/11'));ck('hand signed V2',l['components']['V2']==dict(positive='24',negative='-50',total='-26',sum_absolute='74',cancellation_ratio='37/13'))
 ck('zero total cancellation undefined',q.signed_item(F(3),F(-3))['cancellation_ratio']is None);ck('both-zero discrepancy undefined',q.discrepancy(F(0),F(0))==dict(absolute='0',pure_relative=None,both_zero=True));reject('invalid signed decomposition',lambda:q.signed_item(F(-1),F(1)));reject('negative y outside ledger scope',lambda:q.ledgers(m,p,n,F(-2)))
 for text,want in [('1.25',F(5,4)),('-2.5e-3',F(-1,400)),('+.0',F(0)),('1e1000',F(10**1000))]:ck('decimal '+text,q.decimal(text)==want)
 for text in ['nan','inf','1/2','1e1001','1e-1001','',' 1','1 ','0x1.2',None,3,'1'*2049]:reject('invalid decimal '+str(text)[:20],lambda text=text:q.decimal(text))
 low=[[F(0),F(1)],[F(1),F(0)]];high=[[F(0),F(2)],[F(2),F(0)]];dd=[[F(0),F(2)],[F(2),F(0)]];c=q.compare(low,high,dd,F(1,100),F(1,10));ck('diagnostic failure order',c['precision_failed_entries']==[[0,1,'1/2'],[1,0,'1/2']]);ck('diagnostic zeros',c['zero_counts']==c['nearzero_counts']==[1,1]and not c['precision_diagnostic_passed']);ck('explicit legacy bothzero flag',c['double_pure_relative_maxima'][0]['both_zero'])
 data=dict(schema='FINITE_MP_DECIMALS_V1',total=2,digits=72,width=2,chunk_size=64,bindings={'synthetic':'hand'},start=0,stop=2,rows=[['1.25','-2.5'],['0.0','3e-2']]);data['rows_sha256']=hashlib.sha256(json.dumps(data['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest();folder=D/'valid';chunk(folder,data);r=q.read_chunks(folder,2,2,72,{'synthetic':'hand'},lambda p:None);ck('independent chunk full read',r==[[F(5,4),F(-5,2)],[F(0),F(3,100)]])
 for kind in ['schema','interval','length','width','digest','decimal','extra_key','binding']:
  d=copy.deepcopy(data)
  if kind=='schema':d['schema']='bad'
  elif kind=='interval':d['start']=1
  elif kind=='length':d['rows'].pop()
  elif kind=='width':d['rows'][0].pop();d['rows_sha256']=hashlib.sha256(json.dumps(d['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
  elif kind=='digest':d['rows_sha256']='0'*64
  elif kind=='decimal':d['rows'][0][0]='nan';d['rows_sha256']=hashlib.sha256(json.dumps(d['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
  elif kind=='extra_key':d['extra']=0
  elif kind=='binding':d['bindings']['synthetic']='changed'
  p=D/kind;chunk(p,d);reject('chunk '+kind,lambda p=p:q.read_chunks(p,2,2,72,{'synthetic':'hand'},lambda p:None))
 # Three chunks independently constructed, with hand-identifiable rows.
 folder=D/'multi129';folder.mkdir(exist_ok=True);expectedrows=[[str(i),str(-i)]for i in range(129)]
 for start in [0,64,128]:
  stop=min(129,start+64);d=dict(schema='FINITE_MP_DECIMALS_V1',total=129,digits=108,width=2,chunk_size=64,bindings={'synthetic':'multi129'},start=start,stop=stop,rows=expectedrows[start:stop]);d['rows_sha256']=hashlib.sha256(json.dumps(d['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest();(folder/f'chunk_{start:07d}.json.gz').write_bytes(gzip.compress(json.dumps(d).encode(),mtime=0))
 got=q.read_chunks(folder,129,2,108,{'synthetic':'multi129'},lambda p:None);ck('129 rows three chunks independent',got==[[F(i),F(-i)]for i in range(129)])
 p0=folder/'chunk_0000000.json.gz';p1=folder/'chunk_0000064.json.gz';p2=folder/'chunk_0000128.json.gz';b0,b1,b2=p0.read_bytes(),p1.read_bytes(),p2.read_bytes()
 p0.write_bytes(b1);p1.write_bytes(b0);reject('swapped complete chunks rejected',lambda:q.read_chunks(folder,129,2,108,{'synthetic':'multi129'},lambda p:None));p0.write_bytes(b0);p1.write_bytes(b1)
 p2.unlink();reject('missing last chunk rejected',lambda:q.read_chunks(folder,129,2,108,{'synthetic':'multi129'},lambda p:None));p2.write_bytes(b2)
 ck('restored multichunk intact',q.read_chunks(folder,129,2,108,{'synthetic':'multi129'},lambda p:None)==got)
 reject('empty comparison rejected',lambda:q.compare([],[],[],F(1),F(1)))
 reject('ragged comparison rejected',lambda:q.compare([[F(1)]],[[F(1),F(2)]],[[F(1)]],F(1),F(1)))
 for name,exact,stored in [('positive denominator nan',F(1),float('nan')),('positive Rf nan',F(1,2),float('nan')),('undefined Rf finite',None,0.),('Nf oneulp',F(2),np.nextafter(2.,3.)),('Rf oneulp',F(1,2),np.nextafter(.5,1.))]:ck(name+' rejected',not q.same_round(exact,stored))
 ck('tie summary mutation rejected',dict(s[1]['metrics']['Rf'],index=2)!=s[1]['metrics']['Rf'])
 zero=q.compare([[F(0),F(0)]],[[F(0),F(0)]],[[F(0),F(0)]],F(1,100),F(1,10));ck('all-zero MP diagnostic explicit',zero['precision_diagnostic_passed']and zero['zero_counts']==[1,1]and all(x['both_zero']for x in zero['double_pure_relative_maxima']))
 ck('signed zero identified with zero',q.same_round(F(0),-0.))
 for p,h in bindings.items():ck('stable '+p,sha(p)==h)
 out=dict(status='PASS_INDEPENDENT_FINITE_ARITHMETIC_MANUFACTURES',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,artifacts={str(p):sha(p)for p in D.rglob('*')if p.is_file()})
except Exception:
 out=dict(status='FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,error=traceback.format_exc());print(out['error'])
(V/'FINAL_ARITHMETIC_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks))
if out['status']=='FAIL':raise SystemExit(1)

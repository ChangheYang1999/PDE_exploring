"""Fresh iv200 full propagation; every center interval is retained."""
from common import *
from math import comb
import argparse,importlib.util,gzip,time,resource

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--smoke',action='store_true');smoke=ap.parse_args().smoke;tag='smoke' if smoke else 'full';start=now();tick=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 if smoke:p,deps=base();prep=None
 else:
  p,deps,prep=preflight();qstatus=load(B/'research/radial_tm_refined/evidence/queue_status.json');need(qstatus['status']=='COMPUTATION_AND_AUDITS_COMPLETE_REQUIRES_VERIFIER_CLOSURE','162 heavy queue must already be terminal');need(os.getpriority(os.PRIO_PROCESS,0)>=19,'full computation lowest CPU priority');chronology(qstatus['utc'],start)
 spec=importlib.util.spec_from_file_location('accepted_exact_particular_engine',B/ENGINE);g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g);need(g.iv.dps==200,'fixed iv200');source=g.source();geometry,targets=coordinates();groups={si:[v for v in geometry if v['span']==si] for si in range(1558)}
 for v in geometry:need(list(map(g.q,[v['a_exact'],v['b_exact']]))==source['knots'][v['span']:v['span']+2],'source and partition exact span agreement')
 outfile=E/(tag+'_centers.jsonl.gz');need(not outfile.exists() and not(E/(tag+'_summary.json')).exists(),'fresh producer output; never resume or overwrite');counts=dict.fromkeys(COUNTS,0);counts['exact_anchors']=783;minimum={};selected={'I':[],'J':[]};elapsed=[]
 widths=[source['knots'][i+1]-source['knots'][i] for i in range(1558)];zmin=min([6*h for h in widths]+[2*h for h in widths]+[6*(g.q(v['t_exact'])-g.q(v['a_exact'])) for v in geometry]+[2*(g.q(v['b_exact'])-g.q(v['t_exact'])) for v in geometry]);need(zmin>0,'minimum nonzero exact exponential argument')
 prefix=hashlib.sha256();file=outfile.open('xb');gz=gzip.GzipFile(filename='',fileobj=file,mode='wb',compresslevel=1,mtime=0)
 def emit(v):
  b=canonical(v);gz.write(b);prefix.update(b)
 def state_sha(values):return hashlib.sha256(canonical([[[int(x) for x in endpoint] for endpoint in value._mpi_] for value in values])).hexdigest()
 header={'type':'header','schema':'ipm-canonical-centers-second-v1','utc':now(),'start_utc':start,'full_run':not smoke,'iv_dps':200,'geometry':geometry,'source_sha256':sha(B/SOURCE),'normalization_sha256':sha(B/ZPATH),'target_sha256':sha(B/TARGET),'partition_sha256':sha(B/PARTITION),'cert_green_sha256':sha(GREEN),'preflight_sha256':None if smoke else sha(E/'preflight_manifest.json'),'code_birth_sha256':sha(D/'data_exact/code_birth.json'),'producer_sha256':sha(Path(__file__)),'engine_sha256':sha(B/ENGINE),'anchor_checks':source['anchor_checks'],'I0_exact':list(map(str,source['I0'])),'U0_exact':list(map(str,source['U0'])),'V0_exact':list(map(str,source['V0'])),'Z_exact':source['Z_exact'],'minimum_nonzero_abs_zeta_exact':str(zmin),'expected_full_counts':COUNTS,'scope':'Actual fresh propagation; smoke is never a full integration. No endpoint archive values are propagation inputs.'};emit(header)
 try:
  # Density coefficient binding is complete even in the short diagnostic.
  for point in geometry:
   si=point['span'];h=g.q(point['b_exact'])-g.q(point['a_exact']);xi=g.q(point['xi_exact']);P=g.polynomials(source,si);exact=[]
   for j in range(262):
    row=[]
    for power in range(8):
     value=sum((P[j][k]*comb(k,power)*xi**(k-power) for k in range(power,8)),g.fmpq(0))/h**power;lo,hi=g.decode(targets[point['cell']]['density_polynomial_at_point'][j][power]);need(lo<=value<=hi,'unchanged density target containment');row.append(str(value));counts['H_coefficients']+=1
     if j==261:need(value==lo==hi==0,'exact zero density slot target')
    exact.append(row)
   emit({'type':'density','utc':now(),'cell':point['cell'],'span':si,'t_exact':point['t_exact'],'coefficients':exact,'count':2096})
  I=list(map(g.ii,source['I0']));U=list(map(g.ii,source['U0']));V=list(map(g.ii,source['V0']))
  def compare(family,point,values):
   recs=[];ci=point['cell'];selected[family].append(ci)
   for n,y in enumerate(values,1):
    lo,hi=g.ends(y);tl,tu=g.decode(targets[ci][family.lower()][n-1]);need(tl<=lo<=hi<=tu,f'fixed center containment {family} cell{ci} n{n}');record={'mode':n,'candidate':list(map(str,[lo,hi])),'target':list(map(str,[tl,tu]))};recs.append(record);counts[family+'_targets']+=1
    if family=='J' and n==261:need(lo==hi==tl==tu==0,'exact zero J261 target')
    if tl<tu:
     margin=min(lo-tl,tu-hi)/(tu-tl)
     if family not in minimum or margin<g.q(minimum[family]['relative_margin']):minimum[family]={'cell':ci,'mode':n,'relative_margin':str(margin),'candidate':record['candidate'],'target':record['target']}
   emit({'type':'moments','utc':now(),'family':family,'cell':ci,'span':point['span'],'t_exact':point['t_exact'],'records':recs,'count':261})
  for family,spans in [('I',[0] if smoke else range(1558)),('J',[1557] if smoke else reversed(range(1558)))]:
   for si in spans:
    a,b=source['knots'][si:si+2];h=b-a;P=g.polynomials(source,si)
    for point in (groups[si] if family=='I' else reversed(groups[si])):
     xi=g.q(point['xi_exact']);d=(xi if family=='I' else 1-xi)*h;vals=[]
     for n in range(1,262):
      if family=='I':Qp=[P[n-1][k]*xi**k for k in range(8)];val=g.step(I[n-1],Qp,d,-2*n-4)
      else:
       Qp=[(-(1-xi))**power*sum((P[n][k]*comb(k,power) for k in range(power,8)),g.fmpq(0)) for power in range(8)];lam=4-2*n;val=g.step(U[n-1],Qp,d,lam)+V[n-1]*g.iv.exp(g.ii(lam*d))*source['Z']
      vals.append(val);counts['center_steps_'+family]+=1
     compare(family,point,vals)
    if family=='I':I=[g.step(I[n-1],P[n-1],h,-2*n-4) for n in range(1,262)];st=state_sha(I)
    else:
     U=[g.step(U[n-1],g.reverse_poly(P[n]),h,4-2*n) for n in range(1,262)];V=[V[n-1]*g.iv.exp(g.ii((4-2*n)*h)) for n in range(1,262)];st=hashlib.sha256((state_sha(U)+state_sha(V)).encode()).hexdigest()
    counts['spans_'+family]+=1;counts['full_steps_'+family]+=261;emit({'type':'span','utc':now(),'family':family,'span':si,'a_exact':str(a),'b_exact':str(b),'steps':261,'state_sha256':st})
    if si%50==0 or smoke:gz.flush();file.flush();print(json.dumps({'utc':now(),'family':family,'span':si,'full_run':not smoke,'seconds':time.monotonic()-tick,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
  if not smoke:need(counts==COUNTS and selected['I']==CELLS and selected['J']==list(reversed(CELLS)),'complete actual full coverage')
  foot={'type':'complete','utc':now(),'full_run':not smoke,'counts':counts,'center_cells':selected,'prefix_sha256':prefix.hexdigest()};gz.write(canonical(foot));gz.close();file.close();rehash(p)
  out={'start_utc':start,'utc':now(),'status':'COMPUTED_COMPLETE_CENTERS_REQUIRES_INDEPENDENT_AUDIT' if not smoke else 'OPEN_SHORT_CENTER_PROPAGATION_DIAGNOSTIC','full_run':not smoke,'counts':counts,'center_cells':selected,'iv_dps':200,'anchor_checks':source['anchor_checks'],'minimum_nonzero_abs_zeta_exact':str(zmin),'worst_relative_margins':minimum,'output_sha256':sha(outfile),'producer_sha256':sha(Path(__file__)),'engine_sha256':sha(B/ENGINE),'source_sha256':sha(B/SOURCE),'target_sha256':sha(B/TARGET),'normalization_sha256':sha(B/ZPATH),'partition_sha256':sha(B/PARTITION),'code_birth_sha256':sha(D/'data_exact/code_birth.json'),'preflight_sha256':None if smoke else sha(E/'preflight_manifest.json'),'seconds':time.monotonic()-tick,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'All center endpoint pairs retained. Canonical enclosure correctness uses the reviewed global integration and trusted outward arithmetic; no third integration.'};write(E/(tag+'_summary.json'),out);print(json.dumps(out),flush=True)
 except BaseException:
  gz.close();file.close();raise
if __name__=='__main__':main()

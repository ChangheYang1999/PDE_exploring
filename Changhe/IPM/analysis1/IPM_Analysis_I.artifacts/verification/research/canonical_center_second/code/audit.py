"""Fraction re-read of every pair, independent Newton density/anchor construction."""
from common import *
from math import comb,factorial
import argparse,importlib.util,gzip,bisect,time,resource

def ball(v):
 need(type(v) is dict and set(v)=={'schema','mid_m','mid_e','rad_m','rad_e'} and v['schema']=='arb-dyadic-mid-radius-v1','strict original dyadic ball schema')
 values=[]
 for k in ['mid_m','mid_e','rad_m','rad_e']:
  x=v[k];need(type(x) in [str,int] and re.fullmatch(r'-?\d+',str(x)) is not None,'strict integer dyadic field');values.append(int(x))
 m,e,r,f=values;need(r>=0,'nonnegative exact radius');mid=Q(m)*Q(2)**e;radius=Q(r)*Q(2)**f;return mid-radius,mid+radius

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--smoke',action='store_true');smoke=ap.parse_args().smoke;tag='smoke' if smoke else 'full';start=now();tick=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 if smoke:p,deps=base()
 else:p,deps,prep=preflight()
 spec=importlib.util.spec_from_file_location('independent_recursive_Newton_source',B/NEWTON);api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
 summary=load(E/(tag+'_summary.json'));path=E/(tag+'_centers.jsonl.gz');need(summary['full_run'] is (not smoke) and summary['status']==('OPEN_SHORT_CENTER_PROPAGATION_DIAGNOSTIC' if smoke else 'COMPUTED_COMPLETE_CENTERS_REQUIRES_INDEPENDENT_AUDIT') and summary['output_sha256']==sha(path) and summary['producer_sha256']==sha(D/'code/full.py') and summary['engine_sha256']==sha(B/ENGINE) and summary['code_birth_sha256']==sha(D/'data_exact/code_birth.json'),'actual producer/source/output binding')
 if not smoke:need(summary['preflight_sha256']==sha(E/'preflight_manifest.json'),'same accepted preparation')
 raw=load(B/SOURCE);t=list(map(api.exact_hex,raw['arrays']['knots']['hex']));knots=sorted(set(t));need(len(t)==1573 and len(knots)==1559 and raw['degree']==7,'exact independent source dimensions');S=list(map(api.exact_hex,raw['arrays']['S']['hex']));need(len(S)==260*1565,'all original controls');sc={k:api.exact_hex(v) for k,v in raw['scalars_hex'].items()};samples=load(B/TARGET)['samples'];need([v['cell'] for v in samples]==CELLS,'fixed target cells');targets={v['cell']:v for v in samples};part=load(B/PARTITION);need(part['input_sha256']==FIXED_INPUTS[SOURCE] and part['grid_sha256']==FIXED_INPUTS[str(GREEN)] and part['cells']==7809 and len(part['spans'])==1558,'actual exact partition construction')
 geometry=[];owner={};first=0
 for si,v in enumerate(part['spans']):
  a,b=knots[si:si+2];h=b-a;need(v['span']==si and v['first_cell']==first and Q(v['a_exact'])==a and Q(v['b_exact'])==b and type(v['count']) is int and v['count']>0,'complete independent partition span');count=v['count']
  for ci in CELLS:
   if first<=ci<first+count:
    target=targets[ci];left=a+h*Q(ci-first,count);right=a+h*Q(ci-first+1,count);tc=Q(target['t_exact']);need(list(map(Q,target['cell_endpoints_exact']))==[left,right] and a<=left<tc<right<=b and tc==(left+right)/2,'exact closed cell and interior center');owner[ci]=si;geometry.append({'cell':ci,'span':si,'t_exact':str(tc),'cell_endpoints_exact':list(map(str,[left,right])),'a_exact':str(a),'b_exact':str(b),'xi_exact':str((tc-a)/h)})
  first+=count
 need(first==7809 and [v['cell'] for v in geometry]==CELLS,'all independent center geometries');groups={i:[v for v in geometry if v['span']==i] for i in range(1558)}
 W=[{} for _ in range(262)]
 for m in range(260):
  for frequency in [1+2*m,1-2*m,3+2*m,3-2*m]:
   j=(abs(frequency)-1)//2;W[j][m]=W[j].get(m,Q(0))+Q(1 if frequency>0 else -1,8)
 W=[{m:v for m,v in row.items() if v} for row in W];need(W[-1]=={},'independent zero density slot')
 def bases(si):
  a,b=knots[si:si+2];ell=bisect.bisect_right(t,a)-1;result=[api.recursive_basis(t,ell,a+(b-a)*Q(k+1,9)) for k in range(8)];need(all(sum(row,Q(0))==1 for row in result),'recursive partition of unity at eight exact points');return ell,result
 def values(si,j,basis):
  ell,rows=basis;control=[sum((w*S[m*1565+i] for m,w in W[j].items()),Q(0)) for i in range(ell-7,ell+1)];return [sum((w*c for w,c in zip(row,control,strict=True)),Q(0)) for row in rows]
 expected=[]
 for point in geometry:expected.append(('density',point['cell']))
 for family,spans in [('I',[0] if smoke else range(1558)),('J',[1557] if smoke else reversed(range(1558)))]:
  for si in spans:
   for point in (groups[si] if family=='I' else reversed(groups[si])):expected.append(('moments',family,point['cell']))
   expected.append(('span',family,si))
 counts=dict.fromkeys(COUNTS,0);counts['exact_anchors']=783;minimum={};zero_targets=0;digest=hashlib.sha256();newton_digest=hashlib.sha256();previous=start;center_cells={'I':[],'J':[]}
 with gzip.open(path,'rb') as f:
  def line():
   b=f.readline();need(b and b.endswith(b'\n'),'complete newline JSON record');v=parse(b);return b,v
  hb,head=line();digest.update(hb);need(head['type']=='header' and head['schema']=='ipm-canonical-centers-second-v1' and head['full_run'] is (not smoke) and head['iv_dps']==200 and head['anchor_checks']==3915 and head['expected_full_counts']==COUNTS and head['geometry']==geometry,'complete actual header and independent geometry');need(head['producer_sha256']==summary['producer_sha256'] and head['engine_sha256']==summary['engine_sha256'] and head['code_birth_sha256']==summary['code_birth_sha256'] and head['preflight_sha256']==summary['preflight_sha256'],'header source/preparation identity')
  for key,source in [('source_sha256',SOURCE),('target_sha256',TARGET),('normalization_sha256',ZPATH),('partition_sha256',PARTITION),('cert_green_sha256',str(GREEN))]:need(head[key]==FIXED_INPUTS[source] and (key=='cert_green_sha256' or summary[key]==head[key]),'unchanged defining input '+key)
  chronology(head['start_utc'],head['utc']);previous=head['utc']
  for event in expected:
   rb,row=line();digest.update(rb);chronology(previous,row['utc']);previous=row['utc'];need(row['type']==event[0],'exact event order')
   if event[0]=='density':
    ci=event[1];si=owner[ci];target=targets[ci];tc=Q(target['t_exact']);a,b=knots[si:si+2];h=b-a;xi=(tc-a)/h;need(row['cell']==ci and row['span']==si and Q(row['t_exact'])==tc and row['count']==2096 and len(row['coefficients'])==262 and all(len(v)==8 for v in row['coefficients']),'complete density row identity');basis=bases(si)
    for j in range(262):
     # Nodes are u=(k+1)/9. x=9*(xi+s/h)-1 converts Newton node index to physical s.
     actual=api.newton_coefficients(values(si,j,basis),9*xi-1,9/h)
     for power,value in enumerate(actual):
      lo,hi=ball(target['density_polynomial_at_point'][j][power]);need(Q(row['coefficients'][j][power])==value and lo<=value<=hi,'every independent physical-center Newton coefficient');counts['H_coefficients']+=1;newton_digest.update(canonical([ci,j,power,str(value)]))
      if j==261:need(value==lo==hi==0,'exact zero H target')
   elif event[0]=='moments':
    family,ci=event[1:];target=targets[ci];need(row['family']==family and row['cell']==ci and row['span']==owner[ci] and Q(row['t_exact'])==Q(target['t_exact']) and row['count']==261 and [v['mode'] for v in row['records']]==list(range(1,262)),'complete exact moment identity');center_cells[family].append(ci)
    for rec in row['records']:
     n=rec['mode'];tl,tu=ball(target[family.lower()][n-1]);need(len(rec['candidate'])==len(rec['target'])==2,'exact endpoint pair shape');lo,hi=map(Q,rec['candidate']);need(tuple(map(Q,rec['target']))==(tl,tu) and tl<=lo<=hi<=tu,'each saved pair contained in unchanged exact mode n-1 target');counts[family+'_targets']+=1;counts['center_steps_'+family]+=1;zero_targets+=tl==tu
     if family=='J' and n==261:need(tl==lo==hi==tu==0,'exact zero J261')
     if tl<tu:
      margin=min(lo-tl,tu-hi)/(tu-tl)
      if family not in minimum or margin<Q(minimum[family]['relative_margin']):minimum[family]={'cell':ci,'mode':n,'relative_margin':str(margin),'candidate':rec['candidate'],'target':rec['target']}
   else:
    family,si=event[1:];need(row['family']==family and row['span']==si and Q(row['a_exact'])==knots[si] and Q(row['b_exact'])==knots[si+1] and row['steps']==261 and re.fullmatch('[0-9a-f]{64}',row['state_sha256']) is not None,'all source-ordered span records');counts['spans_'+family]+=1;counts['full_steps_'+family]+=261
  fb,foot=line();need(foot['type']=='complete' and foot['full_run'] is (not smoke) and foot['counts']==summary['counts']==counts and foot['center_cells']==summary['center_cells']==center_cells and foot['prefix_sha256']==digest.hexdigest() and not f.read(),'complete stream footer and no omitted/extra records');chronology(previous,foot['utc'],summary['utc'],start)
 # Independently reconstruct every exact infinite anchor, without importing engine.py.
 endpoint=[]
 for si,right in [(0,False),(1557,True)]:
  h=knots[si+1]-knots[si];basis=bases(si);rows=[]
  for j in range(262):
   P=api.newton_coefficients(values(si,j,basis),Q(-1),Q(9));rows.append([sum((P[k]*Q(factorial(k),factorial(k-v)) for k in range(v,8)),Q(0))/h**v if right else P[v]*factorial(v)/h**v for v in range(7)])
  endpoint.append(rows)
 def angular(name,width):
  data=list(map(api.exact_hex,raw['arrays'][name]['hex']));need(len(data)==260*width,'entire exact tail array');return [[sum((v*data[m*width+i] for m,v in row.items()),Q(0)) for i in range(width)] for row in W]
 hd=angular('D',7);ha=angular('Aout',10);bi,bo=sc['bi'],sc['bo'];alpha=[sc['k']-3-j*(1-sc['k'])-2*l for j,l in raw['outer_jl']];need(len(alpha)==10 and raw['outer_jl'][0]==[0,0] and all(x<-2 for x in alpha),'exact outer exponents');anchors={k:[] for k in ['I0_exact','U0_exact','V0_exact']}
 def correction(g,beta):
  out=[]
  for v in range(7):out.append((g[v]-sum((comb(v,l)*factorial(l)*out[l]*beta**(v-l) for l in range(v)),Q(0)))/factorial(v))
  return out
 for n in range(1,262):
  m=2*n;C=W[n-1].get(0,Q(0));inner_discrepancy=[endpoint[0][n-1][v]-(C if v==0 else 0)-sum((hd[n-1][l]*(2*l+2)**v for l in range(7)),Q(0)) for v in range(7)];e=correction(inner_discrepancy,bi);need(m+4+bi>0 and m-4+bo>0 and all(m-4-x>0 for x in alpha),'every positive exact tail denominator');I=C/(m+4)+sum((hd[n-1][l]/(m+6+2*l)+e[l]*(-1)**l*factorial(l)/(m+4+bi)**(l+1) for l in range(7)),Q(0));outer_discrepancy=[endpoint[1][n][v]-sum((ha[n][l]*alpha[l]**v for l in range(10)),Q(0)) for v in range(7)];e=correction(outer_discrepancy,-bo);U=sum((ha[n][l]/(m-4-alpha[l]) for l in range(10)),Q(0))+sum((e[l]*factorial(l)/(m-4+bo)**(l+1) for l in range(7)),Q(0));C=W[n].get(0,Q(0));V=C*(alpha[0]+bo)**7/((m-4-alpha[0])*(m-4+bo)**7)
  for key,value in [('I0_exact',I),('U0_exact',U),('V0_exact',V)]:anchors[key].append(str(value))
 for key,values_ in anchors.items():need(values_==head[key],'all independent exact analytic anchors '+key)
 z=load(B/ZPATH)['values']['A00_correction'];need(list(map(Q,head['Z_exact']))==[Q(z['lower_exact_dyadic']),Q(z['upper_exact_dyadic'])],'same distinguished normalization enclosure');widths=[b-a for a,b in zip(knots,knots[1:])];zmin=min([6*h for h in widths]+[2*h for h in widths]+[6*(Q(v['t_exact'])-Q(v['a_exact'])) for v in geometry]+[2*(Q(v['b_exact'])-Q(v['t_exact'])) for v in geometry]);need(Q(head['minimum_nonzero_abs_zeta_exact'])==Q(summary['minimum_nonzero_abs_zeta_exact'])==zmin>0 and summary['worst_relative_margins']==minimum,'independent argument minimum and all worst margins')
 if not smoke:need(counts==COUNTS and center_cells=={'I':CELLS,'J':list(reversed(CELLS))},'actual full counts and centers')
 rehash(p);out={'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_CENTER_SAVED_PAIR_NEWTON_DENSITY_AND_ANCHOR_AUDIT' if not smoke else 'PASS_SHORT_CENTER_DIAGNOSTIC_AND_COMPLETE_EXACT_DENSITY_ANCHOR_AUDIT','full_run':not smoke,'counts':counts,'all_saved_moment_pairs':counts['I_targets']+counts['J_targets'],'independent_exact_density_coefficients':counts['H_coefficients'],'independent_exact_anchors':783,'saved_zero_targets':zero_targets,'center_cells':center_cells,'minimum_nonzero_abs_zeta_exact':str(zmin),'worst_relative_margins':minimum,'Newton_values_sha256':newton_digest.hexdigest(),'output_sha256':sha(path),'summary_sha256':sha(E/(tag+'_summary.json')),'auditor_sha256':sha(Path(__file__)),'Newton_source_sha256':sha(B/NEWTON),'code_birth_sha256':sha(D/'data_exact/code_birth.json'),'preflight_sha256':None if smoke else sha(E/'preflight_manifest.json'),'seconds':time.monotonic()-tick,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Complete re-read of every retained pair and independent exact Newton reconstruction of all27248 density coefficients and783 analytic anchors. Does not re-integrate I/J; enclosure correctness uses the reviewed executed global second integration. No third integration.'};write(E/(tag+'_output_audit.json'),out);print(json.dumps(out),flush=True)
if __name__=='__main__':main()

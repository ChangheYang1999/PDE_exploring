"""Independent binary decoding, exact geometry and saved-output composition audit."""
from common import *
import numpy as np
import time,copy,operator
ctx.prec=512;iv.dps=170
PACKSHA=['6905d8c29ea38679b60838efc428578be2c854e35c2d4c08e6910527428e32fa','cd09c72f3021acea4f6edc320b60300483c6985f85658e6ebbdcb1683e81a093','5b7594cc08b19a9cf5c56e9b44d577d529f643983bd96c6020c0c7fae764659f']
RADSHA=['e78ba5fb2aa01d55c92dc4467c37cbc08403879d8fc0d3759da1fdceb06686c7','1ba5c8e2f6488b968f9fc381ad88b6b3cfe98729321c3b3a35912d297b132765','8e289f4c15ab737c1649ff00e9e54cd211245c6a64516217bca600607816c80b']
PREP='research/flow_composition/evidence/preparation.json';PREPSHA='b375ec83f60ae3a561eb3f728b14e83bc9143e5507f47bfcf23e7243197d65e3'
CODE={'exact':('research/flow_composition/code/exact.py','e6195db43b33cb221ca2ad48af3cfb409171ce887fd4c9f190a48cf2a61331f8'),'iv':('research/flow_composition/code/second_iv.py','d3e1f870a09f86a67520720a58173096f77fb8edcdaa2f18961ebb05c130eb5d')}
SHAPES={**{s:(261,13) for s in ['P_mid','P_rad','R_mid','R_rad']},**{s:(261,) for s in ['P_rem','R_rem']},'scalar':(36,),'angular_mid':(3,3,3,261),'angular_rad':(3,3,3,261),'angular_rem':(3,3,261),'d':(3,),'nodes':(3,3),'cl':(2,),'ell':(1,),**{'target_'+n+'_'+s:(3,) for n in NAMES for s in ['lo','hi']}}
def binary64(raw):
 bits=int.from_bytes(raw,'little');ex=(bits>>52)&2047;ma=bits&((1<<52)-1);need(ex!=2047,'finite IEEE754 input');power=-1074 if ex==0 else ex-1075;sig=ma if ex==0 else ma+(1<<52);v=F((-1 if bits>>63 else 1)*sig);v=v*2**power if power>=0 else v/F(2**(-power));need(v==F(struct.unpack('<d',raw)[0]),'manual IEEE754 equals independent float ratio');return v

def packet(path,meta):
 out={};raws={};count=0
 with zipfile.ZipFile(path) as z,np.load(path,allow_pickle=False) as independent:
  need(len(z.namelist())==len(set(z.namelist())) and set(z.namelist())=={k+'.npy' for k in SHAPES},'complete unique packet entries');need(set(meta)==set(SHAPES),'complete array hash manifest')
  for k,shape in SHAPES.items():
   b=z.read(k+'.npy');need(b[:6]==b'\x93NUMPY' and b[6:8] in [b'\x01\x00',b'\x02\x00'],'explicit NPY version');n=struct.unpack('<H' if b[6]==1 else '<I',b[8:10 if b[6]==1 else 12])[0];offset=10 if b[6]==1 else 12;h=ast.literal_eval(b[offset:offset+n].decode('latin1'));payload=b[offset+n:];dtype='<i8' if k=='nodes' else '<f8';need(set(h)=={'descr','fortran_order','shape'} and h['descr']==dtype and h['fortran_order'] is False and h['shape']==shape,'exact NPY schema');need(len(payload)==8*math.prod(shape),'complete NPY payload');need(meta[k]=={'shape':list(shape),'dtype':dtype,'sha256':hashlib.sha256(payload).hexdigest()},'exact packet payload hash');other=independent[k];need(other.shape==shape and other.dtype.str==dtype and other.tobytes(order='C')==payload,'independent NumPy packet decoder');raws[k]=payload;out[k]=[int.from_bytes(payload[i:i+8],'little',signed=True) if k=='nodes' else binary64(payload[i:i+8]) for i in range(0,len(payload),8)];count+=len(out[k])
   if k.endswith('_rad') or k.endswith('_rem'):need(all(x>=0 for x in out[k]),'all saved nonnegative radii/remainders')
 return out,raws,count

def contains(reference,target):
 r=list(map(ff,reference));t=list(map(ff,target));need(len(r)==len(t)==2 and r[0]<=r[1] and t[0]<=t[1],'ordered intervals');need(t[0]<=r[0]<=r[1]<=t[1],'reference inside target');m=[r[0]-t[0],t[1]-r[1]];q=[fmpq(reference[0])-fmpq(target[0]),fmpq(target[1])-fmpq(reference[1])];need(m==list(map(qf,q)),'independent fmpq interval margins');return m

def mpf_exact(v):
 sign,man,expo,bc=v;man=operator.index(man);expo=operator.index(expo);need(sign in (0,1) and man>=0 and bc>=0 and man.bit_length()==bc,'finite interval endpoint');return F((-1 if sign else 1)*man)*(F(2)**expo)
def iv_pair(x):return list(map(mpf_exact,x._mpi_))
def arb_pair(x):
 need(x.is_finite(),'finite Arb endpoint');a,b=x.lower().fmpq(),x.upper().fmpq();return [qf(a),qf(b)]
def aq(x):return arb(fmpq(str(x)))
def iq(x):return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def interval_record(ref,target):
 contains(list(map(str,ref)),list(map(str,target)));return {'reference':list(map(str,ref)),'target':list(map(str,target))}
def check_width(w,h,ell):need(0<w<=h<F(1,522) and h<=2*ell,'actual child and Bernstein radial cover')
def geometry(ci,row,scal,cl,ell):
 a,b=ff(row['a_exact']),ff(row['b_exact']);w=(b-a)/row['count'];left=a+(ci-row['first_cell'])*w;right=left+w;h=scal[0];check_width(w,h,ell);need(scal[2]>=0 and scal[4]>=0 and scal[8]>=0 and 0<scal[5]<=scal[6],'scalar positive hull and radii');contains([str(1/K)]*2,[str(cl[0]-cl[1]),str(cl[0]+cl[1])]);need(cl[1]>=0,'nonnegative cl radius')
 for j in range(27):need(h**j<=scal[9+j] and qf(fmpq(str(h))**j)==h**j,'independent exact h power upper')
 refs={};target=[scal[5],scal[6]]
 for label,fn,q in [('arb512',arb_pair,aq),('iv170',iv_pair,iq)]:
  el=fn(q(left).exp() if label=='arb512' else iv.exp(q(left)));er=fn(q(right).exp() if label=='arb512' else iv.exp(q(right)));refs[label]={'left_radial':interval_record(el,target),'right_radial':interval_record(er,target),'E_left':interval_record(el,[scal[1]-scal[2],scal[1]+scal[2]])}
 def mu(r):return F(1129,1000)+(F(129,20)+F(307,100)-F(1129,1000))/(1+(r/6)**4)
 mus=[mu(scal[6]),mu(scal[5])];need(mus==[qf(fmpq(1129,1000)+(fmpq(129,20)+fmpq(307,100)-fmpq(1129,1000))/(1+(fmpq(str(r))/6)**4)) for r in [scal[6],scal[5]]],'two independent rational mu evaluations');refs['mu']=interval_record(mus,[scal[7]-scal[8],scal[7]+scal[8]])
 return {'cell':ci,'parent':row['span'],'left':str(left),'right':str(right),'width':str(w),'h':str(h),'ell':str(ell),'checks':refs}

def polynomial_identities():
 # U_{n-1}(x) recurrence versus independent finite Chebyshev sum for C,S.
 def add(p,q,sgn=1):
  z=[0]*max(len(p),len(q))
  for i,v in enumerate(p):z[i]+=v
  for i,v in enumerate(q):z[i]+=sgn*v
  while len(z)>1 and z[-1]==0:z.pop()
  return z
 T=[[1],[0,1]]
 for n in range(2,262):T.append(add([0]+[2*x for x in T[-1]],T[-2],-1))
 um=[0];u=[1];h=hashlib.sha256()
 for n in range(1,262):
  c=[1];s=[(-1)**(n+1)]
  for j in range(1,n):c=add(c,[2*x for x in T[j]]);s=add(s,[2*(-1)**(n+j+1)*x for x in T[j]])
  c=add(c,T[n]);s=add(s,T[n],-1);need(c==add(u,[0]+u) and s==add(u,[0]+u,-1),'finite continuous quotient polynomial identity');majorant=8*n**3+16*(n*(n-1)//2)**2;need(majorant<=4*n**4+8*n**3+6*n**2+2*n,'independent third derivative sum majorant');h.update(json.dumps([n,c,s],separators=(',',':')).encode());um,u=u,add([0]+[2*x for x in u],um,-1)
 return h.hexdigest()

def mutations():
 cases=[]
 def run(name,fn,message=None):
  try:fn()
  except ValueError as e:
   need(message is not None and str(e)==message,'intended first failing mutation '+name);cases.append({'name':name,'result':'EXPECTED_REJECTION','reason':str(e)});return
  need(message is None,'mutation accepted '+name);cases.append({'name':name,'result':'PASS_CONTROL'})
 run('valid containment',lambda:contains(['0','1'],['-1','2']))
 run('reversed containment',lambda:contains(['-1','2'],['0','1']),'reference inside target')
 run('unordered reference',lambda:contains(['2','1'],['0','3']),'ordered intervals')
 run('unordered target',lambda:contains(['0','1'],['2','-1']),'ordered intervals')
 run('valid geometry',lambda:check_width(F(1,1000),F(1,900),F(1,1500)))
 for name,w,h,ell in [('negative width',F(-1,1000),F(1,900),F(1,1500)),('width over h',F(1,800),F(1,900),F(1,1500)),('h at threshold',F(1,1000),F(1,522),F(1,100)),('ell too small',F(1,1000),F(1,900),F(1,3000))]:run(name,lambda w=w,h=h,ell=ell:check_width(w,h,ell),'actual child and Bernstein radial cover')
 run('finite binary zero',lambda:binary64(bytes(8)))
 for v in [0x7ff0000000000000,0xfff0000000000000,0x7ff8000000000000]:run('nonfinite binary '+str(v),lambda v=v:binary64(v.to_bytes(8,'little')),'finite IEEE754 input')
 return cases

def main():
 t=time.monotonic();start=now();pins={};pr=proof(pins);deps=parents(pins);pin(pins,PREP,PREPSHA);prep=load(B/PREP);need(prep['nodes']==NODES and prep['radial_cells']==CELLS and len(prep['packets'])==3,'exact selected preparation identities');source=load(B/SOURCE);need(F(float.fromhex(source['scalars_hex']['k']))==K,'same exact unaltered source k');c173=load(B/'research/canonical_boundary_composition/evidence/checks.json');c157=load(B/'research/canonical_three_cell_linkage/evidence/checks.json');need(c173['source_sha256']==SSHA and ff(c173['k_exact'])==K and c173['partition_sha256']==PSHA,'canonical source k and partition binding');part=load(B/PART);need(part['input_sha256']==SSHA and part['cells']==7809 and len(part['spans'])==1558,'exact source partition')
 for n in ['research/canonical_boundary_composition/evidence/checks.json','research/canonical_three_cell_linkage/evidence/checks.json']:need(n in pins,'accepted parent includes checked data')
 sc='research/flow_scalars/evidence/checks.json';need(sc in pins,'accepted scalar checks');scheck=load(B/sc);clrow=next(x for x in scheck['constants'] if x['name']=='cl');need(ff(clrow['exact'])==1/K,'exact topic75 cl constant');cl75=[F(float.fromhex(clrow[x])) for x in ['mid_hex','rad_hex']]
 scalfile='research/flow_scalars/evidence/scalar_arrays.npz';angfile='research/flow_angular/evidence/finite_arrays.npz';need(scalfile in pins and angfile in pins and sha(B/scalfile)==scheck['array_sha256'],'accepted scalar and angular arrays')
 # Resolve actual fixed accepted code paths by matching their pinned SHA.
 codes={}
 for method,(_,h) in CODE.items():
  matches=[n for n,v in deps['125']['files'].items() if n.endswith('.py') and v==h];need(len(matches)==1,'unique original125 actual method code');codes[method]=matches[0]
 stats={'packets':0,'packet_arrays':0,'decoded_entries':0,'radial_array_identities':0,'angular_array_identities':0,'remainder_checks_two_exact_methods':0,'saved_reference_containments_two_exact_methods':0,'saved_margins_two_exact_methods':0,'analytic_error_crosschecks':0};geos=[];rectangles=[];comparisons=[];minrec=None
 with np.load(B/scalfile,allow_pickle=False) as scz,np.load(B/angfile,allow_pickle=False) as az:
  anodes=az['nodes'];selected=az['selected'];aw=az['half_widths'];dw=az['distinct_half_widths']
  for ix,ci in enumerate(CELLS):
   pm=prep['packets'][ix];pn=f'research/flow_composition/evidence/packet_{ci:04d}.npz';rn=f'research/radial_tm_instance/evidence/selected_v3_cell_{ci:04d}.npz';need(pm['ci']==ci and pm['file']==pn and pm['sha256']==PACKSHA[ix] and pm['radial_input_file']==rn and pm['radial_input_sha256']==RADSHA[ix],'complete exact packet identities');pin(pins,pn,PACKSHA[ix]);pin(pins,rn,RADSHA[ix]);need(deps['125']['files'][pn]==PACKSHA[ix] and deps['93']['files'][rn]==RADSHA[ix],'same accepted125/93 packet identity');pk,raws,num=packet(B/pn,pm['arrays']);stats['packets']+=1;stats['packet_arrays']+=len(pk);stats['decoded_entries']+=num;need(pk['nodes']==sum(NODES,[]),'exact packet node order')
   with np.load(B/rn,allow_pickle=False) as rz:
    for key in ['P_mid','P_rad','P_rem','R_mid','R_rad','R_rem','scalar']:need(rz[key].dtype.str=='<f8' and rz[key].shape==SHAPES[key] and rz[key].tobytes()==raws[key],'entrywise canonical radial packet identity');stats['radial_array_identities']+=1
   need(scz['middle'][ci].tobytes()==raws['scalar'] and pk['cl']==cl75,'entrywise accepted scalar and cl identity');row=next(z for z in part['spans'] if z['first_cell']<=ci<z['first_cell']+z['count']);g=geometry(ci,row,pk['scalar'],pk['cl'],pk['ell'][0]);geos.append(g)
   for parent,key in [(c157,'cells'),(c173,'three_cells')]:
    old=parent[key][ix];need(old['cell']==ci and old['parent']==g['parent'] and old['left_exact']==g['left'] and old['right_exact']==g['right'] and old['h_upper_exact']==g['h'],'same canonical child geometry');need(old.get('candidate_sha256',old.get('saved_candidate_sha256'))==RADSHA[ix],'actual canonical theorem candidate identity')
   for ai,node in enumerate(NODES):
    sel=np.flatnonzero(np.all(selected==node,axis=1));orig=np.flatnonzero(np.all(anodes==node,axis=1));need(len(sel)==len(orig)==1,'unique actual accepted angular node');sidx=int(sel[0]);oidx=int(orig[0]);d=pk['d'][ai];need(F(float(aw[oidx]))==d,'same accepted node halfwidth');di=np.flatnonzero(dw==float(d));need(len(di)==1,'unique accepted remainder width');didx=int(di[0]);width=F(node[1]-node[0],102400)
    for label,actual in [('arb512',arb_pair(arb.pi()*aq(width))),('iv170',iv_pair(iv.pi*iq(width)))]:need(0<actual[0]<=actual[1]<=d,'two directed true angular halfwidths')
    for key,origkey in [('angular_mid','midpoints'),('angular_rad','radii')]:
     stride=3*3*261*8;need(raws[key][ai*stride:(ai+1)*stride]==az[origkey][sidx].tobytes(),'all selected angular coefficients identical');stats['angular_array_identities']+=1
    for kind in range(3):
     ref=az['remainder_arrays'][didx,0 if kind==0 else 1];stride=261*8;offset=(ai*3+kind)*stride;need(raws['angular_rem'][offset:offset+stride]==ref.tobytes(),'complete selected angular remainder identity');stats['angular_array_identities']+=1
     for n in range(1,262):
      majorant=8*n**3 if kind==0 else 4*n**4+8*n**3+6*n**2+2*n;q=F(majorant)*d**3/6;need(q==qf(fmpq(majorant)*fmpq(str(d))**3/6) and q<=pk['angular_rem'][(ai*3+kind)*261+n-1],'two exact angular cubic remainder uppers');stats['remainder_checks_two_exact_methods']+=1
    rectangles.append({'cell':ci,'angular_index':ai,'node':node,'log_radius':[g['left'],g['right']],'theta_over_pi':[str(F(node[0],51200)),str(F(node[1],51200))],'targets':{name:[str(pk['target_'+name+'_lo'][ai]),str(pk['target_'+name+'_hi'][ai])] for name in NAMES},'packet_path':pn,'packet_sha256':PACKSHA[ix],'canonical_radial_path':rn,'canonical_radial_sha256':RADSHA[ix]})
   runs={}
   for method in ['exact','iv']:
    path=f'research/flow_composition/evidence/{method}_{ci:04d}.json';need(path in deps['125']['files'],'actual accepted125 output pin');pin(pins,path,deps['125']['files'][path]);v=load(B/path);need(v['status']=='PASS' and v['ci']==ci and v['packet_sha256']==PACKSHA[ix] and v['preparation_sha256']==PREPSHA and v['code_sha256']==CODE[method][1] and len(v['rows'])==3,'complete accepted125 output identities');need(when(prep['utc'])<when(v['start_utc'])<when(v['end_utc'])<when(deps['125']['utc']),'actual125 completed before verdict');runs[method]=v
    for ai,r in enumerate(v['rows']):
     need(r['angular_index']==ai and r['node']==NODES[ai] and r['modal_products']==30537 and r['degree']==12 and r['radial_subintervals']==2 and [x['name'] for x in r['ranges']]==(NAMES if method=='exact' else ['s','v1x','v2y','T0']),'complete accepted125 row order and product scope')
     for data in r['ranges']:
      name=data['name'];target=[str(pk['target_'+name+'_lo'][ai]),str(pk['target_'+name+'_hi'][ai])];need(data['target']==target and data['contained'] is True,'unchanged target and actual saved success');margins=contains(data['reference'],target);need(list(map(str,margins))==data['margins'] and all(x>0 for x in margins),'all unchanged strict saved margins');stats['saved_reference_containments_two_exact_methods']+=1;stats['saved_margins_two_exact_methods']+=2;comparisons.append({'method':method,'cell':ci,'angular_index':ai,'node':NODES[ai],'function':name,'reference':data['reference'],'target':target,'margins':list(map(str,margins))})
      for side,margin in zip(['lower','upper'],margins):
       record={'method':method,'ci':ci,'angular_index':ai,'node':NODES[ai],'function':name,'endpoint':side,'margin_exact':str(margin)}
       if minrec is None or margin<ff(minrec['margin_exact']):minrec=record
   for ar,br in zip(runs['exact']['rows'],runs['iv']['rows']):
    for a in ar['ranges']:
     b=next(z for z in br['ranges'] if z['name']==a['name']);ae=ff(a['analytic_error']);be=list(map(ff,b['analytic_error_interval']));need(0<=be[0]<=ae<=be[1],'independent analytic error interval contains exact error');stats['analytic_error_crosschecks']+=1
 need(minrec=={k:v for k,v in deps['125']['minimum_margin_location'].items() if k!='record_sha256'},'recomputed actual smallest margin identity');expected={'packets':3,'packet_arrays':66,'decoded_entries':None,'radial_array_identities':21,'angular_array_identities':45,'remainder_checks_two_exact_methods':7047,'saved_reference_containments_two_exact_methods':72,'saved_margins_two_exact_methods':144,'analytic_error_crosschecks':36}
 for k,n in expected.items():
  if n is not None:need(stats[k]==n,'all expected counts '+k)
 symbols=polynomial_identities();tests=mutations();targets={'utc':now(),'source_sha256':SSHA,'normalization_sha256':ZSHA,'k_exact':str(K),'c_l_exact':str(1/K),'a_exact':'129/20','b_exact':'307/100','gamma_exact':'1129/1000','rectangles':rectangles,'scope':'Exactly nine closed rectangles; axis quotients continuously extended; distinguished z_star only.'};write(E/'targets_exact.json',targets);pin(pins,E/'targets_exact.json');rehash(pins);out={'start_utc':start,'utc':now(),'status':'PASS_NINE_CANONICAL_FLOW_RECTANGLES_REQUIRES_ACTUAL_REVIEW','source_sha256':SSHA,'normalization_sha256':ZSHA,'partition_sha256':PSHA,'accepted_dependencies':{n:{'path':DEPS[n][0],'sha256':DEPS[n][1],'utc':v['utc'],'status':v['status']} for n,v in deps.items()},'actual_proof_review':pr,'counts':stats,'polynomial_identities':{'modes':261,'identities':522,'two_constructions_sha256':symbols},'geometry':geos,'minimum_margin':minrec,'comparisons':comparisons,'executed_mutations':tests,'targets_sha256':sha(E/'targets_exact.json'),'runtime':{'python':sys.version,'arb_bits':ctx.prec,'iv_decimal_digits':iv.dps,'threads':1},'seconds':time.monotonic()-t,'files':dict(sorted(pins.items())),'scope':'Canonical premise substitution in accepted125. Fresh independent binary decoding, scalar geometry, angular remainder inequalities, polynomial identities, and all72 saved containments in Fraction and fmpq. Does not rerun inherited274833 modal products per engine. No historical array identity, angular cover, global flow, derivative norm, inverse, X3 distance, nonlinear closure or endpoint.'};write(E/'checks.json',out);print(json.dumps({k:out[k] for k in ['utc','status','counts','seconds']}))
if __name__=='__main__':main()

"""Conditional scalar assembly, without invoking a field or peer routine."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import ast,json,time
from flint import arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_registered_assembly';S=R/'research/candidate016_scaled_norm_peer/source'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(x):
 q=Q(x);return arb(q.numerator)/q.denominator
def exact(node):
 if isinstance(node,ast.Constant):return node.value
 if isinstance(node,ast.Tuple):return tuple(exact(x) for x in node.elts)
 if isinstance(node,ast.List):return [exact(x) for x in node.elts]
 if isinstance(node,ast.Dict):return {exact(k):exact(v) for k,v in zip(node.keys,node.values,strict=True)}
 if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='Q' and not node.keywords:return Q(*[exact(x) for x in node.args])
 if isinstance(node,ast.BinOp):
  x,y=exact(node.left),exact(node.right)
  if isinstance(node.op,ast.Add):return x+y
  if isinstance(node.op,ast.Sub):return x-y
  if isinstance(node.op,ast.Mult):return x*y
  if isinstance(node.op,ast.Pow):return x**y
  if isinstance(node.op,ast.Div):return Q(x)/Q(y)
 if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return -exact(node.operand)
 raise ValueError(ast.dump(node))
def bound(x,digits=12):
 scale=10**digits;lo=Q(int((x.lower()*scale).floor().unique_fmpz())-1,scale);hi=Q(int((x.upper()*scale).ceil().unique_fmpz())+1,scale)
 assert ar(lo)<x.lower() and x.upper()<ar(hi)
 return {'ball':x.str(90),'strict_lower_exact':str(lo),'strict_upper_exact':str(hi)}
def main():
 start=time.monotonic();ctx.prec=1536;target=B/'verification/result.json';assert not target.exists();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(p,actual,h);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 man=read(B/'source/MANIFEST.json')
 for rel,h in man['inputs'].items():bind(R/rel,h)
 nm=read(S/'MANIFEST_v02.json')
 for name,e in nm['files'].items():bind(S/name,e['sha256'])
 audit=read(R/'research/candidate016_scaled_norm_peer/verification/source_audit.json')
 for rel,h in audit['inputs'].items():bind(R/rel,h)
 pars=read(B/'source/parameters.json');norm=read(S/'N3_norms_complete_v02.json');peer=read(S/'N3_registered_norms_v01.json')
 checks['candidate_binding']=pars['candidate']==norm['name']==peer['id']=='C1-N1-016-legqs25-quot013' and pars['raw_sha256']==norm['source_sha256']==peer['source_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 comp={}
 for name in ['G0','G1','P2','rF']:
  n=norm['norms'][name];p=peer['components'][name]
  assert n['status']=='FINITE' and p['LB']==n['norm_lower'] and p['UB']==n['norm_upper']
  lower=arb(p['LB']).lower();upper=arb(p['UB']).upper();assert 0<lower<upper
  comp[name]=(lower,upper)
 checks['four_component_transcriptions']=True
 checks['H_proxy_only']=peer['components']['H']['LB']=='0' and 'UB only' in peer['components']['H']['label'] and arb(peer['components']['H']['UB']).upper()>comp['rF'][1] and 'Q3' not in norm['norms'] and 'Q3' not in peer['components']
 tree=ast.parse((S/'N3_assemble_norms_v01.py').read_text());constants={}
 for n in tree.body:
  if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['THRESH','XSW','GRADED_BOX']:constants[n.targets[0].id]=exact(n.value)
 assert set(constants)=={'THRESH','XSW','GRADED_BOX'}
 def match(container,prefix):
  hits=[(k,v) for k,v in container.items() if k==prefix or k.startswith(prefix+' ') or k.startswith(prefix+',')];assert len(hits)==1,(prefix,hits);return hits[0]
 def E(w1,w2):return tuple((comp['P2'][i]**2+w1*comp['G1'][i]**2+w2*comp['G0'][i]**2).sqrt() for i in [0,1])
 star=E(2**14,2**18);E2=(star[0],(star[1]**2+ar(Q(2**18*20,21))*comp['rF'][1]**2).sqrt())
 for label,prefix,val in [('E_star','E_star',star),('E2','E_2',E2)]:
  _,p=match(peer['derived'],prefix);checks[label+'_outward_display']=ar(p['LB'])<val[0] and val[1]<ar(p['UB'])
 sq={'P2^2':comp['P2'][1]**2,'2^14 G1^2':2**14*comp['G1'][1]**2,'2^18 G0^2':2**18*comp['G0'][1]**2,'2^18 (20/21) H^2':ar(Q(2**18*20,21))*comp['rF'][1]**2}
 checks['all_four_weighted_square_uppers']=all(v<ar(peer['derived']['weighted squares UB'][k]) for k,v in sq.items())
 instances=[]
 for name,ss,tt,usedtt in pars['Ns']+[pars['legacy_X3']]:
  s,threshold,used=Q(ss),Q(tt),Q(usedtt);assert 0<s<Q(1,34)
  key,actual=match(constants['THRESH'],name);kind,code_s,code_thr=actual
  assert kind==('X3' if name==pars['legacy_X3'][0] else 'Ns') and code_s==s and code_thr==used
  p=peer['thresholds'][key];low=(1-ar(34*s))*(star[0] if kind=='X3' else E2[0]);ratio=low/ar(threshold);usedratio=low/ar(used)
  assert ar(p['LB'])<low and p['UB'] is None and p['UB/threshold'] is None and ratio>1
  # Ratios in the old output are containing strings of a computed lower endpoint.
  # We do not promote their full precision. Verify conservative integer floors
  # independently, and retain the exact discrepancy of the threshold divisor.
  pr=arb(p['LB/threshold']);agreement=abs(pr-usedratio)<ar(Q(1,10**60));assert agreement
  instances.append({'framework':name,'kind':kind,'s_exact':str(s),'threshold_exact':str(threshold),'peer_used_threshold_exact':str(used),'lower_comparison':bound(low),'correct_source_ratio':bound(ratio,0),'peer_divisor_ratio':bound(usedratio,0),'displayed_lower_is_outward':True,'peer_ratio_matches_its_divisor_to_absolute_1e_minus60':True,'fractional_upper':'OPEN Q3 unavailable','conditional_sufficient_test_fails':True})
 checks['Ns_and_legacy_X3_source_formulas']=True
 for name,ss,w1,w2,cw,tt in pars['XSW']:
  s,threshold=Q(ss),Q(tt);assert 0<s<Q(1,2) and 1-Q(48,25)*s>0
  key,actual=match(constants['XSW'],name);assert actual==(s,w1,w2,Q(cw),threshold)
  p=peer['thresholds'][key];ew=E(w1,w2);low=(1-ar(Q(48,25)*s))*ew[0];ratio=low/ar(threshold)
  assert ar(p['E_w LB'])<ew[0] and ew[1]<ar(p['E_w UB']) and ar(p['LB'])<low
  assert p['UB'] is None and p['UB/threshold'] is None and Q(p['threshold'])==threshold and ratio>1
  assert abs(arb(p['LB/threshold'])-ratio)<ar(Q(1,10**60))
  instances.append({'framework':name,'kind':'XSW','s_exact':str(s),'weights':[w1,w2],'Cw_exact':str(Q(cw)),'threshold_exact':str(threshold),'E_lower':bound(ew[0]),'E_upper':bound(ew[1]),'lower_comparison':bound(low),'correct_source_ratio':bound(ratio,0),'displayed_lower_is_outward':True,'peer_ratio_matches_exact_divisor_to_absolute_1e_minus60':True,'fractional_upper':'OPEN Q3 unavailable','conditional_sufficient_test_fails':True})
 checks['five_XSW_source_formulas']=True
 graded=[]
 for prefix,ss in pars['graded']:
  s=Q(ss);key,(code_s,boxes)=match(constants['GRADED_BOX'],prefix);assert code_s==s and 0<s<1;p=peer['thresholds'][key]
  gamma={'gamma_0':(comp['G0'][0],comp['G0'][1]+ar(s)*comp['G1'][1]),'gamma_1':(comp['G1'][0],comp['G1'][1]+ar(s)*comp['P2'][1])}
  if boxes[3] is not None:gamma['gamma_H']=(arb(0),comp['rF'][1]+ar(s)*comp['G0'][1])
  assert p['gamma_2']['UB'] is None and p['first failing component (LB > box)']=='gamma_1'
  for k,(lo,hi) in gamma.items():
   assert (p[k]['LB']=='0' and lo==0) or ar(p[k]['LB'])<lo
   assert hi<ar(p[k]['UB'])
  assert gamma['gamma_1'][0]>ar(p['gamma_1']['box']) and gamma['gamma_0'][0]>ar(p['gamma_0']['box'])
  graded.append({'framework':key,'s_exact':str(s),'components':{k:{'lower':bound(lo),'upper':bound(hi)} for k,(lo,hi) in gamma.items()},'gamma0_gamma1_exceed_stated_box':True,'gamma2_upper':'OPEN Q3 unavailable','conditional_only':True})
 checks['three_graded_source_formulas']=True
 rebal=Q(91553,10**10)-Q(3,327680);legacy=Q(1,163840)-Q(12207,2*10**9)
 checks['rebalanced_larger_decimal']=rebal==Q(17,640000000000)>0
 checks['legacy_X3_smaller_decimal']=legacy==Q(1,64000000000)>0
 registry=(R/'research/registered_norm_assembly/source/theory_v03.md').read_text()
 checks['legacy_exact_threshold_in_source']='1/163840 = 6.103515625e-6' in registry
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for p in [B/'PROOF.md',Path(__file__)]:bind(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'candidate':pars['candidate'],'raw_sha256':pars['raw_sha256'],'condition':man['condition'],'inputs':inputs,'checks':checks,'check_count':len(checks),'E_star':{'lower':bound(star[0]),'upper':bound(star[1])},'E2_with_Hardy_proxy':{'lower':bound(E2[0]),'upper':bound(E2[1]),'actual_H_value_computed':False},'weighted_square_upper_expressions':{k:bound(v) for k,v in sq.items()},'instances':instances,'graded':graded,'threshold_transcription':{'rebalanced_printed_minus_exact':str(rebal),'rebalanced_ratio_direction':'conservative lower divisor comparison, not exact source ratio','legacy_X3_exact_minus_printed':str(legacy),'legacy_X3_ratio_direction':'printed ratio exceeds cited comparison divided by exact source threshold; not justified as a lower ratio by that calculation alone'},'no_full_plane_integral_computed_here':True,'foreign_code_executed':False,'actual_component_acceptance':'OPEN independent full-plane production pending','elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED conditional scalar assembly and outward25-digit energy/norm-comparison displays; REFUTED legacy X3 printed divisor ratio as exact source-ratio transcription; actual four component hypotheses OPEN'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED CONDITIONAL',len(checks),'checks',len(inputs),'bindings',sha(target),'seconds',out['elapsed_seconds'],flush=True)
 print('E_star',star[0].str(30),star[1].str(30),'E2_proxy_UB',E2[1].str(30))
 for row in instances:print(row['framework'],row['correct_source_ratio']['ball'])
if __name__=='__main__':main()

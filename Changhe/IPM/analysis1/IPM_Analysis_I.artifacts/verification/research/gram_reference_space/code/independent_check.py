"""Independent beta recurrence, Cartesian angular moments and exact recorded-source audit.
Does not import the first checker or numerical lane code.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
from datetime import datetime,timezone
import json,hashlib,ast,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_space'
def sha(p):
 with p.open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def check(x,s):
 if not x:raise ValueError(s)
def beta(p,q):
 # Integral_0^1 z^p(1-z)^q, repeated integration by parts.
 z=Q(1,q+1)
 for j in range(1,p+1):z=z*j/Q(q+j+1)
 return z
I0=beta(0,12)/2;Ic=-6*beta(1,11);I2=72*beta(2,10);total=15*I0+6*Ic+I2
check((I0,Ic,I2,total)==(Q(1,26),-Q(1,26),Q(12,143),Q(123,286)),'beta integral values')
# Independent Cartesian angular powers: Phi^2=c^4-c^6 and Phi'=3c^3-2c.
def cmoment(n):
 a=Q(2)
 for j in range(1,n+1):a*=Q(2*j-1,2*j)
 return a
A0=cmoment(2)-cmoment(3);A1=9*cmoment(3)-12*cmoment(2)+4*cmoment(1)
check(A0==Q(1,8) and A1==Q(5,8),'Cartesian angular moments')
# Independently derive radial energy from radial and angular pieces, no expanded chi convolution.
energy=A0*(I0+9*I0+6*Ic+I2)+A1*I0
check(energy==Q(123,2288) and 3*energy==Q(369,2288) and 12*energy<1,'norm coefficient')
# Beta identity itself independently checked using factorial expression on all terms employed.
for p,q in [(0,12),(1,11),(2,10)]:check(beta(p,q)==Q(factorial(p)*factorial(q),factorial(p+q+1)),'beta factorial')
a=json.loads((D/'evidence/exact_check.json').read_text());check(a['status']=='PASS_EXACT_POLYNOMIAL_LAURENT_AND_SELECTED_SOURCE_CHECKS','producer state')
checks=0
for name,h in a['files'].items():check(sha(B/name)==h,'input '+name);checks+=1
for key,value in [('I0',I0),('cross',Ic),('I2',I2),('total',total)]:check(Q(a['radial_integrals'][key])==value,'saved radial result')
check(Q(a['angular_integrals_over_pi']['Phi_squared'])==A0 and Q(a['angular_integrals_over_pi']['Phi_derivative_squared'])==A1,'saved angular result')
# Audit all recorded binding statements against AST, with uniqueness and actual source line.
for record in a['AST_bindings']:
 tree=ast.parse((D/'sources'/('src__'+record['source']+'.py')).read_text());expect=ast.dump(ast.parse(record['expected_statement']).body[0],include_attributes=False)
 hits=[n for n in ast.walk(tree) if ast.dump(n,include_attributes=False)==expect]
 check(len(hits)==1 and hits[0].lineno==record['line'] and hashlib.sha256(expect.encode()).hexdigest()==record['ast_sha256'],'binding audit')
# Independently parse the concrete J source calls, without evaluating any source.
f=ast.parse((D/'sources/src__c2_fminus.py').read_text());j=[]
for n in ast.walk(f):
 if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='append' and isinstance(n.func.value,ast.Name) and n.func.value.id=='cols' and len(n.args)==1 and isinstance(n.args[0],ast.Tuple):
  e=n.args[0].elts
  if len(e)==3 and isinstance(e[2],ast.Constant) and e[2].value=='J':j.append(e)
check(len(j)==1,'unique actual J source');j=j[0]
check(ast.literal_eval(j[0])==0 and isinstance(j[1],ast.Call) and isinstance(j[1].func,ast.Name) and j[1].func.id=='ExpPolyBasis','J mode and basis')
pieces=j[1].args[0].elts;check(len(pieces)==2,'J two pieces')
ends=[]
for pc in pieces:
 check(ast.literal_eval(pc.elts[2])==0 and ast.literal_eval(pc.elts[3])==[1.0],'constant piece')
 ends.append([ast.unparse(pc.elts[0]),ast.unparse(pc.elts[1])])
check(ends==[['-np.inf','T.tmin'],['T.tmin','T.t0']],'J support')
g=ast.parse((D/'sources/src__c2_gram.py').read_text())
rads=[n.value for n in ast.walk(g) if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='rad_pieces']
check(len(rads)==1 and isinstance(rads[0],ast.BinOp) and isinstance(rads[0].right,ast.List),'radial list');pc=rads[0].right.elts[-1].elts
check(len(pc)==1,'Jinner one piece');pc=pc[0].elts
check([ast.unparse(pc[0]),ast.unparse(pc[1])]==['-np.inf','tmin'] and ast.literal_eval(pc[2])==0 and ast.literal_eval(pc[3])==[1.0],'inner support')
# Nine output extracts, including positive finite broken-energy numbers, checked exactly as decimal records.
for row in a['reported_floating_outputs']:
 raw=json.loads((B/row['source']).read_text(),parse_float=Q);s=raw['sections']['Fminus']
 check(row['nrows']==raw['Ne']*raw['Mout'] and row['n_kept']==s['n_kept'],'row metadata')
 for x in ['J_code','J_inner']:check(Q(row['Xnorm2_'+x])==raw['Xnorm2'][x]>0,'broken energy extract')
 check(Q(row['sigma_min'])==s['sigma_small5'][0] and Q(row['sigma_max'])==s['sigma_max'],'spectrum extract only')
 for x in ['J_code','J_inner','tails']:check(Q(row[x+'_cos2_max'])==max(q[x] for q in s['smallest5_shares']),'correlation extract')
# Finite data do not prove convergence. Strict exact check of the discrepant row-scaling factors.
sel=[r for r in a['reported_floating_outputs'] if r['mode']=='H1m' and r['NJ']==0];sel.sort(key=lambda r:r['ppc'])
refinement=[]
for new in sel[1:]:
 old=sel[0];rmin=Q(new['sigma_min'])/Q(old['sigma_min']);rmax=Q(new['sigma_max'])/Q(old['sigma_max'])
 check(rmin>Q(7,5) and rmax<Q(11,10),'different min and max scaling')
 refinement.append({'from_ppc':old['ppc'],'to_ppc':new['ppc'],'minimum_ratio_exact':str(rmin),'maximum_ratio_exact':str(rmax),'minimum_ratio_gt':'7/5','maximum_ratio_lt':'11/10'})
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_BETA_CARTESIAN_AND_SOURCE_AUDIT','exact_result_sha256':sha(D/'evidence/exact_check.json'),'input_hashes_checked':checks,'bindings_checked':len(a['AST_bindings']),'floating_records_checked':len(a['reported_floating_outputs']),'radial_integrals':dict(I0=str(I0),cross=str(Ic),I2=str(I2),total=str(total)),'angular_integrals_over_pi':dict(A0=str(A0),A1=str(A1)),'norm_coefficient_over_pi':str(energy),'strict_weight_upper_constant_over_pi':str(3*energy),'refinement_record_checks':refinement,'code_sha256':sha(Path(__file__)),'scope':'Confirms exact analytic constants and recorded current-source definitions. Source/JSON correspondence is current, not an authenticated replay of historical C2 computations. Floating min/max do not scale alike; no limit theorem is established.'}
out=D/'evidence/independent_check.json';check(not out.exists(),'immutable output');out.write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],result['status'],checks,len(a['AST_bindings']),sha(out))

from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb
import importlib.util,json,time
R=Path(__file__).resolve().parents[3];B=R/'research/higher_mode_rank_peer';T4=R.parent/'c1-t4';PB=T4/'research/higher_mode_rank_audit'
spec=importlib.util.spec_from_file_location('own_binding303',R/'research/scaled_hessian_peer/code/check.py');H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H);sha=H.sha

def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();checks={}
 op=R/'research/higher_mode_scaled_rank/verification/result.json';own=json.loads(op.read_text());paths=[op,B/'PROOF.md',Path(__file__),R/'research/scaled_hessian_peer/code/check.py']
 for rel,h in own['inputs'].items():p=R/rel;assert sha(p)==h;paths.append(p)
 bind=H.Binding(B,paths);manifest=bind.freeze(PB/'data/manifest.json')
 for rel,d in manifest['files'].items():bind.freeze(PB/rel,d['sha256'])
 bind.freeze(PB/'PROOF.md',manifest['proof_sha256']);pp=PB/'verification/result.json';peer=bind.freeze(pp)
 for rel,h in peer['inputs'].items():p=Path(rel);bind.freeze(p if p.is_absolute() else PB/p,h)
 checks['status']=peer['verdict'].startswith('CONFIRMED N4-294') and not peer['publisher_code_executed'] and peer['actual_candidate_shape_match'] is own['actual_candidate_shape_match'] is None
 checks['peer_reads_own']=manifest['files']['source/N4_result.json']['sha256']==sha(op)
 old=json.loads((R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json').read_text());parent=json.loads((PB/'data/parent016.json').read_text());abstract=json.loads((R/'research/higher_mode_scaled_rank/verification/abstract_shapes.json').read_text())
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']));oldshapes=list(map(shape,old['generators']));parents=list(map(shape,parent['generators']));present={(j,m) for j,m,s in parents}
 blocks=[(j,m) for j in [1,2,3] for m in range(16,24) if (j,m) in present];assert blocks==[(1,m) for m in range(16,20)]+[(j,m) for j in [2,3] for m in range(16,24)]
 shapes=parents+[(j,m,('legqs',0,N,4,25)) for j,m in blocks for N in range(12)];declared=oldshapes+[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(9,20 if j==1 else 24) for N in range(12)]
 checks['complete_shapes']=len(oldshapes)==1922 and len(parents)==2174 and len(shapes)==len(set(shapes))==2414 and shapes==list(map(shape,abstract['generators'])) and set(shapes)==set(declared) and peer['proposed_shape_list_equal']
 checks['dimensions']=peer['potential_dimension']==peer['density_dimension']==own['potential_dimension']==own['density_dimension']==2414
 checks['increments']=peer['new_count']==own['new_functions']==240 and peer['all_scaled_count']==own['all_scaled_functions']==492 and own['all_scaled_blocks']==41 and list(map(tuple,peer['new_blocks']))==list(map(tuple,own['new_blocks']))==blocks
 c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)];ds=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 checks['branches']=list(map(str,ps))==peer['branch_exponents']==own['branch_exponents'] and list(map(str,ds))==peer['noninteger_differences']==own['noninteger_differences'] and all(v.denominator!=1 for v in ps+ds)
 checks['growth']=str(3+gamma)==peer['growth_exponent']==own['growth_exponent'] and 3+gamma<4 and str(gamma-1)==peer['fourth_derivative_exponent']==own['fourth_derivative_exponent'] and gamma-1<0
 a=Q(624);v0=-1/a;pw={(d['m'],d['N']):d for d in peer['Laurent_witnesses']};ow={(d['m'],d['N']):d for d in own['Laurent_witnesses']};checks['witness_map']=set(pw)==set(ow)=={(m,N) for m in range(9,24) for N in range(12)};witnesses=[]
 for m,N in sorted(pw):
  p,q=pw[m,N],ow[m,N];z=625**4*v0**4*comb(2*N,N)*(1-v0)**(m+N)/a**(4+N)
  checks[f'witness{m}_{N}']=z!=0 and z==Q(p['coefficient'])==Q(q['coefficient']) and p['pole_order']==q['pole_order']==4+N and p['full_numerator_formula_equal'] and p['peer_equal'] and q['exact_formula_equal']
  if m<=15:checks[f'calibration{m}_{N}']=p['old_equal'] and q['old_independent_witness_equal']
  witnesses.append({'m':m,'N':N,'coefficient':str(z),'independent_equal':True})
 origin=4*33*32*(ps[1]-16-Q(4,625));support=sorted({2*m+s for j,m in blocks for s in [-1,1]});checks['density31']=origin!=0 and str(origin)==peer['density31_origin_coefficient']==own['density31_origin_coefficient'];checks['support']=support==peer['density_new_mode_support']==own['density_new_mode_support']==list(range(31,48,2))
 assert all(checks.values()),{k:v for k,v in checks.items() if not v};bind.finish()
 result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED N4-294 through independent T4-369; abstract rank and density support only','checks':checks,'check_count':len(checks),'potential_dimension':2414,'density_dimension':2414,'actual_candidate_shape_match':None,'density_new_mode_support':support,'density31_origin_coefficient':str(origin),'witnesses':witnesses,'own_result_sha256':sha(op),'peer_result_sha256':sha(pp),'own_inputs':bind.own,'frozen_or_retained_sources':bind.frozen,'peer_bindings':bind.bindings,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bind.bindings),'bindings',sha(out),result['utc'],'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

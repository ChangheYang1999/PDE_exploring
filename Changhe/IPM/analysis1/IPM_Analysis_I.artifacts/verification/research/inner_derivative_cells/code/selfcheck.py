"""Exact static count/coverage and source checks; no interval cell execution."""
from protocol import *
import ast,subprocess

def main():
 started=now();p,deps=parents();prior_reviews(p);cs=cells();co=load(COEFFICIENTS)
 alpha=[F(0)]+[F(2*l+2) for l in range(7)]+[F(co['bi_exact'])]
 rows=[]
 for j,r in enumerate(co['rows']):
  assert r['j']==j and F(r['C'])==(F(1,4) if j in [0,1] else 0)
  rows.append([[F(r['C'])]]+[[F(v)] for v in r['D']]+[[F(v) for v in r['Ei']]])
 assert len(rows)==262 and not any(v for p0 in rows[-1] for v in p0)
 def count(ps):return sum(any(v!=0 for v in p0) for p0 in ps)
 def dt(ps):return [[(al+3)*v+((l+1)*p0[l+1] if l+1<len(p0) else 0) for l,v in enumerate(p0)] for al,p0 in zip(alpha,ps)]
 components={'Hhat':sum(count(ps) for ps in rows),'rho':0,'D_rho':0,'eta':0,'D_eta':0,'exp2':1,'Bhat1':0}
 for ps in rows[:261]:
  es=[[F(0)]]+ps[1:]
  for name,terms in [('rho',ps),('D_rho',dt(ps)),('eta',es),('D_eta',dt(es))]:components[name]+=count(terms)
 # The exact positive-denominator inverse of a nonzero polynomial is nonzero.
 # Bhat1's forcing is formed independently; no moment engine is imported.
 for al,hm,hp in zip(alpha,rows[0],rows[1]):
  assert len(hm)==len(hp)
  forcing=[((al+2)*hm[l]+(al+6)*hp[l]+((l+1)*(hm[l+1]+hp[l+1]) if l+1<len(hm) else 0))/2 for l in range(len(hm))]
  assert al+2>0;components['Bhat1']+=any(forcing)
 term_calls=sum(components.values());assert term_calls>0
 # For each nonzero input term, Q first-derivative coefficients and Q-1
 # second-derivative coefficients are compared. Zero terms return before count.
 counts={'coefficient_overlap_checks':522*33,'derivative_input_checks':term_calls*31,'cross_method_input_jet_checks':(4*261+262)*(17+16+15),'exact_integer_convolutions':8,'moment_modes':261}
 assert counts['coefficient_overlap_checks']==17226 and counts['cross_method_input_jet_checks']==62688
 assert len(cs)==44 and load(OUT/'algebra_checks.json')['partition']==[[str(a),str(b)] for a,b in cs]
 assert load(OUT/'algebra_checks.json')['source_sha256']==sha(DIR/'code/algebra_checks.py')
 z=load(OUT/'linear_angular_checks.json');assert z['checker_source_sha256']==sha(DIR/'code/linear_angular_checks.py') and z['initial_exact_replay_sha256']==sha(OUT/'linear_angular_checks_initial.json')
 for n,h in ENGINE_HASHES.items():assert sha(DIR/'code'/n)==h
 parsed=[]
 for n in ['engine_arb.py','engine_iv.py','protocol.py','run.py','audit.py','replay.py','gate.py','selfcheck.py']:
  ast.parse((DIR/'code'/n).read_text());parsed.append(n)
 subprocess.run(['bash','-n',str(DIR/'code/queue.sh')],check=True,timeout=10)
 tail=tail_squares();assert tail==[F('0.000002273735')**2,F('0.000035059554')**2]
 rehash(p)
 out={'start_utc':started,'utc':now(),'status':'PASS_EXACT_STATIC_WORKFLOW_CHECKS_NO_NUMERICAL_CELLS','source_sha256':sha(__file__),'source_engine_sha256':ENGINE_HASHES,'canonical_coefficients_sha256':sha(COEFFICIENTS),'canonical_manifest_sha256':sha(MANIFEST),'parent_pin_count':len(p),'expected_checks_per_cell':counts,'independent_nonzero_analytic_term_counts':components,'nonzero_term_calls':term_calls,'partition':[[str(a),str(b)] for a,b in cs],'smoke_indices':SMOKE,'parsed_python_sources':parsed,'bash_syntax_check':True,'accepted_inner_tail_squares':[str(v) for v in tail],'scope':'Static exact source/data checks only. No engine setup, input jets, numerical cell or runtime counter has been executed.'}
 write(OUT/'workflow_selfcheck.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['partition','parsed_python_sources']}),flush=True)
if __name__=='__main__':main()

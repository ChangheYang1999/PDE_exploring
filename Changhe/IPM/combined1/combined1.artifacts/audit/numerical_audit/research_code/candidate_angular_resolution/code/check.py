from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import ast,json,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate_angular_resolution';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def write(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or h==actual,(str(p),h,actual);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__));src=read(B/'source/MANIFEST.json',prep['source_manifest_sha256'])
 for name,row in src['files'].items():bind(B/'source'/name,row['sha256'])
 a=read(R/'research/candidate020_holdout/verification/result.json','7761b0d6033784110bb8bc2189c68d295143cc6daecf8832ff57001c1b889334')
 for p,h in a['inputs'].items():bind(R/p,h)
 D=R/'research/candidate_audits/data/C1-N1-020-legqs25p50-quot013';man=read(D/'MANIFEST.json');row=man['coefficient_files'][0];data=read(D/row['name'],row['sha256']);assert len(data['generators'])==2426 and data['meta']['angular_midpoint']==180
 higher=read(R/'research/higher_mode_scaled_rank/verification/result.json','fba74577bff755e86fd5d473add67f8a9b91473fb99b48808069b2c48a9bd768');shapep=R/'research/higher_mode_scaled_rank/verification/abstract_shapes.json';shapes=read(shapep,higher['inputs'][str(shapep.relative_to(R))]);assert len(shapes['generators'])==2414
 previous=read(R/'research/candidate007_weighted_laplacian/verification/angular_rule.json','e4223ad51ffb23f7a67dae1311f03f54ba444b6f09924ba939081e84b8a7f023')
 for p,h in previous['inputs'].items():bind(R/p,h)
 M=max(g['m'] for g in data['generators']);M2=max(g['m'] for g in shapes['generators']);assert M==M2==79
 N=180;Fmax=4*M+3;derivative_max=Fmax+2;assert derivative_max<2*N and Fmax+47<4*N
 evalsrc=(B/'source/N1_ipm_eval.py').read_text();tree=ast.parse(evalsrc);fun=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='angular_midpoint');snippet=ast.get_source_segment(evalsrc,fun)
 assert 'th = (np.arange(N)+0.5)*np.pi/(2*N)' in snippet and 'return th, np.full(N, np.pi/(2*N))' in snippet
 O2=(B/'source/N1_ipm_opt2.py').read_text();tree2=ast.parse(O2);derivs=next(n.value for n in tree2.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DERIVS' for t in n.targets));derivs=ast.literal_eval(derivs);assert derivs==[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
 cls=next(n for n in tree2.body if isinstance(n,ast.ClassDef) and n.name=='Problem2');obj=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='objective_parts');init=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='__init__');wts=next(n.value for n in ast.walk(init) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) and t.attr=='wts' for t in n.targets))
 assert {n.id for n in ast.walk(wts) if isinstance(n,ast.Name)}<={'base','wF','hw','r','mesh','maskr','wlog','wG','wP','omega2'}
 assert 'parts = {d: float(torch.sum(self.wts[d]*comp[d]**2)) for d in DERIVS}' in ast.get_source_segment(O2,obj)
 assert "(('rho', (2, 0)), base*wkap*c1)" in O2 and "(('rho', (0, 2)), base*wkap*c2)" in O2
 O3=(B/'source/N1_ipm_opt3.py').read_text();assert 'base*r*u0**2*t**K*torch.sin(n*th)' in O3 and "parts['pair'] = sum(w*I*I" in O3
 launch=(B/'source/N1_run_quot.py').read_text();assert 'EV.angular_midpoint(ANG)' in launch
 chain=(B/'source/N1_chain022.sh').read_text();assert 'run_quot.py' in chain and ' 180 12 ' in chain and ' 180 28 ' in chain
 histories=read(R/'research/expanded_objective_span/verification/result.json');assert sha(B/'source/N1_chain022.sh')==sha(R/'research/expanded_objective_span/data/N1_chain022.sh');bind(R/'research/expanded_objective_span/data/N1_chain022.sh')
 rows=[];pair_count=0
 for x,y in derivs:
  d=x+y;bound=Fmax+d;kind='c' if y%2 else 's';parity=bound%2;freqs=list(range(parity,bound+1,2));freqs=[n for n in freqs if n or kind=='c'];qs=set()
  for i,n in enumerate(freqs):
   for m in freqs[:i+1]:
    assert (n+m)%2==0 and (n-m)%2==0;qs.update([(n+m)//2,abs(n-m)//2]);pair_count+=1
  assert max(qs)==bound and all(q<2*N for q in qs)
  rows.append({'component':[x,y],'sine_or_cosine':kind,'permitted_modes':len(freqs),'frequency_bound':bound,'square_cosine_q_bound':max(qs),'nonconstant_q_count':len(qs-{0}),'ideal_rule_exact':True})
 probes=[]
 for n in range(1,48,2):
  qs={(f+n)//2 for f in range(1,Fmax+1,2)}|{abs(f-n)//2 for f in range(1,Fmax+1,2)};assert max(qs)<2*N
  probes.append({'n':n,'cosine_q_bound':max(qs),'ideal_rule_exact':True})
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'actual020_raw_sha256':row['sha256'],'actual020_generators':2426,'proposed022_generators':2414,'max_potential_m':M,'max_residual_frequency':Fmax,'max_second_derivative_frequency':derivative_max,'midpoint_quadrant_nodes':N,'first_alias_cosine_q':2*N,'derivative_components':rows,'exact_frequency_pairs_checked':pair_count,'weak_probe_rows':probes,'rho_hessian_frequency_bound':2*M+3,'source_angular_midpoint_function_sha256':sha256(snippet.encode()).hexdigest(),'source_weights_ast':ast.dump(wts),'objective_parts_sha256':sha256(ast.get_source_segment(O2,obj).encode()).hexdigest(),'inputs':inputs,'publisher_code_executed':False,'scope':'Ideal trigonometric quadrature only; no floating-node/sample, radial, omitted-domain, norm, conditioning or optimizer guarantee','verdict':'CONFIRMED exact bandwidth application of independently accepted midpoint theorem; proposed022 identity remains conditional on its listed shapes'}
 assert all(sha(R/p)==h for p,h in inputs.items());write(B/'verification/result.json',out);print(out['utc'],out['verdict'],sha(B/'verification/result.json'),out['elapsed_seconds'])
if __name__=='__main__':main()

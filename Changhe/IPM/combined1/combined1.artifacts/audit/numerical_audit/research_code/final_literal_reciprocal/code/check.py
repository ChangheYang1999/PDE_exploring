"""Independent finite Cartesian jet and reciprocal saved-decimal audit."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from datetime import datetime, timezone
from hashlib import sha256
import ast, json, math, os, sys, time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3]
B=Path(__file__).resolve().parents[1]
def sha(p): return sha256(p.read_bytes()).hexdigest()
def main():
    assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
    start=time.monotonic(); manifest=json.loads((B/'source/MANIFEST.json').read_text())
    assert not manifest['checker_exists'] and sha(B/'PROOF.md')==manifest['proof_sha256']
    inputs=dict(manifest['inputs']); checks={}
    for p in [B/'PROOF.md',B/'source/MANIFEST.json',B/'source/T4_490_parameters.json',Path(__file__)]:
        inputs[str(p.relative_to(R))]=sha(p)
    def ck(k,v):
        assert k not in checks,k
        checks[k]=bool(v);assert v,k
    def peer(n,p):
        row=manifest['files'][f'{n}:{p}'];return R/row['local']
    def read(n,p):return json.loads(peer(n,p).read_text())
    for p,h in inputs.items():ck('input '+p,(R/p).resolve().is_relative_to(R) and sha(R/p)==h)
    for n in [490,492]:ast.parse(peer(n,'code/check.py').read_text())
    par=read(490,'data/parameters.json');a=read(490,'verification/result.json');t=read(492,'verification/result.json')
    ck('parameter copy',par==json.loads((B/'source/T4_490_parameters.json').read_text()))
    raw=peer(490,'../rounding_audit/data/exact_generators.json'); data=json.loads(raw.read_text())
    ck('raw identity',sha(raw)==par['raw_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21')
    c=Q(data['cl_exact']);ck('exact c',c==Q('4076476460239181/2251799813685248'))
    axis=json.loads((R/'research/candidate007_origin_tolerance/verification/result.json').read_text())
    old=json.loads((R/'research/numerics_final_literal_audit/verification/result_v02.json').read_text())
    ck('source axis checks',axis['check_count']==3005 and all(axis['checks'].values()))
    ck('source display checks',old['check_count']==626 and all(old['checks'].values()) and old['display_failures']==[])
    ck('peer finite check counts',a['check_count']==len(a['checks'])==3181 and t['check_count']==len(t['checks'])==1340)
    def add(d,key,value):
        d[key]=d.get(key,Q(0))+value
        if not d[key]:d.pop(key)
    def derivative(d,dx,dy):
        out={}
        for (i,j),value in d.items():
            if i>=dx and j>=dy:
                add(out,(i-dx,j-dy),value*math.prod(range(i-dx+1,i+1))*math.prod(range(j-dy+1,j+1)))
        return out
    def product(A,C,degree=5):
        out={}
        for (i,j),v in A.items():
            for (k,l),w in C.items():
                if i+j+k+l<=degree:add(out,(i+k,j+l),v*w)
        return out
    def harmonic(m,s):
        out={}
        for k in range(m+1):
            for l in range(s+1):
                add(out,(2*(m-k+l),2*(k+s-l)),Q((-1)**k*math.comb(2*m,2*k)*math.comb(s,l)))
        return out
    chi={};used=[];terms=[]
    for index,g in enumerate(data['generators']):
        m,j=g['m'],g['j'];spec=g['spec'];w=spec[1]
        ck('schema '+str(index),isinstance(m,int) and m>=0 and isinstance(j,int) and j>=0 and isinstance(w,int) and w>=0 and spec[0] in ['mono','leg'])
        if m+w>4:continue
        used.append(index);p=(3+1/c-j*(1-1/c))/2
        pieces=[(w,1)] if spec[0]=='mono' else [(w+h,(-1)**(spec[2]-h)*math.comb(spec[2],h)*math.comb(spec[2]+h,h)) for h in range(min(spec[2],4-m-w)+1)]
        for power,L in pieces:
            binomial=Q(1)
            for ell in range(5-m-power):
                if ell:binomial*=Q(p-m-power-ell+1,ell)
                s=power+ell;v=Q(g['coef'])*L*binomial
                pol=harmonic(m,s)
                for key,value in pol.items():add(chi,key,v*value)
                lap=derivative(pol,2,0)
                for key,value in derivative(pol,0,2).items():add(lap,key,value)
                expected={key:4*s*(2*m+s)*value for key,value in harmonic(m,s-1).items()} if s else {}
                ck('term Laplacian '+str(len(terms)),lap==expected)
                terms.append({'source_generator':index,'m':m,'s':s,'coefficient_exact':str(v)})
    ck('complete generators',len(data['generators'])==2982 and used==axis['used_generator_indices']==a['used_generator_indices'] and len(used)==60)
    ck('complete radial terms',len(terms)==axis['finite_summand_count']==140 and terms==a['potential_radial_terms'])
    lap=derivative(chi,2,0)
    for key,value in derivative(chi,0,2).items():add(lap,key,value)
    rho={key:-v for key,v in derivative(lap,0,1).items()}
    ux={key:-v for key,v in derivative(chi,1,2).items()};uy=derivative(chi,2,1)
    F={key:(c*sum(key)-1)*v for key,v in rho.items()}
    for pol in [product(ux,derivative(rho,1,0)),product(uy,derivative(rho,0,1))]:
        for key,v in pol.items():add(F,key,v)
    F={key:v for key,v in F.items() if v}
    jets={'potential_jet_exact':chi,'Laplacian_jet_exact':lap,'density_jet_exact':rho,'horizontal_velocity_jet_exact':ux,'vertical_velocity_jet_exact':uy,'residual_jet_exact':F}
    for name,jet in jets.items():
        theirs={tuple(map(int,key.split(','))):Q(v) for key,v in a[name].items()}
        ck(name+' supports',set(jet)==set(theirs))
        for key,v in jet.items():ck(name+' '+str(key),v==theirs[key])
    ck('even potential',all(i%2==j%2==0 and i+j<=8 for i,j in chi))
    ck('odd density quotient',all(i%2==0 and j%2==1 and i+j<=5 for i,j in F))
    for n in range(5):ck('axis potential '+str(n),chi.get((0,2*n),0)==Q(axis['chi_axis_A_exact'][str(n)]))
    for n in range(4):ck('axis x2 '+str(n),chi.get((2,2*n),0)==Q(axis['chi_x2_B_exact'][str(n)]))
    for j in [1,3,5]:
        for name,pol in [('rho',rho),('uy',uy),('F',F)]:ck('axis '+name+str(j),pol.get((0,j),0)==Q(axis[name+'_axis_exact'][str(j)]))
    ck('constant zero',F.get((0,1),0)==0 and a['quotient_constant_exact']=='0')
    ck('center relation',c+uy[(0,1)]==1 and rho[(0,1)]>0)
    coefficients={}
    for key,(lo,hi) in par['directed_intervals'].items():
        i,j=map(int,key.split(','));v=F[(i,j+1)]
        ck('strict interval '+key,Q(lo)<v<Q(hi))
        ck('tolerance '+key,abs(v)>Q('2e-13'))
        ck('peer coefficient '+key,v==Q(a['quotient_nonconstant_coefficients_exact'][key]))
        coefficients[key]=str(v)
    ck('all five',set(coefficients)=={'2,0','0,2','4,0','2,2','0,4'})
    def nearest(q,s):
        d=Decimal(s);unit=Q(Decimal(1).scaleb(d.as_tuple().exponent))
        return 2*abs(q-Q(d))<=unit
    expected=[];display_count=0
    for k,row in enumerate(old['probe_rows']):
        q=Q(row['new_exact'])/Q(row['old_exact'])
        ck('ratio '+str(k),q==Q(row['ratio_exact']))
        for label,value in [('old',Q(row['old_exact'])),('new',Q(row['new_exact'])),('factor',q)]:
            ck('display '+str(k)+' '+label,nearest(value,row['display'][label]));display_count+=1
        expected.append({'comparison':row['comparison'],'probe':row['probe'],'ratio_exact':str(q)})
    ck('all200 ordered ratios',expected==t['probe_rows'] and len(expected)==200)
    ck('all600 displays',display_count==t['display_count']==600)
    ck('all comparison counts',old['comparison_counts']==t['comparison_counts'])
    fr={str(r['k']):Q(r['improvement_exact']) for r in old['first_mode_rows_k_le128']}
    ck('all first-mode ratios',fr=={k:Q(v) for k,v in t['first_mode_ratios_exact'].items()})
    phase={':'.join(map(str,r['probe'])):Q(r['ratio_exact']) for r in old['phase_final_over12_rows']}
    ck('all25 phase ratios',phase=={k:Q(v) for k,v in t['phase_final_over12_exact'].items()} and len(phase)==25)
    for label,values in [('first_mode',fr),('phase',phase)]:
        for kind,fun in [('minimum',min),('maximum',max)]:ck(label+' '+kind,fun(values.values())==Q(t[label+'_extrema_exact'][kind]))
    ck('no PDE promotion',not t['PDE_or_quadrature_bounds_asserted'] and not t['unobserved_write_times_asserted'] and not t['foreign_code_executed'])
    for p,h in inputs.items():ck('stable '+p,sha(R/p)==h)
    result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'external_readonly_bindings':manifest['external_readonly_bindings'],'checks':checks,'check_count':len(checks),'source_generator_count':2982,'relevant_generators':60,'radial_term_count':140,'quotient_coefficients_exact':coefficients,'strict_intervals':par['directed_intervals'],'display_count':display_count,'all_T4_jets_equal':True,'all_N4_axis_coefficients_equal':True,'all_T4_ratios_equal':True,'source_integrals_repeated':False,'peer_code_executed':False,'verdict':'CONFIRMED T4-490 full exact007 Taylor jet and T4-492 finite FLOAT presentation audit. REFUTED the saved universal Taylor tolerance. No new PDE norm, chronology or existence claim.'}
    target=B/'verification/result.json'
    with target.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(result['utc'],'checks',len(checks),'inputs',len(inputs),'seconds',result['elapsed_seconds'],'sha256',sha(target),flush=True)
if __name__=='__main__':main()

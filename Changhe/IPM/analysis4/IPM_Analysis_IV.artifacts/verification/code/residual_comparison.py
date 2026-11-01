"""Compare independent Cartesian residual enclosures with numerical lane data."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json, pickle
from flint import arb, acb, fmpz, ctx
from cartesian_arb_residuals import Field, rb, addto
ctx.prec=640

def unpack4(t):
    m,e,r,re=t
    return arb(arb(fmpz(m))*arb(2)**e,arb(fmpz(r))*arb(2)**re)

def unpack3(t):
    m,e,r=t
    mid=arb(fmpz(m))*arb(2)**e
    if r=='0': return mid
    if '*2^' in r:
        a,b=r.split('*2^')
        radius=arb(fmpz(a))*arb(2)**int(b)
    else:
        # Older checkpoints printed radii to ten significant decimal digits.
        # This factor dominates the possible relative rounding loss.
        radius=arb(r)*(1+arb('1e-9'))
    return arb(mid,radius)

def decode_field(d):
    return Field(Fraction(d['q']),{int(k):acb(unpack4(v[0]),unpack4(v[1])) for k,v in d['modes'].items()})

root=Path('research/16_certified_residuals')
(root/'sources').mkdir(exist_ok=True)
p=Path('research/16_certified_residuals/verification/reference_sin_residuals_coefficients.json')
data=json.loads(p.read_text())
c=Fraction(data['c']); delta=Fraction(data['delta'])
rho={int(n):decode_field(f) for n,f in data['rho'].items()}
psi={int(n):decode_field(f) for n,f in data['psi'].items()}
cp=Path('../a4-num/ckpt/sin1_c007_arb512.pkl')
cpraw=cp.read_bytes(); state=pickle.loads(cpraw)
retained={'ring':state['ring'],'prec':state['prec'],'c_l_pack':state['c_l_pack'],'delta_pack':state['delta_pack'],'f':{n:a for n,a in state['f'].items() if n<=21},'g':{n:a for n,a in state['g'].items() if n<=21}}
(root/'sources/numerics_coefficients_N21.json').write_text(json.dumps(retained,indent=2)+'\n')
checks=[]
for kind,table,parity in [('f',rho,1),('g',psi,0)]:
    for n,field in table.items():
        actual=field.sine(2*n-1 if parity else 2*n,parity)
        other=state[kind][n]
        indices=range(len(other)) if parity else range(1,len(other))
        for j in indices:
            m=2*j+1 if parity else 2*j
            a=actual.get(m,arb(0)); b=unpack3(other[j])
            assert a.overlaps(b),(kind,n,j,a,b)
        checks.append({'field':kind,'n':n,'coefficient_enclosures_overlap':True,'coefficients':len(other) if parity else len(other)-1})
evpath=Path('../a4-num/notes/eval_sin1_c007_test.json')
evraw=evpath.read_bytes(); ev=json.loads(evraw)
(root/'sources/numerics_sampled_residuals.json').write_bytes(evraw)
for source in ['ffcore.py','evaluate_series.py']:
    raw=(Path('../a4-num/code')/source).read_bytes()
    (root/'sources'/source).write_bytes(raw)
rows=[]
for N in [10,20]:
    residual={}
    for i in range(1,N+1):
        for j in range(max(1,N+1-i),N+1):
            n=i+j
            term=psi[i].dy().scale(-1)*rho[j].dx()+psi[i].dx()*rho[j].dy()
            residual[n]=residual.get(n,Field(1-n*delta,{}))+term
    maxfreq=4*N-1
    for row in [v for v in ev['rows'] if v['N']==N]:
        radius=Fraction(row['R']); z=(-rb(delta)*rb(radius).log()).exp()
        coeff={}
        for n,f in residual.items():
            for m,a in f.sine(maxfreq,1).items():
                coeff[m]=coeff.get(m,arb(0))+z**(n-1)*a
        # The legacy product routine retained one final zero coefficient.
        # Its residual sampling therefore used 2*N+1 sine slots.
        grid=max(512,8*(4*N+3))
        for derivative in [0,1]:
            maximum=arb(0)
            for j in range(grid):
                th=arb.pi()*j/(grid-1)
                value=arb(0)
                for m,a in coeff.items():
                    value+=a*m*(m*th).cos() if derivative else a*(m*th).sin()
                maximum=maximum.max(abs(value))
            numerical=row['resid_k'+str(derivative)]
            error=abs(maximum/rb(Fraction(numerical))-1)
            print('grid check',N,str(radius),derivative,grid,str(error),flush=True)
            assert error < arb('1e-12')
            rows.append({'N':N,'R':str(radius),'angular_derivative_order':derivative,'grid':grid,'verified_grid_max_ball':str(maximum),'numerics_grid_max':numerical,'relative_difference_upper':str(error.upper())})
nd=9*delta; P=2-nd
actual_div=abs(4-P*P)
result={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Independent finite coefficient and identical-grid comparisons. Sampled suprema are not certified full-circle suprema. Legacy decimal checkpoint radii are inflated by 1+1e-9 before comparison.','own_coefficient_sha256':sha256(p.read_bytes()).hexdigest(),'numerics_checkpoint_sha256_at_read':sha256(cpraw).hexdigest(),'numerics_checkpoint_retained_subset':'sources/numerics_coefficients_N21.json','numerics_sampled_residuals_sha256':sha256(evraw).hexdigest(),'source_hashes':{x:sha256((root/'sources'/x).read_bytes()).hexdigest() for x in ['ffcore.py','evaluate_series.py']},'coefficient_checks':checks,'sampled_residual_checks':rows,'legacy_grid_explanation':'The retained old ffcore source uses Mout=J+K+1 and one extra exact zero, giving grid max(512,8*(4*N+3)). Current source drops that zero.', 'diagnostic_corrections':{'stored_min_active_den_is':'2*abs(4*j*j-P_n*P_n)','n9_j1_P':'%s'%P,'n9_j1_true_quadratic_divisor':str(actual_div),'n9_j1_logged_divisor':str(2*actual_div),'precision_stop_quantity':'rad_over_max, not max_rel_rad','max_rel_rad_definition':'maximum per-coefficient radius divided by coefficient midpoint magnitude; differs from norm-relative radius','spot_checks':'evaluate_series.py advertises Arb spot checks but only float64 angular sampling is implemented'}}
(root/'verification/numerics_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print('All',sum(r['coefficients'] for r in checks),'density and stream coefficient enclosures overlap.')
print('All',len(rows),'identical-grid residual comparisons agree to relative error below 1e-12.')
print('True quadratic divisor at n=9,j=1:',float(actual_div))

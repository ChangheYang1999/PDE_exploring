"""Select already proved certificates and round exact endpoint decimals outward."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
ctx.prec=256
ROOT=Path(__file__).resolve().parents[1]

def as_fraction(s):
    return Fraction(str(s))

def arb_endpoint(s,upper):
    x=arb(s); y=arb(x.upper() if upper else x.lower())
    # Enclose once at 30 decimal places, then work only with exact rationals.
    z=y*10**30
    k=int((z.ceil() if upper else z.floor()).unique_fmpz())
    return Fraction(k,10**30)

def display(q,up,n=6):
    z=q*10**n
    k=-((-z.numerator)//z.denominator) if up else z.numerator//z.denominator
    return f'{k//10**n}.{k%10**n:0{n}d}'

def main():
    base=json.loads((ROOT/'data/explicit_bounds_intervals.json').read_text())['rows']
    C={};D={};L={};inputs={}
    def load(path):
        p=ROOT/path;inputs[str(path)]=hashlib.sha256(p.read_bytes()).hexdigest()
        return json.loads(p.read_text())
    def add(dest,a,v,family,path):
        dest.setdefault(Fraction(a),[]).append((v,family,str(path)))
    for row in load(Path('data/explicit_bounds_intervals.json'))['rows']:
        a=row['alpha'];v=row['intervals']
        add(C,a,arb_endpoint(v['upper_C'],True),'optimized radial split','data/explicit_bounds_intervals.json')
        add(D,a,arb_endpoint(v['upper_D'],True),'optimized radial split + identity','data/explicit_bounds_intervals.json')
        add(L,a,arb_endpoint(v['lower_C_and_D'],False),'compact cusps','data/explicit_bounds_intervals.json')
    for row in load(Path('data/homogeneous_lower_intervals.json'))['rows']:
        add(L,row['alpha'],arb_endpoint(row['C_lower_interval'],False),'degree three','data/homogeneous_lower_intervals.json')
    for path,family in [(Path('data/gated_lower_intervals.json'),'gated'),
                         (Path('data/structured_full_a_half.json'),'polygonal a=1/2')]:
        for row in load(path)['rows']:
            add(L,row['alpha'],Fraction(row['safe_decimal_lower_10_places']),family,path)
    path=Path('data/structured_layercake_certificate_fine.json');row=load(path)
    add(L,row['alpha'],Fraction(row['safe_decimal_lower_10_places']),'polygonal a=1/2',path)
    for path in sorted((ROOT/'data/structured_shape_certificates').glob('alpha_*.json')):
        path=path.relative_to(ROOT);obj=load(path)
        for row in obj['rows']:
            add(L,row['alpha'],Fraction(row['safe_decimal_lower_10_places']),f"polygonal a={obj['a']}",path)
    path=Path('data/local_projection_intervals.json')
    for row in load(path)['rows']:
        add(D,row['alpha'],Fraction(row['safe_decimal_upper_10_places']),'local projection',path)
    for name,family in [('midpoint_split_certificate_coarse.json','midpoint split'),
                        ('midpoint_split_certificate_fine.json','midpoint split'),
                        ('reflection_orbit_certificate_v2_coarse.json','reflection orbits, corrected'),
                        ('reflection_orbit_certificate_v2_fine.json','reflection orbits, corrected'),
                        ('circle_composite_upper_fine.json','exterior-circle transport'),
                        ('circle_composite_upper_n768.json','exterior-circle transport, finer compact integral'),
                        ('middle_composite_upper_n512.json','middle and exterior circle transport')]:
        path=Path('data')/name
        if not (ROOT/path).exists():continue
        for row in load(path)['rows']:
            add(C,row['alpha'],Fraction(row['safe_upper_C']),family,path)
            add(D,row['alpha'],Fraction(row['safe_upper_D']),family,path)
    for name in ['local_circle_composite_a30.json','local_circle_composite_a50.json','local_circle_composite_a75.json','local_circle_composite_a90.json']:
        path=Path('data')/name
        if (ROOT/path).exists():
            for row in load(path)['rows']:
                add(C,row['alpha'],Fraction(row['safe_upper_C']),'paired local, middle and exterior circles',path)
    approval=load(Path('08_improved_upper_bounds/explicit_second_term/verification/accepted.json'))
    assert approval['verdict']=='CONFIRMED'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    path=Path('08_improved_upper_bounds/explicit_second_term/verification/rational_cutoffs.json')
    for row in load(path)['rows']:
        for key,dest in [('H_C',C),('H_D',D),('J_C',C),('J_D',D)]:
            add(dest,row['alpha'],Fraction(row['bounds'][key]['upper']),key+' exact rational cutoff',path)
    approval=load(Path('05_team_audit/closed_form37_lead/verification/accepted.json'))
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V124'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    path=Path('05_team_audit/closed_form37_lead/verification/closed_form_values.json')
    for row in load(path)['rows']:
        add(C,row['alpha'],Fraction(row['safe_upper_C']),'sharper closed form, V124',path)
    approval=load(Path('05_team_audit/table37_lead/verification/accepted.json'))
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V131'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    path=Path('05_team_audit/table37_lead/verification/independent_audit.json')
    direct=load(path)
    assert [(r['alpha'],r['safe_upper_C']) for r in direct['rows']]==[(r['alpha'],r['safe_upper_C']) for r in approval['rows']]
    for row in direct['rows']:
        assert Fraction(row['upper']['upper'])<=Fraction(row['safe_upper_C'])
        add(C,row['alpha'],Fraction(row['safe_upper_C']),'direct paired local transport, V131',path)
    path=Path('08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V152'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(C,row['alpha'],Fraction(row['safe_upper_C']),'paired local circles with balanced residual, V152',path)
    path=Path('08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V161'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(C,row['alpha'],Fraction(row['safe_upper_C']),'local circles with radial balanced residual, V161',path)
    path=Path('08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V168'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(C,row['alpha'],Fraction(row['safe_upper_C']),'balanced residual on middle arcs, V168',path)
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'balanced residual on middle arcs, V168',path)
    path=Path('08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V171'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(C,row['alpha'],Fraction(row['safe_upper_C']),'balanced middle residual, direct tables, V171',path)
    path=Path('08_improved_upper_bounds/phase_interpolation/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V177'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(C if row['operator']=='C' else D,row['alpha'],Fraction(row['safe_upper']),'unequal phase interpolation, V177',path)
    path=Path('05_team_audit/d36_recombination/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V179'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'middle recombination and unequal interpolation, V179',path)
    path=Path('05_team_audit/cross2048/recombination/verification/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V190'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'finer cross disks and unequal interpolation, V190',path)
    path=Path('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/fourth_moment/numerical_values/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V198'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'strict symmetric reflection with fourth moment, V198',path)
    path=Path('08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V209'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        if row['mode']=='finite':
            add(C if row['operator']=='C' else D,row['alpha_or_epsilon'],Fraction(row['safe_upper']),'sharper local deficiency with optional retained reflection, V209',path)
    path=Path('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V210'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'exact radial minorant with symmetric fourth moment, V210',path)
    path=Path('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/cross4096_values/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V220'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'cross4096 with exact radial reflection, V220',path)
    for rel,ledger,family in [
        ('08_improved_upper_bounds/explicit_second_term/tail_series/numerical_values/accepted.json','V225','exact exterior denominators, V225'),
        ('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/numerical_values/accepted.json','V226','eight reflection moments on enlarged axis disks, V226'),
        ('08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/numerical_values/accepted.json','V231','phase-uniform reflected density, V231'),
        ('08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks/numerical_values/accepted.json','V235','five disjoint reflection-disk pairs, V235')]:
        path=Path(rel);approval=load(path)
        assert approval['verdict']=='CONFIRMED' and approval['ledger']==ledger
        for filename,digest in approval['sha256'].items():
            assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
        for row in approval['rows']:
            if row['mode']=='finite':
                add(C if row['operator']=='C' else D,row['alpha_or_epsilon'],Fraction(row['safe_upper']),family,path)
    LD={a:list(values) for a,values in L.items()}
    for name in ['finite_D_lower_a001.json','finite_D_lower_a01.json','finite_D_lower_a05.json','finite_D_lower_a10.json','finite_D_lower_a20.json','finite_D_lower_a30.json','finite_D_lower_a30_geometric_fine.json']:
        path=Path('data')/name
        if (ROOT/path).exists():
            obj=load(path)
            add(LD,obj['alpha'],Fraction(obj['safe_D_lower']),'finite projection witness',path)
    for folder, family in [('axis_clamped_layercake','axis polygon clamp'),
                           ('axis_sector_cusp','axis sector cusp')]:
        for full in sorted((ROOT/'11_lattice_pole_constraints'/folder/'verification').glob('*_combined_*.json')):
            path=full.relative_to(ROOT);obj=load(path)
            assert obj['verdict'].startswith('CONFIRMED')
            add(LD,obj['alpha'],Fraction(obj['safe_D_lower_10_places']),family,path)
    for full in sorted((ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/verification').glob('*_combined.json')):
        path=full.relative_to(ROOT);obj=load(path)
        assert obj['verdict'].startswith('CONFIRMED')
        add(LD,obj['alpha'],Fraction(obj['safe_D_lower_10_places']),'axis projection cusp',path)
    path=Path('data/accepted_external_D.json')
    if (ROOT/path).exists():
        for row in load(path)['entries']:
            assert row['verdict']=='CONFIRMED'
            audit_path=Path(row['audit_path']); source_path=Path(row['source_path'])
            assert hashlib.sha256((ROOT/audit_path).read_bytes()).hexdigest()==row['audit_sha256']
            bound_audit=load(audit_path)
            for filename,digest in bound_audit.get('sha256',{}).items():
                assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
            assert hashlib.sha256(source_path.read_bytes()).hexdigest()==row['source_sha256']
            add(LD,row['alpha'],Fraction(row['safe_D_lower']),row['family'],path)
    lines=['# Independently rounded certified table','',
           'Each entry selects an already proved bound. Upper decimals are rounded upward, lower decimals downward. The C ratio is certified only at the listed exponents. The C lower bounds also apply to D because C <= D; the separate D column includes stronger projection witnesses where certified.','',
           '| alpha | upper C | upper D | lower C | lower D | C lower family | C ratio upper |',
           '|---|---:|---:|---:|---:|---|---:|']
    records=[]
    for original in base:
        a=Fraction(original['alpha']);uc=min(C[a],key=lambda z:z[0]);ud=min(D[a],key=lambda z:z[0]);lo=max(L[a],key=lambda z:z[0])
        dlo=max(LD[a],key=lambda z:z[0])
        cs=display(uc[0],True);ds=display(ud[0],True);ls=display(lo[0],False);dls=display(dlo[0],False)
        ratio=display(Fraction(cs)/Fraction(ls),True)
        lines.append(f'| {a} | {cs} | {ds} | {ls} | {dls} | {lo[1]} | {ratio} |')
        records.append(dict(alpha=str(a),upper_C=cs,upper_D=ds,lower_C_and_D=ls,lower_C=ls,lower_D=dls,C_ratio_upper=ratio,
                            selected_lower_D=dict(family=dlo[1],source=dlo[2],exact_safe_endpoint=str(dlo[0])),
                            selected_upper_C=dict(family=uc[1],source=uc[2],exact_safe_endpoint=str(uc[0])),
                            selected_upper_D=dict(family=ud[1],source=ud[2],exact_safe_endpoint=str(ud[0])),
                            selected_lower=dict(family=lo[1],source=lo[2],exact_safe_endpoint=str(lo[0]))))
    lines+=['','The formulas and audit verdicts are in `08_improved_upper_bounds/`, `05_team_audit/structured_endpoints/`, and `VERIFY_REPORT.md`. Exact selected endpoints, source paths and hashes are retained in `verified_table.json`.','']
    (ROOT/'data/verified_table.md').write_text('\n'.join(lines))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=records,input_sha256=inputs,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'data/verified_table.json').write_text(json.dumps(out,indent=2)+'\n')
    print('\n'.join(lines))
if __name__=='__main__':main()

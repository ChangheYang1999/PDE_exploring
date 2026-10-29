#!/usr/bin/env python3
"""First-tail extraction versus manufactured and equivalent source fields."""
from pathlib import Path
import datetime,json,time
import numpy as np
from numpy.polynomial import Polynomial as Poly,Legendre
from scipy.special import roots_legendre
from independent_artifacts import atomic_json,sha256
from independent_fields import ScalarExpansion,PotentialField
from independent_farfield import asymptotic_fixture
from eta_green_basis import EtaGreenField
from piecewise_adapter import PiecewiseField
from coefficient_tail import coefficient_audit,envelope_powers,at_power
ROOT=Path(__file__).resolve().parents[1]
def main():
    start=time.perf_counter();rows=[]
    def check(name,error,tol):
        error=float(np.max(abs(error)))
        if not np.isfinite(error) or error>tol:raise AssertionError((name,error,tol))
        rows.append(dict(name=name,error=error,tolerance=tol))
    mu,w=roots_legendre(48);radii=np.array([32.,128.,512.])
    for alpha in [.45,.5,.8]:
        field,data=asymptotic_fixture(alpha,corrected=True)
        d=coefficient_audit(field,radii,mu,w)
        check(f'corrected mismatch {alpha}',d['correction_mismatch_sphere_norm'],2e-12)
        check(f'first A extraction {alpha}',Poly(d['A1_saved'])(mu)-data['A1'](mu),1e-12)
        check(f'first B extraction {alpha}',Poly(d['B1_saved'])(mu)-data['B1'](mu),1e-12)
        assert not d['intervening_powers']
        errors=[r['observed_first_vs_saved_error'] for r in d['rows']]
        if not errors[-1]<errors[0]/10:raise AssertionError(('observed correction did not converge',alpha,errors))
        check(f'observed correction convergence {alpha}',errors[-1]/errors[0],.1)
        terms=[]
        for ds,dz,coef,extra in [(1,0,-8,0),(2,0,-4,1),(0,2,-1,0)]:
            terms.extend((coef*t.coefficient,t.i+extra,t.j,t.beta) for t in field.phi.differentiated(ds,dz))
        equivalent=EtaGreenField(ScalarExpansion(terms),field.q,field.c_l)
        d2=coefficient_audit(equivalent,np.array([24.,48.]),mu,w)
        check(f'equivalent source A {alpha}',Poly(d2['A'])(mu)-Poly(d['A'])(mu),2e-11)
        check(f'equivalent source A1 {alpha}',Poly(d2['A1_saved'])(mu)-Poly(d['A1_saved'])(mu),2e-11)
        check(f'equivalent source mismatch {alpha}',d2['correction_mismatch_sphere_norm'],2e-10)
        xyz=np.array([[.2,-.3,.7],[0.,0.,0.],[2.,1.,-3.]])
        check(f'equivalent source velocities {alpha}',equivalent.cartesian(xyz)-field.cartesian(xyz),2e-12)
        uncorrected,_=asymptotic_fixture(alpha,corrected=False)
        du=coefficient_audit(uncorrected,np.array([32.]),mu,w)
        if du['correction_mismatch_sphere_norm']<1e-3:raise AssertionError('uncorrected mismatch missed')
        check(f'uncorrected H zero {alpha}',du['saved_correction_sphere_norm'],1e-12)
        for L in [.13,2.3]:
            dl=coefficient_audit(field.dilate(L),np.array([32.*L]),mu,w)
            check(f'dilation A {alpha} {L}',Poly(dl['A'])(mu)-L**(alpha+1)*Poly(d['A'])(mu),2e-11)
            check(f'dilation A1 {alpha} {L}',Poly(dl['A1_saved'])(mu)-L**(2*alpha+2)*Poly(d['A1_saved'])(mu),2e-10)
    # An envelope correction contributes at an integer two-power gap.
    scalar=ScalarExpansion([(2.,0,0,.5)],length=3.)
    check('binomial first two coefficients',np.array([at_power(envelope_powers(scalar,3),1)(0)-2,at_power(envelope_powers(scalar,3),3)(0)+9]),0)
    # Populate a documented exterior independently from its polynomial data.
    old=PiecewiseField.load(ROOT/'external_exports/S1_pilot_L0_20261028T2003Z/coeffs.npz')
    field,data=asymptotic_fixture(old.alpha,corrected=True)
    coeff={k:np.zeros_like(v) for k,v in old.coefficients.items()}
    for key,first,second in [('phi',data['A'],data['A1']),('q',data['B'],data['B1'])]:
        p0=old.alpha+(key=='q');p1=2*old.alpha+1+(key=='q')
        labels=old.elements[2].get('labels_'+key,old.elements[2]['labels'])
        for p,poly in [(p0,first),(p1,second)]:
            leg=poly.convert(kind=Legendre).coef
            for j,(n,e) in enumerate(labels):
                if abs(e-p)<1e-12 and n<len(leg):coeff[key+'_el2'][j]=leg[n]/float(old.elements[2]['Rlo'])**p
    piece=PiecewiseField(old.metadata,coeff)
    dp=coefficient_audit(piece,np.array([32.,128.]),mu,w)
    check('piecewise exact correction',dp['correction_mismatch_sphere_norm'],3e-12)
    check('piecewise direct velocity remainder',dp['rows'][-1]['observed_first_vs_saved_error'],3e-11)
    check('piecewise vs envelope first A',Poly(dp['A1_saved'])(mu)-data['A1'](mu),1e-12)
    field,_=asymptotic_fixture(.6)
    extra=ScalarExpansion(list(field.phi.terms)+[(.3,0,0,.45)])
    intervening=coefficient_audit(PotentialField(extra,field.q,field.c_l),np.array([32.]),mu,w)['intervening_powers']
    if not any(abs(x['decay_power']-.9)<1e-12 for x in intervening):raise AssertionError('intervening power missed')
    check('intervening power detection',0,0)
    try:coefficient_audit(PotentialField(scalar,scalar,.5),np.array([32.]),mu,w)
    except ValueError:check('critical endpoint explicitly refused',0,0)
    else:raise AssertionError('critical endpoint accepted without multipole handling')
    files=[Path(__file__),ROOT/'src/coefficient_tail.py',ROOT/'src/eta_green_basis.py',ROOT/'src/piecewise_adapter.py',ROOT/'src/independent_farfield.py',ROOT/'src/independent_fields.py']
    out=dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start,source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in files})
    atomic_json(ROOT/'results/coefficient_tail_tests.json',out);print('PASS',len(rows),out['elapsed_seconds'])
if __name__=='__main__':main()

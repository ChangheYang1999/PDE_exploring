"""Independent spatial derivatives at the actual large hierarchy's extremal modes."""
from basis_tests import independent_fields,potential_jet,localcontext,D
from spectral_basis import evaluate_modes
from stage12_common import atomic,OUT,ROOT,digest,provenance
import numpy as np


def main():
    cl=1.88359472051
    modes=[{'family':'global','m':m,'n':n,'sigma':0.} for m,n in [(0,22),(4,22),(14,14),(22,0),(22,22)]]
    modes += [{'family':'local','m':m,'center':center,'width':width} for m,center,width in [(22,.5,.9),(22,8.5,.9),(22,8.,.65),(22,8.25,.45),(0,.75,.45)]]
    points=[(.13,.21),(1.2,.7),(3.,4.),(17.,9.),(256.,150.),(2.,0.),(0.,2.),(1e7,0.),(1e7,.3e7)]
    x=np.array([p[0] for p in points]);y=np.array([p[1] for p in points]);fields=evaluate_modes(x,y,cl,modes)
    rows=[]
    with localcontext() as ctx:
        ctx.prec=85
        for j,mode in enumerate(modes):
            for i,(px,py) in enumerate(points):
                exact=independent_fields(px,py,cl,mode)
                for key,value in exact.items():
                    actual=float(fields[key][i,j]);error=abs(actual-value)/max(1.,abs(value))
                    rows.append({'mode':j,'point':i,'field':key,'value':actual,'reference':value,'scaled_error':error})
            for derivative in [False,True]:
                assert not potential_jet(0.,0.,cl,mode,8,derivative).c
    maximum=max(row['scaled_error'] for row in rows)
    # This bound is an evaluator test, never a PDE or optimization tolerance.
    passed=maximum<2e-8
    output={'passed':passed,'maximum_scaled_spatial_error':maximum,'tolerance':2e-8,
            'reference':'85-digit Cartesian Taylor algebra; no native harmonic/radial spatial derivative formulas',
            'modes':modes,'points':points,'checks':rows,'origin_degree0_through8_and_cl_derivative_zero':True,
            'source_sha256':{name:digest(ROOT/name) for name in ['spectral_basis.py','basis_tests.py','basis_extreme_tests.py']},'provenance':provenance()}
    atomic(OUT/'basis_extreme_tests.json',output)
    print({'passed':passed,'maximum_scaled_spatial_error':maximum},flush=True)
    if not passed:raise SystemExit(1)

if __name__=='__main__':main()

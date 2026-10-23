"""Exact pairs built from a smooth scalar potential; not profile solutions."""
import sympy as sp
import numpy as np


def make_pair(p=sp.Rational(1,2), anisotropic=False):
    x,y=sp.symbols('x y',real=True)
    s=x*x+y*y
    if not anisotropic:
        psi=x*y*(1+s)**((p-1)/2)
        # Direct integration of -Delta[xy F(s)] with respect to x.
        rho=-y*(4+(p+3)*s)*(1+s)**((p-3)/2)
    else:
        H=(1+s)**((p+5)/2)
        lapH=sp.diff(H,x,2)+sp.diff(H,y,2)
        rho=sp.diff(lapH,x,2,y,1)
        psi=-sp.diff(H,x,3,y,1)
        a0=sp.diff(rho,y).subs({x:0,y:0})
        rho=rho/a0
        psi=psi/a0
    expressions={'rho':rho,'psi':psi,'u1':-sp.diff(psi,y),'u2':sp.diff(psi,x),'gx':sp.diff(rho,x),'gy':sp.diff(rho,y)}
    funcs={k:sp.lambdify((x,y),v,modules='numpy',cse=True) for k,v in expressions.items()}
    center={'a0':float(sp.diff(rho,y).subs({x:0,y:0})), 'c':float(sp.diff(psi,x,y).subs({x:0,y:0}))}
    if anisotropic:
        poisson=sp.simplify(-sp.diff(psi,x,2)-sp.diff(psi,y,2)-sp.diff(rho,x))
    else:
        poisson=sp.factor(-sp.diff(psi,x,2)-sp.diff(psi,y,2)-sp.diff(rho,x))
    if poisson != 0:
        raise ArithmeticError('Manufactured Poisson identity failed symbolically.')
    return funcs,center

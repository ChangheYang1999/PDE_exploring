"""Strict entry gates around the preserved exact residual arithmetic."""
import math
from fractions import Fraction as F
import numpy as np
from node_export_arithmetic import residual as _residual,decomposition as _decomposition

def exact(v):
    if isinstance(v,F):return v
    if type(v)is int:return F(v)
    if type(v)not in (float,np.float64):raise TypeError('requires Fraction, Python integer or binary64 scalar')
    if not math.isfinite(v):raise ValueError('nonfinite binary64 operand')
    a,b=v.as_integer_ratio();return F(a,b)

def array64(a,shape):
    a=np.asarray(a)
    if a.dtype!=np.dtype('float64')or a.shape!=tuple(shape):raise TypeError('binary64 array with exact declared shape required')
    if not np.all(np.isfinite(a)):raise ValueError('nonfinite exported array')
    return a

def residual(jet,velocity,c,x,y):
    return _residual(tuple(map(exact,jet[:3])),tuple(map(exact,velocity)),exact(c),exact(x),exact(y))

def decomposition(jet,producer_jet,velocity,map_velocity,c,x,y):
    J=tuple(map(exact,jet[:3]));JP=tuple(map(exact,producer_jet[:3]));Q=tuple(map(exact,velocity));M=tuple(map(exact,map_velocity));c,x,y=map(exact,(c,x,y))
    out=_decomposition(J,JP,Q,M,c,x,y)
    alternate_velocity=(Q[0]-M[0])*JP[1]+(Q[1]-M[1])*JP[2]
    alternate_jet=(c*x+Q[0])*(J[1]-JP[1])+(c*y+Q[1])*(J[2]-JP[2])-(J[0]-JP[0])
    denominator=residual(J,Q,c,x,y)['Nf']
    out.update(split_order='velocity at J, then jet change at Vm',common_denominator=denominator,alternate_velocity_term=alternate_velocity,alternate_jet_term=alternate_jet,alternate_identity=out['difference']==alternate_velocity+alternate_jet)
    return out

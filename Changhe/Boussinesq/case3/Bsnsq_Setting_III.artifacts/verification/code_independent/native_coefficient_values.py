"""Evaluate an active coefficient vector in the native physical divided-field basis."""
import numpy as np
from scipy.interpolate import BSpline


def divided_values(state,vector,active,points):
    points=np.asarray(points,dtype=float);r=np.hypot(points[:,0],points[:,1]);phi=np.arctan2(points[:,0],-points[:,1])
    ulog=-np.log1p((r/state.L)**2)/(2*state.bb);t=-np.expm1(ulog);eta=r/np.hypot(r,state.L)
    a=np.zeros(state.K*state.nb);a[np.asarray(active)]=vector;a=a.reshape(state.K,state.nb)
    S=BSpline(state.knots,a.T,state.degree,extrapolate=False)(t);k=np.arange(state.K)
    return np.exp((state.bb+1)*ulog)*np.sum(S*eta[:,None]**(k[None,:]%2)*np.cos(phi[:,None]*k[None,:]),axis=1)

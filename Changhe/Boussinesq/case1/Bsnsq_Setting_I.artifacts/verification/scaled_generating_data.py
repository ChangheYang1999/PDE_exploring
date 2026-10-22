"""Exact scale identities over the independently implemented unit-scale evaluator."""
from fractions import Fraction
import numpy as np
from cheb_generating_data import Model,LD
from cheb_generating_components import ComponentsModel

class ScaledModel(Model):
 def __init__(self,source):
  super().__init__(source)
  with np.load(source,allow_pickle=False) as z:
   self.se=LD(z['se']) if 'se' in z.files else LD(1)
   self.gam=LD(z['gam']) if 'gam' in z.files else LD(0)
   if not np.isfinite(self.se) or self.se<=0:raise ValueError('Finite positive se required')
   if self.gam!=0:raise ValueError('Nonzero gam is not supported')
   if not np.isfinite(self.alpha) or self.alpha<0:raise ValueError('Nonnegative finite alpha required')
  self.unit=ComponentsModel(source)
  if hasattr(self.unit,"se"):raise RuntimeError("Unit evaluator has changed its scale contract")
 def mixed(self,x,e):
  z=self.unit.mixed(x,np.asarray(e,dtype=LD)/self.se)
  if set(z)!=set('x eta y A B0 Psi G Theta Theta_x Theta_y normalized_A'.split()):raise RuntimeError('Unknown unit mixed keys')
  if np.any(~np.isfinite(z['A'])) or np.any(z['A']<=0):raise ValueError('Nonpositive or nonfinite chart at requested mixed point')
  for k in ['eta','y','B0','Psi','G','Theta','Theta_x']:z[k]=z[k]*self.se
  return z
 def mixed_vorticity(self,x,e,diagnostic=False):
  z=self.unit.mixed_vorticity(x,np.asarray(e,dtype=LD)/self.se,diagnostic=diagnostic)
  expected=set('x eta y A Omega Psi_xx Psi_yy Omega_alternate Omega_uncanceled U1 U2 U1_uncanceled U2_uncanceled Psi normalized_A Theta Theta_x Theta_y'.split())
  if diagnostic:expected.update('Ge Gee Geee B Ae Ax Bx V Ve Vx'.split())
  if set(z)!=expected:raise RuntimeError('Unknown unit vorticity keys')
  if np.any(~np.isfinite(z['A'])) or np.any(z['A']<=0):raise ValueError('Nonpositive or nonfinite chart at requested mixed point')
  z['Omega']=-self.se*z['Psi_xx']-z['Psi_yy']/self.se
  for k in ['eta','y','U2','Psi','Theta','Theta_x','Psi_xx']:z[k]=z[k]*self.se
  z['Psi_yy']=z['Psi_yy']/self.se
  # Unit-scale cancellation diagnostics are not physical scaled fields.
  for k in ['Omega_alternate','Omega_uncanceled','U1_uncanceled','U2_uncanceled']:z.pop(k,None)
  if diagnostic:
   for k in ['B','Bx']:z[k]=z[k]*self.se
   for k in ['Ae','Gee','Ve']:z[k]=z[k]/self.se
   z['Geee']=z['Geee']/self.se**2
  return z

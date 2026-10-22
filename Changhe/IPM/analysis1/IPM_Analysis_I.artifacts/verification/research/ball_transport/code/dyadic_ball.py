"""Exact JSON transport of finite real Arb balls; no decimal or float conversion."""
from flint import arb
import re
SCHEMA='arb-dyadic-mid-radius-v1'

def export_ball(x):
 if not x.is_finite():raise ValueError('finite Arb ball required')
 m,e=x.mid().man_exp();r,f=x.rad().man_exp()
 return {'schema':SCHEMA,'mid_m':str(m),'mid_e':str(e),'rad_m':str(r),'rad_e':str(f)}

def import_ball(data):
 if not isinstance(data,dict) or set(data)!={'schema','mid_m','mid_e','rad_m','rad_e'}:raise ValueError('wrong ball keys')
 if data['schema']!=SCHEMA:raise ValueError('wrong ball schema')
 if any(not isinstance(data[k],str) or re.fullmatch(r'0|-[1-9][0-9]*|[1-9][0-9]*',data[k]) is None for k in ('mid_m','mid_e','rad_m','rad_e')):raise ValueError('noncanonical integer string')
 m,e,r,f=[int(data[k]) for k in ('mid_m','mid_e','rad_m','rad_e')]
 if r<0:raise ValueError('negative radius')
 center=arb((m,e));radius=arb((r,f))
 return center+arb(0,radius.upper())

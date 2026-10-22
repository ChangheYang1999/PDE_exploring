"""iv160 independent squared/half-angle physical geometry for all832 blocks."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,sys
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];iv.dps=160;tic=time.monotonic();ff=lambda x:Q.from_float(float(x))
def vi(x):return iv.mpf(x.numerator)/x.denominator
def ep(t):
 s,m,e,_=t;return Q(-m if s else m)*Q(2)**e
def lo(x):return ep(x._mpi_[0])
def hi(x):return ep(x._mpi_[1])
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((D/'evidence/blocks.json').read_text());raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text());assert len(rows)==832
p1,p2=map(ff,raw['x_star_bracket']);assert 0<p1<p2;pp=iv.mpf([vi(p1),vi(p2)]);dth=ff(raw['theta_max'])/16
records=[];fails=[];minlo=minhi=None
for n,r in enumerate(rows):
 H,W,c,U,x=map(ff,[r[k] for k in ['H','W','c0','Umax','xr']]);w,wk=ff(r['w']),ff(r['wk']);center=dth*Q(2*r['q']+1,2)
 aa=max(Q(0),center-w+4*r['bp']*wk);bb=min(center+w,center-w+4*(r['bp']+1)*wk);assert 0<=aa<bb<Q(1,100)
 tlo=ff(r['tb'])-ff(r['tb_rad'])+r['bs']*H;thi=ff(r['tb'])+ff(r['tb_rad'])+min((r['bs']+1)*H,ff(r['h']));assert tlo<thi
 rl=lo(iv.exp(vi(tlo)));ru=hi(iv.exp(vi(thi)));assert 0<rl<ru
 pc=pp*iv.cos(vi(aa));ps=pp*iv.sin(vi(aa));gap=max(Q(0),rl-hi(pc),lo(pc)-ru);yl=max(Q(0),lo(ps))
 ql=lo(vi(gap)**2+vi(yl)**2)
 sh=iv.sin(vi(bb)/2);qu=max(hi((vi(rr)-pp)**2+4*vi(rr)*pp*sh**2) for rr in [rl,ru])
 ml=ql-c*(1-x);mh=c*(1+x)-qu
 if min(ml,mh)<0:fails.append({'index':n,'key':[r[k] for k in ['ci','q','bs','bp']],'lower_margin':str(ml),'upper_margin':str(mh),'active':r['active']})
 minlo=ml if minlo is None else min(minlo,ml);minhi=mh if minhi is None else min(minhi,mh)
 records.append({'index':n,'q_lower':str(ql),'q_upper':str(qu),'q_ratio_lower_margin':str(ml),'q_ratio_upper_margin':str(mh)})
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_IV160_SQUARED_HALFANGLE_GEOMETRY' if not fails else 'OPEN_IV_GEOMETRY_FAILURES','blocks':832,'minimum_q_ratio_lower_margin':str(minlo),'minimum_q_ratio_upper_margin':str(minhi),'failures':fails,'records':records,'blocks_sha256':sha(D/'evidence/blocks.json'),'method':'No distance square roots. Exact squared projection gap lower bound; independent half-angle radial endpoint upper bound, uniform p interval.'}
(D/'evidence/geometry_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],len(fails));print('minimum_q_margins',float(minlo),float(minhi));assert not fails,fails[:2]

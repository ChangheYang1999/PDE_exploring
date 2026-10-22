"""Exact saved-scalar audit with independent interval checks; no producer imports."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal,localcontext
import ast,hashlib,json,math,re,time
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/x3_closure_diagnostics';ctx.prec=384;iv.dps=140
assert not sys.flags.optimize
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def unique(items):
 d={}
 for k,v in items:need(k not in d,'duplicate key');d[k]=v
 return d
def load(p):return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def scalar(x):
 need(type(x) is float and math.isfinite(x),'finite binary64');return F.from_float(x)
def av(x):return arb(x.numerator)/arb(x.denominator)
def ivv(x):return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def binary_tuple(t):
 s,m,e,b=t;need(b>=0,'finite iv endpoint');return F((-1)**s*m)*(F(2)**e)
def pair(v):return [binary_tuple(t) for t in v._mpi_]
def check_interval(x,y,q):
 aa=(av(y)-av(x))/av(x);ii=ivv(y)/ivv(x)-1;al,ah=F(str(aa.lower().fmpq())),F(str(aa.upper().fmpq()));il,ih=pair(ii);need(al<=q<=ah and il<=q<=ih,'two independent arithmetic enclosures');return [str(v) for v in [al,ah,il,ih]]
def rounded(q,text):
 d=Decimal(text);step=F(10)**d.as_tuple().exponent
 need(abs(q-F(d))<=step/2,'printed rounding cell '+text)
 return {'printed':text,'exact_value':str(q),'step':str(step)}
m=load(D/'data_exact/manifest.json');pins=dict(m['files'])
for n,h in pins.items():need(sha(B/n)==h,'captured source pin')
x3=load(B/'data_exact/x3.json');p=load(D/'data_exact/parameters.json');k,L=F(p['k']),F(p['L']);a=1-k
need(k==F.from_float(float.fromhex(x3['scalars_hex']['k'])) and L==F.from_float(float.fromhex(x3['scalars_hex']['L'])),'exact X3 parameter identity');need(0<k<F(1,3) and L>0 and F(p['p'])==6+2*k/(2-k),'power hypotheses')
knots=[F.from_float(float.fromhex(v)) for v in x3['spline_knots_hex']];need(knots==sorted(knots) and knots[0]==0 and knots[-1]==1 and any(t<1 for t in knots),'last nonempty spline span');need(x3['integers']==p['x3_integers'],'exact integer conventions');need(len(x3['z_hex'])==1+(p['x3_integers']['angular']+1)*p['x3_integers']['degree']+p['x3_integers']['singular'],'coefficient count')
ordered=sorted((j*a+2*l,j,l) for j in range(8) for l in range(4));need([(j,l) for _,j,l in ordered[:5]]==[(0,0),(1,0),(2,0),(0,1),(3,0)],'four ordered powers and next');powers=[k-1-z for z,_,_ in ordered[:5]];need(powers==[k-1,2*k-2,3*k-3,k-3,4*k-4],'all exponents')
# Bind the complete captured source functions and the relevant assignments, without importing them.
asts={n:ast.parse((D/'sources'/n).read_text()) for n in ['num/inverse.py','num/x3_resid.py','lead/run.py','lead/run2.py']}
def dump(x):return ast.dump(x,include_attributes=False)
def has(tree,s):
 target=ast.parse(s).body[0];return any(dump(n)==dump(target) for n in ast.walk(tree))
checks=[('num/inverse.py','f = self.modes(fx)'),('num/inverse.py','b[-1] = self._tail_start(f)'),('num/inverse.py','qs = np.asarray(self.tail_powers, float)'),('num/inverse.py','denom = (2 * n[None, :] - 2 - qs[:, None])'),('num/inverse.py','return R ** 2 * (A / denom).sum(0)'),('num/inverse.py','return dst(fx[:, 1:-1], type=1, axis=1) / self.Nt'),('lead/run.py',"TD = float(sys.argv[5])"),('lead/run.py',"kw['tail_decades'] = TD"),('lead/run2.py',"MODE = sys.argv[5]"),('lead/run2.py',"kw['tail_powers'] = None"),('lead/run2.py',"kw['tail_powers'] = [kw['k'] - 1]"),('num/x3_resid.py','inv = ModalInverse(r, th, p=p, tail_powers=tail_powers, k=k, tail_decades=tail_decades)'),('num/x3_resid.py','psi, dpsi, c = inv.solve(rho_x)')]
for n,s in checks:need(has(asts[n],s),'exact source AST '+s)
functions={v.name:v for v in ast.walk(asts['num/inverse.py']) if isinstance(v,ast.FunctionDef)};tail=functions['_tail_start'];need(has(tail,'if self.tail_powers is None:\n return np.zeros(f.shape[1])'),'zero source closure');need(has(tail,'A, *_ = np.linalg.lstsq(X, f[sel], rcond=None)'),'least squares coefficients');need(has(tail,'X = (self.r[sel, None] / R) ** qs[None, :]'),'scaled source powers')
# Both labels and all ten reported regions are checked for finite scalars and grid provenance.
files={'saved16875':D/'sources/num/resid_N16875_q512.json','saved22500':D/'sources/num/resid_N22500_q768.json'}
files.update({n:D/'sources/lead'/f'{n}.json' for n in ['base']+m['variants']});data={n:load(p) for n,p in files.items()};rows={};gridchecks=0
for name,v in data.items():
 need(type(v['Nr']) is int and v['Nr']>1 and type(v['Nt']) is int and v['Nt']>1 and v['p']==6,'grid parameters');r0,r1=scalar(v['rmin']),scalar(v['rmax']);need(0<r0<r1,'positive grid limits')
 need(scalar(v['c_l_stored'])==F.from_float(float.fromhex(x3['scalars_hex']['c_l'])),'stored c_l identity');need(scalar(v['c_stored'])==F.from_float(float.fromhex(x3['scalars_hex']['c'])),'stored c identity');need(v['c_l_identity']==(1+v['c'])/3,'identity output formula');need(set(v['results'])=={'stored','identity'},'two c_l labels')
 for label in ['stored','identity']:
  rr=v['results'][label]['rows'];need(len(rr)==10 and len({t['region'] for t in rr})==10,'unique complete regional rows');rm={t['region']:t for t in rr};need(set(m['regions'])|{'all','r<=1000'}==set(rm),'all expected regions');need(v['results'][label]['c_l']==v['c_l_'+('stored' if label=='stored' else 'identity')],'row c_l');xp=scalar(v['results'][label]['x_star'])
  for g,row in rm.items():
   for col in ['Nf_max','Nv_max','abs_max','Nf_max_cut','Nv_max_cut']:
    val,rad,theta=map(scalar,row[col]);need(val>=0 and r0<=rad<=r1 and 0<=theta<=F.from_float(math.pi/2),'finite maximum triple')
    # Diagnostic grid reconstruction from stored endpoints; not a physical argmax re-evaluation.
    ti=(math.log(float(rad))-math.log(float(r0)))/(math.log(float(r1))-math.log(float(r0)))*(v['Nr']-1);tj=float(theta)/(math.pi/2)*v['Nt'];need(abs(ti-round(ti))<1e-7 and abs(tj-round(tj))<1e-9,'saved point belongs to stated grid');gridchecks+=1
    if col.endswith('_cut'):need(math.pi/2-float(theta)>=0.006-1e-15,'angular cutoff')
    tests={'r<=0.1':rad<=F.from_float(.1),'0.1<=r<=2':F.from_float(.1)<=rad<=2,'2<=r<=10':2<=rad<=10,'10<=r<=100':10<=rad<=100,'100<=r<=1000':100<=rad<=1000,'1000<=r<=1000L':1000<=rad<=1000*L,'r>1000L':rad>1000*L,'r<=1000':rad<=1000,'all':True,'|X-P|<0.5':math.hypot(float(rad)*math.cos(float(theta))-float(xp),float(rad)*math.sin(float(theta)))<.5+1e-13};need(tests[g],'saved point in named region')
  if label=='stored':rows[name]=rm
summary=(D/'sources/lead/SUMMARY.md').read_text();lines=summary.splitlines();relative=[];rounding=[];observed={};base=rows['base']
for name in m['variants']:
 pos=lines.index('== '+name);observed[name]=[]
 for line,g in zip(lines[pos+1:pos+9],m['regions'],strict=True):
  need(line.strip().startswith(g),'regional table order');tokens=re.findall(r'(?:Nf|Nv|abs) ([+-][0-9.]+e[+-][0-9]+)',line);need(len(tokens)==3,'three printed changes')
  for col,token in zip(m['columns'],tokens,strict=True):
   x=scalar(base[g][col][0]);y=scalar(rows[name][g][col][0]);need(x>0,'positive base maximum');q=(y-x)/x;intervals=check_interval(x,y,q);rounding.append(rounded(q,token));record={'variant':name,'region':g,'column':col,'base_exact':str(x),'variant_exact':str(y),'relative_change_exact':str(q),'intervals_arb_iv':intervals,'printed':token};relative.append(record);observed[name].append((abs(q),q,g,col))
# Location table: decimal rounding cells for all 144 scalars, no original float formatting calls.
locpos=next(i for i,s in enumerate(lines) if s.startswith('(a) locations'))
for line,g in zip(lines[locpos+1:locpos+9],m['regions'],strict=True):
 need(line.startswith(g),'location table order');parts=line[len(g):].strip().split(' ; ');need(len(parts)==3,'three maxima table entries')
 for part,col in zip(parts,m['columns'],strict=True):
  vals=re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?',part);need(len(vals)==6,'six location scalars')
  for name,values in [('saved16875',vals[:3]),('saved22500',vals[3:])]:
   for q,t in zip(map(scalar,rows[name][g][col]),values,strict=True):rounding.append(rounded(q,t))
basechange=[]
for g in m['regions']:
 for col in m['columns']:
  old=rows['saved16875'][g][col];new=base[g][col];need(old[1:]==new[1:],'saved/current maximum locations equal');q=(scalar(new[0])-scalar(old[0]))/scalar(old[0]);basechange.append((abs(q),q,g,col))
# Exact ideal log-grid alignment uses number of intervals, independently of float reconstruction.
need(F(10,data['base']['Nr']-1)==F(15,data['ext1e11']['Nr']-1),'aligned nominal extension');need(F(9,data['ext1e5']['Nr']-1)!=F(10,data['base']['Nr']-1) and F(11,data['ext1e7']['Nr']-1)!=F(10,data['base']['Nr']-1),'unaligned nominal extents')
summary_records={}
for name,rr in observed.items():
 small=min(rr);large=max(rr);summary_records[name]={'min_abs_change':str(small[0]),'max_abs_change':str(large[0]),'min_abs_location':list(small[2:]),'max_abs_location':list(large[2:]),'min_abs_change_display':float(small[0]),'max_abs_change_display':float(large[0])}
alllobe=[scalar(v['2<=r<=10']['abs_max'][0]) for v in rows.values()];corelobe=[scalar(rows[n]['2<=r<=10']['abs_max'][0]) for n in files if not n.startswith('tp_')];none=[1+q for _,q,_,_ in observed['tp_none']]
summary_records['base_vs_saved']={'maximum_abs_relative_exact':str(max(basechange)[0]),'display':float(max(basechange)[0]),'location':list(max(basechange)[2:]),'all_24_locations_identical':True};summary_records['core_lobe_range']={'min_exact':str(min(corelobe)),'max_exact':str(max(corelobe)),'display':[float(min(corelobe)),float(max(corelobe))]};summary_records['zero_source_multipliers']={'min_exact':str(min(none)),'max_exact':str(max(none)),'display':[float(min(none)),float(max(none))]}
for n,h in pins.items():need(sha(B/n)==h,'final unchanged inputs')
for pp in [Path(__file__),D/'data_exact/manifest.json']:pins[str(pp.relative_to(B))]=sha(pp)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SAVED_MAXIMA_REPORT_AND_EXACT_FAR_POWER_ORDER','counts':{'source_ast_matches':len(checks)+3,'grid_point_diagnostics':gridchecks,'relative_changes':len(relative),'rounding_cells':len(rounding),'interval_enclosures':2*len(relative),'saved_location_triples':48},'parameters':{'k':str(k),'L':str(L),'last_nonempty_spline_left':str(max(t for t in knots if t<1)),'five_allowed_powers':[str(v) for v in powers]},'summary':summary_records,'relative_changes':relative,'rounding_checks':rounding,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Exact arithmetic about saved binary64 scalars and their printed summaries; source AST and floating grid-location diagnostics. No independent physical argmax computation, full-grid rerun, runtime source attestation, certified X3 residual or tail remainder constant.'}
p=D/'evidence/check.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','counts','summary','seconds']},indent=2))

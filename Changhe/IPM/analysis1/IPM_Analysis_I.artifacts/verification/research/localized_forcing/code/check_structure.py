"""Bind finite dimensions, power tables and source bracket without a radial run."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast,json,hashlib,zipfile
import numpy as np
from flint import arb,ctx
from mpmath import iv
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=256;iv.dps=100

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as z:
  for b in iter(lambda:z.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
def ff(x):return F.from_float(float(x))
def ar(x):return arb(x.numerator)/x.denominator
def ir(x):return iv.mpf(x.numerator)/x.denominator
manifest=read(D/'evidence/snapshot_manifest.json');pins={}
for name in ['src/cert_forcing.py','src/cert_resid.py','src/midrad.py','runs/forcing/p9_K64_n16_P8_merged.json']:
 e=manifest['sources'][name];p=B/e['snapshot'];assert sha(p)==e['sha256'];pins[str(p.relative_to(B))]=e['sha256']
forcing=ast.parse((D/'source/src/cert_forcing.py').read_text());resid=ast.parse((D/'source/src/cert_resid.py').read_text())
# Exact AST matches ensure these are the parsed producing expressions.
def assignment(nodes,target,expr):
 expected=ast.dump(ast.parse(expr,mode='eval').body)
 matches=[n for root in nodes for n in ast.walk(root) if isinstance(n,ast.Assign) and any(ast.unparse(t)==target for t in n.targets)]
 assert len(matches)==1,(target,len(matches))
 assert ast.dump(matches[0].value)==expected,(target,ast.unparse(matches[0].value))
 return {'target':target,'value':ast.unparse(matches[0].value),'line':matches[0].lineno}
cert=next(n for n in resid.body if isinstance(n,ast.ClassDef) and n.name=='Certifier');init=next(n for n in cert.body if isinstance(n,ast.FunctionDef) and n.name=='__init__')
main=next(n for n in forcing.body if isinstance(n,ast.FunctionDef) and n.name=='main')
checks=[]
for t,e in [('self.T','MR(d["T_mid"], d["T_rad"])'),('self.M','self.T.m.shape[2]'),('self.Nmax','2*self.M+2'),('self.Q','Q'),('self.tb','MR(d["tb"], d["tb_rad"])')]:checks.append(assignment([init],t,e))
for t,e in [('C','Certifier(green,trial,Q=12)'),('Qs','C.Q'),('Nmax','C.Nmax'),('h','C.tb[ci+1]-C.tb[ci]'),('h_up','h.mag()'),('cell','Cell(h_up,w_up,Qs,Qp)'),('twoN1','2.0*np.arange(Nmax+1)+1.0'),('epsSup','[eps[i].sup(hpow1) for i in range(NDER+1)]'),('r2','succ((epsSup[i]*A["remfac"][j]).sum()*succ(1+(Nmax+2)*U))')]:checks.append(assignment([main],t,e))
# remfac is rebuilt in each q iteration solely from the same fpow and wq.
remapp=[n for n in ast.walk(main) if isinstance(n,ast.Call) and ast.unparse(n.func)=='remfac.append'];assert len(remapp)==1
assert ast.dump(remapp[0].args[0])==ast.dump(ast.parse('succ(mag(fpow[j+Qp+1])*wq*(1+2*U))',mode='eval').body)
checks.append({'remfac_append':ast.unparse(remapp[0]),'line':remapp[0].lineno})
for t,e in [('fpow','[MR.exact(np.ones(Nmax+1))]'),('wq','succ(w_up**(Qp+1)*(1+2*(Qp+1)*U)/factorial(Qp+1))')]:checks.append(assignment([main],t,e))
fpapp=[n for n in ast.walk(main) if isinstance(n,ast.Call) and ast.unparse(n.func)=='fpow.append'];assert len(fpapp)==1 and ast.dump(fpapp[0].args[0])==ast.dump(ast.parse('fpow[-1]*MR.exact(twoN1)',mode='eval').body)
# Only headers and two tiny knot arrays are read. No large array is loaded.
p=Path('numerics/data/cert_green.npz');geo=read(D/'evidence/geometry_arb.json');assert sha(p)==geo['green_sha256'];pins[str(p)]=geo['green_sha256']
headers={}
with zipfile.ZipFile(p) as z:
 for name in ['T_mid','T_rad','tb','tb_rad','A_mid','A_rad','B_mid','B_rad']:
  with z.open(name+'.npy') as f:
   magic=f.read(8);assert magic[:6]==b'\x93NUMPY' and magic[6] in [1,2,3]
   size=int.from_bytes(f.read(2 if magic[6]==1 else 4),'little');h=ast.literal_eval(f.read(size).decode());assert h['descr']=='<f8' and not h['fortran_order'];headers[name]=h
assert headers['T_mid']==headers['T_rad'] and tuple(headers['T_mid']['shape'])==(7809,8,260)
for name in ['A_mid','A_rad','B_mid','B_rad']:assert tuple(headers[name]['shape'])==(7810,261)
assert headers['tb']==headers['tb_rad'] and tuple(headers['tb']['shape'])==(7810,)
M=headers['T_mid']['shape'][2];Nmax=2*M+2;n=Nmax+1;assert n==523
raw=read(D/'source/runs/forcing/p9_K64_n16_P8_merged.json');pars={'Qs':12,'Qp':8,'KSUB':64,'KP':8,'ntheta':16}
for k,v in pars.items():assert raw[k]==v
part_count=0
for name,e in manifest['sources'].items():
 if name.startswith('runs/forcing/') and name.endswith('.json') and not name.endswith('_merged.json'):
  part=read(B/e['snapshot']);assert all(part[k]==v for k,v in pars.items());part_count+=1
assert part_count==13
Qs,Qp=raw['Qs'],raw['Qp'];assert (Qs+1)*(Qp+1)==117 and (2*Qs+1)*(2*Qp+1)==425
# Isolate the exact frozen primitive and Cell class, omitting module main.
ns={'__name__':'frozen_midrad_structure'};exec(compile((D/'source/src/midrad.py').read_text(),'frozen_midrad_structure','exec'),ns)
MR=ns['MR'];U=ns['U'];succ=ns['succ'];cl=next(x for x in forcing.body if isinstance(x,ast.ClassDef) and x.name=='Cell')
ns2={'np':np,'succ':succ,'U':U};exec(compile(ast.Module(body=[cl],type_ignores=[]),'frozen_Cell','exec'),ns2);Cell=ns2['Cell']
with np.load(p) as z:tb=z['tb'][4096:4110].copy();tr=z['tb_rad'][4096:4110].copy()
dth=ff(raw['theta_max'])/raw['ntheta'];w=float(succ(float(dth/2)));assert ff(w)==ff(geo['w_up'])
power_identity=0
for q,g in enumerate(geo['cells']):
 assert g['ci']==4096+q
 h=float((MR(tb[q+1],tr[q+1])-MR(tb[q],tr[q])).mag());assert ff(h)==ff(g['h_up'])
 c=Cell(h,w,Qs,Qp);assert c.Qs==Qs and c.Qp==Qp and len(c.hpow)==27 and len(c.wpow)==19
 exp_h=[1.0]+[float(succ(h**j*(1+2*j*float(U)))) for j in range(1,27)]
 exp_w=[1.0]+[float(succ(w**j*(1+2*j*float(U)))) for j in range(1,19)]
 for actual,expected in zip(list(c.hpow)+list(c.wpow),exp_h+exp_w):assert ff(actual)==ff(expected);power_identity+=1
 # All truncation weights are identical to the independently checked tables.
 for i in range(25):
  for j in range(17):assert ff(c.hpow[i])*ff(c.wpow[j])>=F(2)**-1022
assert power_identity==598
# Bind the saved geometric source bracket to the certified exact source.
const=next(x for x in forcing.body if isinstance(x,ast.Assign) and ast.unparse(x.targets[0])=='(XSTAR_LO, XSTAR_HI)')
xs=list(map(ff,ast.literal_eval(const.value)));assert xs==list(map(ff,raw['x_star_bracket']))
vpath=B/'research/source_jet_corrections/evidence/verdict.json';v=read(vpath);assert v['status']=='CONFIRMED_LOCAL_SOURCE_JET_AND_NORMALIZED_OBSTRUCTION'
for name,h in v['files'].items():assert sha(B/name)==h; pins[name]=h
pins[str(vpath.relative_to(B))]=sha(vpath)
source=read(B/'research/modal_source/evidence/source_result.json');jets=read(B/'research/source_jet_corrections/evidence/checks.json');root=list(map(F,source['final_root_endpoints_exact']));assert root==list(map(F,jets['root_bracket_exact']))
margins=[root[0]-xs[0],xs[1]-root[1]];assert min(margins)>0
for m in margins:assert ar(m).lower()>0 and ir(m).a>0
proof=D/'DATA_STRUCTURE.md';receipt=D/'evidence/data_structure_proof_first.json';assert read(receipt)['sha256']==sha(proof)
for p in [proof,receipt,Path(__file__),D/'evidence/geometry_arb.json',B/'research/source_jet_corrections/evidence/checks.json',B/'research/modal_source/evidence/source_result.json']:pins[str(p.relative_to(B))]=sha(p)
output={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SOURCE_DIMENSIONS_TABLE_IDENTITY_AND_CANONICAL_ROOT_LINKAGE','source_assignments':checks,'npz_headers':headers,'M':M,'Nmax':Nmax,'n':n,'retained_table':117,'full_table':425,'parameters':pars,'parts':part_count,'power_entry_identity_checks':power_identity,'independent_r2_sums':13*15,'root_bracket_exact':list(map(str,root)),'merged_bracket_exact':list(map(str,xs)),'root_containment_margins':list(map(str,margins)),'prior_source_pins':len(v['files']),'pins':pins,'scope':'Finite structure and geometry/source identity only. No inherited modal enclosure, r2 actual sums, full kernel or physical forcing bound accepted.'}
(D/'evidence/structure.json').write_text(json.dumps(output,indent=2)+'\n');print(output['utc'],output['status'],'pins',len(pins),'assignments',len(checks),'power_checks',power_identity)

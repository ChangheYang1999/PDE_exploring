"""Finite exact block geometry and current-source remainder inclusion."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,ast,copy,sys
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];s=(D/'source/src/cert_forcing.py').read_text();tree=ast.parse(s);pg=json.loads((B/'research/localized_forcing/evidence/geometry_arb.json').read_text());ff=lambda x:Q.from_float(float(x));U=2.0**-53
cellclass=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='Cell');ns={'np':np,'succ':lambda x:np.nextafter(x,np.inf),'U':U};exec(compile(ast.Module(body=[cellclass],type_ignores=[]),'frozen_block_Cell','exec'),ns)
checks=0;powers=0;weights=0;records=[];w=ff(pg['w_up']);wk=ff(pg['wk'])
for row in pg['cells']:
 h=ff(row['h_up']);hk=ff(row['hk']);hb=32*hk;wb=4*wk;assert hb==ff(float(hb)) and wb==ff(float(wb))
 c=ns['Cell'](float(hb),float(wb/2),12,8)
 for p,x in enumerate(c.hpow):assert ff(x)>=hb**p;powers+=1
 for p,x in enumerate(c.wpow):assert ff(x)>=(wb/2)**p;powers+=1
 for a in c.hpow:
  for b in c.wpow:assert ff(a)*ff(b)>Q(2)**-900;weights+=1
 assert 2*hb>=h and 2*wb>=2*w
 for bs in range(2):
  for bp in range(2):
   a_s=bs*hb;a_p=-w+bp*wb+wb/2
   for ks in range(32):
    assert a_s+ks*hk==(bs*32+ks)*hk;assert a_s+(ks+1)*hk==(bs*32+ks+1)*hk;checks+=2
   for kp in range(4):
    assert a_p-wb/2+kp*wk==-w+(bp*4+kp)*wk;assert a_p-wb/2+(kp+1)*wk==-w+(bp*4+kp+1)*wk;checks+=2
 records.append({'ci':row['ci'],'hb_exact':str(hb),'half_wb_exact':str(wb/2)})
bitm=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='BiTM');sup=next(n for n in bitm.body if isinstance(n,ast.FunctionDef) and n.name=='sup_crude');ret=next(n for n in sup.body if isinstance(n,ast.Return));e=ret.value
assert isinstance(e,ast.Call) and ast.unparse(e.func)=='succ' and len(e.args)==1
assert isinstance(e.args[0],ast.BinOp) and isinstance(e.args[0].op,ast.Add) and ast.unparse(e.args[0].right)=='self.r'
# Evaluate exactly the frozen scalar bracket definitions, with no producer import.
needed=['XSTAR_LO','XSTAR_HI','XSTAR','XRAD'];assign=[]
for name in needed:
 n=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for target in n.targets for t in ast.walk(target)))
 if n not in assign:assign.append(n)
bns={'np':np};exec(compile(ast.Module(body=assign,type_ignores=[]),'frozen_source_bracket','exec'),bns)
x=json.loads((D/'source/runs/forcing/v21_p9_merged.json').read_text());lo,hi=map(ff,x['x_star_bracket']);assert ff(bns['XSTAR'])-ff(bns['XRAD'])<=lo<=hi<=ff(bns['XSTAR'])+ff(bns['XRAD'])
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_BLOCK_DOMAINS_AND_REMAINDER_INCLUSION','block_cell_count':13,'coordinate_identities':checks,'outward_power_checks':powers,'normal_weight_checks':weights,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'sup_crude_return_expression':ast.unparse(ret.value),'bracket_exact':[str(lo),str(hi)],'source_center_radius':[str(ff(bns['XSTAR'])),str(ff(bns['XRAD']))],'records':records,'scope':'Restricted-domain interpretation in ADDENDUM; finite new block powers and syntactic radius inclusion, no full Taylor-model certification.'}
(D/'evidence/blocks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],checks,powers,weights)

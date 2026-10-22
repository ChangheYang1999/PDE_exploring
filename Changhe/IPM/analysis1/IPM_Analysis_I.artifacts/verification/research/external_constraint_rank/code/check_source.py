"""Static source binding. Does not execute the numerical assembly or certify runtime arrays."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/external_constraint_rank'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def dump(n):return ast.dump(n,include_attributes=False)
def need(v,s):
 if not v:raise ValueError(s)
a=json.loads((D/'evidence/output_audit.json').read_text());pins=dict(a['files'])
for n,h in pins.items():need(sha(B/n)==h,'accepted input digest')
expected_constraints='''def constraints(NJ, sel):
 rows = []
 for m in range(Mh):
  for join in (tmin, t00):
   for nu in range(NJ + 1):
    row = np.zeros(len(sel))
    for li, gi in enumerate(sel):
     if gi < nF and int(col_m[gi]) == m:
      pcs = cols[gi][1]
      row[li] = (piece_jet(pcs, join, "-", nu) - piece_jet(pcs, join, "+", nu)) * D[gi]
    if np.any(row): rows.append(row)
 return np.array(rows) if rows else np.zeros((0, len(sel)))'''
expected_jet='''def piece_jet(pieces, t, side, nu):
 for (a, b, alpha, c) in pieces:
  if side == "-" and b == t: sig = 0.0 if np.isinf(a) else (t - a)
  elif side == "+" and a == t: sig = 0.0
  else: continue
  cc = np.array(c, float)
  for _ in range(nu):
   dc = alpha * cc
   if len(cc) > 1: dc[:-1] += cc[1:] * np.arange(1, len(cc))
   cc = dc
  return float(np.exp(alpha * sig) * np.polyval(cc[::-1], sig))
 return 0.0'''
assignments=['Mh = int(d["Mh"])','tmin = float(d["tmin"])','t00 = float(d["t0"])','col_m = d["col_m"]','cols = meta["cols"]','nF = len(cols)','dg = np.sqrt(np.maximum(np.diag(G), 1e-300))','D = 1.0 / dg','kptau_idx = [nF, nF + 1]']
records=[]
for label,rel,h in [('frozen_v2','research/gram_internal_jumps/sources/src__c2_gram.py',None),('snapshot_v3','notes/constraint_rank_watch/c2_gram2.py','958a27152449e90e2fd1723bf90a7e479181d913d6edccb7ad3cc48146e7d085')]:
 p=B/rel;need((h is None and rel in pins) or sha(p)==h,'source anchor');s=p.read_text();t=ast.parse(s);nodes=list(ast.walk(t));ex=[]
 for name,exp in [('constraints',expected_constraints),('piece_jet',expected_jet)]:
  f=[n for n in nodes if isinstance(n,ast.FunctionDef) and n.name==name];need(len(f)==1,'unique function');f=f[0];ex.append((name,f));copy=ast.parse(ast.get_source_segment(s,f)).body[0]
  if copy.body and isinstance(copy.body[0],ast.Expr) and isinstance(copy.body[0].value,ast.Constant) and isinstance(copy.body[0].value.value,str):copy.body=copy.body[1:]
  need(dump(copy)==dump(ast.parse(exp).body[0]),'complete function AST')
 for exp in assignments:
  q=ast.parse(exp).body[0];name=q.targets[0].id;hits=[n for n in nodes if isinstance(n,ast.Assign) and any(isinstance(v,ast.Name) and v.id==name for target in n.targets for v in ast.walk(target))];need(len(hits)==1 and dump(hits[0])==dump(q),'unique assignment '+name);ex.append((name,hits[0]))
 tuples=[n for n in nodes if isinstance(n,ast.Tuple) and len(n.elts)==2 and isinstance(n.elts[0],ast.Constant) and n.elts[0].value=='Fminus'];need(len(tuples)==1 and dump(tuples[0])==dump(ast.parse('("Fminus", list(range(nF+2)))',mode='eval').body),'Fminus coefficient selection');ex.append(('Fminus',tuples[0]))
 arrays=[n for n in nodes if isinstance(n,ast.Call) and dump(n.func)==dump(ast.parse('np.column_stack',mode='eval').body) and n.args and dump(n.args[0])==dump(ast.parse('[Mat,KP,TAU,tails]',mode='eval').body)];need(len(arrays)==1,'operator coordinate order');ex.append(('column_stack',arrays[0]))
 ccall=[n for n in nodes if isinstance(n,ast.Assign) and dump(n)==dump(ast.parse('C=constraints(NJ,sel)').body[0])];need(len(ccall)==1,'actual constraints call');ex.append(('C_call',ccall[0]))
 spans=[]
 for name,n in ex:
  text=ast.get_source_segment(s,n)+'\n';out=D/'sources'/(label+'__'+name+'.txt')
  with out.open('x') as f:f.write(text)
  pins[str(out.relative_to(B))]=sha(out);spans.append({'name':name,'line':n.lineno,'end_line':n.end_lineno,'path':str(out.relative_to(B)),'sha256':sha(out)})
 pins[rel]=sha(p);records.append({'label':label,'path':rel,'sha256':sha(p),'spans':spans})
p=B/'research/gram_internal_jumps/sources/src__lin_assembly.py';s=p.read_text();t=ast.parse(s);cl=[n for n in ast.walk(t) if isinstance(n,ast.ClassDef) and n.name=='ExpPolyBasis'];need(len(cl)==1,'class');need(ast.get_source_segment(s,cl[0])+'\n'==(D/'sources/ExpPolyBasis.txt').read_text(),'complete class span');pins[str(p.relative_to(B))]=sha(p)
p=B/'research/gram_internal_jumps/sources/src__c2_fminus.py';s=p.read_text();t=ast.parse(s);calls=[n for n in ast.walk(t) if isinstance(n,ast.Call) and dump(n.func)==dump(ast.parse('np.savez',mode='eval').body)];need(len(calls)==1,'unique raw export');kw={x.arg:x.value for x in calls[0].keywords}
for key,exp in [('col_m','np.array([m for (m,b,lab) in cols])'),('Mh','Mh'),('tmin','T.tmin'),('t0','T.t0')]:need(dump(kw[key])==dump(ast.parse(exp,mode='eval').body),'source export '+key)
out=D/'sources/raw_npz_export.txt'
with out.open('x') as f:f.write(ast.get_source_segment(s,calls[0])+'\n')
pins[str(out.relative_to(B))]=sha(out);pins[str(p.relative_to(B))]=sha(p)
for p in [D/'evidence/output_audit.json',D/'evidence/source_binding.json',D/'sources/ExpPolyBasis.txt',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final source digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STATIC_EXTERNAL_CONSTRAINT_AND_COORDINATE_SOURCE_BINDING','records':records,'assignment_checks':18,'complete_constraint_functions':2,'complete_jet_functions':2,'Fminus_coordinate_selections':2,'raw_export_field_checks':4,'files':dict(sorted(pins.items())),'scope':'Exact unscaled matrix on stored column modes and joins has rank4M. Static source binding only: NJ=1, Mh and col_m and joins must match stored columns, and finite Gdiag is required for finite positive column scaling. No runtime raw-array execution attestation or SVD certificate. Selected rows cannot be omitted by np.any under these conditions because their selected entries are nonzero. The +2 coordinates in this SOURCE matrix have zero constraint columns; their actual physical traces are not revalidated here.'}
with (D/'evidence/source_audit_v2.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','assignment_checks','complete_constraint_functions','complete_jet_functions','Fminus_coordinate_selections','raw_export_field_checks']}))
